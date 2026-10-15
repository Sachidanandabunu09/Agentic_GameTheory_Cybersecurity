# Round 7 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.400 | 0.600 |
| Phishing | 0.100 | 0.150 |
| BruteForce | 0.400 | 0.200 |
| Malware | 0.100 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.114 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #5, game value -5.339, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.692 |
| IDS | 0.000 |
| MFA | 0.308 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.308).

## 6. Attacker's action
- Attack chosen: **Phishing** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.28
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -5.90, damage 0.0, defense cost 5.90, successful attacks 0 of 7 (0.0%)
