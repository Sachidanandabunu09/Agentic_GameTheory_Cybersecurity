"""Payoff model.  CONVENTION (fixed project-wide):
  U[i, j] = DEFENDER utility (<= 0, a loss) for attack i vs defense j.
  Attacker utility = -U  (zero-sum).  Defender MAXIMISES U, attacker MINIMISES U.
  U[i,j] = -(base_success_i * (1 - effectiveness_ij) * damage_i) - cost_j
"""
import numpy as np
import pandas as pd

def load_params(data_dir="data/"):
    atk = pd.read_csv(f"{data_dir}attacks.csv").set_index("attack")
    dfn = pd.read_csv(f"{data_dir}defenses.csv").set_index("defense")
    eff = pd.read_csv(f"{data_dir}effectiveness.csv").set_index("attack")
    eff = eff.loc[atk.index, dfn.index]
    return atk, dfn, eff

def build_payoff(data_dir="data/"):
    """Return (U as DataFrame, success-probability DataFrame)."""
    atk, dfn, eff = load_params(data_dir)
    p_succ = (1 - eff).mul(atk["base_success"], axis=0)
    loss = p_succ.mul(atk["damage"], axis=0)
    U = -(loss.add(dfn["cost"], axis=1))
    return U, p_succ

def validate_payoff(U):
    assert U.shape == (4, 4), "expected 4x4 game"
    assert np.isfinite(U.values).all(), "payoff contains NaN/inf"
    assert (U.values <= 0).all(), "defender utilities must be <= 0"

def bayesian_weights(threat, mode="normalized_prior"):
    """Threat state (array of attack probs) -> row weights w_i."""
    p = np.asarray(threat, dtype=float)
    assert abs(p.sum() - 1) < 1e-9 and (p >= 0).all(), "threat must be a distribution"
    return len(p) * p if mode == "normalized_prior" else p

def weighted_payoff(U, threat, mode="normalized_prior"):
    """Bayesian game:  U'_ij = w_i * U_ij"""
    return U.values * bayesian_weights(threat, mode)[:, None]
