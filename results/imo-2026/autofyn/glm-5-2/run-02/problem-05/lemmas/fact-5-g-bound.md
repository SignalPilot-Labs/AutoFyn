# fact-5-g-bound

*Certified by proof-reviewer, round 1. Proven in `results/imo-2026-05/approaches/gm-lipschitz-partition.md`, Step 3.*

## Statement

Under the hypotheses of `iterate-and-orbit` (i.e. `f : ℝ₊ → ℝ₊` satisfies (P), `g := f − id`), for all `y, z > 0`:

$$\bigl|\,g(z) - g(y)\,\bigr| \;\le\; \bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2.$$

## Proof

Substitute `x = f(z)` (valid: `f(z) > 0`) into the RHS inequality of (P): `(f(f(z)) + y)/2 ≥ √(f(z)·f(y))`.

By the iterate identity (`iterate-and-orbit`), `f(f(z)) = 2f(z) − z = f(z) + g(z)`. Also `y = f(y) − g(y)`. So the LHS equals

$$\frac{f(z) + g(z) + f(y) - g(y)}{2} = \operatorname{AM}\bigl(f(z), f(y)\bigr) + \frac{g(z) - g(y)}{2}.$$

The RHS is `GM(f(z), f(y))`. Therefore

$$\frac{g(z) - g(y)}{2} \;\ge\; -\bigl(\operatorname{AM}-\operatorname{GM}\bigr)\bigl(f(z), f(y)\bigr).$$

By the AM-GM identity `2(AM − GM)(a, b) = (√a − √b)²` (i.e. `(a+b)/2 − √(ab) = (√a − √b)²/2`), the RHS is `−(√f(z) − √f(y))²/2`. So

$$g(z) - g(y) \;\ge\; -\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2. \tag{F5+}$$

Swapping `y ↔ z` (substitute `x = f(y)` instead) gives

$$g(y) - g(z) \;\ge\; -\bigl(\sqrt{f(z)} - \sqrt{f(y)}\bigr)^2. \tag{F5-}$$

Combining (F5+) and (F5-): `|g(z) − g(y)| ≤ (√f(z) − √f(y))²`. ∎

## Note

This is a Lipschitz-type self-referential bound on `g` via the gap of `√f`. It is derived purely from the RHS (GM) inequality of (P) and the iterate identity. The LHS (RMS) inequality gives a parallel but weaker one-sided bound and carries no additional uniqueness information beyond Step 1.
