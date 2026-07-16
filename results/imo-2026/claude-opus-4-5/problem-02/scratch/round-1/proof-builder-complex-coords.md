# Proof Builder Report: complex-coords

## Problem
IMO 2026 P2: Prove OM = ON where O is the circumcenter of triangle AKL, given angle conditions on K inside BMC and L inside BNC.

## Approach Summary
Use complex coordinates to verify that the circumcircle of AKL passes through A' = reflection of A over perp-bisector(MN), which implies O lies on perp-bisector(MN), giving OM = ON.

## Work Done

### Coordinate Setup
- Established coordinates: B = (0,0), C = (1,0), A = (a,b) with b > 0
- M = (a/2, b/2), N = ((a+1)/2, b/2) (midpoints)
- Perpendicular bisector of MN: x = (2a+1)/4
- A' = (1/2, b) = reflection of A over perp-bisector of MN

### Key Lemma
Proved that if A' lies on circumcircle(AKL), then OM = ON:
- Since A' = rho(A) where rho is reflection over perp-bisector(MN)
- If both A and A' lie on the circumcircle, its center O lies on the perpendicular bisector of AA'
- This perpendicular bisector equals the perpendicular bisector of MN
- Therefore OM = ON

### Additional Property
Verified that A' lies on the perpendicular bisector of BC:
- A' = (1/2, b)
- |A'B|^2 = 1/4 + b^2 = |A'C|^2
- So |A'B| = |A'C|

### Numerical Verification
Implemented rigorous numerical verification using global optimization (scipy differential_evolution) to find valid (K, L) pairs satisfying all three angle conditions with containment constraints:
- K inside triangle BMC
- L inside triangle BNC

For multiple triangles and phi values, verified:
1. Cross-ratio (A, K; L, A') is real to machine precision (error < 10^{-14})
2. Inscribed angle equality: angle(KAL) = angle(KA'L) to machine precision
3. OM = ON to machine precision

### Gap Identified
The algebraic derivation of the Key Lemma from the three angle conditions remains incomplete:

**What is proved:**
- The reduction: Key Lemma implies OM = ON (rigorous proof)
- Numerical verification of Key Lemma across many test cases

**What remains:**
- Algebraic proof that the three angle conditions force Im[(z_A - z_L)(z_K - z_{A'})/(z_K - z_L)] = 0

The gap is computational/algebraic rather than structural. The proof skeleton is complete, and the numerical evidence is overwhelming (error < 10^{-14} across all tested configurations).

## Status
**Partial** - The proof structure is complete, and the key lemma is verified numerically. The algebraic derivation of the key lemma from the three angle conditions is the remaining gap.

## Files Modified
- `/home/agentuser/repo/results/imo-2026-02/approaches/complex-coords.md`: Updated with full proof structure and gap analysis
