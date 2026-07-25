# Proof-outliner field — round 2 — imo-2026-04 ("Mulan's Triangle Game")

## MAJOR RESULT THIS ROUND
The round-1 conjecture "Mulan wins iff 0<θ≤90" is **FALSE**. The correct
characterization is:

    Mulan wins  ⟺  θ divides 180°   (θ = 180/n, integer n ≥ 2)
              i.e. winning set = {90°, 60°, 45°, 36°, 30°, 180/7°, 22.5°, 20°, …}.

- Every winning θ is ≤ 90 (so θ>90 still all lose — consistent with the non-obtuse
  defense), BUT θ≤90 is NOT sufficient: θ = 40,50,70,25 (≤90, ∤180) are LOSSES.
- Confirmed computationally (exact-fraction AND-OR game search, forced moves +
  bisection AND-nodes + lattice move, to depth 9): divisors 45,36,30,20 WIN;
  non-divisors 40,50,70,25 have NO win. Both proof directions below are essentially
  complete; remaining work is rigor/edge-case detail, not new ideas.

The engine: **the angle-sum 180 is the ONLY arithmetic anchor.** Every cut preserves
membership in the lattice θℤ, except the constant 180 (a cut-point angle is 180−x−b);
Mulan gets traction exactly when 180 ∈ θℤ, i.e. θ|180.

## imo-2026-04

lattice-invariant-180: new
Target: Mulan wins ⟺ θ|180 (full characterization, both directions).
Technique: invariant/monovariant. Necessity = Shan-Yu maintains "no angle ∈ θℤ" via a
  4-case mod-θ covering; sufficiency = plant a θ-multiple in both children (x≡−b mod θ,
  legal because θ|180 makes the supplementary cut-point angle also ≡0), then descend by
  forced θ-plants to 2θ, then bisect.
Skeleton:
  1. One-cut algebra: child1=(x,b,180−x−b), child2=(a−x,c,x+b); bisection children
     (a/2,b,a/2+c),(a/2,c,a/2+b); forced θ-plant keeps (a−θ,c,b+θ). — angle-sum/ext-angle
  2. Lemma 0 (double-θ exhaustion): only a=2θ and θ=90 give both-children-θ. — casework
  3. Necessity (θ∤180): invariant I = "no angle in θℤ"; base = generic start; preservation
     = 4-case covering (both-bad ⟹ a≡0 or b≡0 or c≡0 or θ|180). — invariant induction
  4. Sufficiency (θ|180): θ=90 altitude; else inject θ-multiple in both children, descend
     mθ→(m−1)θ→…→2θ, bisect. — construction + monovariant m
  5. Answer set {180/n : n≥2}, verify. — direct
Key lemmas:
  - Covering lemma — because both children hitting θℤ forces (mod θ) one of a,b,c≡0 or
    180≡0; the first three contradict I, the last needs θ|180.
  - Supplementary-plant — because 180−x−b and x+b sum to 180≡0 (mod θ) when θ|180, so
    x≡−b makes BOTH ≡0: a double lattice plant in one move.
  - Descent — forced θ-plant at mθ keeps (m−1)θ; m strictly decreases to 2.
Open gaps: G1 explicit generic start; G2 x∈(0,a) representative + non-degeneracy of
  children (esp. boundary a=θ at θ=60); G3 descent validity + bound ≤180/θ; G4 θ=90
  interior-altitude existence (≥2 acute angles); G5 full 6-sub-case Lemma 0.
Cases to cover: θ=90; θ|180 with θ≤60; θ∤180 (subsumes θ>90).
Watch out for: invariant is "no angle in θℤ" (stronger than "no angle=θ") — essential;
  do NOT revert to the refuted θ≤90 target; 180≡0 is the unique anchor.

reduce-to-2theta: new
Target: same answer θ|180 — RIVAL FRAMING as a cross-check.
Technique: reduce whole game (θ≠90) to "force angle 2θ then bisect" via Lemma 0, then a
  boolean potential Φ = "angles meet θℤ?" + monovariant m. Independent bookkeeping that
  catches any covering-step error in the invariant approach.
Skeleton:
  1. Lemma 0 ⟹ for θ≠90, winning = forcing an angle 2θ. — casework
  2. Descent: Φ=true (multiple ≥2θ) ⟹ win by forced plant down to 2θ. — monovariant
  3. Flip: from Φ=false, both children meet θℤ ⟺ θ|180 (covering). θ∤180 ⟹ Φ stuck
     false ⟹ loss; θ|180 ⟹ flip then descend ⟹ win. — invariant + construction
Key lemmas: Lemma 0 (reduction, supplementary cut-point angles); Flip lemma (=covering);
  Descent lemma (forced plant keeps a θ-multiple).
Open gaps: H1 Lemma 0 full proof; H2 flip x-range/non-degeneracy (share G2);
  H3 descent bound; H4 Φ-stays-false induction (share covering lemma).
Cases to cover: θ=90; θ|180,<90; θ∤180.
Watch out for: state the explicit finite move bound (≤180/θ+O(1)); don't conflate "a
  child contains θ" with the double-θ win.

angle-sum-anchor: new
Target: same answer θ|180 — INDEPENDENT re-derivation that does NOT assume the answer,
  to settle θ≤90 vs θ|90 vs θ|180.
Technique: center on the angle-sum 180 as the sole residue anchor; supplement-sum
  identity (cut-point angles sum to 180) gives the double plant iff θ|180. Explicitly
  refutes θ≤90 (θ=40 loses) and θ|90 (θ=60 wins, 60∤90).
Skeleton: 1 cut algebra + supplement identity; 2 "only guaranteed residue is 180's"
  ⟹ lattice reachable ⟺ θ|180; 3 necessity (covering); 4 sufficiency (plant+descend+
  bisect); 5 tabulate/verify answer set.
Key lemmas: Supplement-sum (cut-point residues sum to 180 mod θ); Anchor lemma (only
  180's residue is guaranteed — rigorous core is the covering computation, not the
  intuition).
Open gaps: J1 make "anchor" rigorous via the shared covering lemma (do NOT rest on the
  heuristic); J2 construction validity (share G2/G3); J3 explicit answer tabulation
  n=2..6 → 90,60,45,36,30 win, verify 40,50,70,25 lose.
Cases to cover: three regimes + explicit answer-set statement (compute_and_prove).
Watch out for: keep genuinely independent (reach θ|180 via anchor/supplement, cross-
  check both loss families); the covering computation is load-bearing, the "anchor"
  language is only intuition.

## Shared lemma to certify (all three approaches import it)
`lemmas/lattice-covering.md`: "If a,b,c ∉ θℤ and θ∤180, then for every cut vertex and
every x∈(0,a) at least one child has all angles ∉ θℤ." Proof = the 4-case mod-θ argument.
Once one builder proves it and the reviewer certifies, the other two import it.

## Notes for the reviewer / build set
All three approaches reach the SAME (now essentially proven + computationally confirmed)
answer θ|180; they differ in framing (invariant defense vs 2θ-reduction+potential vs
angle-sum-anchor re-derivation) so a hidden error in one is caught by another. This is a
hedge on a near-complete solution, not three shots at an open gap. lattice-invariant-180
is the most complete — recommend it as the primary build; reduce-to-2theta and
angle-sum-anchor as independent cross-checks (and angle-sum-anchor owns the "state and
verify the answer set" rigor requirement).

build set: lattice-invariant-180, reduce-to-2theta, angle-sum-anchor
</content>
