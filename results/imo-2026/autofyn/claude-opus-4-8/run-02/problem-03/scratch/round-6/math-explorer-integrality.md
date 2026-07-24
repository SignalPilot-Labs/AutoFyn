## imo-2026-03 — LENS: integrality residual (Gap A acyclicity, Gap B μ=3 even-block leaf)

### Distinct openings

1. **(NEW this round, confirmed by direct computation) The abstract linear-algebra data
   (μ_{k,j}∈{1,2,3}, ker U=0, M3 odd-block≤1, M4 no-two-odd-blocks-per-piece) is PROVABLY
   INSUFFICIENT to force Gap A — any proof must additionally use the geometric
   rank-contiguity of the stick-cutting process.** I built the 3-piece/3-value "2-regular"
   cycle system (the exact UPM-4 core shape) with private (unshared) extra mass `e_i≥0`
   siphoned off each cycle piece before the cycle's own conservation equation:
   `v3+v1=2^{a1}-e1`, `v1+v2=2^{a2}-e2`, `v2+v3=2^{a3}-e3}`. Solved numerically over
   `a1<a2<a3≤6` and a grid of `e_i` fractions: **479 combinations give a positive,
   pairwise-distinct solution `v`** (e.g. `a=(0,1,2)`, `e=(0,0,0.3·4)`, `v≈(0.1,1.9,0.9)`),
   i.e. a genuine "chorded 2-regular even cycle" with distinct-powers-of-two piece budgets
   IS abstractly realizable once extra mass is allowed — confirming that UPM-4's clean
   telescoping argument (which excludes the *pure*, no-extra-mass 2-regular case) cannot be
   naively strengthened to the chorded case by multiplicity/kernel data alone. This means
   **Gap A's remaining content is NOT a pure linear-algebra/graph fact** — it must use that
   the "extra mass" pieces are geometrically constrained (their values occupy specific
   RANKS in the global sorted order, and a piece's own sub-pieces are contiguous stick
   segments), a constraint totally external to the incidence matrix `U`. This is a
   strengthened, freshly-verified version of round-5's "opening #2" caution (previously
   only a worry about a 3×3 counterexample with *generic* RHS; I've now shown the
   counterexample survives even restricted to genuinely superincreasing-flavored,
   powers-of-two piece budgets, once chording/extra-mass is allowed).

2. **Candidate fresh technique: aimo-0913's "longest-edge-exceeds-sum-of-shorter-admissible-
   edges ⇒ acyclic" argument — a genuinely new corpus match, not yet surfaced by prior
   explorers.** (See corpus below.) The shape is tantalizingly close to what Gap A needs:
   in aimo-0913, a graph built from a difference condition (Fibonacci gaps) is shown acyclic
   by picking the longest cycle-edge and noting the *other* cycle edges' lengths are
   *distinct* and *smaller*, so their sum (telescoped via `F_1+F_3+…+F_{2m-1}=F_{2m}<F_{2m+1}`)
   cannot span the longest edge — a direct superincreasing-style triangle-inequality
   contradiction. I attempted to port this literally to Gap A (bounding `μ_1u_1+μ_r'u_r`,
   the two cycle-contributions at the max-exponent piece, by the sum of ALL other cycle
   pieces' full masses) but the direct port is NOT strong enough: with only 2 endpoint
   pieces the bound is `2^{a_1}+2^{a_{r-1}} ≤ 2^{a_max-1}+2^{a_max-2} = (3/4)2^{a_max}
   < 2^{a_max}`, which only shows the max piece has *positive* leftover extra mass — i.e.
   it is CONSISTENT with a chord, not a contradiction. The aimo-0913 argument crucially uses
   that ALL cycle edges (not just the two touching the longest) are bounded and telescope
   to exactly `F_{2m}`, achieving a *tight* inequality; the Gap-A analogue would need a
   similar full-path telescoping (not just the two neighbors of the max piece) — plausible
   direction but requires re-deriving the right invariant (perhaps an alternating-sign sum
   over the whole cycle path analogous to UPM-4, generalized to include intermediate extra
   mass terms with signs, rather than one-directional magnitude bounds). **Not solved; flag
   as the single most promising unexplored formal technique**, distinct from consecutive-ones/TU.

3. **Gap B — no fresh global argument found this round; report on why the "obvious" competitor
   constructions fail to close it cheaply.** I tried the natural direct competitor: replace a
   μ=3 even-block leaf `2^k={v,v,v}` (`v=2^k/3`) by a bisection `{2^{k-1},2^{k-1}}` and check
   whether this ever preserves `f=m` exactly while raising `Φ`. This is NOT a valid move in
   general because bisecting changes the RANK POSITIONS globally (the new values `2^{k-1}`
   may not tie with the same tie-block the old `v`'s did) — so `f` is not obviously preserved;
   it needs case analysis on where `2^{k-1}` falls in the sorted order relative to everything
   else, which is exactly the "global" difficulty flagged in current.md. This is a genuine
   dead end as a LOCAL/uniform recipe (do not present a bare "just bisect instead" move as a
   proof) — any correct Gap-B argument needs to track the new value's rank explicitly, likely
   piece-by-piece via Lemma BD (rank-contiguous block decomposition) rather than a one-line swap.

### Candidate technique(s)
- **aimo-0913-style longest-edge/superincreasing-telescoping acyclicity argument** (opening 2)
  — fresh, not yet in the population's toolkit; needs a full-cycle (not two-endpoint) version.
- Consecutive-ones / total unimodularity from stick-geometry (round-5 opening #2, still
  unclosed, but now CONFIRMED necessary — my computation (opening 1) shows the pure
  multiplicity/kernel data is insufficient without it, so this or an equivalent geometric fact
  is not optional).
- For Gap B: a genuine "global Φ-domination via rank-tracked competitor" (no cheap uniform
  recipe found; needs Lemma BD applied piece-by-piece to whatever new rank the competitor's
  value lands at).

### Cheap-kill candidates
- None found this round that close Gap A or B outright. The one useful negative cheap-kill:
  **do not attempt a "kernel + multiplicity bound ⇒ forest" argument without also invoking
  geometric rank-contiguity** — confirmed abstractly insufficient (see opening 1's 479
  counterexamples). This should save the outliner/builder from re-attempting a pure
  linear-algebra closure of Gap A.

### Knowledge-base entries to use
- No `knowledge_base.md` entry directly covers unimodularity/consecutive-ones or the
  "longest-edge exceeds sum" acyclicity technique (grep confirms `knowledge_base.md` has only
  Hall's theorem / SDR under matching-adjacent material, line ~122). If opening 2 or the
  consecutive-ones route is pursued and succeeds, it should be added as a new named KB entry
  (per rigor rules — do not invoke as unproven folklore).

### Analogous past problems (cruxes)
- **`aimo-0913`** (Croatia, Fibonacci-difference set minimum size) — crux: *"Prove an edge
  set on the integer line is acyclic by showing the longest edge length strictly exceeds the
  sum of all admissible shorter edge lengths, so the triangle-inequality path around any cycle
  cannot reach across the longest edge."* This is the closest genuine structural analogue found
  to date for Gap A (closer than the previously-cited `aimo-1002`/`aimo-0151`, which only supply
  the generic "unique-PM ⟺ no alternating cycle" folklore, not a superincreasing-specific
  acyclicity mechanism). Adapting it is NOT immediate (see opening 2's caveat) but it is a
  genuinely novel, unexplored lead for this population.
- `aimo-1002`, `aimo-0151` (previously found, still valid as folklore justification for
  "unique-PM ⟺ no alternating cycle," not as a closing technique) — do not re-present as new.
- `aimo-0281` (pentagon solitaire game) — crux: confirming integer solvability of a reduced
  linear system via a congruence identity that is exactly the invariant's own condition. Only
  loosely analogous (a linear-system-integrality flavor, no cycle/matching structure); not a
  strong match, noted for completeness but not recommended as a primary lead.

### Prior progress
Both Gap A and Gap B remain exactly as characterized in `current.md` / round-5 reports:
Gap A ≡ block-recursion's UPM-5 (chorded even cycles), Gap B = μ=3 even-block piece-leaf
exclusion. All of §0–§4 of `self-similar-recursion` (Lemma S-core, M2, M3, M4, block formula)
are sound and certified; nothing in this lens changes their status. Round-5 explorers already
identified: pendant elimination (insufficient, reduces to but can't avoid UPM-5); consecutive-
ones/TU (promising but unverified, and now shown necessary not just sufficient by my
computation); superincreasing peel-from-top (untested refinement of pendant elimination); and
flagged §2 (within-piece-tie elimination in `block-recursion-tievertex`) as LIKELY FLAWED with
the same failure mode as the refuted Lemma W (a genuine V-kink at internal ties, e.g. the
`{2,3,3}` example) — this should be treated as an open concern, not settled, for any approach
relying on block-recursion's §2.

### Dead ends (do not retry)
- Consecutive-ones/TU and generic-RHS unimodularity as previously REFUTED framings — per
  dispatch instructions, not retried here.
- Odd-integer floor at tied vertices, global integrality of all minimizers — REFUTED, not
  retried.
- **(This round, confirmed)** A pure kernel/multiplicity-bound (ker U=0 + μ≤3 + M3 + M4)
  argument for Gap A's acyclicity, with NO geometric/rank input — refuted abstractly by an
  explicit 479-instance numerical family (2-regular chorded triangle-cycle with distinct
  powers-of-two piece budgets and private extra mass, admitting positive distinct solutions).
  Do not attempt to close Gap A from the incidence-matrix data alone; geometric rank-
  contiguity (or an equivalent) is provably necessary.
- A uniform "bisect the μ=3 leaf instead" competitor construction for Gap B — fails because
  bisection changes global rank positions unpredictably; not a valid one-line move (see
  opening 3).

### Small-case / intuition notes (conjectural except where marked exact)
- **(Exact computation, this round)** The 479-instance family in opening 1 shows the abstract
  graph fact underlying Gap A is FALSE without extra structure — this is a proven fact about a
  synthetic system, NOT a counterexample to Gap A itself (the real polytope's actual vertices
  still satisfy Gap A in all tested cases, n≤5, per round-5's exhaustive/random search) — it
  only shows *why* Gap A is hard: the true proof must use rank-contiguity, which the synthetic
  system deliberately omits.
- min f = 1 remains numerically confirmed at n≤4 (unchanged, not re-verified this round).
