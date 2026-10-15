# Round 6 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.111 | 0.600 |
| Phishing | 0.333 | 0.150 |
| BruteForce | 0.111 | 0.200 |
| Malware | 0.444 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.167 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #4, game value -5.721, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.079 |
| Isolation | 0.921 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.921).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -23.00, damage 14.0, defense cost 9.00, successful attacks 2 of 6 (33.3%)
