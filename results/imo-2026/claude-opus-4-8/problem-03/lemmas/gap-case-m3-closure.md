# Lemma R4 (Gap-case m = 3 closure — actual-A potential, upper bound)

**Status:** CERTIFIED (proof-reviewer, round 8). Proposed by `geometric-selfsimilar`. Reviewer
re-derived the whole chain from scratch and independently verified: `A(F) = Σ − 2p₁` exactly and
`A(F) < Σ/D_b` with **0 formula-mismatches / 0 bound-violations over 60000** exact-Fraction gap-case
configs (b ∈ {2,3,4}, budget-respecting), and the exact identity `D_b − 2(2^b − 1) = 1` for b = 1..8.

## Statement
Let `X = {p₁ > p₂ > p₃}` be three distinct positive pieces with `|X| = 3 ≤ b + 1` (so `b ≥ 2`),
`Σ = p₁ + p₂ + p₃`, `D_b = 2^{b+1} − 1`, `τ := Σ·2^b/D_b`, satisfying the residual gap hypotheses
`p₂ < τ/2`, `p₃ < τ/2`, and `p₁ ≤ Σ/2`. Then
```
μ(X, b) ≤ A(F) = Σ − 2p₁ < Σ/D_b   (strict).
```

## Proof
**Strategy (one R3 cut).** Xiang Yu cuts `p₁` at interior offset `p₂` into `(p₂, p₁ − p₂)`
(legal: `p₁ > p₂ > 0`; one cut, `1 ≤ b`). The final multiset is
`F = {p₂, p₂} ∪ {p₁ − p₂, p₃}`.

**Value of A(F).** The equal pair `{p₂, p₂}` adds an even amount to `N_F(x)` everywhere, so (Lemma R1
`sum-bound-reductions.md`, Lemma M0 `alt-sum-integral.md`) `A(F) = A({p₁ − p₂, p₃}) = |p₃ − (p₁ − p₂)|`.
From `p₁ ≤ Σ/2` we get `2p₁ ≤ p₁ + p₂ + p₃`, i.e. `p₁ − p₂ ≤ p₃`, so `p₃` is the larger effective piece
and
```
A(F) = p₃ − (p₁ − p₂) = (p₂ + p₃) − p₁ = (Σ − p₁) − p₁ = Σ − 2p₁ ≥ 0.
```

**Bound.** `p₂, p₃ < τ/2 ⟹ p₂ + p₃ < τ ⟹ p₁ = Σ − (p₂ + p₃) > Σ − τ = Σ(2^b − 1)/D_b`
(using `D_b − 2^b = 2^b − 1`). With the exact identity `D_b − 2(2^b − 1) = 1`,
```
A(F) = Σ − 2p₁ < Σ − 2·Σ(2^b − 1)/D_b = Σ·[D_b − 2(2^b − 1)]/D_b = Σ/D_b   (strict).
```
Hence `μ(X, b) ≤ A(F) < Σ/D_b`. ∎

## Corollary R4.1 (gap case closed for all m ≤ 3)
For a gap-case instance (distinct `X`, `p₁ < τ`, `p₂ < τ/2`, so `p₃ ≤ p₂ < τ/2`):
- `m = 2`: `p₁ > Σ/2`, Case A.A (`gap-caseAA-subtract-chain.md`) gives `A = 2p₁ − Σ < Σ/D_b`.
- `m = 3`: `p₁ > Σ/2` ⇒ Case A.A; `p₁ ≤ Σ/2` ⇒ Lemma R4. Exhaustive, disjoint.

**Consequence (n = 2 upper bound rigorous).** At `n = 2`: `Σ = 1`, `m ≤ 3`, `b = 2`. Every branch of the
R1/R2/R3 reducer either terminates at the base `b = 0` (where `μ = A(X) ≤ p₁ ≤ Σ`, (SB) holds) or reaches
a gap case with `m ≤ b + 1 ≤ 3`, closed by Corollary R4.1. So `μ(X,2) ≤ Σ/D_2 = 1/7`, i.e. `val ≤ 4/7`
for every LB config; the n = 2 upper bound is rigorous inside the framework.

## Scope
Closes only `m ≤ 3`. For `m ≥ 4` the potential `A(final) = Σ − 2p₁` does NOT control the target (near-
equal pieces give `Σ − 2p₁ ≈ Σ/2 ≫ Σ/D_b`); the builder refuted every simple deterministic m≥4 strategy
(majority violations). The m ≥ 4 residual gap (bites at n ≥ 3) is genuinely open.
