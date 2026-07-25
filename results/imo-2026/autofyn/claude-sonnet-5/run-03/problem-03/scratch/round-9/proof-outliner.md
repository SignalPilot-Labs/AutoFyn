## imo-2026-03

self-similar-induction-on-n: revise
Target: For every n, the geometric partition (1,2,4,...,2^n)/(2^{n+1}-1)
guarantees Liu Bang (LB) total >= c(n) = 2^n/(2^{n+1}-1) against every
Xiang Yu (XY) response (the lower-bound half of the whole problem's
answer). Full problem target unchanged: c(n)=2^n/(2^{n+1}-1) exactly, both
directions.
Technique: strong induction on n via strategy-stealing / self-similar
peeling of the geometric shape, reduced (by round 6-8 work) to a clean
scalar target L_0(l,eps) (l=m-1, "does OddSum(C∪Γ_{l-1}) >= 2^l hold for
every admissible C with sum 2^l+eps"), now further reduced (round 8) to a
single remaining region, the Branch-I.A-restricted window.
Skeleton:
  1. Reduction to multiset minimax — certified (`lemmas/reduction-to-multiset-minimax.md`).
  2. T(2) fully closed, Branch I.B fully closed, Branch I.A main range
     closed, Branch II proved equivalent to the window recurring at lower
     levels — all certified/proved in prior rounds.
  3. NEW this round: close the window via exchange-smoothing (crux
     aimo-0146) using the certified Single-Insertion Lemma as the
     one-unit-move primitive, targeting the closed-form margin
     OddSum(C∪Γ_{l-1}) - 2^l >= eps/2, tight at c_1=2^{l-1} via the
     budget-starved partial duplicate-the-rest family — by tool/theorem:
     Doubling Lemma (instance) + Single-Insertion Lemma + exchange
     argument (new, modeled on aimo-0146's local-perturbation-to-extremal
     technique).
  4. Once the window is closed, Branch II is unconditionally closed (by
     round 8's proved equivalence), hence the whole tail-untouched sliver
     Case-B(m,k), hence — combined with greedy-reduction-geometric's
     TOP-ONLY closures — most of the lower-bound direction's structural
     backbone (still needs greedy-reduction-geometric's own Level-
     Absorption gap closed separately for the fully general interleaved
     case; the two are related but not identical, see below).
Key lemmas (claim + mechanism):
  - Window margin >= eps/2 uniformly in l — because the extremal
    configuration is forced, by the piece-count budget, to be a partial
    (bottom-rank-only) instance of the Doubling Lemma; any deviation from
    this shape can only add OddSum mass at odd ranks (exchange-smoothing
    argument, to be made rigorous via the Single-Insertion Lemma's exact
    delta formula).
  - Single-Insertion Lemma (already certified in-file): exact formula for
    how AltSum changes inserting one value at an arbitrary sorted
    position — the mechanism that makes an exchange argument tractable
    here (it is the "unit move" whose effect on the objective is known in
    closed form).
Open gaps: the exchange-smoothing proof itself (not yet attempted on this
gap — only the extremal witness and the crux analogy are established);
re-verify eps/2 at l=7,8 before trusting the pattern beyond l<=6.
Cases to cover: the window's own sub-range (c_1 from 2^{l-1} to
2^{l-1}+1-eps) is one continuous parameter, not discrete casework — the
proof must show monotonicity/extremality across it, not enumerate cases.
Watch out for: do NOT retry order-statistics/two-peel transplant (wrong
bound direction, already diagnosed dead by round 7); do not assume the
infimum eps/2 is attained in the closed window without checking (it is,
per the explorer's witness, but re-verify explicitly in the proof).

greedy-reduction-geometric: revise
Target: same as self-similar-induction-on-n (the lower-bound direction:
LB's geometric partition guarantees >= c(n) against every XY response),
approached via peeling/dominance-chain machinery on the top-piece split
plus tail refinement, rather than the l-indexed scalar recursion.
Technique: casework on how XY's <=n cuts split between LB's top piece and
the tail, closed via Dominance-Chain / Prefix-Run peeling arguments and
(new) quantitative insertion-gain bounds.
Skeleton:
  1. Reduction (shared, certified) + Case 1 (XY never touches top piece):
     closed, certified.
  2. TOP-ONLY (all XY cuts on top piece): closed except a narrow residual,
     largely handled by self-similar-induction-on-n's overlapping work.
  3. General interleaved Case 2 (top piece AND tail both cut): Theorem 7
     (top-levels-clear) closed; Theorem 7'(m,k;L)'s inductive step splits
     into Subcase (a) Insertion-Robustness (closed round 8, Theorems
     12/13) and Subcase (b) Level-Absorption — the sole remaining gap.
  4. NEW this round: close Level-Absorption via a QUANTITATIVE
     insertion-gain bound (not a hypothesis-dropping generalization of
     Theorem 13, which the explorer proved does not transfer) chained
     with the cut-budget cap, using either (a) a direct chained-gain
     computation from Theorem 12's own Delta formula, or (b) exchange-
     smoothing (crux aimo-0146, same crux family as the sibling gap in
     self-similar-induction-on-n) reducing the adversary's response space
     to a finite extremal-profile family, then checking the inequality
     there directly (round 7's tight instance already gives margin
     2^(m-3)-1/2 > 0, so real slack is expected once the budget is
     correctly enforced).
Key lemmas (claim + mechanism):
  - Total insertion gain from splitting level 2^{m-1} into p pieces
    (p <= level's actual cut budget) is >= b_2 — because each additional
    cut beyond "no fragmentation" can cost the adversary at most one
    dyadic "pairing" unit of margin (evidenced by the m=3 tight case:
    exactly 1 cut over budget costs exactly 1 unit), so a correctly
    budgeted split cannot manufacture enough tied pairs to erase the
    b_2-sized gain.
  - Exchange-smoothing extremal-profile reduction — because OddSum is a
    fixed-weight (1,0,1,0,...) sum of a sorted sequence under a sum
    constraint plus a piece-count budget, exactly aimo-0146's target
    shape; local mass-shifting toward equalized/tied profiles is the
    adversary's only lever, and the budget caps how many such profiles
    are reachable.
Open gaps: both leads are unattempted (round 8 focused on Subcase (a)
only); the exact cut-budget bookkeeping formula must be re-derived
correctly before any inequality manipulation (round 7's bug was exactly a
budget-accounting mismatch).
Cases to cover: the two-peel structure already splits by mu_1 vs b_2 (10.2a/10.2b) — Subcase (b) itself may still need a sub-case split on how many of the p pieces of {mu_1}∪R_1 land at even vs odd rank, to be discovered during the proof.
Watch out for: do NOT attempt a hypothesis-dropping proof (checked and
ruled out this round — the cut-budget hypothesis is proven necessary, not
over-restrictive); do NOT cite Theorem 13 directly for Subcase (b) (gives
only a zero gain bound, a category mismatch with the quantitative
b_2-sized gain actually needed).

global-lp-vertex-sufficiency: revise (major pivot — concavity abandoned)
Target: the upper-bound direction's Existence Theorem — V(p) <= c(n) for
every p in the balanced region (k=n+1, p_1<1/2, every consecutive gap
> gamma(n)) — as part of proving no LB partition beats c(n).
Technique: LP/compactness framing of the inner minimization V(p), now
reduced to a finite hyperplane-arrangement / cell-wise-affine-vertex
argument instead of concavity (concavity is PROVED FALSE this round —
retire it as a target entirely).
Skeleton:
  1. Global Vertex Lemma (certified): V(p) = min over a finite,
     p-independent set of shapes sigma of an affine-in-p formula f_sigma(p),
     valid on an affine (half-space) region D_sigma.
  2. Lipschitz continuity of V(p) (certified) + existence of a maximizer
     via compactness (certified).
  3. NEW this round (replaces the old concavity section): build the
     finite hyperplane arrangement L in p-space from (a) every component
     of every x_sigma(p) (validity boundaries) and (b) every pairwise
     difference f_sigma(p)-f_tau(p) (branch-comparison boundaries), plus
     the balanced region's own defining inequalities. On each open cell
     of the induced polyhedral subdivision, V is a single fixed affine
     formula (both which sigma are valid and which wins are locally
     constant), so V's max over (cell ∩ balanced region) is attained at a
     vertex of that intersection.
  4. Assemble: the true global maximizer p* of V over the whole balanced
     region is attained at one of finitely many arrangement vertices;
     verify V(p*) <= c(n) at each candidate (or find/rule out a genuine
     counterexample).
  5. Tractability shortcut to try FIRST: check whether the global
     maximizer coincides with an already-catalogued "survivor"
     configuration (universal-halving-adversary's tiny-excess points at
     n=6,8; lp-duality-split-polytope's triangular family, now being
     pushed toward an explicit multi-piece sufficiency witness) —
     verifying V<=c(n) directly at these known candidates may avoid a
     full arrangement enumeration.
Key lemmas (claim + mechanism):
  - Cell-wise affine formula for V — because on any open cell of the
    hyperplane arrangement L, every affine functional in L (validity and
    branch-comparison boundaries) has constant sign, so the identity of
    the winning valid shape sigma cannot change within the cell.
  - Concavity of V is FALSE (established this round, not a gap anymore):
    a high-fidelity two-optimizer sweep at n=2 exhibits genuine
    sign-alternating second differences (deficit ~0.01, far outside
    noise) — because even within one fixed cut-allocation shape m, the
    optimal pin value for the free fragment switches as p varies,
    producing real kinks.
Open gaps: the hyperplane-arrangement argument's practical tractability
(bounding/classifying |Sigma(n,k)| and which cells actually intersect the
balanced region) is unattempted; the shortcut check against known
survivor configurations is also unattempted.
Cases to cover: none yet enumerated — the whole point of this section is
to reduce the continuum of cases to a finite candidate set; that
reduction itself must be executed, not just asserted.
Watch out for: do NOT re-attempt concavity in any form (refuted, with a
reproducible two-optimizer counterexample — this is a genuine dead end,
not merely unresolved); do NOT trust small/coarse numeric concavity-style
checks on V(p) in general (round 8's "no violation in 15 trials" was a
false negative from a coarse proxy that happened to stay within one
affine chamber) — any future check on this object must deliberately sweep
across branch/validity boundaries, not just sample random interior
points.

lp-duality-split-polytope: advance
Target: same overall problem; this approach's specific contribution is
the upper-bound direction restricted to the "triangular family" of LB
partitions (p_i = (n+2-i)/D_n), now pushing toward a full
necessity+sufficiency result for that family and a concrete link to
global-lp-vertex-sufficiency's new arrangement target.
Technique: LP-vertex enumeration (Single/Two-Piece-Split Vertex Lemmas) on
the triangular family's exact-AP landmark structure.
Skeleton:
  1. Multi-Piece Necessity for the triangular family: COMPLETE (certified
     this round, `lemmas/idx1-closure-and-full-multi-piece-necessity.md`)
     — no single-piece XY response reaches c(n), for every idx, every
     n>=3.
  2. NEW this round's target: prove a matching SUFFICIENCY result — an
     explicit closed-form 2-piece (or few-piece) XY response achieving
     OddSum <= c(n) for the triangular family, for every n>=3 (currently
     only hand-verified at n=3). Use the certified Two-Piece-Split Vertex
     Lemma to search the finite candidate set exactly at several n
     (n=3..7 already have data from Multi-Piece Necessity's own
     computation), find the general-n pattern (which landmark pairs get
     matched — likely governed by the AP structure p_i+p_j=p_1 iff
     i+j=n+3, already observed at n=6), then prove it in general.
  3. Feed the resulting closed-form witness to global-lp-vertex-
     sufficiency as a concrete candidate extremal configuration for its
     hyperplane-arrangement argument.
Key lemmas (claim + mechanism):
  - General-n 2-piece closing response exists — because the triangular
    family's landmarks are in exact AP (after scaling by 1/D_n, they are
    exactly 1,...,n+1), so a pair of landmarks (i,j) with i+j=n+3 sums
    exactly to p_1, giving a natural "split p_1 to match two landmarks at
    once" construction whose OddSum can be computed in closed form via
    the same block/tie-counting bookkeeping already used in Multi-Piece
    Necessity's proof.
Open gaps: the general-n sufficiency construction and its proof are not
yet found — only the n=3 instance is hand-verified; the AP-based
pattern-matching idea is a lead, not a proof.
Cases to cover: n even vs odd (since the AP-pair existence for i+j=n+3
depends on parity/range, as already flagged by the round-6/7 "false
closed-form conjecture" finding for the necessity floor — expect similar
number-theoretic casework here).
Watch out for: do NOT assume monotonicity in n for the winning
configuration's value (round 6/7 found the single-piece floor itself is
NOT monotonic in n, for structurally similar number-theoretic reasons —
check the sufficiency construction's value at consecutive n values
explicitly rather than assuming a smooth trend).

universal-halving-adversary: advance (deprioritized, per round 8 redirect — unchanged this round)
Target: same overall problem, upper-bound direction via explicit additive
constructions (k=1, k=2 anchor-merge, Subset-Tie family).
Technique: named finite-construction family (Doubling Lemma, Anchor-Merge,
Subset-Tie, Generalized Subset-Tie) applied per-instance.
Skeleton: unchanged from round 8 — Theorem 12 (Generalized Subset-Tie, any
index) is certified; the family's survivor rate appears to GROW with n,
so full closure of the Existence Theorem via this family alone is
flagged as asymptotically borderline, not merely incomplete.
Key lemmas: Theorem 12 (certified) — no new lemma targeted this round.
Open gaps: full closure of the Existence Theorem is NOT this approach's
job anymore (redirected to global-lp-vertex-sufficiency per round 8's
plateau-break decision, unchanged this round). No new build work is
proposed for this approach this round; it stays registered and its
certified tools remain importable (e.g. as candidate survivor
configurations for global-lp-vertex-sufficiency's shortcut check).
Cases to cover: none proposed this round.
Watch out for: do not re-litigate the "does the survivor rate really grow"
question without a from-scratch, deliberately-uncapped verification
script (round 8 found a builder's own speed-cap could manufacture a
spurious growth trend) — if revisited, redo the check as a first step,
not an afterthought.
