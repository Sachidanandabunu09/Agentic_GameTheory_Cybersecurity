import copy, os, yaml
from experiments import run_all
from visualization import make_all

CFG = yaml.safe_load(open("config.yaml"))


def test_all_figures_generated(tmp_path):
    cfg = copy.deepcopy(CFG); cfg["n_runs"] = 3; cfg["n_rounds"] = 40; cfg["environment"]["switch_every"] = 20
    raw, tab, fig = [str(tmp_path / n) + "/" for n in ("raw", "tab", "fig")]
    run_all.main(cfg, raw, tab, verbose=False)
    make_all.main("data/", tab, raw, fig)
    for f in ["payoff_heatmap", "nash_strategy", "damage_comparison", "strategy_over_time", "utility_comparison"]:
        assert os.path.getsize(f"{fig}{f}.png") > 5000
