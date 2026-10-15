# Round 176 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.125 | 0.650 |
| Malware | 0.792 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #46, game value -8.217, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 1.000 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.14
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 1.50 = loss 11.50  (defender utility -11.50)

## 8. Running totals
- Cumulative utility -788.50, damage 580.0, defense cost 208.50, successful attacks 69 of 176 (39.2%)
