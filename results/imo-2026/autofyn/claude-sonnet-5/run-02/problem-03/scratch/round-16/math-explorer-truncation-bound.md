# Scouting report: upper bound on A(R'_{>v}) (round 15's unified Claim-B crux)

## The target, precisely

Round 15 (`results/imo-2026-03/approaches/greedy-halving-adversary.md`,
Proposition 30, and `lemmas/upper-truncation-identity.md`) reduced items
1≡2 (ℓ(F)=1, v<s) **and** item 3 (ℓ(F)=2, P≠∅, τ_P≥p_3) to one isolated
open fact:

> Bound **A(R'_{>v})** from above, where R' is any legal ≤(n-2)-cut
> refinement of the (n-2)-ladder tail {p_3,...,p_{n+1}} (rescaled: an
> arbitrary legal (n-2)-ladder response) and v∈(0,s) is an arbitrary real
> threshold, R'_{>v} := {r∈R' : r>v}.

By `tail-self-similarity`/scaling this is literally "bound A(S_{>v}) for S
a legal (n-2)-ladder response, v arbitrary" — self-similar at every
recursion depth, which is exactly why it has resisted the population's
main tool (induction on n, i.e. "assume L(n-2), prove L(n-1)"): the needed
fact is not a special value of the *lower bound* L already available, it's
a structurally different (upper, partial/truncated) statement about the
same object.

## What's been tried and killed (do not re-attempt)

1. **`max-domination-lemma`** (A(S)≤max(S)): computed explicitly in
   Proposition 30's write-up — substituting the crude bound
   A(R'_{>v})≤max(R')≤s back into the target gives
   A(F∪G')≥v−p_2+3f(n), which goes *negative* for small v. Confirmed too
   weak by direct computation, not just asserted.
2. **`triangle-bound-for-a`/`max-domination-lemma` "cheap" combination**
   for Target B (item 3): refuted concretely — the required hypothesis
   max(G')≤t*/2 fails whenever p_3 is left uncut, and even where it
   doesn't apply the naive conclusion fails in ~92% of random trials
   (round 15 outline's own refutation). Margin at n=3,4 is razor-thin
   (0.002–0.14×f(n)), not the "17×f(n) generous slack" the round-15
   outline assumed — so no crude/slack-absorbing bound is expected to
   work; whatever closes it must be close to sharp.
3. **`ratio-2-spacing-lemma` / `last-element-bound`** (A(X)≥min(X) for X a
   sub-collection of a *raw, untouched* ratio-2 tail): does not transfer.
   These need the elements of X to literally be undivided ladder pieces
   τ_i with the exact ratio-2 spacing. R'_{>v}'s elements are *fragments*
   of a legal refinement — already cut, so consecutive elements need not
   satisfy the ratio-2 gap. This exact transfer failure was already
   diagnosed independently in round 13 (Case-13's "no-dominant-fragment"
   branch: "those two lemmas' proofs use the raw ratio-2 spacing of an
   *untouched* reference sequence, which R does not have once it has
   itself been cut") — the same obstruction recurs here under a new name.
   Also explicitly listed in orchestrator history as a permanently-refuted
   route ("fixed-ratio bijective pairing", "binary-digit/carry
   mechanisms").
4. **Peel-induction on ℓ(S)/size** and **naive mass-only bounds**: both
   already ruled out per the run's standing "never retry" list (Parity
   Coincidence Lemma; proven-too-weak mass bounds).

## Candidate techniques not yet tried on this exact quantity

### (a) LP-duality / vertex-extremal characterization (most promising — a genuinely different framing)
The project's one confirmed "broke a 4-round plateau" moment (round 5→6)
was exactly this shape of problem — stuck needing an upper bound while
only lower-bound induction machinery existed — and it was broken by
`lp-duality-certificate.md`'s vertex/LP framing, not by a sharper
induction. Separately, `lemmas/vertex-minimum-theorem.md` already proves,
in full generality (no ladder assumption needed for the argument
structure), that any extremum of an A-type functional over the compact
polytope of legal refinements is attained at a **vertex** — a point
pinned by finitely many "fragment=0" or "fragment=fragment" tie
constraints — via `odd-run-reduction-lemma` this collapses to a genuinely
small combinatorial object (a distinct-valued multiset). **Untried
idea:** apply the vertex-minimum-theorem machinery directly to the
functional S ↦ A(S_{>v}) (jointly maximizing over both the legal
refinement S and, if needed, the threshold-adjacent tie structure),
instead of trying to bound it via an inductive lower-bound composition.
This sidesteps "only lower-bound machinery available" by attacking the
*max* directly as an extremal/combinatorial-enumeration problem over
finitely many vertex types, exactly the mechanism that worked once
already in this project on a structurally analogous obstruction.
Caveat: enumerating vertices for A(S_{>v}) specifically (a function of a
sub-threshold restriction of S, not of S itself) is new — the existing
vertex enumerations (`per-piece-vertex-decomposition-theorem`,
`rank-tie-vertex-reduction`) were built for A(S) or A(F∪G), not for a
truncated sub-object; this would need genuine new work to adapt, not a
direct citation.

### (b) Continuous-perturbation/monotonicity-in-threshold, applied to A(S_{>v}) itself
Round 12's Proposition 26 broke its own analogous case by treating the
*split point* as a continuous real parameter t and showing
d/dt[ψ(t) − target(t)] is sign-definite, reducing the whole inequality to
one boundary value. That trick was applied to A(F∪G') as a function of a
split value t. **Untried variant:** apply the same continuous-parameter
differentiation directly to v ↦ A(S_{>v}) (a monotone-decreasing step
function of v, jumping by ±(element value) at each element of S) and try
to bound its *total variation* or *rate of change* using the ladder's
ratio-2 structure on the *un-refined* piece boundaries (i.e., even though
S's fragments aren't ratio-2-spaced after cutting, the piece boundaries
p_3,p_4,... that S refines still are) — this is a different lever than
directly bounding the value pointwise, and hasn't been tried on this
specific object. Genuinely speculative; no positive result to report,
just an unexplored angle that reuses certified machinery (Lemma 8 /
`cross-term-identity-threshold`, `general-ladder-dominance`) in a new
combination.

### (c) Recurse the Upper-Truncation Identity one level further (round 15's own suggestion)
Apply `upper-truncation-identity` again to R' itself (S=R', now at the
(n-2)-ladder), converting A(R'_{>v}) into a further partial integral
∫_v^∞ u_{R'} plus a parity correction — but this is exactly the same
shape of problem recursed one level down (round 15 says as much), so it
is not obviously progress unless combined with (a) or (b) to actually
terminate the recursion rather than just relabel it. Flagged by round 15
itself as "the same shape of question... not an instance of any
already-certified lemma."

## Crux corpus search (per crux_moves_documentation.md)

Queried `past_crux_moves_database.json` (2434 cruxes) across
`combinatorics`/`algebra`/`number_theory` for keyword hits on: alternating
sum, superincreasing, truncat*, dyadic/geometric-progression/doubling,
subset-sum, sorted/descending, adversary, cut-budget, majorize/
rearrangement. Result: **no crux directly matches** "upper bound on the
alternating sum of a top-truncated portion of a legal response to a
superincreasing/ladder constraint." The closest generic subtopics are
`extremal-principle` (boundary/vertex attainment — already matched by the
in-house `vertex-minimum-theorem`, candidate (a) above) and
`size-bounding-and-descent` (induction-with-a-smaller-self-similar-
instance — already matched by the in-house `tail-self-similarity`
recursion, candidate (c) above, already flagged as circular by itself).
A few hits used "doubling"/"ladder" language but in unrelated contexts
(p-adic valuation maximization, functional-equation recurrences on
geometric-progression restrictions) — none transplant a technique for
*bounding a truncated alternating sum*. **Conclusion: this appears to be a
genuinely novel sub-problem for the corpus, not one where an existing
crux hands over a ready-made mechanism** — the fix will have to come from
recombining this project's own certified general lemmas (most promisingly
vertex-minimum-theorem/LP-duality-style extremal reasoning, per (a)
above), not from an import.

## Recommendation for next round

Rank candidate (a) — direct vertex/extremal characterization of
max A(S_{>v}), styled after `lp-duality-certificate`'s historically
successful break of the same *shape* of plateau — as the highest-leverage
genuinely new angle to try, since it does not reuse the induction
machinery the population has repeatedly hit a wall with. Candidate (b) is
a secondary, more speculative angle worth a time-boxed attempt in
parallel (different enough in mechanism to diversify the field). Do NOT
re-route through max-domination/triangle-bound (killed, confirmed too
weak with an explicit negative computation) or ratio-2-spacing/last-
element-bound (does not apply to already-refined multisets, confirmed
in round 13's independent diagnosis of the structurally identical
obstruction). Numerics should stay tight: the margin at small n
(0.002–0.14×f(n)) means whatever mechanism is used must be close to sharp,
not a slack-absorbing crude bound.
