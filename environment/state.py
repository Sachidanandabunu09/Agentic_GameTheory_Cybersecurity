"""Threat state: the TRUE attack distribution, switching on a fixed schedule.
The agent does NOT see this directly (it only observes attacks); the oracle baseline may."""
import numpy as np


class ThreatSchedule:
    def __init__(self, states, switch_every):
        """states: list of probability vectors (each sums to 1)."""
        self.states = [np.asarray(s, dtype=float) for s in states]
        for s in self.states:
            assert abs(s.sum() - 1) < 1e-9, "each threat state must sum to 1"
        self.switch_every = int(switch_every)

    def state_index(self, t):
        return (t // self.switch_every) % len(self.states)

    def threat_at(self, t):
        return self.states[self.state_index(t)]
