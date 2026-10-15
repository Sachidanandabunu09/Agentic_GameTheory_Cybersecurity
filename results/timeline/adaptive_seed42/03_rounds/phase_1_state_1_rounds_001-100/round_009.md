# Round 9 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.083 | 0.600 |
| Phishing | 0.500 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.333 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.045, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #5, game value -6.646, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.417 |
| Isolation | 0.583 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.417).

## 6. Attacker's action
- Attack chosen: **BruteForce** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.06
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -26.60, damage 14.0, defense cost 12.60, successful attacks 2 of 9 (22.2%)
