# Case I Closure Theorem

**Certified:** round 8, from `rank-pigeonhole-budget.md` §5 (headline
result). Reviewer independently re-derived and re-verified:
- Exhaustively (exact `Fraction`) for $m=1,\dots,10$ over every
  $(X,q)$-configuration in all three branches (q-even, q-odd sub-case (a),
  q-odd sub-case (b)): zero violations, matching the builder's own
  6655-configuration exhaustive check
  (`/tmp/round-8/verify_57.py`: 5120+2046+2036 configurations checked, zero
  violations).
- Via an independent coordinate-ascent numerical maximizer (not vertex-
  restricted, searching the full continuum polytope from many random
  starts) that confirms $\max_F E(F\cup\tau)$ never exceeds $R(\tau)$, with
  observed margin $\to0$ (tight, not violated)
  (`/tmp/round-8/optimize_search.py`).
- Identity $R(\tau)+\tau_m=2\tau_1$ (used in §5.5) re-derived and confirmed
  exhaustively for $m=1,\dots,8$.

**Statement.** For every $m\ge1$, every ratio-2 superincreasing tail
$\tau=(\tau_1,\dots,\tau_m)$, every $s\in(0,2\tau_1]$, and every partition
$F$ of $s$ into at most $m+1$ nonnegative parts each $\le\tau_1$ (the "Case
I" hypothesis):
$$A(F\cup\tau)\ \ge\ s-R(\tau),\qquad\text{equivalently}\qquad E(F\cup\tau)\le R(\tau).$$

**Proof outline.** Via `exchange-smoothing-vertex-maximization.md`, it
suffices to check "pinned + one tied group" configurations. Via
`odd-run-reduction-lemma`, $A(S)$ at such a configuration depends only on
the parity pattern $X$ (which reference levels have even pin-count) and the
parity of the tied-group size $q$ (plus, if $q$ odd, the tied value $v$).
Three branches, each closed unconditionally: $q$ even (via
`last-element-bound.md` + the identity $R(\tau)+\tau_m=2\tau_1$), $q$ odd
with the box bound $v=\tau_1$ binding (forces $q=1$, closed via $A\le
\mathrm{Total}$), and $q$ odd with the domain bound binding (closed via
`ratio-2-spacing-lemma.md` and `half-bound-lemma` in a short case split on
$j=|X|$: $j=0$, $j=1$, even $j\ge2$, odd $j\ge3$).

**Depends on:** `exchange-smoothing-vertex-maximization.md`,
`odd-run-reduction-lemma.md`, `ratio-2-spacing-lemma.md`,
`last-element-bound.md`, `half-bound-lemma.md`.

**Combined with the already-certified `case-ii-closure-theorem.md`, this
gives Claim (A)'s full lower bound for every $m$ (hence every $n$).**

**Scope.** Closes Claim (A)'s Case I only (every element of $F$ $\le\tau_1$).
Does NOT address: (i) Claim (B) (arbitrary tail refinement combined with a
Case-I-style split of $p_1$ — $\tau$ here is the fixed, untouched tail); (ii)
the general upper bound. See `current.md` for the project-level scoping.
