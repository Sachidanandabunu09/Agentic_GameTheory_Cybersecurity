"""Figure 3: average damage per round, all defenders, both attackers (lower is better)."""
import pandas as pd
from ._style import barh_panels


def plot(summary_csv="results/tables/experiment_summary.csv", path="results/figures/damage_comparison.png"):
    s = pd.read_csv(summary_csv)
    return barh_panels(s, "damage_mean", "damage_std", "Average damage per round (lower is better)",
                       "Damage comparison", path, ci_from_std=True)
