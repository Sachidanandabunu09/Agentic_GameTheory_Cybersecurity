"""Resolves one attack vs one defense using the SAME parameters as the payoff matrix,
so E[utility] of a round equals U[attack, defense] exactly."""
import numpy as np


def resolve(attack_idx, defense_idx, p_succ, damage, cost, rng):
    """p_succ: (n_attacks, n_defenses) array; damage: (n_attacks,); cost: (n_defenses,)."""
    success = bool(rng.random() < p_succ[attack_idx, defense_idx])
    dmg = float(damage[attack_idx]) if success else 0.0
    c = float(cost[defense_idx])
    return {"attack_success": success, "damage": dmg, "defense_cost": c, "utility": -(dmg + c)}
