# Round 116 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.417 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.417 | 0.650 |
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
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.60 = loss 6.60  (defender utility -6.60)

## 8. Running totals
- Cumulative utility -362.10, damage 301.0, defense cost 61.10, successful attacks 45 of 116 (38.8%)
