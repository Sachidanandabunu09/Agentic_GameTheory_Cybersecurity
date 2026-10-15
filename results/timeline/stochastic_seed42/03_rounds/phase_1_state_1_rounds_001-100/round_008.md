# Round 8 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.364 | 0.600 |
| Phishing | 0.182 | 0.150 |
| BruteForce | 0.364 | 0.200 |
| Malware | 0.091 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.082, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #5, game value -5.339, mixed)
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
- Cumulative utility -12.50, damage 6.0, defense cost 6.50, successful attacks 1 of 8 (12.5%)
