"""Expected defender utility  E = sum_i sum_j p_i q_j U_ij = p @ U @ q."""
import numpy as np


def expected_utility(U, p_attacker, q_defender):
    U = np.asarray(getattr(U, "values", U), dtype=float)
    return float(np.asarray(p_attacker) @ U @ np.asarray(q_defender))
