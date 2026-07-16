## Goal
Solve IMO 2026 P2 (geometry, difficulty 8).

**Problem statement:** Let ABC be a triangle with midpoints M (of AB) and N (of AC). Points K and L are chosen inside triangles BMC and BNC respectively, with K inside angle LBA, L inside angle ACK, and:
- ∠KBA = ∠ACL
- ∠LBK = ∠LNC
- ∠LCK = ∠BMK

Let O be the circumcenter of triangle AKL. Prove that OM = ON.

**Metric:** approach ranking — population health (Elo spread, live vs dead-ended), gaps closing, and ultimately a `solved` status (proof-reviewer APPROVE).
**Eval:** read `results/imo-2026-02/approaches/.ranking.json` and `results/imo-2026-02/current.md` Status.
**Baseline:** unsolved, no approaches.
**Target:** Status = solved with a complete, rigorous proof.

## Goal Updates
(none)

## Eval History
Round 1: Status `partial`. 3 approaches built, all CHANGES REQUESTED.
- **Key Reduction PROVEN:** A' = reflection of A over perp-bisector(MN). If A' on circumcircle(AKL), then OM = ON.
- **Key Lemma UNPROVEN:** The three angle conditions force A' onto circumcircle(AKL).
- Numerical verification: Key Lemma holds to 10^{-14} precision across 10+ configurations.
- All approaches converge to the same gap: proving the Key Lemma from the angle conditions.
- Ranking: all at Elo 1500 (cold start, no head-to-head yet).

Round 3: Status `solved`. BREAKTHROUGH.
- **complex-coords APPROVED (SOLVED):** Complete proof via resultant elimination.
  - C2 and C3 translate to polynomial equations P_2 and P_3.
  - Key Lemma translates to P_KL = 0.
  - Resultant Res(P_2, P_KL, r_t) is divisible by P_3 (Q_3 factor).
  - Therefore P_2 = 0 ∧ P_3 = 0 ⟹ P_KL = 0.
  - Divisibility verified symbolically with exact arithmetic (sympy).
- inversion-collinearity: partial, framework correct, can import Key Lemma.
- directed-angle-concyclic: partial, framework correct, can import Key Lemma.

## Rules
ALWAYS: Define A' as reflection of A over perp-bisector(MN) = intersection of (perp-bisector of BC) with (line through A parallel to BC). This is the canonical definition used by all approaches.
ALWAYS: The Key Lemma is "A' on circumcircle(AKL)". All approaches reduce to this. Focus builders on proving this lemma.
NEVER: Pursue spiral-similarity approach without first verifying the spiral similarity actually exists (Round 1 showed the naive interpretation is false).
ALWAYS: For algebraic approaches, use resultant elimination to prove polynomial implications — this was the successful technique.

## State
**Done:** 
- Round 1: Setup, 3 explorers (structure, computation, analogy), 1 outliner, 1 reviewer.
- 4 approaches created: `directed-angle-concyclic`, `power-of-point`, `complex-coords`, `spiral-similarity` (rejected).
- 3 approaches built: all partial. Key Reduction proven. Key Lemma unproven but numerically verified.
- 1 lemma certified: Power-Midpoint Reduction (written to lemmas/).
- Round 3: 3 explorers (isogonal, direct-om-on, spiral bypass), 1 outliner, 1 reviewer.
- 2 new approaches created: `inversion-collinearity`, `trig-identity-direct`.
- 3 approaches built: `complex-coords` SOLVED, 2 partial.
- **PROBLEM SOLVED via complex-coords approach (resultant elimination).**

**Broken:** (none)

**Next:** 
- End session — problem is solved.
