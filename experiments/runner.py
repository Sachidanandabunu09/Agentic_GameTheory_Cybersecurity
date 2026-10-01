"""Run episodes and compute per-run metrics."""
import numpy as np
import pandas as pd


def run_episode(env, policy, seed):
    obs = env.reset(seed)
    policy.reset(seed)
    rows = []
    while True:
        j = policy.act(obs, true_threat=env.true_threat())
        info = env.step(j)
        policy.update(info)
        rows.append(info)
        obs = info["observation"]
        if info["done"]:
            return rows


def adaptation_score(rows, n_def):
    """Strategy adaptation: total-variation distance between the defense frequencies used
    while threat state 0 was active vs while threat state 1 was active (0 = no adaptation, 1 = completely different)."""
    freq = {}
    for k in (0, 1):
        js = [r["defense_idx"] for r in rows if r["threat_index"] == k]
        if not js:
            return float("nan")
        freq[k] = np.bincount(js, minlength=n_def) / len(js)
    return 0.5 * float(np.abs(freq[0] - freq[1]).sum())


def episode_metrics(rows, n_def):
    return {
        "avg_utility": float(np.mean([r["utility"] for r in rows])),
        "asr": float(np.mean([r["attack_success"] for r in rows])),
        "avg_damage": float(np.mean([r["damage"] for r in rows])),
        "total_defense_cost": float(np.sum([r["defense_cost"] for r in rows])),
        "avg_defense_cost": float(np.mean([r["defense_cost"] for r in rows])),
        "adaptation": adaptation_score(rows, n_def),
    }


def evaluate(make_policy, env, label, attacker, n_runs, seed0=0):
    """Same seeds across policies -> paired comparison."""
    out = []
    for s in range(seed0, seed0 + n_runs):
        pol = make_policy()
        rows = run_episode(env, pol, seed=s)
        m = episode_metrics(rows, len(env.defenses))
        m.update({"policy": label, "attacker": attacker, "seed": s,
                  "n_solves": getattr(pol, "n_solves", np.nan)})
        out.append(m)
    return pd.DataFrame(out)
