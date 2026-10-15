# Round 144 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.083 | 0.150 |
| Phishing | 0.417 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.417 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #37, game value -6.579, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.262 |
| Isolation | 0.738 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.738).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -628.90, damage 454.0, defense cost 174.90, successful attacks 54 of 144 (37.5%)
