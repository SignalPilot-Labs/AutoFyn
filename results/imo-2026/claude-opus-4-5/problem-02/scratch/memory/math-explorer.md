# Math Explorer Role Memory

## Rules

ALWAYS: Verify numerical examples PASS all constraints (positional AND angle), not just satisfy the polynomial equations — wrong branches give false negatives (round 1)

ALWAYS: For geometry angle conditions, determine the SIGNED angle encoding (directed angles via complex arg) before searching numerically — unsigned conditions often lead to wrong solutions that don't satisfy OM=ON (round 1)

ALWAYS: Check positional constraints (K inside BMC, L inside BNC) separately from angle conditions — the solver can find solutions violating the positional constraints (round 1)

NEVER: Trust that Im(complex ratio) = 0 encodes the correct signed angle — always verify the ratio is POSITIVE (not just real), which determines the correct branch (round 1)

ALWAYS: Translate "OM = ON" into 4(B-C)·(O-A) = AB²-AC² (single dot-product identity) before looking for transformations — this pinpoints exactly what the proof must establish. (round 1, imo-2026-02)

ALWAYS: When "OM = ON" involves a circumcenter O of AKL and midpoints M,N of AB,AC: reformulate as pow(M, circumcircle(AKL)) = pow(N, circumcircle(AKL)), which becomes (AB/2)·MA_M = (AC/2)·NA_N where A_M,A_N are second intersections of lines AB,AC with the circumcircle. (round 1, imo-2026-02)

NEVER: Assume the spiral similarity S centered at A (mapping B→C) maps interior point K to interior point L — S maps K to the isogonal reflection of L at C (same unsigned angle but opposite signed angle), not L itself. (round 1, imo-2026-02)
ALWAYS: Verify directed angle sign conventions numerically before encoding angle conditions in complex form — wrong sign gives a non-real expression when it should be real (round 1, imo-2026-02).
ALWAYS: Check KLMN concyclicity numerically before assuming it — for this problem they are NOT concyclic despite small numerical distance differences (round 1, imo-2026-02).
NEVER: Assume condition "∠LBK = ∠LNC" encodes a full spiral similarity — it is only ONE angle of what would be a similarity, and the ratio condition does not follow (round 1, imo-2026-02).
ALWAYS: In A-origin complex encoding, the midpoint conditions N=c/2 and M=b/2 produce factors (2l-c) and (2k-b) in the "∈ ℝ" conditions, which is the algebraic trace of why midpoints appear in the conclusion (round 1, imo-2026-02).
ALWAYS: For coupled angle constraint systems, check if the constraints decouple — C1 automatic, C2 determines ν, C3 determines μ independently. If C2/μ and C3×ν are each parameter-free in the other variable, the constraint variety is a PRODUCT, enabling univariate polynomial certificates (round 2, imo-2026-02).
ALWAYS: When a "ratio ∈ ℝ" condition has a Möbius form f(z)/g(z) with pole at P and zero at Q (both known geometric points), the "Im=0" locus is a circle through P and Q — this gives a purely geometric characterization of each angle condition (round 2, imo-2026-02).
ALWAYS: For algebraic ideal membership T ∈ (f(ν), g(μ)) in ℚ[ca,sa,μ,ν]/(ca²+sa²−1), compute Res_μ(T,g) and check if it factors as f(ν) × [poly] + (ca²+sa²−1) × [poly] — if so, T = 0 on V(f,g) in the geometric setting (round 2, imo-2026-02).
ALWAYS: When two angle conditions C2, C3 produce "Im=0" conditions with the SAME leading polynomial F after parameterization, check if one is a quadratic in ν only and the other in μ only (decoupling). If so, seek the identity F·T = P1·C2_q + P2·C3_q with P1 linear in μ and P2 linear in ν — this is the minimal-degree certificate (round 2, imo-2026-02).
ALWAYS: After finding decoupled quadratics C2_q(ν) and C3_q(μ) with same leading coefficient F, the clean certificate for T ∈ <C2_q, C3_q> has the form F·T = c²(S+μH₂)C2_q - b²(S+νH₃)C3_q where S=Im(bc_bar), H₂=F/2-|b|²sinα, H₃=F/2-|c|²sinα — verify by sequential polynomial division (round 2, imo-2026-02).
