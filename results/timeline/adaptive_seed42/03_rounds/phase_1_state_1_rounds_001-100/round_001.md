# Round 1 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- First round: nothing observed yet.

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.600 |
| Phishing | 0.250 | 0.150 |
| BruteForce | 0.250 | 0.200 |
| Malware | 0.250 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES, first solve:** no equilibrium yet.

## 4. Equilibrium in use (solve #1, game value -4.072, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.111 |
| IDS | 0.000 |
| MFA | 0.224 |
| Isolation | 0.666 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.666).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.14
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -1.50, damage 0.0, defense cost 1.50, successful attacks 0 of 1 (0.0%)
