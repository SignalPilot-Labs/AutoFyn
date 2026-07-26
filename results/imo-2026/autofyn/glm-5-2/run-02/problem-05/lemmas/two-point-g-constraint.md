# two-point-g-constraint

*Certified by proof-reviewer, round 1. Proven in `results/imo-2026-05/approaches/orbit-close-encounter.md`, Step 2.*

## Statement

Under the hypotheses of `iterate-and-orbit` (i.e. `f : ℝ₊ → ℝ₊` satisfies (P), `g := f − id`), the squared right inequality of (P) is equivalent, for all `x, y > 0`, to:

> **(`star`)** `4x·g(y) ≤ (x−y)² + 2(x+y)g(x) + g(x)²`.

Swapping `x ↔ y` gives:

> **(`star star`)** `4y·g(x) ≤ (x−y)² + 2(x+y)g(y) + g(y)²`.

**Level-set tautology.** Within a level set `g(x) = g(y) = c`, `(star)` reduces to the tautology `(x − y − c)² ≥ 0`. So `(star)` carries no information within a single level set; all content is across distinct level sets.

## Proof

Square the right inequality of (P): `(f(x)+y)/2 ≥ √(x·f(y))` gives `(f(x)+y)² ≥ 4x·f(y)`. Substitute `f(t) = t + g(t)`:

LHS = `(x + g(x) + y)² = (x+y)² + 2(x+y)g(x) + g(x)² = x² + 2xy + y² + 2(x+y)g(x) + g(x)²`.

RHS = `4x(y + g(y)) = 4xy + 4x·g(y)`.

Subtract `4xy`: `(x−y)² + 2(x+y)g(x) + g(x)² ≥ 4x·g(y)`. This is `(star)`.

`(star star)` is obtained by exchanging `x ↔ y` (valid since (P) holds for all `x, y > 0`).

**Level-set tautology:** with `g(x) = g(y) = c`, RHS of `(star)` − `4xc` = `(x−y)² + 2(x+y)c + c² − 4xc` = `(x−y)² − 2c(x−y) + c²` = `(x − y − c)² ≥ 0`.
