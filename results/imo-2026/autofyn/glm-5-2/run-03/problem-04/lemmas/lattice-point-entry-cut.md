# Lattice-point entry cut (Mulan's triangle game)

**Statement.** Suppose θ=180°/n for an integer n≥2. From any triangle state with no angle a positive multiple of θ (a "Phase-1" state), Mulan can force BOTH children to contain a positive multiple of θ in a single move.

**Proof.** Relabel the state so A≥B≥C are the three angles in non-increasing order.

*Lemma (lattice-point-in-open-interval).* There exists an integer k with 1≤k≤n−1 such that kθ ∈ (C, A+C).
- n≥3 (θ≤60°): A≥60° (max of three positives summing to 180°). A>θ, else every angle <θ (non-multiple) ⟹ sum <3θ≤180°=sum, contradiction. The interval (C,A+C) has length A>θ. C is not a multiple of θ, so C/θ∉Z; let m=⌈C/θ⌉≥1. Then mθ>C (strict, C non-multiple) and mθ<C+θ<C+A (θ<A), so mθ∈(C,A+C). Finally mθ<A+C<180°=nθ gives m≤n−1. Take k=m.
- n=2 (θ=90°): take k=1; need 90°∈(C,A+C)=90°∈(C,180°−B). C<90° (min; at most one angle ≥90°); B<90° (else A≥B≥90° ⟹ C≤0°). So 90°<A+C. (Covers equilateral (60,60,60).)

*Entry cut.* Set x=A+C−kθ. The inequalities C<kθ<A+C give 0<x<A, a legal cut at vertex A. By the cut-geometry lemma the children are C1=(x,B,A+C−x) and C2=(A−x,C,B+x). Using A+B+C=180°=nθ:
- C1's third angle = A+C−x = kθ ∈ θZ_{>0};
- C2's third angle = B+x = 180°−kθ = (n−k)θ ∈ θZ_{>0} (n−k≥1 since k≤n−1).
Both children are marked. Positivity: x>0, A−x=kθ−C>0, kθ>0, (n−k)θ>0. ∎

**Certified by:** proof-reviewer, round 1. **Source:** approaches/lattice-coset-descent.md §4 (Lemma B + Corollary C).
