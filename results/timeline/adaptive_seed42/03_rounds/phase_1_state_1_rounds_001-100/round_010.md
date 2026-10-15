# Round 10 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.077 | 0.600 |
| Phishing | 0.462 | 0.150 |
| BruteForce | 0.154 | 0.200 |
| Malware | 0.308 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.070, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #5, game value -6.646, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.417 |
| Isolation | 0.583 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.583).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 1.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -35.10, damage 21.0, defense cost 14.10, successful attacks 3 of 10 (30.0%)
