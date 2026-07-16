## Math-explorer role notes

ALWAYS: For geometry problems, set up coordinates FIRST (small numeric example, non-isosceles triangle) and run numerical checks before attempting algebra — it reveals the structure quickly. (imo-2026-02, round 1)

ALWAYS: Check OM=ON type claims by computing the circumcenter x-coordinate in a coordinate system where the perp bisector of MN is vertical. (imo-2026-02, round 1)

ALWAYS: When checking concyclicity, use the actual circumcenter radius equality test numerically — directed angle checks can be misleading. (imo-2026-02, round 1)

NEVER: Assume spiral similarity maps B to N and K to C from a single angle condition alone — one angle condition gives only one angle of a potential similarity, not the full similarity. (imo-2026-02, round 1)

ALWAYS: For "O lies on perp bisector of MN" problems, restate as "power of M = power of N w.r.t. circumcircle" — this opens the power-of-a-point path using the second intersections A', A'' of lines AB, AC with the circumcircle. (imo-2026-02, round 1)

ALWAYS: When all approaches share the same gap and a "bypass" is assigned, first check whether the bypass is mathematically possible — for imo-2026-02, OM=ON is provably equivalent to Key Lemma, so no bypass exists. Report this as a negative result immediately. (imo-2026-02, round 3)

ALWAYS: When conditions C2, C3 involve ∠LBK, ∠LNC, ∠LCK, ∠BMK with cross-pairing (B↔N, C↔M), the explicit trig forms come from law of sines in triangles BCK and BCL: condition C3 gives 2sin(α)sin(γ-φ-ν)sin(φ+ν) = sin(γ)sin(ν)sin(α+2φ+ν), and condition C2 gives the symmetric form with β. The "2" comes from the midpoint BM = AB/2. (imo-2026-02, round 3)

ALWAYS: Verify the midpoint is essential before spending time on general approaches — for imo-2026-02, numerically confirmed that r≠1/2 breaks OM=ON, so any proof must use BM=AB/2, CN=AC/2 crucially. (imo-2026-02, round 3)

NEVER: Claim rho(K) lies on the circumcircle without numerical verification — for imo-2026-02, rho(K) is NOT on circumcircle(AKL): |O − rho(K)| ≈ 2.317 vs R ≈ 0.780. The session summary erroneously claimed it was. (imo-2026-02, round 3)

ALWAYS: For IMO 2026 P2 specifically, the conditions C2 and C3 are NOT equivalent to B,K,L,N concyclic and C,K,L,M concyclic respectively. CR(B,K;L,N) is NOT real. The conditions in complex form are K*(N-L)/(L*(A-1)) ∈ ℝ [C2] and A*(C-K)/((C-L)*(K-M)) ∈ ℝ [C3]. (imo-2026-02, round 3)

ALWAYS: When looking for secondary geometric structure in a problem, check whether the "special" derived points form a cyclic figure. For imo-2026-02: A, A', M, N are ALWAYS concyclic (cyclic isosceles trapezoid, |AM|=|A'N|=|AB|/2, AA'∥MN). (imo-2026-02, round 3)

ALWAYS: When three angle conditions each produce a "product of two complex ratios whose arguments cancel" (arg sum = 0), look for the SYMMETRIC PAIRING STRUCTURE: each condition pairs two special points (vertex ↔ midpoint-analog). For imo-2026-02: C1 pairs B↔C (via A), C2 pairs B↔N, C3 pairs C↔M, Key Lemma pairs A↔A'. The proof should "lift" from {B,C} level to {M,N} level to {A,A'} level. (imo-2026-02, round 3)

ALWAYS: For spiral-similarity and inversion bypasses, verify the center and what points are fixed BEFORE committing to the approach. For imo-2026-02: inversion centered at A' with radius |A'B|=|A'C| fixes B and C (both on the inversion circle), transforming Key Lemma to collinearity A*K*L*. This is a genuine simplification. (imo-2026-02, round 3)

NEVER: In an exhaustive check of concyclic quadruples, include trivial cases where a query point equals one of the defining three points — the check returns 0 error trivially and produces false positives. Always filter out cases where the query point is one of the defining points. (imo-2026-02, round 3)
