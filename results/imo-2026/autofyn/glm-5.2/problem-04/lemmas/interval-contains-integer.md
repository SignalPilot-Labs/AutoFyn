# Lemma: an open interval of length > 1 contains an integer

**Statement.** For real `α, β` with `β − α > 1`, the open interval `(α, β)`
contains an integer.

**Proof.** Set `k = ⌊α⌋ + 1`. Then `k` is an integer, `k > α` (since
`⌊α⌋ ≤ α < ⌊α⌋ + 1 = k`), and `k ≤ α + 1 < β` (using `β − α > 1`). Hence
`k ∈ (α, β)`. ∎

(Equivalently: if `α ∉ ℤ`, take `k = ⌈α⌉`; then `k > α` and
`k ≤ α + 1 < β`. If `α ∈ ℤ`, take `k = α + 1 ∈ (α, β)` since `β − α > 1`.)

**Technique.** Pigeonhole / extremal principle (knowledge_base.md).

Source: `direct-four-case-interval` §II.2 / `attractor-level-fixpoint` §3.
