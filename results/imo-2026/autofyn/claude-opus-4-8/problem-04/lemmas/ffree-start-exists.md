# Lemma: F-free start exists (CERTIFIED, round 3)

**Statement.** For any θ with 180/θ ∉ ℤ, a legal (nondegenerate) F-free triangle exists, where
F = { mθ : m ∈ ℤ_{≥1}, mθ < 180 }.

**Proof.** Consider T(t) = (t, t, 180−2t), t ∈ (0,90); all angles positive, so legal. T(t) fails
F-freeness only if t ∈ F or 180−2t ∈ F. F is finite, so { t : t ∈ F } is finite and
{ t : 180−2t ∈ F } = { (180−f)/2 : f ∈ F } is finite. Their union is finite; (0,90) is infinite.
Pick t₀ ∈ (0,90) outside the union; T(t₀) is a legal F-free triangle. Works for θ rational or
irrational (only finiteness of F is used). ∎

Reviewer-verified.
