# torsion-subgroup — ℝ/θℤ framing of the mod-θ invariant

## Status
partial

## Approaches tried
- Subgroup / torsion framing on the circle group ℝ/θℤ (this file) — the defense explorer's angle-group lens done RIGHT: the invariant is "no angle maps to 0 in ℝ/θℤ," which tolerates arbitrary γ (unlike the broken "group ⊆ ℤ/p" attempt).

## Current best
A clean group-theoretic statement: Mulan wins ⇔ 180° is torsion (zero) in ℝ/θℤ, i.e. θ | 180° (θ is a unit fraction). The defense invariant is "no angle ≡ 0 (mod θ)," a coset-avoidance condition.

## Target (whole problem)
Same full characterization: θ = 180°/N, N ∈ ℤ_{≥2}.

## Technique
Modular arithmetic / subgroup structure on the additive group ℝ/θℤ (NT KB: modular arithmetic, CRT). The angle triple lives in (ℝ/θℤ)³ with the relation A+B+C ≡ 180 (mod θ); Mulan wins iff she can force some coordinate to 0.

## Skeleton

Work in the additive group G = ℝ/θℤ. Let ρ: ℝ → G be the reduction. Let r̄ = ρ(180°) = 180 mod θ ∈ G.
- If θ is a unit fraction (θ = 180/N), then r̄ = 0 (180 ≡ 0 mod θ).
- If θ is not a unit fraction, r̄ ≠ 0 in G.

A triangle (A,B,C) maps to (ā, b̄, c̄) ∈ G³ with **ā + b̄ + c̄ = r̄** (the triangle relation mod θ). Mulan "wins" if she forces some coordinate to 0̄ in G (an angle ≡ 0 mod θ — the θ-multiple condition; θ itself is a special case, handled by the descent).

### IF direction (r̄ = 0, i.e. θ = 180/N)

Relation becomes ā + b̄ + c̄ = 0. The **create-move** in G: Mulan picks vertex with residue x̄ (= ā), adjacent ȳ (= b̄), chooses γ̄ = −ȳ (i.e. γ = θ − (Y mod θ) in representatives). Then:
- child1's P-angle: 180 − Y − γ ↦ r̄ − ȳ − γ̄ = 0 − ȳ − (−ȳ) = 0̄. So child1 has a 0-coordinate at P.
- child2's P-angle: Y + γ ↦ ȳ + γ̄ = ȳ + (−ȳ) = 0̄. So child2 has a 0-coordinate at P.
Both children acquire a 0-coordinate. Whichever survives has a θ-multiple. The k-descent then reduces kθ → (k−1)θ exactly as in mod-theta-descent (in G: 0̄ stays 0̄; the integer k descends because we split kθ into θ + (k−1)θ at the representative level).

### ONLY direction (r̄ ≠ 0)

**Invariant:** "no coordinate of (ā, b̄, c̄) is 0̄" (equivalently, no angle is a θ-multiple). This is a coset-avoidance condition: the angle-triple (ā, b̄, c̄) lies in (G \ {0̄})³ subject to ā+b̄+c̄ = r̄ ≠ 0.

**Key structural fact (this is the corrected defense-explorer invariant):** The condition "no coordinate = 0̄" is preserved under Mulan's move for ARBITRARY γ̄ — it does NOT require γ̄ to lie in any fixed subgroup (the flaw that broke the explorer's "group ⊆ ℤ/p" version). The reason is the four-case residue chase, restated in G:

Suppose both children could acquire a 0-coordinate. Child1's coordinates are (γ̄, ȳ, r̄ − ȳ − γ̄); child2's are (x̄ − γ̄, z̄, ȳ + γ̄). With ȳ, z̄ ≠ 0̄ (invariant), a 0-coordinate in child1 forces γ̄ = 0̄ OR r̄ − ȳ − γ̄ = 0̄; a 0-coordinate in child2 forces x̄ − γ̄ = 0̄ OR ȳ + γ̄ = 0̄. The four combinations yield x̄ = 0̄, ȳ = 0̄, z̄ = 0̄, or r̄ = 0̄ — all contradictions (first three violate the invariant, the last violates r̄ ≠ 0). So at least one child remains 0̄-free; Shan-Yu keeps it.

**Initial triangle:** pick (ā, b̄, c̄) with ā+b̄+c̄ = r̄ ≠ 0 and all coordinates ≠ 0̄ (exists by the generic-choice argument: the forbidden locus is a finite/countable union of hyperplanes in the angle-simplex).

### Conclusion
Mulan wins ⇔ r̄ = 0̄ ⇔ θ = 180°/N. The subgroup framing makes the boundary (r̄ = 0 vs r̄ ≠ 0) and the four-case obstruction (each case ends in "a coordinate forced to 0̄, contradiction") transparent.

## Key lemmas (claim + mechanism)
- **Torsion-boundary lemma:** 180 mod θ = 0 ⇔ θ is a unit fraction of 180° — by definition of divisibility in ℝ (180/θ ∈ ℤ).
- **Create-coset lemma (IF):** choosing γ̄ = −ȳ makes both children's P-angles 0̄ in G — because the P-angles are ȳ+γ̄ and r̄−ȳ−γ̄, and with γ̄ = −ȳ and r̄ = 0̄ both equal 0̄.
- **Coset-avoidance invariance (ONLY):** the 0̄-free locus is preserved — because the four ways both children could acquire a 0̄ each reduce to "some existing coordinate is 0̄ or r̄ = 0̄," both excluded.
- **Arbitrary-γ robustness:** unlike the explorer's subgroup-invariant, the 0̄-free condition does not constrain γ̄ — γ̄ = −ȳ is ONE choice that works for IF; for ONLY, NO γ̄ works, which is exactly the obstruction.

## Open gaps (builder fills)
1. **Lift "0-coordinate in G" to "angle = θ exactly" for the win.** The G-framing forces angle ≡ 0 mod θ (a θ-multiple), not angle = θ. The k-descent (representative-level) closes this gap — write it in G-language: among representatives kθ (1 ≤ k ≤ N−1), splitting kθ with γ = θ sends k ↦ k−1, bottoming at k = 1 = θ. (Imported from mod-theta-descent.)
2. **Create-move validity (representative inequalities)** — the γ ∈ (0,X), child-non-degeneracy bounds — same gap as mod-theta-descent.
3. **Initial-triangle existence in G** — a clean measure/countability argument: {triples with some coordinate 0̄} is a finite/countable union of codim-1 loci in the 2-simplex {(A,B): A,B>0, A+B<180}; its complement is nonempty (indeed full-measure) when r̄ ≠ 0.

## Cases to cover
Same as mod-theta-descent.

## Watch out for
- This framing is the SAME core proof as mod-theta-descent, re-skinned in the language of ℝ/θℤ. Its value is that it makes the "arbitrary γ robustness" of the invariant transparent and exposes why the explorer's stronger "group ⊆ ℤ/p" invariant was wrong (that one tried to constrain γ̄ to a subgroup; the correct invariant constrains the COORDINATES, not γ̄).
- The "3-smooth only" conclusion from the defense explorer is contradicted by θ = 36° = 180/5 (verified win); do not import it. The torsion boundary is r̄ = 0̄ (unit fraction), NOT "denominator 3-smooth."
- Shared wall with mod-theta-descent: the create-move + four-case facts. If those fail, this fails too.
