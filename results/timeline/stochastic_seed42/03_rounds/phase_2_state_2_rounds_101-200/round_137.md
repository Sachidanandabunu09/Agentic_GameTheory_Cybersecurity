# Round 137 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.458 | 0.650 |
| Malware | 0.167 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #15, game value -4.019, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.104 |
| IDS | 0.000 |
| MFA | 0.717 |
| Isolation | 0.179 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.179).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 1.50 = loss 1.50  (defender utility -1.50)

## 8. Running totals
- Cumulative utility -451.80, damage 377.0, defense cost 74.80, successful attacks 55 of 137 (40.1%)
