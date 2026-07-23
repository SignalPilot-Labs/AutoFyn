# Approach: tangent-envelope

## Status
partial

## Approaches tried
- Round-1 outline: reframe the two original inequalities as a two-sided envelope of explicit curves pinching the graph of f, both tangent with slope 1 at every point of range(f); propagate near-constancy of d = f − id locally and then globally. Slopes-at-tangency computed; the anchor-density gap is explicitly open.

## Current best
Skeleton below; tangency computation done, density-of-anchors step open.

## Target
Determine all f: R_{>0} → R_{>0} with sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y)) for all x,y > 0.
**Answer to prove: exactly the family f(x) = x + c, c ≥ 0 a constant.**

## Technique
Supporting-curve / envelope geometry (the "supporting line ⟹ affine" mechanism of crux aimo-0089, adapted from lines to tangent curves): for each fixed y the chain gives explicit lower and upper curves for f, which TOUCH the graph at x = f(y) with common slope 1; the graph is trapped in a quadratically thin wedge of slope 1 around every range point, forcing d to be locally almost-constant near range points, then globally constant. KB: "Standard inequalities", "Sum of squares / completing the square", "Functional equations".

## Proof skeleton

1. **Sufficiency.** f(x) = x + c, c ≥ 0: both squared inequalities reduce to (x − y − c)² ≥ 0. — direct computation.

2. **Core identity + f ≥ id.** x = f(y) collapses the chain to f(f(y)) = 2f(y) − y; orbit APs + positivity give d := f − id ≥ 0. — squeeze collapse + AP positivity (shared with sibling approaches; certify as a lemma).

3. **Envelope.** For every fixed y > 0, the original chain says, for ALL x > 0:
   L_y(x) := 2√(x·f(y)) − y ≤ f(x) ≤ √(2(x² + f(y)²)) − y =: U_y(x).
   Both bounds pass through the SAME graph point: at x₀ = f(y), L_y(x₀) = 2f(y) − y = f(f(y)) = U_y(x₀) (by step 2). So the graph of f touches both envelope curves at (x₀, f(x₀)) for every x₀ ∈ range(f). — rearranging the chain + step 2.

4. **Slope-1 tangency ⟹ quadratic pinch at range points.** With B = f(y), x₀ = f(y): L_y'(x₀) = √(B/x₀) = 1 and U_y'(x₀) = 2x₀/√(2(x₀² + B²)) = 1. Second-order expansion (exact inequalities, not calculus limits — e.g. 2√(xB) ≥ x + B − (x−B)²/(4·min(x,B)) and the analogous upper estimate for U_y) gives constants such that for all x in a neighborhood scale of x₀:
   **|d(x) − d(x₀)| ≤ C·(x − x₀)²/x₀ for every anchor x₀ ∈ range(f)** (C absolute).
   — because both envelope curves have slope 1 and curvature O(1/x₀) at the touching point, and the graph is squeezed between them.

5. **GAP (open): anchors are dense enough to chain.** To conclude, need: every interval [a, b] ⊂ R_{>0} can be subdivided by points of range(f) with mesh → 0 (or any weaker statement letting the quadratic errors telescope to 0). Candidate mechanisms to try, in order:
   - range(f) ⊇ every forward orbit {y + n·d(y)}, and each anchor x₀ pins d on an interval around x₀ of definite relative length (from step 4 with the explicit C) — cover [a, b] by finitely many such intervals with matching d-values;
   - show inf range(f) = inf f and that range is "syndetic" (bounded gaps ≤ sup local d), using d(f(y)) = d(y);
   - or bypass density: apply step 4 with anchor x₀ = f(y') and target x = f(y'') both range points and compare with the marching-orbit placement.
   — this is the load-bearing unproved step of this approach.

6. **Chaining.** Given step 5, telescope step 4 along a mesh-ε subdivision of [a, b]: |d(a) − d(b)| ≤ Σ C·(Δ_i)²/a ≤ C·ε·(b−a)/a → 0, so d ≡ c constant; c ≥ 0 by step 2. With step 1, answer = {x + c : c ≥ 0}.

## Open gaps (builder fills)
- Step 5 entirely (the density/chaining lemma) — the crux of this route.
- Step 4's exact second-order inequalities with explicit constants (no calculus hand-waving: use algebraic inequalities like (√x − √B)² ≥ 0 rearrangements).
- Steps 1–2 full write-up (shareable lemma).

## Cases to cover
None (no dichotomy) unless step 5 is resolved via the d ∈ {0, c} dichotomy, in which case inherit the mixed-case analysis.

## Watch out for
- f is NOT assumed continuous/monotone — "curvature" talk in step 4 must be replaced by exact algebraic two-sided inequalities.
- The pinch of step 4 is anchored at x₀ ∈ range(f) only; d at points off the range is controlled only through the envelope, not directly.
- Note: sibling approach two-point-pinch achieves an anchor-free version of the same quadratic pinch by substituting x = f(y') algebraically; if that route closes first, this approach is redundant — keep it only while two-point-pinch is unverified.
