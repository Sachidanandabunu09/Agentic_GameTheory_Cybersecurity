"""Sensitivity analysis: how robust are the equilibrium conclusions to the ASSUMED payoff parameters?

(1) Joint random perturbation: every parameter (damage, base_success, cost, effectiveness) is multiplied by an
    independent factor ~ U[1-level, 1+level]; the game is re-solved for both threat states.
(2) Per-group perturbation: only ONE parameter group is perturbed at a time -> which assumption matters most.

Usage (project root):   python -m experiments.sensitivity
"""
import os, sys
import numpy as np
import pandas as pd
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from game_theory.payoff import load_params
from game_theory.game_engine import solve_game

GROUPS = ["damage", "base_success", "cost", "effectiveness"]


def payoff_from(damage, base, cost, eff):
    p_succ = base[:, None] * (1 - eff)
    return -(p_succ * damage[:, None]) - cost[None, :]


def perturb(params, rng, level, groups):
    d, b, c, e = (params[k].copy() for k in GROUPS)
    f = lambda x: x * rng.uniform(1 - level, 1 + level, size=x.shape)
    if "damage" in groups: d = f(d)
    if "base_success" in groups: b = np.clip(f(b), 0, 1)
    if "cost" in groups: c = f(c)
    if "effectiveness" in groups: e = np.clip(f(e), 0, 1)
    return d, b, c, e


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def solve_states(U, states, cfg):
    return [solve_game(U, s, cfg["game"]["weighting"], cfg["game"]["tolerance"]) for s in states]


def run(cfg=None, level=None, n_samples=None, verbose=True):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(root)
    cfg = cfg or yaml.safe_load(open("config.yaml"))
    sc = cfg.get("sensitivity", {})
    level = sc.get("level", 0.20) if level is None else level
    n_samples = sc.get("n_samples", 500) if n_samples is None else n_samples
    rng = np.random.default_rng(cfg["seed"])

    atk, dfn, eff = load_params(cfg["paths"]["data"])
    params = {"damage": atk["damage"].values.astype(float), "base_success": atk["base_success"].values.astype(float),
              "cost": dfn["cost"].values.astype(float), "effectiveness": eff.values.astype(float)}
    defs = list(dfn.index)
    states = [np.array(list(cfg["threat_states"][s].values())) for s in ("state_1", "state_2")]
    base = solve_states(payoff_from(*[params[k] for k in GROUPS]), states, cfg)

    def one_sample(groups):
        U = payoff_from(*perturb(params, rng, level, groups))
        res = solve_states(U, states, cfg)
        row = {}
        for k, (r, b) in enumerate(zip(res, base), start=1):
            row[f"tv_s{k}"] = tv(r["defense_probs"], b["defense_probs"])
            row[f"top_same_s{k}"] = int(np.argmax(r["defense_probs"]) == np.argmax(b["defense_probs"]))
            row[f"value_change_s{k}"] = abs(r["value"] - b["value"]) / abs(b["value"])
            row[f"pure_s{k}"] = int(r["is_pure"])
            row[f"top_s{k}"] = defs[int(np.argmax(r["defense_probs"]))]
        row["state_gap"] = tv(res[0]["defense_probs"], res[1]["defense_probs"])
        row["adapts"] = int(row["state_gap"] > 0.5 and row["top_s1"] != row["top_s2"])
        row["verified"] = int(all(r["verified"] for r in res))
        return row

    joint = pd.DataFrame([one_sample(GROUPS) for _ in range(n_samples)])
    per_group = []
    for g in GROUPS:
        d = pd.DataFrame([one_sample([g]) for _ in range(max(100, n_samples // 2))])
        per_group.append({"group": g, "mean_tv_s1": d.tv_s1.mean(), "mean_tv_s2": d.tv_s2.mean(),
                          "top_same_s1": d.top_same_s1.mean(), "top_same_s2": d.top_same_s2.mean(),
                          "adapts": d.adapts.mean()})
    per_group = pd.DataFrame(per_group)

    summary = pd.DataFrame([{
        "level": level, "n_samples": n_samples,
        "baseline_top_s1": defs[int(np.argmax(base[0]['defense_probs']))],
        "baseline_top_s2": defs[int(np.argmax(base[1]['defense_probs']))],
        "top_defense_unchanged_s1": joint.top_same_s1.mean(), "top_defense_unchanged_s2": joint.top_same_s2.mean(),
        "mean_tv_s1": joint.tv_s1.mean(), "p90_tv_s1": joint.tv_s1.quantile(0.9),
        "mean_tv_s2": joint.tv_s2.mean(), "p90_tv_s2": joint.tv_s2.quantile(0.9),
        "mean_value_change_s1": joint.value_change_s1.mean(), "mean_value_change_s2": joint.value_change_s2.mean(),
        "s1_still_pure": joint.pure_s1.mean(), "s2_still_pure": joint.pure_s2.mean(),
        "adaptation_holds": joint.adapts.mean(), "all_verified": bool(joint.verified.all()),
    }])

    tab = cfg["paths"]["tables"]; os.makedirs(tab, exist_ok=True)
    joint.to_csv(f"{tab}sensitivity_samples.csv", index=False)
    per_group.to_csv(f"{tab}sensitivity_by_group.csv", index=False)
    summary.to_csv(f"{tab}sensitivity_summary.csv", index=False)
    if verbose:
        pd.set_option("display.width", 200)
        print(f"Perturbation level: +-{level:.0%}, {n_samples} joint samples\n")
        print(summary.T.to_string(header=False)); print("\nPer parameter group (one group perturbed at a time):")
        print(per_group.round(3).to_string(index=False))
    return summary, per_group, joint


if __name__ == "__main__":
    run()
