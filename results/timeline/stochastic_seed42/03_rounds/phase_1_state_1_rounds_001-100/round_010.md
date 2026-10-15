# Round 10 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.462 | 0.600 |
| Phishing | 0.154 | 0.150 |
| BruteForce | 0.308 | 0.200 |
| Malware | 0.077 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.115 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #6, game value -4.973, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.908 |
| IDS | 0.000 |
| MFA | 0.092 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.908).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -19.50, damage 12.0, defense cost 7.50, successful attacks 2 of 10 (20.0%)
