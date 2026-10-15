# Setup of this run

- Attacker type: **stochastic**
- Random seed: **42**
- Rounds: **200**
- Threat schedule: state_1, state_2 (switch every **100** rounds)
- Agent: memory window **20** attacks, re-solve threshold **0.1** (total variation), defense **sampled** from the equilibrium mix

## Attack parameters
| Attack | Damage | Base success |
|---|---|---|
| DDoS | 6.0 | 0.80 |
| Phishing | 7.0 | 0.70 |
| BruteForce | 8.0 | 0.60 |
| Malware | 10.0 | 0.70 |

## Defense parameters
| Defense | Cost |
|---|---|
| Firewall | 0.50 |
| IDS | 0.80 |
| MFA | 0.60 |
| Isolation | 1.50 |

## Defense effectiveness (fraction by which success probability is reduced)
| Attack | Firewall | IDS | MFA | Isolation |
|---|---|---|---|---|
| DDoS | 0.60 | 0.30 | 0.00 | 0.50 |
| Phishing | 0.10 | 0.30 | 0.60 | 0.40 |
| BruteForce | 0.20 | 0.30 | 0.90 | 0.40 |
| Malware | 0.30 | 0.60 | 0.10 | 0.80 |

## Resulting payoff matrix U (defender utility = -(success x (1 - effectiveness) x damage) - cost)
| Attack | Firewall | IDS | MFA | Isolation |
|---|---|---|---|---|
| DDoS | -2.42 | -4.16 | -5.40 | -3.90 |
| Phishing | -4.91 | -4.23 | -2.56 | -4.44 |
| BruteForce | -4.34 | -4.16 | -1.08 | -4.38 |
| Malware | -5.40 | -3.60 | -6.90 | -2.90 |

## True threat states (hidden from the agent)
| State | DDoS | Phishing | BruteForce | Malware |
|---|---|---|---|---|
| state_1 | 0.60 | 0.15 | 0.20 | 0.05 |
| state_2 | 0.15 | 0.10 | 0.65 | 0.10 |

## What the agent can and cannot see
- It sees only the *last attack* and whether it succeeded.
- It never sees the true threat distribution; it estimates it from its memory.
- It never computes equilibria itself; it calls the game engine (`solve_game`).
