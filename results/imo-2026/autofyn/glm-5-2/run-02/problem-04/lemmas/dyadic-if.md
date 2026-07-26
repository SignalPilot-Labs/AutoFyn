# Lemma: dyadic IF (independent synthetic-geometry certification)

## Statement
For every integer a ≥ 1, set θ = 180°/2^a. Then from any non-degenerate initial triangle T, Mulan has a strategy guaranteeing that θ appears as an angle of T within at most a moves, regardless of Shan-Yu's discards.

## Proof (self-contained, no mod-θ arithmetic)

**Lemma 1 (altitude-foot interior).** In any non-degenerate triangle, the foot of the altitude from a largest-angle vertex lies strictly interior to the opposite side. *Proof:* let A be a largest-angle vertex; if ∠B ≥ 90° then ∠A ≥ ∠B ≥ 90° so ∠A+∠B ≥ 180°, forcing ∠C ≤ 0, contradiction; hence ∠B,∠C < 90°. The foot of the perpendicular from A to line BC lies on segment BC iff both base angles are acute, which holds. ∎

**Corollary (perpendicular anchor).** θ = 90° is forcible in one move from any triangle: pick the altitude foot F from a largest-angle vertex A; cut from F to A. Both children have a 90° angle at F. ✓ (Base case a = 1.)

**Lemma 2 (bisector step).** If T has an angle 2θ at vertex V (0° < θ < 90°), the internal angle bisector from V meets the opposite side at an interior point P; cut from P to V splits 2θ into θ+θ, so both children have angle θ at V. ✓

**Lemma 3 (IH-reuse).** A winning decision tree for target τ (depth ≤ m, leaves τ-bearing, robust to discards) is executable inside the game with any other official target τ′: at each node, if τ′ already appears Mulan has won, else follow the tree's prescribed cut. After ≤ m steps, either τ′ appeared (win) or a τ-bearing leaf is reached. The game mechanics are target-independent; only the stop condition depends on the target. ✓

**Induction on a.** Base a = 1: perpendicular anchor, 1 = a move. Step (a ≥ 2): θ = 180°/2^a ≤ 45° < 90°. Run the IH-strategy for target 2θ = 180°/2^{a−1} (depth ≤ a−1) inside the θ-game via Lemma 3; at each node check for early θ. Reach a 2θ-bearing triangle within ≤ a−1 moves (unless θ already appeared). Then apply Lemma 2 (bisect 2θ), getting θ in both children in one more move. Total ≤ a. ∎

## Where proved
`results/imo-2026-04/approaches/geometric-anchor.md`.

## Status
**Certified** by proof-reviewer, round 1. Statement correct and no stronger than proved (only the dyadic subfamily N = 2^a is claimed). Self-contained: uses only the altitude-foot-interior fact, the angle-bisector definition, and ordinary induction — no modular arithmetic, no create-move, no four-case obstruction. Independent insurance on the IF direction's dyadic core. Does NOT cover non-dyadic IF or any part of the ONLY direction (those require mod-θ machinery, certified separately in `mod-theta-obstruction.md` and the create-move/k-descent of `mod-theta-descent.md`).
