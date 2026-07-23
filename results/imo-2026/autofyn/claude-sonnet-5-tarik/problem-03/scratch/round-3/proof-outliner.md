## imo-2026-03

dyadic-cascade-induction: revise
Target: c(n) = 2^n/(2^{n+1}-1) for all positive integers n, BOTH directions (upper bound: XY
can always force LB ≤ c(n); lower bound: LB's dyadic construction guarantees ≥ c(n)).
Technique: strong induction on level m (= number of cuts used), carrying the recursion
e_m = e_{m-1}/(2+e_{m-1}) via Lemma G (greedy/order-statistic reduction) + Lemma P
(duplicate-pair invariance of e=L-X); explicit case-split casework (Case i/ii) for the upper
bound, now extended with a dominance/superincreasing-lock case split (Branch A/B) for the
lower bound.
Skeleton:
  1. Reduce the claiming phase via Lemma G (certified, imported) — problem becomes: LB
     picks ≤n+1 pieces summing to 1, XY responds with ≤n further cuts, minimize e=L-X.
  2. Induction on level m: Case (i) a_1≥2a_2 — XY bisects a_1, Lemma P zeroes the resulting
     pair exactly, residual is a level-(m-1) instance. Case (ii) a_1<2a_2 — genuinely harder,
     needs a mechanism beyond top-two matching (see potential-weighting-upper-bound).
  3. NEW this round (§2d): Case (i)'s top-level form-A bound (e≤e_m·S) now closes for
     ALL m via 1-variable calculus (crossing point of e_{m-1}(1-a_1) and a_1/2^m, exactly at
     the dyadic a_1* = 2^m/(2^{m+1}-1)) — replaces the old n=2-only exact-2-element-residual
     trick with a strictly more general argument. Verified numerically/algebraically for
     m=1..6 by this round's general-n explorer; needs formal write-up.
  4. NEW this round (§5): Lower-bound skeleton via the dominance/superincreasing lock. D_m's
     top piece a_1=2^m/(2^{m+1}-1) strictly exceeds the sum of all other pieces (elementary
     superincreasing identity 2^k>2^k-1). Split XY's response to the dyadic input into
     Branch A ("a_1 untouched" — locks a_1 at rank 1 forever, numerically confirmed hopeless
     for XY, e≈2/7 vs target 1/7 at m=2) vs. Branch B ("a_1 is cut" — by the vertex lemma,
     bisecting a_1 reduces via Lemma P exactly to the level-(m-1) lower-bound problem on the
     residual, which IS a rescaled copy of D_{m-1}).
Key lemmas (claim + mechanism):
  - Lemma G, Lemma P — certified, imported, no re-derivation needed.
  - Case (i) general-m closure — because combining IH form A and form B on the residual
    (their min, since both hold) and maximizing over LB's choice of a_2≤a_1/2 gives a pure
    1-variable crossing-point problem whose solution is exactly the dyadic a_1.
  - Dominance lock (new) — because D_m is superincreasing, no combination of XY's cuts to the
    residual can ever displace a_1 from rank 1 if a_1 itself is untouched — a genuine
    two-sided (not just sufficient) case split for the lower-bound direction specifically.
  - Bisection-dominates-on-a_1 (new, unproved) — conjectured: among all tie/match choices for
    XY's cut on a_1 in Branch B, bisecting is XY's best option; this is the one piece of real
    new content the lower-bound direction needs and has NOT been attempted anywhere yet.
Open gaps: (1) §2d needs formal write-up (verified computation, not yet a hand proof in the
file); (2) §5 Step 5a/5b (dominance lock formalization, Branch A bound) — elementary, should
close quickly; (3) §5 Step 5c's "bisection dominates" sub-claim — genuinely new, unattempted;
(4) Case (ii) at general m explicitly handed off to potential-weighting-upper-bound (do not
re-attempt the failed two-candidate casework here).
Cases to cover: Case (i) a_1≥2a_2 (upper bound, closed for all m via §2d); Case (ii) a_1<2a_2
(upper bound, closed only at n=2, general m open — see potential-weighting-upper-bound);
Branch A (a_1 untouched, lower bound, should close quickly) vs Branch B (a_1 cut, lower
bound, genuine open content).
Watch out for: do not re-extend the n=2-specific exact-2-element-residual trick to n≥3 (now
confirmed unnecessary — §2d supersedes it); do not conflate "XY has a sufficient strategy
achieving e≤e_m·S" (upper bound, existential over XY) with "no XY strategy beats e_m at the
dyadic point" (lower bound, universal over XY) — these are logically independent, confirmed
by the lowerbound explorer (strategy-stealing does NOT work as a shortcut between them).

potential-weighting-upper-bound: revise (un-benched — no longer redundant)
Target: same c(n) = 2^n/(2^{n+1}-1), specifically targeting the general-m closure of Case
(ii) (a_1<2a_2) of the upper-bound direction, which dyadic-cascade-induction's two-candidate
casework is now CONFIRMED unable to reach for m≥3.
Technique: potential/invariant argument (KB "Invariants & monovariants"), reframed this round
as a gap-decomposition + greedy pairing mechanism over the WHOLE multiset at once (not just
the top two pieces), replacing the abandoned round-1 "undetermined weight sequence" idea.
Skeleton:
  1. Reduce via Lemma G (certified, imported).
  2. Exact identity: e(M) = Σ_{i odd}(a_i - a_{i+1}) (telescoping the alternating sum) —
     exposes e as a sum of "gaps" between rank-adjacent pieces at odd positions.
  3. Formalize "one cut zeroes one gap-term": splitting a piece to tie another piece's value
     collapses the corresponding gap via Lemma P (vertex lemma already certified elsewhere).
  4. Conjecture (open, central gap): a greedy rule — close gaps in order of weighted value
     matching the dyadic 2^{-i} decay, recursing on the residual with one fewer cut — whose
     worst case over all LB openings is exactly the dyadic sequence.
  5. Sanity checks (bounded, do FIRST): verify the greedy rule reproduces the certified n=2
     answer (1/7, all four sign regimes) and the correct near-zero value at the m=3
     near-uniform counterexample (1/3,1/3,1/3) — this is the specific point that killed the
     old two-candidate approach (XY bisects any ONE piece there, creating TWO simultaneous
     duplicate pairs via Lemma P, reaching e=0 with 1 of 3 cuts — a "whole-multiset" effect
     the top-two-only view cannot see).
Key lemmas (claim + mechanism):
  - Gap-decomposition identity — trivial telescoping algebra, but the right reformulation to
    expose whole-multiset pairing structure.
  - Greedy weighted-gap-priority rule (unproved, central gap) — because D_m is exactly the
    configuration where every gap is simultaneously "tight" in the ratio-2 sense, so no
    single gap dominates enough to make prioritizing it (over the recursive residual
    argument) suboptimal for XY; general-m LB openings that deviate from this ratio should
    let XY find a strictly better (non-top-two) gap to close first.
Open gaps: the greedy rule itself (item 4) is entirely open — this is the one substantive new
mathematical content needed. Everything else (Lemma G, Lemma P, the gap identity) is
certified or trivial.
Cases to cover: none pre-determined — the point of the greedy mechanism is to avoid a hand
sign-regime split; if it needs its own casework, discover it live rather than guessing.
Watch out for: verify against the m=3 near-uniform counterexample FIRST (cheap, bounded)
before attempting any general-m argument — this is the confirmed failure point of the prior
mechanism and the correct stress test for any replacement.

concavity-minimax-duality: revise (revived — genuinely different framing, no longer
deprioritized)
Target: same c(n) = 2^n/(2^{n+1}-1), specifically a casework-free proof of the ENTIRE n=2
upper-bound direction via global concavity of the value function g(a), combined with
elementary-exchange-smoothing's already-certified local result.
Technique: convex analysis — global concavity of a Stackelberg (sequential, not simultaneous)
game's value function, replacing dyadic-cascade-induction's explicit sign-regime casework
with one convexity lemma. Numerically well-supported this round (0 violations across 34 test
pairs at n=2, including boundary-straddling pairs) but the file's OLD Step 3 justification
("min of affine functions is concave") is confirmed logically unsound (each XY strategy's
formula is only affine within its own sorted-order sub-region, not globally) — needs a
genuinely correct proof, not a discard of the underlying (numerically-supported) claim.
Skeleton:
  1. Reduce via Lemma G (certified, imported).
  2. Import elementary-exchange-smoothing's Step A (tie-or-degenerate lemma) and Step C
     (local certificate λ=(2/7,1/7,4/7): (4/7,2/7,1/7) is a strict LOCAL maximizer of g in a
     neighborhood inside Case (ii), conditional on g(dyadic)=1/7) — do not re-derive.
  3. NEW correct mechanism for global concavity (replaces the unsound old Step 3): an
     adjacent-regime concave-kink check — at each of the finitely many breakpoints between
     dyadic-cascade-induction's already-computed exact sign sub-regimes, verify the slope of
     g decreases when crossing from smaller- to larger-coordinate side, using the exact
     formulas already on file. Converts "global concavity" into finitely many local slope
     comparisons at known breakpoints.
  4. Cheap gate FIRST: run a denser/adversarial (not random) numerical search for a
     concavity violation at points straddling each of the four regime boundaries closely on
     both sides, before investing in Step 3's proof.
  5. If Step 3 succeeds: "a concave function's strict local max is its unique global max"
     (standard convex analysis) promotes Step 2's local result to the ENTIRE n=2 upper bound
     in one shot.
Key lemmas (claim + mechanism):
  - Global concavity of g (central open gap) — conjectured, needs the adjacent-regime
    concave-kink argument, not the old unsound "min of affine functions" claim.
  - Concave-local-max-is-global-max — standard convex analysis fact, the promotion mechanism.
  - elementary-exchange-smoothing's certificate — imported directly.
Open gaps: Step 3 (correct global concavity proof) is the entire remaining content; Step 4's
denser numerical gate has not yet been run (only coarse random sampling so far); n≥3
concavity is explicitly unconfirmed (a possible sampler artifact, not resolved) — do not
extend to n≥3 yet. Even on success, this closes only the upper bound at n=2; the lower-bound
import (g(dyadic)=1/7) remains a separate shared gap.
Cases to cover: the finitely many sign sub-regimes dyadic-cascade-induction already computed
(four in Case ii, plus the Case i/ii boundary) — Step 3 needs a slope check at each pairwise
boundary, not fresh case discovery.
Watch out for: DROP the old Sion's-minimax-theorem invocation entirely — confirmed this round
to be a red herring (this is a sequential/Stackelberg game, not simultaneous zero-sum; no
minimax order-swap is needed or applicable, existence of the value follows from ordinary
compactness + upper semicontinuity). If Step 4's numerical gate finds a real violation,
abandon this approach immediately rather than patching around it.

elementary-exchange-smoothing: advance
Target: same c(n) = 2^n/(2^{n+1}-1); this approach's own scope is the n=2, Case (ii) local-
uniqueness result near the dyadic point, via a concave-min-of-3-affine-functions gradient-
hull certificate.
Technique: convex analysis (finite min of affine functions is concave; 0 in the strict
interior of the active gradient hull ⟹ strict local max), certified this population's only
working concrete convexity certificate (λ=(2/7,1/7,4/7)).
Skeleton: unchanged from its existing file — Step A (tie-or-degenerate lemma, proved), Step B
(explicit n=2 Case (ii) candidate formulas f1,f2,f3, hand-derived and cross-checked), Step C
(gradient-hull certificate proving strict local uniqueness in a neighborhood).
Key lemmas: Step A's tie-or-degenerate lemma (proved, general, reusable — already imported
by concavity-minimax-duality above); Step C's gradient-hull criterion (proved for the
specific λ=(2/7,1/7,4/7), directly reusable by concavity-minimax-duality's Step 2 import).
Open gaps (unchanged, its own next targets): (1) extend local uniqueness across the FULL
Case (ii) region (currently only the neighborhood where the branch conditions a_1≥1/2,
a_1/2≥a_3 hold); (2) the symmetric a_2/a_3=2 condition (not yet derived); (3) the shared
import g(dyadic)=1/7 remains open (same as dyadic-cascade-induction's §5); (4) boundary/
degenerate cases (a_3=0 or a_2=a_3).
Cases to cover: none new this round — continue extending the existing neighborhood outward.
Watch out for: this approach's Step C certificate is now dual-purpose — valuable both as a
standalone local-uniqueness result (its own trajectory) AND as the direct input to
concavity-minimax-duality's global promotion (if that approach's Step 3 succeeds). Continue
independently; do not wait on concavity-minimax-duality's outcome before extending gap (1).

Notes for the outline-reviewer:
- Field is 4 approaches, genuinely diverse in mechanism (explicit casework induction;
  whole-multiset greedy potential/gap-decomposition; global convexity/duality; local
  smoothing certificate) — not variants of one wall. potential-weighting-upper-bound and
  concavity-minimax-duality were previously benched/deprioritized; both are un-benched this
  round with concrete, non-redundant new content (confirmed by this round's three explorers,
  not merely re-asserted).
- The single shared remaining gap across ALL FOUR approaches for a full "solved" verdict is
  the lower-bound direction (g(dyadic)=1/7, i.e. the dyadic construction resists every XY
  response) — dyadic-cascade-induction's new §5 is the only approach directly attacking it
  this round; recommend prioritizing a builder there if the round allows only one lower-bound
  attempt, since concavity-minimax-duality and potential-weighting-upper-bound both only
  address the upper bound and would need §5 (or an equivalent) regardless of their own
  success.
- Strategy-stealing from the proved upper bound to the lower bound is a CONFIRMED non-
  sequitur (independently re-derived by two explorers this round) — do not let any builder
  attempt this shortcut.
- Recommended build set (for the outline-reviewer to weigh): dyadic-cascade-induction (formalize
  §2d and attempt §5 Steps 5a-5b), potential-weighting-upper-bound (run the two sanity checks,
  then attempt the greedy rule), concavity-minimax-duality (run the numerical gate first, then
  attempt Step 3 if it passes). elementary-exchange-smoothing can advance in parallel on its
  own gap-1 extension, or be deferred a round if builder capacity is limited, since its
  certificate is already usable by concavity-minimax-duality as-is.
