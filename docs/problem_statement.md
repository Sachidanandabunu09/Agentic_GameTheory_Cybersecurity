# Problem Statement

## Context

Cyber-defence is an adversarial, information-asymmetric problem. An organisation must pick
which *defensive control* to deploy each round (it usually cannot run them all: controls
have cost and capacity limits), while an attacker chooses which *attack* to launch. Neither
side sees the other's private information:

- the defender does **not** know the attacker's current threat distribution,
- the attacker does **not** know, with certainty, the defender's control policy.

Real defenders must therefore (a) infer the threat from noisy observations, (b) reason
about a strategic adversary, and (c) continuously re-optimise as the threat landscape
shifts — all under a budget.

## Research question

> Can a **lightweight agentic** layer that *estimates the threat state online* and
> *solves a game-theoretic (Nash) equilibrium on the fly* outperform static, random, and
> oracle baselines in a simulated attacker–defender security game — particularly against
> an **adaptive attacker that learns the defender's habits**?

## Sub-questions

1. Does repeatedly solving the Bayesian-weighted zero-sum game yield a defence policy that
   adapts when the hidden threat state changes?
2. How much performance is lost by *estimating* the threat from observations instead of
   knowing it (`Nash(true threat)` / oracle)?
3. Is **sampling** from the equilibrium mix better than **argmax** when the attacker is
   adaptive (i.e. does unpredictability pay off)?
4. How sensitive are the conclusions to the assumed payoff parameters?

## Scope

In scope: a discrete, simultaneous, **zero-sum** game; a 4×4 action space
(4 attacks × 4 defences); a two-state threat schedule; stochastic and adaptive attackers;
empirical evaluation over many seeds; sensitivity analysis.

Out of scope: multi-stage/multi-agent attack trees, partially observable state beyond the
threat distribution, non-zero-sum incentives, real network emulation, reinforcement
learning of the game itself.

## Objectives

- **O1** Formalise the payoff of an attack/defence pair from interpretable parameters
  (success rate, effectiveness, damage, control cost).
- **O2** Solve the induced zero-sum game exactly (LP) and verify the equilibrium.
- **O3** Build a simulator whose realised utilities match the game payoffs.
- **O4** Implement an agentic defender that observes → estimates → (re)solves → samples,
  plus honest baselines.
- **O5** Quantify, with statistical rigour, whether the agentic defender improves utility
  and reduces damage, and test robustness to parameter error.

## Success criteria

- The equilibrium solver is numerically verified on every instance.
- The simulator's expected utility equals the payoff matrix entries.
- The agent adapts its defence mix when the threat state switches (measurable adaptation
  score > 0), while fixed policies score 0.
- Conclusions survive a ±20% parameter perturbation.

See `methodology.md`, `game_model.md`, `agent_architecture.md` and `experiments.md` for how
each objective is met.
