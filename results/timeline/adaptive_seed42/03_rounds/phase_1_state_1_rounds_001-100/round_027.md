# Round 27 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.292 | 0.600 |
| Phishing | 0.208 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.417 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #9, game value -4.818, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.016 |
| IDS | 0.000 |
| MFA | 0.169 |
| Isolation | 0.816 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.816).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.14
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -123.70, damage 95.0, defense cost 28.70, successful attacks 12 of 27 (44.4%)
