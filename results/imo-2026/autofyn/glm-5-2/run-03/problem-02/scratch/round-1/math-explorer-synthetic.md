## imo-2026-02 (IMO 2026 P2, geometry, difficulty 8, proof_only)

LENS: synthetic angle-chase + spiral similarity + isogonal/isotomic + circumcenter characterization.

### Distinct openings (named slugs the outliner could build)

1. **"A-star concyclicity" (the clean crux).** Define A* = reflection of A across the perpendicular bisector of MN. Equivalently (since that perpendicular bisector is perpendicular to BC): A* is the point on the line through A parallel to BC such that its orthogonal projection onto BC is the midpoint D of BC; equivalently A* = A + (D − F) where F is the foot of the altitude from A to BC (fourth vertex of rectangle A−F−D−A*). Then
   - **A, K, L, A* are concyclic** (verified to machine precision on two different triangles, across the whole 1-parameter family of valid (K,L)).
   - If true: O = circumcenter(AKL) is equidistant from A and A*, hence lies on the perpendicular bisector of AA*. But the perpendicular bisector of AA* IS the perpendicular bisector of MN (A* is the reflection of A across it). Hence O ∈ perp-bis(MN) ⟹ OM = ON. ∎
   - This is the recommended main line. The entire proof reduces to ONE cyclicity claim.
   - The cyclicity can be certified by either of two equalities, both numerically confirmed: **∠AKL = ∠AA*L** (subtend chord AL) or **∠KAL = ∠KA*L** (subtend chord KL). (The third pair ∠ALK, ∠AA*K are supplementary, as expected for opposite-side angles.) Pick whichever the angle chase reaches.

2. **"Power-of-a-point / radical-axis" (dual form of the same crux).** OM = ON ⟺ Pow_{circle(AKL)}(M) = Pow_{circle(AKL)}(N) ⟺ MA·MP = NA·NQ where P, Q are the second intersections of circle(AKL) with lines AB, AC respectively. Since MA = AB/2 and NA = AC/2, this is **AB·MP = AC·NQ** (verified numerically to ~1e-13). A proof computes AP, AQ (hence MP = AP − AB/2, NQ = AQ − AC/2) via inscribed-angle / sine-rule in circle(AKL) using the angle conditions, then checks AB·MP = AC·NQ. Equivalent to opening 1 (A* is the point making the chord AA* ∥ BC; P,Q are the same coaxal picture).

3. **"Coaxal pencil" framing.** All circles (AKL) (as K,L range over the 1-parameter family) form a coaxal pencil: they share the two points A and A* (A* = reflection of A in perp-bis(MN)). Their centers lie on the perpendicular bisector of AA* = perp-bis(MN). This is why O is forced onto that line regardless of where on the family K,L sit. Useful as the "invariant" story; still needs the cyclicity of A*.

### Candidate technique(s)
- Synthetic angle chase + **power of a point** (concyclicity converse `PA·PB = PC·PD`).
- **Circumcenter characterization** via perpendicular bisectors; coaxal pencil / radical-axis.
- Likely a **spiral similarity** or a **composition of two rotations** hidden in the angle chain (see alphabet below) — but the naive A-centered spiral similarity is a DEAD END (see dead ends).
- Isogonal/isotomic flavor: condition (i) `∠KBA = ∠ACL` is an isogonal-like cevian relation across vertices B, C; but it is NOT the standard in-triangle isogonal conjugation, and the natural similarity `△ABK ~ △ACL` FAILS (see dead ends).

### Cheap-kill candidates
- The **master relation on K alone**: since L lies inside ∠ACK, `∠ACK = ∠ACL + ∠LCK = (i) + (iii) = ∠KBA + ∠BMK`. So **∠ACK = ∠KBA + ∠BMK** is a direct consequence of (i)+(iii) — a pure relation on K (no L). Verified: the set of K inside △BMC satisfying this is a 1-parameter curve, and for each such K the point L is then uniquely determined by (ii) `∠LBK = ∠LNC` along the ray CL. This relation is the entry point for any angle chase involving K.
- Triangle **△BMK** has angles `α` (at B, because BM lies on BA so `∠MBK = ∠KBA = α`), `γ` (at M), `π−α−γ` (at K).
- Triangle **△CNL** has angles `α` (at C, because CN lies on CA so `∠NCL = ∠ACL = α`), `β` (at N), `π−α−β` (at L).
- These two small triangles (BMK, CNL) are the natural workhorses; both have angle α.

### Knowledge-base entries to use (from `knowledge_base.md`, Geometry section)
- **Synthetic toolkit**: angle chasing, **power of a point** and its concyclicity converse (`PA·PB = PC·PD`), similar triangles, **spiral similarity**, radical axes & radical center.
- **Circle/triangle configuration facts**: Miquel point of a complete quadrilateral (the lines AB, AC, BK, CL form a complete quadrilateral — Miquel point is a candidate for an auxiliary point); Simson line; Ptolemy.
- **Coordinates / complex / barycentric**: a coordinate or complex-plane bash is a viable fallback if the synthetic chase stalls (place B, C on an axis, A generic). The crux `A* = A + (D−F)` and the cyclicity translate into a polynomial identity; verified numerically.
- Homothety at the midpoint: the A-centered homothety h, factor 1/2, sends B→M, C→N, and sends the perpendicular bisector of BC to the perpendicular bisector of MN; it sends circumcircle(ABC) to circumcircle(AMN). Useful for the FINAL step (O on perp-bis(MN) ⟺ O on h(perp-bis(BC))), but does NOT directly transfer the angle conditions (see dead ends).

### Analogous past problems (cruxes)
- **None from the crux corpus.** The crux corpus has NO geometry cruxes (`crux_moves_documentation.md` explicitly states geometry subtopics are not yet extracted). The `past_problems_database.json` contains geometry problem *statements + solutions* but no load-bearing crux moves indexed, so retrieval there is unguided. Do not expect a crux hint from the corpus for this problem.

### Prior progress
- None. Round 1 baseline; `results/imo-2026-02/` is empty (no approaches, no lemmas, no ranking). This report is the first scouting.

### Dead ends (do not retry)
- **A-centered spiral similarity S_A (rotation ∠BAC, ratio AC/AB, sending B→C, M→N, A→A) does NOT send line BK to line CL.** Condition (i) `∠KBA = ∠ACL` makes the image of line BK under S_A land on the line through C that is the **reflection of CL across CA** (the directed angle flips side). Verified numerically: S_A(K) lies off line CL by ~0.1–0.2. So the "S_A transfers B's ray structure to C's ray structure" guess is wrong.
- **△ABK ≁ △ACL.** Checked: only ∠KBA = ∠ACL (=α) matches; ∠KAB ≠ ∠LAC, ∠AKB ≠ ∠ALC, and side ratios AK/AL ≠ AB/AC ≠ BK/CL. So the "two cevians give a direct triangle similarity" approach fails.
- **△AMK ≁ △ANL** (midpoint-homothety analogue): angles MAK ≠ LAN, AMK ≠ ANL, etc. Fails.
- **The midpoint homothety h does not transfer the angle conditions.** h sends line BK to a line through M parallel to BK making angle α with AB; but the actual angle at M is ∠BMK = γ (between MB and MK), and MK is NOT parallel to BK (γ ≠ α in general). Same failure on the N side. So a "homothety copies the angle picture" proof does not work directly; the angles α, β, γ form a *walk/chain*, not a single copied configuration.

### Small-case / intuition notes (CONJECTURE, labeled as such — numeric evidence only, not a proof)
- The configuration (K,L) forms a **1-parameter family** (3 angle equations, 4 positional DOF → 1 free parameter; the "inside" conditions are open inequalities). OM = ON holds for the ENTIRE family (verified to ~1e-9 on two triangles, ~12 sample (K,L) pairs total). This strongly suggests an invariant-line / coaxal-pencil structure rather than a coincidence at an isolated point.
- **Crux conjecture (the load-bearing claim to prove):** Let A* be the reflection of A in the perpendicular bisector of MN (= the point A + (D−F), where D = midpoint of BC and F = foot of the perpendicular from A to BC; equivalently the second intersection of the line through A parallel to BC with the circumcircle of △AKL). Then **A, K, L, A* are concyclic.** Once this is shown, OM = ON follows in one line (O on perp-bis(AA*) = perp-bis(MN)).
- Numeric angle checks supporting the crux: `∠AKL = ∠AA*L` and `∠KAL = ∠KA*L` both hold to ~1e-3 deg across the family. The chase should target one of these.
- Decoded "angle alphabet" (all unsigned, positive in the inside configuration):
  - α := ∠KBA = ∠ACL (condition (i)). Sets the base angle at both B (BK from BA) and C (CL from CA).
  - β := ∠LBK = ∠LNC (condition (ii)). The "gap" BL→BK at B equals the angle NL makes with NC(=CA) at N.
  - γ := ∠LCK = ∠BMK (condition (iii)). The "gap" CL→CK at C equals the angle MK makes with MB(=BA) at M.
  - Consequence: ∠ACK = α + γ (since L inside ∠ACK). This is the master relation on K alone.
  - Orderings: at B, `BA →(α)→ BK →(β)→ BL`; at C, `CA →(α)→ CL →(γ)→ CK`; at M (on AB), `MB →(γ)→ MK`; at N (on AC), `NC →(β)→ NL`.
  - Workhorse triangles: △BMK = (α, γ, π−α−γ); △CNL = (α, β, π−α−β).
- What OM = ON means geometrically: O lies on the perpendicular bisector of MN; since MN ∥ BC and M,N are midpoints, this line is the image of the perpendicular bisector of BC under the A-centered homothety (factor 1/2), i.e. the line through circumcenter(△AMN) = midpoint of (A, O_ABC) perpendicular to BC.
