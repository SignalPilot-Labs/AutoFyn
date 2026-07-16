## Goal
Produce a complete, rigorous prose proof for problem **imo-2026-04** (Mulan's triangle game).
- Problem: Shan-Yu/Mulan cut-a-triangle game. Find all real θ (0°<θ<180°) for which Mulan can guarantee a triangle with an angle exactly θ in finitely many steps.
- Type: compute_and_prove, answer_type=characterization. Must (a) state the exact set of θ, (b) prove Mulan wins for those θ, (c) prove she cannot for the rest.
- Metric: proof-reviewer verdict on results/imo-2026-04/. Eval command: dispatch proof-reviewer over results/imo-2026-04/approaches/ + current.md.
- Baseline (round 1): unsolved, no approaches. Target: proof-reviewer APPROVE (Status solved) on >=1 approach.
- Constraints: full rigor per CLAUDE.md — characterization needs BOTH the winning strategy for included theta AND impossibility for excluded theta; no skipped cases; name theorems.

## Goal Updates
- [R1] User: "solve the problem imo-2026-04". Note: problem is difficulty_level=medium, not hard, but user explicitly requested it — overrides the hard-only default.

## Eval History
- R1 baseline: Status=unsolved, no approaches in population.
- R1 result: Status=SOLVED (BREAKTHROUGH). proof-reviewer APPROVE on BOTH built slugs (safe-set-invariant Elo 1516, force-2theta-bisect 1484). Answer: **Mulan wins iff θ=180°/N, integer N≥2**. Reviewer independently re-derived closure lemma + Phase-1 cut, brute-forced closure exhaustiveness, ran full-game sims (win N=2..12, loss θ=72/100/40). closure-lemma.md certified. Rival answer θ∈ℚ·180∩(0,90] refuted at θ=72°.

## Rules
- ALWAYS: characterization answer needs both inclusion (strategy) and exclusion (impossibility) proved (because task=characterization, round 1).
- NOTE: imo-2026-04 SOLVED in R1 — do not re-attempt (because Status=solved, round 1).

## State
Done:
- R1 setup: installed numpy/scipy/sympy, created results/imo-2026-04/ workspace.
- R1: 3 explorers (structure/computation/analogy) → outliner opened 3 rivals → outline-reviewer cut rational-below-90, ranked field, build set {safe-set-invariant, force-2theta-bisect} → both builders solved → proof-reviewer APPROVE both. Problem SOLVED.
Broken:
- (none)
Next:
- Goal achieved. Session complete. If continued, no further work needed on imo-2026-04.
