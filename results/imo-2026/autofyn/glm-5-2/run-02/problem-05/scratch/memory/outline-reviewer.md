# outline-reviewer per-role rules

ALWAYS: verify load-bearing algebra with sympy/python before accepting a "close encounter" or "cover iteration" bound — the orbit-close-encounter (B) step had an unjustified `a <= c` hidden in its `3+2sqrt2` derivation that only surfaced under numeric check (the entirely-above orbit seed can be arbitrarily far above the fixed point; backward propagation is unavailable since f is non-surjective). (round 1, imo-2026-05)

ALWAYS: when an approach's "distinct" instrument reduces (after its own gap analysis) to importing (A)+(B) from a sibling approach, flag the single-gap convergence — both die together if the shared wall is wrong. Push the outliner for a genuinely different framing of the SHARED step, not a new instrument for the same step. (round 1, imo-2026-05)

NEVER: accept an asymptotic/coefficient-vanishing approach on a functional inequality without checking that the constant-solution residual (the AM-GM gap) can actually be canceled — for P5 the residual `(x-y-c)^2` is non-negative, `~x^2`-dominant at infinity, AND collapses to `0` (tautology) at the iterate-equality point `x=f(y)`, so it swallows the perturbation at infinity and cancels it at equality. Both GM and RMS sides share this residual. (round 1, imo-2026-05)
