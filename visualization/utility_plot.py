"""Figure 5: defender utility, all defenders, both attackers (higher is better)."""
import pandas as pd
from ._style import barh_panels


def plot(summary_csv="results/tables/experiment_summary.csv", path="results/figures/utility_comparison.png"):
    s = pd.read_csv(summary_csv)
    return barh_panels(s, "utility_mean", "utility_ci95", "Average defender utility per round (higher is better)",
                       "Defender utility comparison", path)
