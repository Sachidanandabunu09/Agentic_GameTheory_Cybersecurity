"""Step-by-step simulation timeline.

Runs ONE simulation episode (agent vs. an attacker) and writes exactly what happened,
round by round, into numbered subfolders.

Usage (from the project root):
    python -m simulation_timeline.run_timeline                       # both attackers, seed from config.yaml
    python -m simulation_timeline.run_timeline --attacker adaptive --seed 7
    python -m simulation_timeline.run_timeline --rounds 60

Output:  results/timeline/<attacker>_seed<seed>/
    README.md                 how to read this folder
    timeline.md               one table: every round in order, with events
    timeline.png              figure of the whole run
    rounds.csv                the same data as a spreadsheet
    01_setup/                 config, parameters, payoff matrix, threat schedule
    02_game_solutions/        every equilibrium the agent computed (JSON), plus reference solutions
    03_rounds/phase_*/        round_001.md, round_002.md ... one file per round
    04_events/                events.md / events.csv (threat switches, re-solves, adaptation lag)
    05_summary/               summary.md
"""
import os, sys, json, shutil, argparse, copy
import numpy as np
import pandas as pd
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from game_theory.payoff import build_payoff, load_params
from game_theory.game_engine import solve_game
from environment.cyber_environment import CyberEnvironment
from agents.defender_agent import DefenderAgent, total_variation

ATK_COL = {"DDoS": "#E45756", "Phishing": "#72B7B2", "BruteForce": "#EECA3B", "Malware": "#9D755D"}
DEF_COL = {"Firewall": "#4C78A8", "IDS": "#F58518", "MFA": "#54A24B", "Isolation": "#B279A2"}


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def dist_table(names, *cols):
    """cols: list of (title, vector)"""
    rows = [[n] + [f"{v[i]:.3f}" for _, v in cols] for i, n in enumerate(names)]
    return md_table(["" ] + [t for t, _ in cols], rows)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)


def jsonable(x):
    if isinstance(x, dict): return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [jsonable(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, (np.floating,)): return float(x)
    if isinstance(x, (np.integer,)): return int(x)
    if isinstance(x, (np.bool_,)): return bool(x)
    return x


def solution_record(sol, est, round_no):
    return jsonable({"round": round_no, "estimated_threat": est, "defense_probs": sol["defense_probs"],
                     "attack_probs": sol["attack_probs"], "game_value": sol["value"], "pure_saddle_point": sol["is_pure"],
                     "maximin": sol["maximin"], "minimax": sol["minimax"], "verified": sol["verified"],
                     "weighted_payoff_matrix": sol["weighted_U"]})


def run(cfg, attacker, seed, out_root, n_rounds=None):
    cfg = copy.deepcopy(cfg)
    if n_rounds: cfg["n_rounds"] = int(n_rounds)
    out = os.path.join(out_root, f"{attacker}_seed{seed}")
    if os.path.exists(out): shutil.rmtree(out)
    os.makedirs(out)

    U, p_succ = build_payoff(cfg["paths"]["data"])
    env = CyberEnvironment(cfg, attacker=attacker)
    agent = DefenderAgent(U, cfg, sample=True)
    A, Dn = env.attacks, env.defenses
    atk_df, def_df, eff_df = load_params(cfg["paths"]["data"])
    n_states = len(env.schedule.states)
    state_names = cfg["environment"]["schedule"]

    # ------------------------------------------------------------- reference solutions (what a perfect-knowledge Nash would play)
    refs = [solve_game(U, st, cfg["game"]["weighting"], cfg["game"]["tolerance"]) for st in env.schedule.states]
    ref_top = [int(np.argmax(r["defense_probs"])) for r in refs]

    # ------------------------------------------------------------- run the episode, recording everything
    obs = env.reset(seed); agent.reset(seed)
    recs, solves = [], []
    cum = {"utility": 0.0, "damage": 0.0, "cost": 0.0, "success": 0}
    for t in range(cfg["n_rounds"]):
        true = env.true_threat(); tidx = env.schedule.state_index(env.t)
        est = agent.memory.estimate_threat()
        solved_before = None if agent.solution is None else agent.solved_threat.copy()
        shift = None if solved_before is None else total_variation(est, solved_before)
        n_before = agent.n_solves
        j = agent.act(obs, true_threat=true)
        lg = agent.memory.log_rows[-1]
        resolved = agent.n_solves > n_before
        if resolved:
            solves.append(solution_record(agent.solution, est, t + 1))
        info = env.step(j); agent.update(info)
        cum["utility"] += info["utility"]; cum["damage"] += info["damage"]; cum["cost"] += info["defense_cost"]; cum["success"] += int(info["attack_success"])
        recs.append({"round": t + 1, "threat_idx": tidx, "true_threat": true.copy(), "est": est.copy(), "shift": shift,
                     "resolved": resolved, "solve_no": agent.n_solves, "mix": lg["defense_probs"].copy(), "defense": j,
                     "attack": info["attack_idx"], "success": info["attack_success"], "damage": info["damage"],
                     "cost": info["defense_cost"], "utility": info["utility"], "last_attack": obs["last_attack"],
                     "last_success": obs["last_success"], "cum": dict(cum), "mix_value": agent.solution["value"],
                     "mix_pure": agent.solution["is_pure"]})
        obs = info["observation"]
    N = len(recs)

    # ------------------------------------------------------------- phases (consecutive blocks of the same true threat state)
    phases, start = [], 0
    for i in range(1, N + 1):
        if i == N or recs[i]["threat_idx"] != recs[start]["threat_idx"]:
            phases.append((len(phases) + 1, recs[start]["threat_idx"], start, i - 1)); start = i
    phase_dir = {}
    for pno, tidx, a, b in phases:
        d = f"phase_{pno}_{state_names[tidx]}_rounds_{a + 1:03d}-{b + 1:03d}"
        for r in recs[a:b + 1]: phase_dir[r["round"]] = d

    # ------------------------------------------------------------- 01_setup
    s1 = os.path.join(out, "01_setup")
    write(os.path.join(s1, "setup.md"), "\n".join([
        f"# Setup of this run", "",
        f"- Attacker type: **{attacker}**", f"- Random seed: **{seed}**", f"- Rounds: **{N}**",
        f"- Threat schedule: {', '.join(state_names)} (switch every **{cfg['environment']['switch_every']}** rounds)",
        f"- Agent: memory window **{cfg['agent']['memory_window']}** attacks, re-solve threshold **{cfg['agent']['resolve_threshold']}** (total variation), "
        f"defense **sampled** from the equilibrium mix", "",
        "## Attack parameters", md_table(["Attack", "Damage", "Base success"], [[a, f"{atk_df.loc[a, 'damage']:.1f}", f"{atk_df.loc[a, 'base_success']:.2f}"] for a in A]), "",
        "## Defense parameters", md_table(["Defense", "Cost"], [[d, f"{def_df.loc[d, 'cost']:.2f}"] for d in Dn]), "",
        "## Defense effectiveness (fraction by which success probability is reduced)",
        md_table(["Attack"] + Dn, [[a] + [f"{eff_df.loc[a, d]:.2f}" for d in Dn] for a in A]), "",
        "## Resulting payoff matrix U (defender utility = -(success x (1 - effectiveness) x damage) - cost)",
        md_table(["Attack"] + Dn, [[a] + [f"{U.loc[a, d]:.2f}" for d in Dn] for a in A]), "",
        "## True threat states (hidden from the agent)",
        md_table(["State"] + A, [[state_names[k]] + [f"{v:.2f}" for v in env.schedule.states[k]] for k in range(n_states)]), "",
        "## What the agent can and cannot see",
        "- It sees only the *last attack* and whether it succeeded.", "- It never sees the true threat distribution; it estimates it from its memory.",
        "- It never computes equilibria itself; it calls the game engine (`solve_game`).", ""]))
    shutil.copy("config.yaml", os.path.join(s1, "config.yaml"))
    for f in ("attacks.csv", "defenses.csv", "effectiveness.csv", "attack_probabilities.csv"):
        src = os.path.join(cfg["paths"]["data"], f)
        if os.path.exists(src): shutil.copy(src, os.path.join(s1, f))

    # ------------------------------------------------------------- 02_game_solutions
    s2 = os.path.join(out, "02_game_solutions")
    ref_lines = ["# Reference equilibria (what a defender who KNEW the true threat would compute)", "",
                 "These are for comparison only. The agent does not see the true threat; it computes its own equilibria from estimates (JSON files in this folder).", ""]
    for k, r in enumerate(refs):
        ref_lines += [f"## {state_names[k]}  (game value {r['value']:.3f}, {'pure saddle point' if r['is_pure'] else 'mixed equilibrium'}, verified={r['verified']})", "",
                      dist_table(Dn, ("Defender mix", r["defense_probs"])), "", dist_table(A, ("Attacker mix (worst case)", r["attack_probs"])), ""]
    write(os.path.join(s2, "00_reference_equilibria.md"), "\n".join(ref_lines))
    for n, rec in enumerate(solves, start=1):
        write(os.path.join(s2, f"solve_{n:02d}_round_{rec['round']:03d}.json"), json.dumps(rec, indent=2))

    # ------------------------------------------------------------- 03_rounds
    for r in recs:
        t, top_est = r["round"], A[int(np.argmax(r["est"]))]
        lines = [f"# Round {t} of {N}", "", f"**Phase:** true threat state = `{state_names[r['threat_idx']]}`  (hidden from the agent)", "",
                 "## 1. What the agent observes",
                 ("- First round: nothing observed yet." if r["last_attack"] is None else
                  f"- Previous round's attack: **{A[r['last_attack']]}** ({'succeeded' if r['last_success'] else 'was blocked'})."), "",
                 f"## 2. Agent estimates the threat (last {cfg['agent']['memory_window']} attacks, smoothed)",
                 dist_table(A, ("Agent estimate", r["est"]), ("True (hidden)", r["true_threat"])), "",
                 "## 3. Does the agent re-solve the game?"]
        if r["shift"] is None:
            lines.append("- **YES, first solve:** no equilibrium yet.")
        elif r["resolved"]:
            lines.append(f"- **YES.** The estimate moved by {r['shift']:.3f} (total variation) since the last solve, above the {cfg['agent']['resolve_threshold']} threshold.")
        else:
            lines.append(f"- **NO.** The estimate moved only {r['shift']:.3f}, below the {cfg['agent']['resolve_threshold']} threshold, so the cached equilibrium is reused.")
        lines += ["", f"## 4. Equilibrium in use (solve #{r['solve_no']}, game value {r['mix_value']:.3f}, {'pure' if r['mix_pure'] else 'mixed'})",
                  dist_table(Dn, ("Defender mix", r["mix"])), "",
                  "## 5. Agent's decision",
                  f"- Sampled from the mix: **{Dn[r['defense']]}** (probability {r['mix'][r['defense']]:.3f}).", "",
                  "## 6. Attacker's action",
                  f"- Attack chosen: **{A[r['attack']]}**" + (" (an adaptive attacker counters the defender's habits)." if attacker == "adaptive" else " (sampled from the true threat state)."), "",
                  "## 7. Outcome",
                  f"- Success probability for this pair: {p_succ.iloc[r['attack'], r['defense']]:.2f}",
                  f"- Result: **{'ATTACK SUCCEEDED' if r['success'] else 'ATTACK BLOCKED'}**",
                  f"- Damage {r['damage']:.1f} + defense cost {r['cost']:.2f} = loss {-r['utility']:.2f}  (defender utility {r['utility']:.2f})", "",
                  "## 8. Running totals",
                  f"- Cumulative utility {r['cum']['utility']:.2f}, damage {r['cum']['damage']:.1f}, defense cost {r['cum']['cost']:.2f}, "
                  f"successful attacks {r['cum']['success']} of {t} ({r['cum']['success'] / t:.1%})", ""]
        write(os.path.join(out, "03_rounds", phase_dir[t], f"round_{t:03d}.md"), "\n".join(lines))

    # ------------------------------------------------------------- events
    events = []
    for pno, tidx, a, b in phases:
        events.append({"round": a + 1, "type": "threat state" if a == 0 else "THREAT SWITCH",
                       "detail": f"True threat state is now `{state_names[tidx]}`: " + ", ".join(f"{A[i]} {env.schedule.states[tidx][i]:.2f}" for i in range(len(A)))})
    for r in recs:
        if r["resolved"]:
            events.append({"round": r["round"], "type": "re-solve", "detail":
                           (f"Solve #{r['solve_no']}" + ("" if r["shift"] is None else f", estimate shifted {r['shift']:.3f}") +
                            f". New mix: " + ", ".join(f"{Dn[i]} {r['mix'][i]:.2f}" for i in range(len(Dn))) + f". Game value {r['mix_value']:.2f}.")})
    lags = []
    for pno, tidx, a, b in phases:
        hit = next((r["round"] for r in recs[a:b + 1] if int(np.argmax(r["mix"])) == ref_top[tidx]), None)
        lags.append((pno, state_names[tidx], a + 1, hit, None if hit is None else hit - (a + 1), Dn[ref_top[tidx]]))
        events.append({"round": hit if hit else a + 1, "type": "adapted" if hit else "not adapted",
                       "detail": (f"Equilibrium in use first favours **{Dn[ref_top[tidx]]}** (the reference best defense for `{state_names[tidx]}`), "
                                  f"{hit - (a + 1)} rounds after the phase began." if hit else f"Never reached the reference best defense ({Dn[ref_top[tidx]]}) in this phase.")})
    events.sort(key=lambda e: (e["round"], 0 if e["type"].lower().startswith("threat") else 1))
    ev = pd.DataFrame(events)
    ev.to_csv(os.path.join(out, "04_events", "events.csv") if os.path.isdir(os.path.join(out, "04_events")) else (os.makedirs(os.path.join(out, "04_events")) or os.path.join(out, "04_events", "events.csv")), index=False)
    write(os.path.join(out, "04_events", "events.md"), "# Events in chronological order\n\n" +
          md_table(["Round", "Event", "Detail"], [[e["round"], f"**{e['type']}**", e["detail"]] for e in events]) + "\n")

    # ------------------------------------------------------------- rounds.csv + timeline.md
    rows = [{"round": r["round"], "phase": phase_dir[r["round"]].split("_rounds")[0], "true_threat_state": state_names[r["threat_idx"]],
             "agent_top_estimate": A[int(np.argmax(r["est"]))], "resolved": r["resolved"], "mix_top_defense": Dn[int(np.argmax(r["mix"]))],
             "defense": Dn[r["defense"]], "attack": A[r["attack"]], "attack_succeeded": r["success"], "damage": r["damage"],
             "defense_cost": r["cost"], "utility": r["utility"], "cum_utility": r["cum"]["utility"]} for r in recs]
    pd.DataFrame(rows).to_csv(os.path.join(out, "rounds.csv"), index=False)
    ev_by_round = {}
    for e in events: ev_by_round.setdefault(e["round"], []).append(e)
    tl = [f"# Timeline: {attacker} attacker, seed {seed}, {N} rounds", "",
          "One row per round. `RE-SOLVE` marks rounds where the agent recomputed the equilibrium; bold rows are events.", "",
          "| Round | True threat | Agent thinks top threat is | Re-solve | Defense played | Attack | Result | Utility |", "|---|---|---|---|---|---|---|---|"]
    for r in recs:
        for e in ev_by_round.get(r["round"], []):
            if e["type"] in ("THREAT SWITCH", "adapted", "not adapted"):
                tl.append(f"| **{r['round']}** | **{e['type']}** | | | | | | {e['detail'].replace('|', '/')} |")
        tl.append(f"| {r['round']} | {state_names[r['threat_idx']]} | {A[int(np.argmax(r['est']))]} | {'RE-SOLVE' if r['resolved'] else ''} | {Dn[r['defense']]} | {A[r['attack']]} | "
                  f"{'success' if r['success'] else 'blocked'} | {r['utility']:.2f} |")
    write(os.path.join(out, "timeline.md"), "\n".join(tl) + "\n")

    # ------------------------------------------------------------- summary
    summ = ["# Summary", "", f"- Rounds: {N}   |   attacker: {attacker}   |   seed: {seed}",
            f"- Attack success rate: {cum['success'] / N:.1%}", f"- Average damage per round: {cum['damage'] / N:.2f}",
            f"- Average defense cost per round: {cum['cost'] / N:.2f}", f"- Average defender utility per round: {cum['utility'] / N:.2f}",
            f"- Times the game was re-solved: {agent.n_solves} (out of {N} rounds)", "", "## Per phase"]
    prow = []
    for pno, tidx, a, b in phases:
        seg = recs[a:b + 1]; n = len(seg)
        dc = np.bincount([r["defense"] for r in seg], minlength=len(Dn)) / n; ac = np.bincount([r["attack"] for r in seg], minlength=len(A)) / n
        prow.append([pno, state_names[tidx], f"{a + 1}-{b + 1}", f"{np.mean([r['utility'] for r in seg]):.2f}", f"{np.mean([r['success'] for r in seg]):.1%}",
                     ", ".join(f"{Dn[i]} {dc[i]:.0%}" for i in range(len(Dn)) if dc[i] > 0), ", ".join(f"{A[i]} {ac[i]:.0%}" for i in range(len(A)) if ac[i] > 0)])
    summ += [md_table(["Phase", "True threat", "Rounds", "Avg utility", "Attack success", "Defenses played", "Attacks seen"], prow), "",
             "## Adaptation lag", md_table(["Phase", "Threat state", "Phase starts at round", "Mix first favours reference best defense at round", "Lag (rounds)", "Reference best defense"],
                                           [[p, s, st, h if h else "never", l if l is not None else "-", d] for p, s, st, h, l, d in lags]), "",
             "The lag is how long the agent needed, after the threat changed, before its equilibrium mix favoured the defense that a perfectly informed Nash defender would favour. "
             "It comes from the memory window: the agent must observe enough new attacks first.", ""]
    write(os.path.join(out, "05_summary", "summary.md"), "\n".join(summ))

    # ------------------------------------------------------------- figure
    x = np.arange(1, N + 1)
    fig, ax = plt.subplots(4, 1, figsize=(12, 11), sharex=True, gridspec_kw={"height_ratios": [1, 1.2, 1.2, 1]})
    def shade(a):
        for pno, tidx, s, e in phases:
            a.axvspan(s + 0.5, e + 1.5, color="#EEEEEE" if tidx % 2 == 0 else "#FFF3D6", alpha=0.7, lw=0)
            if s > 0: a.axvline(s + 0.5, color="black", ls="--", lw=1)
    a = ax[0]; shade(a)
    for r in recs:
        a.scatter(r["round"], r["attack"], s=22, color=ATK_COL[A[r["attack"]]], marker="o" if r["success"] else "x", linewidths=1.2)
    a.set_yticks(range(len(A))); a.set_yticklabels(A); a.set_title("Attacks (o = succeeded, x = blocked), shaded by true threat state")
    a = ax[1]; shade(a)
    for i, nm in enumerate(A): a.plot(x, [r["est"][i] for r in recs], color=ATK_COL[nm], label=nm, lw=1.5)
    a.set_ylabel("Estimated threat"); a.legend(ncol=4, fontsize=8, loc="upper right"); a.set_title("Agent's estimate of the threat (from observed attacks)")
    a = ax[2]; shade(a)
    a.stackplot(x, [[r["mix"][i] for r in recs] for i in range(len(Dn))], labels=Dn, colors=[DEF_COL[d] for d in Dn], alpha=0.9)
    rs = [r["round"] for r in recs if r["resolved"]]
    a.plot(rs, [1.03] * len(rs), "k|", markersize=7, clip_on=False)
    for r in recs: a.scatter(r["round"], -0.07, s=14, color=DEF_COL[Dn[r["defense"]]], clip_on=False, marker="s")
    a.set_ylim(0, 1); a.set_ylabel("Equilibrium mix"); a.legend(ncol=4, fontsize=8, loc="lower right")
    a.set_title("Equilibrium mix in use (ticks above = game re-solved; squares below = defense actually played)")
    a = ax[3]; shade(a)
    a.plot(x, [r["cum"]["utility"] for r in recs], color="#D62728", lw=2); a.set_ylabel("Cumulative utility"); a.set_xlabel("Round")
    a.set_title("Cumulative defender utility")
    fig.suptitle(f"Simulation timeline: {attacker} attacker, seed {seed}", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97]); fig.savefig(os.path.join(out, "timeline.png"), dpi=140); plt.close(fig)

    # ------------------------------------------------------------- README of the run
    write(os.path.join(out, "README.md"), f"""# How to read this folder

This is one simulation: the agent defends for {N} rounds against a **{attacker}** attacker (seed {seed}).

Start with `timeline.png`, then `timeline.md`, then open any round file.

| Where | What it shows |
|---|---|
| `timeline.png` | The whole run in one picture: attacks, the agent's threat estimate, the equilibrium mix, cumulative utility |
| `timeline.md` | One table row per round, in order, with threat switches and adaptation events |
| `rounds.csv` | The same data as a spreadsheet |
| `01_setup/` | Parameters, payoff matrix, threat schedule, config used |
| `02_game_solutions/` | Every equilibrium the agent computed (`solve_NN_round_RRR.json`) and the reference equilibria for comparison |
| `03_rounds/phase_*/` | One markdown file per round: observe, estimate, re-solve?, decide, attacker acts, outcome, running totals |
| `04_events/` | Chronological list of threat switches, re-solves and adaptation lag |
| `05_summary/summary.md` | Totals, per-phase results, adaptation lag |

Each round file follows the agent's loop: **observe, estimate, re-solve if needed, sample a defense, act**, then the attacker acts and the outcome is recorded.
""")
    return out, N, agent.n_solves, lags


def main(argv=None):
    ap = argparse.ArgumentParser(description="Step-by-step simulation timeline")
    ap.add_argument("--attacker", default="both", choices=["stochastic", "adaptive", "both"])
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--rounds", type=int, default=None)
    ap.add_argument("--out", default="results/timeline")
    a = ap.parse_args(argv)
    os.chdir(ROOT)
    cfg = yaml.safe_load(open("config.yaml"))
    seed = cfg["seed"] if a.seed is None else a.seed
    for att in (["stochastic", "adaptive"] if a.attacker == "both" else [a.attacker]):
        out, n, solves, lags = run(cfg, att, seed, a.out, a.rounds)
        print(f"[{att}] {n} rounds, {solves} re-solves -> {out}")
        for p, s, st, h, l, d in lags:
            print(f"    phase {p} ({s}): mix favours {d} at round {h} (lag {l})")


if __name__ == "__main__":
    main()
