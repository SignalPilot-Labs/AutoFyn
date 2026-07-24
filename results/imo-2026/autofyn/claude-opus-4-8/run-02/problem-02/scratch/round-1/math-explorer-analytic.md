## imo-2026-02

### Setup / lens
Analytic-computational lens: built a numeric model of the whole configuration (coordinates + scipy fsolve) and swept it across two scalene triangles to find hidden structure before any synthetic proof attempt. Script saved at `/tmp/round-1/imo2026_02_probe.py` (plus a follow-up diagnostic `/tmp/round-1/imo2026_02_probe2.py`, which `exec`s the first).

### Degrees of freedom (important structural fact)
The three angle conditions
`∠KBA = ∠ACL`, `∠LBK = ∠LNC`, `∠LCK = ∠BMK`
are **3 scalar equations in the 4 unknowns** (K=(x,y), L=(x,y)). So generically the configuration space of valid (K,L) pairs satisfying the hypotheses is a **1-parameter family**, not a single discrete point, for a fixed triangle ABC. I parametrized it explicitly:
- Let `φ = ∠KBA = ∠ACL` (the shared value forced by the first condition).
- K lies on the ray from B making angle `φ` with BA, rotated toward BC (this is exactly "K inside angle ABC" / inside triangle BMC, since M is on ray BA so ∠MBC = ∠ABC).
- L lies on the ray from C making angle `φ` with CA, rotated toward CB (symmetric reason via N on ray CA).
- The two remaining equations `∠LBK=∠LNC` and `∠LCK=∠BMK` then pin down the two radii `r_K = BK`, `r_L = CL` **for each choice of φ** (solved numerically with `fsolve`; converges to essentially a unique positive solution per φ in the tested range).

So the true "moduli" of the problem is a **1-real-parameter family** of valid (K,L), traced by φ. This matches the phrasing "let K, L be chosen ... such that ..." — the hypotheses do NOT pin down K, L uniquely, and the intended proof must work for the *whole family* (or show the conclusion is insensitive to the extra freedom). This is a key fact the outliner should build on: whatever synthetic argument is used, it cannot secretly assume K, L are the unique solution of some clean construction — there is a continuum, and OM=ON must be argued to hold at every point of it.

### Numeric findings (2 independent triangles, ~12-15 φ-samples each)
Triangle 1: A=(0,3), B=(-1.5,0), C=(2.2,0) (angle B≈1.107 rad, angle C≈0.938 rad).
Triangle 2: A=(0.3,2.1), B=(-2,0), C=(1,0) (angle B≈0.740 rad, angle C≈1.249 rad).

For every φ in the valid range (0, min(angle B, angle C)) that gave a convergent, positive (r_K,r_L):
- **OM = ON to ~1e-9** (float-solver precision) at *every* sampled φ, in both triangles — strong numeric confirmation of the target claim across the whole family, not just at one point.
- **Stronger fact (equivalent restatement, but geometrically sharper):** O lies **exactly on the perpendicular bisector line of segment MN** for every φ — I verified `(O − midpoint(MN)) · direction(MN) = 0` to ~1e-10 for all samples. This reframes the goal as: *the locus of O, as (K,L) range over the whole valid family, is contained in the perpendicular bisector of MN* (a full line, not just a single equidistance check at one point) — potentially a cleaner target for a synthetic/algebraic argument (e.g. show OM²−ON² ≡ 0 identically as a function of the free parameter, rather than solving for O explicitly).
- **AK ≠ AL** in general (e.g. Triangle 1, φ=0.409: AK=2.60, AL=2.73) — ruling out "AKL is isosceles from A" as an invariant.
- **∠BAK ≠ ∠CAL** in general (e.g. φ=0.431: ∠BAK=0.128, ∠CAL=0.166) — ruling out a direct spiral-similarity-at-A sending K↔L via equal base angles.
- **B, C are NOT on the circumcircle of AKL** (OB, OC computed and both ≠ R=OA, by a wide margin) — ruling out "AKLB" or "AKLC" concyclic as a shortcut, and ruling out power-of-a-point tricks that rely on B or C lying on that circle.
- **AK/AB and AL/AC are not constant** across the family (they vary smoothly with φ) — no fixed similarity ratio.

### Assessment: is a full complex-number / coordinate proof tractable?
- A **brute-force coordinate/complex bash** (solve the 3 trig equations symbolically for K, L in terms of A,B,C and φ, then compute O and show OM²=ON² algebraically) is likely to be extremely messy: the angle-equality conditions involve arctangents of ratios of quadratic forms in the coordinates, and eliminating φ analytically (given it's a genuine free parameter, not fixed by the hypotheses) means the identity OM²=ON² must hold as a **polynomial/rational identity valid for a continuum of φ**, i.e. it is likely provable by showing OM²−ON² is (after clearing denominators) a rational function of φ that is identically the zero function — this is checkable in principle via a symbolic computation (sympy, treating φ as a symbol and A,B,C as symbolic coordinates, expressing K,L via the rotated-ray parametrization I used numerically), but the algebra will be heavy (trig in φ mixed with two coordinate vertices). This is a plausible but expensive fallback route, not the likely intended solution.
- Given the family structure, a **much more tractable analytic/synthetic hybrid** is suggested by the numerics: since the claim is that O stays on a *fixed line* (perp bisector of MN) as φ varies continuously, a "moving points" argument is natural: (a) identify the two conditions ∠LBK=∠LNC and ∠LCK=∠BMK as saying certain quadrilaterals/triangles are similar or that certain points are concyclic (angle equality at a vertex between two cevians is the classic signal for spiral similarity or for "isogonal conjugate" configurations — worth checking whether BK/BL are isogonal in angle B with respect to some triangle, or whether the equal angles force K, L, and one of M/N onto a common circle); (b) then show OM²−ON² is expressible as a difference of two **power-of-a-point** quantities relative to the circle (AKL), each computable via the fixed angle conditions, independent of which member of the family is chosen. This is the shape a synthetic solution would likely take, but I have NOT verified any specific circle/concyclicity claim yet — that is for the outliner/builder to construct and check.
- **Cheap sanity check available**: because OM=ON holds along an entire continuum (confirmed numerically), any proposed synthetic lemma should be checked for whether it uses any information that pins K,L to a single point — if it does, it is over-specifying the hypothesis and is suspect.

### Candidate technique(s)
- Spiral similarity / equal-angle configurations (angle chasing) is favored by the "∠X = ∠Y" hypothesis shape (classic pattern for constructing similar triangles or concyclic quadruples), per knowledge_base's **Synthetic toolkit** and **Circle/triangle configuration facts** entries.
- Coordinates/complex numbers (KB entry **"Coordinates / complex / barycentric"**) as a verification/fallback route, using A as origin and the explicit rotated-ray parametrization discovered here to keep the algebra as clean as possible (reduces 4 unknowns to 1 free parameter φ plus 2 solved radii).
- Given the fixed perpendicular-bisector-of-MN target, the midline MN (parallel to BC, half its length) and the nine-point-circle-adjacent structure (M, N are midpoints) suggests possibly relating O to the nine-point circle or medial triangle — not yet checked, but worth a synthetic explorer's attention.

### Cheap-kill candidates
None found that shortcut the whole proof — the containment/orientation hypotheses (K inside ∠LBA, L inside ∠ACK, inside the respective sub-triangles) look necessary only to pick the right branch/orientation of the angle equalities (to avoid arccos sign ambiguity), not to reduce dimension. No parity/pigeonhole/injection angle applies (this is a continuous geometry equality, not combinatorial). The one useful structural pruning: **use the 1-dof family to falsify any candidate synthetic claim that would only hold at an isolated configuration** (e.g. AK=AL, ∠BAK=∠CAL, B or C on circle(AKL) — all checked and false in general, see above).

### Knowledge-base entries to use
- **Synthetic toolkit** (angle chasing, spiral similarity, power of a point / concyclicity converse).
- **Circle/triangle configuration facts** (Miquel point, Simson line — worth checking if M, N, K, L or similar quadruple relates to a Miquel-point configuration given the twin-triangle (BMC/BNC) setup).
- **Coordinates / complex / barycentric** entry, for a symbolic fallback verification.

### Analogous past problems (cruxes)
`crux_moves_documentation.md` states explicitly: **"geometry — Not in the corpus yet; the problems DB includes geometry problems with solutions, but no geometry cruxes have been extracted."** So the crux corpus has **no geometry entries at all** — nothing to retrieve for this lens. (The past_problems_database may still contain geometry problem statements+solutions without extracted cruxes, but per the instructions the crux corpus is what's queryable for analogy; I did not force a false match from other domains.)

### Prior progress
None — `results/imo-2026-02/current.md` and `approaches/` do not exist yet (this is the first exploration of this problem in this run).

### Dead ends (do not retry)
- None recorded yet from prior rounds (none exist). From my own numeric probing, flag as **not fruitful directions**: (1) assuming AK=AL, (2) assuming ∠BAK=∠CAL (no spiral similarity centered at A with equal base angles), (3) assuming B or C lies on circumcircle(AKL) — all numerically false, would misdirect a synthetic proof attempt.

### Small-case / intuition notes (all conjectural, numerically supported only)
- Conjecture (strongly supported, ~1e-9 agreement across 2 triangles × ~25 total samples): **O always lies on the perpendicular bisector of MN**, not just equidistant at isolated configurations — i.e. the claim OM=ON is really "the whole 1-parameter locus of O sits on one fixed line," which is a stronger and possibly more tractable target than proving a single numeric equality.
- Conjecture: the hypotheses define a genuine 1-parameter family of (K, L) for fixed ABC (not a unique pair) — confirmed by successfully sweeping φ = ∠KBA = ∠ACL over a sub-interval of (0, min(∠B,∠C)) and getting a smoothly-varying valid solution at each sample via fsolve.
- Conjecture: AK/AB, AL/AC, ∠BAK, ∠CAL all vary continuously (not constant) along the family — the invariant is specifically OM (=ON), not any simpler per-triangle metric quantity.
