# Round 2 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.200 | 0.600 |
| Phishing | 0.200 | 0.150 |
| BruteForce | 0.400 | 0.200 |
| Malware | 0.200 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.150 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #2, game value -4.089, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.553 |
| Isolation | 0.447 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.553).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.06
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -2.10, damage 0.0, defense cost 2.10, successful attacks 0 of 2 (0.0%)
