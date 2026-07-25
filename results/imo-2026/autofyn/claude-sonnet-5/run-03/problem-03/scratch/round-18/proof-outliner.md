## imo-2026-03

self-similar-induction-on-n: revise
Target: c(n) = 2^n/(2^{n+1}-1) is the exact answer — this approach's slice
of the whole proof is the lower-bound direction (Liu Bang's guarantee),
via the multiset-minimax reduction, closing General Theorem GT(m) for
every m (all excess parities e, all k).
Technique: discrete telescoping/peeling induction on the coupled
(OddSum, EvenSum) pair through a chain of "q=0" peels, using the
cardinality cap |D|<=m+1 as a first-class hypothesis (not an afterthought).
Skeleton:
  1. Restate GT(m) sub-case (i)'s ONLY open residual precisely: odd excess
     e=1 (and, separately, flag odd e>=3 as unconfirmed not proved),
     a_1 in [2^{k-1}+1, 2^k] (outside the certified width-1 window),
     under the cap |D|<=m+1 (equivalently |R|<=m where R = D minus the
     peeled top element) — by round 17's reviewer-certified scoping.
  2. Cheap-kill first (mandatory, before any new lemma-writing): for fixed
     sum(R)=S, cap:=2^{k-1}, count bound |R|<=m, compute the minimal
     feasible count n0 = ceil(S/cap) and check whether the crude
     "near-cap-plus-remainder" construction's forced-count-parity slack
     already algebraically dominates the shortfall T_odd - LB_odd for
     every (k,e=1,a1) in the residual range — by direct algebra, no new
     extremal-shape proof needed if it works. Do this BEFORE lemma 3.
  3. If the cheap-kill doesn't close it outright, prove the
     **Cardinality-Constrained Half-Sum Lemma**: for a finite multiset R
     with sum(R)=S, every element <= cap, and |R|<=m (m fixed), the
     minimum possible OddSum(R) over all such R is achieved by an
     explicit extremal shape (as many elements at exactly `cap` as
     possible, one remainder element, count = ceil(S/cap) when that count
     is <= m, else forced to spread more elements at cap) and equals a
     closed form strictly larger than S/2 whenever the minimal feasible
     count n0 is odd (an odd number of elements forces an unpaired
     "extra" element that contributes fully, not half, to OddSum) — this
     is what the cap-free Half-Sum Corollary structurally cannot supply
     (it is tight only for even-count all-equal multisets, which the cap
     rules infeasible at exactly the residual points).
  4. Apply the Cardinality-Constrained Half-Sum Lemma (not the cap-free
     Half-Sum Corollary) to R := D minus the peeled top element inside the
     already-certified coupled (O,E) chain (the corrected e-fold q=0
     recursion, `even-target-companion-peeling-and-corrected-qzero-chain.md`)
     to get a genuinely tighter LB_odd that beats T_odd = 2^k - a1 at the
     true worst case a1 = 2^k (not merely inside the window, which round
     17 already covers) — numeric evidence (this round's explorer,
     4 values of k, thousands of trials under the cap) shows equality is
     attained exactly at a1=2^k, zero violations elsewhere in the range.
  5. Once (k,e)=(*,1) outside-window is closed, run the identical
     cap-aware machinery at fresh odd e=3,5 near a1=2^k specifically
     (not generic random a1) as a cheap-kill BEFORE claiming general odd e
     closure — round 17/18 explorers only verified e=1 rigorously;
     e>=3 is conjectured, not proved.
Key lemmas (claim + mechanism):
  - Cardinality-Constrained Half-Sum Lemma — because an odd forced
    minimal count n0=ceil(S/cap) leaves one element unpaired in the
    odd/even rank alternation, and that element contributes to OddSum at
    its FULL value (not averaged with a partner), producing a slack of at
    least (cap - S/n0)/2-style excess over the naive S/2 bound; the cap
    |R|<=m is exactly what forces n0's parity to sometimes be odd instead
    of allowing an even, perfectly-paired split.
  - Worst-case-at-endpoint identity — because as a1 -> 2^k, sum(R) -> 2^m
    - 2^k exactly, forcing n0 to hit its cap-constrained extremal value
    with zero slack, matching the target exactly (tight, not violated);
    monotonic shrinkage of the margin as a1 increases (explorer-confirmed
    numerically at k=1,2,3,4) supports this being the unique worst point.
Open gaps: the Cardinality-Constrained Half-Sum Lemma itself (steps 2-4);
  odd e>=3 confirmation (step 5, separate deliverable, do not claim closed
  without its own targeted sweep + proof).
Cases to cover: odd e=1 (primary target this round); odd e>=3 (secondary,
  cheap-kill first).
Watch out for: do NOT reuse the cap-free Half-Sum Corollary anywhere in
  the new proof — round 17/18 confirmed a genuine unconditional
  counterexample exists cap-free at (k,e)=(2,1), a1=494/125, so any step
  that silently drops the |R|<=m hypothesis reintroduces a real
  falsehood, not just a weaker bound. Also watch for the same Odd->Odd
  vs Odd->Even telescoping bug class from round 16 recurring inside the
  new lemma's proof — explicitly re-verify which parity the coupled
  recursion produces at each step.

global-lp-vertex-sufficiency: revise
Target: c(n) = 2^n/(2^{n+1}-1) is the exact answer — this approach's
slice is the upper-bound direction (Xiang Yu can always hold Liu Bang to
<= c(n)), specifically the balanced-region residual of the Existence
Theorem (V(p) <= c(n) for every p with p1<1/2 and every gap > gamma(n)).
Technique: pivot away from Flat-Edge-face classification (round 17's
premise) toward directly bounding V(p) using the certified finite-cell/
vertex machinery (Global Vertex Lemma + Lipschitz continuity + existence
of maximizer, all already certified) on the concrete tie-free/sharp-kink
candidate near-maximizers this round's explorer located numerically.
Skeleton:
  1. State the corrected premise explicitly: this round's high-fidelity
     multi-restart search found the balanced-region near-maximizers at
     n=2 (shape m=(1,0,1)) and n=3 (shape m=(1,0,2,0)) are tie-free or a
     sharp Self-Bisection-Crossover kink, NOT Flat-Edge continuum faces —
     Flat-Edge classification (round 17's whole focus) is very likely
     not load-bearing for the actual maximizer; defer it, don't discard
     the certified Flat/Kink Parity Lemma (it stays a valid general tool,
     just not the next step).
  2. Cheap-kill (mandatory, exact arithmetic, before proof investment):
     fix the two concrete shapes m=(1,0,1) (n=2) and m=(1,0,2,0) (n=3),
     derive each shape's explicit affine-in-p formula via the certified
     Global Vertex Lemma (Section 1 of this file already gives the
     mechanism — each free block solved from the piece-sum equation), and
     directly maximize the resulting explicit rational function of p over
     its validity cell in EXACT arithmetic (sympy/Fraction), replacing
     this round's float Nelder-Mead numbers with rigorous ones. This
     converts a heuristic numeric lead into either (a) a genuine exact
     value to compare against c(n), or (b) a refutation of this round's
     float-based conjecture.
  3. If step 2 confirms sup_balanced V(p) < c(n) strictly at these
     shapes (matching the conjectured gap ~0.042 at n=2, ~0.012 at n=3),
     attempt to extend the same finite-cell vertex argument (not a new
     mechanism) across ALL cells whose validity region intersects the
     balanced region: since Sigma(n,k) is finite (already proved) and
     each f_sigma is affine (already proved), V's balanced-region
     supremum is a max over a FINITE list of cell-vertex values — the
     Existence Theorem reduces to checking finitely many exact values
     against c(n), not classifying Flat-Edge geometry at all.
  4. If the finite list is large, use the Zero-Removal Invariance Lemma
     and Mass-Constraint-style structural facts (already certified) to
     prune cells that provably cannot beat c(n) before computing them
     exactly.
Key lemmas (claim + mechanism):
  - Tie-free/kink-vertex sufficiency claim (to be tested, not yet a
    lemma): the balanced-region maximizer of V(p) is attained at a vertex
    of the finite-cell arrangement where the winning shape's fragments
    are either all distinct or meet only at rank-parity-matching
    (kink) ties — because Flat-Edge plateaus, by the certified Flat/Kink
    Parity Lemma, only arise from opposite-parity-avoiding (same-parity)
    tie configurations, and this round's search found none of those at
    the located near-optima; if true, the vertex/finite-cell machinery
    (already proved in Section 4) directly gives the exact value at each
    candidate, no new Flat-Edge geometry needed.
  - Exact-value confirmation at m=(1,0,1), m=(1,0,2,0) — because these are
    concrete, finite-dimensional affine optimization problems, solvable
    by calculus/Lagrange or boundary-case check on an explicit rational
    function, not a search.
Open gaps: whether the finite cell list, once enumerated, is provably
  bounded / tractable for general n (only n=2,3 checked this round);
  whether every OTHER cell (not just the two located near-optima) can
  be ruled out cheaply.
Cases to cover: n=2 shape (1,0,1); n=3 shape (1,0,2,0); general-n
  extension is the open item, not yet attempted.
Watch out for: this round's numeric lead is FLOAT-based (Nelder-Mead,
  explicitly flagged conjectural by the explorer) — do not certify any
  claim ("gap ~0.042", "gap ~0.012", "shrinks with n") until re-derived
  in exact arithmetic; the "gap shrinks with n" trend is a 2-point
  conjecture only, not yet tested at n=4. Also do not assume p_LB
  (the doubling point) is connected to this residual — confirmed out of
  the balanced region entirely (p1 > 1/2 always), a documented dead end
  for continuity arguments.

lp-duality-split-polytope: advance (light/optional)
Target: c(n) = 2^n/(2^{n+1}-1) — this approach's slice is a necessity
direction for split-piece count s at the region vertex e_0 (s >= n-1
conjectured necessary to reach the universal floor OddSum=1/2), a
secondary/optional strengthening, not on the critical path.
Technique: mass-counting (Generalized Mass-Constraint Theorem, already
proved to structurally cap at s >~ N/2) — do NOT spend more effort
sharpening this specific technique, per this round's plateau-check
explorer (it is proved incapable of reaching s>=n-1 by refinement, an
asymptotic argument, not just an unconfirmed numeric limit).
Skeleton (optional, light dispatch only):
  1. If spare capacity remains only: sketch (not fully prove) a
     double-counting/cyclic-sum mechanism analogous to crux aimo-0091 /
     aimo-0178 (sum a per-piece "each active piece must supply at least X
     mass to SOME untouched piece's match" bound over all N pieces
     simultaneously, rather than a single aggregate mass bound) and see
     within ~30 minutes of hand algebra whether it has any traction
     toward s>=n-1 — these are flagged as WEAK analogies by the explorer
     (structurally different target objects: grid seams/cube beams vs.
     split-fragment masses), so treat this purely as a cheap lottery
     ticket, not a committed proof line.
  2. If the sketch shows no traction quickly, formally record s>=n-1
     necessity as open and out of scope for this approach going forward,
     keeping the already-certified Even-Multiplicity Equality Criterion
     and Generalized Mass-Constraint Theorem as the file's standing
     contribution (both already certified, reusable).
Key lemmas: none new required this round; existing certified
  Even-Multiplicity Equality Criterion and Generalized Mass-Constraint
  Theorem stand as this approach's contribution.
Open gaps: s>=n-1 necessity (structurally out of reach of the current
  technique; a genuinely different invariant would be needed).
Cases to cover: none (light/optional dispatch only).
Watch out for: do not let this slug consume a full round's build effort —
  per the plateau-check explorer, this is provably tapped out for its
  headline conjecture; only a cheap (~30 min) alternative-mechanism
  sketch is warranted, not a sustained push.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
