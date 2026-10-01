# Game Model (Bayesian / Prior-Weighted Zero-Sum Game)

**Players:** Defender (maximiser), Attacker (minimiser of defender utility).
**Convention:** `U[i,j]` = defender utility, <= 0. Attacker utility = -U.

## Payoff derivation
`U[i,j] = -(base_success_i * (1 - eff_ij) * damage_i) - cost_j`
Parameters live in `data/attacks.csv`, `data/defenses.csv`, `data/effectiveness.csv`
and are shared by the game engine and the simulator.

## Bayesian weighting (threat state -> game)
`U'_ij = w_i * U_ij`, `w_i = n * p_i` (n = 4, so mean weight = 1).
The threat state p changes the game itself, and the zero-sum equilibrium of U'
is recomputed (via LP) whenever p changes. This keeps Nash and the dynamic
threat state mathematically consistent.

## Limitations (state in report)
Zero-sum assumption; parameters are modelling assumptions; sensitivity analysis planned.
