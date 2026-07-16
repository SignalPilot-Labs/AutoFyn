# Lemma: Safe-set Closure (Mulan's triangle game, imo-2026-04)

Status: CERTIFIED (proof-reviewer, round 1) — statement correct, proof sorry-free and no stronger than proved; 4-case split verified exhaustive and independently confirmed by brute-force search over safe triangles. Proved in full in approaches/safe-set-invariant.md Part A.2 and approaches/force-2theta-bisect.md Lemma II.1.

## Setup

Fix a real θ with 0° < θ < 180°. For a triangle T = (A, B, C) (angles > 0, summing to 180°) and a
cut "from vertex A" with split point parameter A₁ ∈ (0, A), the two children are
- Child 1 = (A₁, B, A + C − A₁)  (inherits B; apex A + C − A₁),
- Child 2 = (A − A₁, C, A₁ + B)  (inherits C; apex A₁ + B),
and the apexes are supplementary: (A + C − A₁) + (A₁ + B) = 180°. Cuts from B or C are the same
after permuting the angle labels.

Define the **safe set** S = { triangles no angle of which is a positive integer multiple of θ }.

## Statement

If **180/θ ∉ ℤ** and T = (A, B, C) ∈ S, then for every cut Mulan can make, at least one child of T
lies in S.

## Proof

By symmetry treat a cut from vertex A. Suppose both children are non-safe. Since B, C are angles of
T ∈ S, they are not multiples of θ, so:
- Child 1 non-safe ⟹ A₁ = nθ or A + C − A₁ = nθ, some positive integer n;
- Child 2 non-safe ⟹ A − A₁ = mθ or A₁ + B = mθ, some positive integer m.

Four cases:
1. A₁ = nθ, A − A₁ = mθ ⟹ A = (n + m)θ (parent angle a multiple) — contradicts T ∈ S.
2. A₁ = nθ, A₁ + B = mθ ⟹ B = (m − n)θ; B > 0 ⟹ m > n ⟹ B a positive multiple — contradicts T ∈ S.
3. A + C − A₁ = nθ, A − A₁ = mθ ⟹ C = (n − m)θ; C > 0 ⟹ n > m ⟹ C a positive multiple — contradicts T ∈ S.
4. A + C − A₁ = nθ, A₁ + B = mθ ⟹ 180° = A + B + C = (n + m)θ ⟹ 180/θ = n + m ∈ ℤ — contradicts 180/θ ∉ ℤ.

All four are contradictory, so both children cannot be non-safe; at least one child ∈ S. ∎

## Corollary (Shan-Yu survives)

For 180/θ ∉ ℤ, Shan-Yu starts at T₀ = (θ/2, θ/2, 180° − θ) ∈ S (θ/2 = jθ needs j = 1/2; 180° − θ = jθ
needs 180/θ = j + 1 ∈ ℤ — both impossible) and keeps a safe child every round. A safe triangle has
no angle θ, so Mulan never wins. Hence θ ≠ 180°/N ⟹ Mulan cannot force a win.
