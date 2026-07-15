# Approach: power-point-trig

## Status
partial

## Target
The full claim of imo-2026-02: prove OM = ON for the circumcentre O of triangle AKL.

## Route (one paragraph)
Coordinate-free power-of-a-point route. Reduce OM = ON to pow(B, ω) − pow(C, ω) = (c² − b²)/2 for ω = (AKL) via the midpoint power formula; express pow(B) and pow(C) through the second intersections of lines AB, AC with ω using the sine rule and inscribed angles; the target becomes a single trigonometric identity (♦) in the angles α, β, γ and the angles λ = ∠ALK, μ = ∠AKL of triangle AKL, which must be closed using the two constraint relations. Fully synthetic-trig, no coordinates; the finish is open and is the hard gap.

## Skeleton (proof with gaps)

Notation as in fixed-point-t (α, β, γ; a, b, c; A, B, C angles of ABC). ω = circumcircle of AKL, R its radius.

**Step 1 (Midpoint power reduction).** For the midpoint M of AB and any circle ω through A with centre O: OM² = (OA² + OB²)/2 − AB²/4 (median-length/parallelogram law in triangle OAB), hence pow(M, ω) = OM² − R² = pow(B, ω)/2 − c²/4 using pow(A) = 0. Similarly pow(N, ω) = pow(C, ω)/2 − b²/4. Therefore
  OM = ON ⟺ pow(M) = pow(N) ⟺ pow(B) − pow(C) = (c² − b²)/2.
(Complete; short. Numerically confirmed: pow(B) − pow(C) = (c²−b²)/2 exactly across the whole family.)

**Step 2 (Power via second intersections).** Let X be the second intersection of line AB with ω, Y the second intersection of line AC with ω. Numerics: X lies strictly between B and M (parameter t ∈ (0.2, 0.45) on segment BA), so B is outside ω and pow(B) = BA·BX = c·BX; similarly pow(C) = b·CY. (GAP: prove the position of X — e.g. show pow(B) > 0 and pow(M) < 0 directly, or handle signs with directed lengths throughout.)

**Step 3 (Sine-rule expression).** In triangle BXK: ∠XBK = ∠ABK = α; ∠BXK = ∠ALK =: λ, because AXKL is cyclic and X, L lie on opposite arcs of chord AK (GAP: configuration argument), so ∠AXK = π − λ and ∠BXK = λ (X between B and A). Hence ∠BKX = π − α − λ and
  BX = BK·sin(α+λ)/sin λ, so pow(B) = c·BK·sin(α+λ)/sin λ = (c²/2)·sin γ·sin(α+λ)/(sin(α+γ)·sin λ),
using the Parametrization Lemma BK = (c/2)sin γ/sin(α+γ) (shared with fixed-point-t, Step 2). Mirrored: pow(C) = (b²/2)·sin β·sin(α+μ)/(sin(α+β)·sin μ), μ := ∠AKL.

**Step 4 (Product-to-sum simplification).** sin γ sin(α+λ) − sin(α+γ) sin λ = sin α sin(γ−λ) (product-to-sum, exact identity). Hence
  pow(B) − c²/2 = (c²/2)·sin α·sin(γ−λ)/(sin(α+γ)·sin λ), and the target of Step 1 becomes
  (♦)  c²·sin(γ−λ)/(sin(α+γ)·sin λ) = b²·sin(β−μ)/(sin(α+β)·sin μ).
Perfectly mirror-symmetric (swap b↔c, β↔γ, λ↔μ).

**Step 5 (Close (♦) — the open gap).** Available relations:
  - λ + μ = π − ∠KAL, and ∠KAL = A − ∠BAK − ∠CAL where ∠BAK, ∠CAL are determined by triangles ABK, ACL (e.g. tan ∠BAK = p_K sin α/(1 − p_K cos α) with p_K = sin γ/(2 sin(α+γ))).
  - sin λ/sin μ = AL/AK (sine rule in AKL), with AK = c·|1 − p_K e^{iα}|, AL = b·|1 − p_L e^{iα}|.
  - cot λ = (AL² + KL² − AK²)/(4·[AKL]), cot μ = (AK² + KL² − AL²)/(4·[AKL]) — writing (♦) as c²(sin γ cot λ − cos γ)/sin(α+γ) = b²(sin β cot μ − cos β)/sin(α+β) and substituting turns everything into side-lengths of AKL.
  - The two constraint quadratics q_K, q_L (shared Constraint Lemma).
GAP: find the combination that closes (♦). Risk: this may reduce to the same bulk algebra as quadratic-ideal-certificate; the hope is that (♦) factors through readable sub-identities.

**Step 6 (Conclusion).** (♦) ⟹ pow(B) − pow(C) = (c²−b²)/2 ⟹ pow(M) = pow(N) ⟹ OM = ON. ∎

## Key lemmas (claim + mechanism)
- Midpoint power formula — parallelogram/median law plus pow(A) = 0.
- pow(B) = c·BK·sin(α+λ)/sin λ — sine rule in BXK with the inscribed-angle transfer ∠BXK = ∠ALK.
- Product-to-sum reduction to (♦) — the identity sin γ sin(α+λ) − sin(α+γ) sin λ = sin α sin(γ−λ).

## Open gaps (for the builder)
1. Step 5: the closing identity (♦) — genuinely open, no verified mechanism yet.
2. Step 2/3 configuration facts (position of X, arc sides), or a clean directed-length/directed-angle setup that avoids them.

## Cases to cover
- Signs of pow(B), pow(C) (B, C outside ω) and of γ−λ, β−μ (numerically λ > γ and μ > β, so both sides of (♦) are negative — keep consistent).

## Watch out for
- λ = γ and μ = β are FALSE (they would force M, N onto ω; numerically refuted). Do not "simplify" (♦) that way.
- If Step 5 devolves into coordinate algebra, stop and defer to quadratic-ideal-certificate rather than duplicating it.

## Approaches tried
- (round 1) Outlined; Steps 1–4 verified numerically; Step 5 open. Not yet built.

## Current best
Steps 1 and 4 complete modulo prose; the reduction to (♦) is a correct and clean intermediate target.
