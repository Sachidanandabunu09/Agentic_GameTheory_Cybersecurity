# Round 153 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.500 | 0.650 |
| Malware | 0.167 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.000, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #17, game value -4.384, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.341 |
| IDS | 0.000 |
| MFA | 0.659 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.341).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK SUCCEEDED**
- Damage 8.0 + defense cost 0.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -514.50, damage 430.0, defense cost 84.50, successful attacks 62 of 153 (40.5%)
