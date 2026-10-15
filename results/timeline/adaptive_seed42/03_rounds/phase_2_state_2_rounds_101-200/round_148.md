# Round 148 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.083 | 0.150 |
| Phishing | 0.583 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.250 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #38, game value -6.713, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.714 |
| Isolation | 0.286 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.714).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.28
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -640.10, damage 461.0, defense cost 179.10, successful attacks 55 of 148 (37.2%)
