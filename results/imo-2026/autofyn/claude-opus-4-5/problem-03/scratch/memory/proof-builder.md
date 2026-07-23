# Proof-Builder Role Memory

ALWAYS: Verify the game structure computationally for small cases before writing the proof (because numerical verification revealed the correct interpretation of the minimax, round 1)

ALWAYS: When dealing with two-player zero-sum games, be clear about whether you're computing max-min or min-max (because confusing these leads to misinterpreting the upper bound, round 1)

NEVER: Claim a step is "straightforward" or "by similar argument" without actually doing the computation or argument (because this violates rigor rules and leaves gaps, round 1)

ALWAYS: When proving upper bounds for game-theoretic problems, verify that the opponent's response space includes ALL valid strategies, not just a natural-looking subset (because assuming only "symmetric/equal" strategies can miss the true optimum, as happened with asymmetric splits in stick-cutting game, round 2)

ALWAYS: When an induction has edge cases where the main recursive strategy doesn't apply, explicitly identify these as potential gaps early and test them numerically (because the sandwich case k* = m+1 required completely different analysis than the main k* < m+1 case, round 3)

NEVER: Assume halving (symmetric splitting) is always optimal for XY; asymmetric splits may be necessary in certain configurations (because numerical search showed asymmetric splits achieving targets where halving failed, round 3)
