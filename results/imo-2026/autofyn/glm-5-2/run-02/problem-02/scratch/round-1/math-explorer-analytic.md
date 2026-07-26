## imo-2026-02  (IMO 2026 P2 — geometry; lens: analytic / coordinate / complex)

Problem (recap): Triangle ABC, M midpoint of AB, N midpoint of AC. K inside △BMC, L inside △BNC, with K inside ∠LBA, L inside ∠ACK, and
∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. O = circumcentre of △AKL. Prove OM = ON.
`task=proof_only`, `answer_type=none`. Round 1, fresh workspace (no approaches, no lemmas).

### Distinct openings surfaced ( all on the analytic route )

1. **Coordinate bash with the perpendicular-bisector reformulation.** Place A at the origin. Then M = B/2, N = C/2, and a one-line computation gives
   `OM² − ON² = O·(C − B) + (|B|² − |C|²)/4`. So **OM = ON  ⟺  O·(C − B) = (|C|² − |B|²)/4**,
   i.e. O lies on the fixed line ℓ through (B+C)/4 perpendicular to MN. This line ℓ is exactly the perpendicular bisector of MN. The target is *linear* in O (degree 1 in the circumcentre), not quadratic — a substantial simplification. (Verified numerically: `O·(C−B)` equals `( |C|²−|B|² )/4` to ~1e-14 on every solution found, three triangles.)

2. **Eliminate K via the linearity-in-K of two of the angle equations.** Encode each angle equality as `cross2(u,v)·dot(p,q) − cross2(p,q)·dot(u,v) = 0` (directed-angle / tangent equality, polynomial). With A=0, B=(4,0), C=(1,3) (representative similarity class — the structure is similarity-invariant so this WLOG is legitimate), the three generators are:
   - `e1` (from ∠KBA = ∠ACL): **degree 2**, and *linear in K* given L (bilinear K–L).
   - `e2` (from ∠LBK = ∠LNC): **degree 3**, and *linear in K* given L (the only K–L products are bilinear; no K² terms).
   - `e3` (from ∠LCK = ∠BMK): **degree 3**, *quadratic in K* given L — but only through `kx² + ky²` (a single radial term times `−2·ly`), so it is linear in `K² := kx²+ky²`.
   Crucially, **e1 and e2 are both homogeneous linear in (K − B)** (K = B is always a solution). Their 2×2 coefficient determinant `det(lx,ly)` is a **cubic in L**; on the curve `det(lx,ly)=0` the two equations collapse to one linear constraint, giving K = B + t·d(L) (a line through B parametrized by L). Then e3 (quadratic in t, linear in K²) selects discrete t for each L on the cubic. This reduces the 4-variable ideal to a **cubic L-curve + a line-through-B parametrisation of K** — the natural analytic spine.

3. **Complex-number route.** Put A = 0 in the complex plane (no circle assumed; B,C free complex). The angle condition `∠(u,v)=∠(p,q)` becomes `arg(u/v) = arg(p/q)`, i.e. `(u/v)/(p/q) ∈ ℝ₊`, i.e. `u·q·conj(v·p) = conj(u·q·conj(v·p))` — same polynomial as the cross/dot form. The circumcentre of (0,K,L) satisfies `O·K̄ + Ō·K = |K|²`, `O·L̄ + Ō·L = |L|²`, solvable as `O = (|K|²·L − |L|²·K)/(K·L̄ − K̄·L)·(?)` — purely rational in K,L. The reformulated target `O·(C−B) = (|C|²−|B|²)/4` becomes a complex rational identity. No advantage over the real-coordinate route was found here — the algebra is identical in substance (complex just packages cross/dot). Report this so the outliner does not waste a slug on a separate complex bash expecting a different wall.

4. **Vector / barycentric hybrid.** M, N as barycentric (1/2:1/2:0) and (1/2:0:1/2) on triangle ABC. The line ℓ (perp-bisector of MN) has a clean barycentric equation. K and L live in fixed sub-triangles, so their barycentric coordinates are sign-constrained. This is the route to *combine* with opening 2 — barycentric gives a clean language for the "inside" inequalities that the pure coordinate ideal misses (see obstacle below).

### Candidate technique(s)
- Coordinate / vector algebra with A at origin, B,C free (similarity WLOG: fix B on x-axis, C=(u,v) with 2 free params).
- Polynomial ideal reduction: solve e1,e2 (linear in K) for K as a function of L on the cubic `det(L)=0`; substitute into e3; verify the target P is a multiple of the resulting curve polynomial. This is a **2-variable divisibility / gcd check**, far lighter than a 4-var Gröbner.
- (Backup) Real-algebraic / Positivstellensatz if a pure ideal-membership certificate is wanted with the inside-inequalities included — but this is the heavy option (see obstacle 2).

### Cheap-kill candidates
- **Reformulation as "O on the perpendicular bisector of MN".** This is the single most useful structural reduction: it converts the problem from "two distances equal" to "O lies on a known fixed line". The perpendicular bisector of MN is the line through (B+C)/4 ⟂ (C−B)/2; equivalently `{X : X·(C−B) = (|C|²−|B|²)/4}` (A=0). Any approach, synthetic or analytic, should target this line. (Verified: numerics match to 1e-14.)
- **1-parameter-family observation** (below) — once K,L are seen to be a 1-param family with the identity holding identically along it, a synthetic geometer would look for an *invariant*: a map whose level sets are exactly the line ℓ.

### Knowledge-base entries to use
- KB `Geometry (synthetic & analytic)`: **Coordinates / complex / barycentric** ("place coordinates to exploit symmetry; rotate axes to align with a key line"). The line ℓ here is the key line.
- KB `Geometry`: **Synthetic toolkit** — circumcentre, perpendicular bisectors, angle chasing — for the eventual selection of the correct branch (the analytic ideal cannot do it alone, see obstacle 2).
- KB `Linear Algebra`: **Gröbner-basis ideal membership / Rabinowitsch trick** — relevant if a CAS certificate on the reduced 2-var curve is wanted (and for verifying the cubic L-curve identity in a fixed triangle).
- KB `Algebra & Polynomials`: **Resultants / "transform the roots"** — alternative to Gröbner for the 2-var divisibility check after eliminating K.

### Analogous past problems (cruxes)
- (Not yet searched — round 1, crux corpus query not run this lens. The crux corpus is geometry-heavy; recommend the outliner query subtopic `circumcenter` / `angle_chasing` / `midpoint` before building. The configuration (midpoints, circumcentre, chained angle equalities, perpendicular-bisector target) is unusual; do not force a match.)

### Prior progress
- None — round 1, fresh workspace.

### Dead ends (do not retry)
- **Pure ideal-membership of P in `<e1,e2,e3>` is DEAD for a direct proof.** With A=(0,0), B=(4,0), C=(1,3): the target polynomial `P := 3·[ −|K|²·ly + |L|²·ky + kx·|L|² − lx·|K|² + (kx·ly − ky·lx) ]` (degree 3, the cleared-denominator form of `O·(C−B) − (|C|²−|B|²)/4`, multiplied by `2·det(K,L)`) has a **nonzero remainder modulo the Gröbner basis of `<e1,e2,e3>`** (basis computed in 0.02 s, 9 polynomials, lex order). So P ∉ `<e1,e2,e3>`. Worse: I searched 5657 real solutions of the *directed-angle polynomial system* `<e1,e2,e3>` and **2094 of them have P ≠ 0** (e.g. K=(4,0)=B, L arbitrary on a spurious branch, gives P up to ±392). The tangent-equality encoding admits spurious real components (K=B trivial branch; L on wrong arcs; etc.). **The inside-region / inside-angle hypotheses are load-bearing**, not removable. Do NOT attempt "P ∈ ideal ⇒ done"; it is false.

### Small-case / intuition notes (labelled CONJECTURE / EVIDENCE)
- **EVIDENCE (strong, 3 triangles):** For A=(0,0), B=(4,0), C=(1,3); for B=(6,0), C=(2,5) (scalene); for B=(5,0), C=(2.5,4) (isoceles) — in each, scipy least_squares found ~140 real (K,L) satisfying all three angle equalities AND the four inside conditions; **OM − ON < 8e-15 on every one**. The statement is solid; the configuration is non-empty and 1-dimensional.
- **CONJECTURE (structural):** The solution set of (angle-equalities ∧ inside-conditions) is a **1-parameter family** (3 polynomial equations in 4 unknowns, generically a curve; numerics confirm ~140 distinct points along a smooth arc). The theorem `OM=ON` holds **identically along the whole family**, not just at an isolated point. This means the proof is an *identity-on-a-curve* statement — strong evidence that a clean invariant / hidden-symmetry proof exists, and a warning that "solve for K,L then check" is the wrong frame (there is nothing to solve to a point).
- **CONJECTURE (analytic spine):** The cubic `det(lx,ly)=0` (determinant of the e1,e2 linear system in K−B) is the L-curve. On it, e1 gives K = B + t·d(L); e3 becomes a univariate quadratic in t (with L on the cubic). The target P, after substituting K=B+t·d(L) and L-cubic, should factor as (curve polynomial)·(something) + (e3-remainder)·0 — i.e. vanish on the good branch. This 2-variable divisibility is the most tractable analytic certificate and should be tested first (CAS for a fixed triangle; then attempt with similarity-normalised parameters u,v).
- **Worked example (T1), fully verified:**
  - A=(0,0), B=(4,0), C=(1,3) → M=(2,0), N=(0.5,1.5).
  - K=(3.12700295, 0.56547641), L=(1.09481219, 2.63333187).
  - Barycentric: K in △BMC = (0.154, 0.188, 0.658) all > 0; L in △BNC = (0.136, 0.810, 0.054) all > 0. K inside ∠LBA and L inside ∠ACK: confirmed (signed-angle test).
  - Angle-equality residuals: 0 to machine precision.
  - Circumcentre O = (1.44393325, 0.94393325).
  - **OM = 1.0955456221374005, ON = 1.0955456221374067, diff = −6.2e-15.**
  - Reformulation check: O·(C−B) = −1.5000000000000142 = (|C|²−|B|²)/4 = −1.5. ✓

### Honest assessment of the analytic route
- **Feasible for verification, NOT as a standalone general proof.** The algebra is *not* a CAS-only mess in the small — Gröbner on the fixed triangle runs in 0.02 s, the polynomials are small (degrees 2,3,3,3), and the e1/e2-linearity-in-K reduction collapses the 4-var problem to a 2-var (L-cubic, t) identity. That part is human-tractable.
- **Where it breaks down:** the **branch problem**. The directed-angle polynomial ideal admits spurious real components (K=B trivial branch; wrong arcs of the angle-equality mod-π relation) on which P ≠ 0. The inside-region and inside-angle hypotheses are *exactly* what rules these out, and they are inequalities (signs of crosses/dots, barycentric positivity), not polynomial equalities. So a rigorous analytic proof must either
  (a) reduce to the L-cubic + t parametrisation and prove the 2-var identity on the *correct real branch* (requires identifying the right arc of the cubic — doable, since the inside-conditions pick a specific interval on the cubic), or
  (b) augment the ideal with Positivstellensatz / CAD constraints (heavy, likely intractable with free triangle parameters).
  Route (a) is the live analytic option; route (b) is a dead end for a general proof.
- **Free parameters:** after similarity normalisation (A=0, B on x-axis, C=(u,v)) the triangle has 2 free parameters; the L-cubic and the t-quadratic then have coefficients in ℚ(u,v). A full symbolic 2-var divisibility certificate in (u,v,lx,ly) is plausibly within CAS reach but has *not* been tested here — recommend the outliner test it before committing a slug to a fully-general analytic proof. For a single fixed triangle the certificate is immediate.
- **Recommendation to outliner:** the analytic route is strong as a *verification tool and as the source of the perpendicular-bisector reformulation* (opening 1), but a *standalone* analytic proof will fight the branch problem. The strongest rival approach uses the perpendicular-bisector reformulation (an analytic *fact*) as the target, then proves O ∈ ℓ synthetically (angle chase / spiral similarity / Miquel-type) — the analytic reduction tells you *what line to hit*, the synthetic angle chase *hits it*. Do not commit more than one slug to a pure-coordinate bash.
