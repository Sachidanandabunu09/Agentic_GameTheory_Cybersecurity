"""Zero-sum mixed equilibrium via linear programming (exact).
U[i, j] = defender utility. Defender maximises, attacker minimises.

Defender LP:  max v   s.t.  sum_j q_j U[i,j] >= v  for every attack i;  sum q = 1;  q >= 0
Attacker LP:  min w   s.t.  sum_i p_i U[i,j] <= w  for every defense j;  sum p = 1;  p >= 0
(Strong duality => v == w == value of the game.)
"""
import numpy as np
from scipy.optimize import linprog


def solve_zero_sum_lp(U):
    U = np.asarray(getattr(U, "values", U), dtype=float)
    m, n = U.shape                      # m attacks (rows), n defenses (cols)

    # ---- defender: variables [q_1..q_n, v], minimise -v
    c = np.r_[np.zeros(n), -1.0]
    A_ub = np.c_[-U, np.ones(m)]        # v - sum_j U_ij q_j <= 0
    b_ub = np.zeros(m)
    A_eq = np.r_[np.ones(n), 0.0].reshape(1, -1)
    res_d = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                    bounds=[(0, None)] * n + [(None, None)], method="highs")
    if not res_d.success:
        raise RuntimeError(f"Defender LP failed: {res_d.message}")
    q, v = res_d.x[:n], res_d.x[n]

    # ---- attacker: variables [p_1..p_m, w], minimise w
    c = np.r_[np.zeros(m), 1.0]
    A_ub = np.c_[U.T, -np.ones(n)]      # sum_i U_ij p_i - w <= 0
    A_eq = np.r_[np.ones(m), 0.0].reshape(1, -1)
    res_a = linprog(c, A_ub=A_ub, b_ub=np.zeros(n), A_eq=A_eq, b_eq=[1.0],
                    bounds=[(0, None)] * m + [(None, None)], method="highs")
    if not res_a.success:
        raise RuntimeError(f"Attacker LP failed: {res_a.message}")
    p, w = res_a.x[:m], res_a.x[m]

    q = np.clip(q, 0, None); q /= q.sum()
    p = np.clip(p, 0, None); p /= p.sum()
    return q, p, float(v), float(w)
