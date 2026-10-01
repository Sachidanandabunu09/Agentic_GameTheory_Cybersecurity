"""Baselines: fixed defense (always the same one)."""
import pandas as pd
from agents.baselines import FixedPolicy
from environment.cyber_environment import CyberEnvironment
from .runner import evaluate


def run(cfg, U, attacker, n_runs):
    env = CyberEnvironment(cfg, attacker=attacker)
    parts = [evaluate(lambda j=j: FixedPolicy(j), env, f"Fixed-{name}", attacker, n_runs)
             for j, name in enumerate(env.defenses)]
    return pd.concat(parts, ignore_index=True)
