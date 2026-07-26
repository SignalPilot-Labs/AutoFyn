## Goal

Prove IMO 2026 Problem 2: Given triangle ABC with midpoints M (of AB) and N (of AC), points K in triangle BMC, L in triangle BNC satisfying K inside angle LBA, L inside angle ACK, angle KBA = angle ACL, angle LBK = angle LNC, angle LCK = angle BMK, and O = circumcenter of triangle AKL, prove OM = ON.

- Metric: proof-reviewer verdict on best approach (solved / partial / unsolved). Target = solved (rigorous proof, no gaps).
- Eval command: read `results/imo-2026-02/current.md` ## Status and `results/imo-2026-02/approaches/.ranking.json`; a proof-reviewer APPROVE on a complete proof = solved.
- Baseline: round 1 — no approaches yet, status unsolved, population empty.
- Constraints: prose Markdown proof; every theorem named and cited in knowledge_base.md; no skipped cases; no hand-waving. answer_type=none, so no numeric verification needed.

## Goal Updates

- [2026-07-25] Task: solve imo-2026-02 (IMO 2026 P2, geometry, difficulty 8, proof_only). Fixed for whole run.

## Eval History

- [Round 1 baseline] status: unsolved. No approaches registered yet. Elo population empty.

## Rules

- ALWAYS: one problem per run — imo-2026-02 only (CLAUDE.md).
- ALWAYS: rank every round via outline-reviewer; no fast-path skip (CLAUDE.md).
- ALWAYS: diversify approaches by framing/route, not just technique — avoid the single-gap trap (CLAUDE.md).
- ALWAYS: each slug targets the whole problem end-to-end, never split one proof across slugs (CLAUDE.md).

## State

### Done
- Round 1: read CLAUDE.md, problem statement, listed hard problems. Installed numpy/scipy/sympy. Set goal + baseline.

### Broken
(none yet)

### Next
- Round 1 cont.: dispatch math-explorers (parallel, different routes) -> proof-outliner -> outline-reviewer -> proof-builders -> proof-reviewer.

## Goal Updates

## Eval History (append)

- [Round 2] BREAKTHROUGH — imo-2026-02 SOLVED. a-star-cyclicity APPROVED by proof-reviewer. Independent re-verification: Gröbner basis of ⟨F1,F2⟩ over Q[p,q,r,P_B,P_C] (grevlex) has 6 elements; Π=num(O_x−(3P_B+P_C)/4) reduces to exact zero remainder (0.12s, exact, rational). K,L coordinate formulas re-derived via sine rule; sign convention (det>0) checked on 8 triangles incl. degenerate B=C; inside hypotheses are pure open inequalities so ideal membership is exactly sufficient. Lemmas 1,2 verified. current.md written with ## Status: solved + full proof. Other build-set approaches: analytic-resultant dead-end (outline only, same crux), miquel-spiral dead-end (numeric gate failed, no transformation exists). dilation-equal-power deferred/unbuilt (sibling). Ranking: a-star 1529 (verified-milestone), analytic 1531 (dead-end), dilation 1484, miquel 1454 (dead-end).

## Rules (append)

## State

### Done (append)
- Round 2: dispatched proof-reviewer to adversarially verify a-star-cyclicity. Verdict APPROVE = solved. Gröbner certificate independently reproduced and confirmed (6-element basis, zero remainder over Q). current.md created.

### Broken
(none)

### Next
- Run complete. Problem imo-2026-02 solved. end_session.
