# Proof-reviewer report — imo-2026-04 (Mulan's Triangle Game), round 3

Answer under review: **Mulan wins iff θ = 180°/m for some integer m ≥ 2**. The ⊇ construction and
the θ>90 impossibility are pre-certified; the NEW load-bearing claim both approaches make is that
the ⊆ survival direction (0<θ<90, 180/θ∉ℤ) is closed by the boolean **F-free** invariant. I attacked
that claim directly.

## Verification of the crux (Sub-lemma B)

Independently re-derived the cevian geometry against the problem statement: P on a side, cut to the
opposite vertex = cevian from vertex A to interior point of opposite side; children
child₁={x,B,180−x−B}, child₂={A−x,C,x+B}, P-angles supplementary. Matches the certified normal form.
The win condition is "kept triangle has an angle exactly θ", so Mulan forces a win in one move only
when BOTH children win — the AND-OR W(θ) characterization is correct, and "guarantee in finitely
many steps" = start ∈ W(θ) = ⋃_k W_k. All sound.

Sub-lemma B (both files, identical): I checked all four combinations by hand. p∈{x,180−x−B} and
q∈{A−x,x+B} because B,C∉F (parent F-free) — exhaustive 2×2 enumeration.
- (1) forces A=(a+b)θ∈F; (2) forces B=(b−a)θ (∈F if b>a, ≤0 else); (3) forces C=(a−b)θ symmetrically;
  (4) forces (a+b)θ=180 ⟹ 180/θ∈ℤ.
Every leg is a genuine contradiction with F-freeness or 180/θ∉ℤ. No size bound on a,b is used or
needed; holds for θ rational or irrational. Case (4) (supplementary P-angles) is the true crux and
is correctly the exact place where 180 — not 90 — enters.

Independent exact-arithmetic (Fraction) stress test: 201,352 adversarial splits over
θ∈{50,72,40,100/3,220/7,48,65,120,37/7,500/7}, F-free parents, all three split-vertex orientations,
including the collapse cuts x=mθ−B, x=180−mθ−B, x=mθ, x=mθ−C and halving x=A/2 — **0 splits produced
two F-containing children**. Consistent with the hand proof.

Rank induction (Lemma III.2) / explicit strategy Σ: base case F-free⟹∉W₀ (θ∈F) correct; inductive
step correctly uses Sub-lemma B to supply an F-free child ∉W_k, blocking the AND. F-free start: the
isosceles slice excludes only finitely many t against finite F — correct. Both the fixpoint-rank
architecture and the explicit-defender architecture are valid and reach the same conclusion.

No skipped cases, no hand-waving, theorems named, final answer stated and verified at boundary
(θ=90,60 winnable; 72,40,120 not). Rigor rules satisfied.

## Verdicts

### 1. and-or-closure-rank-induction — **APPROVE** (Status: solved)
- Correctness: full. Completeness/rigor: full. Progress: closes the round-2 gap (dropping the
  unnecessary transcendence conjunct) and completes the whole characterization.
- Recorded Status `solved` is **correct**. current.md written with Full proof.

### 2. explicit-ffree-strategy — **APPROVE** (Status: solved)
- Correctness: full. Same engine (Sub-lemma B), genuinely distinct final architecture (explicit
  Shan-Yu defender strategy + induction on move number, no W_k rank). Complete and correct.
- Recorded Status `solved` is **correct**.

Both are complete, rigorous solutions of the same problem via the same crux lemma and two different
survival arguments. The problem is **solved**.

## Certified lemmas (this round)
- `sub-lemma-b-ffree-split.md` — Sub-lemma B, full 4-case proof, verified by hand + 201k splits.
- `ffree-start-exists.md` — F-free start existence (finite F).
- `ffree-rank-induction.md` — F-free ⟹ ∉W(θ), rank induction + explicit-defender corollary.

## Scores (both approaches)
- Correctness 10/10 — every step re-derived and verified.
- Completeness/rigor 10/10 — all cases settled, no gaps.
- Progress 10/10 — completes the full characterization (⊆ crux closed).
