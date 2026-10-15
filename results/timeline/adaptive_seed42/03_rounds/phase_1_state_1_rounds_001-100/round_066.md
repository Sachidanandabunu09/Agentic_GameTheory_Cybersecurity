# Round 66 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.375 | 0.600 |
| Phishing | 0.042 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.500 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #20, game value -6.236, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.337 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.663 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.663).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.14
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -302.20, damage 229.0, defense cost 73.20, successful attacks 28 of 66 (42.4%)
