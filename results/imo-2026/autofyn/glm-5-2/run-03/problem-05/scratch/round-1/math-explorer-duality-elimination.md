## imo-2026-05

Determine all `f : R_{>0} -> R_{>0}` with
`sqrt((x² + f(y)²)/2) >= (f(x)+y)/2 >= sqrt(x f(y))` for all `x,y>0`.

### Conjectured answer (verified by construction, not yet proved unique)

**`f(x) = x + c` for an arbitrary constant `c >= 0`.** Numerics: every perturbation of `g(t)=f(t)-t` (linear `a·x+c` with `a≠1`, sinusoidal `c+ε·sin(log x)`, discontinuous step `g`, `g=x^p`, etc.) violates the inequality; only `g ≡ c ≥ 0` survives on a log-spaced grid spanning `1e-4 .. 1e4`. The affine family `f(x)=a x + c` collapses to `a=1` (the (L) quadratic in `t=x/y`, `(2-a²)t² - 2a t + (2a²-1) >= 0` for all `t>0`, forces discriminant `<= 0` i.e. `2(a²-1)² <= 0`, so `a=1`).

**Construction (rigorous):** For `f(x)=x+c`, `c>=0`, set `A=(f(x)+y)/2=(x+y+c)/2`. (L) is `QM-AM` on the pair `(x, y+c)`; (R) is `AM-GM` on the pair `(x, y+c)`. Both hold with `x>0, y+c>0`, i.e. `c>=0` (need `y+c>0` for all `y>0`). For `c<0` the codomain fails (`f(x)=x+c<0` for small `x`). So `c>=0`. Construction fully verified.

### The single hardest gap

**Forcing `g(t) := f(t) - t` to be constant (the converse).** This is the entire open problem; once `g` is constant the construction + the `c>=0` codomain check finishes. Equivalently: prove `A := (f(x)+y)/2` equals `B := (x+f(y))/2` (the natural AM of the pair `(x,f(y))`); then `f(x)-x = f(y)-y` for all `x,y`.

**The dispatch's proposed AM-GM chain is NOT airtight — flag this to the outliner.** The dispatch suggests: "AM-GM gives `(f(x)+y)/2 >= sqrt(f(x)·y)` always; combining with the required `>= sqrt(x·f(y))` suggests `f(x)·y >= x·f(y)`, i.e. `f(x)/x >= f(y)/y`, forcing constancy." This reasoning is **invalid**: `(f(x)+y)/2 >= sqrt(x f(y))` (required) and `(f(x)+y)/2 >= sqrt(f(x) y)` (AM-GM) are *two lower bounds on the same quantity*; both holding does NOT order `sqrt(x f(y))` vs `sqrt(f(x) y)`. You only get `A >= max(sqrt(x f(y)), sqrt(f(x) y))`, which yields no comparison between `f(x)/x` and `f(y)/y`. The outliner must find a different forcing argument.

### Distinct openings (rival framings for the converse)

1. **Interval-collapse at `x = f(y)` (equality-forcing substitution).** For the pair `(x, f(y))` the natural chain is `QM >= AM = B >= GM`. The problem replaces `B` with `A`, demanding `A ∈ [GM(x,f(y)), QM(x,f(y))]`. This interval degenerates to a single point **iff `x = f(y)`** (QM=AM=GM iff the two entries are equal). Setting `x = f(y)` forces `A = f(y)`, i.e. `(f(f(y))+y)/2 = f(y)`, giving the FE `f(f(y)) = 2f(y) - y`, equivalently `g(y + g(y)) = g(y)` (invariance of `g` along `f`-orbits, which advance by the constant step `g(y_0)`).
   - **Caveat (do not over-trust):** This FE is NECESSARY but NOT SUFFICIENT. It has many nonconstant solutions: partition `R_{>0}` into `f`-orbits (arithmetic progressions) and assign each orbit a different constant step `h_o`, with `h_o + y > 0`. All such `f` satisfy the FE but (numerically) violate the full off-diagonal inequality. So the FE alone does not close the gap; the universal `(x,y)` quantification must be used on top.

2. **Squeeze / extremize-one-variable (attacks the gap directly).** Treat (R) as a family of upper bounds on `f(y)`: `f(y) <= (f(x)+y)² / (4x)` for every `x>0`, so `f(y) <= inf_{x>0} (f(x)+y)²/(4x)`. Treat (L) as lower bounds: `2(x²+f(y)²) >= (f(x)+y)²` gives `f(y)² >= ((f(x)+y)²/2 - x²)` (when the radicand is positive), so `f(y) >= sup_{x} sqrt((f(x)+y)²/2 - x²)`. Squeezing these against each other (and using the `x=f(y)` FE to control `f(x)`) is the natural route to `f(y) = y + c`. This is the off-diagonal lever the FE lacks.

3. **Swap-and-chain (cross-inequalities from nonempty interval intersection).** Both `A=(f(x)+y)/2` and `B=(x+f(y))/2` must lie in BOTH intervals `I₁=[GM(x,f(y)), QM(x,f(y))]` and `I₂=[GM(y,f(x)), QM(y,f(x))]` (`A` forced into `I₁` by (L)+(R), `A` natural (as AM of `(y,f(x))`) in `I₂`; `B` the mirror). Nonemptiness of `I₁ ∩ I₂` plus the requirement that it contain BOTH `A` and `B` yields the cross-inequalities `2 x f(y) <= y² + f(x)²` and `2 y f(x) <= x² + f(y)²` for all `x,y`. These are NONTRIVIAL (NOT pure AM-GM: AM-GM only gives `y²+f(x)² >= 2y f(x)`, not `>= 2x f(y)`). Whether these cross-inequalities (plus the `x=f(y)` FE) force `g` constant is the open technical question for the outliner — a candidate for the real crux move.

4. **Equality-case analysis of the full QM-AM-GM chain.** The whole problem is "QM ≥ A ≥ GM of the pair `(x,f(y))`, with `A` a stranger to the pair." Whenever the interval `[GM, QM]` is forced tight by an extremal substitution, equality pins `A` to the AM `B`, giving `g(x)=g(y)`. The only interval-collapse is `x=f(y)` (opening 1); a second, non-collapse equality-forcer (e.g. a limiting `y → 0+` or a fixed-point argument) is what this opening still needs — the outliner should look for a second extremal substitution that forces equality, since a single equality-forcer leaves `g` merely orbit-invariant.

### Cheap-kill candidates

- **Affine reduction (done):** the discriminant argument on `f(x)=a x + c` kills `a≠1` in one move; gives the answer's *shape* `f=x+c` and the construction.
- **Codomain bound:** `c >= 0` is a free kill from `f(x)>0` for all `x>0` (any `c<0` fails at small `x`).
- **The `x=f(y)` FE:** one-move kill yielding `g(f(y))=g(y)` — but it is only a *necessary* lemma, not the converse.

### Candidate technique(s)

- **QM-AM-GM chain reinterpretation** (the inequality IS the chain of the pair `(x, f(y))` with `AM` replaced by `A=(f(x)+y)/2`; equality-case analysis of QM-AM-GM pins structure). Knowledge-base entry: "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration."
- **Functional-equation crux:** the `x=f(y)` substitution produces `f(f(y))=2f(y)-y` (a second-iterate FE); knowledge_base "Functional equations: test special values, check injectivity/surjectivity."
- **Pólya "Specialize":** plug `x=f(y)` (the equality-case-forcing specialization) — knowledge_base heuristics.
- **Squeeze / two-sided bound** (opening 2) — general "Direct proof" chaining.

### Knowledge-base entries to use

- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration." (Algebra & Polynomials) — the load-bearing technique; equality case `x=f(y)` collapses the chain.
- "Functional equations: test special values, check injectivity/surjectivity." — for the `x=f(y)` specialization and iterating `f(f(y))=2f(y)-y`.
- Pólya heuristics: "Specialize: plug in extreme or symmetric values" and "Check the answer: verify edge cases."
- "Direct proof" / "Contradiction" (General Proof Methods) — for the squeeze/forcing step.

### Analogous past problems (cruxes)

- **`aimo-0190`** (functional-equations) — "Pin a Cauchy-additive function to linear by exhibiting one-sided boundedness on a ray, obtained from a square identity" and "Collapse a functional equation into Cauchy's additive equation by applying it to a variable and its negation as two paired substitutions and adding the results to cancel the cross terms." Analogous because the goal there is the same shape — reduce a FE to `f(x)=x` (here `f(x)=x+c`) by exploiting a symmetry/paired substitution and a one-sided bound. Crux move: collapse-to-additive + one-sided boundedness pins linear. **Adapt (not cite):** the `x=f(y)` FE `g(f(y))=g(y)` is the analogous "collapse" step; the missing piece is the analogue of "one-sided boundedness on a ray" — here, an off-diagonal squeeze that bounds `g` from both sides.
- **`aimo-0321`** (functional-equations) — "Substitute a special argument into a two-term FE to force a reflection symmetry that merges the two terms into one" and then "Evaluate a multiplicative function on a square root to force a nonnegative value and eliminate the negative sign branch." Analogous in structure: a clever specialization merges two branches and pins the function pointwise. Crux move: the specialization that collapses the equation. **Adapt:** `x=f(y)` is our collapse-specialization; the remaining task is the "eliminate the unwanted branch" step (kill nonconstant orbit-invariant `g`).
- **`aimo-0288`** (inequalities-SOS-and-convexity) — "Upgrade a non-strict chained bound to strict by intersecting the equality conditions of BOTH bounding steps and showing their conjunction forces the excluded hypothesis." Analogous because the whole inequality is a non-strict `QM >= A >= GM` chain and the conclusion `g` constant is an *equality* conclusion; the move is to intersect equality conditions. Crux move: intersect equality conditions of both bounds. **Adapt:** here the equality condition of the `QM >= AM >= GM` chain is `x=f(y)`; intersecting the equality conditions across the universal `(x,y)` quantifier is the (still-open) forcing step.

No crux in the corpus is a direct match for a QM-AM-GM-sandwich functional inequality; the three above are the closest by *move type*, not by surface.

### Prior progress

Round 1, empty workspace — no approaches, no lemmas. This is the first exploration.

### Dead ends (do not retry)

- **`f(x) = a x` (multiplicative linear), `a ≠ 1`:** fails (L); discriminant argument shows only `a=1` works. Don't retry the multiplicative family.
- **Discontinuous / piecewise-constant `g`:** fails (L) on the grid (e.g. step `g` at `x=1` gives violation `~0.05`). The FE `g(f(y))=g(y)` admits such solutions, but the full inequality rejects them — so a proof relying on the FE alone cannot succeed.
- **The dispatch's AM-GM ratio chain `f(x)/x >= f(y)/y`:** logically invalid (two lower bounds on one quantity do not order). Do not build an approach on it.
- **The diagonal `x = y`:** gives the QM-AM-GM chain of the pair `(x, f(x))`, which holds for ALL `f` — no information. Don't specialize on the diagonal.

### Small-case / intuition notes (conjecture, labeled)

- **Conjecture (strong, numerically robust):** the full solution set is exactly `{f(x) = x + c : c >= 0}`. Tested `f=x+c` for `c ∈ {0, 0.001, 0.5, 1, 5, 1000}` — all pass with zero worst-violation on the grid; all affine `a x + c` with `a≠1` fail (L) (and `a<1` also fails (R)); all perturbations `x + c + ε·(sin(log x), linear, sqrt, piecewise)` fail.
- **Conjecture on the gap:** the correct forcing argument is likely opening 3 (the cross-inequalities `2xf(y) <= y²+f(x)²` and `2yf(x) <= x²+f(y)²` from nonempty `I₁ ∩ I₂`) layered on top of the `x=f(y)` FE — these cross-terms are the only genuinely non-AM-GM constraints and are where the off-diagonal information lives. The outliner should verify whether these cross-inequalities, combined with `g(f(y))=g(y)`, actually pin `g` constant (this was NOT closed by exploration — it is the open question).
