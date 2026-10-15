# Round 111 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.458 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.333 | 0.650 |
| Malware | 0.083 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #12, game value -5.568, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.950 |
| IDS | 0.000 |
| MFA | 0.050 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.950).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -345.50, damage 287.0, defense cost 58.50, successful attacks 43 of 111 (38.7%)
