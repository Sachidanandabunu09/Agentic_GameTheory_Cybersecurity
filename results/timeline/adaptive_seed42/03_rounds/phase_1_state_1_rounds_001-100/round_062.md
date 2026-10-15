# Round 62 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.500 | 0.600 |
| Phishing | 0.083 | 0.150 |
| BruteForce | 0.083 | 0.200 |
| Malware | 0.333 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.042, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #19, game value -5.797, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.827 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.173 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.827).

## 6. Attacker's action
- Attack chosen: **Malware** (an adaptive attacker counters the defender's habits).

## 7. Outcome
- Success probability for this pair: 0.49
- Result: **ATTACK SUCCEEDED**
- Damage 10.0 + defense cost 0.50 = loss 10.50  (defender utility -10.50)

## 8. Running totals
- Cumulative utility -287.20, damage 219.0, defense cost 68.20, successful attacks 27 of 62 (43.5%)
