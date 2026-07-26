# fixed-point-zero-region

*Certified by proof-reviewer, round 1. Proven in `results/imo-2026-05/approaches/orbit-close-encounter.md`, Step 4.*

## Statement

Under the hypotheses of `iterate-and-orbit`, suppose `g : ℝ₊ → {0, c}` for some `c > 0` (i.e. `g` takes at most one positive value, by the conclusion of Part A — see `two-point-g-constraint` and the close-encounter argument). If a fixed point `x_0` (`g(x_0) = 0`) exists, then:

1. **(dagger) Global quadratic upper bound:** `g(y) ≤ (y − x_0)² / (4 x_0)` for all `y > 0`.
2. **Zero-region:** Every fixed point `s` has an open zero-neighbourhood `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊` on which `g = 0`. In particular, the fixed-point set `S := {y > 0 : g(y) = 0}` is open.
3. **Component argument:** The connected component of `S` containing `x_0` is `(0, ∞)` (by boundary-push: `α → 0` and `β → ∞`). Hence `S = ℝ₊`, i.e. `g ≡ 0`, contradicting `c > 0`.

**Conclusion.** A fixed point and a positive value of `g` cannot coexist. (If a fixed point exists, `g ≡ 0`.)

## Proof

**(dagger):** Substitute `x = x_0` (with `g(x_0) = 0`) into `(star)` (`two-point-g-constraint`):

`4 x_0 g(y) ≤ (x_0 − y)² + 2(x_0 + y)·0 + 0² = (y − x_0)²`.

So `g(y) ≤ (y − x_0)² / (4 x_0)`.

**Zero-region:** Let `s > 0` be any fixed point (`g(s) = 0`). By `(dagger)` with `x_0 → s`: `g(y) ≤ (y − s)² / (4 s)`. If `|y − s| < 2√(cs)`, then `(y − s)² / (4s) < (4cs)/(4s) = c`, so `g(y) < c`. Since `g(y) ∈ {0, c}`, this forces `g(y) = 0`. So `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊ ⊆ S`. Every point of `S` has such an open interval, so `S` is open.

**Component argument:** Let `I = (α, β)` be the connected component of the open set `S` containing `x_0`.

- `β = ∞`: If `β < ∞`, then `β ≥ x_0 + 2√(cx_0) > 0`. Pick `s ∈ I` near `β` from below. The interval `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊ ⊆ S` is connected, contains `s ∈ I`, hence ⊆ `I`. But `s + 2√(cs) → β + 2√(cβ) > β` as `s → β⁻`, so points of `I` lie right of `β` — contradiction.
- `α = 0`: If `α > 0`, pick `s ∈ I` near `α` from above. The interval `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊ ⊆ S` ⊆ `I` extends to `s − 2√(cs) → α − 2√(cα) < α` as `s → α⁺`, so points of `I` lie left of `α` — contradiction.

So `I = (0, ∞)`, hence `S = ℝ₊`, hence `g ≡ 0` — contradicting `c > 0`. ∎
