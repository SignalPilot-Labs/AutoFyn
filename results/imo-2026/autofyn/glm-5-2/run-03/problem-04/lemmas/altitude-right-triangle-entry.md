# Altitude + round-up entry (Mulan's triangle game)

**Statement.** Suppose θ=180°/n for an integer n≥2. From any triangle state, Mulan can in at most one move ensure the current triangle is right-angled; and then (for n≥3) in at most one further move ensure the current triangle contains a positive multiple of θ. For n=2 the right triangle already contains θ.

**Proof.**

*Step 1 (altitude-to-right-triangle).* If the current triangle already has a 90° angle, skip. Otherwise:
- Acute (all angles <90°): drop the altitude from any vertex V to the opposite side. The foot F lies interior to that side (acute ⟹ every angle <90° ⟹ foot-on-segment criterion holds for every side). The two children are right-angled at F.
- Obtuse at V: drop the altitude from V to the opposite side. The two other angles are <90°, so the foot lies interior to the side (same criterion). The two children are right-angled at F.
Whichever Shan-Yu keeps is a right triangle. (The foot is interior ⟹ P≠vertices, a legal cut.) At most 1 move.

Relabel the right triangle with ∠A=90°, B+C=90°, B≤C so B≤45°.

*Step 2 (n=2 boundary).* θ=90°; the right triangle already contains θ; 0 further moves; total ≤1.

*Step 3 (n≥3 round-up cut).* Choose an integer k with 45°<kθ≤90°.
- Existence: let L=45°/θ; seek integer in (L,2L].
  - L<1 (45°<θ≤60°, n∈{3,4}): 2L∈[1,2); 1∈(L,2L] (L<1≤2L since L≥0.75). k=1.
  - L=1 (θ=45°, n=4): (1,2] contains 2. k=2.
  - L>1 (θ<45°, n≥5): interval length L>1 contains an integer: ⌈L⌉ if L∉Z (⌈L⌉<L+1≤2L), or L+1 if L∈Z (L<L+1<2L since L>1).
- Bounding: kθ≤90°=nθ/2 ⟹ k≤n/2<n, so n−k≥1; also k≥1. Both kθ and (n−k)θ are positive multiples of θ.

*The cut.* Mulan cuts at the right-angle vertex A with parameter α=kθ−B. Legal: α>0 (kθ>45°≥B by B≤45°); α<90° (kθ≤90°, B>0). By the cut-geometry lemma the children are
  △ABP = (kθ−B, B, (n−k)θ),   △ACP = (90°−kθ+B, C, kθ).
Both contain a positive multiple of θ (kθ and (n−k)θ). Positivity: kθ−B=α>0; 90°−kθ+B≥B>0 (kθ≤90°); all other entries positive. Whichever Shan-Yu keeps is marked.

*Conclusion.* For n=2: ≤1 move total. For n≥3: ≤1 (altitude, if needed) + 1 (round-up) ≤ 2 moves to reach a marked state, then the halving/k-descent lemma finishes in ≤n−2 more (multiplier ≤n−1). Total ≤n moves, finite. ∎

**Certified by:** proof-reviewer, round 1. **Source:** approaches/altitude-halving.md §3 (Lemma + Claim).
