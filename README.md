# Agentic Game-Theoretic Attacker–Defender Strategy Selection

A simulated cyber-security **attacker vs. defender** game in which a *lightweight agentic
defender* observes incoming attacks, estimates the hidden threat state, solves a
**Bayesian (prior-weighted) zero-sum game** on the fly, and samples its defense from the
resulting Nash equilibrium. Roughly **80% Game Theory, 20% Agentic AI**.

The project is complete end-to-end: game core → environment → agent → experiments →
figures → sensitivity analysis, with a passing test-suite. This README doubles as a
**report of exactly what has been built and what the results show**.

---

## 1. What has been done (status)

| Stage | Deliverable | Status |
|-------|-------------|--------|
| 1 | Skeleton, `config.yaml`, `data/`, payoff model | ✅ Done |
| 2 | Game core: payoff, saddle point, LP Nash solver, game engine, best responses | ✅ Done |
| 3 | Cyber environment: threat schedule, stochastic/adaptive attackers, defense simulator | ✅ Done |
| 4 | Defender agent: memory, threat estimation, re-solve logic, baselines, episode runner | ✅ Done |
| 5 | Experiments: static/dynamic/agentic sweeps, metrics, summary + paired tables | ✅ Done |
| 6 | Visualization: 5–6 publication-style figures | ✅ Done |
| 7 | Sensitivity analysis over ±20% parameter uncertainty | ✅ Done |
| – | Test suite (25 tests) | ✅ Passing |
| – | Written report & slides (`final/`) | ✅ Present |

Git history mirrors the stages: `Step 1` … `Step 7` (9 commits).

**Headline result:** the agentic sampled-Nash defender is the **best defender under the
adaptive (learning) attacker** (avg utility −4.03), and stays competitive under the
stochastic attacker while adapting its strategy far more than any fixed baseline
(adaptation score 0.69 vs. 0.0 for fixed defenses).

---

## 2. Repository layout

```
game_theory/     payoff, LP mixed-strategy solver, pure-Nash/saddle, best responses, game engine
environment/     threat schedule, attack simulators (stochastic/adaptive), defense simulator, CyberEnvironment
agents/          DefenderAgent, sliding-window AgentMemory, baseline policies
experiments/     runner (episodes+metrics), static/dynamic/agentic experiments, sensitivity, run_all
visualization/   payoff heatmap, Nash mix, strategy-over-time, damage, utility, sensitivity figures
data/            attacks, defenses, effectiveness, payoff_matrix, attack_probabilities, sim config
docs/            design notes (game_model is complete; others are stubs)
results/         raw/ (per-run CSVs)  tables/ (summaries)  figures/ (PNGs)
tests/           25 pytest tests
final/           Project_Report.docx, Project_Slides.pptx
main.py          quick end-to-end demo of the game core
config.yaml      single source of truth (seed, rounds, game, agent, threat states, paths)
```

---

## 3. Setup & how to run

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python main.py                    # quick demo: payoff matrix + equilibria per threat state
python -m experiments.run_all     # full experiment sweep -> results/raw + results/tables
python -m experiments.sensitivity # ±20% parameter sensitivity -> results/tables
python -m visualization.make_all  # all figures -> results/figures
pytest -q                         # run the test suite
```

Dependencies: `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `pyyaml`, `pytest`.

> Note: `gtenv/` is a committed virtual-env directory (Windows `Scripts/` layout) and is
> git-ignored; create your own `venv` for local runs.

---

## 4. The game model

**Convention.** `U[i,j]` = **defender utility** for attack `i` vs. defense `j`. It is a
*negative loss*. The game is zero-sum, so attacker utility = `−U`. The defender
**maximises** `U`, the attacker **minimises** it.

**Payoff derivation** (`game_theory/payoff.py`):

```
U[i,j] = −( base_success_i · (1 − effectiveness_ij) · damage_i ) − cost_j
```

Parameters live in `data/attacks.csv`, `data/defenses.csv`, `data/effectiveness.csv` and
are **shared by both the game solver and the simulator**, so a round's expected utility
equals `U[i,j]` exactly.

**Bayesian / prior-weighted game.** A threat state `p` (attack probabilities) reweights the
rows: `U'_ij = w_i · U_ij` with `w_i = n · p_i` (mean weight = 1, so payoff scale stays
comparable). The zero-sum equilibrium of `U'` is recomputed whenever `p` changes, keeping
Nash and the dynamic threat state mathematically consistent.

**The project game (4 attacks × 4 defenses):**

```
attack      Firewall   IDS    MFA   Isolation     damage  base_success
DDoS          -2.42   -4.16  -5.40   -3.90           6        0.80
Phishing      -4.91   -4.23  -2.56   -4.44           7        0.70
BruteForce    -4.34   -4.16  -1.08   -4.38           8        0.60
Malware       -5.40   -3.60  -6.90   -2.90          10        0.70
                                    defense cost:  0.5   0.8   0.6   1.5
```

**Solving.** Mixed equilibria come from two exact linear programs
(`game_theory/mixed_strategy.py`, `scipy.optimize.linprog`, HiGHS): the defender LP
`max v s.t. Σ_j q_j U[i,j] ≥ v ∀i` and the attacker LP `min w s.t. Σ_i p_i U[i,j] ≤ w ∀j`.
Strong duality gives `v = w` (game value). A separate pure-saddle check
(`pure_nash.py`) computes maximin/minimax and detects pure equilibria.
`solve_game()` returns defense mix, attack mix, value, purity, maximin/minimax, and a
`verified` flag that certifies the equilibrium.

**Equilibrium by threat state** (`results/tables/nash_results.csv`):

| Threat state | Value | Pure? | Defender mix | Attacker mix |
|---|---|---|---|---|
| `state_1` (DDoS-heavy) | −5.808 | yes | Firewall 1.00 | DDoS 1.00 |
| `state_2` (BruteForce-heavy) | −3.165 | no | MFA 0.958, Firewall 0.042 | BruteForce 0.826, DDoS 0.174 |
| `uniform` | −4.072 | no | Isolation 0.666, MFA 0.224, Firewall 0.111 | Phishing 0.528, DDoS 0.359, Malware 0.113 |

All three are `verified=True`. The strategy shift (Firewall → MFA) is the behaviour the
agent must discover and track.

---

## 5. The environment (`environment/`)

- **`state.ThreatSchedule`** — the *true* attack distribution switches on a fixed schedule
  (config: `[state_1, state_2]`, switch every 100 rounds). The agent never sees it directly.
- **`attack_simulator`** — two attacker types implementing `choose(threat, rng)` / `observe(j)`:
  - `StochasticAttacker`: samples attacks from the current threat state (non-strategic).
  - `AdaptiveAttacker`: tracks the defender's **empirical** defense frequencies
    (Laplace-smoothed) and best-responds to minimise defender utility, exploring ε=0.1 of
    the time.
- **`defense_simulator.resolve`** — samples attack success vs. `p_succ`, computes
  `utility = −(damage·success + cost)`.
- **`CyberEnvironment`** — `reset(seed) → obs`, `step(defense_index) → info`. The agent's
  observation is only `{round, last_attack, last_success}` — never the true threat.
  Fully seeded/reproducible.

---

## 6. The defender agent (`agents/`)

**`DefenderAgent`** runs the loop **OBSERVE → ESTIMATE → (re)SOLVE → SAMPLE → ACT**:

1. **Estimate** the threat from a Laplace-smoothed sliding window of the last
   `memory_window = 20` observed attacks (`AgentMemory.estimate_threat`).
2. **Re-solve** only when the estimate moves more than `resolve_threshold = 0.10`
   (total-variation distance) from the last solved state — an event-driven re-solve that
   keeps the agent cheap (`n_solves` ≈ 25 under stochastic, ≈ 52 under adaptive).
3. **Sample** the defense from the equilibrium mix (config `sample_from_mix: true`) rather
   than argmax — important for unpredictability against the adaptive attacker.
4. It never computes equilibria itself; it only calls `game_theory.game_engine.solve_game`.

**Baselines** (`agents/baselines.py`): `RandomPolicy`, `FixedPolicy` (per defense),
`OracleBestResponse` (knows the true threat — an *upper* bound), and `MinimaxPolicy`
(static robust mix ignoring the threat state). All share the same policy interface, so
they are drop-in comparable in the same harness.

**Agentic ablations** (`experiments/experiment_agentic.py`): `AgenticNash(argmax)`
(deterministic play) and `Nash(true threat)` (no estimation — isolates the value of
inference).

---

## 7. Experiments (`experiments/`)

`run_all.py` sweeps **2 attackers × 10 policies × 50 seeds × 200 rounds** and writes:

- `results/raw/{static,dynamic,agentic}_results.csv` — per-run metrics
  (`avg_utility`, `asr`, `avg_damage`, `total/avg_defense_cost`, `adaptation`, `n_solves`).
- `results/tables/experiment_summary.csv` — mean ± std ± 95% CI per (attacker, policy).
- `results/tables/paired_vs_agent.csv` — **paired same-seed** agent-minus-baseline utility
  with a t-test and `agent_better` flag.
- `results/tables/nash_results.csv` — equilibrium per threat state.
- `results/raw/agent_trace.csv` — one logged episode (estimated threat + mix + action per round).

**Adaptation score** = total-variation distance between the defense-frequency vectors used
while each threat state is active (0 = never adapts, 1 = completely different).

---

## 8. Results

### 8.1 Average defender utility per round (higher is better; 50 seeds)

**Stochastic attacker**

| Policy | Utility | ASR | Damage | Avg cost | Adaptation | Solves |
|---|---|---|---|---|---|---|
| **BestResponse (oracle)** | **−2.89** | 0.328 | 2.34 | 0.55 | 1.00 | – |
| Nash (true threat) | −2.93 | 0.333 | 2.38 | 0.55 | 0.96 | 2.0 |
| AgenticNash (argmax) | −3.05 | 0.347 | 2.49 | 0.56 | 0.81 | 24.7 |
| **AgenticNash (sample)** | **−3.19** | 0.363 | 2.61 | 0.58 | 0.69 | 24.7 |
| Fixed-MFA | −3.31 | 0.406 | 2.71 | 0.60 | 0.00 | – |
| Fixed-Firewall | −3.75 | 0.436 | 3.25 | 0.50 | 0.00 | – |
| Random | −3.82 | 0.420 | 2.97 | 0.85 | 0.09 | – |
| Minimax (static) | −3.84 | 0.379 | 2.65 | 1.19 | 0.06 | – |
| Fixed-Isolation | −4.06 | 0.362 | 2.56 | 1.50 | 0.00 | – |
| Fixed-IDS | −4.09 | 0.466 | 3.29 | 0.80 | 0.00 | – |

**Adaptive attacker**

| Policy | Utility | ASR | Damage | Avg cost | Adaptation | Solves |
|---|---|---|---|---|---|---|
| **AgenticNash (sample)** | **−4.03** | 0.354 | 2.85 | 1.18 | 0.12 | 51.5 |
| Minimax (static) | −4.04 | 0.371 | 2.85 | 1.19 | 0.06 | – |
| AgenticNash (argmax) | −4.04 | 0.356 | 2.87 | 1.18 | 0.12 | 50.5 |
| Fixed-IDS | −4.19 | 0.482 | 3.39 | 0.80 | 0.00 | – |
| Fixed-Isolation | −4.39 | 0.412 | 2.89 | 1.50 | 0.00 | – |
| Random | −4.64 | 0.392 | 3.78 | 0.85 | 0.09 | – |
| Fixed-Firewall | −5.21 | 0.482 | 4.71 | 0.50 | 0.00 | – |
| Nash (true threat) | −5.78 | 0.533 | 5.23 | 0.55 | 0.96 | 2.0 |
| BestResponse (oracle) | −5.80 | 0.535 | 5.25 | 0.55 | 1.00 | – |
| Fixed-MFA | −6.56 | 0.610 | 5.96 | 0.60 | 0.00 | – |

### 8.2 Key findings

1. **Adaptive attacker flips the ranking.** Against the *stochastic* attacker the oracle
   (knowing the true threat) wins. Against the *adaptive* attacker the oracle and
   true-threat Nash are the **worst** policies (−5.80), because their predictable,
   aggressive responses are learned and exploited. The **sampled** agentic defender wins
   (−4.03) — sampling from the equilibrium mix is what makes it hard to exploit.
2. **The agent adapts; fixed policies cannot.** Adaptation score ≈ 0.69 (stochastic) /
   ≈ 0.12 (adaptive) for the agent, vs. exactly 0.0 for every fixed defense.
3. **Cost-aware.** The agent pays a modest defense cost (≈ 0.58/round) while avoiding the
   expensive always-on Isolation baseline and the damage of Firewall-only.
4. **Estimation costs little.** `Nash(true threat)` beats the agent only under the
   stochastic attacker (−2.93 vs −3.19), i.e. a small gap for giving up the oracle threat.
5. **Argmax vs. sample.** Under the stochastic attacker argmax is slightly better; under
   the adaptive attacker they tie, but sampling is the safer, more robust choice.

### 8.3 Paired comparison (same seeds, agent − baseline)

`results/tables/paired_vs_agent.csv` (positive = agent better, t-test vs. 0):

- **Stochastic:** agent significantly beats all fixed/random/minimax policies
  (p < 1e-3). It loses to `BestResponse(oracle)` (−0.30), `Nash(true threat)` (−0.26) and
  `AgenticNash(argmax)` (−0.14) — all expected (oracle information / deterministic play).
- **Adaptive:** agent significantly beats Fixed-Firewall (+1.19), Fixed-MFA (+2.53),
  Random (+0.61), Fixed-Isolation (+0.36), Fixed-IDS (+0.16), and crucially the oracle
  (+1.78) and true-threat Nash (+1.76). It **ties** with `Minimax(static)` (+0.01, p=0.72)
  and `AgenticNash(argmax)` (+0.02, p=0.62).

### 8.4 Sensitivity analysis (`results/tables/sensitivity_*.csv`)

500 games with every parameter (damage, base_success, cost, effectiveness) perturbed by
±20%:

| Metric | State 1 | State 2 |
|---|---|---|
| Top defense unchanged | 100% | 100% |
| Still a pure equilibrium | 98.2% | 35.6% |
| Mean TV shift of the mix | 0.0004 | 0.071 |
| Mean relative value change | 0.158 | 0.174 |

**Adaptation holds in 100%** of perturbed games, and **every** perturbed equilibrium is
`verified`. Per-group: **effectiveness** is the most influential assumption (mean TV 0.060),
then base_success (0.033), damage (0.029), cost (0.011). Conclusion: the qualitative
recommendations are robust to ±20% parameter uncertainty.

---

## 9. Figures (`results/figures/`)

| File | Content |
|---|---|
| `payoff_heatmap.png` | Attack × defense payoff heatmap (defender utility) |
| `nash_strategy.png` | Equilibrium defense & attack mixes per threat state |
| `strategy_over_time.png` | Estimated threat, equilibrium mix in use (re-solve ticks), and defenses actually played |
| `damage_comparison.png` | Average damage per round by policy, both attackers |
| `utility_comparison.png` | Average defender utility by policy, both attackers |
| `sensitivity.png` | TV-distance histogram, robustness bars, per-group influence |

All figures are regenerated by `python -m visualization.make_all` and use a shared style
(`_style.py`) that colour-codes the proposed agent (red), ablations (light red), strong
baselines (gray) and simple baselines (light gray).

---

## 10. Tests (`tests/`, 25 tests)

- `test_payoff` — payoff validity, mean-1 weights, shapes.
- `test_nash` — matching-pennies and RPS known solutions, saddle detection, best
  responses, expected utility, engine on the real game.
- `test_environment` — step keys/done, seed reproducibility, threat switching, **simulator
  matches the payoff matrix**, adaptive attacker beats fixed defense.
- `test_agent` — memory windowing, valid actions/logging, adaptation Firewall→MFA,
  event-driven re-solve, argmax determinism vs. sampling, full episodes.
- `test_experiments` — a scaled-down sweep writes all CSV artefacts.
- `test_sensitivity` — runs and is self-consistent (zero perturbation ⇒ no change).
- `test_visualization` — a scaled-down run produces all figures.

---

## 11. Configuration (`config.yaml`)

Single source of truth: `seed=42`, `n_rounds=200`, `n_runs=50`; `game.weighting:
normalized_prior`, `game.tolerance=1e-9`; `agent.sample_from_mix`, `estimate_threat`,
`memory_window=20`, `resolve_threshold=0.10`; two threat states; attacker `stochastic`
(or `adaptive`), `switch_every=100`, `adaptive_epsilon=0.1`; output paths.

---

## 12. Deliverables & known gaps

**Deliverables:** `final/Project_Report.docx` and `final/Project_Slides.pptx`.

**Known gaps / limitations (state these in the write-up):**
- The game is **zero-sum** and the payoff parameters are **modelling assumptions**
  (mitigated by the sensitivity analysis).
- `docs/problem_statement.md`, `methodology.md`, `agent_architecture.md`,
  `experiments.md`, `references.md` are **stubs** (headers only); only
  `docs/game_model.md` is written.
- `step7/` and `notebooks/` are **empty** directories.
- `.gitignore` lists `gtenv/` twice (harmless duplicate).
- Generating figures requires first running `experiments.run_all` (and optionally
  `experiments.sensitivity`); `make_all` will exit with a hint if inputs are missing.

---

## 13. Team

- **Bunnu** — `game_theory/`, `experiments/`, `main.py`, `config.yaml`
- **Vishu** — `environment/`, `data/`
- **Dimpy** — `agents/`, `visualization/`, `run_all` plotting

**Frozen interfaces (Day 1):** `game_theory/game_engine.py` and
`environment/cyber_environment.py`.
