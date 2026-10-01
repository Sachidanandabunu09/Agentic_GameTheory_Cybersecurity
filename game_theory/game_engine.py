"""PUBLIC INTERFACE (frozen on Day 1 - agents/experiments depend on this).

solve_game(U, threat_state) -> dict:
    {
      "defense_probs":  np.ndarray (4,),   # defender equilibrium mix
      "attack_probs":   np.ndarray (4,),   # attacker equilibrium mix
      "value":          float,             # value of the (weighted) game
      "is_pure":        bool,
      "verified":       bool,              # equilibrium check passed
    }
"""
def solve_game(U, threat_state):
    raise NotImplementedError("Implemented on Days 3-5")
