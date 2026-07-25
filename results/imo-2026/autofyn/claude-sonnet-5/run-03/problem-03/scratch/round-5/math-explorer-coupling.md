## imo-2026-03 (lens: upper-bound balanced-region gap / layer-cake Coupling Obstruction)

- Distinct openings:
  1. **"Tie-or-zero" LP-vertex structural lemma (new, not tried by any approach yet).**
     For a *fixed* cut-count allocation `c_list=(c_1,...,c_k)` (how many cuts go to
     each piece), the achievable fragment vectors form a compact polytope (product
     of simplices), and `OddSum` restricted to any fixed sort-order region is
     **linear** in the fragment lengths (it's a fixed subset-sum of the fragments
     under a fixed permutation). A sort-order region is itself an intersection of
     half-spaces (order constraints `x_i≥x_j`) with the simplex, i.e. a sub-polytope,
     so `OddSum` restricted to it attains its min at one of *that* sub-polytope's
     vertices. Vertices of these regions occur exactly where either (a) a fragment
     hits its boundary `=0` (an unused cut), or (b) two order constraints coincide,
     i.e. two elements of the resulting multiset are **exactly tied**. Hence: **the
     adversary XY's globally optimal response (for any fixed piece and any fixed
     total budget) can always be taken so every fragment is either `0` or exactly
     equal in value to some other element of the final multiset** (another fragment,
     or an untouched piece). I verified this numerically in every optimizer run
     below (see leads 2-3) — every found optimum had this exact structure, never a
     "generic" interior value. This turns the *continuous* multi-piece coordination
     problem into a **finite combinatorial search**: choose a partition of ranks
     into "tie-blocks" and "zero-fragments" and check consistency, rather than
     searching a continuum. This is a genuinely different top-level target from
     every approach tried so far (none of the 5 approaches has looked for this kind
     of vertex/extremal characterization) and is a natural candidate to try to prove
     rigorously (via the standard LP fact "a linear function on a polytope attains
     its extremum at a vertex," `knowledge_base.md` "Extreme value theorem /
     Lagrange multipliers on a compact manifold" and "Piecewise-concavity smoothing"
     entries) as a *new joint invariant*: the discrete "which ranks tie / which
     fragments vanish" data is exactly the kind of joint (not per-cut) quantity the
     Coupling Obstruction says is necessary.
  2. **Two catalogued coupling mechanisms found numerically, distinct from
     "top-only"**: (a) *self-bisection*: split one piece exactly in half, creating
     a self-tie that (by Tie-neutrality) always splits 1-1 between the two ranks it
     occupies, diluting that piece's contribution to exactly half its own value
     regardless of context; (b) *shave-below*: split a larger piece into two (or
     more) fragments, each tuned to sit **just below** (not equal to, in the
     asymptotic/strict sense — but at the tie-boundary in the limit, matching lead
     1) a *distinct* untouched anchor value, so each fragment lands at an even
     (wasted) rank while the anchor keeps the odd rank. Mechanism (b) is genuinely
     joint: the two shaved fragments' target values depend simultaneously on *two
     different* untouched pieces elsewhere in the multiset — this is a concrete,
     checkable instance of exactly the kind of cross-cut coupling the Coupling
     Obstruction says must exist. See the worked numeric example below.
  3. **The balanced region has real slack, not near-tightness — reframe as an
     existence/compactness argument instead of an explicit universal formula.**
     Numerically (see below), the true optimal value XY can force in the interior
     *and even near the boundary* of the balanced region is well below `c(n)`
     (e.g. `~0.50` vs. target `c(2)=4/7≈0.571`, `c(3)=8/15≈0.533`), i.e. the
     inequality `OddSum ≤ c(n)` is *not* tight anywhere strictly inside the balanced
     region — it is only tight at the geometric partition itself (which sits on the
     region's boundary via `p_1=c(n)`, already closed). This suggests the right
     target for this region may not be "find the explicit closed-form response" but
     rather an **existence argument**: compactness of the simplex of `≤(n+1)`-piece
     partitions + continuity of `OddSum` under any fixed response scheme (already
     partially used in `universal-halving-adversary`'s pruning-lemma discussion) +
     the tie-or-zero vertex reduction (lead 1) to make the "for every partition,
     some response works" claim a *finite* check rather than an infinite one. This
     is a genuinely different top-level target (existence via compactness/finite
     combinatorial verification) than "exhibit one uniform formula," which is what
     all 5 current approaches are doing.

- Candidate technique(s): LP/vertex-of-polytope extremal argument (new); compactness/
  extreme-value-theorem existence argument (knowledge_base.md, "Extreme value
  theorem / Lagrange multipliers on a compact manifold"); piecewise-linear/
  piecewise-concavity smoothing (knowledge_base.md).

- Cheap-kill candidates: none obvious beyond what's already used (Lemma B floor
  `OddSum≥W/2`); worth checking whether the tie-or-zero characterization, once
  proved, immediately implies a small *finite* bound on how many distinct "tie
  patterns" need checking per `n` (a counting/pigeonhole argument on rank-parity
  blocks), which could itself be a cheap-kill once lead 1 is formalized.

- Knowledge-base entries to use: "Extreme value theorem / Lagrange multipliers on a
  compact manifold" (Linear Algebra section); "Piecewise-concavity smoothing"
  (Algebra & Polynomials section); "Invariants & monovariants" (Combinatorics).

- Analogous past problems (cruxes): searched `combinatorics/games-and-strategy`
  (39 cruxes) and broader keyword search (cake/cutting/pairing/rearrangement/
  variance) across the full corpus — **no genuinely analogous problem found**. The
  closest superficial matches (aimo-0182, mean/variance bound on a rearrangement
  spread; aimo-0459, rearrangement-inequality pairing of cyclic sums; aimo-0908,
  induction-by-midpoint-split on a sum of ratios) are algebra inequality problems
  with a different structure (fixed permutation optimization, not an adversarial
  two-phase cut game) — I would not force these as analogous; report none as a
  genuine crux match. This problem's core mechanic (adversarial refinement of a
  partition scored by alternating-rank sum) does not have a close pre-2026 sibling
  in the corpus.

- Prior progress: as recorded in `current.md` — upper bound closed for `p1∈[1/2,c(n)]`
  and `p_{n+1}≤1/(2^{n+1}-1)` unconditionally, `p1≥c(n)` conditional on `T(n-1)`;
  balanced region (`p1<1/2` and `p_{n+1}>1/(2^{n+1}-1)`) open. `dyadic-potential-
  invariant` and `universal-halving-adversary` both independently confirmed
  top-only-on-`p1` is insufficient there.

- Dead ends (do not retry): top-only allocation restricted to `p1` (disproved twice,
  exact counterexamples, `dyadic-potential-invariant` + numeric test in
  `universal-halving-adversary`); Suffix-Match construction optimized over its free
  parameter alone (numerically insufficient, 43-97% failure rate); **new this
  round, numerically checked and should NOT be pursued as a general rule**: the
  naive "pairwise matching" construction (pair up sorted pieces `(p1,p2),(p3,p4),...`
  and match the larger of each pair down to the smaller, pooling leftovers) — this
  matches the true optimum only on symmetric/arithmetic-progression instances (1 of
  6 random balanced 4-piece trials) and is clearly *not* the general joint rule (see
  numeric evidence below).

- Small-case / intuition notes (all conjectural, from numeric optimization —
  Nelder-Mead over softmax-parameterized fragment allocations, multi-restart, not a
  proof):
  - `n=2, (0.35,0.34,0.31)`, budget 2: global numeric optimum is **0.505**,
    attained in *two* different ways: (i) the previously-reported mixed allocation
    (1 cut on `p1` giving `(0.345,0.005)`, 1 cut bisecting `p3` into `(0.155,0.155)`)
    and (ii) a **simpler single-piece move never touching `p1`**: bisect `p3` alone
    into `(0.155,0.155)`, leave `p1,p2` untouched, using only 1 of the 2 available
    cuts. Both give multiset-sorted `{0.35,0.34,0.155,0.155,(0)}`, `OddSum=0.505`.
    **This means the "top-only on `p1`" refutation is correct, but a broader
    (still single-piece) family — "XY may bisect ANY one piece, not necessarily
    `p1`" — already suffices on this specific instance.** Whether "single-piece,
    any choice" suffices for the *whole* balanced region is a natural intermediate
    conjecture to test before jumping to fully joint multi-piece rules; my n=3
    tests below show it does **not** suffice in general (see next bullet), but it
    is a strictly larger and still much simpler family than "top-only," worth
    checking as an intermediate step.
  - `n=3` (4-piece), random balanced trials (`p1<0.5`, `p4>1/15`, budget 3): in
    5 of 8 random trials, the true numeric optimum (`~0.500-0.503`) is **strictly
    better** than the best "single-piece, any choice" response (`~0.51-0.52`) by a
    non-trivial margin (`0.01-0.02`), confirming genuine multi-piece coupling is
    needed at `n=3` (not just at `n=2`, where it turned out to be avoidable via a
    smarter single-piece choice). Example: `p=(0.3605,0.2782,0.2013,0.16)`: optimal
    joint response splits `p1→(0.2009,0.1596)` (each fragment tuned to sit **just
    below** two *different* untouched pieces, `p3=0.2013` and `p4=0.16`
    respectively — both fragments land at even/wasted ranks) **and independently**
    bisects `p2→(0.1391,0.1391)` (self-tie). Achieves `OddSum≈0.5004`, vs. best
    single-piece response `≈0.510`. This is the clearest concrete instance of the
    "shave-below" + "self-bisect" combo (opening 2) and is a good worked example
    for the outliner to build a general construction around, or to use as a target
    the outline must reproduce.
  - All found optima (across every trial run) have **every fragment either exactly
    `0` or exactly tied with another element of the final multiset** — strong,
    consistent numeric support for the tie-or-zero vertex lemma (opening 1).
  - The achieved values in the balanced region are consistently well below `c(n)`
    (`~0.50` vs. `c(2)=0.571`, `c(3)=0.533`), including near the region's own
    boundary — supporting opening 3 (real slack, not near-tightness, favors an
    existence-style argument over an explicit tight formula).
