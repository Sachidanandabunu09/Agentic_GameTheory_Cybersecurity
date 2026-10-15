# Round 171 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.167 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.667 | 0.650 |
| Malware | 0.083 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #20, game value -3.466, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.067 |
| IDS | 0.000 |
| MFA | 0.933 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.933).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -556.00, damage 460.0, defense cost 96.00, successful attacks 66 of 171 (38.6%)
