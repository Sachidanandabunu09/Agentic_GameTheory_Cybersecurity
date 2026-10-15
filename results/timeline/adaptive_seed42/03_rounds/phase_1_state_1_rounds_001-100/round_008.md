# Round 8 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.091 | 0.600 |
| Phishing | 0.455 | 0.150 |
| BruteForce | 0.091 | 0.200 |
| Malware | 0.364 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.121 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #5, game value -6.646, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.417 |
| Isolation | 0.583 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.583).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -26.00, damage 14.0, defense cost 12.00, successful attacks 2 of 8 (25.0%)
