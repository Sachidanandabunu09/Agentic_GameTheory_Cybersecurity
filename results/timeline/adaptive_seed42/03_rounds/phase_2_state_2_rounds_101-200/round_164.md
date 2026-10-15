# Round 164 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.333 | 0.100 |
| BruteForce | 0.042 | 0.650 |
| Malware | 0.417 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #43, game value -5.623, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.118 |
| Isolation | 0.882 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.118).

## 6. Attacker's action
- Attack chosen: **BruteForce** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.06
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -732.50, damage 542.0, defense cost 190.50, successful attacks 65 of 164 (39.6%)
