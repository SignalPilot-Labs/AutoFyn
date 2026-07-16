# Lemma: onepos-right

**Status:** certified (round 1, proof-reviewer; proposed by proof-builder for `right-spreading-fixed-points`). Exact expansion (EXP) re-verified symbolically; chase indices and thresholds checked.

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy the right inequality (f(x) + y)/2 ≥ √(x·f(y)) for all x, y > 0 and the functional equation f(f(y)) = 2f(y) − y (lemma `fe-double-iterate`). Then h := f − id takes at most one positive value.

**Proof.** Suppose h(x₀) = a and h(y₀) = b with 0 < a < b. By lemma `orbit-invariance`, xₘ := fᵐ(x₀) = x₀ + m·a with h(xₘ) = a, and yₙ := fⁿ(y₀) = y₀ + n·b with h(yₙ) = b, for all integers m, n ≥ 0.

Choose an integer n ≥ 0 with yₙ ≥ x₀ and yₙ > a²/(b − a) (possible: n = max(0, ⌈(x₀ − y₀)/b⌉, ⌊(a²/(b − a) − y₀)/b⌋ + 1)). Set m := ⌈(yₙ − x₀)/a⌉ ≥ 0; then yₙ ≤ xₘ < yₙ + a. Put x := xₘ and s := x − yₙ ∈ [0, a).

Both sides of the right inequality at (x, yₙ) are positive, so it is equivalent to (f(x) + yₙ)² ≥ 4x·f(yₙ), i.e. (x + a + yₙ)² ≥ 4x(yₙ + b). Substituting x = yₙ + s and expanding exactly:
```
LHS − RHS = 4yₙ(a − b) + (s + a)² − 4sb.
```
Since 0 ≤ s < a: (s + a)² < 4a² and −4sb ≤ 0; and 4yₙ(a − b) = −4yₙ(b − a) < −4a² by yₙ > a²/(b − a). Hence LHS − RHS < −4a² + 4a² = 0, contradicting the right inequality. ∎

**Where proved:** `results/imo-2026-05/approaches/right-spreading-fixed-points.md`, Step 2.5'.
