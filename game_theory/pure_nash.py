"""Pure-strategy equilibrium / saddle-point check for a zero-sum game.
U[i, j] = defender utility.  Defender picks column j (maximiser), attacker picks row i (minimiser)."""
import numpy as np


def _arr(U):
    return np.asarray(getattr(U, "values", U), dtype=float)


def maximin_minimax(U):
    """Return (maximin, minimax).  Defender guarantees maximin; attacker holds defender to minimax.
    Always maximin <= minimax; a pure saddle point exists iff they are equal."""
    U = _arr(U)
    maximin = U.min(axis=0).max()     # defender: best of the worst-case per defense
    minimax = U.max(axis=1).min()     # attacker: best of the best-case per attack
    return float(maximin), float(minimax)


def find_pure_nash(U, tol=1e-9):
    """All cells (i, j) where U[i,j] is the max of row i (defender can't improve)
    and the min of column j (attacker can't improve).  Returns list of (i, j, value)."""
    U = _arr(U)
    out = []
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            if U[i, j] >= U[i].max() - tol and U[i, j] <= U[:, j].min() + tol:
                out.append((i, j, float(U[i, j])))
    return out


def find_saddle_point(U, tol=1e-9):
    """First pure Nash equilibrium (i, j, value) or None."""
    eq = find_pure_nash(U, tol)
    return eq[0] if eq else None
