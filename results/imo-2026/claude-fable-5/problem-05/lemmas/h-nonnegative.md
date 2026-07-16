# Lemma: h-nonnegative

**Status:** certified (round 1, proof-reviewer). Archimedean orbit-escape argument checked; depends only on `orbit-invariance` (functional-equation hypothesis) and the codomain ℝ_{>0}.

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy f(f(y)) = 2f(y) − y for all y > 0 (e.g. any solution of the problem's double inequality, by lemma `fe-double-iterate`). Then h(y) := f(y) − y ≥ 0 for all y > 0. Consequently every forward orbit {y + n·h(y) : n ≥ 0} (lemma `orbit-invariance`) is non-decreasing, and if h(y) > 0 it is strictly increasing and unbounded above.

**Proof.** Suppose h(y₀) < 0 for some y₀ > 0. By lemma `orbit-invariance`, fⁿ(y₀) = y₀ + n·h(y₀) for all n ≥ 0, and fⁿ(y₀) ∈ ℝ_{>0}. By the Archimedean property of ℝ there is an integer n with n > y₀/(−h(y₀)); for that n,
```
fⁿ(y₀) = y₀ − n·(−h(y₀)) < y₀ − y₀ = 0,
```
contradicting fⁿ(y₀) > 0. Hence h(y) ≥ 0 for all y > 0. The consequences are immediate from the arithmetic-progression form of the orbit: step h(y) ≥ 0 gives a non-decreasing sequence; step h(y) > 0 gives a strictly increasing sequence with fⁿ(y) = y + n·h(y) → ∞. ∎

**Where proved:** `results/imo-2026-05/approaches/orbit-forbidden-zone.md`, Step 2.3.
