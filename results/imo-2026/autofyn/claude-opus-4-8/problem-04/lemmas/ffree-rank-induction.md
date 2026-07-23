# Lemma: F-free rank induction — F-free ⟹ outside W(θ) (CERTIFIED, round 3)

**Statement.** For θ with 180/θ ∉ ℤ, no F-free triangle lies in any W_k, hence none lies in
W(θ) = ⋃_k W_k. (W₀ = {angle=θ}; W_{k+1} = W_k ∪ {∃ split with both children in W_k}.)

**Proof.** Strong induction on k. Base k=0: F-free ⟹ no angle equals θ = 1·θ ∈ F ⟹ ∉ W₀. Step:
assume the claim for all indices ≤ k. Let T be F-free. If T ∈ W_{k+1}, then either T ∈ W_k
(excluded by hypothesis) or some legal split of T has both children in W_k. But by Sub-lemma B
(`sub-lemma-b-ffree-split`) every legal split of the F-free T has an F-free child, which ∉ W_k by
hypothesis. So not both children are in W_k. Hence T ∉ W_{k+1}. ∎

**Corollary (explicit defender).** Equivalently, from an F-free start Shan-Yu keeps an F-free child
each move (one exists by Sub-lemma B); the position stays F-free forever (induction on move number),
so no angle ever equals θ. Shan-Yu survives ⟹ Mulan cannot force a win when 180/θ ∉ ℤ.

Reviewer-verified. Both live approaches (rank induction; explicit strategy Σ) instantiate this.
