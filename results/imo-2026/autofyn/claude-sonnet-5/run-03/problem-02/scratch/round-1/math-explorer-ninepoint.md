## imo-2026-02

- Distinct openings:
  1. **Fixed-line reformulation (algebraic/vector).** Take A as the origin. Then M = B/2, N = C/2. Direct computation gives
     OM² − ON² = O·(C−B) + (|B|²−|C|²)/4 (vectors from A). So **OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4**, i.e. O lies on the fixed
     line ℓ = {X : X·(C−B) = (|C|²−|B|²)/4}. Since the circumcenter O_ABC of ABC satisfies O_ABC·(C−B) = (|C|²−|B|²)/2 (same
     identity, undivided), the target condition is exactly "O's projection onto BC direction is **half** that of O_ABC's" —
     i.e. **ℓ is the image of the perpendicular bisector of BC under the homothety h(A, 1/2)** (the same homothety sending
     B↦M, C↦N). This is elementary (no need to invoke the nine-point circle at all), and gives the outliner a clean,
     coordinate-free target: *show O lies on h(A,1/2)(perp-bisector of BC)*.
  2. **Nine-point-circle framing (equivalent, heavier machinery).** M, N lie on the nine-point circle (well known). OM=ON
     says O lies on the perpendicular bisector of chord MN of that circle, which passes through the nine-point center
     N9 and is perpendicular to BC (since MN ∥ BC). Verified numerically N9 is equidistant from M,N (as expected) and that
     this perpendicular bisector coincides with the line from opening 1. This framing is not obviously more useful than
     opening 1 (it adds an unnecessary named object, the nine-point center) — recommend opening 1's vector identity as the
     target unless the outliner finds a synthetic angle-chase that naturally produces the nine-point circle.
  3. **Spiral-similarity structure in the three given angle equalities — worth flagging, unproven.** Each of the three
     hypotheses pairs two triangles sharing a vertex with an angle equality at the "other" vertices, the classic signature
     of a spiral-similarity conclusion (not yet shown to literally hold, but suggestive as the intended engine):
     - `∠KBA = ∠ACL`: triangles ABK, ACL — angles at B, C respectively equal. Consistent with (but not proven equal to) a
       spiral similarity centered at A sending B↦C, K↦L.
     - `∠LBK = ∠LNC`: triangles LBK, LNC share vertex L, with angle at B (in LBK) = angle at N (in LNC). This is exactly the
       shape of one conclusion of a spiral similarity centered at L sending B↦N, K↦C (SAS-similar triangles LBK ~ LNC would
       give both `∠LBK=∠LNC` AND `∠LKB=∠LCN`; here only one of the two is given as hypothesis).
     - `∠LCK = ∠BMK`: triangles KCL, KMB share vertex K, angle at C = angle at M. Same shape, spiral similarity centered
       K sending C↦M, L↦B.
     If the outliner can show these spiral similarities actually hold (using the *other* two hypotheses to supply the missing
     ratio/angle condition each time — the three conditions look set up to bootstrap each other, three unknowns/three
     conditions), then O (circumcenter of AKL) becomes the image, under the A-centered map, of a well-understood point
     (circumcenter of ABC or a related triangle), and opening 1's vector identity becomes a direct computation. This is the
     likely intended route but is NOT verified here — flagged as a promising direction, not a result.

- Candidate technique(s): vector/coordinate identity for "equidistant from two points" (opening 1) as the target reduction;
  spiral similarity (opening 3) as the likely mechanism generating that target from the hypotheses; angle chasing to locate
  K, L relative to circles through B,M,C-side and N-side triangles. Homothety h(A,1/2) (mapping B↦M, C↦N) is the key fixed
  map — note it also sends the circumcircle of ABC to a circle through M,N tangent-configuration-adjacent to the nine-point
  circle (in fact IS a scaled copy, not literally the nine-point circle, but carries the same equidistance structure).

- Cheap-kill candidates: none found — this is a genuine construction/angle-chase problem, no parity/pigeonhole shortcut
  applies. The one "cheap" win is the vector reduction in opening 1, which converts the target from "circle geometry" to a
  single linear equation in O — worth doing first since it's free and sharply narrows what must be proven.

- Knowledge-base entries to use: "Synthetic toolkit" (angle chasing, power of a point, spiral similarity, radical axes) —
  `knowledge_base.md` line ~129-131; "Coordinates / complex / barycentric" (line ~137) for the A-origin vector computation
  in opening 1; "Circle/triangle configuration facts" (Miquel point, Simson line) — possibly relevant if K, L end up as
  Miquel-point-like constructions of some quadrilateral, but not confirmed.

- Analogous past problems (cruxes): **none** — per `crux_moves_documentation.md`, the crux corpus (`past_crux_moves_database.json`)
  has **zero geometry entries** ("Not in the corpus yet; the problems DB includes geometry problems with solutions, but no
  geometry cruxes have been extracted"). So no crux-move retrieval is possible for this problem; do not force a match from
  another domain. (The `past_problems_database.json` does contain full geometry problem statements+solutions with no domain
  filter for cruxes, but there is no indexed "geometry" subtopic list to query against.)

- Prior progress: none (round 1, workspace just created).

- Dead ends (do not retry): none recorded yet — this is the first exploration round.

- Small-case / intuition notes (all labeled conjecture/numerical, not proof):
  - Built two independent numerical instances of the full configuration (two different scalene triangles), parametrizing
    the residual 1-parameter freedom by t = ∠KBA = ∠ACL (this angle appears directly in hypothesis 1, so setting it as a
    shared parameter automatically satisfies that equation; then solved the remaining 2 equations `∠LBK=∠LNC`,
    `∠LCK=∠BMK` for the two free radii `BK`, `CL` via numerical root-finding). This **confirms the problem is a 4-dof
    (K,L)-configuration with only 3 equations, hence a genuine 1-parameter family of valid (K,L) for fixed ABC** — the
    positional constraints (K inside triangle BMC, L inside triangle BNC, K inside ∠LBA, L inside ∠ACK) cut this down to a
    sub-arc of the parameter t (verified numerically: both containment conditions hold only for a sub-range of t, e.g.
    roughly t ∈ (0.05, 0.42) in one instance).
  - Across the entire valid sub-range of t in both test triangles, **OM = ON held to numerical precision (~1e-11 to 1e-15
    relative)** — strong (but non-proof) confirmation of the claim, and confirms it is not an artifact of a special/isoceles
    triangle.
  - Also confirmed numerically that O traces along the fixed line ℓ (opening 1 / opening 2's perpendicular bisector of MN)
    as t varies across the valid range — i.e. O moves but stays exactly on the predicted fixed line, giving direct visual
    confirmation that "O ∈ ℓ" is the right intermediate target, not just a coincidental OM=ON at isolated points.
  - Verified separately (pure vector algebra, exact) that h(A,1/2) applied to the ABC-circumcenter lands exactly on ℓ, and
    that the nine-point center of ABC also lies on ℓ (both checked to float precision ~1e-16), corroborating the two
    equivalent framings in openings 1–2.
