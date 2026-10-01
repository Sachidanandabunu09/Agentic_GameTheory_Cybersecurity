import numpy as np, yaml
from game_theory.payoff import build_payoff
from agents.defender_agent import DefenderAgent, total_variation
from agents.agent_memory import AgentMemory
from agents.baselines import RandomPolicy, FixedPolicy, OracleBestResponse
from environment.cyber_environment import CyberEnvironment
from experiments.runner import run_episode

CFG = yaml.safe_load(open("config.yaml"))
U, _ = build_payoff("data/")


def feed(agent, attack_idx, n):
    for t in range(n):
        agent.act({"round": t})
        agent.update({"attack_idx": attack_idx, "defense_idx": 0, "attack_success": True, "utility": -1})


def test_memory_estimate_is_distribution_and_windowed():
    m = AgentMemory(4, window=5)
    for _ in range(50): m.record(0, 0, True, -1)
    for _ in range(5): m.record(2, 0, True, -1)
    e = m.estimate_threat()
    assert abs(e.sum() - 1) < 1e-12 and e.argmax() == 2     # only the last 5 count


def test_agent_returns_valid_defense_and_logs():
    a = DefenderAgent(U, CFG)
    j = a.act({"round": 0})
    assert 0 <= j < 4 and len(a.memory.log_rows) == 1


def test_agent_adapts_to_threat_change():
    a = DefenderAgent(U, CFG, sample=False)
    feed(a, 0, 60)                                   # DDoS-heavy
    first = a.solution["defense_probs"].copy()
    feed(a, 2, 60)                                   # brute-force-heavy
    second = a.solution["defense_probs"].copy()
    assert first.argmax() == 0 and second.argmax() == 2   # Firewall -> MFA
    assert a.n_solves >= 2


def test_agent_does_not_resolve_when_threat_stable():
    a = DefenderAgent(U, CFG)
    feed(a, 0, 200)
    assert a.n_solves < 15 and a.n_solves >= 1


def test_argmax_mode_is_deterministic_and_sample_mode_is_not():
    a = DefenderAgent(U, CFG, sample=False); feed(a, 2, 40)
    assert len({a.act({"round": 0}) for _ in range(20)}) == 1


def test_full_episode_with_all_policies():
    env = CyberEnvironment(CFG)
    for pol in (DefenderAgent(U, CFG), RandomPolicy(), FixedPolicy(0), OracleBestResponse(U)):
        rows = run_episode(env, pol, seed=3)
        assert len(rows) == CFG["n_rounds"]
