# Round 169 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.083 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.708 | 0.650 |
| Malware | 0.125 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #19, game value -4.258, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.872 |
| Isolation | 0.128 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.872).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.60 = loss 6.60  (defender utility -6.60)

## 8. Running totals
- Cumulative utility -553.90, damage 460.0, defense cost 93.90, successful attacks 66 of 169 (39.1%)
