# outline-reviewer — round 2 (imo-2026-05)

Problem is SOLVED (orbit-close-encounter APPROVE, round 1). No new approaches opened; no outliner output this round. Only change: `gm-lipschitz-partition` Part B cover-iteration gap closed by swapping rightward-only iteration for the maximal-connected-component boundary-push argument (same `(†)` zero-region radius `2√(cs)`); Part A (Fact 5 + close-encounter) unchanged. `asymptotic-vanishing-coefficient` stays RETHINK/dead — all three closures of the `(x−y−c)²` swallowing obstruction are tautologies; not registered, not built.

## Per-approach verdicts

- **orbit-close-encounter** — APPROVE (terminal). Solved, verified-milestone round 1; round-2 cosmetic corrections (QM²−AM² gap factor, `(⋆⋆)` justification) are non-load-bearing. Still the certified complete proof. Elo 1530.5.
- **gm-lipschitz-partition** — CHANGES REQUESTED → now a complete peer route pending re-review. Part B maximal-component argument is structurally identical to orbit's Step 4 (same `(†)`, same boundary-push, same `α→0, β→∞`), so the gap is genuinely closed; Part A remains genuinely different (Fact 5 self-referential `g`-bound as engine vs. raw `(⋆)` contradiction). Distinct framing on (A), shared (B) — acceptable for a second complete proof. Re-review will confirm. Elo 1469.5.
- **asymptotic-vanishing-coefficient** — RETHINK (dead, unregistered). Not ranked.

## Ranking
Single pairwise comparison: orbit-close-encounter (verified-milestone, solved) beats gm-lipschitz-partition (partial last outcome, now complete pending re-review). Both `stale` flags cleared. Field: orbit 1530.5 > gm-lipschitz 1469.5. (asymptotic not in pool — RETHINK, never registered.)

## Note on diversity
Both surviving approaches now share the maximal-component Part B argument (gm-lipschitz adopted it from orbit). Genuine diversity lives only in Part A (Fact 5 vs. raw `(⋆)`). Since the problem is solved, this convergence is acceptable; if gm-lipschitz's re-review returns CHANGES REQUESTED, the builder should re-examine Part A's Fact 5 engine independence, not re-derive Part B.

build set:
