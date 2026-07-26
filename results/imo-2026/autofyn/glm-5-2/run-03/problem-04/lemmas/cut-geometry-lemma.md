# Cut-geometry lemma (Mulan's triangle game)

**Statement.** In a triangle △ABC with angles (A,B,C) (A+B+C=180°), let P be a point in the interior of side BC, and let the cut from P to the opposite vertex A be made. Write α = ∠BAP ∈ (0,A). Then the two resulting triangles have angle triples

  △ABP = (α, B, 180°−B−α),   △ACP = (A−α, C, B+α).

Conversely, every α ∈ (0,A) is realized by exactly one such point P on the open segment BC.

**Proof.** In △ABP the angle at B is ∠ABP = B (P lies on BC), the angle at A is ∠BAP = α, and the third angle is 180°−B−α. In △ACP the angle at C is ∠ACP = C, the angle at A is ∠CAP = A−α, and the third angle is 180°−C−(A−α) = B+α (using A+B+C=180°). The two angles at P are supplementary: (180°−B−α)+(B+α)=180°. For the converse, as P travels along open segment BC from B to C, the angle ∠BAP is continuous with limits 0 and A; by the IVT every α∈(0,A) is attained. ∎

**Certified by:** proof-reviewer, round 1 (all three approaches proved it from scratch identically). **Source:** approaches/lattice-coset-descent.md §1, approaches/altitude-halving.md §1, approaches/safe-unsafe-pairing.md §0.
