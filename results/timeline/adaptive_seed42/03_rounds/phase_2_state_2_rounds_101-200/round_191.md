# Round 191 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.625 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.042 | 0.650 |
| Malware | 0.292 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #50, game value -6.190, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.962 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.038 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.962).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -832.00, damage 604.0, defense cost 228.00, successful attacks 73 of 191 (38.2%)
