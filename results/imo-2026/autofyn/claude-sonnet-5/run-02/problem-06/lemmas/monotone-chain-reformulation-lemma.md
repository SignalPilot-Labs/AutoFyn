## Lemma: Monotone Chain Reformulation Lemma (CERTIFIED, round 19)

**Source.** `core-growth-monotonicity`, round 19, §5.1. Independently
re-verified by the round-19 proof-reviewer (trivial, re-derived from
scratch).

**Depends on (certified).** `finite-core-theorem.md` (for `S_0`);
`extended-persistent-type-pigeonhole.md` (for `N(S)` at any finite core);
`self-absorbing-core-theorem.md` (for the definitions of the absorption
operator `(·)⁺` and self-absorption).

**Setup.** For `M = 0, 1, 2, ...` define the explicit, monotone, non-adaptive
family `S_M := S_0 ∪ ⋃_{j=1}^{M} P(a_j)` (a finite union of finite sets,
`⊇ S_0 ⊇ Q`, so `N(S_M)` is well-defined for every `M`).

**Statement (sufficiency direction).** If there exists `M ≥ 0` with
`N(S_M) ≤ M`, then `S* := S_M` is a finite self-absorbing core `⊇ S_0`.

**Proof.** By definition `S_M⁺ = S_M ∪ ⋃_{j=1}^{N(S_M)} P(a_j)`. Since
`N(S_M) ≤ M`, `⋃_{j=1}^{N(S_M)} P(a_j) ⊆ ⋃_{j=1}^{M} P(a_j) ⊆ S_M`, so
`S_M⁺ = S_M`. ∎

**What is NOT established (honest scope, independently confirmed).** The
converse is open: an arbitrary self-absorbing `S**` need not be dominated by
a working member of the `S_M` family in a way that makes `N(S_M) ≤ M` hold
(see the companion Non-Monotonicity Gap finding in
`approaches/core-growth-monotonicity.md` §7, Proposition 5 — self-absorption
is not known to be monotone under further core enlargement). So this Lemma
gives only a sufficient, not necessary, numeric reformulation of "a
self-absorbing core exists."

**Status.** Correct, complete, unconditional — a one-line consequence of the
definitions, but genuinely new (this specific explicit monotone family, and
its use as a sufficient existence criterion, was not previously stated in
the workspace). Reusable as the cleanest currently-known sufficient
reformulation of H2's existence sub-gap.
