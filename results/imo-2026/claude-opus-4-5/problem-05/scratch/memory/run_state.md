## Goal
**Problem:** IMO 2026 P5 (imo-2026-05)
Determine all functions $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}} \ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x, y \in \mathbb{R}_{>0}$.

**Metric:** Approach ranking (Elo, live vs dead-ended, gaps closing). Solve = proof-reviewer APPROVE with Status `solved`.
**Eval:** Check `results/imo-2026-05/approaches/.ranking.json` and `results/imo-2026-05/current.md` `## Status`.
**Baseline:** No approaches yet, Status `unsolved`.
**Target:** Status `solved` with rigorous proof.
**Task type:** `compute_and_prove`, `answer_type: characterization`.

## Goal Updates

## Eval History
- Round 1 start: No approaches, Status `unsolved`.
- Round 2: orbit-invariance APPROVE (verified-milestone, Elo 1531). differentiability-squeeze CHANGES REQUESTED (partial, Elo 1500). Status: **solved**.

## Rules

## State
**Done:**
- R1: Set up workspace, read problem, ran 1 explorer (substitution lens).
- R2: Ran 2 more explorers (monotonicity, asymptotic). Outliner generated 3 approaches. Outline-reviewer ranked and emitted build set: orbit-invariance, differentiability-squeeze. Builders filled both proofs. Proof-reviewer: orbit-invariance APPROVE (solved), differentiability-squeeze CHANGES REQUESTED (Step 6 gaps).

**Broken:**

**Next:**
- Problem solved. orbit-invariance proof is complete and verified.
