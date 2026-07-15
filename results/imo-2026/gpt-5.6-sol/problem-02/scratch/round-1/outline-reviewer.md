## oriented-determinant-elimination — APPROVE

This is a whole end-to-end attempt, and its main reductions are concrete and independently sanity-checked. On the numerical samples from the computation explorer, the two stated incidence equations and determinant target agree to the precision allowed by the rounded angle data; moreover, the determinant formula follows correctly from Cramer's rule and the linearization of `OM^2-ON^2`. Unlike the discarded structural opening, it does not rely on the numerically false claim that `B,C,K,L` are concyclic.

Builder requirements:
- Derive every ray direction from the actual order conditions (`K` inside angle `LBA`, `L` inside angle `ACK`, and membership in the two triangles), rather than merely drawing the intended picture. In particular, prove positivity of the six ray parameters and of every sine denominator used.
- Derive both equations `q=F(delta)` and `q^{-1}=F(beta)` by explicit oriented cross products or sine rules. The displayed trigonometric compression identity must also be verified.
- Prove `[K,L] != 0` from the existence of the circumcentre of triangle `AKL`/nondegeneracy before applying Cramer's rule.
- Step 6 is load-bearing. The final proof must display a checkable identity expressing the residual determinant in terms of the two incidence residuals, or an equivalent line-by-line trigonometric reduction. “CAS factorization” or “terms pair” is not itself a proof.

## antipode-quarter-turn — CHANGES REQUESTED

The antipode reduction is correct and strong: the factor-2 homothety centered at `A` maps `(O,M,N)` to `(X,B,C)`, so it converts the exact original claim into `XB=XC`. The Thales/real-part equations are also valid. Thus this is a whole approach with a genuinely different presentation from direct circumcentre elimination.

The quarter-turn telescoping lemma, however, is currently more a desired conclusion than a specified mechanism. “Successive imaginary-part equations cancel” does not identify which quotients are taken, which multipliers align the equations, or why all six unknown positive lengths disappear. One equal angle supplies an argument relation but no scale relation, so this omission is precisely where a false similarity could be hidden.

Builder requirements:
- Write all six directed ray equations with their signs justified from interiority.
- Before presenting prose around the route, produce the exact ordered imaginary-part/real-part equalities and their multipliers. Show the coefficient of each of `r,s,w,u,v,h` cancels.
- Explicitly identify where `2BM/AB=2CN/AC=1` enters; midpoint data cannot merely be mentioned after the cancellation.
- Include the cases `lambda=0` or `mu=0` without dividing by either, and verify that any quotient used has nonzero denominator.
- If this exact telescoping identity cannot be obtained without expanding to the same determinant identity as the first slug, record the gap rather than claiming an independent synthetic cancellation.

## sine-product-antipode — CHANGES REQUESTED

The opening and endpoint are sound, but Steps 3–5 are under-specified. The outline names four triangles and promises a product in which every non-midpoint factor cancels, yet gives no actual sine-rule formula for `XB/XC`. The claimed “four-triangle sine-product lemma” is therefore not presently verified, and ordinary angle subtraction is particularly unsafe in this configuration. This is still a complete intended route, not a fragment, and is worth retaining as a rival synthetic attempt, but it is weaker than the first two candidates.

Builder requirements:
- State the exact directed sine-rule identity for `XB/XC` before claiming cancellation, including every side and every directed sine.
- Derive each angle at `X,B,C,K,L` from the three given equalities and `XK perpendicular AK`, `XL perpendicular AL`; do not assume `B,C,K,L` cyclic.
- Give a disjoint accounting table or equivalent calculation showing where each side and sine occurs once in numerator and once in denominator.
- Prove all divided sines are nonzero from the interior hypotheses. If the exact product leaves any additional scale or angular factor, leave the approach partial; do not suppress it by an unsupported similarity.

## inverted-circle-intercepts — CHANGES REQUESTED

The equal-power reduction is legitimate in principle and the approach targets the full claim. It also provides population diversity by avoiding the antipode. However, its load-bearing inverted-line intercept lemma is the least supported claim in the field. The statement that elimination becomes linear after reciprocal-square inversion is not established: `K/AK^2` and `L/AL^2` introduce nonlinear reciprocal norms, and merely having three affine ray descriptions for each original point does not make those terms linear. Thus the proposed mechanism may fail even though the target intercept identity is equivalent to the theorem.

Required revision before this should enter a future build set:
- First derive formulas for the two intercepts of the line through `K/AK^2` and `L/AL^2`, then exhibit an actual cancellation using the angle-incidence equations. A bare assertion that ray parameters eliminate is insufficient.
- Correctly use directed secant power. The signs of `MA*MP` and `NA*NQ` depend on whether the second intersections lie on the segments or extensions; the displayed `AB*AP-AC*AQ` formula must be derived under one declared signed-length convention.
- Handle a side tangent to the circle (coincident second intersection), an intercept at infinity, and zero-power midpoint cases without illegal division, or prove these cannot occur from the hypotheses.
- Continue to exclude the false identities derived from alleged `B,C,K,L` cyclicity.

## Field ranking and selection

All four new whole-problem approaches were registered. The evidence-based order is:
1. `oriented-determinant-elimination` — explicit parametrization and explicit algebraic target, numerically checked; Elo 1516.0.
2. `antipode-quarter-turn` — excellent exact reduction but an unexpanded cancellation lemma; Elo 1500.7363.
3. `sine-product-antipode` — plausible synthetic analogue with no exact product yet; Elo 1500.0338.
4. `inverted-circle-intercepts` — distinct but its claimed simplification under inversion is currently speculative; Elo 1483.2299.

Pairwise ranking updates used the first over the second, the second over the third, and the third over the fourth. Build the strongest analytic route and the two antipode formulations in parallel: they have different algebraic organizations and can reveal whether the hoped-for telescoping is real. Defer inversion until its intercept lemma has an explicit formula.

build set: oriented-determinant-elimination, antipode-quarter-turn, sine-product-antipode