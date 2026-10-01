"""Figure 1: attack x defense payoff heatmap (defender utility)."""
import seaborn as sns
import matplotlib.pyplot as plt
from game_theory.payoff import build_payoff
from ._style import setup


def plot(data_dir="data/", path="results/figures/payoff_heatmap.png"):
    setup()
    U, _ = build_payoff(data_dir)
    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    sns.heatmap(U, annot=True, fmt=".2f", cmap="RdYlGn", center=U.values.mean(), linewidths=0.6,
                cbar_kws={"label": "Defender utility (higher = better)"}, ax=ax)
    ax.grid(False)
    ax.set_title("Payoff matrix: attack x defense\n(defender utility = -(expected damage) - defense cost)", fontsize=11)
    ax.set_xlabel("Defense"); ax.set_ylabel("Attack")
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    return path
