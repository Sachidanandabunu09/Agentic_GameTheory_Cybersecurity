"""Best responses.  U[i, j] = DEFENDER utility (defender maximises, attacker minimises)."""
import numpy as np


def _arr(U):
    return np.asarray(getattr(U, "values", U), dtype=float)


def defender_best_response(U, attacker_mix):
    """Defense index j maximising expected defender utility vs. a known attacker mix.
    With attacker_mix = threat state this is the 'best-response-to-known-distribution' baseline."""
    U = _arr(U)
    exp = np.asarray(attacker_mix, dtype=float) @ U          # length n_defenses
    return int(np.argmax(exp)), exp


def attacker_best_response(U, defender_mix):
    """Attack index i minimising expected defender utility vs. a known defender mix."""
    U = _arr(U)
    exp = U @ np.asarray(defender_mix, dtype=float)          # length n_attacks
    return int(np.argmin(exp)), exp
