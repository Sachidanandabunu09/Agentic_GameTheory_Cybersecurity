# Agent Architecture

The agentic layer is deliberately thin (~20% of the project). It contributes **online
threat estimation** and **decision timing**; all game-theoretic reasoning is delegated to
the frozen `game_theory.game_engine.solve_game`.

## Control loop

```
        ┌────────────────────────────────────────────────────────────┐
        │                        DefenderAgent                        │
        │                                                             │
 obs ──▶│ 1. ESTIMATE   AgentMemory.estimate_threat()  ───────────┐   │
        │               (Laplace-smoothed, window = 20)           │   │
        │                                                         ▼   │
        │ 2. CHECK      total_variation(est, last_solved) > 0.10 ?    │
        │               yes ─▶ solve_game(U, est)  (re-solve)         │
        │               no  ─▶ reuse cached equilibrium mix           │
        │                                                             │
        │ 3. SAMPLE     j ~ defense_probs   (sample_from_mix = True)  │
        │                                                             │
        │ 4. ACT        return j                                      │
        │ 5. UPDATE     memory.record(attack, defense, success, util) │
        └────────────────────────────────────────────────────────────┘
```

## Components

### `agents/agent_memory.py` — `AgentMemory`
- Stores the sequence of observed attacks (and a record log).
- `estimate_threat()` returns Laplace-smoothed attack frequencies over the **last
  `window`** observations: `counts = prior + histogram(recent); p = counts / Σ`. The prior
  (`1.0` per attack) keeps the estimate valid early in an episode.
- The window makes the estimate **non-stationary-aware**: when the threat state switches,
  the estimate drifts to the new distribution within ~one window.

### `agents/defender_agent.py` — `DefenderAgent`
- `__init__(U, cfg, sample=None, window=None, name=None)` — reads `game.weighting`,
  `game.tolerance`, and the `agent.*` block from `config.yaml`.
- `reset(seed)` — fresh RNG, empty memory, `solution = solved_threat = None`, `n_solves = 0`.
- `act(obs, true_threat=None)`:
  - estimate = `memory.estimate_threat()` (or the true threat when the ablation disables
    estimation),
  - re-solve iff no cached solution or `total_variation(estimate, solved_threat) >
    resolve_threshold`,
  - **sample** the defence from the (renormalised) equilibrium mix, or take the argmax in
    the deterministic ablation,
  - log the round.
- `update(info)` — records the realised attack/defence/outcome/utility into memory.
- `total_variation(p, q) = ½ Σ|p − q|` is the change detector.

### Tunables (`config.yaml → agent`)
| Key | Value | Meaning |
|---|---|---|
| `sample_from_mix` | `true` | sample defence from the mix (vs. argmax) |
| `estimate_threat` | `true` | infer threat online (vs. use the true threat) |
| `memory_window` | `20` | observations in the sliding window |
| `resolve_threshold` | `0.10` | TV shift that triggers a re-solve |

## Design rationale

- **Unpredictable play.** Against an aggressive, adaptive attacker, a deterministic
  (argmax) policy is learnable and gets exploited. Sampling from the Nash mix preserves the
  security guarantee and empirically wins under the adaptive attacker.
- **Event-driven solving.** Re-solving every round is wasteful; only a meaningful change in
  the estimated threat (`TV > 0.10`) triggers a solve. Typical cost: ~25 solves (stochastic)
  to ~52 solves (adaptive) over 200 rounds, and just 2 for the clairvoyant ablation.
- **Separation of concerns.** The agent never re-implements the solver. This is enforced by
  the frozen interface and keeps the equilibrium maths independently tested.

## Baselines and ablations (`agents/baselines.py`, `experiments/experiment_agentic.py`)

| Policy | What it represents |
|---|---|
| `RandomPolicy` | uniform random defence |
| `FixedPolicy(j)` | always use one control |
| `OracleBestResponse` | knows the true threat → best response (information upper bound) |
| `MinimaxPolicy` | static robust mix ignoring the threat state |
| `AgenticNash(argmax)` | ablation: deterministic play |
| `Nash(true threat)` | ablation: no estimation (isolates the value of inference) |

All policies implement the same interface — `reset(seed)`, `act(obs, true_threat)`,
`update(info)` — so they are drop-in comparable in a single harness.

## Behavioural evidence (`tests/test_agent.py`)

- The mix's top defence moves **Firewall → MFA** when the observed threat moves from
  DDoS-heavy to BruteForce-heavy.
- The agent does **not** re-solve when the threat is stable (`n_solves` stays small).
- argmax mode is deterministic across repeated acts; sample mode is not.
