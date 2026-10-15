# Round 61 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.542 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.292 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #19, game value -5.797, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.827 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.173 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.827).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.49
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.50 = loss 10.50  (defender utility -10.50)

## 8. Running totals
- Cumulative utility -276.70, damage 209.0, defense cost 67.70, successful attacks 26 of 61 (42.6%)
