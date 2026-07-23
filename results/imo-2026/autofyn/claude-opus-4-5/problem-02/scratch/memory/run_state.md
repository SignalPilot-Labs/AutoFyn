# Run State — imo-2026-02

## Goal
Prove that OM = ON for the IMO 2026 P2 geometry problem.

**Problem:** Triangle ABC with midpoints M (of AB) and N (of AC). Points K and L inside triangles BMC and BNC respectively, satisfying:
- K lies inside angle LBA
- L lies inside angle ACK
- ∠KBA = ∠ACL
- ∠LBK = ∠LNC
- ∠LCK = ∠BMK

O is the circumcenter of triangle AKL. Prove OM = ON.

**Metric:** approach ranking Elo and solved status
**Eval:** Check `results/imo-2026-02/approaches/.ranking.json` and `results/imo-2026-02/current.md` ## Status
**Baseline:** No approaches (round 1 start)
**Target:** Status = solved with APPROVE verdict

## Goal Updates
(none)

## Eval History
Round 1: 
- complex-identity: CHANGES REQUESTED (overclaimed solved, Step 6 is numerical not rigorous)
- power-balance: CHANGES REQUESTED (honest partial, same algebraic gap)
- Both approaches reduce to same gap: algebraic elimination from C1,C2,C3 to target identity
- Numerical evidence strong: |OM-ON| < 10^-14 for 22 configurations
- Status: partial

Round 2:
- Explorers discovered BREAKTHROUGH: decoupling of C2 and C3 into univariate quadratics C2_q(ν) and C3_q(μ)
- Explicit polynomial certificate: F·T = |c|²(S+μH₂)C2_q − |b|²(S+νH₃)C3_q
- complex-identity: APPROVE (all gaps closed with explicit derivations)
- F≠0 proven via barycentric coordinates (F=0 forces K outside BMC)
- Status: **SOLVED**

## Rules
ALWAYS: When a proof uses "numerical verification" or "CAS computation" as justification, flag it as partial not solved — numerical evidence is not proof.
NEVER: Claim an approach is "solved" when the core derivation is computational verification without explicit algebra.
ALWAYS: Check for "single-gap trap" — if multiple approaches share the same gap, they will fail together.
ALWAYS: Require explicit polynomial identity derivations, not "verified symbolically" claims.

## State
**Done:**
- Round 1: Setup, 3 explorers scouted problem, 4 approaches created, 2 built (complex-identity, power-balance), both CHANGES REQUESTED
- Round 2: Explorers found decoupling breakthrough, proof-builder closed all gaps with explicit algebra, APPROVE verdict, problem SOLVED

**Broken:**
(none — problem solved)

**Next:**
End session — IMO 2026 P2 is solved with rigorous proof.
