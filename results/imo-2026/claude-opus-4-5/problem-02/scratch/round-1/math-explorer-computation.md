## imo-2026-02

### Coordinate Setup

Place B=(0,0), C=(1,0), A=(a,b) with b>0. Then:
- M = midpoint(AB) = (a/2, b/2)
- N = midpoint(AC) = ((a+1)/2, b/2)
- MN is horizontal (both endpoints at height b/2)
- Perpendicular bisector of MN: vertical line x = (M_x+N_x)/2 = (2a+1)/4

**Degrees of freedom**: Triangle has 2 free parameters (a,b). Given K inside BMC and L inside BNC (4 real DOF), the 3 angle conditions reduce to a 1-parameter family of valid (K,L) pairs.

### Key Reduction (Computational)

**OM=ON iff circumcenter O has x-coordinate = (2a+1)/4.**

Proof: |OM|² - |ON|² = (m_x² - n_x²) - 2(m_x - n_x)·O_x = -(2a+1)/4 + O_x.
So OM=ON iff O_x = (2a+1)/4. This is exact (coordinate computation).

### Pivotal Computational Discovery

**All circumcircles of AKL (over the entire 1-parameter family) pass through the fixed point A' = (1/2, b).**

Verified numerically to machine precision (error < 10^{-14}) across 6+ triangles and 22 valid (K,L) pairs. 

**A' is the reflection of A over the perpendicular bisector of MN:**
- Perp bisector of MN is x = (2a+1)/4
- Reflection of A=(a,b) over this line: x_new = 2·(2a+1)/4 - a = 1/2
- So A' = (1/2, b). ✓

**A' has a clean geometric description**: A' is the unique point that lies on both (i) the perpendicular bisector of BC (since A'_x = 1/2 = midpoint(BC)_x, giving |A'B|=|A'C|) and (ii) the horizontal line through A (since A'_y = b = A_y). Equivalently: A' is the intersection of the perpendicular bisector of BC with the line through A parallel to BC.

### The Proof Skeleton (Computational Observation → Strategy)

1. **Define A'** = reflection of A over perp bisector of MN = intersection of (perp bisector of BC) with (line through A parallel to BC). In coordinates: A' = (1/2, b).

2. **Key Lemma** (all three conditions needed): The circumcircle of AKL passes through A'.

3. **Conclusion**: Since A and A' = ρ(A) (reflection over perp bisector of MN) both lie on the circumcircle, the circumcircle is symmetric under ρ, so its center O lies on the perp bisector of MN, giving OM = ON.

The algebraic condition for Key Lemma (A, K, L, A' concyclic) in complex notation:
With p = A-K, q = A-L, δ = 1/2-a (real horizontal displacement from A to A'):
**(p+δ)q / (p(q+δ)) must be real** (cross-ratio condition).

### Which Conditions Are Needed?

- Conditions 2+3 alone: do NOT guarantee A' on circumcircle (numerical error ~10%, not ~10^{-14})
- Conditions 1+2 alone: do NOT guarantee A' on circumcircle (error ~10^{-2})
- All 3 together: A' on circumcircle to machine precision

So all three conditions are genuinely needed for the key lemma.

### Distinct Openings

1. **Reflection/fixed-point attack** (primary): Define A' = intersection(perp-bisector(BC), line through A parallel BC). Prove circumcircle(AKL) passes through A'. Since A' = ρ(A), this forces O on perp-bisector(MN). The hard step is showing A' on the circumcircle.

2. **Directed angle chase**: The Key Lemma ↔ ∠KAL = ∠KA'L (directed, mod π). Since |A'B|=|A'C|, A' has a special relationship to B and C. Look for a chain:
   ∠KA'L = ∠KA'B + ∠BA'L → express via conditions 2 and 3 → use condition 1 to close.

3. **Spiral similarity attack**: Condition 2 (∠LBK = ∠LNC) says the spiral similarity centered at L mapping B→N also maps the ray BK to the direction of NC (up to mod π). Condition 3 similarly. These two spiral similarities (centered at L and K respectively) might compose to fix A' or constrain the circumcircle.

4. **Power-of-a-point attack**: Show pow(A', circumcircle(AKL)) = 0 using:
   pow(A') = A'K · A'K' (for some second intersection K' of line A'K with the circle).
   The angle conditions might pin down K' to a known point.

5. **Coordinate bash (sympy)**: Write all three conditions as polynomial equations (using cross-product / dot-product form for angles), substitute and verify (p+δ)q / (p(q+δ)) is real. Likely messy but mechanically correct.

### Candidate Techniques

- **Directed angles mod π** (inscribed angle theorem + concyclicity criterion)
- **Spiral similarities** (conditions 2 and 3 look like spiral similarity conditions)
- **Radical axes** (if A' lies on a radical axis of two natural circles)
- Synthetic: angle chasing with the specific role of midpoints M, N

### Knowledge-Base Entries to Use

- **Synthetic toolkit** (geometry section): "angle chasing, power of a point, radical axes, spiral similarity" — directly applicable.
- **Circle/triangle configuration facts**: Inscribed angle theorem (central tool), Miquel point of a complete quadrilateral (might be relevant given the four points B, C, K, L and their connections to M, N).
- **Coordinates / complex / barycentric**: The key lemma (p+δ)q/(p(q+δ)) real can be attacked algebraically in complex coordinates.

### Analogous Past Problems (Cruxes)

The crux corpus has no geometry entries; cannot retrieve analogous problems.

### Prior Progress

None — this is Round 1, problem is unsolved, no approaches exist yet.

### Dead Ends (Do Not Retry)

- **No 4-point concyclicities** among {A,B,C,M,N,K,L} for a generic valid (K,L) pair (checked all 35 combinations of 4 points, none are concyclic).
- **Spiral similarity at L mapping B→N, K→C** does NOT hold ((C-L)/(K-L) ≠ (N-L)/(B-L), error ~0.76).
- **K and L symmetric about perp-bisector of MN**: NOT true (k_x + l_x ≠ 2·(2a+1)/4 in general).

### Small-Case / Intuition Notes

- **Isoceles case** (a=1/2): A = A', so the circumcircle trivially passes through A (= A'). The reflection symmetry of the isoceles triangle makes the conclusion obvious. The general case requires genuine work.
- **Conjecture** (strongly supported, not proved): The Key Lemma (circumcircle of AKL passes through A') is the crux. It is an intrinsic property of the angle system—all three conditions contribute.
- **The 1-parameter family** of valid (K,L) pairs traces out a curve in the (K,L) space; along this curve, circumcenter O always has O_x = (2a+1)/4 exactly (to 15 digits). The family is non-degenerate (varies over a range of angles).
- **Angle at A**: angle_KAL = angle_BAC - (angle_BAK measured from A) - (angle_CAL measured from A). This provides another way to compute angle_KAL in terms of the given conditions.
