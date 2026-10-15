# Round 23 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.292 | 0.600 |
| Phishing | 0.333 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.292 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.092, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #8, game value -5.318, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.325 |
| IDS | 0.000 |
| MFA | 0.675 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.675).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.60 = loss 10.60  (defender utility -10.60)

## 8. Running totals
- Cumulative utility -98.60, damage 75.0, defense cost 23.60, successful attacks 10 of 23 (43.5%)
