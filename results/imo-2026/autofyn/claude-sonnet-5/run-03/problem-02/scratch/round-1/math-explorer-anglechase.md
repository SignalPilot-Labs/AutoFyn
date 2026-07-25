## imo-2026-02

### Distinct openings (synthetic / angle-chasing / spiral-similarity lens)

1. **Reduce OM=ON to a fixed-point concyclicity.** Numerically (see below) the
   circumcircle of AKL, as (K,L) range over the whole family of points satisfying
   the three given angle equalities, always passes through a **second fixed
   point Q** (besides A) that does **not** depend on which valid (K,L) is chosen.
   Q is exactly the reflection of A across the perpendicular bisector of MN
   (equivalently: Q is the point with QM = AN, QN = AM, and AQ ∥ MN ∥ BC).
   Since O is the center of a circle through the two fixed points A and Q, O
   automatically lies on the perpendicular bisector of AQ — and by the very
   definition of Q that perpendicular bisector *is* the perpendicular bisector
   of MN. So **the whole problem reduces to: prove A, K, L, Q are concyclic**,
   where Q is a *point defined purely from A, B, C* (not from K, L) — this
   converts an equal-length goal into a pure angle/concyclicity goal, ideal for
   directed-angle chasing: show ∠(QA,QK) = ∠(LA,LK) (or equivalent) using the
   three hypothesis angle equalities and the inside-angle containment
   conditions. This is the strongest, most concrete opening found.

2. **Power-of-a-point reformulation.** OM=ON ⟺ pow(M; circle AKL) = pow(N;
   circle AKL) (since OM²−R² and ON²−R² are the powers, R cancels). Numerically
   confirmed to 10 significant figures. This is an equivalent target to (1) but
   phrased without introducing Q explicitly — could be attacked by finding an
   explicit secant of circle(AKL) through M (using the ∠BMK hypothesis, which
   ties M's position to K directly) and a matching secant through N (using the
   ∠LNC hypothesis), then comparing the two power products directly. The
   hypothesis ∠LBK = ∠LNC and ∠LCK = ∠BMK are exactly the two conditions that
   "anchor" M and N respectively to the K,L configuration — they look designed
   to be the two power-of-a-point / spiral-similarity engines, one for each of
   M, N.

3. **Spiral similarity / isogonality reading of the three conditions.**
   ∠KBA = ∠ACL looks like the "same angle from B and from C" signature that
   normally comes with a spiral similarity taking segment (or ray) at B to a
   segment/ray at C — worth checking (see cheap-kill probes below) whether
   there is a spiral similarity centered at a fixed point (candidates: the
   midpoint of BC, the circumcenter of ABC, or A itself) carrying B ↦ C and
   K ↦ L, or more precisely carrying ray BK ↦ ray CL. The other two conditions,
   ∠LBK = ∠LNC and ∠LCK = ∠BMK, each equate an angle at B or C (between the two
   unknown points K,L) to an angle at N or M (between a midpoint, one unknown
   point, and the opposite fixed vertex) — this smells like a *spiral similarity
   at K* sending B ↦ N, L-ray ↦ C-ray or similar (K plays the role of the
   spiral-similarity center relating triangle "K,B,L" to triangle
   "K,N,C"-ish), and symmetric for L. This needs to be checked carefully;
   flagged as promising but unverified — a genuine spiral-similarity-center
   argument (rather than raw angle chase) could shortcut the concyclicity in
   opening (1). Not chased further (out of scope for exploration).

4. **Direct perpendicular-bisector-of-MN target without Q.** Instead of naming
   Q, one could aim directly to show O lies on the perpendicular bisector of MN
   using vector/trig identities (e.g. express O via the circumcenter formula in
   terms of A,K,L and expand OM²−ON² algebraically, using the three angle
   conditions as trig constraints on K,L). This is the "brute force" fallback
   if the synthetic concyclicity in (1) proves hard to pin down; more
   computational, less illuminating, higher risk of an unmanageable expression
   swamp for an 8-rated IMO problem, but is a safety net.

### Candidate technique(s)
Directed-angle chasing (to establish A,K,L,Q concyclic, or equivalently the
spiral-similarity structure linking K and L to B,C,M,N); power-of-a-point /
radical-axis argument as the bridge from concyclicity to OM=ON; possibly one
or two spiral similarities centered at K and at L (reading conditions 2 and 3
of the hypothesis as spiral-similarity signatures) to *construct* the fixed
point Q synthetically.

### Cheap-kill candidates
- Check whether Q (reflection of A over the perpendicular bisector of MN) has
  a simpler description, e.g. as the reflection of A over line BC, the
  circumcircle-ABC antipode of A, or the reflection of the orthocenter — all
  checked numerically and **ruled out** (none matched Q in the test triangle).
  Q does NOT lie on the circumcircle of ABC (checked to 6 sig figs: distances
  1.971237 vs 1.971355 — close only because the test triangle was near
  isosceles, not exact). So Q is likely *not* a classical named center; it must
  be established directly as "the point with QM=AN, QN=AM, AQ∥MN" and then
  matched to a synthetic description built from K, L via the hypothesis angles
  — this synthetic identification of Q *purely from the configuration*
  (independent of the K,L family) is the crux gap to close.
- A weaker, purely structural pruning: since the three hypothesis equations (3
  scalar equations) are imposed on only 4 real unknowns (coordinates of K, L),
  the valid (K,L) pairs numerically form a **1-parameter family**, not a single
  point — confirmed by direct computation (see below). Any approach that
  implicitly assumes K, L are uniquely determined by the stated conditions
  alone is wrong / must additionally use the containment conditions ("K inside
  ∠LBA", "L inside ∠ACK", K inside △BMC, L inside △BNC) only to select a
  *connected branch* of that family, not to pin a single point. The outliner
  should not chase a "unique construction" line of attack — OM=ON must be
  proved to hold identically along the whole family (that's what makes O trace
  a whole open arc of the perpendicular bisector of MN, not a single point).

### Knowledge-base entries to use
- "Synthetic toolkit" entry (angle chasing, power of a point + concyclicity
  converse `PA·PB=PC·PD`, spiral similarity, inversion) — `knowledge_base.md`,
  Geometry section. This is the only geometry-specific entry in the KB; it is
  generic (names the tools) but does not give a worked geometry lemma to
  import directly. No other KB entry (nine-point circle, isogonal conjugates,
  nine-point/nine-point-circle-lemma etc.) currently exists as a named
  reusable fact in `knowledge_base.md` — if the outliner needs one (e.g. a
  spiral-similarity-center lemma or a "concyclic via equal power" lemma) it
  will have to be stated and proved from scratch, then optionally added to the
  KB.

### Analogous past problems (cruxes)
`crux_moves_documentation.md` states plainly: **the crux corpus has no
geometry cruxes yet** ("Not in the corpus yet; the problems DB includes
geometry problems with solutions, but no geometry cruxes have been
extracted."). So there is nothing to retrieve by domain=geometry from
`past_crux_moves_database.json`. I did not force a mismatch from another
domain — none genuinely analogous.

### Prior progress
None — this is round 1, `results/imo-2026-02/current.md` is `unsolved` with no
approaches yet.

### Dead ends (do not retry)
None recorded yet (no prior approaches exist). From my own probing: attempts to
identify Q as a classical triangle center (circumcircle-ABC point, reflection
of A over BC, reflection of orthocenter, nine-point center reflection, `B+C-A`,
etc.) all **failed to match** numerically — don't waste round-1 outline effort
searching a "named center" lookup table for Q; it must be built from the
hypothesis synthetically.

### Small-case / intuition notes (numerical, conjectural)
Used a scalene test triangle A=(0.3,2.7), B=(−1.5,0), C=(2.2,0.1),
M=(A+B)/2, N=(A+C)/2. Solved the 3-equation/4-unknown system for (K,L) with a
1-parameter gauge (varying K's x-coordinate) via `scipy.optimize.fsolve`,
filtering to solutions with K inside △BMC and L inside △BNC (containment
holds for a wide sub-range of the parameter, e.g. Kx ∈ [−0.95, −0.63] in this
example — outside that range fsolve fails to converge or containment breaks).
Findings (all *numerical evidence*, not proofs):
- **OM = ON holds to ~15 significant digits at every sampled point of the
  family** — strong confirmation of the target claim itself.
- **O is not a fixed point** — it moves (its y-coordinate ranges roughly from
  1.13 to 1.58 across the sampled family while x stays near 0.32–0.33) but
  stays on a fixed line = the perpendicular bisector of MN.
- **All circumcircles of AKL (across the family) pass through one common
  second point Q** besides A — verified via pairwise radical-axis
  intersections across widely separated family members (different circle
  radii 1.12–1.57), matching to 8 decimal places. Q = reflection of A across
  the perpendicular bisector of MN (verified this is exactly consistent with,
  but not a coincidence — it's forced once the fixed-second-point fact is
  granted).
- `pow(M; ⊙AKL) = pow(N; ⊙AKL)` exactly (checked to 10 sig figs), the
  power-of-a-point restatement of OM=ON.
- The similarity ratios AB/AC, BK/CL, AK/AL are close but not exactly equal in
  the (near-isosceles-ish) test triangle — inconclusive on whether ABK ~ ACL
  is an exact similarity; would need a more scalene test triangle to check
  cleanly (not done, time-boxed).

Numeric probe scripts used (for reference/reproducibility, not part of the
proof): `/tmp/probe5.py`, `/tmp/probe6.py`, `/tmp/probe8.py`.
