# Round 196 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.708 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.167 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.000, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #51, game value -6.857, pure)
|  | Defender mix |
|---|---|
| Firewall | 1.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.49
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -844.50, damage 614.0, defense cost 230.50, successful attacks 74 of 196 (37.8%)
