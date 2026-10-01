"""Defender Agent:  OBSERVE -> ESTIMATE threat -> (RE)SOLVE game if threat shifted -> SAMPLE defense -> ACT.
The agent never computes equilibria itself; it only calls game_theory.game_engine.solve_game.

Policy interface (shared with baselines):
    reset(seed)
    act(obs, true_threat=None) -> defense index
    update(info)               -> called with the env.step() result
"""
import numpy as np
from game_theory.game_engine import solve_game
from .agent_memory import AgentMemory


def total_variation(p, q):
    return 0.5 * float(np.abs(np.asarray(p) - np.asarray(q)).sum())


class DefenderAgent:
    name = "AgenticNash"

    def __init__(self, U, cfg, sample=None, window=None, name=None):
        self.U = np.asarray(getattr(U, "values", U), dtype=float)
        self.n_attacks, self.n_def = self.U.shape
        a = cfg["agent"]
        self.sample = a["sample_from_mix"] if sample is None else sample
        self.estimate = a["estimate_threat"]
        self.threshold = a["resolve_threshold"]
        self.window = a["memory_window"] if window is None else window
        self.weighting = cfg["game"]["weighting"]
        self.tol = cfg["game"]["tolerance"]
        if name:
            self.name = name
        self.reset(cfg["seed"])

    def reset(self, seed=None):
        self.rng = np.random.default_rng(seed)
        self.memory = AgentMemory(self.n_attacks, self.window)
        self.solution, self.solved_threat, self.n_solves = None, None, 0

    def act(self, obs, true_threat=None):
        est = true_threat if (not self.estimate and true_threat is not None) else self.memory.estimate_threat()
        resolved = False
        if self.solution is None or total_variation(est, self.solved_threat) > self.threshold:
            self.solution = solve_game(self.U, est, self.weighting, self.tol)
            self.solved_threat, resolved = est.copy(), True
            self.n_solves += 1
        probs = np.clip(self.solution["defense_probs"], 0, None)
        probs = probs / probs.sum()
        j = int(self.rng.choice(self.n_def, p=probs)) if self.sample else int(np.argmax(probs))
        self.memory.log(round=obs["round"], est_threat=est.copy(), defense_probs=probs.copy(),
                        chosen=j, resolved=resolved)
        return j

    def update(self, info):
        self.memory.record(info["attack_idx"], info["defense_idx"], info["attack_success"], info["utility"])
