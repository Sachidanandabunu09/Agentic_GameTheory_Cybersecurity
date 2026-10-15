# Round 188 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.150 |
| Phishing | 0.042 | 0.100 |
| BruteForce | 0.583 | 0.650 |
| Malware | 0.125 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.000, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #21, game value -4.589, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.272 |
| IDS | 0.000 |
| MFA | 0.728 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.272).

## 6. Attacker's action
- Attack chosen: **Phishing** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 0.50 = loss 7.50  (defender utility -7.50)

## 8. Running totals
- Cumulative utility -607.00, damage 501.0, defense cost 106.00, successful attacks 71 of 188 (37.8%)
