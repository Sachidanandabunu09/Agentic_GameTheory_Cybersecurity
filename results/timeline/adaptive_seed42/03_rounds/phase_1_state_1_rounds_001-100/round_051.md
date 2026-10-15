# Round 51 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.583 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.292 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #17, game value -6.203, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.701 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.299 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.701).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.50 = loss 0.50  (defender utility -0.50)

## 8. Running totals
- Cumulative utility -201.70, damage 139.0, defense cost 62.70, successful attacks 18 of 51 (35.3%)
