# How to read this folder

This is one simulation: the agent defends for 200 rounds against a **adaptive** attacker (seed 42).

Start with `timeline.png`, then `timeline.md`, then open any round file.

| Where | What it shows |
|---|---|
| `timeline.png` | The whole run in one picture: attacks, the agent's threat estimate, the equilibrium mix, cumulative utility |
| `timeline.md` | One table row per round, in order, with threat switches and adaptation events |
| `rounds.csv` | The same data as a spreadsheet |
| `01_setup/` | Parameters, payoff matrix, threat schedule, config used |
| `02_game_solutions/` | Every equilibrium the agent computed (`solve_NN_round_RRR.json`) and the reference equilibria for comparison |
| `03_rounds/phase_*/` | One markdown file per round: observe, estimate, re-solve?, decide, attacker acts, outcome, running totals |
| `04_events/` | Chronological list of threat switches, re-solves and adaptation lag |
| `05_summary/summary.md` | Totals, per-phase results, adaptation lag |

Each round file follows the agent's loop: **observe, estimate, re-solve if needed, sample a defense, act**, then the attacker acts and the outcome is recorded.
