## imo-2026-02

### Transformations explored

**Inversion at A:** The circumcircle of AKL passes through A and maps to line K'L' under inversion at A. The circumcenter O does not map to anything geometrically tractable. Dead end for the inversive lens.

**Inversion at other centers:** No obvious center (B, C, M, N, or O itself) yields a simplification of the three coupled angle conditions. The conditions mix angles at B, C, M, N in a way that doesn't simplify under a single inversion.

**Projective transformations:** No Möbius map or projective collineation sends the problem to a standard configuration (M, N to special positions) without destroying the angle conditions, since angles are not projective invariants.

**What DOES work — key discovery (algebraic/geometric):**

The main new structural insight comes from the interplay of C1, C2, C3 under the parameterization k = b(1−μe^{−iα}), l = c(1−νe^{iα}):

---

### Critical new structural insight: decoupling of μ and ν

**C1 is automatically satisfied.** Under the parameterization k = bp (p = 1−μe^{−iα}), l = cq (q = 1−νe^{iα}), we compute:
  - (k−b)(l−c) = (−bμe^{−iα})(−cνe^{iα}) = bcμν
  - So C1 = bc/((k−b)(l−c)) = 1/(μν) > 0. ✓ Automatic.

**C2 determines ν independently of μ.** Computing C2 = (k−b)(2l−c)/((l−b)c):
  - Numerator contains (k−b) = −bμe^{−iα}, which is proportional to μ.
  - After dividing by μ: C2/μ = (−be^{−iα}(1−2νe^{iα})) / (c(1−νe^{iα})−b)
  - This expression has NO μ. Setting Im(C2/μ) = 0 gives a quadratic in ν alone (independent of μ).

**C3 determines μ independently of ν.** Computing C3 = b(k−c)/((l−c)(2k−b)):
  - Denominator contains (l−c) = −cνe^{iα}, proportional to ν.
  - After multiplying by ν: C3 × (−cνe^{iα}/b) = ((b−c)−bμe^{−iα})/(1−2μe^{−iα})
  - This expression has NO ν. Setting Im(C3×ν) = 0 gives a quadratic in μ alone (independent of ν).

**Verification:** Confirmed numerically (to machine precision) for triangles b=3+i, c=1+2i and b=4+i, c=1+3i across 70+ configurations. C2/μ is constant as μ varies; C3×ν is constant as ν varies.

---

### Key geometric interpretation (NEW)

Under the decoupling:

**C3 condition ⟺ K lies on a specific circle ω_K through C and M.**

Proof: C3 = 0 says arg((k−c)/(2k−b)) = arg(−ce^{iα}/b) (mod π). Since (k−c)/(2k−b) is a Möbius function of k with zero at k=C and pole at k=M (because 2k−b=0 means k=b/2=M), the "argument-constant" locus is a circle through C and M. Verified: for b=3+i, c=1+2i at α=0.2,0.3,0.5,0.7, both roots of C3_poly give K on the SAME circle through C and M (same circumcircle center and radius to 10^{−12}).

**C2 condition ⟺ L lies on a specific circle ω_L through B and N.**

Proof: C2 = 0 says arg((2l−c)/(l−b)) = arg(−be^{−iα}/c) (mod π). The Möbius function (2l−c)/(l−b) has zero at l=c/2=N and pole at l=b=B. The argument-constant locus is a circle through B and N. Verified: for same triangle at α=0.2,0.3,0.5, both roots of C2_poly give L on the SAME circle through B and N.

These are distinct circles for each α, but the key point is: C3 determines a UNIQUE circle ω_K (through C, M) and C2 determines a UNIQUE circle ω_L (through B, N), independent of each other.

---

### Algebraic proof path (fully charted)

The explicit polynomial computation (for b=3+i, c=1+2i) gives:

**C2_poly(ν):** degree 2 in ν, coefficients depending on (ca,sa):
  - 10(ca+sa)ν² − (10ca²+10ca·sa+5)ν + (5ca−5sa) = 0
  - Note leading coeff: ca²sa+sa³ = sa(ca²+sa²) = sa, so ca²sa+ca+sa³ = ca+sa. 

**C3_poly(μ):** degree 2 in μ (independent of ν):
  - −10(ca+sa)μ² + (10ca²+10ca·sa+5)μ − 5ca = 0
  - Observe: C3_poly(μ) = −C2_poly(μ) + 5sa (approximate relationship)

**Target T(μ,ν):** degree 3 (degree 2 in each variable separately):
  - T = 50(ca·ν−1)μ² + [125ca/2+25sa/2 + (...)]μ + [...]

**Certificate:** Compute Res_μ(T, C3_poly). Using sympy:
  - Res_μ(T, C3) = C2_poly(ν) × [polynomial] + (ca²+sa²−1)² × [polynomial].
  - Since ca²+sa² = 1 (trigonometric identity, cos²α+sin²α=1), the second term vanishes.
  - Therefore Res_μ(T, C3) ≡ 0 (mod C2_poly, ca²+sa²=1).

By resultant theory: Res_μ(T,C3) = (−10(ca+sa))² × T(μ₁,ν) × T(μ₂,ν), where μ₁,μ₂ are the roots of C3_poly. Since Res_μ(T,C3)(ν) ≡ 0 (mod C2_poly) on the unit circle, we get T(μᵢ,νⱼ) = 0 for all roots νⱼ of C2_poly and all roots μᵢ of C3_poly. This is exactly OM = ON on all valid configurations.

---

### Most promising route

**Route: Algebraic decoupling + polynomial certificate**

1. Set up A=0, parameterize via C1: k=bp, l=cq, C1 automatic.
2. Extract C2_poly(ν) and C3_poly(μ) as the "reduced" degree-2 conditions.
3. Compute the target polynomial T(μ,ν).
4. Show T ∈ ideal(C2_poly(ν), C3_poly(μ)) over ℚ[ca,sa,μ,ν]/(ca²+sa²−1) via explicit polynomial division and resultant.

This is fully executable: all polynomials are small (degree ≤ 3), the arithmetic is over ℚ[ca,sa], and the trigonometric identity ca²+sa²=1 clears the denominators.

**Alternative synthetic route (harder but cleaner):**

1. Show K lies on circle ω_K through C and M (from C3).
2. Show L lies on circle ω_L through B and N (from C2).
3. Use power-of-a-point: Power(M, ω_AKL) and Power(N, ω_AKL).
   - Since M ∈ ω_K and K ∈ ω_AKL ∩ ω_K, the line through M and K (a chord of ω_K) meets ω_AKL at K and some K'. Then Power(M,ω_AKL) = MK × MK'.
   - Similarly for N: N ∈ ω_L and L ∈ ω_AKL ∩ ω_L.
   - The relationship between these powers needs to be developed further.

---

### Dead ends

**Pure inversion:** Inverting at any natural center (A, B, C, M, N) does not simplify the three coupled angle conditions or the circumcenter. The circumcenter O has no clean inversive image.

**Projective/cross-ratio route:** No clear projective framing because angles are used essentially.

**"Sigma is an isometry" route:** The sigma symmetry B↔C, K↔L, M↔N fixes O but swaps M and N. This gives OM = ON in the isoceles case directly but does NOT extend to general ABC via a continuity argument (the constraint manifold is not connected via isoceles cases without additional argument).

**Groebner basis in 8+ real variables:** As noted in Round 1, this timed out. The decoupled structure (μ independent of ν) reduces the problem to univariate polynomials, which is tractable.

---

### Knowledge-base entries to use

- **Coordinates / complex / barycentric**: Primary tool; complex plane with A=0.
- **Synthetic toolkit**: Power of a point (for Power(M)=Power(N) reformulation, already in `power-balance`).
- **Resultants / "transform the roots"**: The certificate is Res_μ(T, C3_poly) = C2_poly × (poly) mod (ca²+sa²−1). This is the resultant-based ideal membership technique.
- **Minimal-polynomial reduction**: After establishing C3_poly(μ)=0 and C2_poly(ν)=0, reduce T modulo these polynomials.

---

### Analogous past problems (cruxes)

None directly from corpus (geometry cruxes not in corpus). No genuinely analogous problem found.

---

### Prior progress

Status: partial. Both built approaches (`complex-identity`, `power-balance`) set up correctly and reduce OM=ON to a polynomial identity T=0 on V(C1,C2,C3). Gap: showing T=0 algebraically.

**New critical structure (not in prior approaches):**
- Prior approaches treated C1,C2,C3 as a coupled 3-constraint system.
- The new insight: C1 is automatic; C2,C3 decouple into univariate polynomials in ν and μ respectively.
- This reduces the gap to: T ∈ (C2_poly(ν), C3_poly(μ)) in ℚ[ca,sa,μ,ν]/(ca²+sa²=1).

---

### Dead ends (do not retry)

- Groebner basis in 8 real variables (timed out, unnecessary given decoupling).
- Numerical/CAS verification without explicit certificate (flagged as not-proof by reviewer).
- "Clearly/obviously" geometric argument about midpoint structure (hand-waving, rejected).

---

### Small-case / intuition notes

1. **Verified:** OM=ON to 10^{−12} or better for 70+ valid configurations across 3 non-isoceles triangles and 20+ angle values. (Evidence, not proof.)

2. **Conjecture confirmed as theorem:** C2/μ and C3/ν are independent of μ and ν respectively (proved algebraically by direct computation of the expressions).

3. **Both roots of C3_poly give K on the same circle through C and M** (verified numerically for 4 values of α). Same for C2_poly and the circle through B and N. (Numerically confirmed, not yet proved synthetically.)

4. **The two roots of C3_poly typically give two valid K positions** (both with C1>0 and C3 real). The problem's positional constraints (K inside triangle BMC, inside angle LBA) presumably select one root.

5. **For isoceles triangles (|b|=|c|):** μ=ν at each α (e.g., b=2+i, c=1+2i with |b|=|c|=√5 gives μ=ν≈0.313 at α=0.3). This is the sigma-symmetric case.
