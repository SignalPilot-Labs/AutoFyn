## imo-2026-03

self-similar-induction-on-n: revise
Target: c(n) = 2^n/(2^(n+1)-1) — full lower-bound direction (LB's geometric
partition guarantees ≥ c(n) against every XY response), of which the sole
remaining gap is the Branch-I.A-restricted window claim (‡): writing
D:=C\{c1}, T:=Γ_{ℓ-1}, W:=sum(D), show
max{OddSum(D∪T): D admissible, sum=W} ≤ 2^ℓ+ε−1 for all W in the window range,
with equality approached only at the endpoint (Theorem W, already certified).
Technique: extremal-principle / exchange-smoothing on a fixed-sum-constrained
sequence maximizing a positional (odd-rank) weighted sum — the aimo-0146
pattern — but the explorer this round found the naive transfer breaks
(Theorem W's witness shape does NOT generalize verbatim to interior W: a
different, unidentified D dominates at low W), so the skeleton below routes
around exhibiting an explicit witness family and instead targets a pure
upper bound plus an isolated, narrow open sub-case.
Skeleton:
  1. Keep Theorem W (certified) as the anchor: exact value at W = 2^{ℓ-1}+ε,
     the window's right/top endpoint.
  2. Split (‡) into gap (a) [optimality of Theorem W's witness AT the
     endpoint W = 2^{ℓ-1}+ε] and gap (b) [max-over-D as a function of W is
     non-decreasing on the window] — by the algebraic identity already
     proved (W+c1 = 2^ℓ+ε identically).
  3. Close gap (b) by the explorer's isolated reduction (Opening 3): for
     W1 < W2 in the window (width always < 1−ε), construct an admissible D'
     at W2 from any admissible D at W1 by adding the extra mass W2−W1 (< 1)
     either (i) as a new tiny piece, if |D| < ℓ — placed just below D's
     current minimum, changing at most one rank so OddSum cannot decrease
     (by the already-certified rank-counting/Peeling-Lemma mechanism); or
     (ii) if |D| = ℓ (piece cap already saturated), added to D's current
     smallest element — the one genuinely open sub-case (may cause a rank
     swap with a neighbor; NOT automatically safe per the certified
     Schur-monotonicity dead end). Step 3 reduces gap (b) to exactly
     sub-case (ii).
  4. Close gap (a) [and, if step 3(ii) needs it, sub-case (ii) too] via
     exchange-smoothing on the fixed-W slice, careful to move mass toward
     the SPECIFIC odd-rank slot being fed (not "toward the top" in
     general — the Schur dead end refutes the naive version), using the
     certified Single-Insertion Lemma as the one-unit exchange primitive,
     terminating at a finite KKT/vertex characterization of surviving
     profiles (aimo-0146 pattern, done correctly this time).
  5. Cross-check candidate: if global-lp-vertex-sufficiency's finite-cell
     machinery (Lemma 4.1/4.2, cell-wise-affine-vertex reduction) is fixed
     (adds p_k) this round, (‡) is itself an instance of maximizing an
     affine functional cell-by-cell over the bounded polytope
     {D : sum(D)=W, 0<d_i<2^{ℓ-1}, |D|≤ℓ}, giving a finite candidate vertex
     list for D at each W directly — record as an alternative route to
     steps 3-4, not a replacement (build whichever closes first).
Key lemmas (claim + mechanism):
  - Single-move safety for the "new tiny piece" case — because inserting a
    value below the current minimum changes only that one element's own
    rank (all other elements' relative order to T and each other is
    untouched), so by the certified rank-counting identity OddSum changes
    by 0 or +1 per shifted rank, never negative.
  - Piece-cap-saturation sub-case (3(ii)/gap (a)) needs genuine new work:
    because feeding the current minimum may cross a rank boundary with T's
    fixed breakpoints (powers of two), which is exactly where the Schur
    dead end shows majorization-style monotonicity can fail — the fix must
    track the SPECIFIC crossing, not appeal to a general monotonicity
    principle.
Open gaps: gap (a) [endpoint optimality] and the piece-cap-saturated
sub-case of gap (b) — both reduce to the same exchange-smoothing argument
per step 4; step 5's LP cross-connection is untested as an actual proof
route, only flagged as promising.
Cases to cover: window's endpoint (Theorem W, done); interior W via step 3
non-piece-cap-saturated case (done by rank-counting, step 3(i)); interior W
piece-cap-saturated case (open, step 3(ii)/step 4).
Watch out for: do NOT assume the endpoint's witness family (duplicate-the-
rest, r=1+ε/2) generalizes to smaller W — explorer's simulated annealing
found a different D dominates at low W. Do NOT invoke Schur/majorization
monotonicity in any form without tracking the specific rank fed (certified
dead end).

greedy-reduction-geometric: revise
Target: same c(n) lower bound — Case 2 (top piece AND tail cut
simultaneously) of TOP-ONLY's complement; specifically Subcase (b)
(Level-Absorption): show OddSum(M'∪P) ≥ b2+sum(B'') whenever level m-1 is
split into P={μ1}∪R1 (sum 2^{m-1}) with μ1<b2, for every k≥1 and every
cut-budget-respecting split.
Technique: direct asymmetric decomposition of the target using B''/S'''s
OWN slack (previously-untried "opening 2" from this round's explorer),
replacing the abstract, previously-shown-insufficient Split-Degradation
bound.
Skeleton:
  1. Recall Lemma L (Unsplit-Baseline, certified): OddSum(M'∪{2^{m-1}}) ≥
     2^{m-1} ≥ b2+sum(B''), with slack Σ = 2^{m-1} − b2 − sum(B'') ≥ 0.
  2. NEW asymmetric decomposition: observe B'' itself has the
     Dominance-Chain property one level down (at level m-2), so apply
     Theorem 7a (already certified, k=1 base case of the Dominant-Chain
     Theorem) to B''∪S''' directly: OddSum(B''∪S''') ≥ sum(B'') — i.e. get
     the "sum(B'')" half of the target FOR FREE from B'''s own internal
     structure, without touching P at all.
  3. This reduces the remaining burden on P to a SMALLER target: show
     OddSum((M'\setminus B'')∪P) ≥ b2 alone (against the baseline with
     B'' removed from the ledger, since step 2 already banked sum(B'')).
     This is a strictly easier inequality than the original (dropping the
     +sum(B'') term entirely), matching Lemma L's baseline 2^{m-1} ≥ b2
     restricted to the "no B''" residual — i.e. reduces Level-Absorption
     to (a version of) Lemma L itself, one level down in complexity.
  4. Verify step 3's reduced inequality by re-applying the same
     General Insertion Monotonicity (Theorem 13, certified, no hypothesis
     on the inserted piece needed) that proved Lemma L in the first place,
     now with P playing the role of the "inserted" fragment against the
     baseline 2^{m-1} restricted to M'\B''.
  5. Combine steps 2+4: OddSum(M'∪P) = OddSum contributions from the B''
     part (≥ sum(B'') by step 2) plus the rest (≥ b2 by step 3-4) — modulo
     checking the decomposition of OddSum across the two disjoint
     sub-multisets is additive/well-founded under the interleaved sort
     (this is the one place the argument needs care: OddSum is NOT simply
     additive across an arbitrary partition of a merged, sorted multiset,
     so this step must either (i) prove the two pieces occupy disjoint,
     non-interleaving rank bands, or (ii) fall back to a direct application
     of Theorem 13/Lemma S rather than naive additivity).
Key lemmas (claim + mechanism):
  - "B'' banks sum(B'') for free" — because B'' satisfies the
    Dominance-Chain hypothesis at level m-2 (its own top element dominates
    the rest of its own chain, same structural fact Theorem 7a already
    uses one level up), so Theorem 7a applies verbatim with B''∪S''' in
    place of the original (M', 2^{m-1}) pair.
  - Step 5's additivity concern — because OddSum's rank assignment depends
    on the FULL interleaved sort, the "add the two lower bounds" step is
    not free; must be justified via Lemma S (Subadditivity, certified) or
    a direct rank-band-separation argument, not asserted.
Open gaps: step 5's additivity/rank-band justification is the crux new
difficulty — the previous round already found the abstract bound
insufficient specifically because it discards B'''s own contribution, and
this skeleton is the first attempt to recover it; whether the two banked
quantities compose cleanly under OddSum is unverified.
Cases to cover: k=1 (Lemma L only, done); k≥2 general (this skeleton, all
new); the piece-cap/cut-budget interaction across levels m-1 and m-2
simultaneously (must confirm the cut budget for B'''s own split doesn't
conflict with the cut budget already spent on P).
Watch out for: do NOT reuse the abstract Split-Degradation candidate bound
in isolation (confirmed insufficient for k≥3, certified as a dead end this
round) — it must be combined with, not replace, the B''-slack mechanism
above. The explorer's numeric search (opening 3, pigeonhole on exact-tie
counting) is a secondary fallback if step 5's additivity fails; not this
round's primary route.

global-lp-vertex-sufficiency: advance
Target: same problem — the upper-bound direction: no configuration in the
balanced region B(n) exceeds c(n); i.e. V(p) ≤ c(n) for all p in the
closure of B(n).
Technique: finite hyperplane-arrangement / cell-wise-affine-vertex
reduction (concavity-free), now completing the narrow found gap plus using
this round's explorer computation to shrink the remaining work sharply.
Skeleton:
  1. FIX the found gap: add p_k (positivity of the last piece) to the
     functional list L, exactly as diagnosed in current.md — redo the
     vertex-extraction step of the Finite-Cell theorem with the corrected L.
     (Lemma 4.1/4.2, both already certified, are UNCHANGED by this fix —
     they only used finiteness/affineness of L, which still holds.)
  2. Use this round's explorer computation as the concrete target: the
     REGION-only part of L (dropping the Σ-shape functionals) already gives
     an exact, small candidate vertex set — 2 "genuinely new" vertices
     (p1=1/2-anchored; all-gaps-uniformly-tight) plus 2(n-1) degenerate
     vertices with p_k=0, for every n≥4 (verified exactly by sympy for
     n=2..6). State and prove this as an explicit Region-Vertex Enumeration
     Lemma (the region alone, before intersecting with Σ's functionals).
  3. Boundary reduction: prove the 2(n-1) vertices with p_k=0 need no fresh
     Σ-enumeration — each is a limit point of the already-closed slack-
     budget regime k≤n (a (k-1)-piece configuration with one vanishing
     coordinate), so by the already-certified Lipschitz continuity of V,
     V at these points equals (in the limit) V of the corresponding
     n-piece configuration, already handled. This must be written out
     precisely against the k≤n closure's exact statement (not assumed).
  4. Close the 2 genuinely-new region-corner vertices directly: exhibit,
     for each, an explicit XY response using the certified General
     k-Anchor-Merge Lemma (Theorem 10, `lemmas/singleton-interleaving-and-
     k-anchor-merge.md`) and prove V(q) ≤ c(n) there in exact arithmetic —
     the explorer's numeric check (Nelder-Mead, n=3,4) found V≈1/2 at both,
     well under c(n); this step converts that numeric finding into an
     exact closed-form proof, using the Consecutive-Block AltSum Formula
     (certified, `lemmas/consecutive-block-altsum-and-bottom-block-
     doubling.md`) to evaluate the AP-tail structure these vertices have
     exactly.
  5. State honestly what remains outside this region-only sub-list: the
     FULL candidate set Q also includes (k-1)-subsets drawn from Σ's
     shape-validity/ordering functionals (not just the region's own
     inequalities) — the |Σ(n,k)| unboundedness obstruction is UNTOUCHED
     by steps 1-4 and must be flagged as still open, not silently dropped.
Key lemmas (claim + mechanism):
  - Region-only vertex set is 2n (n≥4), split 2/(2(n-1)) — because the
    region B(n)'s closure is cut out by exactly n+2 affine functionals
    (p1-1/2, n gaps, p_k), and enumerating all feasible (k-1)-subsets
    (verified exactly by sympy) gives this count with p_k=0 splitting off
    cleanly as the "drop one gap constraint, keep p_k=0" family.
  - p_k=0 vertices reduce via continuity — because they are literal limit
    points of the k≤n regime (one coordinate → 0), and V is 1-Lipschitz
    (already certified), so V's value there is forced by continuity from
    already-proved territory, not fresh work.
Open gaps: step 3's continuity argument needs to be matched precisely
against the k≤n closure lemma's exact hypotheses (not yet verified, flagged
as "needs checking" by the explorer); step 4's exact-arithmetic upgrade of
the numeric V≈1/2 finding is not yet done for general n (only checked
numerically at n=3,4); the |Σ(n,k)| unboundedness obstruction (the full
vertex list beyond the region-only sub-list) remains completely open and is
NOT addressed by this round's skeleton — must not be overclaimed as closed.
Cases to cover: n=2,3 small-n boundary effects (region-only vertex count is
3, 5 respectively, not the general 2n pattern — must be checked separately,
not assumed to follow the n≥4 formula).
Watch out for: do not let step 4's "V≈1/2 suspiciously exact" numeric
pattern get treated as proved without the exact AltSum/k-Anchor-Merge
derivation — Nelder-Mead is not a proof. Do not conflate "region-only
vertices are easy" (this round's finding) with "the Existence Theorem is
closed" — the hard, unaddressed part (Σ-shape vertices / |Σ(n,k)| growth)
is untouched.

lp-duality-split-polytope: advance
Target: same problem, as an evaluation-tool supplier and secondary direct
target — (i) supply exact-arithmetic evaluation machinery (Consecutive-
Block AltSum Formula, Bottom-Block-Doubling) to global-lp-vertex-
sufficiency's step 4 above for AP-tail-structured vertices; (ii) directly
close the one remaining case of its own Multi-Piece Necessity Theorem
(idx=1, i.e. k=N, splitting p1 itself), currently the sole gap in an
otherwise-fully-proved theorem for the triangular family.
Technique: (i) is a direct reuse of already-certified formulas, no new
proof needed beyond the wiring (leave to whichever builder works
global-lp-vertex-sufficiency step 4, or do it here as a joint deliverable);
(ii) is a case-split/peeling argument adapted from Theorem B's technique,
targeting specifically the boundary mismatch the round-7 attempt found.
Skeleton (for target (ii), idx=1):
  1. Recall the obstruction found in round 7: Theorem B's one-step peel
     (peel N, land on {1,...,N-1}∪Y'), applied naively to idx=1 (peeling
     N-1 instead since N itself is now a "free" fragment in Y, not a fixed
     landmark), produces a residual {1,...,N-2}∪Y with sum(Y)=N against
     only N-2 landmarks — an off-by-one mismatch with Theorem A's clean
     recursive family.
  2. NEW: instead of peeling one landmark at a time, directly handle the
     mismatch by strengthening the induction hypothesis to a
     PARAMETRIZED family A(N', N, ...) that tracks the actual sum excess
     (currently exactly 1, "N against N-2 landmarks") as an explicit extra
     parameter, rather than requiring the clean N'=N' match Theorem A's
     base recursion assumes — i.e. prove a slightly more general
     Theorem A' by induction on N' that absorbs a bounded excess, then
     specialize back to idx=1's specific excess-1 instance.
  3. Alternative (fallback per round-7's own option (b)): prove m≥4 is
     always dominated by m∈{2,3} for the triangular family's structure
     (landmarks a full consecutive run) — this reduces idx=1 to the two
     already-partially-computed closed forms (m=2: N/2 even, (N-3)/2 odd;
     m=3: strictly better for even N, exact value not yet in closed form)
     — finish deriving m=3's closed form and prove the m≥4 domination
     claim (currently unproved, only numerically observed for N≤10).
  4. Verify the resulting closed form ⌊(N-3)/2⌋ (N≥5) / A=1 (N=4) matches
     both the peeling-based Theorem A' (step 2) and the m∈{2,3}-domination
     route (step 3) — either one suffices; attempt both since it's unclear
     in advance which closes first.
Key lemmas (claim + mechanism):
  - Excess-parametrized Theorem A' — because the idx=1 mismatch is always
    exactly a fixed, boundedly-growing excess (not an unbounded drift), a
    generalized induction that carries the excess as an explicit tracked
    parameter (rather than forcing an exact match to the N'=N' pattern)
    should close the same way Theorem A closed the clean case, one level
    of generality up.
  - m≥4 domination (step 3) — because the triangular family's landmarks
    are a full consecutive run {1,...,N-1}, more than 3 free fragments in
    Y necessarily forces at least two of them into adjacent ranks that a
    2-or-3-piece split could merge without loss (needs to be made precise
    and proved, currently only a numeric pattern with no proof mechanism
    identified).
Open gaps: both step 2 (excess-parametrized induction) and step 3
(m≥4 domination) are unproved — pick whichever the builder finds tractable
first; the m=3 closed form itself is not yet derived in step 3's own
right and is a prerequisite for that route.
Cases to cover: N=4 (documented exception to the ⌊(N-3)/2⌋ formula, must be
handled as a separate base case in either route); parity split (even N: m=3
wins; odd N: m=2 wins) throughout step 3.
Watch out for: do not treat the triangular family's idx=1 closure as
needed for global-lp-vertex-sufficiency's step 4 — that step uses only the
AltSum evaluation TOOLS (Blk(c,m)), not this theorem's own remaining gap;
keep the two deliverables (tool-supply vs. own-theorem-closure) clearly
separated so a builder doesn't conflate "the tool is certified" with "the
theorem this approach owns is fully proved" (it is not, pending idx=1).

build set: global-lp-vertex-sufficiency, greedy-reduction-geometric, self-similar-induction-on-n, lp-duality-split-polytope
