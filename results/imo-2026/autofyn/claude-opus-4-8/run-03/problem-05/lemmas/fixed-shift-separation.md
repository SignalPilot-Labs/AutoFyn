# Lemma (fixed points and shifts cannot coexist)

Let f be a solution with d(x)∈{0,b}, b>0. Then not both F={f(x)=x} and G={f(x)=x+b} are nonempty.

**Proof.** For p∈F, q∈G, L(q,p): 2(q²+p²)≥(q+b+p)² ⟺ (p−q)²≥b²+2b(p+q)≥b², so |p−q|≥b (Sep).
Then F is open (for p∈F, δ=min(b,p)/2: (p−δ,p+δ)⊆(0,∞) has no G point, so ⊆F), and G is open
symmetrically. Two nonempty disjoint open sets covering the connected interval (0,∞) is impossible. ∎

Certified round 1 (identity sympy-verified; openness + connectedness re-checked).
