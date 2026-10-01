"""PUBLIC INTERFACE (frozen on Day 1).

solve_game(U, threat_state, mode="normalized_prior", tol=1e-7) -> dict
    defense_probs : np.ndarray (n_defenses,)  defender equilibrium mix
    attack_probs  : np.ndarray (n_attacks,)   attacker equilibrium mix
    value         : float                      value of the Bayesian-weighted game (defender utility)
    is_pure       : bool                       True if a pure saddle point exists
    saddle        : (i, j, value) or None
    maximin, minimax : floats (equal iff saddle point exists)
    verified      : bool                       equilibrium check passed
    weighted_U    : np.ndarray                 the game that was actually solved (U')
"""
import numpy as np
from .payoff import weighted_payoff
from .pure_nash import find_saddle_point, maximin_minimax
from .mixed_strategy import solve_zero_sum_lp


def verify_equilibrium(Uw, q, p, value, tol=1e-7):
    """Defender mix must guarantee >= value vs EVERY pure attack;
    attacker mix must hold defender to <= value vs EVERY pure defense;
    both are valid distributions."""
    ok_q = abs(q.sum() - 1) < tol and (q >= -tol).all()
    ok_p = abs(p.sum() - 1) < tol and (p >= -tol).all()
    defender_guarantee = (Uw @ q).min()     # worst case over attacks
    attacker_bound = (p @ Uw).max()         # best case over defenses
    return bool(ok_q and ok_p
                and defender_guarantee >= value - tol
                and attacker_bound <= value + tol)


def solve_game(U, threat_state, mode="normalized_prior", tol=1e-7):
    Uw = weighted_payoff(U, threat_state, mode)          # Bayesian game  U'_ij = w_i * U_ij
    q, p, v, w = solve_zero_sum_lp(Uw)
    maximin, minimax = maximin_minimax(Uw)
    saddle = find_saddle_point(Uw)
    return {
        "defense_probs": q,
        "attack_probs": p,
        "value": v,
        "is_pure": saddle is not None,
        "saddle": saddle,
        "maximin": maximin,
        "minimax": minimax,
        "verified": verify_equilibrium(Uw, q, p, v, tol) and abs(v - w) < tol,
        "weighted_U": Uw,
    }
