import numpy as np, yaml
from environment.cyber_environment import CyberEnvironment

CFG = yaml.safe_load(open("config.yaml"))


def run(env, policy, n=None):
    obs = env.reset(CFG["seed"]); rows = []
    for _ in range(n or env.n_rounds):
        r = env.step(policy(obs)); rows.append(r); obs = r["observation"]
        if r["done"]: break
    return rows


def test_step_keys_and_done():
    env = CyberEnvironment(CFG)
    rows = run(env, lambda o: 0)
    assert len(rows) == CFG["n_rounds"] and rows[-1]["done"]
    for k in ["attack", "defense", "attack_success", "damage", "defense_cost", "utility", "observation", "done"]:
        assert k in rows[0]


def test_reproducible_with_seed():
    a = [r["attack_idx"] for r in run(CyberEnvironment(CFG), lambda o: 1)]
    b = [r["attack_idx"] for r in run(CyberEnvironment(CFG), lambda o: 1)]
    assert a == b


def test_threat_switches():
    env = CyberEnvironment(CFG)
    rows = run(env, lambda o: 0)
    se = CFG["environment"]["switch_every"]
    assert rows[0]["threat_index"] == 0 and rows[se]["threat_index"] == 1


def test_simulator_matches_payoff_matrix():
    """Core consistency: mean simulated utility == U[i,j] (shared parameters)."""
    from environment.defense_simulator import resolve
    env = CyberEnvironment(CFG); rng = np.random.default_rng(0)
    for i, j in [(0, 0), (2, 2), (3, 1)]:
        u = np.mean([resolve(i, j, env.p_succ, env.damage, env.cost, rng)["utility"] for _ in range(40000)])
        assert abs(u - env.U.values[i, j]) < 0.08


def test_adaptive_attacker_beats_fixed_defense():
    cfg = dict(CFG); cfg["n_rounds"] = 600
    fixed = np.mean([r["utility"] for r in run(CyberEnvironment(cfg, attacker="adaptive"), lambda o: 0)])
    stoch = np.mean([r["utility"] for r in run(CyberEnvironment(cfg, attacker="stochastic"), lambda o: 0)])
    assert fixed <= stoch + 0.05
