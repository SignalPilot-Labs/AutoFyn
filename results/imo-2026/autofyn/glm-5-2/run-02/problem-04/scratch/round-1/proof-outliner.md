## imo-2026-04

mod-theta-descent: new
Target: Characterize all θ ∈ (0°,180°) with Mulan guaranteed finite victory — prove the answer is exactly θ = 180°/N for integers N ≥ 2 (unit fractions of 180°), both directions.
Technique: Invariant/monovariant + modular arithmetic over ℝ/θℤ + induction on k. Direct two-direction proof: Shan-Yu's mod-θ "no θ-multiple" invariant (ONLY direction, four-case residue chase ending in r ≡ 0); Mulan's create-a-multiple move (γ = θ − (Y mod θ) at the max-angle vertex) feeding a k-descent (split kθ with γ = θ, k ↦ k−1) for the IF direction.
Skeleton:
  1. Exact angle transform: splitting angle X into γ (near Y) + (X−γ) (near Z) gives child1 = (γ, Y, 180−Y−γ), child2 = (X−γ, Z, Y+γ); the two P-angles sum to 180° (supplementary pair). — by direct angle chase
  2. IF / Step 1 (create a θ-multiple): θ = 180/N, no angle is a θ-multiple; pick X = max ≥ 60°, adjacent Y; set γ = θ − (Y mod θ) ∈ (0,θ). Then Y+γ ≡ 0 and 180−Y−γ ≡ 180 ≡ 0 (mod θ) (Nθ = 180); both children carry a θ-multiple at P. — by modular arithmetic
  3. IF / Step 2 (k-descent): angle = kθ, k ≥ 2; split it with γ = θ ⇒ child1 has θ (Shan-Yu avoids), child2 has (k−1)θ. Monovariant k ↦ k−1; terminates at k = 1 (angle = θ) in ≤ N−2 steps. — by induction on k
  4. IF / validity: γ ∈ (0,X) (X ≥ 60 ≥ θ > γ, with θ = 90 handled by Z < 90); child non-degeneracy via Y < 180−θ. — by angle-size casework
  5. ONLY / invariant: r := 180 mod θ ∈ (0,θ); maintain "no angle ≡ 0 mod θ." Four-case chase (γ≡0∧X−γ≡0; γ≡0∧Y+γ≡0; 180−Y−γ≡0∧X−γ≡0; 180−Y−γ≡0∧Y+γ≡0) yields X≡0, Y≡0, Z≡0, or r≡0 — all contradictions. So no move makes both children θ-multiple; Shan-Yu keeps a θ-multiple-free child. — by modular casework
  6. ONLY / initial triangle: a θ-multiple-free triangle exists whenever r ≠ 0 (forbidden angle-values form a countable subset of the 2-simplex). — by generic choice
Key lemmas (claim + one-line mechanism):
  - Create-multiple: Y+γ ≡ 0 (mod θ) by γ = θ − (Y mod θ), and 180−Y−γ ≡ 0 because Nθ = 180.
  - k-descent: splitting kθ at γ = θ literally produces θ and (k−1)θ at the split vertex; k strictly decreases.
  - Four-case obstruction: each of the four ways both children could acquire a 0-mod-θ coordinate reduces to "an existing coordinate is 0" or "r = 0," both excluded.
  - Boundary: r = 0 ⇔ θ | 180 ⇔ θ = 180/N (unit fraction) — this is the exact answer boundary.
Open gaps: (1) write the IF validity inequalities as one clean lemma (θ ≤ 60 vs θ = 90 casework); (2) initial-triangle existence for irrational θ (countable-forbidden-set argument, NOT a Kronecker density obstruction — clarify); (3) confirm four-case exhaustiveness over the three angle-slots.
Cases to cover: θ > 90° (ONLY, r ∈ (0,θ)); θ = 90° (IF, N=2 sub-case); 60° ≤ θ < 90° only θ = 90 wins; θ < 60° unit fractions win, the rest lose; irrational θ loses.
Watch out for: the defense explorer's "3-smooth only" conjecture is WRONG (θ = 36° = 180/5 wins — numerically verified); the explorer's "group ⊆ ℤ/p" invariant FAILS (Mulan picks γ outside) — the mod-θ invariant here is the correct weaker one tolerating arbitrary γ; integer-grid evidence is consistent with (not contradicting) the unit-fraction answer.

fixpoint-attractor: new
Target: Same full characterization via the AND-OR game fixpoint.
Technique: Co-induction / greatest-fixpoint of the AND-OR game operator. W = least fixpoint of F(S) = {has θ} ∪ {∃ move both children ∈ S}; L = greatest fixpoint of G(Q) = {no θ ∧ ∀ moves ∃ child ∈ Q}.
Skeleton:
  1. Define W, L as least/greatest fixpoints; T ∈ W ⇔ finite forced win. — by AND-OR game semantics
  2. IF (θ = 180/N): show W = 𝒯. Base {has θ} ⊆ W; induct on k: {has kθ, k ≥ 2} ⊆ W via split-at-θ (child1 ∈ W base, child2 ∈ W by IH); {no θ-multiple} ⊆ W via create-move (both children ∈ M ⊆ W). — by fixpoint induction
  3. ONLY (θ not unit fraction): C = {no θ-multiple} is G-closed (four-case obstruction ⇒ every move leaves a child in C); so C ⊆ L, W ⊊ 𝒯. — by coinduction
Key lemmas:
  - W-fixpoint identity: W = 𝒯 when r = 0 — create-move sends θ-multiple-free triples into two θ-multiple children.
  - C-greatest-fixpoint: C is G-closed when r ≠ 0 — four-case chase.
Open gaps: justify fixpoint well-foundedness (k-induction finite in {1,…,N−1}); extract Shan-Yu's explicit choice function from coinductive membership. Shares the create-move + four-case wall with mod-theta-descent.
Cases to cover: same.
Watch out for: SAME core proof as mod-theta-descent, re-skinned in fixpoint language — diversity insurance, shared wall.

torsion-subgroup: new
Target: Same full characterization, framed on the additive group G = ℝ/θℤ.
Technique: Modular arithmetic / subgroup structure on ℝ/θℤ. The angle-triple (ā, b̄, c̄) ∈ G³ satisfies ā+b̄+c̄ = r̄ := 180 mod θ; Mulan wins ⇔ she forces a coordinate to 0̄.
Skeleton:
  1. Set G = ℝ/θℤ, r̄ = ρ(180). r̄ = 0 ⇔ θ unit fraction. Triangle → (ā,b̄,c̄) with sum r̄. — by definition
  2. IF (r̄ = 0): choose γ̄ = −ȳ; child1 P-angle ↦ r̄−ȳ−γ̄ = 0̄, child2 P-angle ↦ ȳ+γ̄ = 0̄. Both children 0̄-free→0-coordinate. k-descent at representative level closes to θ. — by group algebra + descent
  3. ONLY (r̄ ≠ 0): invariant "no coordinate = 0̄." Four combinations of 0̄-acquisition yield x̄=0̄, ȳ=0̄, z̄=0̄, or r̄=0̄ — all excluded. — by coset-avoidance
Key lemmas:
  - Torsion boundary: r̄ = 0 ⇔ θ = 180/N.
  - Arbitrary-γ robustness: the 0̄-free invariant constrains the COORDINATES, not γ̄ — exposing why the explorer's "group ⊆ ℤ/p" (which constrained γ̄) was wrong.
Open gaps: lift "0̄ in G" to "angle = θ exactly" via the k-descent; create-move validity; initial-triangle existence (countable union of codim-1 loci). Shares the wall with mod-theta-descent.
Cases to cover: same.
Watch out for: same core proof re-skinned; makes the explorer's invariant-flaw transparent; do NOT import "3-smooth only."

geometric-anchor: new
Target: Same full characterization, but via synthetic geometry (perpendiculars + bisectors) for the IF direction.
Technique: Altitude (perpendicular anchor) + angle bisector + induction on the dyadic exponent a. Independently certifies θ = 180°/2^a; extends to general N by importing the mod-θ create-move for odd factors.
Skeleton:
  1. Perpendicular anchor: every triangle has an altitude with foot interior to the opposite side (acute: all three; right: the legs; obtuse: from the obtuse vertex). Splitting there gives 90° in both children. — by altitude classification
  2. Bisector step: angle 2θ at V ⟹ bisect (γ = θ) ⟹ θ in both children. — by bisection
  3. Dyadic induction: θ = 180/2^a wins in ≤ a moves — IH forces 2θ = 180/2^{a−1} to appear, then bisect. — by induction on a
  4. General N (odd factor): import create-move + k-descent from mod-theta-descent (geometric framing breaks down here). — by deferral
  5. ONLY direction: import mod-θ four-case obstruction. — by deferral
Key lemmas:
  - Altitude-foot interior: classification by acute/right/obtuse.
  - Dyadic induction: force 2θ appears (IH for target 2θ) then bisect.
Open gaps: altitude-foot classification (only non-trivial geometric step); IH-reuse statement; general N and ONLY entirely deferred. Does NOT stand alone for the full characterization — only independently certifies dyadic θ.
Cases to cover: dyadic N handled here; non-dyadic N and ONLY deferred.
Watch out for: only independently certifies θ = 180/2^a; shared wall on create-move (non-dyadic) and four-case (ONLY); retrieval explorer confirmed bisector chain alone is insufficient.

---

Field of slugs opened (4): mod-theta-descent, fixpoint-attractor, torsion-subgroup, geometric-anchor.
Copy request: NONE this round — the create-move + four-case facts are a single shared wall; copying an approach into two gap-fills would just double the same wall (the single-gap trap the orchestrator warns about). Wait until the wall is certified before duplicating.
Nominees to advance: **mod-theta-descent** is the primary — its two directions are numerically verified (create-move for N ∈ {2,…,99} incl. non-integer-degree N=7,11,13,17,19,23,99; obstruction for non-unit-fractions θ ∈ {72,100,50,7,13,40,135}) and the skeleton is essentially complete; the builder should write the validity-inequality lemma and the initial-triangle existence rigorously, then the reviewer can certify. The other three are diversity insurance (different framings of the same core) — advance them only if mod-theta-descent stalls.
