"""Sliding-window memory: remembers recent attacks and turns them into an estimated threat state."""
import numpy as np


class AgentMemory:
    def __init__(self, n_attacks, window=20, prior=1.0):
        self.n, self.window, self.prior = n_attacks, int(window), float(prior)
        self.reset()

    def reset(self):
        self.attacks, self.records, self.log_rows = [], [], []

    def record(self, attack_idx, defense_idx, success, utility):
        self.attacks.append(int(attack_idx))
        self.records.append({"attack": int(attack_idx), "defense": int(defense_idx),
                             "success": bool(success), "utility": float(utility)})

    def estimate_threat(self):
        """Laplace-smoothed attack frequencies over the last `window` observed attacks."""
        recent = self.attacks[-self.window:]
        counts = np.full(self.n, self.prior)
        for a in recent:
            counts[a] += 1
        return counts / counts.sum()

    def log(self, **kw):
        self.log_rows.append(kw)
