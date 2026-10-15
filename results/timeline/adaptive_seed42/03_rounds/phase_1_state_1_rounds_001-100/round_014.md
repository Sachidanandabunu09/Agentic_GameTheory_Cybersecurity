# Round 14 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.176 | 0.600 |
| Phishing | 0.471 | 0.150 |
| BruteForce | 0.118 | 0.200 |
| Malware | 0.235 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.110 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #7, game value -5.631, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.771 |
| Isolation | 0.229 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.229).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -51.30, damage 33.0, defense cost 18.30, successful attacks 5 of 14 (35.7%)
