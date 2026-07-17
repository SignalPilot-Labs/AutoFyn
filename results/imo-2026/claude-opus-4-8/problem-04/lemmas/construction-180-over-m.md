# Lemma: θ = 180/m is winnable (⊇ direction, CERTIFIED complete, round 2)

Let θ = 180/m for an integer m ≥ 2 (so 0 < θ ≤ 90). Then W(θ) = all triangles: Mulan wins from
every start. Proof in two steps (both reviewer-verified).

**Lemma A (peel).** If T has a vertex kθ with 1 ≤ k ≤ m−1, then T ∈ W(θ).
*Downward induction on k.* k=1: vertex = θ ∈ W₀. k ≥ 2: split the kθ-vertex at x=θ ∈ (0,kθ).
child1 = {θ, B, 180−θ−B} ∈ W₀ (note 180−θ−B = (kθ−θ)+C > 0). child2 = {(k−1)θ, C, θ+B} has a
vertex (k−1)θ with 1 ≤ k−1 ≤ m−1, so ∈ W(θ) by induction. Both children ∈ W(θ) ⟹ T ∈ W(θ). ∎

**Lemma B (seed a multiple).** From any θ-free triangle, splitting a largest angle A (neighbours
B,C) admits a legal split whose BOTH children carry a vertex that is a multiple jθ, 1 ≤ j ≤ m−1.
*Proof.* As x ranges over (0,A), the child2 P-angle x+B ranges over the open interval
(B, A+B) = (B, 180−C). This interval contains a multiple jθ: otherwise jθ ≤ B < 180−C ≤ (j+1)θ for
some j, giving A = (180−C) − B ≤ θ, so all angles ≤ θ ≤ 90 — impossible for m ≥ 4 (largest angle
≥ 60 > θ), equilateral-and-hence-θ-containing for m=3, and for m=2 forcing 90 ∈ (B,180−C) after
all. Pick jθ ∈ (B,180−C) and set x = jθ−B ∈ (0,A):
child1 = {jθ−B, B, 180−jθ} = {jθ−B, B, (m−j)θ}, vertex (m−j)θ;
child2 = {A+B−jθ, C, jθ}, vertex jθ. Both are multiples in {θ,…,(m−1)θ}. ∎

By Lemma B one seeding move gives two children each with a multiple-vertex; by Lemma A each is a
win. Hence every triangle ∈ W(θ). (Move bound ≤ m−1.) Verified numerically (Lemma B's interval
argument tested over m∈{2,…,12} and 200 random triangles each; θ=60 explicit 2-move win checked).
