# Goal

**Problem:** imo-2026-04 (IMO 2026 P4, "Mulan's Triangle Game"). Combinatorics/game theory, task=compute_and_prove, answer_type=characterization.

**Statement:** Shan-Yu & Mulan play. θ fixed, 0°<θ<180°, known to both. Shan-Yu makes an initial triangle T of his choice. Repeat: if T has an angle = θ exactly, Mulan wins & game stops. Else Mulan picks a point P on the perimeter (not a vertex), cuts from P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one, the other becomes new T. For which θ can Mulan guarantee victory in finitely many steps regardless of Shan-Yu?

**Metric:** proof-reviewer verdict on the population of approaches in results/imo-2026-04/. Target = one approach reaching Status `solved` (APPROVE): a correct characterization of θ + full rigorous proof (both directions).
**Eval:** proof-reviewer verdict + results/imo-2026-04/approaches/.ranking.json Elo + current.md ## Status.
**Baseline:** no approaches yet, Status unsolved.
**Target:** Status solved. -- ACHIEVED round 2.
**Constraints:** rigor rules in CLAUDE.md.

# Goal Updates

- [Round 1] User: solve imo-2026-04.

# Eval History

- Round 1 (start): no approaches, Status unsolved. (Round interrupted — math-explorer force-killed after 900s+ simulation.)
- Round 1 explorers: conjectured Mulan wins iff θ≤90° (θ=90 altitude win, θ>90 non-obtuse defense proven; θ<90 flagged as hard open direction).
- Round 2: BREAKTHROUGH. θ≤90 conjecture REFUTED. Correct answer: **Mulan wins ⟺ θ | 180°** (θ=180/n, n≥2; {90,60,45,36,30,...}). Necessity: invariant "no angle ∈ θℤ" preserved for all Mulan cut-params x via airtight 4-case mod-θ covering; start (θ/2,θ/2,180−θ). Sufficiency: supplementary double-plant (180≡0 mod θ) then forced descent kθ→(k−1)θ to a 2θ vertex, bisect. Both approaches lattice-invariant-180 (Elo 1531) and angle-sum-anchor (Elo 1483) APPROVE/solved; reduce-to-2theta live/unbuilt. current.md Status=solved with Full proof. Confirmed computationally to depth 9 + brute checks. BREAKTHROUGH (unsolved → solved in one round).

# Rules

- ALWAYS: characterization problems need BOTH directions proven — the winning θ set AND impossibility for the rest (CLAUDE.md rigor rule, round 1).
- NEVER: trust an early "θ≤bound" conjecture from numeric intuition without a mod/arithmetic-invariant check — round-1's θ≤90 was numerically plausible but WRONG; the real answer θ|180 came from asking what arithmetic anchor (angle-sum 180) the invariant "no angle ∈ θℤ" needs (round 2).
- ALWAYS: cap subagent Bash/python at <30s, no big simulations — a math-explorer was force-killed at 900s in round 1 (round 1). Anti-stuck guardrails in prompts worked in round 2.
- ALWAYS: for triangle-cutting angle games, the child algebra is child1={x,β,180−x−β}, child2={α−x,γ,x+β}; Mulan owns continuous x + vertex choice, Shan-Yu owns which child to keep (round 2).

# State

## Done
- Round 1: env setup (numpy/scipy/sympy), workspace results/imo-2026-04/ created; two explorer reports (strategy, defense lenses).
- Round 2: forcing explorer (crux, exact BFS negative result); outliner opened 3 rival approaches + refuted θ≤90; outline-reviewer verified θ|180 numerically + ranked; built lattice-invariant-180 + angle-sum-anchor; proof-reviewer APPROVE/solved both; lemma lattice-covering.md certified; current.md Full proof written. PROBLEM SOLVED.

## Broken
- (none)

## Next
- Problem solved. If run continues: could build reduce-to-2theta for a third independent cross-check, or polish current.md Full proof presentation. Otherwise nothing required.
