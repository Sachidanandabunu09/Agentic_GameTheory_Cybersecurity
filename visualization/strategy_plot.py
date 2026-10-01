"""Figure 2: Nash strategy distribution per threat state.  Figure 4: strategy over time."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ._style import setup, DEF_COLORS, ATK_COLORS


def plot_nash(nash_csv="results/tables/nash_results.csv", path="results/figures/nash_strategy.png"):
    setup()
    df = pd.read_csv(nash_csv).set_index("threat_state")
    defs = [c[4:] for c in df.columns if c.startswith("def_")]
    atks = [c[4:] for c in df.columns if c.startswith("atk_")]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
    for ax, prefix, names, cols in [(axes[0], "def_", defs, DEF_COLORS), (axes[1], "atk_", atks, ATK_COLORS)]:
        w = 0.8 / len(df)
        for k, (st, row) in enumerate(df.iterrows()):
            ax.bar(np.arange(len(names)) + k * w, [row[prefix + n] for n in names], w * 0.95, label=f"{st} (value {row['value']:.2f})")
        ax.set_xticks(np.arange(len(names)) + 0.4 - w / 2); ax.set_xticklabels(names); ax.set_ylim(0, 1.05)
        ax.set_title("Defender equilibrium mix" if prefix == "def_" else "Attacker equilibrium mix (worst case)")
        ax.set_ylabel("Probability"); ax.legend(fontsize=8)
    fig.suptitle("Nash equilibrium of the Bayesian-weighted game", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.94]); fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    return path


def plot_over_time(trace_csv="results/raw/agent_trace.csv", path="results/figures/strategy_over_time.png", smooth=10):
    setup()
    t = pd.read_csv(trace_csv)
    defs = [c[2:] for c in t.columns if c.startswith("p_")]
    atks = [c[4:] for c in t.columns if c.startswith("est_")]
    fig, axes = plt.subplots(3, 1, figsize=(11, 8.5), sharex=True, gridspec_kw={"height_ratios": [1, 1, 1]})
    switches = t.index[t.true_threat_index.diff().fillna(0) != 0].tolist()

    def shade(ax):
        start = 0
        for s in switches + [len(t)]:
            ax.axvspan(start, s, color="#EEEEEE" if t.true_threat_index[start] == 0 else "#FFF3D6", alpha=0.6, lw=0)
            start = s
        for s in switches: ax.axvline(s, color="black", ls="--", lw=1)

    ax = axes[0]; shade(ax)
    for a in atks: ax.plot(t["round"], t[f"est_{a}"], label=a, color=ATK_COLORS[a], lw=1.6)
    ax.set_ylabel("Estimated\nthreat prob."); ax.legend(ncol=4, fontsize=8, loc="upper right"); ax.set_title("Agent's estimate of the threat state (from observed attacks)")
    ax = axes[1]; shade(ax)
    ax.stackplot(t["round"], [t[f"p_{d}"] for d in defs], labels=defs, colors=[DEF_COLORS[d] for d in defs], alpha=0.9)
    rs = t.index[t.resolved].tolist()
    ax.plot(rs, [1.02] * len(rs), "k|", markersize=6, clip_on=False)
    ax.set_ylim(0, 1); ax.set_ylabel("Equilibrium mix\nin use"); ax.legend(ncol=4, fontsize=8, loc="lower right")
    ax.set_title("Equilibrium defense mix the agent is using  (ticks on top = game re-solved)")
    ax = axes[2]; shade(ax)
    for d in defs:
        ax.plot(t["round"], (t.defense == d).astype(float).rolling(smooth, min_periods=1).mean(), label=d, color=DEF_COLORS[d], lw=1.6)
    ax.set_ylabel(f"Defense chosen\n(rolling {smooth} rounds)"); ax.set_xlabel("Round"); ax.legend(ncol=4, fontsize=8, loc="upper right")
    ax.set_title("Defenses actually played (sampled from the mix)")
    fig.text(0.99, 0.005, "Gray = threat state 1, yellow = threat state 2 (dashed line = switch)", ha="right", fontsize=8, color="#444")
    fig.suptitle("Strategy over time: the agent adapts when the threat state changes", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0.01, 1, 0.96]); fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    return path
