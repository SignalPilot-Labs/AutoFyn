## imo-2026-02

### Setup recap
Triangle ABC, M,N midpoints of AB,AC. K inside triangle BMC, L inside triangle BNC, with
K inside ∠LBA, L inside ∠ACK, and
- (E1) ∠KBA = ∠ACL  (=: θ)
- (E2) ∠LBK = ∠LNC
- (E3) ∠LCK = ∠BMK
O = circumcenter of AKL. Prove OM = ON.

No prior approaches exist yet (workspace was empty at start of round 1: `results/imo-2026-02/approaches/` and `/lemmas/` both empty, no `current.md`). This is a fresh problem — nothing to avoid yet, nothing to build on yet.

### Distinct openings (all discovered/verified this round via the metric lens)

1. **Power-of-a-point reduction (the headline finding).** Since O is the circumcenter of
   AKL with radius R = OA, for any point X: OX² − R² = pow(X, ⊙(AKL)). Hence
   **OM² − ON² = pow(M,⊙AKL) − pow(N,⊙AKL)**, so
   `OM = ON  ⟺  pow(M, ⊙AKL) = pow(N, ⊙AKL)`.
   This converts the whole problem into a single power-of-a-point equality, dropping the
   circumcenter machinery entirely — the target is now purely about the circle ⊙(AKL)
   meeting lines AB and AC.

2. **Second-intersection formulation.** Line AB meets ⊙(AKL) again at a point A' (A is
   already on the circle); line AC meets it again at A''. Using signed lengths along each
   line with A at parameter 0, B at parameter 1 (so M is at parameter 1/2), and writing
   t = A'-parameter on AB, u = A''-parameter on AC:
   `pow(M) = AB² · (1/4 − t/2)`, `pow(N) = AC² · (1/4 − u/2)`.
   So the goal becomes an explicit relation between AB, AC and where ⊙(AKL) cuts back
   through lines AB, AC — i.e. a statement about A', A'' that must be proven from
   (E1)-(E3). This is the load-bearing lemma the outliner should target: **identify /
   characterize A' and A'' (or directly the ratio AB²(1−2t) = AC²(1−2u)) using the three
   angle conditions.** I checked numerically whether A' lies on lines BK, BL, CK, or CL
   (natural guesses from a spiral-similarity configuration) — none matched, so the
   characterization is not one of those simple incidences; it likely needs an actual
   trig computation (Law of Sines in the various sub-triangles cut out by K, L, M, N) or
   a spiral-similarity center distinct from A', A''.

3. **Perpendicular-bisector / fixed-line reformulation.** MN is the midline, parallel to
   BC, with midpoint(MN) = (A + midpoint(BC))/2. The perpendicular bisector of MN is
   therefore the fixed line through this point, perpendicular to BC. Numerically (see
   below) O does not just satisfy OM=ON at isolated points — as the free parameter of the
   configuration varies over the whole valid family, **O sweeps exactly along this fixed
   line** (its component along BC relative to midpoint(MN) is 0 to machine precision,
   while its component along the perpendicular varies substantially). This is a strictly
   equivalent restatement of OM=ON (not new information), but the fact that it holds
   *identically along a whole 1-parameter family*, not just at a single configuration, is
   strong structural confirmation and suggests the intended proof shows directly that O's
   projection onto BC (measured from midpoint(MN)) is a fixed value — e.g. via a vector
   identity `2·(O − A)·\hat{BC} = (something depending only on ABC)` that the angle
   conditions force to vanish after subtracting the fixed offset. Could point toward a
   vector/coordinate-bash proof: write O via the circumcenter formula in terms of A,K,L
   and push the three angle equalities through as trig relations.

4. **Trig-Ceva / spiral-similarity framing of (E1)-(E3).** (E1) ∠KBA=∠ACL looks like the
   signature of two triangles sharing a spiral-similarity relationship anchored at A
   (reminiscent of the classical spiral-similarity lemma in knowledge_base.md's synthetic
   toolkit): if two circles through A meet again at a second point T, T is the center of
   a spiral similarity carrying one chord to another with matching base angles. Since
   ∠KBA=∠ACL, circles (ABK)... and (ACL) might be the natural pair to consider (both pass
   through A), and their second intersection T could be a genuinely useful auxiliary
   point tying K and L together independent of M, N — worth the outliner testing whether
   T interacts nicely with (E2),(E3) (which mix in M, N directly through ∠LNC, ∠BMK — so
   T probably needs to also relate to the medial configuration, not just A,B,C,K,L).

### Candidate technique(s)
- Power of a point + directed lengths on cevian-like lines (knowledge_base.md "Synthetic
  toolkit": power of a point, its concyclicity converse, radical axes).
- Law of Sines / trig identities to compute the second-intersection parameters t, u
  explicitly in terms of the angles defined by (E1)-(E3) (knowledge_base.md "trig
  cevians (Ceva/Menelaus)").
- Spiral similarity (knowledge_base.md "Synthetic toolkit … spiral similarity") as a
  candidate for organizing the two equal-angle conditions (E1) and possibly (E2)/(E3).
- Coordinates/complex numbers as a fallback if the synthetic route stalls — the problem
  has a genuine free parameter (see below), so any coordinate proof must carry that
  parameter through symbolically and show OM−ON cancels identically, which is a decent
  sanity target for a CAS-assisted route (Gröbner-style elimination, per knowledge_base
  Linear Algebra "Gröbner-basis ideal membership" idea, or straight symbolic sympy).

### Cheap-kill candidates
None found via the metric lens — no parity/pigeonhole/injection shortcut applies to a
continuous configuration like this. The one genuine structural shortcut is the power-of-
a-point reduction itself (item 1 above), which collapses "prove two distances equal" to
"prove two signed power values equal" — worth doing first in any approach since it is
free (a two-line algebraic fact) and immediately reframes the target.

### Knowledge-base entries to use
- **Synthetic toolkit**: angle chasing, power of a point (+ concyclicity converse
  PA·PB=PC·PD), radical axes & radical center, trig cevians (Ceva/Menelaus), spiral
  similarity — all directly relevant.
- **Coordinates / complex / barycentric**: fallback heavy route; exploit the AB/AC
  midline symmetry.
- General proof methods: direct proof via the reduction chain above is the natural shape.

### Analogous past problems (cruxes)
The crux corpus documentation states plainly: **"geometry — Not in the corpus yet; the
problems DB includes geometry problems with solutions, but no geometry cruxes have been
extracted."** So there is no queryable geometry crux move for this problem domain. No
match to report; the outliner should not expect corpus hints for imo-2026-02 and should
rely entirely on knowledge_base.md + first-principles synthetic/trig work.

### Prior progress
None — workspace was empty at the start of this round.

### Dead ends (do not retry)
- **A' (second intersection of ⊙(AKL) with line AB) does not lie on lines BK, BL, CK, or
  CL** — checked numerically (distances were all ≥0.2, not ~0) across two independent
  configurations. Don't waste a proof attempt assuming a simple incidence there; the
  characterization of A', A'' needs actual metric/trig content, not a one-line incidence.
- **Quadrilateral B,K,L,C is not concyclic** in general (checked numerically, |O₂C|−R₂
  ≈ −0.08 to −0.25, clearly nonzero across the family) — do not assume this as a lemma.

### Small-case / intuition notes (all labeled CONJECTURE / numerically verified, not proved)
- Built a concrete numerical solver: fixed a scalene triangle A=(0,0), B=(5,0.5),
  C=(2,4); parametrized K by (θ, s) = (angle KBA, distance BK) and L by (θ, u) = (angle
  ACL = same θ by (E1), distance CL), then solved (E2),(E3) for (θ,u) given s via
  `scipy.optimize.fsolve`. Found that for `sideK=-1` (K on the same side as the interior
  of triangle BMC, angle measured from ray BA rotating toward the interior) and
  `sideL=+1`, solutions exist satisfying all containment/angle conditions
  (K∈int(BMC), L∈int(BNC), K∈∠LBA, L∈∠ACK) for a continuous range of s ≈ 0.7–2.0 (and
  presumably beyond).
- **The configuration is a genuine 1-parameter family** (4 unknowns for (K,L), 3
  independent scalar equations (E1)-(E3)) — the problem does not pin down K, L uniquely;
  OM=ON is claimed (and holds) for *every* member of this family, for a fixed triangle
  ABC. This is an important structural fact for the outliner: any proof must work for
  the whole family, so it should isolate a quantity that is manifestly parameter-free
  once expressed correctly (this is exactly why the power-of-a-point reduction is
  promising — it reduces to an identity that should hold "for free" once A', A'' are
  correctly characterized via the angle data, rather than needing to pin down (θ,s,u)
  individually).
- **Numerically confirmed OM=ON to ~1e-10–1e-14 relative precision** across 10+ points
  spanning the parameter family (s from 0.7 to 2.0), and also confirmed
  pow(M,⊙AKL)=pow(N,⊙AKL) to the same precision — validating the power-of-a-point
  reduction as correct (not just plausible).
- **Stronger numeric fact (conjecture, but very robust)**: as s varies over the whole
  family, O = circumcenter(AKL) sweeps along a *fixed* line, namely the perpendicular
  bisector of MN (equivalently, the line through midpoint(MN) = (A+midpoint(BC))/2
  perpendicular to BC) — its component along BC relative to that fixed point is 0 to
  machine precision (~1e-16) for every s tested, while its component along the
  perpendicular direction varies smoothly and substantially (−0.41 → +0.47 over the
  tested range). This is logically equivalent to OM=ON but the fact that it holds
  identically along a continuous family is a strong sanity check and suggests O's
  position might be computable in closed form as a function of the free parameter,
  landing exactly on that line — a promising target for a coordinate/vector approach if
  the synthetic route via item 2 stalls.
