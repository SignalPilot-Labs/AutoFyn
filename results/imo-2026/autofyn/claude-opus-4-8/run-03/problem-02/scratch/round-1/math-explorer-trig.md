## imo-2026-02

### Setup recap (trig/metric framing)
Degrees of freedom count: the three given equalities
`∠KBA = ∠ACL =: β`, `∠LBK = ∠LNC`, `∠LCK = ∠BMK`
are only **3 scalar equations** for the **4 scalar unknowns** (K has 2 coordinates, L
has 2). Given β, the first equation pins K to a known ray from B (making angle β
with BA, into the triangle) and pins L to a known ray from C (making angle β with
CA). That leaves 2 unknowns (distance of K along its ray, distance of L along its
ray) and the remaining 2 equations (`∠LBK=∠LNC`, `∠LCK=∠BMK`) generically fix K, L
for that β. So **β is a free parameter**: the valid configurations form a
1-parameter family, and the betweenness conditions ("K inside ∠LBA", "L inside
∠ACK", K inside △BMC, L inside △BNC) just cut down β to a sub-interval, not to a
point. **The problem is therefore a moving-point statement**: OM=ON must be proved
for every β in the admissible range, not just for one configuration.

### Numeric confirmation (conjecture, not proof)
Verified with `scipy.optimize.fsolve` on two triangles (one has A above the BC
midpoint, one fully scalene: A=(0.7,3.4), B=(-2.3,0), C=(3.1,-0.4)). For each β I
solved the two remaining equations for (t_K, t_L), built circle(AKL), and computed
O:
- OM = ON to machine precision (1e-14) for β = 15°..50° on the scalene triangle,
  and for β = 20°..50° on the first triangle. (At β=55° on the scalene triangle
  the numeric branch fsolve found violates the region constraints — K or L exits
  the required triangle/angle region — and OM≠ON there; this is *not* a
  counterexample, it's evidence the admissible β-interval is bounded and the
  claim is only asserted inside it.)
- **Stronger structural finding**: O's coordinates trace what looks like an exact
  straight line as β varies, and that line is the perpendicular bisector of MN
  itself (checked via `(O - midpoint(MN)) · (N-M) = 0`, holds to 1e-14 across the
  whole β sweep). So the natural target is not just "OM=ON" pointwise but "O
  moves along the fixed line = perp-bisector(MN)" — proving the identity
  `(O - midpoint(MN))·(N-M) ≡ 0` as a function of β (or equivalently of b,c,B,C
  and β) may be a cleaner algebraic target than reproving OM=ON case-by-case.

### Key reformation: power of a point (recommended top-level target)
`OM² - R² = pow(M, circle(AKL))`, `ON² - R² = pow(N, circle(AKL))` where R is the
circumradius of AKL. So **OM=ON ⟺ pow(M, ⊙AKL) = pow(N, ⊙AKL)**. This is the
natural way to avoid ever computing O's coordinates or R explicitly.

Numerically pinned down further: let line AB meet ⊙(AKL) again at X, and line AC
meet ⊙(AKL) again at Y (both A itself is one intersection since A ∈ ⊙AKL). Then
- `pow(M) = -MA·MX` (M lies between A and X on the chord — signs checked
  numerically: MA=2.267, MX=1.157, product 2.622 = |pow(M)|).
- `pow(N) = -NA·NY` (NA=2.247, NY=1.167, product 2.622 = |pow(N)|, matching
  |pow(M)| to 8 significant figures).
- Since **MA = MB** and **NA = NC** (M, N are midpoints — this is the one place
  the midpoint hypothesis enters!), the target power-equality becomes
  `MB·MX = NC·NY`, i.e. a **length-ratio identity `MX/NY = NC/MB = b/c`**
  (b=CA, c=AB) to be derived from the angle conditions defining K, L. This is a
  concrete, checkable trig target: express MX and NY via the law of sines/cosines
  in triangles built from B, C, β, and the derived positions of K, L, and show
  their ratio is exactly b/c. This sidesteps ever locating O or R explicitly.

This reformation should be handed to the outliner as **the** trig/metric approach:
"reduce OM=ON to pow(M,⊙AKL)=pow(N,⊙AKL), then to MA·MX=NA·NY via second
intersections of AB, AC with ⊙AKL, then to MX/NY = b/c using MA=MB, NA=NC."

### Candidate technique(s)
- Power of a point + radical-axis framing (perp bisector of MN is exactly the
  radical axis of ⊙(AKL) and the degenerate "point circle" ... more precisely:
  OM=ON iff M,N have equal power in ⊙AKL iff MN ⊥ (line OA-analog) — standard:
  the locus of points with equal power to a fixed circle is the perpendicular to
  the line through the center, i.e. exactly the requirement M,N symmetric about
  the diameter through O perpendicular to MN — but simplest is the pow(M)=pow(N)
  algebraic route above).
- Trig Ceva / directed-angle chase to pin down the rays BK, CL, BL, CK in terms
  of β and angles B, C (needed to get X, Y, MX, NY explicitly).
- Law of sines in triangles ABX, ACY (or BMK, CNL, LNC, BMK as literally named in
  the hypotheses) to get MX, NY as explicit trig expressions in β, B, C, b, c.
- Directed angles mod 180° recommended throughout since K, L are described purely
  by angle equalities and the configuration (which side of a ray) — protects
  against sign/orientation case splits.

### Cheap-kill candidates
- None found that finishes the problem, but a useful *sanity/reduction* short-cut:
  since MA=MB and NA=NC always (midpoint hypothesis, no proof needed — trivial),
  any approach that tries to prove pow(M)=pow(N) directly via circle-power should
  immediately substitute MA=MB, NA=NC to collapse the target to the single
  ratio identity MX/NY=b/c — cutting the amount of new trig computation roughly
  in half.
- Symmetry check: swapping (B↔C, M↔N, K↔L, β fixed) should exchange X↔Y and the
  target identity `MX/NY=b/c` becomes `NY/MX=c/b` — consistent (same identity
  inverted), a cheap self-consistency check the outliner/builder can use to catch
  sign errors early.

### Knowledge-base entries to use
- `knowledge_base.md` line ~129: "Synthetic toolkit: angle chasing, power of a
  point (and its concyclicity converse `PA·PB=PC·PD`), radical axes & radical
  center, similar triangles, trig cevians (Ceva/Menelaus), inversion, spiral
  similarity" — power of a point and trig Ceva are exactly the tools used above.
- line ~132: "Circle/triangle configuration facts: Ptolemy ... Simson line ...
  Miquel point of a complete quadrilateral" — Miquel-point / spiral-similarity
  machinery could be relevant if X, Y, K, L end up concyclic with B or C in some
  sub-configuration (untested — flag for outliner to check numerically if this
  route is picked).
- line ~137: "Coordinates / complex / barycentric: place coordinates to exploit
  symmetry" — a complex-number computation of O directly (bypassing power of a
  point) is the fallback if the pow(M)=pow(N) reduction stalls; but per CLAUDE.md
  this would be a genuinely different approach/slug (complex-coordinate route),
  not a variant of this one.

### Analogous past problems (cruxes)
The crux corpus (`crux_moves_documentation.md`) explicitly states: **"geometry —
Not in the corpus yet; the problems DB includes geometry problems with solutions,
but no geometry cruxes have been extracted."** So there is no geometry subtopic to
query. I did not force a match from other domains (number_theory/combinatorics/
algebra) since none would be genuinely analogous to a synthetic-geometry
circumcenter problem. **Conclusion: no crux corpus matches — report "none."**

### Prior progress
None — `results/imo-2026-02/current.md`, `approaches/`, `lemmas/` are all empty
at the start of round 1. No prior approaches exist yet to sanity-check.

### Dead ends (do not retry)
None recorded yet (first round). One thing to flag as a *pitfall*, not a dead
end: naively trying to prove OM=ON only "at one representative configuration"
(e.g. only checking a symmetric/isosceles case) is insufficient — the problem is
a 1-parameter family in β (see DOF count above) and a correct proof must handle
the whole admissible range, or must produce a β-free argument (e.g. the pow(M)
=pow(N) reduction above is attractive precisely because if MX/NY=b/c can be shown
to hold for the *general* β-dependent construction of X, Y, it never needs to
split into cases on β).

### Small-case / intuition notes (conjecture, labeled)
- Conjecture (strong numeric support, 2 triangles × ~8 β values each, agreement
  to 1e-14): O moves along the fixed line = perpendicular bisector of MN as β
  ranges over the admissible interval. This is strictly stronger than the
  problem's OM=ON statement and, if provable, immediately implies it.
- Conjecture (numeric, same runs): `pow(M,⊙AKL) = -MA·MX` and `pow(N,⊙AKL)
  = -NA·NY` where X,Y are second intersections of lines AB, AC with ⊙(AKL); hence
  OM=ON is equivalent to `MX/NY = CA/AB` (using MA=MB=AB/2, NA=NC=CA/2). This is
  the concrete trig identity a metric proof should target.
- The admissible β-interval is bounded by when K or L exits the required
  triangle/angle regions (K ∈ int(△BMC), L ∈ int(△BNC), K inside ∠LBA, L inside
  ∠ACK) — the outliner should expect to either (a) prove the identity for all β
  in an open interval algebraically (making the boundary irrelevant), or (b) need
  to characterize the interval's endpoints if a case-split proof is attempted.
  Route (a) is far preferable and is what the pow(M)=pow(N) algebraic identity
  naturally gives (an identity in β holds either everywhere or nowhere on a
  connected domain, so a single non-degenerate check + the trig identity being a
  literal algebraic identity in β suffices).
</content>
