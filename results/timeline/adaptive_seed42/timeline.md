# Timeline: adaptive attacker, seed 42, 200 rounds

One row per round. `RE-SOLVE` marks rounds where the agent recomputed the equilibrium; bold rows are events.

| Round | True threat | Agent thinks top threat is | Re-solve | Defense played | Attack | Result | Utility |
|---|---|---|---|---|---|---|---|
| 1 | state_1 | DDoS | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 2 | state_1 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 3 | state_1 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 4 | state_1 | Malware |  | Isolation | Phishing | success | -8.50 |
| 5 | state_1 | Malware |  | Isolation | Phishing | success | -8.50 |
| 6 | state_1 | Malware | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 7 | state_1 | Phishing |  | Isolation | Phishing | blocked | -1.50 |
| 8 | state_1 | Phishing | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 9 | state_1 | Phishing |  | MFA | BruteForce | blocked | -0.60 |
| 10 | state_1 | Phishing |  | Isolation | Phishing | success | -8.50 |
| 11 | state_1 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 12 | state_1 | Phishing | RE-SOLVE | Isolation | DDoS | success | -7.50 |
| 13 | state_1 | Phishing |  | MFA | DDoS | success | -6.60 |
| 14 | state_1 | Phishing | RE-SOLVE | Isolation | DDoS | blocked | -1.50 |
| 15 | state_1 | Phishing |  | MFA | DDoS | blocked | -0.60 |
| 16 | state_1 | Phishing |  | MFA | DDoS | success | -6.60 |
| 17 | state_1 | Phishing | RE-SOLVE | MFA | DDoS | success | -6.60 |
| 18 | state_1 | Phishing |  | Firewall | Malware | success | -10.50 |
| 19 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 20 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 21 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 22 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 23 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 24 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 25 | state_1 | Malware | RE-SOLVE | Isolation | Malware | success | -11.50 |
| 26 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 27 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 28 | state_1 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 29 | state_1 | Malware |  | Isolation | Malware | success | -11.50 |
| 30 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 31 | state_1 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 32 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 33 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 34 | state_1 | Malware | RE-SOLVE | Isolation | DDoS | success | -7.50 |
| 35 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 36 | state_1 | Malware |  | Isolation | Malware | success | -11.50 |
| 37 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 38 | state_1 | Malware | RE-SOLVE | Isolation | DDoS | blocked | -1.50 |
| 39 | state_1 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 40 | state_1 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 41 | state_1 | Malware | RE-SOLVE | Isolation | DDoS | success | -7.50 |
| 42 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 43 | state_1 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 44 | state_1 | Malware | RE-SOLVE | Isolation | DDoS | blocked | -1.50 |
| 45 | state_1 | Malware |  | Isolation | DDoS | success | -7.50 |
| 46 | state_1 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 47 | state_1 | Malware | RE-SOLVE | Isolation | DDoS | success | -7.50 |
| 48 | state_1 | DDoS |  | Isolation | DDoS | blocked | -1.50 |
| 49 | state_1 | DDoS |  | Isolation | DDoS | blocked | -1.50 |
| **50** | **adapted** | | | | | | Equilibrium in use first favours **Firewall** (the reference best defense for `state_1`), 49 rounds after the phase began. |
| 50 | state_1 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 51 | state_1 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 52 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 53 | state_1 | DDoS | RE-SOLVE | Firewall | BruteForce | success | -8.50 |
| 54 | state_1 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 55 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 56 | state_1 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 57 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 58 | state_1 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 59 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 60 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 61 | state_1 | DDoS | RE-SOLVE | Firewall | Malware | success | -10.50 |
| 62 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 63 | state_1 | DDoS |  | Firewall | Malware | success | -10.50 |
| 64 | state_1 | DDoS | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 65 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 66 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 67 | state_1 | Malware | RE-SOLVE | Isolation | Malware | success | -11.50 |
| 68 | state_1 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 69 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 70 | state_1 | Malware | RE-SOLVE | Isolation | Phishing | success | -8.50 |
| 71 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 72 | state_1 | Malware |  | Isolation | Phishing | success | -8.50 |
| 73 | state_1 | Malware | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 74 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 75 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 76 | state_1 | Malware | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 77 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 78 | state_1 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 79 | state_1 | Phishing | RE-SOLVE | Isolation | Phishing | success | -8.50 |
| 80 | state_1 | Phishing |  | Isolation | Phishing | success | -8.50 |
| 81 | state_1 | Phishing |  | Isolation | Phishing | blocked | -1.50 |
| 82 | state_1 | Phishing | RE-SOLVE | MFA | Phishing | blocked | -0.60 |
| 83 | state_1 | Phishing |  | Isolation | Phishing | blocked | -1.50 |
| 84 | state_1 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 85 | state_1 | Phishing | RE-SOLVE | MFA | Phishing | success | -7.60 |
| 86 | state_1 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 87 | state_1 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 88 | state_1 | Phishing | RE-SOLVE | MFA | Phishing | blocked | -0.60 |
| 89 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 90 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 91 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 92 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 93 | state_1 | Phishing | RE-SOLVE | MFA | Malware | success | -10.60 |
| 94 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 95 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 96 | state_1 | Phishing | RE-SOLVE | MFA | Malware | blocked | -0.60 |
| 97 | state_1 | Phishing |  | MFA | Malware | success | -10.60 |
| 98 | state_1 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 99 | state_1 | Phishing | RE-SOLVE | MFA | Malware | success | -10.60 |
| 100 | state_1 | Malware |  | Isolation | DDoS | success | -7.50 |
| **101** | **THREAT SWITCH** | | | | | | True threat state is now `state_2`: DDoS 0.15, Phishing 0.10, BruteForce 0.65, Malware 0.10 |
| 101 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 102 | state_2 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 103 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 104 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 105 | state_2 | Malware | RE-SOLVE | Isolation | Malware | success | -11.50 |
| 106 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 107 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 108 | state_2 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 109 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 110 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 111 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 112 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 113 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 114 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 115 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 116 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 117 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 118 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 119 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 120 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 121 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 122 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 123 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 124 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 125 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 126 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 127 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 128 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 129 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 130 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 131 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 132 | state_2 | Malware |  | Isolation | DDoS | success | -7.50 |
| 133 | state_2 | Malware |  | Isolation | BruteForce | blocked | -1.50 |
| 134 | state_2 | Malware |  | Isolation | Phishing | success | -8.50 |
| 135 | state_2 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 136 | state_2 | Malware |  | Isolation | Phishing | success | -8.50 |
| 137 | state_2 | Malware | RE-SOLVE | Isolation | Phishing | success | -8.50 |
| 138 | state_2 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 139 | state_2 | Malware |  | Isolation | Phishing | success | -8.50 |
| 140 | state_2 | Malware | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 141 | state_2 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 142 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 143 | state_2 | Malware |  | Isolation | Phishing | blocked | -1.50 |
| 144 | state_2 | Phishing | RE-SOLVE | Isolation | Phishing | blocked | -1.50 |
| 145 | state_2 | Phishing |  | Isolation | Phishing | blocked | -1.50 |
| 146 | state_2 | Phishing |  | Isolation | Phishing | success | -8.50 |
| **147** | **adapted** | | | | | | Equilibrium in use first favours **MFA** (the reference best defense for `state_2`), 46 rounds after the phase began. |
| 147 | state_2 | Phishing | RE-SOLVE | MFA | Phishing | blocked | -0.60 |
| 148 | state_2 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 149 | state_2 | Phishing |  | MFA | Phishing | blocked | -0.60 |
| 150 | state_2 | Phishing | RE-SOLVE | MFA | Phishing | success | -7.60 |
| 151 | state_2 | Phishing |  | MFA | DDoS | success | -6.60 |
| 152 | state_2 | Phishing |  | MFA | DDoS | success | -6.60 |
| 153 | state_2 | Phishing |  | MFA | DDoS | success | -6.60 |
| 154 | state_2 | Phishing | RE-SOLVE | MFA | DDoS | success | -6.60 |
| 155 | state_2 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 156 | state_2 | Phishing |  | MFA | Malware | success | -10.60 |
| 157 | state_2 | Phishing | RE-SOLVE | MFA | Malware | success | -10.60 |
| 158 | state_2 | Phishing |  | MFA | Malware | blocked | -0.60 |
| 159 | state_2 | Phishing |  | MFA | Malware | success | -10.60 |
| 160 | state_2 | Phishing | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 161 | state_2 | Phishing |  | MFA | Malware | success | -10.60 |
| 162 | state_2 | Phishing |  | Isolation | Malware | blocked | -1.50 |
| 163 | state_2 | Phishing |  | MFA | Malware | success | -10.60 |
| 164 | state_2 | Malware | RE-SOLVE | MFA | BruteForce | blocked | -0.60 |
| 165 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 166 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 167 | state_2 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 168 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 169 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 170 | state_2 | Malware | RE-SOLVE | Isolation | BruteForce | success | -9.50 |
| 171 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 172 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 173 | state_2 | Malware | RE-SOLVE | Isolation | Malware | blocked | -1.50 |
| 174 | state_2 | Malware |  | Isolation | Malware | blocked | -1.50 |
| 175 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 176 | state_2 | Malware |  | Isolation | Malware | success | -11.50 |
| 177 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 178 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 179 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 180 | state_2 | Malware |  | Isolation | DDoS | success | -7.50 |
| 181 | state_2 | Malware |  | Isolation | DDoS | success | -7.50 |
| 182 | state_2 | Malware | RE-SOLVE | Isolation | DDoS | success | -7.50 |
| 183 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 184 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 185 | state_2 | Malware | RE-SOLVE | Isolation | DDoS | blocked | -1.50 |
| 186 | state_2 | Malware |  | Isolation | DDoS | blocked | -1.50 |
| 187 | state_2 | DDoS |  | Isolation | DDoS | blocked | -1.50 |
| 188 | state_2 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 189 | state_2 | DDoS |  | Isolation | DDoS | blocked | -1.50 |
| 190 | state_2 | DDoS |  | Firewall | DDoS | success | -6.50 |
| 191 | state_2 | DDoS | RE-SOLVE | Firewall | DDoS | blocked | -0.50 |
| 192 | state_2 | DDoS |  | Firewall | BruteForce | blocked | -0.50 |
| 193 | state_2 | DDoS |  | Firewall | DDoS | blocked | -0.50 |
| 194 | state_2 | DDoS | RE-SOLVE | Firewall | Malware | success | -10.50 |
| 195 | state_2 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 196 | state_2 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 197 | state_2 | DDoS |  | Firewall | Malware | success | -10.50 |
| 198 | state_2 | DDoS |  | Firewall | Malware | success | -10.50 |
| 199 | state_2 | DDoS |  | Firewall | Malware | blocked | -0.50 |
| 200 | state_2 | DDoS | RE-SOLVE | Firewall | Malware | success | -10.50 |
