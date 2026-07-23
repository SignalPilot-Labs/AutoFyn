# Lemma L2 (exact multiple finishes in ≤ k − 1 cuts) — CERTIFIED (round 1)

**Statement.** Let θ = 180°/n, n ≥ 2 an integer. If the current triangle has an angle equal to kθ exactly, for an integer 1 ≤ k ≤ n − 1, then Mulan wins using at most k − 1 further cuts, no matter how Shan-Yu plays. (Strategy: if an angle equals θ the round-start check has already stopped the game; otherwise attack the vertex with angle kθ using t = θ, giving children containing θ and (k−1)θ respectively; descend.)

**Proof.** Lemma 4.2 of `approaches/circle-group-quotient.md` (strong induction on k; legality 0 < θ < kθ for k ≥ 2 from Lemma L0). Also Lemma 2 of `approaches/residue-divisibility-characterization.md`. Verified by exhaustive-keep game-tree simulation for n = 2..12.

**Note on use.** The descent must be applied to the specific multiple kθ produced at each step (the child C₂ inherits (k−1)θ); descending on an arbitrary — e.g. maximal — multiple present in the triple can cycle.
