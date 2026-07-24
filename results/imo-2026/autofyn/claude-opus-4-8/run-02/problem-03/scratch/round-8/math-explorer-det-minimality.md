## imo-2026-03 — lens: minimality ⇒ |det U|=1 on the visible reduced subsystem

### Precise linear-algebra statement of the target
At the Φ=Σx_i²-maximal non-degenerate global minimizer P* of a step of the induction, let `w_1>…>w_p`
be the distinct sub-piece values, `C_j` their tie-blocks (ranks `[a_j,a_j+μ_j-1]`), `U` the
`(n+1)×p` incidence matrix `U_{k,j}=μ_{k,j}` (# sub-pieces of piece `2^k` equal to `w_j`), `b=(2^0,…,2^n)`.
Certified: `Uw=b`, `ker U={0}` (S-core), `f(P*)=Σ_j s_jw_j` with `s_j=σ_{a_j}` (odd `μ_j`) or `0` (even
`μ_j`) (BF). By Lemma CRAMER (certified, square case `p=n+1`): `f·det(U)=Σ_j s_j det(U_j)=:M∈ℤ`, so
`f=M/det(U)` — a Cramer ratio. **|det U|=1 ⟹ f∈ℤ**, but is NOT necessary in general and is literally
FALSE on raw `U` at genuine minimizers: even (`s_j=0`) matched-pair columns `2·e_k` force `m|det U`
(Lemma 1, concentration-exclusion), giving `|det U|` even (verified: `gcd=2` at the `n=3` minimizer
`{3,3,2,2,2,2,1}`). The Reduction Lemma (certified) shows these invisible columns *peel off exactly*
(delete piece-row `k` and column `j`, `f` and every other `w_i` unchanged, `det U=±2·det U'`), leaving a
strictly smaller **visible reduced subsystem** `U^★` (only odd-size/visible classes, no concentrated
column). **The target is `|det U^★|=1`** (square) / coprime maximal minors (rectangular) — equivalently,
by the graph-theoretic dictionary (peeling a `2×e_k` or `1×e_k` column ≡ peeling a degree-1 piece-leaf
of the bipartite incidence multigraph `H`), **`U^★` benign ⟺ the 2-core of `H` (after all leaf-peeling)
is empty ⟺ `H` is a forest ⟺ no cycle survives**. This is EXACTLY self-similar's Gap A′ (after Gap B
excludes the one leaf-shape, `μ=3`, that peeling can't reach) — confirming Cramer/concentration/primal
are the SAME fact, not three facts. **So: Gap 1 (concentration route) ≡ Gap A′ (primal route) ≡ (D′)
minus the Budget Lemma (dual route), all literally the statement "H has no cycle with a degree-≥3
cycle-piece."** Φ-maximality enters only through S-core (kills value-class shifts, i.e. `ker U=0`) and
through M2/M3 (bound within-piece multiplicities `≤3`, force odd blocks to `μ=1`) — minimality/Φ-max
do NOT by themselves touch the *cyclic* structure; that is the open residual.

### Distinct proof openings (NOT the dead circulation V-kink)

1. **Verified NEGATIVE (this round, numeric): the natural "M4-generalization" (pairwise transfer
   between ANY two distinct sub-piece values of one piece, dropping M4's odd-odd restriction) is ALSO
   a V-kink, not a fresh lever.** I hand-derived the per-copy Lemma-I slope for a mixed-parity pair
   and it predicted a strict descent at the certified minimizer `{3,3,2,2,2,2,1}` (piece8=`{3,3,2}`,
   values `3` even-block and `2` even-block) — but this used a FIXED rank ordering valid only for one
   sign of `δ`; re-sorting correctly for both signs gives (verified numerically, `python3`):
   `f({3+δ,3,2−δ,2,2,2,1}) = 1+2|δ|` for `δ∈{±0.01,±0.1,±0.2}` — i.e. **exactly the same V-kink** as
   the certified circulation carve-out. So a *naive* extension of M2/M3/M4 to mixed/even-block pairs
   in one piece is DEAD (re-derives, not escapes, the wall) — record this so nobody retries it as if
   fresh. (Do trust the *certified* M4 as stated — restricted to two ODD blocks, where the rank
   ordering stays fixed on both sides of `δ=0` because interior copies bound the block on both ends;
   that special case is genuinely different and already proven.)

2. **Most promising: a UNIFIED degenerate-domination lemma (extend Lemma BD to cover Gap A′ too).**
   Both surviving residuals — Gap A′ (deg-≥3 cycle-piece) and Gap B (μ=3 even leaf) — independently
   turn out to be **inherently budget/minimality facts that no local variational move can touch**: Gap
   B has an explicit `f=1/3<1` over-budget witness (round 7, certified negative), and this round's
   check shows the natural local moves at deg-≥3 cycle-pieces are V-kinks just like Gap B's local moves
   are V-kinks. This parallel strongly suggests ONE mechanism closes both: construct, for ANY surviving
   deg-≥3-cycle-piece OR μ=3-leaf configuration at the Φ-max minimizer of a `≤N`-cut instance, an
   EXPLICIT **degenerate competitor** `P'` (a `≤N−1`-cut refinement, i.e. one sub-piece driven to length
   `0`) with `f(P')=f(P*)` EXACTLY — then Claim(N−1) (already proved) gives `f(P*)=f(P')≥1` directly,
   with NO determinant/kernel argument needed at all. This is the outline's already-flagged "Lemma BD"
   for Gap B; the new suggestion is to seek the SAME kind of degenerate-competitor construction for
   Gap A′ (e.g. shrink the offending chord/off-cycle sub-piece to `0`, redistributing its mass along the
   cycle in the unique way that keeps `f` flat — this is a *large*, not infinitesimal, move, unlike the
   dead local levers, and is exactly the kind of move the Gap-B analysis (`bisect-instead`,
   `symmetric-to-degenerate`) tried but only as one-liners). **Untried, concrete next step:** for a
   chorded/off-mass cycle, walk the (unique) circulation direction not infinitesimally but ALL THE WAY
   to where one sub-piece hits `0` (the boundary of the simplex), and check whether `f` is flat along
   the WHOLE segment (not just to first order) — the V-kink result says `f` is *not* flat near `δ=0` on
   BOTH sides (it strictly rises both ways), so a degenerate competant with EQUAL `f` is not reachable
   by circulation alone; but a genuinely two-parameter move (circulation AND a value-class shift
   together, since off-cycle attachments give extra simplex dimensions unused by pure circulation) might
   trace a flat curve to the boundary. This is the concrete unexplored generalization.

3. **Asymmetric partial-circulation (untested, structurally distinct from the dead symmetric
   circulation).** The certified V-kink move splits BOTH cycle-adjacent copies of a cycle piece
   symmetrically (`+δ`/`−δ` on `Q_{i-1}`,`Q_i`). For a deg-≥3 piece with an *extra* off-cycle or chord
   sub-piece `w_off`, an untried alternative is transferring mass between `w_off` and ONLY ONE
   cycle-neighbor (leaving the other cycle-neighbor fixed) — a genuinely different feasible direction
   in that piece's simplex (dimension ≥2 there, vs. dimension-1 for the pure-cycle case), not covered
   by the round-7 "natural circulation" test. Not verified this round (time-limited); flag as the
   cleanest remaining local lever nobody has tried.

4. **Rank-contiguity / global-count argument (distinct machinery, not yet tried).** Since every value
   class occupies a *contiguous* rank interval and every piece's sub-pieces sum to a power of 2, a
   cycle in `H` induces a closed walk through rank-intervals; one could try a **pigeonhole on rank
   positions** around the cycle (e.g. count how many rank-boundaries the cycle's components must
   collectively straddle, forced by the strictly-decreasing values `w_1>…>w_p`, versus the number
   available from `n+1` pieces) to get a size/counting contradiction independent of the algebraic
   `ker U`/superincreasing machinery used so far. This is genuinely different in flavor (combinatorial
   counting vs. linear algebra) and untested.

### Cheap-kill candidates
- Parity/size counts on `μ_{k,j}∈{1,2,3}` (already certified, M2) rule out `m≥4` cheaply — no new
  mileage there.
- A quick necessary condition worth checking before heavy work: for a deg-≥3 cycle-piece, the
  **number of edges vs. nodes** in the cycle-plus-attachment subgraph — if the attachment count forces
  more independent columns than available rows (`p>n+1`), S-core (`ker U=0`, so `p≤n+1`) already kills
  it outright without any variational argument. Worth an exhaustive small-case check (n≤4) of whether
  EVERY concrete deg-≥3-cycle instance that is otherwise consistent with S-core's dimension bound
  really occurs, or whether the dimension count alone already excludes most/all of them — this was not
  explicitly isolated as its own cheap filter in prior rounds (M2/M3 bound multiplicities but nobody
  checked the raw `p≤n+1` count against the cycle's own component/piece count for deg-≥3 shapes).

### Knowledge-base entries to use
- **Cramer's rule / determinant solution of a linear system** (Linear Algebra section) — already the
  backbone of Lemma CRAMER; no new KB entry beyond what's cited.
- **Rank / image / kernel — common nonzero vector in shared kernel** (Linear Algebra) — matches the
  S-core mechanism (feasible-shift `d∈ker U`) already used; nothing further to add.
- **Extreme value theorem / Lagrange multipliers on a compact manifold** (Linear Algebra section) —
  the general template behind the Φ-maximal-selection device; already exploited, but its
  "ideal-saturation + Gröbner normal form" follow-on (used elsewhere in the KB for stationarity ideals)
  is NOT yet tried here and could in principle certify "no all-positive solution of the closed
  chorded-cycle system" symbolically for a family of shapes instead of case-by-case (0/32, 0/12
  verification) — a candidate for turning the honest exhaustive verification into a real proof.
- No KB entry on total unimodularity / network matrices applies (already correctly ruled out, round 5
  — `μ` up to 3 breaks the `{0,±1}` entry requirement of classical TU theorems).

### Analogous past problems (cruxes)
Searched `linear-algebra-method` and `extremal-principle` subtopics (combinatorics + relevant others)
in the crux corpus for determinant/unimodular/incidence/forest/cycle techniques. Found:
- **aimo-0450** (`symmetric-functions-and-substitution`): "unimodular array" where every 2×2 minor is
  `±1`, solved via a LOCAL-to-GLOBAL filling argument (fix an 8-entry 3×3 grid, deduce the 9th entry is
  forced integral via a coprimality congruence). Thematically close (unimodularity forced by an integer
  arithmetic identity) but the mechanism (local congruence propagation on a fixed combinatorial grid) is
  NOT analogous to our situation (our `U` isn't a fixed grid — it's a variable-shape incidence multigraph
  whose shape itself is the unknown). Not a strong match; noted for the "arithmetic force integrality"
  flavor only.
- **aimo-0950** (`extremal-principle`, spanning-tree color-count problem, RMM): uses an
  induction-plus-exchange argument among spanning trees of a graph with prescribed color counts. Only a
  distant topical analogy (graph/tree exchange under an extremal count) — could inspire framing Gap A′
  as a matroid/tree-exchange question (is there always an EXCHANGE from the actual `H` toward a forest
  that keeps `f` unchanged?), but no concrete technique transfers directly.
- **aimo-0180** (`extremal-principle`+`bijections-and-encoding`): unit-determinant `|a_ib_j-a_jb_i|=1`
  lattice-triangle counting — genuinely about `2×2` unimodularity but in a totally different
  (geometric/counting) context; no transferable mechanism.
- **Conclusion: nothing in the corpus is a genuine analogue of "minimality forces a variable-shape
  incidence matrix built from powers of two to be unimodular."** This appears to be a bespoke
  structural fact of this problem, not a standard crux move — the KB's Cramer's rule and kernel
  arguments (already in use) are the closest generic tools available.

### Prior progress
Exactly as stated in run_state.md/current.md: upper bound fully certified; lower bound reduced (LBL) →
{Gap A′: cycle with a deg-≥3 cycle-piece} ∪ {Gap B: μ=3 even leaf} (primal) ≡ {Gap 1: benign visible
subsystem} ∪ {Gap 2: Positivity now = Budget Lemma} (dual/concentration). ~24 lemmas certified. Numerically
`min f=1` confirmed n≤4.

### Dead ends (do not retry)
- Circulation feasible direction (symmetric `±δ` on the two cycle-neighbors of a cycle-piece) — V-kink,
  certified round 7.
- **NEW this round, verified: the naive generalization of M4 to a pair of distinct sub-piece values
  in one piece where NOT both blocks are odd (e.g. both even, or one odd one even) is ALSO a V-kink** —
  confirmed by direct computation on `{3,3,2,2,2,2,1}`'s piece8 `{3,3,2}`: `f=1+2|δ|` for both signs of
  `δ`. Do not re-propose "extend M4 to arbitrary pairs" as a fresh lever — it reproduces the same wall.
- "benign-U = det/gcd = ±1" on raw `U` — false (round 7, even matched-pair columns make gcd even).
- Consecutive-ones/TU, Jacobsthal-decrement driver, laminar geometry, λ₀-parity Positivity — all
  previously refuted, still dead, not re-examined here (out of scope for this lens).

### Small-case / intuition notes (conjecture, labeled)
- The V-kink phenomenon recurring at BOTH Gap A′'s natural local move and Gap B's natural local moves
  (and now also at the naive M4-extension) is itself suggestive evidence (not proof) that the true
  closing mechanism is a **global inductive/degenerate-competitor** one (opening 2 above), not a local
  first/second-order variational one — every local lever tried so far produces a V-kink, i.e. `P*` really
  is a genuine local min/max along every 1-parameter feasible line found, so the excluding argument must
  be non-local (compare `P*` against a DIFFERENT combinatorial type entirely, which is exactly what
  Claim(N−1)-via-degenerate-competitor does).
- No new numeric enumeration of Φ-max minimizers for n=2,3,4 was run this round beyond the confirmatory
  hand-check above (time budget spent on the derivative/V-kink verification instead, which directly
  refutes a candidate lever rather than just confirming known facts) — recommend next round's builder
  spend compute on tracing the FULL (not infinitesimal) circulation-plus-shift curve to the simplex
  boundary for a synthetic chorded-cycle instance, to test opening 2 concretely.

### Most promising opening to close this wall
**Opening 2** (unified degenerate-domination / extend Lemma BD to also produce a degenerate competitor
for deg-≥3-cycle-piece configurations) — because the parallel V-kink structure between Gap A′ and Gap B
is now doubly confirmed (their independent local moves AND the naive M4-generalization all V-kink), and
Gap B's certified honest analysis already establishes that ONLY a global budget/degenerate argument can
work there; the same logic very plausibly applies to Gap A′. A single generalized Lemma BD closing both
gaps at once would finish the whole problem.
