# Agentic Game-Theoretic Attacker-Defender Strategy Selection

Bayesian (prior-weighted) zero-sum security game + lightweight defender agent.
80% Game Theory, 20% Agentic AI.

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
pytest -q
```

## Team
- Bunnu: game_theory/, experiments/, main.py, config.yaml
- Vishu: environment/, data/
- Dimpy: agents/, visualization/, run_all plotting

## Frozen interfaces (Day 1)
See `game_theory/game_engine.py` and `environment/cyber_environment.py`.
