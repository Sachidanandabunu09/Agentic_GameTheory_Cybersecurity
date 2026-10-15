# Round 18 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.333 | 0.600 |
| Phishing | 0.381 | 0.150 |
| BruteForce | 0.095 | 0.200 |
| Malware | 0.190 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.033, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #8, game value -5.318, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.325 |
| IDS | 0.000 |
| MFA | 0.675 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.325).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.49
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.50 = loss 10.50  (defender utility -10.50)

## 8. Running totals
- Cumulative utility -75.60, damage 55.0, defense cost 20.60, successful attacks 8 of 18 (44.4%)
