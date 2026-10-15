# Round 190 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.583 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.292 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #49, game value -6.278, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.514 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.486 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.514).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.50 = loss 6.50  (defender utility -6.50)

## 8. Running totals
- Cumulative utility -831.50, damage 604.0, defense cost 227.50, successful attacks 73 of 190 (38.4%)
