# Round 11 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.071 | 0.600 |
| Phishing | 0.500 | 0.150 |
| BruteForce | 0.143 | 0.200 |
| Malware | 0.286 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.097, below the 0.1 threshold, so the cached equilibrium is reused.

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
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.28
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -35.70, damage 21.0, defense cost 14.70, successful attacks 3 of 11 (27.3%)
