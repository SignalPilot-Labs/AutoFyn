# Lemma: Device classification + θ>90 impossibility (CERTIFIED complete, round 2)

**Device classification.** For a triangle (A,B,C) with no angle equal to θ, a split of vertex A has
BOTH children containing θ ⟺ θ = 90° or A = 2θ.
*Proof.* θ enters child1={x,B,180−x−B} only via x=θ or 180−x−B=θ (B≠θ); enters child2={A−x,C,x+B}
only via A−x=θ or x+B=θ (C≠θ). The four combinations:
 • x=θ, A−x=θ ⟹ A=2θ.
 • x=θ, x+B=θ ⟹ B=0, impossible.
 • 180−x−B=θ, A−x=θ ⟹ A+B=180 ⟹ C=0, impossible.
 • 180−x−B=θ, x+B=θ ⟹ 180=2θ ⟹ θ=90°.
So only A=2θ or θ=90°; both are realizable. ∎

**θ > 90° is never winnable.** For θ>90: θ=90 is out, and A=2θ>180 is impossible in a triangle.
So no split of a θ-free triangle has both children in W₀ ⟹ W₁=W₀; by the same argument
W_{k+1}=W_k inductively, hence W(θ)=W₀. Shan-Yu picks any θ-free start (e.g. equilateral, since
θ≠60) and survives forever. ∎

Reviewer note: an independent invariant confirms this — from all angles < θ, Mulan can force both
children to have max-angle ≥ θ only if some current vertex angle > θ (needs the cut-vertex angle
> θ); starting all angles < θ, Shan-Yu maintains "all angles < θ" indefinitely.
