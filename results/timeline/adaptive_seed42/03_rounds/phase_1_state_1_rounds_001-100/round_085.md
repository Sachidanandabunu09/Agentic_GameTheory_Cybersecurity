# Round 85 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.708 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.208 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #27, game value -7.253, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 1.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.28
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 0.60 = loss 7.60  (defender utility -7.60)

## 8. Running totals
- Cumulative utility -373.00, damage 274.0, defense cost 99.00, successful attacks 34 of 85 (40.0%)
