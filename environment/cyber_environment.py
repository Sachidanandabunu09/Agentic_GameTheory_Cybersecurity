"""PUBLIC INTERFACE (frozen on Day 1).

CyberEnvironment.reset(seed) -> observation
CyberEnvironment.step(defense_index) -> dict:
    attack, attack_idx, defense, defense_idx, attack_success, damage,
    defense_cost, utility, observation, done, threat_index, true_threat

observation (what the AGENT sees; never the true threat):
    {"round": t, "last_attack": idx or None, "last_success": bool or None}
"""
import numpy as np
from game_theory.payoff import load_params, build_payoff
from .state import ThreatSchedule
from .attack_simulator import make_attacker
from .defense_simulator import resolve


class CyberEnvironment:
    def __init__(self, cfg, data_dir="data/", attacker=None):
        atk, dfn, _ = load_params(data_dir)
        self.attacks, self.defenses = list(atk.index), list(dfn.index)
        self.damage = atk["damage"].values.astype(float)
        self.cost = dfn["cost"].values.astype(float)
        self.U, p = build_payoff(data_dir)
        self.p_succ = p.values
        ec = cfg["environment"]
        states = [list(cfg["threat_states"][s].values()) for s in ec["schedule"]]
        self.schedule = ThreatSchedule(states, ec["switch_every"])
        self.n_rounds = int(cfg["n_rounds"])
        self._attacker_kind = attacker or ec["attacker"]
        self._eps = ec["adaptive_epsilon"]
        self.reset(cfg["seed"])

    def reset(self, seed=None):
        self.rng = np.random.default_rng(seed)
        self.attacker = make_attacker(self._attacker_kind, self.U, self._eps)
        self.t = 0
        return {"round": 0, "last_attack": None, "last_success": None}

    def true_threat(self):
        return self.schedule.threat_at(self.t)

    def step(self, defense_index):
        threat = self.true_threat()
        a = self.attacker.choose(threat, self.rng)
        out = resolve(a, defense_index, self.p_succ, self.damage, self.cost, self.rng)
        self.attacker.observe(defense_index)
        info = {"attack": self.attacks[a], "attack_idx": a,
                "defense": self.defenses[defense_index], "defense_idx": int(defense_index),
                "threat_index": self.schedule.state_index(self.t),
                "true_threat": threat.copy(), **out}
        self.t += 1
        info["observation"] = {"round": self.t, "last_attack": a, "last_success": out["attack_success"]}
        info["done"] = self.t >= self.n_rounds
        return info
