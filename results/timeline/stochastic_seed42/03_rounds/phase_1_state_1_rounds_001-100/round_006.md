# Round 6 of 200

**Phase:** true threat state = `state_1`  (hidden from the agent)

## 1. What the agent observes
- Previous round's attack: **DDoS** (was blocked).

## 2. Agent estimates the threat (last 20 attacks, smoothed)
|  | Agent estimate | True (hidden) |
|---|---|---|
| DDoS | 0.333 | 0.600 |
| Phishing | 0.111 | 0.150 |
| BruteForce | 0.444 | 0.200 |
| Malware | 0.111 | 0.050 |

## 3. Does the agent re-solve the game?
- **NO.** The estimate moved only 0.063, below the 0.1 threshold, so the cached equilibrium is reused.

## 4. Equilibrium in use (solve #4, game value -4.536, mixed)
|  | Defender mix |
|---|---|
| Firewall | 0.480 |
| IDS | 0.000 |
| MFA | 0.520 |
| Isolation | 0.000 |

## 5. Agent's decision
- Sampled from the mix: **MFA** (probability 0.520).

## 6. Attacker's action
- Attack chosen: **DDoS** (sampled from the true threat state).

## 7. Outcome
- Success probability for this pair: 0.80
- Result: **ATTACK BLOCKED**
- Damage 0.0 + defense cost 0.60 = loss 0.60  (defender utility -0.60)

## 8. Running totals
- Cumulative utility -5.30, damage 0.0, defense cost 5.30, successful attacks 0 of 6 (0.0%)
