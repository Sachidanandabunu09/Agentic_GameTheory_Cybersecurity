# Methodology

## Overview

The project is a controlled simulation study. We (1) define an interpretable payoff model,
(2) solve the induced zero-sum game exactly, (3) build a simulator that reproduces those
payoffs, (4) implement an agentic defender and baselines behind one interface, and
(5) evaluate them over many seeds with paired statistics and a sensitivity analysis.

Data-flow: `data/*.csv` → payoff matrix → (game solver ⇄ environment ⇄ agent) →
episodes → metrics → tables → figures.

## 1. Payoff modelling

Each attack `i` and defence `j` is scored by the **defender's** utility (a loss):

```
U[i,j] = −( base_success_i · (1 − effectiveness_ij) · damage_i ) − cost_j
```

- `base_success_i` — probability attack `i` succeeds against no control,
- `effectiveness_ij` — fraction of that success removed by defence `j`,
- `damage_i` — loss if the attack succeeds,
- `cost_j` — per-round cost of running defence `j`.

This single formula is the **shared contract** between the game and the simulator, so a
round's expected utility equals `U[i,j]` (`tests/test_environment.py::
test_simulator_matches_payoff_matrix`).

## 2. Bayesian / prior-weighted game

The threat state is a probability vector `p` over attacks. It reweights the payoff rows:

```
U'_ij = w_i · U_ij ,    w_i = n · p_i  (n = number of attacks)
```

The `n·` scaling keeps the mean weight at 1 so values stay comparable across threat states.
The equilibrium is recomputed whenever `p` changes — this is what makes the "game" dynamic
rather than a single fixed matrix.

## 3. Exact equilibrium solving

Zero-sum games are solved exactly with two linear programs (`scipy.optimize.linprog`,
HiGHS):

```
Defender:  max v   s.t.  Σ_j q_j U'[i,j] ≥ v  ∀i ,  Σ q = 1, q ≥ 0
Attacker:  min w   s.t.  Σ_i p_i U'[i,j] ≤ w  ∀j ,  Σ p = 1, p ≥ 0
```

Strong duality ⇒ `v = w` (value of the game). Purity is detected separately via
maximin/minimax. Every returned solution is **verified**: the defender mix must guarantee
≥ value against every pure attack, the attacker mix must hold the defender to ≤ value
against every pure defence, and both must be valid distributions.

## 4. Simulation design

- **Threat schedule:** the *true* attack distribution cycles `state_1 → state_2`, switching
  every `switch_every` rounds. The agent never observes it.
- **Attackers:** `stochastic` (samples from the threat state) and `adaptive` (tracks the
  defender's empirical defence frequencies and best-responds, with ε-greedy exploration).
- **Observation:** the agent only sees `{round, last_attack, last_success}`.
- **Determinism:** all randomness flows through seeded `numpy` generators, so runs are
  reproducible and policies can be compared on identical seeds (paired design).

## 5. Agentic defender

`OBSERVE → ESTIMATE → (re)SOLVE → SAMPLE → ACT`:

- *Estimate* the threat from a Laplace-smoothed sliding window of recent attacks.
- *Re-solve* only when the estimate moves more than a total-variation threshold — an
  event-driven policy that avoids re-solving every round.
- *Sample* the defence from the equilibrium mix for unpredictability.
- The agent contains **no game-theoretic logic of its own**; it only calls the frozen
  engine. This keeps the "20% agentic" layer thin and the maths auditable.

## 6. Evaluation

- **Runs:** 2 attackers × 10 policies × 50 seeds × 200 rounds.
- **Metrics:** average per-round defender utility, attack-success rate, average damage,
  defence cost, an **adaptation score** (total variation between the defence-frequency
  vectors used in each threat state), and number of re-solves.
- **Statistics:** per-policy mean ± std ± 95% CI, plus **paired same-seed** differences
  (agent − baseline) with a one-sample t-test.
- **Baselines:** Random, Fixed (each defence), Minimax(static), and
  BestResponse(oracle) as an information upper bound; ablations `AgenticNash(argmax)`
  and `Nash(true threat)`.

## 7. Sensitivity analysis

Because the payoff parameters are assumptions, we recompute the equilibrium for 500 games
in which every parameter is independently multiplied by `U[1−0.20, 1+0.20]`, and separately
perturb one parameter group at a time. We measure the TV shift of the defence mix, how
often the top defence changes, how often the game stays pure, and whether the
state-to-state adaptation still holds — all under the same verification check.

## 8. Validation

A 25-test pytest suite validates the payoff model, known textbook equilibria (matching
pennies, rock-paper-scissors), saddle detection, the simulator/payoff equivalence,
reproducibility, threat switching, the adaptation behaviour of the agent, the experiment
pipeline, and figure generation. See `experiments.md` for outputs.

## Limitations

Zero-sum assumption; parameters are modelling assumptions (addressed by sensitivity);
abstract (non-network) environment; single scalar threat distribution.
