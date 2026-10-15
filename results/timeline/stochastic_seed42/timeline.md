# Timeline: stochastic attacker, seed 42, 200 rounds

One row per round. `RE-SOLVE` marks rounds where the agent recomputed the equilibrium; bold rows are events.

| Round | True threat | Agent thinks top threat is | Re-solve | Defense played | Attack | Result | Utility |
|---|---|---|---|---|---|---|---|
| 1 | state_1 | DDoS | RE-SOLVE | Isolation | BruteForce | blocked | -1.50 |
| 2 | state_1 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 3 | state_1 | BruteForce | RE-SOLVE | Isolation | DDoS | blocked | -1.50 |
| 4 | state_1 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 5 | state_1 | BruteForce |  | Firewall | DDoS | blocked | -0.50 |
| 6 | state_1 | BruteForce |  | MFA | DDoS | blocked | -0.60 |
| **7** | **adapted** | | | | | | Equilibrium in use first favours **Firewall** (the reference best defense for `state_1`), 6 rounds after the phase began. |
| 7 | state_1 | DDoS | RE-SOLVE | MFA | Phishing | blocked | -0.60 |
| 8 | state_1 | DDoS |  | MFA | DDoS | success | -6.60 |
| 9 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 10 | state_1 | DDoS | RE-SOLVE | Firewall | BruteForce | blocked | -0.50 |
| 11 | state_1 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 12 | state_1 | DDoS |  | MFA | Malware | blocked | -0.60 |
| 13 | state_1 | DDoS | RE-SOLVE | Firewall | BruteForce | success | -8.50 |
| 14 | state_1 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 15 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 16 | state_1 | DDoS |  | Firewall | Phishing | blocked | -0.50 |
| 17 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 18 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 19 | state_1 | DDoS |  | MFA | DDoS | success | -6.60 |
| 20 | state_1 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 21 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 22 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 23 | state_1 | DDoS |  | MFA | BruteForce | blocked | -0.60 |
| 24 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 25 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 26 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 27 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 28 | state_1 | DDoS |  | Firewall | Phishing | blocked | -0.50 |
| 29 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 30 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 31 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 32 | state_1 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 33 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 34 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 35 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 36 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 37 | state_1 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 38 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 39 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 40 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 41 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 42 | state_1 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 43 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 44 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 45 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 46 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 47 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 48 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 49 | state_1 | DDoS | RE-SOLVE | Firewall | DDoS | success | -6.50 |
| 50 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 51 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 52 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 53 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 54 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 55 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 56 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 57 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 58 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 59 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 60 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 61 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 62 | state_1 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 63 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 64 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 65 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 66 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 67 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 68 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 69 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 70 | state_1 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 71 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 72 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 73 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 74 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 75 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 76 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 77 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 78 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 79 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 80 | state_1 | DDoS |  | Firewall | Phishing | blocked | -0.50 |
| 81 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 82 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 83 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 84 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 85 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 86 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 87 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 88 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 89 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 90 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 91 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 92 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 93 | state_1 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 94 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 95 | state_1 | DDoS |  | Firewall | Phishing | success | -7.50 |
| 96 | state_1 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 97 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 98 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 99 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 100 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| **101** | **THREAT SWITCH** | | | | | | True threat state is now `state_2`: DDoS 0.15, Phishing 0.10, BruteForce 0.65, Malware 0.10 |
| 101 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 102 | state_2 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 103 | state_2 | DDoS | RE-SOLVE | Firewall | DDoS | success | -6.50 |
| 104 | state_2 | DDoS |  | MFA | DDoS | success | -6.60 |
| 105 | state_2 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 106 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 107 | state_2 | DDoS |  | Firewall | Phishing | blocked | -0.50 |
| 108 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 109 | state_2 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 110 | state_2 | DDoS |  | Firewall | Malware | success | -10.50 |
| 111 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 112 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 113 | state_2 | DDoS | RE-SOLVE | Firewall | BruteForce | blocked | -0.50 |
| 114 | state_2 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 115 | state_2 | DDoS |  | Firewall | BruteForce | success | -8.50 |
| 116 | state_2 | DDoS |  | MFA | DDoS | success | -6.60 |
| 117 | state_2 | DDoS |  | MFA | Malware | success | -10.60 |
| 118 | state_2 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 119 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 120 | state_2 | BruteForce | RE-SOLVE | MFA | DDoS | success | -6.60 |
| 121 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 122 | state_2 | BruteForce |  | MFA | Phishing | blocked | -0.60 |
| 123 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 124 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 125 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| **126** | **adapted** | | | | | | Equilibrium in use first favours **MFA** (the reference best defense for `state_2`), 25 rounds after the phase began. |
| 126 | state_2 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 127 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 128 | state_2 | BruteForce |  | MFA | Phishing | blocked | -0.60 |
| 129 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 130 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 131 | state_2 | BruteForce |  | MFA | DDoS | blocked | -0.60 |
| 132 | state_2 | BruteForce |  | Isolation | BruteForce | success | -9.50 |
| 133 | state_2 | BruteForce |  | MFA | Malware | success | -10.60 |
| 134 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 135 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 136 | state_2 | BruteForce |  | Firewall | DDoS | success | -6.50 |
| 137 | state_2 | BruteForce |  | Isolation | DDoS | blocked | -1.50 |
| 138 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 139 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 140 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 141 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 142 | state_2 | BruteForce |  | MFA | Phishing | success | -7.60 |
| 143 | state_2 | BruteForce |  | Isolation | BruteForce | blocked | -1.50 |
| 144 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 145 | state_2 | BruteForce | RE-SOLVE | Firewall | BruteForce | success | -8.50 |
| 146 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 147 | state_2 | BruteForce |  | Firewall | Malware | success | -10.50 |
| 148 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 149 | state_2 | BruteForce |  | Firewall | Malware | blocked | -0.50 |
| 150 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 151 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 152 | state_2 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 153 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 154 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 155 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 156 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 157 | state_2 | BruteForce | RE-SOLVE | MFA | Phishing | blocked | -0.60 |
| 158 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 159 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 160 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 161 | state_2 | BruteForce |  | MFA | Malware | success | -10.60 |
| 162 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 163 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 164 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 165 | state_2 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 166 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 167 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 168 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 169 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 170 | state_2 | BruteForce |  | Isolation | DDoS | blocked | -1.50 |
| 171 | state_2 | BruteForce | RE-SOLVE | MFA | DDoS | blocked | -0.60 |
| 172 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 173 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 174 | state_2 | BruteForce |  | MFA | Malware | success | -10.60 |
| 175 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 176 | state_2 | BruteForce |  | Firewall | BruteForce | success | -8.50 |
| 177 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 178 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 179 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 180 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 181 | state_2 | BruteForce |  | MFA | Malware | success | -10.60 |
| 182 | state_2 | BruteForce |  | MFA | DDoS | success | -6.60 |
| 183 | state_2 | BruteForce | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 184 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 185 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 186 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 187 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 188 | state_2 | BruteForce |  | Firewall | Phishing | success | -7.50 |
| 189 | state_2 | BruteForce |  | MFA | Malware | success | -10.60 |
| 190 | state_2 | BruteForce |  | Firewall | BruteForce | blocked | -0.50 |
| 191 | state_2 | BruteForce | RE-SOLVE | Isolation | BruteForce | blocked | -1.50 |
| 192 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 193 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 194 | state_2 | BruteForce |  | Isolation | BruteForce | blocked | -1.50 |
| 195 | state_2 | BruteForce |  | MFA | DDoS | blocked | -0.60 |
| 196 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 197 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 198 | state_2 | BruteForce |  | Isolation | DDoS | blocked | -1.50 |
| 199 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
| 200 | state_2 | BruteForce |  | MFA | BruteForce | blocked | -0.60 |
