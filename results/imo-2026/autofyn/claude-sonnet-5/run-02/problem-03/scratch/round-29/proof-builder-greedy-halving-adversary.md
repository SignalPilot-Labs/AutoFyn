# Round 29 build report — greedy-halving-adversary

## Task
Fix the outline-reviewer's two flagged gaps in the "Anchor-Switching Lemma
trichotomy" outline for `h(m)`'s q1-cut sub-case (m>=3):
(1) the outline applied `general-anchored-tie-bound` (Lemma A) to an
arbitrary continuum `c` without first invoking vertex-pinning to justify
restricting to a specific tie-point;
(2) boundary sub-cases c=0, c=w=q1-x, c=q1 were not addressed.

## What was done
Restricted this round's target to the round-29 dispatch's narrower
"single-cut-on-q1, tail-untouched" piece: S = {x, q1-x} ∪ tail, tail
completely untouched, x in (0, q1/2]. For fixed S, rigorously invoked the
certified `single-insert-point-vertex-lemma` (one free coordinate c
inserted into a fixed rest S) to pin the minimizer over c in [0,q1] to
exactly 5 candidate points: c=0, c=q1, c=x, c=q1-x, c=t (t in tail) — this
closes gap (1) explicitly, before any anchored-tie bound is invoked.

Closed 4 of these 5 vertex types unconditionally for every m>=3 (modulo
only the pre-existing (star_m)/(star_{m-1})/(star_{m-2}) strong-induction
dependence already present in Theorem 38/42, nothing new):
- c=0: direct citation of Theorem 38 Claim (I).
- c=q1: new — peels q1 via `sharp-dominant-removal-identity`, then
  recognizes {x}∪tail as exactly Theorem 42's own instantiation one level
  down (m-1), giving the needed bound.
- c=q1-x (the "tie with the anchor itself" boundary the reviewer flagged):
  new — pair-cancellation collapses this to A({x}∪tail), again exactly
  Theorem 42 one level down; this range is closed at x=q1/2 too (unlike
  the c=q1 case), so it also settles the full symmetric boundary x=q1/2.
- c=x: new — pair-cancellation collapses to A({q1-x}∪tail), then an
  exact closed-form evaluation of A(tail) (tail is completely explicit, a
  raw doubling sequence — standard geometric-series algebra, verified
  symbolically for m=3..7) reduces the target to the elementary numeric
  inequality 2^{m-1} >= 3+(-1)^{m-1}, true for every m>=3 (false only at
  m=1, irrelevant since h(1) needs 0 cuts).

The 5th vertex type (c tied to a genuine, non-degenerate tail element t)
is honestly left OPEN: the natural argument (pair-cancel t, peel q1-x,
bound the remainder via the new Insert-Bound Corollary) provably loses a
factor of 2x against a gain of only t — the same "lose more than you gain"
shortfall that sank the outline's own general anchor-switching mechanism,
now isolated to exactly this one vertex type. Verified numerically only
(3000 trials/m, m=3,4,5, zero violations) — explicitly flagged as
corroboration, not a proof.

New reusable lemma: **Insert-Bound Corollary** (|A({y}∪T)-A(T)|<=y for any
y>=0, any finite multiset T of nonnegative reals) — a one-line integration
of the already-certified `single-insert-point-vertex-lemma`'s slope-±1
fact. Proposed for certification at
`results/imo-2026-03/lemmas/insert-bound-corollary.md`.

## Net effect on scope
Within h(m)'s q1-cut sub-case, the single-cut-on-q1/tail-untouched piece
now has only ONE open vertex type (down from "all of c outside two
boundary points" per the pre-round-29 state). h(m) for m>=3 remains open
in full: the complementary piece (S cuts q1 AND refines the tail with
remaining budget, available whenever m>=3 since budget m-1>=2) is
untouched this round, as is Vertex 5. Status remains `partial`; no
overclaim — every closed claim above was independently re-verified this
round by fresh exact-`Fraction` scripts (`/tmp/round-29/check_vertices1234.py`,
`/tmp/round-29/check_vertex5.py`), and every open item is stated precisely
as open, with the exact obstruction (the 2x-vs-t shortfall) named rather
than glossed over.

## Files touched
- `results/imo-2026-03/approaches/greedy-halving-adversary.md` — new
  "Round 29" section (Vertices 1-5), updated Status/Approaches
  tried/Current best/Open gaps/Promotable lemmas.
- `results/imo-2026-03/lemmas/insert-bound-corollary.md` — new proposed
  lemma file.
