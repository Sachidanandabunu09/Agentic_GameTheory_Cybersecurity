# Round 20 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.478 | 0.600 |
| Phishing | 0.130 | 0.150 |
| BruteForce | 0.304 | 0.200 |
| Malware | 0.087 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.109 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #8, game value -5.015, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.932 |
| IDS | 0.000 |
| MFA | 0.068 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.932).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -58.80, damage 46.0, defense cost 12.80, successful attacks 7 of 20 (35.0%)
