# Lemma F: reach a multiple of θ from a generic triangle (n ≥ 3)

**Statement.** Let `n = 180°/θ` be an integer with `n ≥ 3` (so `θ = 180°/n`,
`B_θ = {θ, 2θ, …, (n−1)θ}`). Let `T = (A,B,C)` be a triangle with **no** angle in
`B_θ`. Then Mulan can make a single move such that **both** children carry a
`B_θ`-angle.

**Proof.** Relabel so `C` is a largest angle: `C ≥ A`, `C ≥ B`. Then
`3C ≥ A+B+C = 180°`, so `C ≥ 60°`. Since `n ≥ 3`, `θ = 180°/n ≤ 60°`, hence
`C ≥ θ`. Because `T` is `B_θ`-free and `θ ∈ B_θ`, `C ≠ θ`; therefore `C > θ`,
i.e. `C/θ > 1`.

Consider the open interval
```
I = ( A/θ , (A+C)/θ ),    length  (A+C)/θ − A/θ = C/θ > 1.
```
By the *interval-contains-integer* fact, `I` contains an integer `k` strictly
inside: `A/θ < k < (A+C)/θ`.

Set `γ := kθ − A`. Then:
- `γ > 0` from `k > A/θ`;
- `γ < C` from `k < (A+C)/θ` (i.e. `kθ < A + C`, so `γ = kθ − A < C`).

So `γ ∈ (0, C)`: the cut is non-degenerate. Mulan cuts at vertex `C` with this
`γ`. The two new `P`-angles (one-move transition) are
```
p₂ = A + γ = A + (kθ − A) = kθ,
p₁ = 180° − A − γ = 180° − kθ = (n − k)θ      (using 180° = nθ).
```
**Range of `k`:** `k > A/θ > 0` (as `A > 0`) gives `k ≥ 1`. And
`k < (A+C)/θ = (180° − B)/θ = n − B/θ < n` (as `B > 0`) gives `k ≤ n−1`. So
`k ∈ {1,…,n−1}` and likewise `n−k ∈ {1,…,n−1}`. Hence `p₂ = kθ ∈ B_θ` and
`p₁ = (n−k)θ ∈ B_θ` (both positive multiples of `θ` strictly below `180°`).

Child `T₁ = (A, γ, p₁)` carries `p₁ ∈ B_θ`; child `T₂ = (B, C−γ, p₂)` carries
`p₂ ∈ B_θ`. ∎

**Corollary.** By Lemma R, `T₁ ∈ W_{(n−k)−1} ⊆ W_{n−2}` and
`T₂ ∈ W_{k−1} ⊆ W_{n−2}`, so `T ∈ W_{n−1}`: from any generic (`B_θ`-free)
opening Mulan wins in `≤ 1 + (n−2) = n−1` moves.

**Technique.** Pigeonhole / extremal (knowledge_base.md) for the
integer-in-an-open-interval step.

Source: `direct-four-case-interval` §II.2 / `attractor-level-fixpoint` §3.
