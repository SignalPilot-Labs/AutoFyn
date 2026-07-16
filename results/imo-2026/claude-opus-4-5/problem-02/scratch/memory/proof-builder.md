# Proof Builder Rules

ALWAYS: When using scipy.optimize.differential_evolution, set workers=1 (not -1) to avoid multiprocessing issues in stdin scripts (because multiprocessing fails on <stdin>, round 1)

ALWAYS: For geometry problems with "inside triangle" constraints, explicitly check containment using signed area - solutions without this check often find spurious solutions that satisfy angle conditions but violate containment (because numerical solvers find multiple local minima, round 1)

ALWAYS: When verifying inscribed angle / concyclicity conditions numerically, use cross-ratio imaginary part as the check - it's more robust than comparing angles directly (because arccos precision degrades near 0 and pi, round 1)

ALWAYS: Place coordinates at midpoint of BC with BC on the real axis when working on geometry problems with perpendicular bisectors and midpoints - it dramatically simplifies calculations (because A' = Im(A)*i becomes purely imaginary), round 1

NEVER: Trust a single numerical optimization result without multiple starting points - degenerate solutions (like K=M, L=N in IMO 2026 P2) can satisfy conditions trivially, round 1

ALWAYS: For power-of-point proofs, check if the target identity is equivalent to a concyclicity condition (A' on circumcircle) - this often gives a cleaner synthetic path than direct algebraic verification (because concyclicity can be verified via inscribed angles), round 1

ALWAYS: When parameterizing points on rays, verify the direction conventions numerically before doing symbolic computation - rotating "toward interior" depends on the specific triangle orientation (because sympy substitution errors from wrong angles waste significant time), round 1

ALWAYS: When using numerical optimization for geometry problems with "inside triangle" constraints, use grid search first to find valid starting points before local optimization - differential_evolution can find mathematically valid but geometrically invalid solutions that satisfy angle conditions but violate containment (round 3)

ALWAYS: When the Key Lemma of a geometry problem is numerically verified to machine precision but algebraically hard to prove, use RESULTANT ELIMINATION: if C2 and C3 are polynomial conditions and KL is the target, compute Res(C2, KL, r_t) and check if it's divisible by C3. This proves C2=0 AND C3=0 => KL=0 algebraically. Successfully used to close IMO 2026 P2 (round 3)

ALWAYS: For IMO 2026 P2, the inversion-collinearity approach transforms the Key Lemma (A' on circumcircle AKL) to collinearity (A*, K*, L*) - the gap is proving collinearity from angle conditions. This is numerically verified but needs algebraic derivation via Menelaus or trig identities (round 3)

ALWAYS: When inversion fixes two vertices (B, C on inversion circle), angles at those vertices are preserved in MAGNITUDE but not necessarily orientation - points that cross to opposite side of inversion circle have reversed orientation (round 3)

ALWAYS: When A - A' is purely real (horizontal translation), the cross-ratio (A-K)(A'-L)/((A-L)(A'-K)) being real reduces to an "angular shift equality" - both u = A'-K and v = A'-L must rotate by the same angle when adding d = A-A'. This gives an explicit algebraic identity that is cleaner than the full cross-ratio expansion (round 3)

ALWAYS: In IMO 2026 P2, condition C1 constrains K, L to specific rays (2 DOF), and C2+C3 provide 2 equations determining unique positions. The Key Lemma then follows as a consequence on this determined variety - it's NOT in the ideal <C2, C3> globally, but holds specifically when all three C1, C2, C3 are satisfied (round 3)
