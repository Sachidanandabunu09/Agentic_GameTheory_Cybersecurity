"""Entry point:  python main.py"""
import yaml
import numpy as np
from game_theory.payoff import build_payoff, validate_payoff
from game_theory.game_engine import solve_game
from game_theory.best_response import defender_best_response


def show(name, probs, labels):
    for l, p in zip(labels, probs):
        print(f"  {l:<12}{p:6.3f}")


def main():
    cfg = yaml.safe_load(open("config.yaml"))
    np.random.seed(cfg["seed"])
    U, _ = build_payoff(cfg["paths"]["data"])
    validate_payoff(U)
    U.round(3).to_csv("data/payoff_matrix.csv")
    atk, dfn = list(U.index), list(U.columns)

    print("=" * 46, "\n AGENTIC GAME-THEORETIC CYBER DEFENSE\n", "=" * 46, sep="")
    print("\nDefender payoff matrix U:\n", U.round(2))

    for name, probs in cfg["threat_states"].items():
        t = np.array(list(probs.values()))
        r = solve_game(U, t, cfg["game"]["weighting"], cfg["game"]["tolerance"])
        br, _ = defender_best_response(r["weighted_U"], t)
        print(f"\n--- {name} | threat {dict(zip(atk, t))}")
        print(f"Game value: {r['value']:.3f} | pure saddle: {r['is_pure']} | verified: {r['verified']}")
        print("Defender equilibrium mix:"); show(name, r["defense_probs"], dfn)
        print("Attacker equilibrium mix:"); show(name, r["attack_probs"], atk)

    print("\n[Step 2 OK] Game core working. Environment/agent come next.")


if __name__ == "__main__":
    main()
