## imo-2026-03

greedy-halving-adversary: new
Target: For every positive integer n, prove c(n) = 2^n/(2^{n+1}-1), where c(n) is
the largest value Liu Bang can guarantee.
Technique: Direct/constructive — no induction on n at the top level. (A) an
explicit Xiang Yu strategy ("bisect the current max, n times") proved via a
potential-function/monovariant induction on the number of remaining moves to
cap Liu Bang at ≤ 2^n/(2^{n+1}-1) against ANY Liu Bang marking; (B) the
geometric-ladder construction (pieces 1,2,4,...,2^n scaled) proved via a
superincreasing-sequence domination lemma to guarantee ≥ 2^n/(2^{n+1}-1)
against ANY Xiang Yu response.
Skeleton:
  1. Claiming-subgame reduction: fixed final multiset, greedy-largest-first is
     dominant for both players (exchange/swap argument) — Liu Bang's value =
     sum of odd sorted ranks. Shared lemma across all approaches.
  2. Reformulate as two-stage minimax on piece multisets (Liu Bang picks ≤n
     cuts, Xiang Yu picks ≤n refining cuts).
  3. Xiang Yu's strategy: bisect current max piece, n times.
  4. Potential-function induction (on remaining Xiang Yu moves j, with
     invariant tying current-max-normalized Φ to 2^j/(2^{j+1}-1)) shows this
     strategy caps Liu Bang at ≤ 2^n/(2^{n+1}-1) for ANY starting config —
     OPEN GAP, charging scheme for how vacated slots interact with the rest
     of the multiset not yet nailed down.
  5. Ladder construction: n points, pieces 2^i/(2^{n+1}-1), i=0..n.
  6. Superincreasing domination lemma: for any refinement of a superincreasing
     sequence, Σ_odd-rank ≥ top term — induction on k, peeling L_1, handles
     the case Xiang Yu splits L_1 itself (open sub-gap).
  7. Combine both directions to get exact value; check n=1 (2/3).
Key lemmas (claim + mechanism):
  - Claiming-subgame value = sum of odd sorted ranks — because deviating from
    "take current max" is weakly dominated by a pairwise swap argument
    (payoffs additive, no cross-term besides which pieces remain).
  - Superincreasing sequences dominate refinements by their top term —
    because the sum of ALL strictly-smaller original pieces is < top term
    regardless of how finely subdivided.
  - Bisect-the-max caps Liu Bang — via potential-function induction on
    remaining moves (mechanism not yet fully derived — the actual open gap).
Open gaps: Step 4's charging-scheme induction (the crux of the whole proof);
Step 6's case where Xiang Yu splits the ladder's largest piece itself;
confirming "bisect current max" only needs to be SUFFICIENT (not provably
optimal) since the matching lower bound already pins the value.
Cases to cover: none beyond upper/lower bound; Step 4 may need sub-cases on
tie-breaking among equal max pieces.
Watch out for: tie-breaking among tied max pieces during Xiang Yu's bisection
sequence; Step 6 must handle Xiang Yu cutting the ladder pieces at arbitrary
(non-bisecting) points, not just exact halves; both players may use FEWER
than n points ("at most n" in the problem statement) — both directions must
allow for this.

induction-first-move-reduction: new
Target: Same as above — prove c(n) = 2^n/(2^{n+1}-1) for all n.
Technique: Strong induction directly on n via a "first-move reduction": Liu
Bang's first cut peels off a piece of the target size, reducing the
(n)-instance to the (n-1)-instance on the rescaled remainder, closed with IH.
Genuinely different top-level architecture from a single global invariant —
this is a self-similarity/recursive-value argument, not a static
potential-function proof.
Skeleton:
  1. Import the shared claiming-subgame reduction lemma (Step 1 of
     greedy-halving-adversary; reuse via lemmas/ once certified).
  2. Base case n=1: c(1)=2/3, proved by hand (all three explorers agree,
     x=1/3 optimal for Liu Bang).
  3. Inductive hypothesis: c(n-1) = 2^{n-1}/(2^n-1), both directions proved.
  4. Lower bound: Liu Bang peels off piece p = 2^n/(2^{n+1}-1), recurses with
     the (n-1)-ladder on the remainder (1-p rescaled). Need: Xiang Yu cannot
     profitably attack the peeled piece p instead of only playing in the
     remainder (an exchange/domination argument transplanting Xiang Yu's
     cuts) — open gap.
  5. Upper bound: symmetric recursive spoiling strategy for Xiang Yu — NOT
     pinned down; arbitrary Liu Bang markings don't hand Xiang Yu a clean
     "one piece = p, rest = remainder" structure to recurse on. Largest open
     gap in this approach.
  6. Solve the recursion c(n) = p + c(n-1)(1-p) — VERIFIED ARITHMETICALLY
     FALSE: for n=2, p=4/7, c(1)=2/3, p + c(1)(1-p) = 6/7 ≠ 4/7 = c(2)
     (computed exactly via fractions). The naive linear peel-recursion is
     REFUTED; the correct recursive relation (if one exists at all) must be
     rederived, likely via a different induction variable or a stronger
     multi-parameter inductive statement, not a literal "first piece is
     exactly p, remainder inherits c(n-1) verbatim" claim.
Key lemmas: claiming-subgame value formula (shared); recursive self-similarity
of the ladder under rescaling (true structurally, but the value recursion
built on it as stated is false — see Step 6).
Open gaps: Step 4 (protect-the-first-piece exchange argument); Step 5 (no
recursive spoiling strategy identified at all — the harder direction); Step 6
(the literal recursion is disproved by direct computation — this is a
concrete, confirmed obstruction, not just an unfilled gap).
Cases to cover: base case n=1 (done); general inductive step (open, both
directions, and the recursion itself needs repair).
Watch out for: do not let the builder paper over the Step 6 arithmetic
mismatch (2^n + 2^{n-1} ≠ 2^n) with hand-waving. If no correct recursion
is found within a round, report this approach as refuted/stuck rather than
force a false step through.

smoothing-compactness-certificate: new
Target: Same as above — prove c(n) = 2^n/(2^{n+1}-1) for all n.
Technique: Static optimization / smoothing (majorization-style) argument.
Treat the two-stage minimax as optimization over a compact configuration
space; show via compactness (Weierstrass) that an optimal Liu Bang config
exists, then via a local-exchange/perturbation ("smoothing") lemma that any
non-ladder-shaped configuration can be strictly improved, forcing the unique
extremizer to be the geometric ladder, then evaluate the value there directly
using lemmas shared with greedy-halving-adversary. This is a genuinely
different top-level target (identify-the-unique-extremizer-by-perturbation
vs. exhibit-explicit-strategies-and-bound-them), useful as a rival framing in
case the direct potential-function argument (approach 1) stalls.
Skeleton:
  1. Import shared claiming-subgame reduction lemma.
  2. Compactness: Liu Bang's / Xiang Yu's configuration spaces are compact,
     Φ is continuous and piecewise-linear (finitely many combinatorial-type
     cells determined by linear inequalities on cut positions), so max_L
     min_X Φ is attained (Weierstrass extreme value theorem).
  3. Local-exchange/smoothing lemma (KEY, UNPROVEN): any configuration not
     "ladder-related" (pairwise ratios not all in {1,2,4,...}) can be
     perturbed to strictly improve the maximizer's value, via a directional-
     derivative computation on the piecewise-linear value function. This is
     the technical heart, currently open with no derived mechanism — the
     highest-risk gap of the three approaches on the table.
  4. Conclude maximizer is (up to normalization) the ladder; separately show
     using all n points weakly dominates fewer (open sub-gap).
  5. Evaluate Φ at the ladder directly (reuses superincreasing-domination +
     bisection-response lemmas from greedy-halving-adversary — shareable).
  6. Conclude c(n) = 2^n/(2^{n+1}-1).
Key lemmas: piecewise-linearity/compactness of the minimax value (mechanism:
finitely many linear cells + Weierstrass); smoothing toward 2:1 ratios
strictly helps the maximizer (mechanism NOT YET FOUND — flagged explicitly as
the central open gap, no explorer attempted this).
Open gaps: Step 3 (smoothing lemma, entirely open — recommend testing on the
n=2 case by hand/computer algebra as a quick feasibility check before
committing further builder effort); Step 4's "all n points weakly dominate
fewer" sub-claim; Step 5 overlaps with greedy-halving-adversary and can share
lemmas once either is certified.
Cases to cover: interior vs. boundary configurations (some piece length → 0,
i.e. Liu Bang using fewer than n points) in the perturbation argument.
Watch out for: real risk this approach collapses into a heavier restatement
of greedy-halving-adversary if Step 3 can't be closed with a genuinely
different mechanism from the potential-function argument. If after one round
Step 3 shows no concrete, distinct progress, the outline-reviewer/next-round
outliner should deprioritize this in favor of the other two rather than
continue funding it — flagged here so the reviewer can watch for that signal
without waiting a full 3-round plateau.

Summary / rationale for the reviewer: all three approaches share the (already
solid) claiming-subgame reduction lemma and the geometric-ladder construction
target value 2^n/(2^{n+1}-1) (numerically confirmed by all three explorers
for n=1,2,3 and analytically proved for n=1). They differ genuinely in HOW
they attack the hard, unproven upper-bound-for-arbitrary-Liu-Bang-marking
direction: (1) explicit adversary strategy + potential function (most
concrete, recommend as primary build target this round), (2) induction on n
via first-move peeling (interesting but has a CONFIRMED arithmetic
obstruction in its naive form — needs real repair before it can proceed, so
treat as higher-risk / needs-rethink-first), (3) static smoothing/compactness
argument (most conceptual but least derisked — no mechanism found yet for
the core lemma). Recommend the outline-reviewer prioritize builder effort on
(1)'s Step 4 potential-function gap and (1)'s Step 6 superincreasing-lemma
gap as the highest-value target this round, with (2) needing a rethink of
its recursion before further building, and (3) worth a light feasibility
probe (e.g. hand-check n=2 local optimality) before heavier investment.
