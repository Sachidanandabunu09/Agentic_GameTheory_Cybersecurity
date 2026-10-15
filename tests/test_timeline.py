import copy, os, yaml
from simulation_timeline.run_timeline import run

CFG = yaml.safe_load(open("config.yaml"))


def test_timeline_writes_expected_files(tmp_path):
    cfg = copy.deepcopy(CFG); cfg["environment"]["switch_every"] = 15
    out, n, solves, lags = run(cfg, "stochastic", 1, str(tmp_path), n_rounds=30)
    assert n == 30 and solves >= 1
    for f in ["README.md", "timeline.md", "timeline.png", "rounds.csv", "01_setup/setup.md", "02_game_solutions/00_reference_equilibria.md",
              "04_events/events.md", "05_summary/summary.md"]:
        assert os.path.exists(os.path.join(out, f)), f
    rounds = [f for d, _, fs in os.walk(os.path.join(out, "03_rounds")) for f in fs]
    assert len(rounds) == 30
