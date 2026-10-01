import numpy as np
from game_theory.payoff import build_payoff, validate_payoff, weighted_payoff, bayesian_weights

def test_payoff_valid():
    U, p = build_payoff("data/")
    validate_payoff(U)
    assert ((p >= 0) & (p <= 1)).all().all()

def test_weights_mean_one():
    w = bayesian_weights([0.6, 0.15, 0.2, 0.05])
    assert abs(w.mean() - 1) < 1e-9

def test_weighted_shape():
    U, _ = build_payoff("data/")
    assert weighted_payoff(U, [0.25] * 4).shape == (4, 4)
