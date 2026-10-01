import copy, os, yaml
from experiments import run_all

CFG = yaml.safe_load(open("config.yaml"))


def test_small_experiment_runs_and_writes_files(tmp_path):
    cfg = copy.deepcopy(CFG); cfg["n_runs"] = 3; cfg["n_rounds"] = 40
    cfg["environment"]["switch_every"] = 20
    raw, tab = str(tmp_path / "raw") + "/", str(tmp_path / "tab") + "/"
    summary, paired = run_all.main(cfg, raw, tab, verbose=False)
    for f in ["static_results.csv", "dynamic_results.csv", "agentic_results.csv", "agent_trace.csv"]:
        assert os.path.exists(raw + f)
    for f in ["experiment_summary.csv", "paired_vs_agent.csv", "nash_results.csv"]:
        assert os.path.exists(tab + f)
    assert set(summary.attacker) == {"stochastic", "adaptive"}
    assert summary.policy.nunique() == 10
    assert summary.utility_mean.notna().all()
