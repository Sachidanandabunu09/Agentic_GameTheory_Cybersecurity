# Round 99 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.458 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.458 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #31, game value -7.237, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.262 |
| Isolation | 0.738 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.262).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.60 = loss 10.60  (defender utility -10.60)

## 8. Running totals
- Cumulative utility -451.40, damage 344.0, defense cost 107.40, successful attacks 41 of 99 (41.4%)
