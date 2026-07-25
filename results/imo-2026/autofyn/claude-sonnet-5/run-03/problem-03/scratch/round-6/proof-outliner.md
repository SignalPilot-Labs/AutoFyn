## imo-2026-03

self-similar-induction-on-n: revise
Target: c(n) = 2^n/(2^{n+1}-1) — this approach owns the LOWER-BOUND direction:
LB's geometric partition achieves ≥ c(n) against every XY refinement.
Technique: self-similar peeling induction on the number of top-level cuts,
now generalized to track an EXTRA FREE PARAMETER (target value V, not fixed
at 2^m) through the existing G(m,k;V) machinery introduced round 4.
Skeleton:
  1. (already certified) Peeling Lemma + Companion Peeling Lemma + Lemma B
     reduce T(m,k)=G(m,k;2^m) to peel-the-max induction.
  2. (already certified, Theorem 2) Case-B(m,k) closed for max(B) outside
     the width-1 sliver (2^{m-1}-1, 2^{m-1}) via a direct extremal argument
     (closed-form B*).
  3. NEW — prove Theorem 2': the parametrized statement G(m,k;V) for
     V = 2^{m-1}+eps, eps∈(0,1) (i.e. the sliver reduced target), by
     applying the SAME tail-untouched dichotomy recursively one level down:
     split the residual B' by its own top fragment b1' vs max(T)=2^{m-2},
     landing on a strictly smaller instance of G(m-1,·;V') with
     V'=2^{m-2}+eps (halved eps, one level down) — a genuine induction on m,
     not a flat single-shot bound.
  4. Prove the margin is exactly linear: OddSum(B'∪T) ≥ 2^(m-1) + eps/2,
     matching this round's numeric conjecture (exact to 6 decimals at
     m=4,5,6). The mechanism: at each recursive level the "excess" eps
     entering the level-m dichotomy is exactly halved (mirrors how B*
     itself splits one geometric level's mass in half at the boundary
     eps=0 case) — so unrolling the recursion k levels gives a geometric
     series with ratio 1/2, summing to the observed eps/2 margin in the limit.
  5. NEW (second target, same machinery, different regime) — attempt the
     general middle regime μ ≤ b1 < 2^{m-1} (round-4 trichotomy's harder
     case) as a further instance of G(m,k;V) with V determined by the
     Companion-Peel reduction on S (not yet carried out by anyone) — lower
     priority than step 3-4 this round; state the reduction explicitly even
     if not fully closed.
Key lemmas (claim + mechanism):
  - Theorem 2' (parametrized sliver closure): OddSum(B'∪T) ≥ 2^(m-1)+eps/2
    for eps∈(0,1) — because the extremal minimizer is an exact scaled echo
    of B* one recursion level down (numerically confirmed extremal shape:
    geometric run down to level q, bottom two entries tied at (2^{q-1}+eps)/2),
    so the SAME two-sub-case dichotomy that proved Theorem 2 applies
    recursively to B' itself with target V=2^(m-1)+eps instead of 2^(m-1).
  - G(m,k;V) linearity in V near V=2^(m-1): margin(V) is affine in
    (V - 2^(m-1)) — because each peeling step's slack contributes additively
    and the recursion's ratio is exactly 1/2 (companion-peel halves the
    residual excess at each level).
Open gaps: Theorem 2' itself (currently only a clean numeric conjecture, not
proved) is the deliverable this round. The general middle regime (step 5) and
the Leftover-Fragment Obstruction (owned by greedy-reduction-geometric, but
same G(m,k;V)-style fix) remain open after this round even if Theorem 2' closes.
Cases to cover: eps ∈ (0,1) continuum — the proof must be a genuine induction
on m/recursion depth, not case-split on eps value.
Watch out for: the recursive dichotomy must re-verify the SAME three-way-tie
edge cases (per the standing memory rule) at each new recursion level, not
just at the top; do not assume the eps/2 pattern extrapolates from m=4,5,6
numerics without an actual induction proof — round 5's Two-Level Half-Bound
Lemma looked plausible numerically too and failed.

greedy-reduction-geometric: revise
Target: c(n) = 2^n/(2^{n+1}-1), lower-bound direction, general Case 2 (top
piece AND tail cut simultaneously).
Technique: Dominance-Chain induction (Lemma 8 + Theorem 7), extended with an
explicit extra leftover-mass parameter L, mirroring self-similar-induction-on-n's
V-parametrization — apply the SAME cross-approach idea the lower-bound
explorer identified (the three open lower-bound regions all reduce to
tracking one extra free parameter through the peeling machinery).
Skeleton:
  1. (already certified) Theorem 7 closes the "top-levels-clear" joint case:
     Dominance-Chain split b1≥...≥bk of ≤2^m, refinement S of Γ_{m-1} with
     top k levels entirely unsplit — OddSum(B∪S) ≥ Σbi.
  2. NEW — Theorem 7'(m,k;L): allow the top tail level (level 2^{m-1}, the
     first one Theorem 7 required untouched) to be split into (μ1, rest)
     where rest sums to L=2^{m-1}-μ1 and rest's own further splitting is
     ARBITRARY (any shape) — prove OddSum degrades by at most a controlled,
     conjecturally-linear function of L relative to the L=0 (Theorem 7)
     baseline.
  3. Mechanism: peel b1, then peel μ1 (the surviving top fragment of the
     split level) as the new global max — Companion Peeling Lemma pairs μ1
     against the rest of the top level's fragments plus lower levels; the
     residual after these two peels is a smaller instance carrying leftover
     mass L, which the induction must absorb rather than discard (this is
     exactly where the plain Theorem 7 argument broke — it implicitly
     assumed L=0).
  4. Close the fully general joint Case 2 by combining Theorem 7'(m,k;L)
     with Theorem 2'/G(m,k;V) from self-similar-induction-on-n (import as a
     certified lemma once proved there) — the interleaved case is precisely
     the composition of "top piece split" (V-parametrization) and "top tail
     level split" (L-parametrization) simultaneously.
Key lemmas (claim + mechanism):
  - Theorem 7'(m,k;L): OddSum(B∪S) ≥ Σbi − f(L) for some controlled f,
    conjecturally f(L) linear in L — because peeling μ1 (the new max after
    b1) via Companion Peeling produces a residual identical in shape to
    Theorem 7's induction hypothesis but with target reduced by exactly the
    mass diverted into "rest," which by the same halving mechanism as
    Theorem 2' contributes a bounded, shrinking correction.
Open gaps: Theorem 7'(m,k;L) is not yet stated in exact closed form (unlike
self-similar-induction-on-n's eps/2 conjecture, no numeric target for f(L)
has been computed yet this round) — first task for the builder is to
numerically pin down f(L)'s exact form (small m, sweep L) before attempting
the proof, exactly as the lower-bound explorer did for Theorem 2'.
Cases to cover: L ∈ (0, 2^{m-1}) continuum, plus the boundary L=0 (must
recover Theorem 7 exactly) and L→2^{m-1} (top level fully split, degenerates
toward the general middle regime — flag if it coincides with self-similar-
induction-on-n's step 5 target, in which case merge effort there instead of
duplicating).
Watch out for: do not let this become a second independent proof of the same
"extra parameter" lemma self-similar-induction-on-n is proving — if the
builder finds Theorem 7'(m,k;L) is literally the same statement as G(m,k;V)
under a variable rename, STOP and import instead of re-deriving (per the
standing memory rule on shared-crux assignment).

universal-halving-adversary: revise
Target: c(n) = 2^n/(2^{n+1}-1), upper-bound direction, "large gaps
everywhere" balanced-region sub-case (the region Anchor-Merge does not cover).
Technique: adaptive two-piece-split existence argument (NOT a single
closed-form rule) — retarget away from finding one universal formula, per
this round's upper-bound explorer finding that the merge-chain / single-rule
family is exhaustively refuted, and toward proving existence of SOME good
2-piece response using the LP-vertex machinery.
Skeleton:
  1. (already certified) Anchor-Merge Lemma closes the sub-case with some
     consecutive gap gi ≤ 1/(2^{n+1}-1).
  2. NEW — prove the Two-Piece-Split Vertex Lemma: the mechanical
     generalization of lp-duality-split-polytope's certified Single-Piece-
     Split Vertex Lemma to two simultaneously-split pieces (i,j): the
     minimum OddSum over all ≤n-cut splits of pi and pj jointly (all other
     pieces fixed) is attained at a finite vertex set (each new fragment
     either 0, tied to another fragment, or tied to a fixed untouched
     piece) — same LP active-constraint argument, one more free pair of
     dimensions.
  3. NEW — Existence Theorem: for every balanced partition (p1<1/2,
     p_{n+1}>1/(2^{n+1}-1)) with no small consecutive gap (Anchor-Merge
     inapplicable), SOME pair (i,j) achieves OddSum ≤ c(n) via the Two-
     Piece-Split Vertex Lemma's finite candidate set — proved via a
     covering/counting argument over the O(n^2) candidate pairs (not a
     closed-form single choice), using the 25/25 random-instance numeric
     evidence (winning response is overwhelmingly (top,2nd) or (top,bottom),
     2 pieces, 1 cut each) to motivate which candidate pairs to prioritize
     checking first.
Key lemmas (claim + mechanism):
  - Two-Piece-Split Vertex Lemma — because the LP feasible region for
    2-piece splits is still a polytope (linear constraints: fragment sums
    fixed, nonnegativity) and OddSum restricted to it is piecewise-linear
    (rank order changes at finitely many hyperplanes), so the minimum is at
    a vertex, exactly as in the 1-piece case.
  - Existence Theorem — because the merge-chain negative result shows NO
    single fixed rule works, but the vertex lemma converts "does some pair
    work" into a finite check per instance; the proof must show the finite
    vertex candidate set is non-empty of good candidates for every
    partition shape, likely via a case split on which pair is "closest to
    the (top,2nd)/(top,bottom) pattern" the numerics favor.
Open gaps: the Existence Theorem is the deliverable — currently only
supported by 25/25 random numeric evidence, no proof. The known Multi-Piece
Necessity instances (n=3,4 triangular family, owned by lp-duality-split-
polytope) are exactly the test cases this Existence Theorem must handle
(both ARE closable by 2-piece responses per lp-duality-split-polytope's
file, so they are consistent, not counterexamples — verify this explicitly
first).
Cases to cover: which pair (i,j) is optimal may depend on partition shape;
enumerate at least the (top,2nd), (top,bottom), (2nd,3rd)-adjacent-pair
families as the primary candidates before falling back to full O(n^2) search.
Watch out for: per this round's cheap-kill finding, do NOT re-attempt any
single fixed-rule merge/split heuristic (two-largest, largest-smallest,
closest-pair, bisect-smallest-only) as the closing mechanism — all
exhaustively refuted. The existence argument must genuinely be "some pair
among several works," not one universal formula.

lp-duality-split-polytope: advance
Target: c(n) = 2^n/(2^{n+1}-1), upper-bound direction — owns the Multi-Piece
Necessity results and the underlying vertex machinery that
universal-halving-adversary's revision above will directly build on.
Technique: LP-vertex/active-constraint characterization of XY's optimal
response, extended from single-piece (certified) toward proving the general
Multi-Piece Necessity pattern for the triangular family at general n.
Skeleton (continue from current file):
  1. (already certified) Single-Piece-Split Vertex Lemma.
  2. (already certified) Multi-Piece Necessity instances at n=3,4 for the
     triangular partition family (1/3,4/15,1/5,2/15,1/15)-style, single-
     piece floor exceeds c(n).
  3. NEW — generalize the triangular family's landmark structure
     (arithmetic-progression-like, q_i ∝ n+2-i) to general n and prove the
     single-piece floor exceeds c(n) for all n≥3 via the Single-Piece-Split
     Vertex Lemma's finite candidate set applied symbolically (not per
     instance) — closed form in n, per the explorer's flagged "natural next
     step, not attempted due to time" note.
  4. Cross-supply the Two-Piece-Split Vertex Lemma (if universal-halving-
     adversary's builder needs it first) — this is the SAME LP-vertex
     mechanism this approach already owns; coordinate so only one slug
     proves it and the other imports.
Key lemmas: as in current file, plus the general-n Multi-Piece Necessity
Theorem (mechanism: the finite vertex candidate set for a single split of
piece idx, evaluated symbolically across the triangular family's exact
arithmetic-progression structure, gives a closed-form floor value
comparable to c(n) via a direct algebraic inequality).
Open gaps: general-n Multi-Piece Necessity Theorem; possible Two-Piece-Split
Vertex Lemma (coordinate with universal-halving-adversary to avoid duplicate
proof per the standing shared-crux rule).
Cases to cover: general n≥3 for the triangular family; note the certified
n=2 exception ((0.35,0.34,0.31)-style instances ARE single-piece-closable)
must remain consistent — the general theorem should predict n≥3 only.
Watch out for: don't let this and universal-halving-adversary duplicate the
Two-Piece-Split Vertex Lemma proof — assign it to whichever builder starts
first this round and have the other import once certified.

dyadic-potential-invariant: advance
Target: c(n) = 2^n/(2^{n+1}-1), upper-bound direction — the balanced-region
"finite characterization of the optimum" tool, now the natural home for the
fresh-framing explorer's flagged majorization/suffix-domination lead.
Technique: Vertex Pinning Lemma (LP-vertex active-constraint counting,
already certified) — this round, spend the FIRST effort on a cheap
feasibility check of the majorization/suffix-domination monotonicity claim
(aimo-0287-style) before committing further proof effort to it.
Skeleton:
  1. (already certified) Vertex Pinning Lemma: at XY's optimum, ≥ Σmi
     independent exact ties are active.
  2. NEW (cheap check, do first) — numerically test the candidate
     monotonicity lemma "M ⪯ M' (suffix-domination: |M∩[i,n]| ≤ |M'∩[i,n]|
     for every suffix) implies OddSum(M) ≤ OddSum(M')" on random refinement
     multisets. Per the fresh-framing explorer's honest caveat, this is
     UNVERIFIED and OddSum is a fixed-parity-of-rank sum (not a chosen
     subset sum), so the aimo-0287 analogy may not transfer — if it fails
     on random tests, record as a dead end immediately and do NOT build
     further on it this round.
  3. IF the monotonicity lemma survives the cheap check: use it plus an
     incomparability/exchange argument (in the style of aimo-0287's proof)
     to force XY's true optimum into a small ⪯-extremal candidate family,
     narrowing the balanced-region search space — a genuinely different
     proof mechanism from LP-vertex enumeration (combinatorial rank-
     domination order vs. linear-algebra active-constraint counting).
  4. IF it fails: fall back to using the Vertex Pinning Lemma directly as a
     supporting tool for universal-halving-adversary's Existence Theorem
     (step 2/3 above) — i.e. this approach's positive tool feeds the
     revised universal-halving-adversary target rather than closing the
     gap independently.
Key lemmas (claim + mechanism):
  - Suffix-domination monotonicity (UNVERIFIED, test first) — analogy: in
    aimo-0287, Σ_X a ≤ Σ_Y a for X ⪯ Y under any increasing sequence a,
    because suffix-domination controls how much "large-index mass" each
    set carries; here it's speculative since OddSum picks alternating RANKS
    of a single sorted multiset, not a subset sum of a fixed sequence — the
    mechanism may not transfer at all.
Open gaps: the entire majorization mechanism is a lead, not a proof — must
survive the cheap numeric check before any further proof effort. Vertex
Pinning Lemma alone still does not close the outer maximization.
Cases to cover: none yet — this round's deliverable is the feasibility
verdict (kill or keep) plus, if it survives, a first attempt at the
exchange argument.
Watch out for: per the standing memory rule, do NOT let this unverified
"dual"/analogy-borrowed lemma get written into Current Best as a target
without the numeric stress test happening FIRST, in this same round, before
any proof narrative is built on it.

layer-cake-parity-reframing: retire (formally deprioritize, not rebuilt)
Rationale: the fresh-framing explorer's dedicated audit this round confirms
its unique content (layer-cake identity, per-piece additivity, T(n) ⟺
AltSum ≥ 1 reduction) is strictly subsumed by self-similar-induction-on-n's
independently-proved Lemma AS + the strictly more general Single-Insertion
Lemma (which handles arbitrary single-value insertion at any position, not
just whole-piece bisection, and is the actual engine behind this round's
Theorem 2/Theorem 2' work). Its proved Coupling Obstruction blocks only the
"independent per-cut, piece-local bound" mechanism, which no live approach
is using. Do not dispatch a builder to it this round. Its 4 certified
lemmas remain importable by any approach that later needs the threshold/
measure viewpoint specifically (e.g. if the balanced-region gap turns out
to need a measure-theoretic argument). If it accumulates a 3rd idle round
with no new lead touching it, treat as fully retired in the population
(kept on disk as a certified-lemma source, no longer sampled for building).

## Build set this round (recommended)
self-similar-induction-on-n, greedy-reduction-geometric,
universal-halving-adversary, lp-duality-split-polytope,
dyadic-potential-invariant.
(layer-cake-parity-reframing excluded — formally deprioritized this round
per fresh-framing explorer's audit; not a new approach, no 6th builder slot.)

## Diversity check (single-gap-trap guard)
Two genuinely distinct top-level gaps remain, and the field splits cleanly
across them without collapsing to one shared wall:
- LOWER bound (self-similar-induction-on-n, greedy-reduction-geometric):
  both now use the SAME underlying extra-parameter-through-peeling-induction
  idea (V for self-similar, L for greedy) — this is intentional convergence
  on a cross-approach unification the explorer found, not an accidental
  duplication; they attack different sub-regions (sliver/middle-regime vs.
  interleaved joint case) and are told explicitly to import from each other
  rather than re-derive if the parametrizations turn out identical.
- UPPER bound (universal-halving-adversary, lp-duality-split-polytope,
  dyadic-potential-invariant): three approaches on the same split-fragment-
  polytope object, flagged as a plateau watch since round 5. This round
  redirects them to three DIFFERENT sub-tasks on that object: (i)
  universal-halving-adversary proves existence via 2-piece vertex search,
  (ii) lp-duality-split-polytope proves the general-n necessity theorem
  (a negative/structural result, complementary not competing), (iii)
  dyadic-potential-invariant tries a genuinely different mechanism
  (majorization/exchange, not LP-vertex) as a first cheap check — if it
  survives, this becomes the field's first non-LP-vertex mechanism on the
  balanced region, breaking the 3-approach-same-object plateau for real.
