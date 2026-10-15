# Round 141 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.542 | 0.650 |
| Malware | 0.083 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #15, game value -4.019, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.104 |
| IDS | 0.000 |
| MFA | 0.717 |
| Isolation | 0.179 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.717).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK SUCCEEDED**
- Damage 6.0 + defense cost 0.60 = loss 6.60  (defender utility -6.60)

## 8. Running totals
- Cumulative utility -460.10, damage 383.0, defense cost 77.10, successful attacks 56 of 141 (39.7%)
