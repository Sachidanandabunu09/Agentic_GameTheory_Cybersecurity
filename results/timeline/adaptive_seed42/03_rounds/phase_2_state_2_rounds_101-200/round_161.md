# Round 161 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.417 | 0.100 |
| BruteForce | 0.042 | 0.650 |
| Malware | 0.333 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #42, game value -6.119, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.586 |
| Isolation | 0.414 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.586).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.60 = loss 10.60  (defender utility -10.60)

## 8. Running totals
- Cumulative utility -719.80, damage 532.0, defense cost 187.80, successful attacks 64 of 161 (39.8%)
