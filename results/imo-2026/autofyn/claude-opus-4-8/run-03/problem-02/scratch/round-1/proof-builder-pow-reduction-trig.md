# Build report — pow-reduction-trig (imo-2026-02), round 1

Status: **partial** (strong progress; one bounded gap).

## What got closed
- **Reduction fully proved.** Placing A at the origin makes M=B/2, N=C/2. Then
  `OM=ON ⟺ O·(B−C)=(|B|²−|C|²)/4 ⟺ pow(B,⊙AKL)−pow(C,⊙AKL)=(c²−b²)/2` (Lemma 1). This
  is cleaner than the outline's `MX/NY=b/c`: it eliminates O, R, and the second
  intersections X, Y entirely. Recommend promoting Lemma 1.
- **GAP-1 (outline) closed.** All four sub-triangle law-of-sines relations derived from
  scratch: `BK=(c/2)sinψ/sin(β+ψ)` (△BMK) `= a·sin(C−β−ψ)/sin(A+2β+ψ)` (△BKC), giving
  constraint (★); σ-image gives (★★) for CL. The angle mis-assignment trap (∠LNC, ∠BMK
  at the midpoints) is handled explicitly and correctly.
- Circumcentre relations `O·K=|K|²/2`, `O·L=|L|²/2` (A on circle) reduce the target to a
  single scalar identity (‡).

## What remains (GAP-2, the balance identity)
- Prove `E(β):=O·(B−C)−(|B|²−|C|²)/4 ≡ 0` symbolically, given ψ,φ solve (★),(★★).
- Verified numerically to ≤1.4e-13 on THREE independent scalene triangles at their
  admissible β (and E=O(1e−2) off-constraint, so it genuinely uses (★),(★★)). So the
  identity is true; only a from-scratch symbolic derivation is missing.
- Two concrete routes for next round: (a) exhibit `E = f·R_ψ + g·R_φ` (ideal membership
  in the two constraint residuals); (b) solve each of (★),(★★) — each is a single
  sinusoid `P cos2ψ+Q sin2ψ+S=0` — in closed form and substitute. Both are finite
  trig computations; ran out of budget.

## Spec / correctness concerns
- None with the problem statement. Orientation of the interior rays was pinned against
  explicit numerics (the correct signs are recorded in the approach file's direction
  vectors), so no sign ambiguity remains in the setup.
- σ-antisymmetry is necessary but NOT sufficient to finish (both sides are
  σ-antisymmetric); flagged in the file so no one over-claims a σ-only finish. This
  matches the outline-reviewer's warning.

## Handoff suggestion
This approach is one honest trig identity away from solved. A focused next-round build
(or a short sympy-assisted closed-form solve of (★) transcribed as prose) should close
it. The reduction (Lemma 1) is worth certifying into results/imo-2026-02/lemmas/ for the
other approaches (coordinate-identity, synthetic-sigma-spiral) to import.
