# Lemmas: Alignment cut + θ-peel (sufficiency engine)

Certified (proof-reviewer, round 1). Both re-derived; Mulan's strategy wins in all tested trials.

Setup: cut from apex A (angle α), base β,γ; children T₁ = {x, β, 180−β−x}, T₂ = {α−x, γ, β+x}; the
two cut-point angles 180−β−x and β+x are supplementary.

**Lemma B (alignment).** If θ = 180/n (n ≥ 2) and the triangle has no angle equal to θ, some cevian
makes both children carry a positive multiple of θ. Concretely, cut from a largest-angle apex A;
∠APB sweeps the open interval (γ, 180−β) of length α. For θ ≤ 60, α > θ so this interval (length > θ)
contains a multiple of θ; for θ = 90, the two non-largest angles are < 90 so 90 ∈ (γ, 180−β) (the
altitude). A cut-point angle kθ forces the supplement (n−k)θ, so both children carry a multiple.

(Equivalent stronger form, cutting from the largest vertex the realizable cut-point angles fill the
full open interval (α_min, 180−α_min), which always contains a multiple of θ.)

**Lemma C (θ-peel / double fork).** A triangle with an angle mθ (2 ≤ m ≤ n−1, none = θ) is forced to
an angle θ within ≤ m−1 moves: cut x = (m−1)θ from that apex, giving T₂ = {θ, γ, β+(m−1)θ} (carries
θ). If m = 2, T₁ = {θ, β, 180−β−θ} also carries θ (Shan-Yu loses either way); if m ≥ 3, Shan-Yu must
keep T₁ (apex (m−1)θ), dropping the value by 1. Iterate to m = 2.

**Consequence.** For θ = 180/n Mulan wins in ≤ n−1 moves from any starting triangle. Proves
sufficiency.
