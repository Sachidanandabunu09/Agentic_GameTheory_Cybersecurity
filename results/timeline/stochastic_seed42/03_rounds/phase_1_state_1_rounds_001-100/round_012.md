# Round 12 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (succeeded).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.400 | 0.600 |
| Phishing | 0.133 | 0.150 |
| BruteForce | 0.400 | 0.200 |
| Malware | 0.067 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.092, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #6, game value -4.973, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.908 |
| IDS | 0.000 |
| MFA | 0.092 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.092).

## 6. Attacker's action
- Attack chosen: **Malware** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.63
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -28.60, damage 20.0, defense cost 8.60, successful attacks 3 of 12 (25.0%)
