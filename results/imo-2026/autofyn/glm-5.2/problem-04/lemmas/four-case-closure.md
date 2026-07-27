# Lemma: four-case closure of S_θ

**Statement.** Let `θ ∈ (0°,180°)` with `180°/θ ∉ ℤ`. Define
`B_θ = {kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180°}` (strict upper bound; `180° ∉ B_θ`) and
the safe region `S_θ = {(A,B,C) : A,B,C > 0, A+B+C=180°, no angle in B_θ}`.
Then for every `(A,B,C) ∈ S_θ` and every Mulan cut at the `C`-vertex with
parameter `γ ∈ (0,C)`, at least one of the two children
`T₁ = (A, γ, 180°−A−γ)` and `T₂ = (B, C−γ, A+γ)` again lies in `S_θ`.

**Proof.** The two new `P`-angles `p₁ = 180°−A−γ`, `p₂ = A+γ` satisfy
`p₁ + p₂ = 180°` (supplementary — angles at a point on a straight line).
Suppose both children leave `S_θ`. Since `A ∉ B_θ` (parent safe), the bad angle
of `T₁` is `γ` or `p₁`; since `B ∉ B_θ`, the bad angle of `T₂` is `C−γ` or `p₂`.
Four disjoint exhaustive cases:

- **(i)** `γ = k₁θ`, `C−γ = k₂θ` (`k₁,k₂ ≥ 1`). Then `C = (k₁+k₂)θ ∈ B_θ`
  (as `0 < C < 180°`), contradicting `C ∉ B_θ`.
- **(ii)** `γ = k₁θ`, `p₂ = A+γ = k₂θ`. Then `A = (k₂−k₁)θ`; `A > 0 ⇒ k₂ > k₁ ⇒ k₂−k₁ ≥ 1`;
  `A < 180° ⇒ A ∈ B_θ`, contradicting `A ∉ B_θ`.
- **(iii)** `p₁ = k₁θ`, `C−γ = k₂θ`. Then `p₁ − (C−γ) = 180°−A−C = B = (k₁−k₂)θ`;
  `B > 0 ⇒ k₁ > k₂ ⇒ k₁−k₂ ≥ 1`; `B < 180° ⇒ B ∈ B_θ`, contradicting `B ∉ B_θ`.
- **(iv)** `p₁ = k₁θ`, `p₂ = k₂θ`. Then `p₁+p₂ = 180° = (k₁+k₂)θ`, so
  `180°/θ = k₁+k₂ ∈ ℤ`, contradicting the hypothesis.

Each case contradicts; the disjunction is exhaustive; hence at least one child
remains in `S_θ`. ∎

**Verified.** Symbolic check confirms the four linear combinations of `γ`
telescope to `C, A, B, 180°` respectively. Source: `attractor-level-fixpoint` §2
/ `chip-transfer-monovariant` Theorem N / `direct-four-case-interval` §I.1.
