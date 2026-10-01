"""Runs all experiments over n_runs seeds and writes results/raw and results/tables.

Usage (from project root):   python -m experiments.run_all
"""
import os, sys
import numpy as np
import pandas as pd
import yaml
from scipy import stats

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from game_theory.payoff import build_payoff
from game_theory.game_engine import solve_game
from environment.cyber_environment import CyberEnvironment
from agents.defender_agent import DefenderAgent
from experiments import experiment_static, experiment_dynamic, experiment_agentic
from experiments.runner import run_episode

ATTACKERS = ["stochastic", "adaptive"]
AGENT_MAIN = "AgenticNash(sample)"


def ci95(x):
    x = np.asarray(x, float)
    return float(stats.t.ppf(0.975, len(x) - 1) * x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else float("nan")


def summarize(df):
    g = df.groupby(["attacker", "policy"], sort=False)
    rows = []
    for (att, pol), d in g:
        rows.append({
            "attacker": att, "policy": pol, "n_runs": len(d),
            "utility_mean": d.avg_utility.mean(), "utility_std": d.avg_utility.std(ddof=1), "utility_ci95": ci95(d.avg_utility),
            "asr_mean": d.asr.mean(), "asr_std": d.asr.std(ddof=1),
            "damage_mean": d.avg_damage.mean(), "damage_std": d.avg_damage.std(ddof=1),
            "total_cost_mean": d.total_defense_cost.mean(), "avg_cost_mean": d.avg_defense_cost.mean(),
            "adaptation_mean": d.adaptation.mean(), "n_solves_mean": d.n_solves.mean(),
        })
    return pd.DataFrame(rows)


def paired_vs_agent(df, main=AGENT_MAIN):
    """Paired (same-seed) utility difference: agent minus each other policy. Positive = agent better."""
    rows = []
    for att in df.attacker.unique():
        base = df[(df.attacker == att) & (df.policy == main)].sort_values("seed").avg_utility.values
        for pol in df[df.attacker == att].policy.unique():
            if pol == main:
                continue
            other = df[(df.attacker == att) & (df.policy == pol)].sort_values("seed").avg_utility.values
            d = base - other
            t, p = stats.ttest_1samp(d, 0.0) if len(d) > 1 else (np.nan, np.nan)
            rows.append({"attacker": att, "baseline": pol, "mean_diff": d.mean(), "ci95": ci95(d),
                         "p_value": p, "agent_better": bool(d.mean() > 0 and p < 0.05)})
    return pd.DataFrame(rows)


def nash_table(cfg, U):
    atk, dfn = list(U.index), list(U.columns)
    states = dict(cfg["threat_states"]); states["uniform"] = {a: 0.25 for a in atk}
    rows = []
    for name, probs in states.items():
        r = solve_game(U, np.array(list(probs.values())), cfg["game"]["weighting"], cfg["game"]["tolerance"])
        row = {"threat_state": name, "value": r["value"], "is_pure": r["is_pure"],
               "maximin": r["maximin"], "minimax": r["minimax"], "verified": r["verified"]}
        row.update({f"def_{d}": p for d, p in zip(dfn, r["defense_probs"])})
        row.update({f"atk_{a}": p for a, p in zip(atk, r["attack_probs"])})
        rows.append(row)
    return pd.DataFrame(rows)


def agent_trace(cfg, U, attacker="stochastic", seed=0):
    """One logged agent episode (for the 'strategy over time' figure)."""
    env = CyberEnvironment(cfg, attacker=attacker)
    agent = DefenderAgent(U, cfg, sample=True)
    rows = run_episode(env, agent, seed)
    out = []
    for r, lg in zip(rows, agent.memory.log_rows):
        d = {"round": lg["round"], "true_threat_index": r["threat_index"], "attack": r["attack"],
             "defense": r["defense"], "resolved": lg["resolved"], "utility": r["utility"]}
        d.update({f"est_{a}": v for a, v in zip(env.attacks, lg["est_threat"])})
        d.update({f"p_{dn}": v for dn, v in zip(env.defenses, lg["defense_probs"])})
        out.append(d)
    return pd.DataFrame(out)


def main(cfg=None, raw_dir=None, tab_dir=None, verbose=True):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(root)
    cfg = cfg or yaml.safe_load(open("config.yaml"))
    raw_dir = raw_dir or cfg["paths"]["raw"]; tab_dir = tab_dir or cfg["paths"]["tables"]
    os.makedirs(raw_dir, exist_ok=True); os.makedirs(tab_dir, exist_ok=True)
    U, _ = build_payoff(cfg["paths"]["data"])
    n = int(cfg["n_runs"])

    static, dynamic, agentic = [], [], []
    for att in ATTACKERS:
        if verbose: print(f"[{att}] running {n} seeds x {cfg['n_rounds']} rounds ...", flush=True)
        static.append(experiment_static.run(cfg, U, att, n))
        dynamic.append(experiment_dynamic.run(cfg, U, att, n))
        agentic.append(experiment_agentic.run(cfg, U, att, n))
    static, dynamic, agentic = (pd.concat(x, ignore_index=True) for x in (static, dynamic, agentic))
    static.to_csv(f"{raw_dir}static_results.csv", index=False)
    dynamic.to_csv(f"{raw_dir}dynamic_results.csv", index=False)
    agentic.to_csv(f"{raw_dir}agentic_results.csv", index=False)

    allr = pd.concat([static, dynamic, agentic], ignore_index=True)
    summary = summarize(allr); paired = paired_vs_agent(allr)
    summary.to_csv(f"{tab_dir}experiment_summary.csv", index=False)
    paired.to_csv(f"{tab_dir}paired_vs_agent.csv", index=False)
    nash_table(cfg, U).to_csv(f"{tab_dir}nash_results.csv", index=False)
    agent_trace(cfg, U).to_csv(f"{raw_dir}agent_trace.csv", index=False)

    if verbose:
        pd.set_option("display.width", 200)
        for att in ATTACKERS:
            print(f"\n=== attacker: {att} (higher utility is better) ===")
            s = summary[summary.attacker == att][["policy", "utility_mean", "utility_std", "asr_mean", "damage_mean", "avg_cost_mean", "adaptation_mean"]]
            print(s.round(3).to_string(index=False))
        print("\n=== paired difference: agent minus baseline (utility) ===")
        print(paired.round(3).to_string(index=False))
        print(f"\nWrote tables to {tab_dir} and raw results to {raw_dir}")
    return summary, paired


if __name__ == "__main__":
    main()
