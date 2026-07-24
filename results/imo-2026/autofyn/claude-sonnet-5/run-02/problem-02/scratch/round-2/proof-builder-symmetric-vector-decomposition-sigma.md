# Build report — symmetric-vector-decomposition-sigma, round 2

## What I did

1. Read `results/imo-2026-02/current.md`, the approach file (round-2
   outliner's revision), `/tmp/round-2/outline-reviewer.md`, and the two
   named certified lemmas (`o-free-circumcenter-reformulation.md`,
   `nine-point-center-reduction.md`).
2. Wrote out, in full and rigorously, the clause-by-clause verification
   that σ (B↔C, M↔N, K↔L, A fixed) is a symmetry of the eight-clause
   hypothesis system defining (K,L) — upgrading the outline's "steps 1-2"
   from asserted/numerically-checked to a written proof. Confirmed it
   matches the round-2 explorer's numerics exactly (no discrepancy).
3. Attempted the actual load-bearing step (outline's step 3/4): derive
   that the σ swap forces `T := (O−N9)·(C−B) = 0`. **Found and proved a
   genuine obstruction**: `T(A,C,B,L,K) = −T(A,B,C,K,L)` holds as a pure
   algebraic tautology for ALL points A,B,C,K,L, independent of hypotheses
   (i)-(iii). Proved this by hand (via circumcenter/nine-point-center's
   order-invariance) and independently cross-checked symbolically in
   `sympy` with fully free, unconstrained coordinates (the sum of the
   O-free-lemma expression and its σ-swap is identically 0 with no
   conditions imposed). Traced the tautology to its root: it is exactly
   the elementary fact that `OM²−ON²` is antisymmetric under swapping the
   names M,N for any point O (also verified in `sympy`), which needs no
   geometry of this problem at all. Concluded that this sign-flip, by
   itself, can never force `T=0` (it lacks the accompanying "second
   independent evaluation" that would be needed), and showed exactly why
   it *does* work in the isosceles special case (there σ is realized by
   an actual reflection isometry, not just a relabeling, which supplies
   the missing relation) but not in the general scalene case.
4. Wrote up both results (positive: the full σ-invariance proof; negative:
   the vacuity theorem) into
   `results/imo-2026-02/approaches/symmetric-vector-decomposition-sigma.md`,
   with an honest partial status and a precise account of what a genuine
   rescue would require (a real sine-rule computation using conditions
   (ii),(iii) directly, not just their formal σ-pairing — comparable in
   difficulty to the `complex-number-argument-bash` leader's remaining
   gap, not accomplished this round).

## Outcome

Per the dispatch instructions ("if you find an obstruction... be honest
about it... don't force a false proof"), I did not force a proof. The
round's genuine contribution is: (a) the σ-invariance clause verification
now fully rigorous (was only numerically checked before), and (b) a
rigorous negative result showing the specific mechanism the outline
proposed (naive antisymmetry ⟹ vanishing) cannot work as conceived — this
is valuable to the population because it prevents wasted future effort on
this exact framing and precisely localizes what a real fix would need.

Status set to `partial` (real content established, but the top-level goal
OM=ON is not proved by this approach). I recommend the outline-reviewer
treat this as RETHINK-worthy for the "naive σ-antisymmetry" mechanism
specifically — any future revival of this slug should pivot to the
"genuine rescue" route sketched at the end of the approach file (explicit
sine-rule computation from conditions (ii),(iii), not relabeling alone),
or the field should treat `complex-number-argument-bash` as the sole live
route unless a third, structurally different framing is found.

## File written

`/home/agentuser/repo/results/imo-2026-02/approaches/symmetric-vector-decomposition-sigma.md`
(Status: partial)
