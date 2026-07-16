# Outline review — round 1, imo-2026-05

Fresh run; no `current.md` / recorded dead ends to conflict with. I re-derived every load-bearing identity independently in sympy (all five checked: both verification SOS margins = (x−y−c)²/4; the left inequality h-coordinate form (x−f(y))² ≥ 2c(x+f(y))+c²; the forbidden-interval roots y₀+a ± sqrt(4ay₀+2a²) with length²−a² = a(7a+16y₀) > 0; the right-inequality expansion (x+y+α)²−4x(y+β) = 4y(α−β)+(s+α)²−4sβ; the fixed-point zone (y−y₀)² ≥ 4ay₀). All checks passed — the outliner's "sympy-verified" claims are genuine.

All three approaches are whole attempts: each targets the full characterization (verification of f = id+c, c ≥ 0, AND uniqueness), not a fragment. The two orbit approaches share the reduction steps 2.1–2.3 but their kill mechanisms are genuinely different (left vs right inequality; supremum squeeze vs spreading), so they are legitimate rivals, not one proof split across slugs. chain-lipschitz-squeeze is fully independent (never forms the functional equation).

---

## chain-lipschitz-squeeze — APPROVE

Verdict basis (every step re-derived by hand):
- Step 2.1 (*): left at (f(y₂), y₂) gives f(f(y₂)) ≤ 2f(y₂)−y₂; right at (f(y₂), y₁) gives f(f(y₂)) ≥ 2sqrt(f(y₁)f(y₂))−y₁; chaining is valid. Correct, and it genuinely uses only one-sided bounds — good hedge value.
- Step 2.2(A): 2pq ≤ 2q²+t → p ≤ q+t/(2q) → f(z+t) ≤ f(z)+t+t²/(4f(z)). Checked.
- Step 2.2(B): 2pq ≤ 2p²−t → t ≤ 2p(p−q) → p > q (strict monotonicity, derived not assumed) and f(z+t)−f(z) ≥ t − t(p−q)/(2p). Checked, including the GAP 1 mechanism: p−q ≤ (t+t²/(4m))/(2√m), p ≥ √m, deficit ≤ t²/(4m)+t³/(16m²). The uniform m = f(y) on [y, y+T] is justified by the monotonicity established in the same step — order is sound.
- Step 2.3 telescoping: upper T+T²/(4mn), lower T−T²/(4mn)−T³/(16m²n²), both → T. The limit argument is elementary and needs no continuity of f (it is a statement about the fixed value f(y+T)−f(y) squeezed between explicit sequences).
- Step 2.4: c ≥ 0 codomain argument present; combined with Part 1 gives both directions.

Issues (minor, close while building): (a) in Step 2.4 the c < 0 exclusion via "y = −c/2" needs −c/2 > 0 stated (holds since c < 0); (b) state positivity at every squaring/division as the file already warns. GAP 1 and GAP 2 are writeup, not mathematics. This is the closest to a finished proof.

## orbit-forbidden-zone — APPROVE

- Steps 2.1–2.3 (FE f∘f = 2f−id from x = f(y) in both inequalities, h(f(y)) = h(y), fⁿ(y) = y+n·h(y) by induction, h ≥ 0 by orbit escape) are correct and gap-free modulo the one-line induction the file itself flags.
- Step 2.4 (L) verified symbolically.
- Step 2.5 (two positive values a < b die): I traced it — the f-image of the a-orbit is a step-a unbounded AP, the minimal-n choice gives 0 ≤ f(y)−x < a, and (L) forces (x−f(y))² ≥ 4(b−a)x → ∞. Sound; the threshold bookkeeping is GAP 1 (writeup).
- Step 2.6 (fixed points cannot coexist with h = a > 0): interval I(y₀) roots and |I(y₀)| > a verified; the two sub-cases in (ii) (u ∈ I vs u ≤ inf I with the AP-hits-interval lemma) are exhaustive — note inf I(y₀) can be ≤ 0, which the AP lemma handles unchanged; (iii)'s (T,∞) ⊆ P follows from F ∪ P = R_{>0} and T = sup F, and the ε-squeeze a < 2ε is correct.
- Case coverage complete: {two positive values} / {0 and a > 0 coexist} / {h constant}; a = 0 correctly routed to 2.6, not 2.5 (the file's own warning).

Issues to close while building: in 2.6(iii), state explicitly that P nonempty bounds F above (so T < ∞) and that y₀ ∈ F with y₀ > T−ε exists because T = sup F of a nonempty set.

## right-spreading-fixed-points — APPROVE

- Shares 2.1–2.3; the right-inequality expansion (R) verified symbolically.
- Step 2.5' chase: with s ∈ [0, a) and 0 < a < b, the bound 0 ≤ −4y(b−a)+(s+a)²−4sb ≤ −4y(b−a)+4a² < 0 for y > a²/(b−a) is correct ((s+a)² < 4a², −4sb ≤ 0). The file's warning against the lossy crude bound is a real trap correctly avoided.
- Step 2.6' spreading: (i) (y−y₀)² ≥ 4ay₀ verified, so J(y₀) ∩ R_{>0} ⊆ F given two-valuedness (order dependency on 2.5' correctly flagged). (ii) I traced the sup argument: [y₀,S) ⊆ F as the union over admissible s; S ≥ y₀+2√(ay₀) > y₀+√(ay₀) so the window (S−√(ay₀), S) is nonempty and inside F; a fixed y there pushes F to y+2√(ay) > S+√(ay₀), covering S itself since S ∈ (y, y+2√(ay)). Contradiction with the sup is genuine. (iii) orbit escape is immediate.

Issues to close while building: (a) in (ii), explicitly justify [y₀,S) ⊆ F (union of the nested intervals) and that the chosen y satisfies y ≥ y₀; (b) in the chase 2.5', the chasing m exists only once y ≥ x₀ — state the threshold on n.

---

## Rejected routes — concur with the outliner

- Differentiability route: assumes unproven regularity — correctly not opened.
- Legendre/envelope: collapses to (*) of chain-lipschitz-squeeze — correctly merged, not a rival.
- Rational/irrational step casework: unnecessary given the within-one-step chase — correctly excluded; builders must not reintroduce it.

## Selection

Registered all three (population was empty). Ranking recorded via `update_ranking`:
- chain-lipschitz-squeeze > orbit-forbidden-zone (smaller gaps, no casework, hedges the FE combination)
- chain-lipschitz-squeeze > right-spreading-fixed-points (same reasons)
- orbit-forbidden-zone = right-spreading-fixed-points (draw — equal-quality rival kill mechanisms, same gap sizes)

Resulting Elo: chain-lipschitz-squeeze 1531, right-spreading-fixed-points 1486, orbit-forbidden-zone 1483.

No copies requested; none needed. All three go to builders in parallel — one per slug. First APPROVE among the orbit pair should certify steps 2.1–2.3 into `lemmas/` (functional-equation, orbit-invariance, h-nonnegative) for import by the sibling.

build set: chain-lipschitz-squeeze, orbit-forbidden-zone, right-spreading-fixed-points
