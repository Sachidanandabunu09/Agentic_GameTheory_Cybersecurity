# Round 70 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.625 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #22, game value -7.250, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 1.000 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 1.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -325.20, damage 246.0, defense cost 79.20, successful attacks 30 of 70 (42.9%)
