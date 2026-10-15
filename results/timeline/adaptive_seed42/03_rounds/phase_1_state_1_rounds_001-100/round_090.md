# Round 90 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.833 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.083 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.000, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #28, game value -8.533, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 1.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -386.00, damage 284.0, defense cost 102.00, successful attacks 35 of 90 (38.9%)
