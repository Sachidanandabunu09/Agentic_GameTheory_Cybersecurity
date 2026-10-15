# Round 175 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **Malware** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.208 | 0.150 |
| Phishing | 0.083 | 0.100 |
| BruteForce | 0.583 | 0.650 |
| Malware | 0.125 | 0.100 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.083, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #20, game value -3.466, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.067 |
| IDS | 0.000 |
| MFA | 0.933 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.933).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.06
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -568.40, damage 470.0, defense cost 98.40, successful attacks 67 of 175 (38.3%)
