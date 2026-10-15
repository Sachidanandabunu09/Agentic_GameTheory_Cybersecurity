# Round 67 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.333 | 0.600 |
| Phishing | 0.042 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.542 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #21, game value -6.283, pure)
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
- Cumulative utility -313.70, damage 239.0, defense cost 74.70, successful attacks 29 of 67 (43.3%)
