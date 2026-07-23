## imo-2026-02

- Distinct openings:
  1. **Power-of-a-point reformulation (strongest lead).** OM=ON is equivalent to
     pow(M, ⊙AKL) = pow(N, ⊙AKL). Since A ∈ ⊙AKL and M is the midpoint of AB, the
     power of M along line AB is the signed product MA·MP where P is the *second*
     intersection of line AB with ⊙AKL; similarly pow(N,⊙AKL) = NA·NQ with Q the
     second intersection of line AC with ⊙AKL. Numerically confirmed MA·MP = NA·NQ
     to ~1e-9 in an independent scalene example. This turns the problem into: show
     these two directed-length products along AB, AC are equal — a route that avoids
     ever locating O explicitly and only needs the two secant lengths AP, AQ (or
     equivalently the chord lengths KP-type relations via power of B and C too,
     since B, C are *not* generally on the circle). This looks like the most
     promising synthetic target for the outliner: identify P (second meet of AB with
     ⊙AKL) and Q (second meet of AC with ⊙AKL) synthetically (likely via the angle
     conditions turning into inscribed-angle statements ∠AKP-type or ∠ALQ-type) and
     show AM·AP-type / AN·AQ-type quantities agree — probably by proving AP/AQ has a
     fixed ratio tied to AB/AC, or by directly identifying P, Q as reflections /
     images of B, C under some involution fixed by the K,L construction.
  2. **Perpendicular-bisector-of-MN as the real target (sharper than OM=ON).**
     Numerically, as the (numerically observed) 1-parameter family of valid (K,L)
     pairs is varied, O does not just satisfy OM=ON pointwise — it visibly *slides
     along* the fixed line = perpendicular bisector of MN (verified: the component
     of O − midpoint(MN) along the MN-direction is ~0 to numerical precision, for
     every valid t tested). Concretely this perpendicular bisector is the line
     through the midpoint of segment [A, A'] (A' = midpoint BC) perpendicular to BC
     (since midpoint(M,N) = midpoint(A, A') and MN ∥ BC). This suggests the intended
     proof shows something stronger/cleaner: an explicit fixed line ℓ (perpendicular
     to BC through the midpoint of the A-median) that O always lies on, rather than
     an ad hoc distance computation. Any lemma pinning O to ℓ directly (e.g. via a
     symmetric construction swapping B↔C, M↔N, K↔L that fixes ℓ pointwise) would
     finish the problem in one stroke.
  3. **B↔C, K↔L, M↔N swap symmetry.** The angle hypotheses are manifestly symmetric
     under swapping (B,M,K) ↔ (C,N,L): ∠KBA=∠ACL is self-dual under this swap;
     ∠LBK=∠LNC and ∠LCK=∠BMK are exchanged into each other under (B↔C,K↔L,M↔N).
     This strongly suggests looking for an actual geometric involution (not just a
     relabeling) — e.g. a reflection in ℓ from opening 2, or an inversion/spiral
     map — under which the whole configuration is invariant, swapping B↔C, K↔L,
     M↔N, A↦A (fixed), which would immediately force O (circumcenter of AKL,
     invariant point set {A,K,L} except swapped K,L) onto the symmetry axis, hence
     equidistant from M,N. This is likely the "real" one-line idea behind the
     problem; establishing that such a symmetry literally exists (not just
     label-level) is the crux gap.
  4. **Direct similar-triangle / spiral-similarity search (this lens's primary
     brief) — mostly negative results, reported as leads eliminated.** Tested
     numerically on a scalene triangle: (a) B,K,L,C concyclic — FALSE; (b)
     M,K,L,N concyclic — FALSE; (c) B,N,L,K concyclic — FALSE; (d) C,M,K,L
     concyclic — FALSE; (e) spiral similarity at A carrying B→C, K→L (i.e.
     AB/AC = AK/AL and ∠BAK = ∠CAL) — FALSE (ratios 1.1205 vs 1.0682, angles
     0.1218 vs 0.1063, not equal); (f) BK·CK vs BL·CL equal — FALSE. So the
     "obvious" single spiral similarity or single auxiliary circle does *not*
     exist in this configuration; the true structural relation is more subtle
     (likely a composition of two similarities/spiral maps, one hinged at B via
     the BMK data and one at C via the CNL data, that only becomes visible
     through the circle ⊙AKL itself, matching opening 1).

- Candidate technique(s): power of a point / radical axis (opening 1) combined
  with an underlying symmetry/involution argument (openings 2–3); classical
  spiral-similarity search (opening 4) is largely exhausted for the "obvious"
  candidates and should not be the main line pursued further without a new idea
  for *which* two circles/points to compare.

- Cheap-kill candidates: none obvious as a full kill; but "pow(M,ω)=pow(N,ω) via
  A-secants" (opening 1) is a genuinely cheap reformulation worth handing to the
  outliner before any coordinate bash — it replaces "compute circumcenter" with
  "compare two secant products," which is far more tractable synthetically and
  numerically exact.

- Knowledge-base entries to use: **Synthetic toolkit** (power of a point,
  concyclicity converse `PA·PB=PC·PD`, spiral similarity) — geometry section of
  `knowledge_base.md`; the KB's geometry section is otherwise generic (no
  problem-specific entries yet, no P2-specific lemma). **Coordinates / complex /
  barycentric** entry is a fallback if synthetic power-of-a-point stalls
  (the midline/midpoint structure is very coordinate-friendly, as my numerics
  show: with BC on the x-axis, O always has x-coordinate exactly
  (M_x+N_x)/2 = midpoint of A's projection structure — an analytic/complex-number
  computation of ⊙AKL's center is plausible as a fallback if synthetic routes
  stall, though it requires expressing K, L from the three angle conditions,
  which is itself nontrivial algebraically).

- Analogous past problems (cruxes): **none** — `crux_moves_documentation.md`
  explicitly states the crux corpus has **no geometry cruxes yet**
  ("Not in the corpus yet; the problems DB includes geometry problems with
  solutions, but no geometry cruxes have been extracted"). Domains available
  are number_theory/combinatorics/algebra only. No genuinely analogous crux to
  retrieve for this problem; do not force a match.

- Prior progress: none (round 1, workspace was empty — no `current.md`, no
  approaches, no lemmas existed before this round).

- Dead ends (do not retry): direct/simple concyclicity of {B,K,L,C},
  {M,K,L,N}, {B,N,L,K}, {C,M,K,L} — all numerically false on a generic scalene
  triangle (A=(1,4), B=(−3,0.5), C=(2.5,−0.5)); a single spiral similarity at A
  sending B→C and K→L — numerically false (unequal ratios AB/AC vs AK/AL and
  unequal angles ∠BAK vs ∠CAL). Do not re-test these; they are cleanly refuted
  by the numeric example above, not just "unproven."

- Small-case / intuition notes (all conjectural, verified only numerically to
  ~1e-9–1e-11 residual on two independent scalene triangles with a swept free
  parameter, using `scipy.optimize.fsolve` with region-validity filters for
  K ∈ int(BMC), L ∈ int(BNC), K inside ∠LBA, L inside ∠ACK):
  - The three given angle equations under-determine (K,L) by one degree of
    freedom (4 unknowns, 3 equations); there is a genuine 1-parameter family of
    valid configurations for fixed △ABC, not a unique (K,L).
  - OM = ON holds for every member of this family that was tested (residuals
    ~1e-9 to 1e-11, well below numerical noise), strongly supporting the claim.
  - Stronger conjecture (opening 2): O does not just satisfy OM=ON at each
    instance but literally moves along the fixed perpendicular bisector of MN
    as the free parameter varies — i.e. the *locus* of O over the valid family
    is contained in that one line. If provable, this is likely a cleaner
    target than a pointwise distance computation.
  - pow(M, ⊙AKL) = pow(N, ⊙AKL) exactly (opening 1), confirmed via both the
    direct OM²−R² / ON²−R² formula and via the secant-length products
    MA·MP = NA·NQ along lines AB, AC.
