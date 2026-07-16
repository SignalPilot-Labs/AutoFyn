# Build report — descending-chain — round 2

## Result
Status: **solved** (claimed). Full proof written to `results/imo-2026-04/approaches/descending-chain.md`. Both directions of the characterization proved: Mulan wins iff θ = 180°/n, n ∈ ℤ, n ≥ 2.

## Mandatory reviewer fixes — all applied
1. **Fix 1 (H2, false monovariant):** removed all "largest multiple drops" language. Phase D is now **Lemma A1 (Descent)**: strong induction on k for "T has an angle kθ ⟹ Mulan wins within k − 1 cuts" — cut to the kθ vertex with s = θ; p₁ carries θ (kept ⟹ win at next check), p₂ carries (k − 1)θ (IH applies). Companion-independent. The refuting counterexample (θ = 15°, (75°, 60°, 45°)) is recorded in the file as a remark so nobody revives the monovariant.
2. **Fix 2 (H4):** grind safety-preservation stated and proved: kept piece (y, x−θ, z+θ) has residues mod θ unchanged (y, x, z), all nonzero, hence safe; so the phase re-enters (III) or (II) and never needs (I) mid-grind; the boundary x − θ = θ cannot arise (x = 2θ contradicts safety). Both remarks are in Lemma A3.
3. **Fix 3 (H5):** step arithmetic made consistent: grind ≤ n − 3 (x₀ < (n−2)θ, x₀ ∈ (mθ,(m+1)θ) with m ≤ n−3, exactly m grind cuts), ignition + descent ≤ n − 1, total ≤ 2n − 4 for n ≥ 4 and ≤ n − 1 for n ∈ {2, 3}.

## Gaps closed (all of H0–H8)
- **H0 (cut formula + realizability):** Lemma 0, full proof — continuity via arccos, strict monotonicity via angle addition (ray through an interior point of the opposite side), IVT bijection [0,1] → [0,v]; piece angles derived; nondegeneracy; supplementary P-angles; companion relabeling (s ↔ v−s).
- **H1 (trichotomy):** proved exhaustive and disjoint inside Proposition A; (III) empty unless n ≥ 4 (x ≤ 60°).
- **H2:** replaced per Fix 1 (Lemma A1), including k−1 = 1 sub-case via the induction base.
- **H3 (ignition validity):** one uniform argument for all n ≥ 2: z ≥ 90° − x/2 (from y ≤ z), so z − s ≥ (90° − θ) + x/2 > 0 since θ ≤ 90°. Covers the n = 2 sub-case without extra casework; n = 2 both-pieces-contain-θ noted.
- **H4:** Lemma A3 per Fix 2; smallest angle of kept piece is exactly x − θ (y ≥ x > x−θ, z+θ > x−θ).
- **H5:** assembly per Fix 3, with the initial-position check (0 cuts if T already has θ) and both Shan-Yu options handled at every cut.
- **H6 (safe start):** isoceles family, finite exclusion set — Lemma B1.
- **H7 (closure):** four-case congruence proof written **inline** as Lemma B2 (per the shared-lemma condition; did NOT import the uncertified `lemmas/safe-piece-exists.md`; the remainder-forcing builder files it). Congruence mod θ over ℝ defined before the case split; "positive angle ≡ 0 ⟺ positive multiple" stated once; quantified over every vertex choice and every parameter via Lemma 0(c).
- **H8 (assembly of B):** explicit induction; covers θ > 90°, rational non-divisors, irrational θ uniformly.
- **Answer verified** by substitution at θ = 90°, 40°, 120° per the rigor rules.

## Numeric sanity checks run (not proof steps)
- Adversarial exact-rational simulation of the finished three-phase strategy: n = 2,…,12, 400 random triangles each, bound n−1 / 2n−4 held with 0 failures; every cut-validity assertion passed.
- Descent Lemma adversarially simulated (n = 3, 4, 5, 7, 12): 0 failures.
- Closure Lemma: θ ∈ {40°, 72°, 120°, 7/3°, 170°}, 2000 random safe triangles + random cuts each: 0 failures.

## What remains open
Nothing within this approach. For next round: once the proof-reviewer certifies `lemmas/safe-piece-exists.md`, the inline Lemma B2 may be swapped for an import (optional; the file is self-contained as is).

## Spec concerns
(none)
