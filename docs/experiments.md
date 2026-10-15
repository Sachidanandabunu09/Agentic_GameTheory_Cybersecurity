# Experiments

## How to run

```bash
python main.py                     # sanity demo of the game core (no CSVs)
python -m experiments.run_all      # full sweep  -> results/raw + results/tables
python -m experiments.sensitivity  # +/-20% sensitivity -> results/tables
python -m visualization.make_all   # all figures -> results/figures
pytest -q                          # 25-test suite
```

Order matters only for outputs: `run_all` must precede `make_all`; `sensitivity` is
optional but its figure is skipped if its tables are absent.

## Design

`experiments/runner.py` runs episodes and computes per-run metrics; three experiment
modules supply policies; `run_all.py` orchestrates and writes artefacts.

- **Sweep:** 2 attackers × 10 policies × `n_runs = 50` seeds × `n_rounds = 200` rounds.
- **Paired design:** every policy is run on the *same* seeds, enabling same-seed paired
  t-tests (removes environment variance from the comparison).

### Policies evaluated
`Fixed-{Firewall,IDS,MFA,Isolation}`, `Random`, `BestResponse(oracle)`,
`Minimax(static)`, and the agent variants `AgenticNash(sample)`, `AgenticNash(argmax)`,
`Nash(true threat)`.

### Metrics (`runner.episode_metrics`)
| Metric | Definition |
|---|---|
| `avg_utility` | mean per-round defender utility (higher is better) |
| `asr` | attack-success rate |
| `avg_damage` | mean damage per round (lower is better) |
| `total/avg_defense_cost` | sum / mean control cost |
| `adaptation` | total-variation between the defence-frequency vectors used in each threat state (0 = never adapts, 1 = completely different) |
| `n_solves` | re-solves performed by the agent |

## Outputs

- `results/raw/static_results.csv`, `dynamic_results.csv`, `agentic_results.csv` —
  per-run rows.
- `results/raw/agent_trace.csv` — one logged agent episode (estimated threat, equilibrium
  mix in use, chosen defence, re-solve flag per round) for the "strategy over time" figure.
- `results/tables/experiment_summary.csv` — mean ± std ± 95% CI per (attacker, policy).
- `results/tables/paired_vs_agent.csv` — paired agent-minus-baseline utility, t-test
  p-value, and `agent_better` flag.
- `results/tables/nash_results.csv` — equilibrium per threat state.
- `results/tables/sensitivity_*.csv` — sensitivity samples, per-group, and summary.

## Results (n = 50 seeds, 200 rounds)

**Stochastic attacker — average defender utility (higher is better)**

| Policy | Utility | ASR | Damage | Avg cost | Adaptation |
|---|---|---|---|---|---|
| BestResponse(oracle) | −2.89 | 0.328 | 2.34 | 0.55 | 1.00 |
| Nash(true threat) | −2.93 | 0.333 | 2.38 | 0.55 | 0.96 |
| AgenticNash(argmax) | −3.05 | 0.347 | 2.49 | 0.56 | 0.81 |
| **AgenticNash(sample)** | **−3.19** | 0.363 | 2.61 | 0.58 | 0.69 |
| Fixed-MFA | −3.31 | 0.406 | 2.71 | 0.60 | 0.00 |
| Fixed-Firewall | −3.75 | 0.436 | 3.25 | 0.50 | 0.00 |
| Random | −3.82 | 0.420 | 2.97 | 0.85 | 0.09 |
| Minimax(static) | −3.84 | 0.379 | 2.65 | 1.19 | 0.06 |
| Fixed-Isolation | −4.06 | 0.362 | 2.56 | 1.50 | 0.00 |
| Fixed-IDS | −4.09 | 0.466 | 3.29 | 0.80 | 0.00 |

**Adaptive attacker — average defender utility**

| Policy | Utility | ASR | Damage | Avg cost | Adaptation |
|---|---|---|---|---|---|
| **AgenticNash(sample)** | **−4.03** | 0.354 | 2.85 | 1.18 | 0.12 |
| Minimax(static) | −4.04 | 0.371 | 2.85 | 1.19 | 0.06 |
| AgenticNash(argmax) | −4.04 | 0.356 | 2.87 | 1.18 | 0.12 |
| Fixed-IDS | −4.19 | 0.482 | 3.39 | 0.80 | 0.00 |
| Fixed-Isolation | −4.39 | 0.412 | 2.89 | 1.50 | 0.00 |
| Random | −4.64 | 0.392 | 3.78 | 0.85 | 0.09 |
| Fixed-Firewall | −5.21 | 0.482 | 4.71 | 0.50 | 0.00 |
| Nash(true threat) | −5.78 | 0.533 | 5.23 | 0.55 | 0.96 |
| BestResponse(oracle) | −5.80 | 0.535 | 5.25 | 0.55 | 1.00 |
| Fixed-MFA | −6.56 | 0.610 | 5.96 | 0.60 | 0.00 |

## Findings

1. **Adaptive attacker flips the ranking.** The oracle and true-threat Nash become the
   *worst* policies under the adaptive attacker because their predictable, aggressive
   responses are learned and exploited (−5.80). The **sampled** agentic defender is best
   (−4.03): unpredictability is the defence against a learning adversary.
2. **Fixed policies cannot adapt** (adaptation exactly 0.0), while the agent adapts
   (0.69 stochastic / 0.12 adaptive).
3. **Cost-aware**: the agent avoids both the expensive always-on Isolation control and the
   damage-heavy Firewall-only choice.
4. **Estimation is cheap**: `Nash(true threat)` beats the agent only under the stochastic
   attacker (−2.93 vs −3.19) — the small price of giving up oracle threat knowledge.
5. **Paired tests** (agent − baseline): significantly positive versus all fixed/random/
   minimax baselines; against the adaptive attacker it **beats the oracle by +1.78** and
   true-threat Nash by +1.76 (p < 1e-39), and ties Minimax(static) and `AgenticNash(argmax)`.

## Sensitivity (±20%, 500 perturbed games)

| Metric | State 1 | State 2 |
|---|---|---|
| Top defence unchanged | 100% | 100% |
| Still pure equilibrium | 98.2% | 35.6% |
| Mean TV shift of mix | 0.0004 | 0.071 |
| Mean relative value change | 0.158 | 0.174 |

Adaptation holds in **100%** of perturbed games and **all** equilibria verify. Most
influential parameter group: **effectiveness** (mean TV 0.060), then base_success (0.033),
damage (0.029), cost (0.011). Conclusion: the qualitative recommendations are robust.

## Figures (`results/figures/`)

`payoff_heatmap.png`, `nash_strategy.png`, `strategy_over_time.png`,
`damage_comparison.png`, `utility_comparison.png`, `sensitivity.png`.
