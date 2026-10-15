# Round 3 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.167 | 0.600 |
| Phishing | 0.167 | 0.150 |
| BruteForce | 0.500 | 0.200 |
| Malware | 0.167 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.100 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #3, game value -3.898, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.737 |
| Isolation | 0.263 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.263).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -3.60, damage 0.0, defense cost 3.60, successful attacks 0 of 3 (0.0%)
