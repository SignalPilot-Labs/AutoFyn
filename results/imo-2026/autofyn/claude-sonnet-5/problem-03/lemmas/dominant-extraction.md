# Fact 1 (e ≥ 0) and Fact 2 (dominant extraction, e ≤ max)

**Certified by:** proof-reviewer, round 3, from approach `dyadic-cascade-induction`
(round-3 builder; Fact 1 was already implicit, uncredited, inside Lemma G's own proof).

**Depends on:** nothing beyond the definition `e(M) := Σ_{i} (-1)^{i+1} m_i` for a sorted
descending multiset `M = (m_1≥m_2≥…≥m_K)` (as used throughout this problem's population,
consistent with `lemmas/duplicate-pair-invariance.md`'s setup).

## Statement

**Fact 1.** For any sorted multiset `M = (x_1≥x_2≥…≥x_K≥0)` (`K≥0`), `e(M) ≥ 0`.

**Fact 2 ("dominant extraction").** For any sorted multiset `M = (x_1≥…≥x_K≥0)` with `K≥1`,
writing `rest := (x_2,…,x_K)` (itself sorted descending),
```
e(M) = x_1 - e(rest),
```
exactly, and consequently `e(M) ≤ x_1 = \max(M)`.

## Proof

**Fact 1.** Group consecutive pairs: `e(M) = (x_1-x_2)+(x_3-x_4)+\dots`, with possibly one
unpaired trailing term `x_K` (if `K` is odd) added at the end. Each parenthesized difference
is `≥0` since `M` is sorted descending (`x_{2i-1}\ge x_{2i}`), and the trailing unpaired term
(if present) is `\ge0` since all entries are nonnegative. Summing nonnegative terms gives
`e(M)\ge0`. (This is the same pairing inequality used inside Lemma G's proof,
`lemmas/greedy-reduction.md`; here it is stated and used as a standalone corollary.)

**Fact 2.** Directly from the definition of `e` as an alternating sum starting with a `+`
sign at rank 1: `e(M) = x_1 - x_2 + x_3 - x_4 + \dots = x_1 - (x_2-x_3+x_4-\dots) = x_1 -
e(rest)`. Combining with Fact 1 applied to `rest` (`e(rest)\ge0`), `e(M) = x_1-e(rest)\le x_1`.
∎

## Verification

Independently re-verified by the proof-reviewer, round 3, via 2000 random-sorted-multiset
trials (exact `fractions.Fraction` arithmetic, sizes `1` to `7`, random rational entries):
`e(M)\ge0` and `e(M)\le\max(M)` held in every trial, no violation.

## Reusable by

Any approach needing a cheap, general lower/upper bound on `e` of a multiset with a clearly
dominant (or arbitrary) top element — used in `dyadic-cascade-induction`'s lower-bound §5
(Branch A and Case B2), and potentially useful to `concavity-minimax-duality`'s or
`elementary-exchange-smoothing`'s certificate computations as a sanity bound. Fully general —
no reference to cuts, budgets, or this problem's specific numbers.
