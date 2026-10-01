"""Attackers.  Both expose:  choose(threat, rng) -> attack index ;  observe(defense_idx)."""
import numpy as np


class StochasticAttacker:
    """Non-strategic: samples an attack from the current true threat state."""
    def choose(self, threat, rng):
        return int(rng.choice(len(threat), p=threat))

    def observe(self, defense_idx):
        pass


class AdaptiveAttacker:
    """Strategic: tracks defender's empirical defense frequencies and best-responds to them
    (attacker minimises defender utility U).  Explores with probability epsilon by following the threat state."""
    def __init__(self, U, epsilon=0.1):
        self.U = np.asarray(getattr(U, "values", U), dtype=float)
        self.counts = np.ones(self.U.shape[1])          # Laplace-smoothed
        self.epsilon = epsilon

    def choose(self, threat, rng):
        if rng.random() < self.epsilon:
            return int(rng.choice(len(threat), p=threat))
        q_hat = self.counts / self.counts.sum()
        return int(np.argmin(self.U @ q_hat))

    def observe(self, defense_idx):
        self.counts[defense_idx] += 1


def make_attacker(kind, U, epsilon=0.1):
    return AdaptiveAttacker(U, epsilon) if kind == "adaptive" else StochasticAttacker()
