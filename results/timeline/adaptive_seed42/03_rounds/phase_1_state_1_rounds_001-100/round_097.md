# Round 97 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.542 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.375 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #30, game value -7.430, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.668 |
| Isolation | 0.332 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.668).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.60 = loss 10.60  (defender utility -10.60)

## 8. Running totals
- Cumulative utility -440.20, damage 334.0, defense cost 106.20, successful attacks 40 of 97 (41.2%)
