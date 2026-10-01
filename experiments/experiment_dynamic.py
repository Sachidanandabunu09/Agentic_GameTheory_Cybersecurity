"""Baselines: random defense and best-response-to-known-threat (oracle)."""
import pandas as pd
from agents.baselines import RandomPolicy, OracleBestResponse, MinimaxPolicy
from environment.cyber_environment import CyberEnvironment
from .runner import evaluate


def run(cfg, U, attacker, n_runs):
    env = CyberEnvironment(cfg, attacker=attacker)
    return pd.concat([
        evaluate(lambda: RandomPolicy(len(env.defenses)), env, "Random", attacker, n_runs),
        evaluate(lambda: OracleBestResponse(U), env, "BestResponse(oracle)", attacker, n_runs),
        evaluate(lambda: MinimaxPolicy(U), env, "Minimax(static)", attacker, n_runs),
    ], ignore_index=True)
