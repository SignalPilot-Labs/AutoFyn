# Proof-builder report — two-regime-disjunctive (round 2, imo-2026-03)

## What I proved (rigorous, in `results/imo-2026-03/approaches/two-regime-disjunctive.md`)

1. **`U(1)` (the corrected two-mode upper bound)** — fully rigorous. The regime boundary is **dyadic vs non-dyadic** (per reviewer F2), not dominant vs non-dominant. Bisect mode (`x ≤ 1/3 = α(1)`, `Liu = (1+x)/2 ≤ 2/3`) + sliver mode (`x ≥ 1/3`, `Liu = 1−x ≤ 2/3`); threshold `x = 1/3 = α(1)` is the dyadic, where both give `2/3`. Strict for `x ≠ 1/3`. The sliver mode handles `x ∈ (1/3, 1/2]` which IS dominant — confirming the reviewer's F2 point.

2. **`U(2)` (NEW — four-strategy upper bound)** — fully rigorous. Closed the previously-open `U(2)`. Four explicit Xiang strategies against Liu config `(a, b, c)`, `a ≤ b ≤ c`:
   - **A** (match 2nd-largest in largest): `Liu = (1+a)/2` (exact).
   - **B** (bisect largest + sliver): `Liu → (1+b−a)/2` (infimum).
   - **C** (split smallest into halves + sliver): `Liu → (1+c−b)/2` (infimum).
   - **E** (match 2nd-largest in largest + sliver from smallest): `Liu → max(c, 1−c)` (infimum).
   
   The inequality `min(A, B, C, E) ≤ 4/7 = f(2)` is a clean `4`-way contradiction: if all four `> 4/7` then `a > 1/7 ∧ b−a > 1/7 ∧ c−b > 1/7`, giving `c > 3/7` hence (iv) forces `c > 4/7`, but then `a + b = 1−c < 3/7` while `b > a+1/7 > 2/7` forces `a+b > 3/7` — contradiction. Equality forces `(a,b,c) = (1/7, 2/7, 4/7)` (the dyadic). All four strategy formulas verified exactly by rational arithmetic (`/tmp/verify_four2.py`); the bound `min ≤ 4/7` with equality iff dyadic verified over a `D=200` grid.

3. **Regime D (dyadic), all `n ≥ 1` — the equality/attainment upper bound** — imported (certified pair-pile lemma), restated for self-containment. `A = α(n)`, `Liu = f(n)` exactly.

4. **Combined with round-1-certified `L(1), L(2)`**, this gives **`c(1) = 2/3` and `c(2) = 4/7` rigorously end-to-end** (both bounds).

## What gaps remain (honest)

1. **Regime N for `n ≥ 3` (the headline open gap).** The `n=2` four-strategy proof does not lift to a clean induction: each strategy (`A, B, C, E`) is `n=2`-specific (consumes 2 marks in a particular pattern; the `n=2` case analysis is a 4-way contradiction in 3 variables with no obvious `(2^n−1)`-way generalization). The conjecture "non-dyadic ⟹ `Liu < f(n)`" is strongly supported numerically for `n=3` (dyadic `(1,2,4,8)/15` → min-oddsum exactly `8/15`; every tested non-dyadic `n=3` config strictly less), but NO analytic proof for `n ≥ 3`. **Do not claim it is proven.**

2. **Lower bound Lemma L general `n`.** Imported as a dependency from the sibling `pairing-partner` (single-aux `L*(n)` closes `k=1`; `k≥2` open there). `c(n) ≥ f(n)` for `n ≥ 3` not established by this approach.

## Spec concerns / reviewer-facing notes

- **F1 (regime-N mechanism was FALSE): ADDRESSED.** The false claim "non-dominant ⟹ `A ≤ 0` (Liu ≤ 1/2)" is replaced by the actual mechanism: four pile-matching + sliver strategies whose infimum is bounded above by `4/7` (for `n=2`) via a 4-way contradiction. No claim of `A ≤ 0` is made. The strict slack `4/7 − min(A,B,C,E)` for non-dyadic configs is a small positive number (consistent with the reviewer's "≈ 0.503–0.525" finding), NOT `4/7 − 1/2 = 1/14`.
- **F2 (regime boundary): ADDRESSED.** Regimes redefined as dyadic vs non-dyadic; the `n=1` two-mode base falls out cleanly (threshold `x = 1/3 = α(1)`).
- **F3 (regime-D rescaling circular): ADDRESSED.** Regime D restricted to the dyadic config itself (the genuine equality/attainment case), where the certified pair-pile fires. All non-dyadic configs (dominant or not) are handled by regime N. The rescaling argument is NOT invoked for arbitrary dominant configs.
- **Sliver strategies give infima, not attained values.** For non-dyadic configs, `min < 4/7` strictly (by the equality analysis), so Xiang picks a small-enough sliver `s > 0` to achieve `Liu < 4/7` concretely. At the dyadic (where all four infs `= 4/7`), the pair-pile attains exactly `4/7`. So the upper bound `Liu ≤ f(n)` is attained as required.

## New lemma proposed for certification

**Lemma `U(2)` — four-strategy upper bound, equality iff dyadic** (candidate file `results/imo-2026-03/lemmas/lemma-u2-four-strategy.md`, to be written if the reviewer approves). Statement and full proof in Section 4 of the approach file. This closes `U(2)` (previously open) and, with `L(2)` (round-1 certified), pins `c(2) = 4/7` rigorously. Reviewer is asked to (a) verify the four strategy formulas by direct construction (python check provided), (b) verify the 4-way contradiction argument and the equality-forces-dyadic analysis.

## Per-role rule learned

ALWAYS: when a reviewer flags a load-bearing lemma as "verified FALSE" with a concrete counterexample (here: non-dominant `n=2` configs give cap `≈ 0.503–0.525 > 1/2`, falsifying "regime-N ⟹ `A ≤ 0`"), re-derive the actual mechanism numerically BEFORE writing the proof — the correct bound (`4/7` for `n=2`) was still true, but via a completely different argument (pile-matching + slivers, not pairing-to-zero). The false mechanism would have wasted the whole build. (round 2, imo-2026-03, F1.)

NEVER: conflate "the bound holds" with "the bound holds via this mechanism" — the `n=2` upper bound `≤ 4/7` is true, but the outliner's claimed mechanism (greedy pairing drives pair-excesses `≤ 0`) was false; a verification of the VALUE is not a verification of the PROOF. Always separately verify the mechanism. (round 2, imo-2026-03, F1.)
