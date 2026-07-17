# Lemma: Sub-lemma B — F-free split exclusion (CERTIFIED, round 3)

**Statement.** Let θ satisfy 180/θ ∉ ℤ. Let F = { mθ : m ∈ ℤ_{≥1}, mθ < 180 } (finite). Call a
triangle F-free if none of its three angles lies in F. If T = (A,B,C) is F-free, then for EVERY
legal cevian split — every choice of split vertex (angle A, neighbours B,C) and every x ∈ (0,A),
with children child₁ = {x, B, 180−x−B}, child₂ = {A−x, C, x+B} — at least one child is F-free.

**Proof.** Fix the split vertex and x ∈ (0,A). Suppose both children carry an F-angle: child₁ has
p = aθ, child₂ has q = bθ (a,b ∈ ℤ_{≥1}). Since T is F-free, B ∉ F and C ∉ F, so p ∈ {x, 180−x−B}
and q ∈ {A−x, x+B}. Four combinations, each contradictory:
- (1) x=aθ, A−x=bθ ⟹ A=(a+b)θ ∈ F (a+b≥2, A<180) — contradicts T F-free.
- (2) x=aθ, x+B=bθ ⟹ B=(b−a)θ: if b>a then B∈F; if b≤a then B≤0. Both impossible.
- (3) 180−x−B=aθ, A−x=bθ ⟹ C=180−A−B=(a−b)θ: if a>b then C∈F; if a≤b then C≤0. Both impossible.
- (4) 180−x−B=aθ, x+B=bθ (supplementary P-angles) ⟹ (a+b)θ=180 ⟹ 180/θ=a+b∈ℤ — contradicts hyp.
Hence at least one child is F-free. ∎

Holds for all positive integers a,b (no size bound), θ rational or irrational. Case (4) is the crux:
supplementary aθ, bθ are simultaneously multiples of θ iff 180/θ ∈ ℤ — why 180 (not 90) is the
boundary. Reviewer-verified: all four combinations by hand + 201,352 exact-arithmetic adversarial
splits (0 failures), including x = mθ−B, x = 180−mθ−B, and halving.
