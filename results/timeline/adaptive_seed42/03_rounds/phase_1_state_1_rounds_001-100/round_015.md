# Round 15 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.222 | 0.600 |
| Phishing | 0.444 | 0.150 |
| BruteForce | 0.111 | 0.200 |
| Malware | 0.222 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.046, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #7, game value -5.631, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.771 |
| Isolation | 0.229 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.771).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -51.90, damage 33.0, defense cost 18.90, successful attacks 5 of 15 (33.3%)
