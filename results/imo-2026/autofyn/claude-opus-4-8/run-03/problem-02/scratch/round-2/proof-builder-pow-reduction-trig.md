# Build report — pow-reduction-trig (imo-2026-02), round 2

Status: **partial** (major structural advance on GAP-2; the balance identity is reduced
from a transcendental claim to an exact finite linear-algebra membership whose consistency
is verified. Explicit symbolic cofactors not extracted in budget — so NOT a full solve.)

## What got closed / advanced this round (all EXACT, reproducible in sympy)
1. **Constraint normal form (Lemma 4).** (★) equals, identically,
   `C1(γ) = 2 sinA cosC sin²γ + sinC sin(β+γ) sin(γ−A−β)` with `γ=β+ψ=∠ACK`; this is
   **affine-linear in (cos2γ, sin2γ)**. σ-image gives (★★) affine-linear in (cos2δ,sin2δ).
   Verified `C1 − (raw law-of-sines residual) = 0` symbolically.
2. **Bilinearity of the cleared residual (Lemma 5).** `Ẽ := E·sin²(A+β+γ)·sin²(A+β+δ)`
   (with `E = O·(B−C) − (|B|²−|C|²)/4`) is **exactly bilinear** in
   (cos2γ,sin2γ)×(cos2δ,sin2δ): the sympy polynomial has degree ≤1 in each of the four
   variables and no odd-harmonic remainder. So `Ẽ = [1,cos2γ,sin2γ] M [1,cos2δ,sin2δ]ᵀ`.
3. **Reduction to linear algebra.** Balance identity `⟺ Ẽ = f·C1 + g·C2`, `f` affine in
   (cos2δ,sin2δ), `g` affine in (cos2γ,sin2γ) — a 6-parameter linear system. Verified
   **consistent** (coefficient matrix rank 5 = augmented rank 5 at generic A,B,β), and `Ẽ`
   vanishes at **all four** common zeros of (C1,C2) on the two unit circles (both branches).

This upgrades round 1's numeric-only `|E|≤1e-13` to an exact structural identity: the whole
problem is now a `3×3` bilinear-form membership `M w_i ∥ c1`, a finite algebraic fact.

## Remaining gap (GAP-2′) — precise
Produce the explicit cofactors `f, g` (rational-trig in A,B,β, valid mod sin²+cos²=1) and
verify `Ẽ − f C1 − g C2 ≡ 0` symbolically. The linear system is consistent (established),
but: sympy `solve`/`linsolve` returned empty on the trig function field (choked, not truly
inconsistent — the numeric rank check contradicts that); a subset LUsolve gave candidate
cofactors whose residual is zero only *modulo* the Pythagorean relations, and that final
Gröbner reduction (6 base vars, 3 relations) did not terminate in the 2-min sympy budget.
Per run-state rule "no numeric-only load-bearing step", the rank-5=rank-5 consistency
(currently numeric-at-generic-point) is not yet a from-scratch symbolic certificate.

## Two clean finishes for next round (either closes it)
- (a) **3×3 factorisation.** Compute `M`, `c1=(p₀,p₁,p₂)`, `c2=(q₀,q₁,q₂)` explicitly
  (each ~one line of trig) and exhibit `a,b ∈ ℝ³` with `M = c1 aᵀ + b c2ᵀ`. Then
  `Ẽ = C1·(a·[1,cos2δ,sin2δ]) + (b·[1,cos2γ,sin2γ])·C2` is immediate. Far smaller than raw.
- (b) **Affine-form proportionality (no cofactors).** For fixed admissible δ, `Ẽ` is an
  affine form in (cos2γ,sin2γ) vanishing at BOTH circle-zeros of `C1` (verified); two
  distinct circle points determine a chord, so `Ẽ|_δ ∝ C1`, hence `Ẽ=0` at the geometric γ.
  Requires proving the "both zeros" fact exactly — equivalent to `M c2⊥ ⊆ span c1`.

## Handoff
Lemmas 4, 5 are exact and worth certifying. The approach is now one small linear-algebra
computation (the `M = c1 aᵀ + b c2ᵀ` factorisation) from a second independent full solve,
on a wall genuinely different from coordinate-identity's orientation gap.
