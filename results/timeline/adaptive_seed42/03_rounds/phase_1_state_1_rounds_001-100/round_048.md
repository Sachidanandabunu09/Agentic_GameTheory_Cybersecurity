# Round 48 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.458 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.417 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #16, game value -6.086, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.168 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.832 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.832).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -199.20, damage 139.0, defense cost 60.20, successful attacks 18 of 48 (37.5%)
