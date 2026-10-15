# Round 103 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.542 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.333 | 0.650 |
| Malware | 0.042 | 0.100 |

## 3. Does the agent re-solve the game?
- **YES.** The estimate moved by 0.125 (total variation) since the last solve, above the 0.1 threshold.

## 4. Equilibrium in use (solve #12, game value -5.568, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.950 |
| IDS | 0.000 |
| MFA | 0.050 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.950).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.32
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.50 = loss 6.50  (defender utility -6.50)

## 8. Running totals
- Cumulative utility -319.40, damage 265.0, defense cost 54.40, successful attacks 40 of 103 (38.8%)
