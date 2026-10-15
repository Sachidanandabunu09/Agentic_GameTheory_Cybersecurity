# Game Model (Bayesian / Prior-Weighted Zero-Sum Game)

**Players:** Defender (maximiser), Attacker (minimiser of defender utility).
**Convention:** `U[i,j]` = defender utility, `<= 0`. Attacker utility `= -U`. The game is
simultaneous, discrete, and **zero-sum**.

## Payoff derivation

```
U[i,j] = -( base_success_i · (1 - eff_ij) · damage_i ) - cost_j
```

| Symbol | Meaning | Source |
|---|---|---|
| `base_success_i` | success prob. of attack `i` with no defence | `data/attacks.csv` |
| `eff_ij` | fraction of that success removed by defence `j` | `data/effectiveness.csv` |
| `damage_i` | loss if attack `i` succeeds | `data/attacks.csv` |
| `cost_j` | per-round cost of defence `j` | `data/defenses.csv` |

Term 1 is the expected damage; term 2 is the control cost. Parameters are **shared by the
game engine and the simulator**, so `E[round utility | i,j] = U[i,j]` exactly
(`environment/defense_simulator.resolve`).

## The concrete game (4 attacks × 4 defences)

Defender utility matrix `U` (higher = better for the defender):

```
attack      Firewall   IDS    MFA   Isolation
DDoS          -2.42   -4.16  -5.40   -3.90
Phishing      -4.91   -4.23  -2.56   -4.44
BruteForce    -4.34   -4.16  -1.08   -4.38
Malware       -5.40   -3.60  -6.90   -2.90
```

Attack parameters (`damage`, `base_success`): DDoS (6, 0.80), Phishing (7, 0.70),
BruteForce (8, 0.60), Malware (10, 0.70).
Defence costs: Firewall 0.5, IDS 0.8, MFA 0.6, Isolation 1.5.

## Bayesian weighting (threat state → game)

A threat state is a distribution `p` over attacks. It reweights the rows:

```
U'_ij = w_i · U_ij ,    w_i = n · p_i     (n = 4, so mean weight = 1)
```

The `n·p_i` normalisation keeps the payoff scale comparable across states. Because the
threat state changes the *game itself*, the zero-sum equilibrium of `U'` is **recomputed
whenever `p` changes** (via LP). This keeps Nash and the dynamic threat state
mathematically consistent — the agent is not merely switching between two pre-baked
answers.

Two scheduled states (`config.yaml`, `data/attack_probabilities.csv`):

```
state_1: {DDoS 0.60, Phishing 0.15, BruteForce 0.20, Malware 0.05}   (DDoS-heavy)
state_2: {DDoS 0.15, Phishing 0.10, BruteForce 0.65, Malware 0.10}   (BruteForce-heavy)
```

## Equilibrium and solution concept

The relevant solution concept is the **mixed Nash equilibrium** of the zero-sum game, which
coincides with the maximin/minimax value. It is computed exactly by two LPs
(`game_theory/mixed_strategy.py`):

```
Defender:  max v   s.t.  Σ_j q_j U'[i,j] ≥ v  ∀i ,  Σ q = 1, q ≥ 0
Attacker:  min w   s.t.  Σ_i p_i U'[i,j] ≤ w  ∀j ,  Σ p = 1, p ≥ 0
```

Strong duality ⇒ `v = w`. `game_engine.solve_game` additionally reports `maximin`,
`minimax`, whether a **pure** saddle point exists, and a `verified` flag (defender mix
guarantees ≥ value vs. every pure attack; attacker mix holds the defender to ≤ value vs.
every pure defence; both are valid distributions).

### Verified equilibria

| Threat state | Value | Pure? | Defender mix | Attacker mix |
|---|---|---|---|---|
| `state_1` | −5.808 | yes | Firewall 1.000 | DDoS 1.000 |
| `state_2` | −3.165 | no | MFA 0.958, Firewall 0.042 | BruteForce 0.826, DDoS 0.174 |
| `uniform` | −4.072 | no | Isolation 0.666, MFA 0.224, Firewall 0.111 | Phishing 0.528, DDoS 0.359, Malware 0.113 |

All instances are `verified = True`. The qualitative behaviour the agent must track is the
**Firewall → MFA** shift between states (see `agent_architecture.md`).

## Limitations (state in the report)

- **Zero-sum** assumption (real security games are often not strictly zero-sum).
- Parameter values are **modelling assumptions**; addressed by the ±20% sensitivity
  analysis (`experiments.md`).
- A single scalar threat distribution captures only aggregate attack frequency, not
  sequential or multi-stage attacker behaviour.
- The defender's utility is expressed purely in expected-damage + cost terms.
