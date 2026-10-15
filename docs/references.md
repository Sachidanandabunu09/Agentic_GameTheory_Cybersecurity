# References

## Game theory foundations

- von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*.
  Princeton University Press. — minimax theorem for zero-sum games.
- Nash, J. F. (1950). Equilibrium points in n-person games. *PNAS*, 36(1), 48–49. —
  existence of mixed-strategy equilibria.
- Nash, J. F. (1951). Non-cooperative games. *Annals of Mathematics*, 54(2), 286–295.
- Harsanyi, J. C. (1967–1968). Games with incomplete information played by "Bayesian"
  players, Parts I–III. *Management Science*, 14. — the Bayesian/Harsanyi game formalism
  that motivates prior-weighting by the threat state.
- Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press.
- Dantzig, G. B. (1963). *Linear Programming and Extensions*. Princeton University Press. —
  LP formulation and duality used by the solver.

## Game theory for security

- Lye, K., & Wing, J. M. (2005). Game strategies in network security.
  *International Journal of Information Security*, 4(1–2), 71–86.
- Alpcan, T., & Başar, T. (2011). *Network Security: A Decision and Game-Theoretic
  Approach*. Cambridge University Press.
- Manshaei, M. H., Zhu, Q., Alpcan, T., Başar, T., & Hubaux, J.-P. (2013). Game theory
  meets network security and privacy. *ACM Computing Surveys*, 45(3), 1–39.
- Roy, S., Ellis, C., Shiva, S., Dasgupta, D., Shandilya, V., & Wu, Q. (2010). A survey of
  game theory as applied to network security. *HICSS*.
- Tambe, M. (2011). *Security and Game Theory: Algorithms, Deployed Systems, Lessons
  Learned*. Cambridge University Press. — Stackelberg/security-games background.
- van Dijk, M., Juels, A., Op den Akker, R., & Alvim, M. S. (2013). FlipIt: The game of
  "stealthy takeover". *Journal of Cryptology*, 26(4), 655–713. — attacker/defender
  control games.
- Zhu, Q., & Başar, T. (2013). Game-theoretic approach to feedback-driven multi-stage
  moving target defense. *GameSec*. — dynamic/adaptive defence, closest to the adaptive
  attacker here.
- Anderson, R. (2001). Why information security is hard — an economic perspective.
  *ACSAC*. — economic framing of security decisions.

## Learning / adaptive agents

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*
  (2nd ed.). MIT Press. — context for the adaptive attacker's ε-greedy learning.

## Software

- Harris, C. R., et al. (2020). Array programming with NumPy. *Nature*, 585, 357–362.
- Virtanen, P., et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing
  in Python. *Nature Methods*, 17, 261–272. — `scipy.optimize.linprog` (HiGHS) used for
  the equilibria.
- McKinney, W. (2010). Data structures for statistical computing in Python. *SciPy
  Proceedings*. — pandas.
- Hunter, J. D. (2007). Matplotlib: a 2D graphics environment. *Computing in Science &
  Engineering*, 9(3), 90–95.
- Waskom, M. L. (2021). seaborn: statistical data visualization. *JOSS*, 6(60), 3021.
- Hierarchical Data Format / HiGHS: Huangfu, Q., & Hall, J. A. J. (2018). Parallelizing the
  dual revised simplex method. *Mathematical Programming Computation*, 10, 119–142.
- pytest documentation — https://docs.pytest.org

## Project-internal design notes

- `game_model.md` — payoff derivation and Bayesian weighting.
- `methodology.md` — experimental and statistical protocol.
- `agent_architecture.md` — the defender agent control loop.
- `experiments.md` — experiment design and results.
