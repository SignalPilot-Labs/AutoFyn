# Lemma: Cevian-split normal form (CERTIFIED, round 2)

A game state is an unordered triple (A,B,C) of positive reals with A+B+C=180 (the angles).
A move: Mulan picks a vertex (angle A) and a real x ∈ (0,A) — the part of A on the B-side of the
cevian to a point P strictly interior to the opposite side. The two children are

    child1 = { x, B, 180−x−B }        (triangle V_A V_B P)
    child2 = { A−x, C, x+B }          (triangle V_A V_C P)

where B,C are the two neighbours of the split vertex. All six angles are positive for x∈(0,A)
(180−x−B = (A−x)+C > 0). The two P-angles 180−x−B and x+B are **supplementary** (sum to 180),
the straight-angle fact at P. Shan-Yu keeps one child; Mulan wins the instant some angle = θ.

**AND–OR winning set.** W₀={T: θ∈T}; W_{k+1}=W_k ∪ {T: ∃ split with BOTH children ∈ W_k};
W(θ)=⋃_k W_k. Mulan forces a win from T ⟺ T∈W(θ). Since Shan-Yu also picks the start, **Mulan
wins the game for θ ⟺ W(θ)=all triangles**; equivalently Shan-Yu survives ⟺ some θ-free triangle
∉ W(θ).

Verified by the reviewer (angle bookkeeping and supplementarity checked directly).
