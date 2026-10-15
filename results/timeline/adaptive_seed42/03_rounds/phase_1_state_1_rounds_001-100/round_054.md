# Round 54 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.667 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.167 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #18, game value -6.453, pure)
|  | Defender mix |
|---|---|
| Firewall | 1.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.50 = loss 6.50  (defender utility -6.50)

## 8. Running totals
- Cumulative utility -223.20, damage 159.0, defense cost 64.20, successful attacks 21 of 54 (38.9%)
