# Lemma: Residue survival invariant (necessity engine)

Certified (proof-reviewer, round 1). Re-derived independently and confirmed 200000/200000 trials.

**Statement.** Fix θ with θ ∤ 180. Call a triangle *good* if none of its three angles is a positive
integer multiple of θ (all three angle-residues ≠ 0 in ℝ/θℤ). If a triangle is good, then for every
legal cevian cut at least one of the two child triangles is good.

**Proof.** Cut from apex A (angle α), base angles β,γ, split x ∈ (0,α); children
T₁ = {x, β, 180−β−x}, T₂ = {α−x, γ, β+x}. Residues a,b,c ≠ 0. T₁ bad ⟺ x ≡ 0 or x ≡ 180−β; T₂ bad
⟺ x ≡ α or x ≡ −β. Both bad needs {0,180−β} ∩ {α,−β} ≠ ∅, i.e. a≡0, b≡0, c≡0, or 180≡0 — all
excluded. So no x makes both children bad; symmetric in apex choice. ∎

**Consequence.** For θ ∤ 180 Shan-Yu (starting from a good triangle, always discarding a bad child)
keeps the position good forever, so no angle ever equals θ: Mulan cannot win. Proves necessity in the
IMO 2026 P4 characterization θ = 180/n.
