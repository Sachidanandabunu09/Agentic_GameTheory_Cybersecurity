# Round 170 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.625 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #45, game value -7.250, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 1.000 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **BruteForce** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.36
- Result: **ATTACK SUCCEEDED**
- Damage 8.0 + defense cost 1.50 = loss 9.50  (defender utility -9.50)

## 8. Running totals
- Cumulative utility -759.50, damage 560.0, defense cost 199.50, successful attacks 67 of 170 (39.4%)
