## imo-2026-03

**Round-1 note on conflicting explorer conjectures (resolved before outlining):** the
game-theory explorer's `(3^n+1)/(2·3^n)` (from the arithmetic-progression construction
{2,3,4}/9 at n=2, giving 5/9) conflicts with the small-cases and extremal explorers'
`2^n/(2^{n+1}-1)` (dyadic construction {4,2,1}/7 at n=2, giving 4/7). I independently
re-verified via exact-`Fraction` exhaustive/local grid search (not floats, not restricted
to bisection responses) that: (a) XY's best response against {4/9,3/9,2/9} truly bottoms
out at exactly 5/9 (confirmed over single cuts, both-cuts-on-one-piece, and cuts split
across every pair of pieces); (b) XY's best response against {4/7,2/7,1/7} truly bottoms
out at exactly 4/7 under the same exhaustive check; (c) a local search in partition-space
around {4/7,2/7,1/7} finds no nearby partition beating 4/7, and a coarse global search
over all 3-piece partitions found nothing above ≈0.567 < 4/7 elsewhere. Since 4/7 > 5/9,
the dyadic construction strictly dominates the arithmetic-progression one — the
game-theory explorer found a genuine local optimum for its own restricted construction
family, but not the global optimum. **All approaches below target c(n) = 2^n/(2^{n+1}-1)
as the answer; the arithmetic-progression family is a confirmed dead end (subsumed by /
strictly worse than the dyadic family) and should not be revisited as a rival construction
family.**

dyadic-cascade-induction: new
Target: c(n) = 2^n/(2^{n+1}-1) for all n ≥ 1 — both the upper bound (XY always has a
≤n-cut response capping Liu Bang's total at ≤ c(n), for every LB opening) and the matching
construction (LB's ≤n-cut dyadic partition guarantees ≥ c(n) against every XY response).
Technique: reduce the claiming phase to an explicit order-statistic formula (exchange
argument), then attack via a general "duplicate-pair invariance" structural lemma, using
it (i) directly + self-similarity for the lower-bound construction and (ii) via a
case-split (top-piece-dominates vs. comparable) induction on n for the general upper
bound.
Skeleton:
  1. Reduce alternating claiming to "LB gets odd-rank pieces of the sorted final
     multiset, both players play greedy-largest" — by Lemma G (exchange/induction).
  2. Prove Lemma P: a value repeated an even number of times (duplicate pair, adjacent in
     sorted order) contributes exactly half its total to each player, and removing it
     leaves every other element's rank parity (hence LB/XY ownership) unchanged — by a
     direct parity-shift argument on sorted-list rank removal (verified on 2000 random
     exact-rational trials by the outliner; needs a written proof, not just the check).
  3. Lower bound: LB uses dyadic partition b_i=2^{n+1-i}/(2^{n+1}-1); show by induction
     on n (using Lemma P + the self-similarity that peeling the top piece and its matched
     difference leaves exactly the rescaled (n-1)-dyadic sequence) that every XY response
     with ≤n cuts leaves L ≥ c(n).
  4. Upper bound: general XY strategy against ANY LB opening a_1≥…≥a_k, k≤n+1, by strong
     induction on n with an explicit case split at a_1 vs 2a_2 (top piece dominant ⇒
     recurse *inside* a_1 with n-1 cuts; top piece comparable to second ⇒ pair a_1 down
     to a_2 via Lemma P then recurse on the residual with n-1 cuts).
Key lemmas:
  - Lemma G (greedy reduction) — because swapping a suboptimal first pick for the current
    max weakly dominates in any alternating finite-value pick game (induction on size).
  - Lemma P (duplicate-pair invariance) — because removing 2 equal-valued adjacent-rank
    elements shifts all later ranks by an even amount, preserving parity, while the pair
    itself spans exactly one odd + one even rank.
  - Self-similarity of the dyadic sequence under top-piece peeling — because the sequence
    2^{n-1},…,1 (rescaled) is exactly what remains after matching and removing the top
    piece against the second, which is why ratio 2 is a fixed point of the attack.
Open gaps: Lemma G and Lemma P need formal write-ups (currently numerically verified
only, though I have complete correct proof sketches for both above); the lower-bound
induction (step 3) needs to cover ALL of XY's responses, not just the single-cut cascade
pattern found numerically (single cuts, multiple cuts on one piece, cuts split across
several pieces); the upper-bound induction (step 4) case split is only sketched — the
Case (i) "recurse inside a_1" accounting, where ranks interleave between a_1's internal
sub-pieces and the untouched tail a_2,…,a_k, is unresolved and is the single biggest gap
in the whole approach.
Cases to cover: upper bound — a_1 ≥ 2a_2 vs a_1 < 2a_2; lower bound — XY cutting once on
one piece / twice-or-more on one piece / split across ≥2 pieces.
Watch out for: ties in Lemma G composing correctly with Lemma P; LB/XY using fewer than
their full budget of points (must show this never helps, or handle explicitly); do not
let the "XY only matches existing pieces" restriction sneak in as an unproven assumption
in the general upper-bound proof (this is exactly the trap two explorers initially fell
into with weaker constructions).

potential-weighting-upper-bound: new
Target: same as dyadic-cascade-induction (c(n) = 2^n/(2^{n+1}-1), both directions) — a
hedge specifically on dyadic-cascade-induction's hardest step (the general upper bound),
attacked here via a single global potential/weight function instead of explicit case-split
strategy construction.
Technique: potential-function / monovariant argument (KB "Invariants & monovariants"),
adapted from crux aimo-0198's "sum a geometric weight into a single potential the
adversary greedily minimizes, bound total damage by moves × per-move decrease" pattern.
Skeleton:
  1. Reduce claiming phase via Lemma G (import from dyadic-cascade-induction once
     certified, don't re-derive).
  2. Define Φ(multiset) = Σ x_i w_i for a rank-dependent weight sequence w_i (the naive
     ±1 alternating choice collapses to L itself and must be replaced — candidate:
     geometric decay matching ratio 2, e.g. w_i ∝ (-1)^{i+1} 2^{-⌈i/2⌉}, needs
     experimentation).
  3. Prove a uniform per-move bound: every possible single XY cut decreases Φ by at least
     a fixed amount, regardless of where it lands or which piece it targets.
  4. Bound Φ at the LB-optimal start via a majorization argument connecting to the same
     "dyadic maximizes" extremal question as elementary-exchange-smoothing.
  5. Combine: Φ(start) − n·(per-move decrease) ≤ Φ(target) ⟹ L ≤ c(n).
Key lemmas: Lemma G (shared); potential-decrease lemma (undetermined weight choice — the
central open gap); extremal/majorization sub-claim (shared open question with
elementary-exchange-smoothing).
Open gaps: the weight sequence in step 2 is undetermined and the naive choice fails; step
3's "uniform per-move decrease" may not exist as a single clean bound at all (the n=2
exhaustive check shows XY's optimal cut varies qualitatively by LB configuration) — if
so, this approach should be abandoned within 1-2 rounds in favor of the case-split
induction.
Cases to cover: none yet — exploratory at the weight-design stage.
Watch out for: verify Φ isn't a disguised copy of L before investing further; test
candidate weights against the exact n=1,2 game values before trusting any induction step.

concavity-minimax-duality: new
Target: same closed form, reached via continuous convex-analysis: characterize LB's
optimal partition as the maximizer of a concave function g(a) = min over XY's responses
of L(a), via subgradient/KKT stationarity, rather than constructing explicit strategies.
Technique: minimax/concavity (generalizing KB's "Piecewise-concavity smoothing" pattern
from a scalar trig-sum setting to a multivariable simplex setting) + Sion's minimax
theorem for existence.
Skeleton:
  1. Reduce claiming phase via Lemma G (shared).
  2. Fix k=n+1 pieces (using fewer never strictly helps LB — needs its own short proof);
     define g(a) = min over XY's ≤n-cut refinements of L(final multiset) on the simplex.
  3. Prove g is concave: for any fixed combinatorial response pattern of XY, L is affine
     in a; g, as an infimum of affine functions, is concave.
  4. Characterize the maximizer a* via subgradient optimality — at least two of XY's
     response patterns must be simultaneously optimal at a* (else a directional
     perturbation would strictly improve g), and solving the resulting equality-of-slopes
     system is conjectured (from numerics) to force a*_i/a*_{i+1}=2 for all i.
  5. Evaluate g(a*) at the dyadic point (reuse dyadic-cascade-induction's lower-bound
     computation) to recover c(n).
Key lemmas: concavity of g (infimum of affine functions); stationarity-forces-ratio-2
(the central open claim — not yet algebraically derived, only numerically motivated).
Open gaps: step 3's "finitely many combinatorial patterns" claim needs justification (that
XY's optimal response is always at a pattern boundary, not a continuously varying
interior point); step 4's actual stationarity algebra is not carried out at all.
Cases to cover: enumerating XY's finitely-many active response patterns near the
optimum.
Watch out for: this is the highest-risk/most-abstract approach on the table — if step 3's
piecewise-affine structure has infinitely many relevant regions the whole approach
collapses; deprioritize relative to dyadic-cascade-induction unless it shows fast,
concrete progress.

elementary-exchange-smoothing: new
Target: same closed form, reached via an elementary discrete local-exchange (smoothing)
argument directly on LB's partition — the most "IMO-native" and elementary of the four
approaches, proving the dyadic ratio-2 partition is the unique optimum by showing every
other partition admits a strictly improving local mass-shift toward ratio 2.
Technique: extremal/smoothing (KB Problem-Solving Heuristics: perturb an extremal
configuration, derive the necessary condition it must satisfy), combined with Lemma P.
Skeleton:
  1. Reduce claiming phase + Lemma P (shared prerequisites).
  2. Local-pattern-constancy lemma: near a fixed partition a, XY's optimal response
     pattern is locally constant (small perturbations don't cross a region boundary,
     except exactly at ties) — same underlying piecewise-affine structure as
     concavity-minimax-duality step 3, used locally/combinatorially here instead of
     globally/analytically.
  3. Two-piece exchange lemma: for adjacent pieces a_i, a_{i+1}, show that if a_i>2a_{i+1}
     a mass-shift toward ratio 2 strictly raises g(a) (piece i "wastes" mass in the
     pairing-neutralized region), and if a_i<2a_{i+1} a shift the other way strictly
     raises g(a) too (pieces too close ⇒ cheaper direct pairing attack) — both directions
     conjectural, motivated only by the n=2 data point, and are the central open gap.
  4. Conclude: the (compactness-guaranteed) global maximizer has a_i/a_{i+1}=2 for all i,
     i.e. is exactly the dyadic sequence; evaluate to get c(n).
Key lemmas: Lemma G, Lemma P (shared); local-pattern-constancy (plausible,
genericity-style, unproven); two-sided improving-shift lemma (the crux, entirely
conjectural).
Open gaps: step 3 is pure conjecture from a single data point (n=2) — must be numerically
verified for n=3 (fine exact-fraction grid near the dyadic point) before investing in a
full symbolic derivation, to avoid a false lead; step 2's genericity/transversality claim
needs an argument.
Cases to cover: interior stationary point (main case) vs. boundary (fewer than n+1
positive pieces, dispatch with a short separate monotonicity argument).
Watch out for: don't invest in the full symbolic derivation of step 3 until the n=3
numeric check confirms the conjectured two-sided slope claim; this is the approach most
likely to look promising on paper but fail on a case the n=2 data didn't reveal.

Build-set recommendation for outline-reviewer: dyadic-cascade-induction is the most
developed and has concrete, correct, checkable lemmas (G and P) ready to certify
immediately — prioritize it. potential-weighting-upper-bound and
elementary-exchange-smoothing are reasonable parallel hedges on the hard upper-bound step
but should be re-evaluated (and possibly cut) within 1-2 rounds if their central
conjectural claims (uniform potential decrease; two-sided improving shift) don't get
concrete numeric/algebraic support. concavity-minimax-duality is the highest-risk/most
abstract entry — worth one round of investigation into whether the piecewise-affine
structure is genuinely finite, but deprioritize if not.
