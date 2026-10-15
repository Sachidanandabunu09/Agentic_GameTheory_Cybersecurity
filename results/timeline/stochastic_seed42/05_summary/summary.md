# Summary

- Rounds: 200   |   attacker: stochastic   |   seed: 42
- Attack success rate: 36.0%
- Average damage per round: 2.56
- Average defense cost per round: 0.58
- Average defender utility per round: -3.13
- Times the game was re-solved: 22 (out of 200 rounds)

## Per phase
| Phase | True threat | Rounds | Avg utility | Attack success | Defenses played | Attacks seen |
|---|---|---|---|---|---|---|
| 1 | state_1 | 1-100 | -3.04 | 38.0% | Firewall 89%, MFA 9%, Isolation 2% | DDoS 66%, Phishing 11%, BruteForce 21%, Malware 2% |
| 2 | state_2 | 101-200 | -3.23 | 34.0% | Firewall 34%, MFA 59%, Isolation 7% | DDoS 21%, Phishing 6%, BruteForce 63%, Malware 10% |

## Adaptation lag
| Phase | Threat state | Phase starts at round | Mix first favours reference best defense at round | Lag (rounds) | Reference best defense |
|---|---|---|---|---|---|
| 1 | state_1 | 1 | 7 | 6 | Firewall |
| 2 | state_2 | 101 | 126 | 25 | MFA |

The lag is how long the agent needed, after the threat changed, before its equilibrium mix favoured the defense that a perfectly informed Nash defender would favour. It comes from the memory window: the agent must observe enough new attacks first.
