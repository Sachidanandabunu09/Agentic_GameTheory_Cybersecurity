# Round 5 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.125 | 0.600 |
| Phishing | 0.250 | 0.150 |
| BruteForce | 0.125 | 0.200 |
| Malware | 0.500 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #3, game value -5.800, pure)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 1.000 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 1.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -21.50, damage 14.0, defense cost 7.50, successful attacks 2 of 5 (40.0%)
