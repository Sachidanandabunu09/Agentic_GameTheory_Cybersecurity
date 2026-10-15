# Simulation timeline add-on

Shows, step by step, exactly what happens in one simulation run.

## Run it (from the project root, venv active)
```bash
python -m simulation_timeline.run_timeline                  # both attackers
python -m simulation_timeline.run_timeline --attacker adaptive --seed 7 --rounds 60
```
Output goes to `results/timeline/<attacker>_seed<seed>/`. Pre-generated runs for seed 42 are included.

## Where to look
1. `timeline.png`: the whole run in one picture.
2. `timeline.md`: one row per round, with the threat switch and adaptation events.
3. `03_rounds/phase_*/round_NNN.md`: one file per round (observe, estimate, re-solve?, decide, attacker acts, outcome, totals).
4. `02_game_solutions/`: every equilibrium the agent computed, as JSON.
5. `04_events/events.md` and `05_summary/summary.md`: events and totals.

## What each round file shows (the agent's loop)
1. What the agent observes (the previous attack).
2. Its estimate of the threat next to the true (hidden) threat.
3. Whether it re-solves the game (shift vs. the 0.10 threshold).
4. The equilibrium mix in use.
5. The defense it samples.
6. The attacker's action.
7. The outcome (success, damage, cost, utility).
8. Running totals.
