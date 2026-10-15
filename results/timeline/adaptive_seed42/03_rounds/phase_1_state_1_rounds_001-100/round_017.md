# Round 17 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.300 | 0.600 |
| Phishing | 0.400 | 0.150 |
| BruteForce | 0.100 | 0.200 |
| Malware | 0.200 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.124 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #8, game value -5.318, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.325 |
| IDS | 0.000 |
| MFA | 0.675 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.675).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.60 = loss 6.60  (defender utility -6.60)

## 8. Running totals
- Cumulative utility -65.10, damage 45.0, defense cost 20.10, successful attacks 7 of 17 (41.2%)
