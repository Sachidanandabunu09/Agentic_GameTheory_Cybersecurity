# Round 79 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Phishing** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.458 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.458 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #25, game value -7.237, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.262 |
| Isolation | 0.738 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.738).

## 6. Attacker's action
- Attack chosen: **Phishing** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.42
- Result: **ATTACK SUCCEEDED**
- Damage 7.0 + defense cost 1.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -352.70, damage 260.0, defense cost 92.70, successful attacks 32 of 79 (40.5%)
