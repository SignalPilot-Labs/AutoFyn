## imo-2026-03 — lens: block-recursion-tievertex / Lemma UPM-5 (chorded even cycles)

### Precise statement of what's open
**Lemma UPM** (in `approaches/block-recursion-tievertex.md` §4): a square `t×t` `0/1` matrix `M'`
invertible over `Q`, with `M'v=d'` having a solution `v>0` pairwise distinct and `d'` a vector of
**distinct powers of two**, has a UNIQUE perfect matching in its bipartite incidence graph `B(M')`
(equivalently `det M' = ±1`, hence `v` integer). Proved: PM exists (UPM-1); unique-PM ⟺ no
alternating cycle w.r.t. any fixed PM (UPM-2, standard fact — see corpus match below); no two
columns identical / no length-2 alternating cycle (UPM-3, from invertibility); no "2-regular" (every
cycle-piece has *exactly* its two cycle values, no extra mass) even-cycle core, via the telescoping
identity `Σ_i(-1)^i 2^{a_i} = Σ_i(-1)^i(u_{i-1}+u_i) = 0`, impossible since exponents are distinct so
the term of smallest exponent can't cancel (UPM-4). **Open (UPM-5):** a chorded even cycle, i.e. a
cycle where some cycle-piece `P_i` carries EXTRA sub-piece mass beyond its two cycle values
(`u_{i-1}+u_i < 2^{a_i}` strictly). The telescoping then reads `Σ_i(-1)^i 2^{a_i} = Σ_i(-1)^i extra_i`
— a nonzero RHS, so positivity of the exponents' smallest term alone no longer forces a
contradiction. Verified exhaustively true for `n≤5` (up to 13800 cross-tie vertices, some containing
chorded cycles yet still unique-PM/det=±1), never proved in general.

### Distinct openings

1. **Pendant-elimination / Laplace-expansion induction (tempting, but genuinely blocked).**
   Unique-PM bipartite graphs are exactly those buildable by repeatedly deleting a degree-1 vertex
   and its unique neighbour (standard elimination-order characterization; equivalent to "no
   alternating cycle"). If `B(M')` has ANY row (piece) or column (value) of degree 1, Laplace
   expansion along it reduces `det M'` up to sign to a smaller `0/1` minor, and the induction would
   close UPM in one step *for graphs with no 2-core*. **Why this is not free:** deleting a
   degree-1-column (value `v_j` used by only one piece `k`) forces `v_j=2^k` (fine, power of two
   preserved for THAT variable), but if `v_j` is ALSO used as part of OTHER rows' equations
   (i.e. it's really a degree-1 COLUMN but the corresponding ROW has higher degree — need to expand
   along the correct axis), the reduced system's RHS for the remaining rows becomes `2^m - v_j`,
   which is generally **not a power of two anymore**. So plain pendant peeling breaks the
   power-of-two hypothesis needed to re-run UPM-4's argument on the reduced system — this is
   presumably *exactly* why UPM-5 (the genuinely 2-core / no-pendant case) is the hard residual: a
   graph with min-degree ≥ 2 on both sides has no pendant to peel at all, so this route only ever
   reaches the 2-core case, which is where UPM-4/UPM-5 already live. **Conclusion: peeling alone
   cannot avoid UPM-5; it can at best reduce to it.**

2. **Consecutive-ones / total-unimodularity from the geometric (stick) structure — the most
   promising fresh opening.** A classical fact (candidate KB addition — NOT currently in
   `knowledge_base.md`, should be added if used): a `0/1` matrix in which the `1`s of every ROW form
   a set of CONSECUTIVE columns (w.r.t. some fixed column order) is totally unimodular (TU) — every
   square submatrix has determinant in `{0,±1}` — independent of the RHS. This would prove UPM in
   one shot with NO case analysis on cycles, and would explain the round-4 empirical note that
   integrality "holds even for generic increasing integer RHS" (TU works for *any* integer RHS, not
   just powers of two). Sub-pieces of ONE original piece `2^k` are literally CONSECUTIVE
   sub-intervals of the stick before any further cut (Xiang Yu cuts a single interval into
   consecutive pieces) — this is exactly the geometric fact Lemma BD already exploits
   ("rank-contiguous run"). The open question is whether, ordering the `t` distinct VALUES by rank
   (descending), each piece's set of value-columns is an interval `[i_min(k), i_max(k)]` — i.e.
   whether cross-tie value-sharing respects this linear order, not just same-piece contiguity.
   **This is unverified — flag as the single most promising and most tractable-looking route,** but
   it needs an actual geometric argument (or a counterexample) connecting stick position to value
   rank; it is *not* automatic (see caution #4 below — abstract 0/1 matrices with degree ≥2 rows can
   easily fail consecutive-ones, e.g. any genuine closed alternating cycle is NOT interval-representable
   by rows, since a cyclic incidence pattern can't be linearized into intervals without wraparound —
   this actually matches UPM-4/5's cycles being exactly the hard case, so establishing
   consecutive-ones would automatically kill closed cycles, chorded or not, in one blow).

3. **Superincreasing strengthening.** The RHS is not merely "distinct powers of two" but
   *superincreasing* (`2^{a_max} > Σ_{smaller a} 2^a`), a much stronger property than plain
   distinctness. UPM-4's telescoping only used "distinct exponents ⇒ unique smallest term survives."
   A finer argument might isolate the row of LARGEST exponent among the `t` chosen pieces and use
   `2^{a_max} > `sum of every other row's total budget to pin at least one value adjacent to that row
   uniquely, then induct downward on `a_max`. This is essentially a refinement of opening #1 (a
   "peel from the top" induction) but exploiting superincreasing-ness rather than a naive pendant
   search, which might survive even when min-degree is 2 everywhere. Untested, but a natural next
   step if #2 doesn't pan out.

4. **Caution — an explicit counterexample refutes "generic RHS" claim.** I built and verified
   (`numpy`, det + matrix-vector check) a `3×3` `0/1` matrix `M=[[1,1,0],[0,1,1],[1,0,1]]`
   (a genuine chordless 2-regular 3-piece/3-value cycle, `det M = 2`) with `Mv=(3,5,4)` for
   `v=(1,2,3)` — a **positive, pairwise-distinct integer solution to a non-unimodular `0/1`
   system**, i.e. det=2 ≠ ±1 despite a fully valid positive/distinct integer RHS. This directly
   contradicts a bare "0/1 matrix + positive distinct solution ⇒ unimodular" claim for GENERIC
   RHS — powers-of-two (or at least superincreasing) structure on the RHS is NOT incidental, it is
   load-bearing. (Consistency check: the same cycle equations with a genuinely superincreasing RHS
   `(1,2,4)` give `v1=1.5`, non-integer/infeasible-positive — matches UPM-4's claim that
   2-regular cores are infeasible under powers-of-two RHS.) **Recommendation for the outliner/builder:
   do not trust or repeat round-4's "confirmed for generic increasing integer RHS" note as evidence
   that UPM-5 is RHS-independent — my counterexample shows a *generic distinct-integer* RHS is not
   sufficient in general; whatever holds for the actual problem's vertices must be using either the
   geometric consecutive-ones structure (opening #2) or genuine superincreasing-ness (opening #3),
   not "any distinct RHS."** This does not refute UPM-5 itself (which is specifically about
   powers-of-two / the actual polytope vertices) — it refutes an over-generalization noted in the
   round-4 build report as a possible easy shortcut.

### Assessment of §2 (within-piece-tie elimination) — LIKELY FLAWED, same failure mode as Lemma W

This is a significant finding, not just a "shared risk" flag. §2 claims: holding all other pieces
fixed, minimizing `σ_a·f_block(w)` over `Δ_k∩chamber` reaches a vertex pinned EITHER by `w_j=0`
(degenerate) OR by `w_j` tying to a value from a **different** piece (external/cross tie) — i.e. it
asserts within-piece ties always reduce away, terminating only at degenerate/tie-free/cross-tie-only
minimizers.

I re-derived the actual round-4 counterexample `{2,3,3}` (n=3: piece1={1}, piece2={2}, piece4={2,2},
piece8={2,3,3}, multiset sorted `3,3,2,2,2,2,1`, `f=3−3+2−2+2−2+1=1`) directly against this claim.
Perturbing piece8's tied pair `(3,3)→(3+t,3−t)`, holding everything else fixed: for small `t` the
sort order is unchanged (`3±t` both stay above the `2`-block), and by Lemma BD the block's
contribution is `σ_1·((3+t)−(3−t)) = 2t` for `t>0` but flips to `σ_1·((3−t)−(3+t))=−2t=2|t|` for
`t<0` (the top/bottom roles inside the block swap at `t=0`) — i.e. `f(t) = f(0) + 2|t|`, a **strict
V-shaped kink at `t=0`, exactly as in the refuted Lemma W**. This shows `t=0` (the tie `w=w'`) is
itself a genuine FACET of the sort-chamber — a boundary between the "`w2>w3`" and "`w2<w3`"
sub-chambers of the SAME piece — that §2's dichotomy (only `w_j=0` or **external** tie) does not
list as a valid terminal vertex type. Also, piece4={2,2} is pinned by exactly this same mechanism
(its 1-dimensional ordered sub-simplex `{w1≥w2≥0, w1+w2=4}` has genuine endpoints at `w2=0`
(degenerate) and `w1=w2` (**internal** tie) — the internal tie endpoint is a real vertex of that
1-dim polytope, not reducible further within piece4 alone).

**Conclusion: §2 as written likely has the identical gap that sank `self-similar-recursion`'s Lemma
W (round 4) — same-piece ties CAN be genuine terminal vertex facets (not just external-tie or
zero facets), so case (c) does not fully reduce to (a)/(b)/(d).** If confirmed, `block-recursion-
tievertex`'s scope is narrower than claimed: §3's cross-tie/UPM machinery only ever applies to
minimizers with NO surviving within-piece tie, but such minimizers (e.g. `{2,3,3}`) genuinely exist
and are NOT visited by §1-§3 as currently cased. This is a real gap **in addition to** UPM-5, and
should be flagged to the outliner/builder as a priority to patch (either extend the vertex taxonomy
in §2 to include internal-reordering ties as a valid terminal case, handling them directly — note
`{2,3,3}` gives an ODD INTEGER `f=1` anyway, so a targeted argument for "mixed" minimizers via a
generalized Lemma BD + a parity/integrality argument on top of the *within*-tie block's own affine
structure may close this small case cheaply — or show it never actually survives as a *global*
minimizer by a sharper argument than Lemma W's, e.g. combining the within-tie kink with the
cross-tie mass constraint it interacts with).

### Candidate technique(s)
- Bipartite unique-perfect-matching ⟺ no-alternating-cycle criterion (standard; matches corpus
  `aimo-1002`'s symmetric-difference-of-two-matchings-decomposes-into-alternating-cycles argument).
- Consecutive-ones / interval-matrix total unimodularity (classical LP fact, not yet in KB — worth
  adding as a named entry if the outliner commits to opening #2).
- Laplace/cofactor expansion along a degree-1 row/column (standard linear algebra) — useful but
  insufficient alone (see opening #1's caveat).
- `aimo-0151`'s fact "2-regular bipartite graph = disjoint even cycles, each contributing 2 PMs" —
  directly matches and cross-validates UPM-4's exclusion mechanism (positivity + distinct exponents
  kill the "2 PMs" outcome for THIS cycle type).

### Knowledge-base entries to use
- Hall's marriage theorem / SDR (`knowledge_base.md` line ~122) — background for PM existence,
  already used implicitly in UPM-1; cite explicitly if formalizing.
- No existing KB entry for total unimodularity / consecutive-ones — if opening #2 is pursued, this
  should be added as a new named lemma once proved (with citation to the classical TU criterion), not
  invoked as an unproven "well-known fact" per the rigor rules (no-hand-waving).

### Analogous past problems (cruxes)
- **`aimo-1002`** (unique domino-tiling marking problem) — crux: *"Superimpose a perfect matching
  with its reflection... red/blue alternating cycles whose per-cycle swap produces another valid
  configuration."* This is precisely the "symmetric difference of two distinct PMs decomposes into
  alternating cycles, and each cycle can be independently flipped to get a genuinely different PM"
  argument underlying UPM-2's "unique-PM ⟺ no alternating cycle" criterion. Directly reusable as the
  formal justification for that step (currently stated as folklore in the approach file — this
  crux gives the exact proof pattern to cite/adapt).
- **`aimo-0151`** (Onewaynia one-way-road problem) — crux: *"Count perfect matchings of a 2-regular
  bipartite graph by decomposing into even cycles, each contributing an independent factor of two."*
  Confirms/cross-validates that a 2-regular bipartite graph (UPM-4's setting) generically has exactly
  2 PMs unless some extra constraint (here: positivity + distinct powers of two) kills one of them —
  exactly the shape of UPM-4's argument. Good as a sanity-check citation, not a new technique.
- No corpus problem closely resembles UPM-5's "chorded even cycle with extra mass, RHS = distinct
  powers of two" configuration specifically — the powers-of-two/superincreasing flavor combined with
  a matching-uniqueness question appears to be a genuinely novel combination for this problem; do not
  force a further match.

### Prior progress
Everything up to UPM-5 is proved and reviewer-verified per `current.md`/round-4 review: reduction
`(∗)`, square-system extraction, `det=±1 ⇒ integer`, PM existence (UPM-1), length-2 exclusion
(UPM-3), 2-regular exclusion (UPM-4). Only UPM-5 (chorded even cycles) is open, verified
exhaustively `n≤5`.

### Dead ends (do not retry)
- Plain pendant/degree-1 elimination as a standalone closing argument for UPM-5 — it only reaches
  cases with a pendant vertex, which are already covered implicitly by UPM-3/4's style of argument;
  it cannot touch genuine 2-core (min-degree-≥2) chorded cycles, i.e. it cannot avoid UPM-5, only
  reduce to it (see opening #1).
- Treating "positive distinct solution + distinct/generic integer RHS ⇒ unimodular" as a free fact —
  REFUTED by an explicit 3×3 counterexample (det=2, `Mv=(3,5,4)`, `v=(1,2,3)`); the power-of-two /
  superincreasing structure is essential, not incidental (see opening #4). Do not repeat round-4's
  "confirmed for generic RHS" framing as if it settles RHS-independence in general.
- (Carried from round 4, still valid) Lemma W (within-piece-tie-p1) and Lemma T
  (forest-vertex-integrality) as stated — REJECTED, do not re-propose.

### Small-case / intuition notes (conjectural, numerically supported)
- UPM-5 verified true for all pure-cross-tie vertices at `n≤5` (exhaustive `n≤4`, random sample
  `n=5`) — strong evidence the lemma is true, not a hint about *why*.
- The `{2,3,3}`-type minimizer is NOT covered by §3's premises at all (it retains a within-piece
  tie) — its own `f=1` is an odd integer, so IF §2 is patched to handle it as an explicit extra case
  (rather than claiming it reduces away), the fix may be cheap: a direct argument that any surviving
  within-tie block, when combined with Theorem F applied block-by-block via Lemma BD, still yields
  an integer (or at least `f≥1`) — this is conjectural, untested this round, flagged as a concrete
  next probe for whichever approach owns the within-tie case.
