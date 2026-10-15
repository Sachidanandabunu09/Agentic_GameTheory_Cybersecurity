# Round 49 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.625 | 0.600 |
| Phishing | 0.208 | 0.150 |
| BruteForce | 0.125 | 0.200 |
| Malware | 0.042 | 0.050 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #10, game value -6.050, pure)
|  | Defender mix |
|---|---|
| Firewall | 1.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.50 = loss 6.50  (defender utility -6.50)

## 8. Running totals
- Cumulative utility -173.40, damage 146.0, defense cost 27.40, successful attacks 22 of 49 (44.9%)
