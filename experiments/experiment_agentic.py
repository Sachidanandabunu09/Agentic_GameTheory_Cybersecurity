"""Proposed system: agentic Bayesian-Nash defender (+ ablations)."""
import copy
import pandas as pd
from agents.defender_agent import DefenderAgent
from environment.cyber_environment import CyberEnvironment
from .runner import evaluate


def run(cfg, U, attacker, n_runs):
    env = CyberEnvironment(cfg, attacker=attacker)
    cfg_oracle = copy.deepcopy(cfg)
    cfg_oracle["agent"]["estimate_threat"] = False       # ablation: Nash given the TRUE threat
    return pd.concat([
        evaluate(lambda: DefenderAgent(U, cfg, sample=True, name="AgenticNash(sample)"),
                 env, "AgenticNash(sample)", attacker, n_runs),
        evaluate(lambda: DefenderAgent(U, cfg, sample=False, name="AgenticNash(argmax)"),
                 env, "AgenticNash(argmax)", attacker, n_runs),
        evaluate(lambda: DefenderAgent(U, cfg_oracle, sample=True, name="Nash(true threat)"),
                 env, "Nash(true threat)", attacker, n_runs),
    ], ignore_index=True)
