# Build Report: power-of-point approach for IMO 2026 P2

## Summary

**Status: partial**

The power-of-point approach establishes a complete proof framework with all key lemmas proven, but one algebraic identity remains unverified analytically (though confirmed numerically to machine precision).

## What was accomplished

### 1. Proved the key reduction (Claim 1)
OM = ON is equivalent to:
$$\text{pow}(B, \omega) - \text{pow}(C, \omega) = \frac{|AB|^2 - |AC|^2}{2}$$
where ω = circumcircle(AKL).

This reduction uses only the definitions of power of a point and the perpendicular bisector of MN.

### 2. Proved Law of Sines formulas (Claims 2-3)
- BK = (AB/2) · sin(ν)/sin(φ+ν)
- CL = (AC/2) · sin(μ)/sin(φ+μ)

These follow directly from the Law of Sines in triangles BMK and LNC, using the angle conditions.

### 3. Established the algebraic structure (Step 3)
The power identity reduces to:
$$2[(B-C) \times L] \cdot |K|^2 - 2[(B-C) \times K] \cdot |L|^2 = (|B|^2 - |C|^2)(K \times L)$$
using the circumcenter equations O·K = |K|²/2 and O·L = |L|²/2.

### 4. Numerical verification (Claim 4)
The algebraic identity was verified numerically:
- Multiple triangles tested (scalene, with various shapes)
- Multiple φ values (10°, 15°, 20°, 25°, 30°, 35°)
- All verifications show error < 10⁻¹⁰

### 5. Alternative characterization (Claim 5)
The identity is equivalent to A' ∈ circumcircle(AKL), where:
- A' = reflection of A over perpendicular bisector of MN
- A' = intersection of (perpendicular bisector of BC) with (line through A parallel to BC)

This provides a geometric interpretation: the circumcircle of AKL is symmetric under reflection over the perpendicular bisector of MN.

## The remaining gap

**Gap:** Analytic proof that the three angle conditions force the algebraic identity in Claim 4.

The symbolic computation (using sympy) produces a complicated trigonometric expression that does not simplify to zero automatically. The expression involves:
- 6 angle parameters: φ, μ, ν, β (angle of AB), γ (angle of AC), and angle(BAC)
- Products of sin²(φ+μ) and sin²(φ+ν) in the denominator
- Hundreds of terms involving sin/cos of linear combinations of these angles

The complexity arises because:
1. μ and ν are implicitly coupled through conditions (C2) and (C3)
2. K and L depend on both the triangle parameters and the angles μ, ν
3. The final identity must hold for the specific locus of (K, L) satisfying all three conditions

### Possible paths to close the gap

1. **Parametric elimination:** Express μ and ν explicitly in terms of φ and the triangle, then substitute into the identity.

2. **Geometric argument:** Prove A' ∈ circumcircle(AKL) directly using directed angles and the inscribed angle theorem.

3. **Cross-ratio approach:** Show that the cross-ratio (A, K; L, A') is real using the angle conditions.

4. **Trigonometric identity:** Find a clever trigonometric manipulation that shows the numerator of the symbolic expression is identically zero.

## Recommendations for next round

1. **Try the directed-angle-concyclic approach** for A' ∈ circumcircle(AKL), which may give a cleaner synthetic proof.

2. **Attempt parametric elimination:** Use conditions (C2) and (C3) to express ∠LBK and ∠LCK in terms of the other angles, then verify the identity.

3. **Check the crux corpus** for similar power-of-point proofs in geometry, especially those involving midpoints.

## Files modified

- `/home/agentuser/repo/results/imo-2026-02/approaches/power-of-point.md` — complete proof framework with the gap clearly identified
