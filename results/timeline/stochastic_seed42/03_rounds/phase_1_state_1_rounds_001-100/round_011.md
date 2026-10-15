# Round 11 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **BruteForce** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.429 | 0.600 |
| Phishing | 0.143 | 0.150 |
| BruteForce | 0.357 | 0.200 |
| Malware | 0.071 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.049, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #6, game value -4.973, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.908 |
| IDS | 0.000 |
| MFA | 0.092 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **Firewall** (probability 0.908).

## 6. Attacker's action
- Attack chosen: **BruteForce** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.48
- Result: **ATTACK SUCCEEDED**
- Damage 8.0 + defense cost 0.50 = loss 8.50  (defender utility -8.50)

## 8. Running totals
- Cumulative utility -28.00, damage 20.0, defense cost 8.00, successful attacks 3 of 11 (27.3%)
