# Round 14 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.353 | 0.600 |
| Phishing | 0.118 | 0.150 |
| BruteForce | 0.412 | 0.200 |
| Malware | 0.118 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.037, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #7, game value -5.005, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.692 |
| IDS | 0.000 |
| MFA | 0.308 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.308).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.60 = loss 6.60  (defender utility -6.60)

## 8. Running totals
- Cumulative utility -43.70, damage 34.0, defense cost 9.70, successful attacks 5 of 14 (35.7%)
