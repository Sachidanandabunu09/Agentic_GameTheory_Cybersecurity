"""Figure 6: sensitivity of the equilibrium to +-20% parameter uncertainty."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ._style import setup


def plot(tab_dir="results/tables/", path="results/figures/sensitivity.png"):
    setup()
    joint = pd.read_csv(f"{tab_dir}sensitivity_samples.csv")
    grp = pd.read_csv(f"{tab_dir}sensitivity_by_group.csv")
    summ = pd.read_csv(f"{tab_dir}sensitivity_summary.csv").iloc[0]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

    ax = axes[0]
    bins = np.linspace(0, 1, 21)
    ax.hist(joint.tv_s1, bins, alpha=0.7, label=f"State 1 (baseline: {summ.baseline_top_s1})", color="#4C78A8")
    ax.hist(joint.tv_s2, bins, alpha=0.7, label=f"State 2 (baseline: {summ.baseline_top_s2})", color="#54A24B")
    ax.set_xlabel("Total-variation distance from baseline defender mix"); ax.set_ylabel("Number of perturbed games")
    ax.set_title("How far does the equilibrium move?"); ax.legend(fontsize=8)

    ax = axes[1]
    labels = ["State 1:\ntop defense\nunchanged", "State 2:\ntop defense\nunchanged", "Adaptation\nbetween states\nholds"]
    vals = [summ.top_defense_unchanged_s1, summ.top_defense_unchanged_s2, summ.adaptation_holds]
    b = ax.bar(labels, vals, color=["#4C78A8", "#54A24B", "#D62728"], edgecolor="black", linewidth=0.5)
    for r, v in zip(b, vals): ax.text(r.get_x() + r.get_width() / 2, v + 0.02, f"{v:.0%}", ha="center", fontweight="bold")
    ax.set_ylim(0, 1.12); ax.set_ylabel("Fraction of perturbed games"); ax.set_title("Do the conclusions survive?")

    ax = axes[2]
    x = np.arange(len(grp)); w = 0.38
    ax.bar(x - w / 2, grp.mean_tv_s1, w, label="State 1", color="#4C78A8"); ax.bar(x + w / 2, grp.mean_tv_s2, w, label="State 2", color="#54A24B")
    ax.set_xticks(x); ax.set_xticklabels(grp.group, rotation=15)
    ax.set_ylabel("Mean TV distance"); ax.set_title("Which assumption matters most?"); ax.legend(fontsize=8)

    fig.suptitle(f"Sensitivity analysis: all parameters perturbed by up to +-{summ.level:.0%} ({int(summ.n_samples)} random games)",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.93]); fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    return path
