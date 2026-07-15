## Goal
Solve `imo-2026-02` with a complete, rigorous prose proof certified by the proof-reviewer. Metric: `results/imo-2026-02/current.md` has `## Status` = `solved`, with every built approach independently ranked and reviewed. Eval command: `python - <<'PY'
from pathlib import Path
p=Path('results/imo-2026-02')
cur=p/'current.md'
rank=p/'approaches/.ranking.json'
print(cur.read_text() if cur.exists() else 'STATUS: workspace absent (unsolved)')
print(rank.read_text() if rank.exists() else 'RANKING: no approaches registered')
PY`. Baseline (2026-07-15, round 1): workspace absent; status unsolved; no approaches registered. Target: reviewer verdict APPROVE and status solved. Constraints: attack only this hard problem; consult `knowledge_base.md` and the documented crux corpus; maintain rival whole-problem approaches; use the mandated explorer → outliner → outline-reviewer → builder → proof-reviewer flow; commit only `results/imo-2026-02/` artifacts.

## Goal Updates

## Eval History
- Round 1 baseline: `STATUS: workspace absent (unsolved)`; `RANKING: no approaches registered`.
- Round 1 IMPROVED — Goal Progress (raw): current status `partial`. Rankings: `oriented-determinant-elimination` Elo `1516.0`, expanded `1`, stale `true`, last outcome `advanced`; `antipode-quarter-turn` Elo `1500.736306793522`, expanded `1`, stale `true`, last outcome `advanced`; `sine-product-antipode` Elo `1500.0338330211207`, expanded `1`, stale `true`, last outcome `partial`; `inverted-circle-intercepts` Elo `1483.2298601853572`, expanded `0`, stale `false`, no outcome. Verdicts: all three built slugs CHANGES REQUESTED / partial. Certified progress: `OM=ON iff XB=XC` for the antipode `X` of `A`, plus a correct Cartesian/Cramer determinant reduction.
- Round 2 BREAKTHROUGH — Goal Progress (raw): Status: `solved`. Reviewer verdict: `APPROVE` for `oriented-determinant-elimination`. Current ranker metadata, intentionally unchanged to avoid double-counting the correction review: `oriented-determinant-elimination` Elo `1531.2975328274754`, expanded `2`, stale `true`, last outcome `partial` (round 2), with the pre-repair residual-error note; `antipode-quarter-turn` Elo `1502.110506192537`, expanded `1`, stale `false`, last outcome `advanced` (round 1); `sine-product-antipode` Elo `1499.3560108898125`, expanded `1`, stale `false`, last outcome `partial` (round 1); `inverted-circle-intercepts` Elo `1467.235950090175`, expanded `0`, stale `false`, no recorded outcome. The goal is met: `results/imo-2026-02/current.md` has a complete proof of `OM=ON` and Status `solved`. The only metadata mismatch is the deliberately unmodified, already-counted ranker outcome.

## Rules
- ALWAYS: Treat each approach slug as a complete end-to-end attempt at the original claim, never as one fragment of a split proof (because shared-line collapse defeats population diversity, round 1).
- ALWAYS: Consult both `knowledge_base.md` and the crux corpus documentation/corpus before advancing an approach (because project instructions require both retrieval resources, round 1).
- NEVER: Hand-edit `approaches/.ranking.json`; use ranker tools only (because the sidecar is tool-owned, round 1).
- ALWAYS: Run the outline-reviewer and proof-reviewer in every round (because ranking and adversarial verification are mandatory, round 1).
- ALWAYS: Require an exact displayed trigonometric/determinant or sine-product identity and coefficient-by-coefficient cancellation before treating a promised telescoping as proof (because all three round-1 candidates stalled at unsupported cancellation, round 1).
- NEVER: Infer `B,C,K,L` cyclic or use consequences of that claim without independent verification (because a generic admissible numerical configuration falsified it, round 1).
- ALWAYS: Write ray-order/interiority sign derivations and prove every cleared sine denominator nonzero (because these were asserted but absent from all round-1 analytic attempts, round 1).
- ALWAYS: Independently re-expand every displayed residual coefficient before certification (because the first round-2 coefficient table differed from the true residual by `2hqr x`, round 2).
- NEVER: Double-record a ranker outcome for an in-round repair of the same built slug when the tool has no idempotent correction operation (because doing so would inflate `expanded`, round 2).

## State
### Done
- Round 1 setup completed; installed numpy, scipy, and sympy.
- Three independent lenses scouted structural, analytic/computational, and transformational routes while consulting required resources.
- Registered and ranked four rival whole-problem approaches.
- Built and independently reviewed exactly the selected three approaches.
- Certified the antipode reduction: if `X` is the antipode of `A` on `(AKL)`, the factor-2 homothety about `A` maps `(O,M,N)` to `(X,B,C)`, hence `OM=ON iff XB=XC`; Thales gives `XK ⟂ AK`, `XL ⟂ AL`.
- Certified a coordinate reduction of the goal to `2(|K|^2[C-B,L]+|L|^2[K,C-B])=(q^2-1)[K,L]`.

- Round 2 sent three distinct lenses against the determinant gap, bypass routes, and synthetic antipode reconstruction; the ranking gate selected only `oriented-determinant-elimination`.
- The initial build exposed an incorrect sign and residual table; an in-round repair recomputed them and supplied a finite tangent-half-angle coefficient certificate.
- The proof-reviewer independently reproduced the corrected sign, all five determinant expansions, all three residual coefficients, and the decisive three-coefficient factorization.
- Certified reusable lemmas `corrected-directed-incidence.md` and `corrected-determinant-residual.md`.
- Reviewer updated `current.md` to `solved` with a complete proof and issued APPROVE.

### Broken
- No mathematical gap remains in the certified proof.
- Ranking metadata still records the pre-repair `partial` result for `oriented-determinant-elimination`; it was intentionally not double-recorded because the ranker has no correction/idempotency operation.

### Next
- Goal achieved; end the session after committing the solved workspace.
