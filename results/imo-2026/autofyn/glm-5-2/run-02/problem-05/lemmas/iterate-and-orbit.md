# iterate-and-orbit

*Certified by proof-reviewer, round 1. Proven in `results/imo-2026-05/approaches/orbit-close-encounter.md`, Step 1.*

## Statement

Let `f : ℝ₊ → ℝ₊` satisfy

$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}\qquad(\forall x,y>0).\tag{P}$$

Set `g(x) := f(x) − x`. Then:

1. **Iterate identity:** `f(f(y)) = 2f(y) − y` for all `y > 0`.
2. **Orbit invariance:** `g(f(y)) = g(y)` for all `y > 0`.
3. **Forward orbits are APs:** `fⁿ(y) = y + n·g(y)` for all `n ≥ 0`.
4. **Non-negativity:** `g(y) ≥ 0` for all `y > 0` (i.e. `f ≥ id`).
5. **Injectivity:** `f` is injective.

## Proof

**Substitute `x = f(y)` into (P).** The LHS becomes `√((f(y)²+f(y)²)/2) = f(y)`, the RHS becomes `√(f(y)·f(y)) = f(y)`. The middle `(f(f(y))+y)/2` is sandwiched: `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`, forcing `f(f(y)) = 2f(y) − y`. (Parts 1.)

**Part 2:** `g(f(y)) = f(f(y)) − f(y) = (2f(y)−y) − f(y) = f(y) − y = g(y)`.

**Part 3:** By induction. Base `n=0`: `f⁰(y) = y = y + 0·g(y)`. Step: `f^{n+1}(y) = f(fⁿ(y)) = fⁿ(y) + g(fⁿ(y)) = (y + n·g(y)) + g(y) = y + (n+1)·g(y)`, using Part 2.

**Part 4:** If `g(y) < 0`, then `fⁿ(y) = y + n·g(y) → −∞` as `n → ∞`, so `fⁿ(y) ≤ 0` for large `n`, contradicting `f : ℝ₊ → ℝ₊` (the forward orbit must stay in `ℝ₊`).

**Part 5:** If `f(a) = f(b)`, apply `f`: `f(f(a)) = f(f(b))`, so by Part 1 `2f(a) − a = 2f(b) − b`. Since `f(a) = f(b)`, `a = b`.
