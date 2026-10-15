# Summary

- Rounds: 200   |   attacker: adaptive   |   seed: 42
- Attack success rate: 38.5%
- Average damage per round: 3.22
- Average defense cost per round: 1.16
- Average defender utility per round: -4.38
- Times the game was re-solved: 52 (out of 200 rounds)

## Per phase
| Phase | True threat | Rounds | Avg utility | Attack success | Defenses played | Attacks seen |
|---|---|---|---|---|---|---|
| 1 | state_1 | 1-100 | -4.59 | 42.0% | Firewall 15%, MFA 29%, Isolation 56% | DDoS 23%, Phishing 28%, BruteForce 2%, Malware 47% |
| 2 | state_2 | 101-200 | -4.18 | 35.0% | Firewall 12%, MFA 16%, Isolation 72% | DDoS 21%, Phishing 16%, BruteForce 4%, Malware 59% |

## Adaptation lag
| Phase | Threat state | Phase starts at round | Mix first favours reference best defense at round | Lag (rounds) | Reference best defense |
|---|---|---|---|---|---|
| 1 | state_1 | 1 | 50 | 49 | Firewall |
| 2 | state_2 | 101 | 147 | 46 | MFA |

The lag is how long the agent needed, after the threat changed, before its equilibrium mix favoured the defense that a perfectly informed Nash defender would favour. It comes from the memory window: the agent must observe enough new attacks first.
