# Round 69 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.750 | 0.600 |
| Phishing | 0.042 | 0.150 |
| BruteForce | 0.167 | 0.200 |
| Malware | 0.042 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #11, game value -6.453, pure)
|  | Defender mix |
|---|---|
| Firewall | 1.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 1.000).

## 6. Attacker's action
- Attack chosen: **Malware** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.49
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.50 = loss 10.50  (defender utility -10.50)

## 8. Running totals
- Cumulative utility -217.40, damage 180.0, defense cost 37.40, successful attacks 27 of 69 (39.1%)
