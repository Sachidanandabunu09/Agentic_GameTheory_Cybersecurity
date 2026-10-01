import copy, os, yaml
from experiments import sensitivity

CFG = yaml.safe_load(open("config.yaml"))


def test_sensitivity_runs_and_is_consistent(tmp_path):
    cfg = copy.deepcopy(CFG); cfg["paths"]["tables"] = str(tmp_path) + "/"
    summary, per_group, joint = sensitivity.run(cfg, level=0.2, n_samples=30, verbose=False)
    assert len(joint) == 30 and len(per_group) == 4
    assert joint.verified.all()                              # every perturbed equilibrium verified
    assert ((joint.tv_s1 >= 0) & (joint.tv_s1 <= 1)).all()
    assert os.path.exists(str(tmp_path) + "/sensitivity_summary.csv")


def test_zero_perturbation_changes_nothing(tmp_path):
    cfg = copy.deepcopy(CFG); cfg["paths"]["tables"] = str(tmp_path) + "/"
    summary, _, joint = sensitivity.run(cfg, level=0.0, n_samples=5, verbose=False)
    assert joint.tv_s1.max() < 1e-6 and joint.tv_s2.max() < 1e-6
