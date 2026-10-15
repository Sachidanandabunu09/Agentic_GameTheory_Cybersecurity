# Round 22 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.542 | 0.600 |
| Phishing | 0.125 | 0.150 |
| BruteForce | 0.250 | 0.200 |
| Malware | 0.083 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.063, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #8, game value -5.015, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.932 |
| IDS | 0.000 |
| MFA | 0.068 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.932).

## 6. Attacker's action
- Attack chosen: **Phishing** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 0.50 = loss 7.50  (defender utility -7.50)

## 8. Running totals
- Cumulative utility -66.80, damage 53.0, defense cost 13.80, successful attacks 8 of 22 (36.4%)
