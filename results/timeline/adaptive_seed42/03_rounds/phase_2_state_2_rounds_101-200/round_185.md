# Round 185 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.375 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.500 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #48, game value -5.835, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.007 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.993 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.993).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -820.00, damage 598.0, defense cost 222.00, successful attacks 72 of 185 (38.9%)
