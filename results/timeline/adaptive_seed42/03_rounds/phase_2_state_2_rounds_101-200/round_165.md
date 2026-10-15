# Round 165 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.292 | 0.100 |
| BruteForce | 0.083 | 0.650 |
| Malware | 0.417 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #43, game value -5.623, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.118 |
| Isolation | 0.882 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.882).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.14
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 1.50 = loss 11.50  (defender utility -11.50)

## 8. Running totals
- Cumulative utility -744.00, damage 552.0, defense cost 192.00, successful attacks 66 of 165 (40.0%)
