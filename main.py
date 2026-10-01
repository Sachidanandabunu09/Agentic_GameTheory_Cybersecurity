"""Entry point:  python main.py"""
import yaml
import numpy as np
from game_theory.payoff import build_payoff, validate_payoff, weighted_payoff

def main():
    cfg = yaml.safe_load(open("config.yaml"))
    np.random.seed(cfg["seed"])
    U, p_succ = build_payoff(cfg["paths"]["data"])
    validate_payoff(U)
    U.round(3).to_csv("data/payoff_matrix.csv")
    print("=" * 46, "\n AGENTIC GAME-THEORETIC CYBER DEFENSE\n", "=" * 46, sep="")
    print("\nDefender payoff matrix U (derived from parameters):\n", U.round(2))
    for name, probs in cfg["threat_states"].items():
        t = np.array(list(probs.values()))
        print(f"\nWeighted payoff U' for {name}:\n", np.round(weighted_payoff(U, t), 2))
    print("\n[Setup OK] Game engine, environment, agent arrive in later phases.")

if __name__ == "__main__":
    main()
