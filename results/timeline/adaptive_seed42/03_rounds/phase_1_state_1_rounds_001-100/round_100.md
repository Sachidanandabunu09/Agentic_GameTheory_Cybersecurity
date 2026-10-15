# Round 100 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.042 | 0.600 |
| Phishing | 0.417 | 0.150 |
| BruteForce | 0.042 | 0.200 |
| Malware | 0.500 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #31, game value -7.237, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.000 |
| IDS | 0.000 |
| MFA | 0.262 |
| Isolation | 0.738 |

## 5. Agent's decision
- Sampled from the mix: **Isolation** (probability 0.738).

## 6. Attacker's action
- Attack chosen: **DDoS** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.40
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 1.50 = loss 7.50  (defender utility -7.50)

## 8. Running totals
- Cumulative utility -458.90, damage 350.0, defense cost 108.90, successful attacks 42 of 100 (42.0%)
