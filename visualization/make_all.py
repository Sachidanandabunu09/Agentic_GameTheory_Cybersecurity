"""Generate all figures from the CSVs written by experiments.run_all.

Usage (project root):   python -m visualization.make_all
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from visualization import payoff_heatmap, strategy_plot, damage_plot, utility_plot


def main(data_dir="data/", tab_dir="results/tables/", raw_dir="results/raw/", fig_dir="results/figures/"):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(root)
    for f in (f"{tab_dir}experiment_summary.csv", f"{tab_dir}nash_results.csv", f"{raw_dir}agent_trace.csv"):
        if not os.path.exists(f):
            raise SystemExit(f"Missing {f}. Run first:  python -m experiments.run_all")
    os.makedirs(fig_dir, exist_ok=True)
    out = [
        payoff_heatmap.plot(data_dir, f"{fig_dir}payoff_heatmap.png"),
        strategy_plot.plot_nash(f"{tab_dir}nash_results.csv", f"{fig_dir}nash_strategy.png"),
        damage_plot.plot(f"{tab_dir}experiment_summary.csv", f"{fig_dir}damage_comparison.png"),
        strategy_plot.plot_over_time(f"{raw_dir}agent_trace.csv", f"{fig_dir}strategy_over_time.png"),
        utility_plot.plot(f"{tab_dir}experiment_summary.csv", f"{fig_dir}utility_comparison.png"),
    ]
    for p in out: print("saved", p)


if __name__ == "__main__":
    main()
