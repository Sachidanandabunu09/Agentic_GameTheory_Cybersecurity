# Round 13 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.375 | 0.600 |
| Phishing | 0.125 | 0.150 |
| BruteForce | 0.375 | 0.200 |
| Malware | 0.125 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.115 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #7, game value -5.005, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.692 |
| IDS | 0.000 |
| MFA | 0.308 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.692).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK SUCCEEDED**
- Damage 8.0 + defense cost 0.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -37.10, damage 28.0, defense cost 9.10, successful attacks 4 of 13 (30.8%)
