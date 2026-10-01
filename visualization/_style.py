"""Shared plotting style / helpers."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEF_COLORS = {"Firewall": "#4C78A8", "IDS": "#F58518", "MFA": "#54A24B", "Isolation": "#B279A2"}
ATK_COLORS = {"DDoS": "#E45756", "Phishing": "#72B7B2", "BruteForce": "#EECA3B", "Malware": "#9D755D"}
ORDER = ["Random", "Fixed-Firewall", "Fixed-IDS", "Fixed-MFA", "Fixed-Isolation", "Minimax(static)",
         "BestResponse(oracle)", "Nash(true threat)", "AgenticNash(argmax)", "AgenticNash(sample)"]
MAIN = "AgenticNash(sample)"
ABLATIONS = {"Nash(true threat)", "AgenticNash(argmax)"}
TITLES = {"stochastic": "Stochastic attacker (follows threat state)", "adaptive": "Adaptive attacker (learns defender habits)"}


def setup():
    plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 200, "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
                         "grid.alpha": 0.25, "axes.axisbelow": True})


def bar_color(policy):
    if policy == MAIN: return "#D62728"
    if policy in ABLATIONS: return "#F4A6A6"
    if policy in ("BestResponse(oracle)", "Minimax(static)"): return "#7F7F7F"
    return "#BDBDBD"


def barh_panels(summary, metric, err, xlabel, title, path, ci_from_std=False, higher_better=True):
    """Two panels (one per attacker), one horizontal bar per policy, error bars = 95% CI."""
    setup()
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)
    for k, (ax, att) in enumerate(zip(axes, ["stochastic", "adaptive"])):
        d = summary[summary.attacker == att].set_index("policy").reindex([p for p in ORDER[::-1] if p in set(summary.policy)])
        if ci_from_std:
            e = 1.96 * d[err] / np.sqrt(d["n_runs"])
        else:
            e = d[err]
        y = np.arange(len(d))
        ax.barh(y, d[metric], xerr=e, color=[bar_color(p) for p in d.index], edgecolor="black", linewidth=0.5, capsize=3)
        ax.set_yticks(y); ax.set_yticklabels(d.index)
        if k == 0: ax.invert_yaxis()          # shared y-axis: invert once only (agent on top)
        lo, hi = min(0, (d[metric] - e).min()), max(0, (d[metric] + e).max())
        pad = 0.14 * (hi - lo)
        ax.set_xlim(lo - pad, hi + pad)
        ax.set_title(TITLES[att], fontsize=11); ax.set_xlabel(xlabel)
        for yi, v, ei in zip(y, d[metric], e):
            x = v + ei if v >= 0 else v - ei
            ax.text(x, yi, f" {v:.2f} " , va="center", ha="left" if v >= 0 else "right", fontsize=8, fontweight="bold")
    fig.suptitle(title, fontsize=13, fontweight="bold")
    fig.text(0.5, 0.005, "Red = proposed agent, light red = agent ablations, dark gray = strong baselines, light gray = simple baselines. "
             "Error bars: 95% CI over runs.", ha="center", fontsize=8, color="#444")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95]); fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    return path
