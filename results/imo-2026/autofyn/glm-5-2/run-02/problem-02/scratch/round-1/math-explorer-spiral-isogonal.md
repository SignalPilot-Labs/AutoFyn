## imo-2026-02 (IMO 2026 P2) — lens: spiral similarity / isogonal / circumcenter

### Distinct openings (this route to the WHOLE problem)

**Opening A — homothety + antipode reduction (the clean one; VERIFIED numerically).**
Let h be the homothety centered at A, ratio 1/2. Then M = h(B), N = h(C). The perpendicular bisector of MN is the image under h of the perpendicular bisector of BC (parallel to it, through h(midpoint of BC) = midpoint of MN). Hence
  OM = ON  ⟺  O ∈ h(pbis(BC))  ⟺  h⁻¹(O) = 2O − A ∈ pbis(BC).
But 2O − A is exactly the antipode of A on the circumcircle of △AKL (the point A' diametrically opposite A, since O is the circle's center). So:

  **OM = ON  ⟺  A' := 2O − A satisfies A'B = A'C  ⟺  A' lies on the perpendicular bisector of BC.**

This is an equivalence, not a conjecture: A' − B = 2O − A − B = 2(O − (A+B)/2) = 2(O − M), so |A'B| = 2·|OM| and |A'C| = 2·|ON|; thus A'B = A'C ⇔ OM = ON exactly. (Confirmed numerically to 1e-12.) The problem becomes: prove the antipode of A on (AKL) is equidistant from B and C.

A' is characterised without O by two right angles: ∠AKA' = ∠ALA' = 90° (angle in semicircle, AA' a diameter). So A' = (line through K ⊥ AK) ∩ (line through L ⊥ AL). Target: this point lies on pbis(BC).

**Opening B — spiral-similarity reading of the three angle conditions.**
Write α = ∠KBA = ∠ACL, β = ∠LBK = ∠LNC, γ = ∠LCK = ∠BMK. Because M ∈ AB and N ∈ AC, MB ∥ AB and NC ∥ AC, so:
  α = ∠(BK, AB) = ∠(AC, CL);
  β = ∠(BL, BK) = ∠(NL, AC);        (NL is a ray from N)
  γ = ∠(CL, CK) = ∠(AB, MK).
Numerically (B=(−1,0), C=(1,0), A=(0.3,2), ∠A≈52.3°, ∠B≈57.0°, ∠C≈70.7°) the following three triangle similarities hold simultaneously (one per condition; the other two angle equalities are forced by the construction):
  - (cond 1) △ABK ~ △ACL with A↔A, B↔C, K↔L  ⟹  spiral similarity centered at **A** sending BK → CL, ratio AB/AC, rotation ∠BAC. Consequence: ∠BAK = ∠CAL, i.e. **AK and AL are isogonal cevians of ∠A** (this is the isogonal thread).
  - (cond 2) △LBK ~ △LNC with L↔L, B↔N, K↔C  ⟹  spiral similarity centered at **L** sending BK → NC, ratio LB/LN = LK/LC.
  - (cond 3) △LCK ~ △BMK with K↔K, L↔B, C↔M  ⟹  spiral similarity centered at **K** sending LC → BM, ratio KL/KB = KC/KM.
The midpoint choice (M on AB, N on AC) is exactly what makes the ratios in (2) and (3) chainable: BM = AB/2, CN = AC/2 link the spiral at L (uses N) and at K (uses M) to the spiral at A (uses B, C). So the three spirals compose, and the composition is a projective/linear map whose fixed structure should force A' onto pbis(BC).

**Opening C — target as a constant-angle condition (conjectured, numerically robust).**
Across all choices of the free parameter α (the configuration is a 1-parameter family: 4 unknowns (K,L) × 2 coords − 3 angle eqns = 1 DOF), the antipode A' satisfies, independently of α:
  **∠A'BK = 90° − ∠C,   ∠A'CL = 90° − ∠B.**
These two equalities are equivalent (each implies A' on pbis(BC) since ∠A'BK = 90°−C ⇔ ∠A'BC = 90°−∠A−α ⇔ base angles of △A'BC equal). Equivalent clean form: ∠A'BC = ∠A'CB = 90° − ∠BAC − α, i.e. ∠BA'C = 2∠BAC + 2α. (Numerically exact to 3 dp for α = 10°,12°,15°,18°,20°,25°.) Proving either of these is the load-bearing step.

### Candidate technique(s)
- Spiral similarity (centred at A, L, K) — three of them, one per angle condition; the KB entry "spiral similarity" under Synthetic toolkit.
- Isogonal cevians in ∠A (AK, AL): the consequence ∠BAK = ∠CAL of cond (1).
- Circumcenter / perpendicular-bisector characterisation via the antipode / diameter (AA' is a diameter of (AKL)).
- Power of a point: OM = ON ⟺ Pow_(AKL)(M) = Pow_(AKL)(N); with M∈AB, N∈AC this becomes a relation on the second intersections of AB, AC with (AKL). (Alternative route, less direct than the antipode.)
- Radical axis / coaxal: pbis(MN) is the radical axis of the point-circles at M, N; equidistant-from-M,N = equal power. Could pair with Miquel of the spiral configuration.

### Cheap-kill candidates
- The homothety+antipode equivalence (Opening A) IS the cheap kill for the *target reformulation*; it removes O and the circle radius entirely and reduces the problem to one pure incidence/angle statement about A'. Use this first — every rival approach should at least state the target this way.
- Isogonality ∠BAK = ∠CAL (free from cond 1 + spiral at A) is a one-line structural consequence worth isolating as a lemma.

### Knowledge-base entries to use (named)
- **Synthetic toolkit — spiral similarity** (the three spiral centres A, L, K).
- **Synthetic toolkit — angle chasing, power of a point / concyclicity converse PA·PB=PC·PD** (for the radical-axis / power reformulation of OM=ON).
- **Circle/triangle configuration facts — Miquel point of a complete quadrilateral** (the three spiral centres arise from the complete quadrilateral BKM-CN-L; a Miquel-style point may coincide with A').
- **Synthetic toolkit — radical axes & radical center, perpendicular bisector / circumcenter characterizations** (circumcenter of AKL ↔ pbis(AK) ∩ pbis(AL); antipode via diameter).
- General: **Reformulate** (geometry ↔ the homothety image) and **Work backward** (assume A' on pbis(BC), derive angle conditions).

### Analogous past problems (cruxes)
- `aimo-0021` (IMO-SL 2013, Iran): same midpoint pair M of AB, N of AC; uses perpendicular bisectors of AC, AB and circumcircles of AMT, ANT meeting them — the *midline + perpendicular-bisector* structural crux is analogous, but the construction (arc-midpoint T, circumcircle intersections) is different. Weak analogy; useful only for the "midpoints of AB, AC ⟹ pbis(MN) ∥ pbis(BC)" reflex.
- `aimo-0644` (USA TSTST 2011): M, N midpoints of AB, AC; circumcenter O, orthocenter H; rays MH, NH meet circumcircle. Targets a perpendicularity at A. Shares the M,N-midpoint + circumcenter setting but the orthocenter/circumcircle mechanism differs.
- No genuinely close crux match found in the corpus for the *three-paired-angles + antipode* structure. The geometry crux corpus is empty (per documentation), so this is a hint to adapt, not a citation.

### Prior progress
None — round 1, no approaches yet.

### Dead ends (do not retry)
None yet (round 1). One warning from probing: the interior-angle function in numpy picks the smaller angle, so obtuse angles in the spiral triangles read as their supplements — outliner must handle directed angles mod 180 throughout to avoid spurious "angle equalities" / wrong cases.

### Small-case / intuition notes (all CONJECTURED from numerics, not proved)
- 1-parameter family of (K, L) for fixed △ABC (4 coord unknowns − 3 angle conditions); OM = ON holds throughout — robust identity, not a rigidity. So the proof should be an angle/directed-angle chase, not a metric computation that pins K, L.
- The free parameter can be taken as α = ∠KBA = ∠ACL; β, γ are then determined (numerically β ≈ 24°, γ ≈ 32° for α=15° in the test triangle, both decreasing as α grows).
- Antipode A' moves *along* pbis(BC) as α varies (its x-coordinate is exactly 0 when BC is placed symmetrically at (±1,0)); its height shrinks as α grows. A'B = A'C ≡ constant 2·OM.
- The three spiral similarities (at A, L, K) all hold simultaneously in every sampled configuration — strong evidence they are theorem-grade, not numerical coincidence. Cond (1) ⇒ spiral at A; the other two angle equalities of △ABK~△ACL (∠BAK=∠CAL, ∠AKB=∠ALC) are *forced* by the construction, not extra hypotheses — outliner should prove this forcing (likely via the ray picture below).
- Ray picture (clean): with directions measured from BA / CA into the triangle, BK is at angle α from BA; BL at α+β; CL at α from CA; CK at α+γ from CA; MK at γ from MB (∥AB); NL at β from NC (∥AC). K = (ray B, α) ∩ (ray M, γ); L = (ray C, α) ∩ (ray N, β); the two remaining constraints are ∠LCK = γ and ∠LBK = β. This ray parametrisation is the natural language for the angle chase.

### Where is the genuine difficulty / crux move this route needs
The reformulation (Opening A) is clean and done. The crux, the 1–2 hard steps an outliner must plan:

1. **Link the three spiral similarities (which involve M, N) to the antipode A' (defined by A'K ⊥ AK, A'L ⊥ AL).** Concretely: show ∠A'BK = 90° − ∠C (and symmetrically ∠A'CL = 90° − ∠B). The mechanism is that MB ∥ AB and NC ∥ AC turn conditions (2),(3) into relations between {MK, CK} and {NL, BL}; the two right angles at K, L (from A' being the antipode) then convert these into the angle-at-A' relations. This is a *three-step angle chase through the right angles*, not a one-liner; directed angles mod 180 are mandatory.
2. **Certify that △ABK ~ △ACL, △LBK ~ △LNC, △LCK ~ △BMK are all genuine (not just one-angle)**, i.e. that the construction forces the other angle equalities. The ray picture above is the proof vehicle: once K, L are placed by the ray intersections, ∠LCK = γ and ∠LBK = β are *constraints* that close the similarity. The outliner should derive the second angle equality of each pair from the ray configuration before chaining into the antipode step.

### Does this route feel promising vs a known trap?
**Promising.** The antipode reduction removes the circumcenter/radius entirely and converts OM = ON into the single, checkable incidence "A' = (K⊥AK)∩(L⊥AL) lies on pbis(BC)." The numerical target ∠A'BK = 90°−C is exact and α-independent, so it is a real theorem, not an artifact. The three spiral similarities give a rich, structured supply of angle equalities to feed the chase.

**Trap to watch:** the chase through the right angles can branch on configuration (which side of AK the point A' lies, whether ∠A'KB = 90°+∠AKB or 90°−∠AKB). The 1-parameter freedom means the *quantities* are continuous in α but the *sign* of a directed angle can flip at a degenerate α; the outliner should phrase everything as directed angles mod 180 from the start, and the builder should verify the configuration assumptions (K inside △BMC, L inside △BNC, K inside ∠LBA, L inside ∠ACK) are exactly what pins the signs.
