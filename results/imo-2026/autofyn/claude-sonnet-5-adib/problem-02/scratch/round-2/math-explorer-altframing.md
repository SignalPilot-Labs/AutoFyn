## imo-2026-02

### Headline finding: a genuinely different, fully-proved reduction that bypasses Apollonius/power-of-B,C entirely

Both live approaches (labeling-duality, coordinate-trig-bash) reduce OM=ON to
a scalar identity built from the powers of **B and C** w.r.t. Γ=circumcircle(AKL)
(the boxed (TI): pow_Γ(B)−pow_Γ(C) = (AB²−AC²)/2, via the Apollonius
median-length theorem). I found a cleaner, equally rigorous, but *structurally
different* reduction that never introduces B, C, AB, AC at all, and instead
produces a single new synthetic point worth handing to the outliner as its own
top-level target.

**Construction.** Let A* = 2O − A, i.e. the point diametrically opposite A on
Γ = circumcircle(AKL) (its "antipode"; O is the midpoint of segment AA*, so
this is well-defined for any O and needs no extra hypothesis).

**Claim (proved, one line of vector algebra, no Apollonius needed).**
Since M = (A+B)/2:
  A* − B = (2O−A) − B = 2·(O − (A+B)/2) = 2(O − M).
So A*B = 2·OM. Identically, A* − C = 2(O−N), so A*C = 2·ON. Hence

  **OM = ON ⟺ A*B = A*C ⟺ A* lies on the perpendicular bisector of BC.**

This is a complete, gap-free equivalence (pure affine/vector identity — even
more elementary than the Apollonius route the other approaches use, since it
needs no dot-product/parallelogram-law step at all, just M=(A+B)/2 and
N=(A+C)/2 substituted directly). I verified it numerically to machine
precision on two independent scalene triangles across the valid branch of the
family (see Small-case notes) — it reproduces OM=ON exactly and gives a
completely different-looking equivalent target: **A*B = A*C**, i.e. **A*
lies on the perpendicular bisector of BC** — instead of a power-of-a-point
scalar identity involving AB², AC².

**Why this is a different route, not just a repackaging of (TI):** since Γ
has center O and A,A* are antipodal on it, ∠AKA* = ∠ALA* = 90° (Thales) for
FREE — i.e. A* is characterized purely synthetically, without reference to
circle power at all, as:

  **A* = the intersection of (the line through K perpendicular to AK) and
  (the line through L perpendicular to AL).**

So the whole problem becomes: *show that the point constructed by erecting
perpendiculars to AK at K and to AL at L meets on the perpendicular bisector
of BC.* This opens attack routes that never touch pow_Γ(B), pow_Γ(C), or
AB²−AC² — e.g. law of cosines in triangles A*KB and A*LC using
∠A*KB = 90°±∠AKB, ∠A*LC = 90°±∠ALC together with the given angle hypotheses
on ∠KBA, ∠LCK etc., or a direct rotation argument (is there a spiral
similarity/rotation taking A*→ itself while swapping (K,B)↔(L,C) structure?
untested, flagged as the natural next probe).

### Refuted sub-conjecture (do not re-try)
I tested whether MK is tangent to Γ at K (which would give pow_Γ(M)=MK²
directly, an even shorter route to the same target via the also-true but
unused simplification pow_Γ(M)=pow_Γ(N) ⟺ OM=ON). Numerically FALSE: on two
triangles, at the valid branch (e.g. triangle A=(0.3,1.7),B=(-1,0),C=(1,0),
t=0.35: OK·MK ≈ 0.279, t=0.45: OK·MK ≈ 0.372 — nowhere near 0, and drifting
smoothly with t, not an artifact). So MK is NOT tangent to Γ at K in general;
do not re-attempt this specific mechanism. (The weaker, still-true fact
pow_Γ(M)=pow_Γ(N) ⟺ OM=ON, with no tangency, is subsumed by the A* framing
above and doesn't need restating separately.)

### Distinct openings
1. **A*-antipode / perpendicular-bisector target** (new, this report, fully
   proved reduction): OM=ON ⟺ A* (antipode of A on Γ, = intersection of
   perpendicular to AK at K and perpendicular to AL at L) lies on perp
   bisector of BC. Recommend as a new top-level approach, distinct in kind
   from the (TI) power-of-B,C identity both live approaches share.
2. Attack A*B=A*C via law of cosines in triangles A*KB, A*LC, converting
   ∠A*KB, ∠A*LC into 90°±∠AKB, 90°±∠ALC and chasing these against the three
   given angle hypotheses (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) plus extended
   law of sines in Γ (AK=2R sin∠ALK, etc.) — this is the natural next
   computational step but UNTRIED; flagged as the concrete gap for a builder.
3. Nine-point circle framing (already in the field as `nine-point-link`):
   worth explicitly noting the A*-construction gives that approach a concrete
   new lever — since M, N are already known to lie on the nine-point circle,
   and A* must lie on perp-bisector(MN)-adjacent line perp-bisector(BC)
   (NOT the same line as perp-bisector(MN) in general — check before
   conflating), the outliner could investigate whether A* relates to the
   nine-point center via a homothety-of-ratio-2 argument analogous to the one
   used here (O↔A* is itself a homothety of ratio −1 centered at... no, it's
   a point-reflection through O — a cheap structural fact worth having on
   hand).
4. Spiral-similarity/rotation fixing A*: untested — does the rigid map taking
   B→K, C→L (if such exists per the angle hypotheses) fix A* or relate it
   simply to O? Not explored due to time; flagged as open.

### Candidate technique(s)
Thales/antipode + perpendicularity, law of cosines in the two "attached"
triangles A*KB / A*LC, extended law of sines in circle Γ to convert AK, AL,
KL lengths into inscribed-angle sines. Classical synthetic toolkit
(knowledge_base.md "Synthetic toolkit": power of a point, inscribed angle /
Thales, is the closest named entry — Thales/right-angle-in-semicircle isn't
separately named in knowledge_base.md but is standard and should be cited by
name in any proof using it).

### Cheap-kill candidates
None found for ruling out the whole problem; the one concrete cheap test I
ran (MK tangent to Γ at K) was a kill of a specific sub-mechanism, not the
problem itself — reported above as a dead end to avoid re-testing.

### Knowledge-base entries to use
- "Synthetic toolkit" (power of a point, spiral similarity, inversion) —
  knowledge_base.md line ~129.
- "Coordinates / complex / barycentric" — line ~137, if the builder wants to
  cross-check A*B=A*C algebraically as a fallback to the synthetic route.
- No entry currently names Thales'/antipode-perpendicularity explicitly;
  cite it as a standard fact (angle inscribed in a semicircle is a right
  angle) when writing the proof.

### Analogous past problems (cruxes)
The crux corpus (`past_crux_moves_database.json`) only covers domains
`number_theory`, `combinatorics`, `algebra` (see crux_moves_documentation.md
subtopics list) — there is no `geometry` domain in this corpus, so no
genuinely analogous crux exists to retrieve for this synthetic-geometry
problem. Report: **none** (do not force a match from an unrelated domain).

### Prior progress
Both live approaches (labeling-duality, coordinate-trig-bash) are fully
correct up to their shared gap (proving (TI) / O_x=p/2 from the angle
hypotheses) — see current.md for the exact state; not re-litigated here.
`two-step-spiral-chain` is a confirmed dead end (two specific rigid-map
mechanisms refuted numerically, robustly, on two triangles) — do not retry
those two specific claims (spiral similarity BKL~NLC; C,K,M,X concyclicity
for any natural X). `nine-point-link` and `complex-circle-power` are
unbuilt outlines from round 1, not yet tested.

### Dead ends (do not retry)
- MK tangent to Γ at K (this report; refuted numerically, see above).
- Spiral similarity △BKL ~ △NLC (two-step-spiral-chain; refuted, ratio
  BK/BL ≠ NL/NC and even changes sign across the family).
- Concyclicity of C,K,M with any natural 4th point among {A,B,C,M,N,K,L}
  (two-step-spiral-chain; exhaustively tested, all 20 relevant 4-subsets
  refuted).

### Small-case / intuition notes
Verified numerically (Python, `fsolve` on the 4 hypothesis equations, filtered
to the containment/orientation branch) on two independent scalene triangles:
- Triangle 1: A=(0.3,1.7), B=(−1,0), C=(1,0). At t=0.35, 0.45 (valid branch):
  OM=ON to 1e-6+ precision, and A*B=A*C confirmed simultaneously (exact same
  precision, as expected from the proved algebraic identity).
- Triangle 2: A=(−0.5,2.1), B=(−1.3,0), C=(0.9,0). At t=0.25,0.32,0.40,0.50:
  OM=ON and A*B=A*C agree to 1e-6+, and the defining right-angle conditions
  (AK)·(A*K)=0, (AL)·(A*L)=0 hold to 1e-15 (as they must, by construction —
  sanity check on the numeric rig, not new evidence).
This is strong numerical confirmation that the A*-reduction is correct
(expected, since it's an exact algebraic identity, not a conjecture) and that
the reformulated target A*B=A*C is exactly as hard/easy as OM=ON — i.e. no
information is lost or gained by the reduction itself; the value is purely in
offering the outliner a structurally different, perpendicularity-flavored
target to attack instead of a power-of-a-point scalar identity, diversifying
the field away from the shared (TI) gap.
