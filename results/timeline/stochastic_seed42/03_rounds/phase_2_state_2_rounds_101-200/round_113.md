# Round 113 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.417 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.375 | 0.650 |
| Malware | 0.083 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #13, game value -5.281, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.749 |
| IDS | 0.000 |
| MFA | 0.251 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.749).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -346.50, damage 287.0, defense cost 59.50, successful attacks 43 of 113 (38.1%)
