# Round 12 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.067 | 0.600 |
| Phishing | 0.533 | 0.150 |
| BruteForce | 0.133 | 0.200 |
| Malware | 0.267 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.121 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #6, game value -6.381, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.771 |
| Isolation | 0.229 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.229).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 1.50 = loss 7.50  (defender utility -7.50)

## 8. Running totals
- Cumulative utility -43.20, damage 27.0, defense cost 16.20, successful attacks 4 of 12 (33.3%)
