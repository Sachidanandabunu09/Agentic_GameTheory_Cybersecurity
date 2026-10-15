# Round 44 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.542 | 0.600 |
| Phishing | 0.250 | 0.150 |
| BruteForce | 0.167 | 0.200 |
| Malware | 0.042 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #9, game value -4.890, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.992 |
| IDS | 0.000 |
| MFA | 0.008 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.992).

## 6. Attacker's action
- Attack chosen: **Phishing** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 0.50 = loss 7.50  (defender utility -7.50)

## 8. Running totals
- Cumulative utility -164.90, damage 140.0, defense cost 24.90, successful attacks 21 of 44 (47.7%)
