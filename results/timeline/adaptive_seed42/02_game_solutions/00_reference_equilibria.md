# Reference equilibria (what a defender who KNEW the true threat would compute)

These are for comparison only. The agent does not see the true threat; it computes its own equilibria from estimates (JSON files in this folder).

## state_1  (game value -5.808, pure saddle point, verified=True)

|  | Defender mix |
|---|---|
| Firewall | 1.000 |
| IDS | 0.000 |
| MFA | 0.000 |
| Isolation | 0.000 |

|  | Attacker mix (worst case) |
|---|---|
| DDoS | 1.000 |
| Phishing | 0.000 |
| BruteForce | 0.000 |
| Malware | 0.000 |

## state_2  (game value -3.165, mixed equilibrium, verified=True)

|  | Defender mix |
|---|---|
| Firewall | 0.042 |
| IDS | 0.000 |
| MFA | 0.958 |
| Isolation | 0.000 |

|  | Attacker mix (worst case) |
|---|---|
| DDoS | 0.826 |
| Phishing | 0.000 |
| BruteForce | 0.174 |
| Malware | 0.000 |
