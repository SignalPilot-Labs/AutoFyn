## imo-2026-03

lp-duality-split-polytope: revise
Target: the whole problem — c(n) = 2^n/(2^{n+1}-1) is the game's value (via the
certified Reduction Lemma, `lemmas/reduction-to-multiset-minimax.md`); this
approach's job is the upper-bound half, and this round closes the last open
`idx` case (`idx=1`, splitting the top landmark) of the Multi-Piece Necessity
theorem for the triangular family.
Technique: peeling / AltSum-reformulation (Theorem A/B's own method), plus a
new odd-multiplicity normal-form reduction to shrink the search space before
peeling.
Skeleton:
  1. Restate the reduced target: for `N=n+1`, `k=N`, only `A(N,N,y)≥1` is
     needed — NOT the closed form `⌊(N-3)/2⌋` (explorer found the closed-form
     conjecture is likely FALSE for `N≥11`, e.g. true min at `N=11` is `3` not
     `4`; drop it as a target entirely, it is unneeded extra work) — by
     Theorem A's reformulation `OddSum=(1+AltSum)/2`.
  2. Reduce arbitrary fragment choices `Y` to vertex candidates via the
     already-certified Single-Piece-Split Vertex Lemma (no new proof needed):
     blocks pinned to `0`, tied to each other, tied to a landmark, or one
     free block solved from the leftover budget.
  3. Apply the new **Odd-multiplicity reduction** (elementary, prove from
     scratch, ~2 lines): `AltSum(T)=AltSum(Odd(T))` where `Odd(T)` is the set
     of values of odd multiplicity in `T` — collapses vertex candidates to
     "which landmarks get cancelled."
  4. **Claim D** (discrete floor): for `M=N-1`, `B={1,...,M}`, every
     `C⊆B` with `sum(C)≤M+1` has `AltSum(B\C)≥1`. Two-case proof (both cases
     fully worked by the explorer, reuse Theorem B's own two named facts
     verbatim — Peel identity + Upper-bound fact):
     - `M∉C`: `M` survives as unique max; peel it, bound residual (max
       `≤M-1`) by the Upper-bound fact, giving `≥M-(M-1)=1`.
     - `M∈C`: forces `sum(C\{M})≤1`, so `C\{M}⊆{1}` — exactly 2 sub-cases
       (`C={M}` or `C={M,1}`), each computed directly by one more peel.
  5. Bridge Claim D to the continuous vertex enumeration: show every vertex
     from step 2 is either (a) "exact landmark cancellation + hidden free
     pair," which is literally an instance of Claim D via step 3's reduction
     — done; or (b) a "stray" free block of odd size landing on a value that
     is not any landmark — the one remaining open case.
  6. Close case (b) [OPEN GAP]: show the stray-value vertex is dominated by
     (never beats) the best Claim-D configuration — candidate mechanism: an
     exchange/perturbation argument moving the stray value continuously to
     the nearest landmark, using the piecewise-linear/rank-crossing structure
     of `AltSum` in one coordinate, showing this move cannot increase
     `AltSum`. Not yet proved — numerics (300+ trials) never refuted it.
  7. Conclude `idx=1` closed in full, hence Multi-Piece Necessity closed for
     all `n+1` index choices, hence (combined with the already-closed
     slack-budget and full-budget regimes) the upper-bound direction reduces
     to exactly the balanced-region "large-gaps-everywhere" residual (handed
     to the other UB approaches below).
Key lemmas (claim + mechanism):
  - Odd-multiplicity reduction: `AltSum(T)=AltSum(Odd(T))` — because grouping
    `T`'s sorted list into maximal equal-value blocks, an even-size block
    contributes canceling `±v` pairs (net 0) and shifts parity evenly, so
    iterating from largest to smallest value reproduces exactly
    `AltSum(Odd(T))`.
  - Claim D — because the `M∉C` case peels the true max and applies the
    already-certified Upper-bound fact to the residual; the `M∈C` case is
    forced into exactly 2 explicit small sub-cases by the tight budget
    `sum(C)≤M+1`.
  - Stray-block domination (open) — candidate mechanism: continuity/exchange,
    moving the stray value to the nearest landmark along a path where
    `AltSum` is piecewise-linear (rank does not cross except at landmark
    values), and showing the move is weakly `AltSum`-decreasing.
Open gaps: step 6, the stray-free-block domination lemma — the sole
remaining piece of `idx=1` (and hence of the whole Multi-Piece Necessity
theorem).
Cases to cover: `M∈C` vs `M∉C` (Claim D — closed); "exact cancellation"
vertex vs "stray block" vertex (only the latter open).
Watch out for: do NOT resurrect the `⌊(N-3)/2⌋` closed-form target — it is
both unneeded and apparently false for `N≥11`; degenerate sub-case where the
stray value coincides exactly with a landmark (should reduce to Claim D,
must be checked at the boundary, not silently assumed).

self-similar-induction-on-n: revise
Target: the whole problem — LB direction, that the geometric construction
achieves `≥c(n)`; this round closes Branch II of the `L_0(ℓ,ε)` residual via
a genuine strong induction on `ℓ` (a materially different framing from round
7's "needs an incompatible upper-bound direction," now shown to be the wrong
diagnosis).
Technique: strong induction on `ℓ`, via two applications of the already-
certified Peeling Lemma / Companion Peeling Lemma pair (exact identities, not
bounds).
Skeleton:
  1. Peel `T`'s own top `2^{ℓ-1}` (present since `Γ_{ℓ-1}` always contains it):
     `OddSum(C∪Γ_{ℓ-1}) = 2^{ℓ-1} + EvenSum(C∪Γ_{ℓ-2})` — exact identity, by
     the Peeling Lemma.
  2. Throughout Branch II's range (`c_1∈(2^{ℓ-1}-1+ε,2^{ℓ-1})`), verify
     `c_1>2^{ℓ-2}` (true since `2^{ℓ-1}-1≥2^{ℓ-2}` for `ℓ≥2`), so `c_1` is the
     max of `C∪Γ_{ℓ-2}`; apply the Companion Peeling Lemma to get, exactly,
     `EvenSum(C∪Γ_{ℓ-2}) = OddSum(C'∪Γ_{ℓ-2})`, `C'=C\{c_1}`.
  3. Identify the reduced target `OddSum(C'∪Γ_{ℓ-2})≥2^{ℓ-1}` as exactly the
     `L_0(ℓ-1,ε')` instance, `ε'=2^{ℓ-1}+ε-c_1∈(ε,1)⊂(0,1)` throughout the
     window; piece-count transfers correctly (`C` has `≤ℓ+1` parts ⟹ `C'`
     has `≤ℓ=(ℓ-1)+1` parts, matching `L_0(ℓ-1,·)`'s own cap).
  4. Case split on `max(C')` vs `2^{ℓ-1}`:
     - `max(C')≥2^{ℓ-1}`: closed immediately, free, by the certified Element
       Bound Lemma (`OddSum(S)≥max(S)`).
     - `max(C')<2^{ℓ-1}`: `C'` is a genuine `L_0(ℓ-1,ε')` instance — apply the
       strong induction hypothesis (covering Branch I.A, I.B, and Branch II
       at level `ℓ-1`, all already handled/being handled recursively).
  5. Base case `ℓ=1`: Branch II is vacuous — `sum(C)=2+ε` with `≤2` total
     parts forces `max(C)≥1+ε/2>1`, contradicting `c_1<1`.
  6. Conclude Branch II closed for all `ℓ` by strong induction, completing
     `Case-B(m,k)`'s tail-untouched sliver except the (separate, narrower,
     untouched-by-this-round) Branch-I.A-restricted window.
Key lemmas (claim + mechanism):
  - Exact peel identity `OddSum(C∪Γ_{ℓ-1})=2^{ℓ-1}+OddSum(C'∪Γ_{ℓ-2})` —
    because two applications of the certified Peeling/Companion-Peeling
    identity pair are exact (`Odd+Even=sum`, no discard), valid throughout
    Branch II's range specifically because `c_1` is provably the max of
    `C∪Γ_{ℓ-2}` there (step 2). NOTE: verified 0/3000 mismatches by the
    explorer but must be re-derived symbolically by the builder first, as the
    whole closure rests on it.
  - `ℓ=1` base-case vacuity — because the piece-count/sum arithmetic forces
    `max(C)>1`, contradicting Branch II's defining constraint.
  - Element-Bound short-circuit for `max(C')≥2^{ℓ-1}` — already certified,
    trivial application.
Open gaps: rigorous handling of the boundary behavior as `ε'→0` or `ε'→1`
(does the induction hypothesis, stated for `ε'∈(0,1)` open, need invoking at
values grazing the boundary? flagged by explorer as unchecked); double-check
the induction is well-founded (strictly decreasing `ℓ`, bottoming at the
vacuous `ℓ=1` case).
Cases to cover: `ℓ=1` base case; `max(C')≥2^{ℓ-1}` vs `<2^{ℓ-1}`; boundary
`ε'`.
Watch out for: do not re-frame Branch II as "needing an incompatible upper-
bound direction" — that framing is refuted this round (Odd/Even bounds are
equivalent via the fixed-sum identity); the Branch-I.A-restricted window is
a *different*, still-fully-open piece, untouched by this induction — do not
conflate the two as both closed once Branch II is done.

greedy-reduction-geometric: revise
Target: the whole problem — LB direction; this round attacks
Insertion-Robustness (Sub-Problem A of Case 2's joint closure) via an
exchange/telescoping reduction to the already-proved `k'=1` case.
Technique: exchange argument / monovariant telescoping (crux move analogous
to `aimo-0003`'s "reduce invariance under all insertions to invariance under
one adjacent transposition"), built on the certified Single-Insertion Lemma.
Skeleton:
  1. State Insertion-Robustness precisely: for arbitrary `R_1` (any finite
     positive multiset, fixed sum, replacing one slot), `OddSum(B'∪S''∪R_1)`
     is bounded below by the already-established `k'=1` bound.
  2. Reuse the certified Single-Insertion Lemma (exact `ΔAltSum`/`ΔOddSum`
     formula for inserting one value at an arbitrary sorted rank) as the
     atomic move.
  3. Exchange step: for `R_1` with `m'>1` pieces, pick two pieces `r_i,r_j`;
     compare "insert them separately" against "insert their sum as one
     value" using the exact Single-Insertion formula at each affected rank;
     show the split's total effect on `OddSum` is bounded below by the
     unsplit single-insertion's effect (NOT that the single-element shape is
     literally worst — that is a confirmed dead end, refuted by a 3000-trial
     exact counterexample; the bound must be additive/telescoped, not a
     worst-case-shape claim).
  4. Telescope over `m'-1` such exchange steps to reduce to `m'=1`, the
     already-proved-trivial base case.
  5. Conclude Insertion-Robustness holds for arbitrary `m'`.
Key lemmas (claim + mechanism):
  - Single-Insertion Lemma (already certified) — exact, reused as the atomic
    step; no re-proof needed.
  - Split-vs-single exchange bound (the open step) — candidate mechanism:
    directly compare the two exact `ΔOddSum` formulas (combined insertion vs.
    two separate insertions at their respective ranks) using the rank-parity
    structure already used throughout the project (Odd/Even alternation
    under insertion), aiming to show the split's total effect telescopes to
    at least the single-insertion bound, not that either shape dominates
    outright.
Open gaps: step 3, the exchange/telescoping bound itself — the core unproved
claim.
Cases to cover: `m'=1` (done, trivial); general `m'` via induction on `m'`
using the exchange step.
Watch out for: the confirmed dead end "single-element `R_1` is worst case"
(false ~50% of trials) — the exchange argument must not assume any fixed
shape is worst; it needs a genuinely additive bound over successive
single-insertions, matching the file's own honest diagnosis ("chaining this
bound over an arbitrary number of inserted pieces" is exactly the open step).

universal-halving-adversary: revise (narrow scope, redirect)
Target: the whole problem — UB direction, balanced-region residual
("large-gaps-everywhere"); this round adds one more incremental narrowing
tool but explicitly caps ambition here per the plateau diagnosis (see new
approach below for the actual closing attempt).
Technique: mechanical generalization of the certified Singleton-Interleaving
Lemma (same proof template as Theorem 11), plus honest quantitative
bookkeeping of why this family cannot be expected to fully close the gap.
Skeleton:
  1. Generalize Theorem 11 (Subset-Tie, currently stated only for splitting
     `p_1`) to allow tying-and-splitting **any** index — a direct mechanical
     corollary of the certified Singleton-Interleaving Lemma (Theorem 9),
     same construction/cut-cost/closed-form derivation, just re-indexed.
  2. Take best-of-{k=1, generalized-subset-tie-over-all-indices} as the new
     named-tool bound; report the honestly-measured survivor rate (1.25-4%
     at `n=4-8`, growing to 8-30% at `n=10-15`, per this round's unbiased
     resampling) as a real but non-terminal improvement.
  3. Record explicitly (not as new proof, as documentation) the quantitative
     diagnosis: `gamma(n)~2^{-n}` races against the subset-sum granularity
     achievable by any *fixed* combinatorial tie-rule, which is also
     `~2^{-n}` generically — explaining structurally why no single further
     named additive tool is expected to close the gap as `n→∞`.
  4. Explicitly redirect: the Existence Theorem's full closure is handed to
     `global-lp-vertex-sufficiency` (new approach below); this approach's
     remaining value is incremental narrowing + serving as the concrete
     source of "vertex-shape" data (subset-tie constructions) that the new
     approach's LP-vertex enumeration must reproduce/subsume.
Key lemmas (claim + mechanism):
  - Generalized Subset-Tie (any index) — mechanical corollary of the
    certified Singleton-Interleaving Lemma, same tail-tied-fragments-plus-
    remainder construction applied to an arbitrary chosen index instead of
    `p_1`; cut-cost and closed-form `OddSum` derivation transfer verbatim.
Open gaps: the full Existence Theorem — honestly not expected to close via
this family (this round's own quantitative finding); step 1-2 (the
generalization itself) should close cleanly and cheaply.
Cases to cover: none new beyond the index generalization.
Watch out for: **do not report undersampled survivor-rate claims** (e.g.
"0/300") without stating the exact sampling method — this round found prior
"0/300" reports were an artifact of narrow/biased sampling, not genuine
near-closure (true rate is 33-46% under honest uniform Dirichlet sampling of
the region before any named tool is applied); any future numeric claim here
must state sample size and generation method explicitly.

global-lp-vertex-sufficiency: new
Target: the whole problem — UB direction, but a genuinely different
top-level framing from `universal-halving-adversary`'s explicit-construction
family: prove directly, via an LP/vertex argument uniform in `n` (extending
`lp-duality-split-polytope`'s Theorem A/B peeling machinery from a
*necessity* direction to a *sufficiency* direction), that XY's true optimal
response — the min over ALL cut-patterns and ALL fragment values, not any
named subfamily — is `≤c(n)` everywhere on the balanced-region simplex. This
is the plateau-break move CLAUDE.md flags: the additive-construction family
has a real, quantitatively-diagnosed wall (survivor rate growing with `n`,
not shrinking), so this approach abandons "exhibit one more explicit
construction" and instead targets an existence-over-a-compact-region
argument, the same style of move Theorem 3 and Theorem B already used
successfully one level down.
Technique: LP duality / extreme-point optimality (a piecewise-linear
objective over a compact polytope attains its optimum at a vertex),
combined with a compactness/continuity reduction of "for every point of the
simplex, some construction works" to finitely many extremal configurations.
Skeleton:
  1. Fix a combinatorial cut-pattern `π` (which piece splits into how many
     further fragments, total cuts `≤n+1-k`, per the certified Reduction
     Lemma). Via the certified reformulation `OddSum=(1+AltSum)/2` and the
     rank-parity/greedy-optimality machinery already used throughout the
     project, `OddSum` is piecewise-linear in the fragment values for fixed
     `π` (linear on each region where the sorted rank order is fixed; breaks
     only at finitely many rank-crossing hyperplanes).
  2. Hence, for fixed `π`, minimizing `OddSum` over the fragment simplex
     (fixed per-piece sums, positivity) is a linear program; by the
     Fundamental Theorem of LP (extreme-point optimality), its minimum is
     attained at a vertex — exactly the enumeration already certified by the
     Vertex Pinning Lemma / Single-Piece-Split Vertex Lemma (ties among
     fragments, ties to an untouched landmark, or one free block).
  3. State the Existence Theorem in LP terms: for every point `p` of LB's
     balanced-region simplex, `min_π (vertex-optimum of π at p) ≤ c(n)`.
  4. Reduce this "for all `p`, some `π` works" claim to finitely many
     extremal `p`: each vertex-optimum is continuous (piecewise-linear or
     piecewise-rational) in `p` for fixed `π` and fixed vertex-shape; the
     finite min over `π` of continuous functions is continuous; a continuous
     function's sup over a compact region is attained, so it suffices to
     locate the (finitely many) boundary/tie configurations where the
     minimizing `π` switches and check those directly — the same
     extreme-point-reduction style Theorem 3 (slack-budget) and Theorem B
     (peeling, uniform in `n`) already used successfully.
  5. At the identified extremal configurations, verify directly (exact
     arithmetic, extending the Multi-Piece Necessity data already computed
     for `n=3..9`) that the best `π`'s vertex-value is `≤c(n)` — closing the
     Existence Theorem in full generality, not just at sampled points.
Key lemmas (claim + mechanism):
  - Piecewise-linearity of `OddSum` in fragment values for fixed `π` —
    because `OddSum`, via the `AltSum` reformulation, is a signed rank-count
    sum, linear in each fragment once the sorted rank order is fixed, and
    the order changes only at finitely many crossing hyperplanes (implicit
    already in the certified Vertex Pinning / Single-Piece-Split Vertex
    Lemma's enumeration).
  - LP-vertex attainment — standard fact (Fundamental Theorem of Linear
    Programming: a linear/piecewise-linear objective over a compact polytope
    attains its extremum at an extreme point); cited as a named tool, not
    re-derived.
  - Finite reduction of "for all `p` exists `π`" to finitely many extremal
    `p` (the delicate open step) — because a finite min of continuous
    functions is continuous and attains its extrema on a compact domain;
    turning this into an *explicit, checkable* finite list (rather than an
    unbounded search) is the real content still to be built, analogous to
    how Theorem 3/Theorem B located their own uniform-in-`n` extremal cases
    directly rather than searching.
Open gaps: everything past step 2 is new content. Steps 1-2 (piecewise-
linearity, vertex attainment) should be quick, near-immediate consequences
of already-certified lemmas. Steps 3-5 (the finite reduction and its
extremal-case verification) are the real, currently-unproved core. A key
sub-question, itself open: whether the set of candidate cut-patterns `π`
worth considering can be pruned to a small dominant family (matching
`universal-halving-adversary`'s best-of-{k1,k2,subset-tie}) before taking
the LP-vertex view, or whether the fully general `π` must be handled.
Cases to cover: enumeration of which `π` are even candidates for the
minimizer (exponentially many in principle; needs a pruning argument, not
brute enumeration).
Watch out for: this approach risks re-deriving the whole problem from
scratch if the builder doesn't reuse already-certified machinery (Vertex
Pinning, Theorem B, the Reduction Lemma) — the payoff is only real if the
LP-vertex enumeration is genuinely smaller/more tractable than "guess one
more named construction." If the vertex-shape enumeration turns out to
already coincide with best-of-{k1,k2,subset-tie}-plus-stray-cases (as this
round's numerics hint), this approach may collapse back into needing exactly
the Existence Theorem it's trying to avoid — the builder must report this
honestly rather than force a false sense of progress.

build set: lp-duality-split-polytope, self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, global-lp-vertex-sufficiency
