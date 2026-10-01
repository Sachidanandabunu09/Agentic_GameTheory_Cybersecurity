"""PUBLIC INTERFACE (frozen on Day 1).

CyberEnvironment.reset(seed) -> observation
CyberEnvironment.step(defense_index) -> dict:
    {"attack", "defense", "attack_success", "damage",
     "defense_cost", "utility", "observation", "done"}
"""
class CyberEnvironment:
    def reset(self, seed=None):
        raise NotImplementedError
    def step(self, defense_index):
        raise NotImplementedError
