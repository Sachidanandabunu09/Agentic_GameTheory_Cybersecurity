"""Baseline policies (same interface as DefenderAgent)."""
import numpy as np


class RandomPolicy:
    name = "Random"
    def __init__(self, n_def=4, seed=0):
        self.n_def = n_def; self.reset(seed)
    def reset(self, seed=None): self.rng = np.random.default_rng(seed)
    def act(self, obs, true_threat=None): return int(self.rng.integers(self.n_def))
    def update(self, info): pass


class FixedPolicy:
    def __init__(self, defense_idx, label="Fixed"):
        self.j = int(defense_idx); self.name = label
    def reset(self, seed=None): pass
    def act(self, obs, true_threat=None): return self.j
    def update(self, info): pass


class OracleBestResponse:
    """Strongest honest baseline: knows the TRUE threat state and maximises expected utility against it."""
    name = "BestResponse(oracle)"
    def __init__(self, U): self.U = np.asarray(getattr(U, "values", U), dtype=float)
    def reset(self, seed=None): pass
    def act(self, obs, true_threat=None): return int(np.argmax(np.asarray(true_threat) @ self.U))
    def update(self, info): pass
