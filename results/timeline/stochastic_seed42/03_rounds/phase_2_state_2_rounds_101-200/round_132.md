# Round 132 of 200

**Phase:** true threat state = `state_2`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.250 | 0.150 |
| Phishing | 0.125 | 0.100 |
| BruteForce | 0.500 | 0.650 |
| Malware | 0.125 | 0.100 |

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
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.36
- Result: **ATTACK SUCCEEDED**
- Damage 8.0 + defense cost 1.50 = loss 9.50  (defender utility -9.50)

## 8. Running totals
- Cumulative utility -426.00, damage 355.0, defense cost 71.00, successful attacks 52 of 132 (39.4%)
