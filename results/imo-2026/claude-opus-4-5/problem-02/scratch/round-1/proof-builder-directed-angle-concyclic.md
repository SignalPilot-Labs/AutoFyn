# Build Report: directed-angle-concyclic

## Status: partial

## Summary

Built the `directed-angle-concyclic` approach for IMO 2026 P2. The approach aims to prove OM = ON by showing the circumcircle of AKL passes through A' (the reflection of A over the perpendicular bisector of MN).

## What was accomplished

1. **Complete proof of A' characterization:** Established that A' is the intersection of (i) the perpendicular bisector of BC and (ii) the line through A parallel to BC. In optimal coordinates (origin at midpoint of BC, BC on real axis), A' = Im(A) * i is purely imaginary.

2. **Complete proof of the reduction:** If A, K, L, A' are concyclic, then the circumcircle is symmetric under reflection over the perpendicular bisector of MN, so O lies on this line, giving OM = ON.

3. **Concyclicity criterion:** Four points are concyclic iff the inscribed angle equality holds: angle(KAL) = angle(KA'L) (mod pi).

4. **Numerical verification:** The key lemma (A' on circumcircle of AKL) was verified to machine precision (10^-14) across multiple triangle configurations and parameter values.

5. **Cross-ratio formulation:** The concyclicity condition was reformulated as:
   - arg((K-A')/(L-A')) = arg((A-K)/(A-L)) (mod pi)
   - Using A - A' = Re(A) (a real number in the optimal coordinate system)

## Remaining gap

**The main gap:** A proof that the three angle conditions (1), (2), (3) imply the inscribed angle equality angle(KAL) = angle(KA'L).

The conditions create an intricate relationship between K and L through the "cross-pairing" structure (B linked to N in condition 2, C linked to M in condition 3). While the Law of Sines gives formulas for BK and CL in terms of the angles, converting these to a proof of the angle equality at A and A' requires further work.

Specifically, we need to show:
angle(KAB) - angle(KA'B) = angle(BA'L) - angle(BAL)

This geometric interpretation says: the angular shift in viewing direction KB from A to A' equals the angular shift in viewing direction BL from A to A'.

## Approach file

Updated: `/home/agentuser/repo/results/imo-2026-02/approaches/directed-angle-concyclic.md`

## Recommendation for next round

- Try to close the gap by:
  1. Using the Law of Sines cascade more systematically to express all angles at A and A'
  2. Finding an intermediate concyclic quadrilateral that bridges K and L
  3. Alternatively, verify algebraically via complex cross-ratio computation (may overlap with complex-coords approach)
