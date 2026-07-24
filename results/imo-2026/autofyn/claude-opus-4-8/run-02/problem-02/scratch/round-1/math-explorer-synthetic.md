## imo-2026-02 (lens: pure synthetic geometry — spiral similarity / perpendicular-bisector structure)

- Distinct openings:
  1. **Homothety reduction of the goal (verified numerically, cheap and rigorous).**
     Since M,N are midpoints of AB, AC, the homothety h = h(A, 1/2) sends B→M, C→N.
     Hence h sends the perpendicular bisector of BC to the perpendicular bisector of
     MN (homothety preserves perpendicularity and midpoint ratios, mapping segment BC
     to segment MN). So **OM = ON ⟺ O lies on h(perp-bisector of BC) ⟺ the point
     O' := h(A,2)(O) = 2O − A is equidistant from B and C** (apply the inverse
     homothety h(A,2), noting A is the fixed point). Moreover, since A is the center
     of h, and h(A,2) maps K↦K'=2K−A, L↦L'=2L−A (i.e. K is the midpoint of A and
     K'; likewise L), and homothety centered at the circumcenter's own defining point
     A carries circumcenters to circumcenters, **O' is exactly the circumcenter of
     triangle A K' L'.** So the target becomes: *the circumcenter of AK'L' is
     equidistant from B and C*, where K' = 2K−A, L' = 2L−A. I verified this
     equivalence numerically (see below) — it is an exact algebraic restatement, not
     a new hypothesis, so it's a safe reduction for the outliner to build on. It
     also isolates a single fixed target line (perpendicular bisector of MN, a line
     through the midpoint of the median AA′ perpendicular to BC, where A′=midpoint
     BC) that O must lie on for ALL valid (K,L) satisfying the angle system — a
     strong invariant worth exploiting (see below: it suggests O's position along
     that line is a genuine one-parameter family, i.e., the constraint "OM=ON" is
     not an accident of one particular K,L but a whole line of possible O's).
  2. **Degenerate/symmetric case as a sanity template, not a proof.** In the
     isosceles case AB=AC, by the reflection symmetry across the perpendicular
     bisector of BC (= axis through A), K and L become mirror images of each other
     (verified numerically to ~1e-9), and O automatically lands on the axis, giving
     OM=ON trivially. This suggests the general (scalene) proof should produce K,L
     related by a "generalized reflection" (an affine involution swapping the B-side
     data with the C-side data: B↔C, M↔N, K↔L in some categorical sense) even when
     no literal mirror symmetry exists — i.e., look for an involutive
     correspondence (perhaps a spiral similarity or isogonal-type conjugation)
     linking the K-side conditions (∠KBA, ∠BMK) to the L-side conditions (∠ACL,
     ∠LNC) via swapping B↔C and M↔N, since the three given equalities visibly pair
     up as: (∠KBA ↔ ∠ACL), (∠LBK ↔ ∠LNC is NOT a clean swap of a single ∠LCK-type
     term — see gap below).
  3. **Spiral-similarity attempt on conditions 2 & 3.** ∠LBK = ∠LNC and ∠LCK =
     ∠BMK each equate an angle at B (resp. C) to an angin at N (resp. M) — i.e. an
     angle in the "K,L configuration near B/C" to an angle in the "midpoint
     configuration near N/M". This is exactly the shape of the spiral-similarity
     lemma's angle hypothesis (spiral similarity centered at a point P mapping X→X′,
     Y→Y′ exists iff the circles (P,X,X′) and (P,Y,Y′) meet again at the similarity
     center, and the defining angle equality is of the same "cross" form). Candidate
     to test: is there a spiral similarity centered at L taking B↦N and K↦C (this
     would force ∠LBK=∠LNC automatically as the equal base angles, PLUS a ratio
     condition LB/LN=LK/LC that is NOT given — so the hypothesis alone gives only
     the angle equality, not full similarity). Symmetric candidate: spiral
     similarity centered at K taking C↦M, L↦B for condition 3. **These are only
     partial (one angle, not two), so proving genuine spiral similarity requires an
     extra ratio fact not obviously in the hypotheses — flag as a likely dead end
     unless a second angle relation can be extracted from conditions 1 and the
     region constraints (K inside ∠LBA, L inside ∠ACK).**
  4. **Direct trig/vector computation of O exploiting the homothety-reduced target.**
     Given the reduction in (1), the cleanest fully rigorous route may be: express
     O's position via the standard circumcenter formula (intersection of
     perpendicular bisectors of AK and AL, or via the extended law of sines /
     rotation formula O = A + rotation by the angles at K, L), substitute the three
     given angle equalities as constraints relating ∠KBA, ∠LBK, ∠LCK to fixed
     angles of the base triangle (∠ACL, ∠LNC, ∠BMK), and directly show the
     resulting expression for (O−midpoint(MN))·(C−B) vanishes. This is not
     "synthetic" in the classical sense but is a natural fallback if spiral
     similarity in (3) stalls; it uses only "extended law of sines in circumcircle"
     + the homothety reduction — no heavy coordinate bash needed since direction
     vectors along BC are all that's required (one scalar equation).

- Candidate technique(s): homothety (ratio 1/2 at A) transferring perpendicular
  bisector of BC to perpendicular bisector of MN (rigorous reduction, safe to use);
  spiral similarity lemma (conditional, see gap in opening 3); extended law of
  sines / rotation representation of circumcenter as fallback computation.

- Cheap-kill candidates: the homothety reduction (opening 1) is itself a cheap,
  rigorous structural move that should be adopted by every approach regardless of
  route — it turns "OM=ON" into "circumcenter of AK'L' is equidistant from B,C" or
  equivalently "O lies on the fixed line through midpoint(AA′) ⊥ BC" — a strictly
  smaller and more concrete target. No parity/pigeonhole applicable (this is a
  continuous geometry problem); the isosceles-symmetry check (opening 2) is a
  cheap sanity filter to validate any proposed closed-form for O before trusting it.

- Knowledge-base entries to use: **Synthetic toolkit** (spiral similarity, similar
  triangles, angle chasing) and **Coordinates/complex/barycentric** (as fallback,
  entry in Geometry section) from `knowledge_base.md`. No entry specifically
  covers homothety-of-perpendicular-bisectors, but it follows directly from
  "Circle/triangle configuration facts" style reasoning (similarity transforms
  preserve perpendicularity/concyclicity — same family of facts as Miquel
  point/spiral similarity entries).

- Analogous past problems (cruxes): **none** — `crux_moves_documentation.md`
  states explicitly: "geometry — Not in the corpus yet; the problems DB includes
  geometry problems with solutions, but no geometry cruxes have been extracted."
  So the crux corpus cannot be queried for this domain; no analogous crux to cite.

- Prior progress: none (first round, empty `results/imo-2026-02/approaches/`).

- Dead ends (do not retry): none recorded yet (first round). Flagging in advance:
  the "AK=AL" conjecture is FALSE in general (see numeric data below) — do not
  assume K,L are symmetric about line AO or that triangle AKL is isosceles from A;
  also the "A,K',L',B,C all concyclic" conjecture (with K'=2K−A, L'=2L−A) is FALSE
  (checked numerically: circumradius of AK'L' ≠ distance to B,C, even though
  O'B=O'C holds) — don't waste a round trying to prove a 5-point concyclicity.

- Small-case / intuition notes (all CONJECTURE / numerical, not proof):
  - Built a concrete scalene example: B=(0,0), C=(5,0), A=(1.3,4.0). For a
    1-parameter family of valid (K,L) (parametrized by t=∠KBA=∠ACL ∈ [10°,40°],
    solving the remaining two angle equations numerically via `scipy.fsolve` for
    the two free distances r_K=BK, r_L=CL), I confirmed **OM=ON holds to ~1e-11**
    at every sampled t (see computed table: t=10..40 degrees, diff OM−ON ~1e-11
    to 1e-15).
  - Stronger empirical fact: **the circumcenter O has CONSTANT x-coordinate
    (=1.9) across the entire family**, in coordinates where BC is the x-axis. That
    constant equals exactly the x-coordinate of the midpoint of M and N (M=(0.65,
    2.0), N=(3.15,2.0), midpoint x=1.9). I.e. **O doesn't just satisfy OM=ON for
    each individual valid (K,L) — it traces the entire fixed line "perpendicular
    bisector of MN" as the free parameter t varies.** This is strong structural
    evidence that the right proof strategy is to show O always lies on this one
    fixed line (a codimension-1 condition, i.e. one real equation), rather than
    trying to pin down K and L individually — supports opening 1/4.
  - Isosceles-symmetry check (B=(−2,0), C=(2,0), A=(0,4)): confirms K,L become
    exact mirror images (K_x=−L_x, K_y=L_y to 1e-9) and O lands on the axis
    (O_x≈0 to 1e-12) — consistent, sanity-checks the whole numerical setup and
    the homothety reduction, but is not itself a general proof (only the isosceles
    special case).
  - AK ≠ AL numerically (e.g. at t=10°: AK≈2.78, AL≈3.24) — rules out any approach
    assuming triangle AKL is isosceles from A in the scalene case.
