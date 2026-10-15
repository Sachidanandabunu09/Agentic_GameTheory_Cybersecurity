# Round 117 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.458 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.375 | 0.650 |
| Malware | 0.083 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #13, game value -5.281, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.749 |
| IDS | 0.000 |
| MFA | 0.251 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.251).

## 6. Attacker's action
- Attack chosen: **Malware** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.60 = loss 10.60  (defender utility -10.60)

## 8. Running totals
- Cumulative utility -372.70, damage 311.0, defense cost 61.70, successful attacks 46 of 117 (39.3%)
