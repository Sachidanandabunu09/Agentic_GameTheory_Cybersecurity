# Round 123 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.333 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.375 | 0.650 |
| Malware | 0.167 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #14, game value -4.919, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.574 |
| IDS | 0.000 |
| MFA | 0.426 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.574).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -382.00, damage 317.0, defense cost 65.00, successful attacks 47 of 123 (38.2%)
