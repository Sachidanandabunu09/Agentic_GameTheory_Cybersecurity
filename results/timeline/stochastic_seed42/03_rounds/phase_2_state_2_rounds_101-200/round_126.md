# Round 126 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.500 | 0.650 |
| Malware | 0.167 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #15, game value -4.019, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.104 |
| IDS | 0.000 |
| MFA | 0.717 |
| Isolation | 0.179 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.717).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.06
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -399.60, damage 333.0, defense cost 66.60, successful attacks 49 of 126 (38.9%)
