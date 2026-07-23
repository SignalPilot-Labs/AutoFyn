## imo-2026-05

- **IMPORTANT correction to run_state.md's conjecture**: run_state.md guesses "f(x)=x is likely the only solution." This is **wrong** — I verified algebraically (sympy, exact) that **f(x) = x + c satisfies both inequalities for EVERY constant c ≥ 0**, not just c=0. The true answer is (conjecturally, pending the uniqueness half) the one-parameter family `f(x) = x + c, c ≥ 0`. The outliner must build the proof around this family, not around f=identity alone.

### Distinct openings
1. **x=y substitution is a dead end / vacuous.** Setting x=y makes the middle term `(f(x)+x)/2` exactly the AM of the pair `(x,f(x))`, while the outer terms are exactly QM and GM of that same pair. So the whole chain reduces to the trivial universal fact QM ≥ AM ≥ GM applied to `(x,f(x))` — true for *every* function f, no information gained. Do not waste an approach slug on "x=y forces f(x)=x"; it doesn't.
2. **x = f(y) substitution is the load-bearing move.** Plug x=f(y) into each half of the inequality separately:
   - Right half `(f(x)+y)^2 ≥ 4x f(y)` at x=f(y): `(f(f(y))+y)^2 ≥ 4f(y)^2` ⟹ `f(f(y)) ≥ 2f(y) - y`.
   - Left half `2x^2+2f(y)^2 ≥ (f(x)+y)^2` at x=f(y): `4f(y)^2 ≥ (f(f(y))+y)^2` ⟹ `f(f(y)) ≤ 2f(y) - y`.
   - Combined: **`f(f(y)) = 2f(y) - y` exactly, for all y > 0.** This is a clean, rigorously derived necessary condition (no hand-waving, both directions used).
3. **Orbit/arithmetic-sequence argument.** Iterating f from any x: `x_0=x, x_{n+1}=f(x_n)`, the relation `f(f(y))=2f(y)-y` applied along the orbit gives `x_{n+1}-x_n = x_n - x_{n-1}` for all n, i.e. `x_n` is an *arithmetic* sequence: `x_n = x + n(f(x)-x)`. Since every `x_n` must stay in `R_{>0}` for all n≥0 (f's codomain), the common difference `d=f(x)-x` cannot be negative (else `x_n → -∞`). **This forces `f(x) ≥ x` for every x.**
4. **Injectivity is free.** From `f(f(y))=2f(y)-y`, if `f(a)=f(b)` then `f(f(a))=f(f(b))` ⟹ `2f(a)-a=2f(b)-b` ⟹ `a=b` (since f(a)=f(b)). So f is injective — a one-line consequence, worth stating but not by itself enough to finish.
5. **The scaling family is ruled out, sharpening the target.** I tested f(x)=kx (pure scaling) symbolically: the right-hand inequality factors as `(kx-y)^2 ≥ 0` (always true, no info), but the left-hand inequality's quadratic form in t=x/y has discriminant `8(k^2-1)^2`, which is strictly positive for k≠1 — meaning the inequality is violated for some x,y whenever k≠1 (verified numerically: e.g. k=1.2, k=0.8 both fail near t≈1–3). So **only k=1 survives among scalings** — confirms the "shift" direction (additive c) is the real degree of freedom, not a multiplicative one.
6. **The remaining gap: pin the additive constant globally.** `f(f(y))=2f(y)-y` only forces `h(x):=f(x)-x` to be *invariant along each forward f-orbit* (`h(f(y))=h(y)`), not globally constant. I built a discrete counterexample-shaped test: `h(x)=1` for x≤10, `h(x)=2` for x>10 (i.e. f jumps from x+1 to x+2 at x=10) — this is NOT invariant under f in the required sense but tests whether "locally-constant-with-a-jump" h can survive the *full* two-variable inequality (not just orbit substitutions). Numerically it **fails badly** (found A-value ≈ -46 at x≈12.01, y≈9.99), confirming h cannot jump — some genuinely cross-orbit (non-x=f(y)) pair of substitutions must be used to force h globally constant. This is the true remaining gap for the outliner to close, and it needs a two-variable (not orbit) argument.
7. **A usable cross-variable inequality for closing gap 6** (derived by expanding the original inequalities with `f(x)=x+a, f(y)=x... wait f(y)=y+b` symbolically, a=h(x), b=h(y), for literal *unrelated* x,y): expanding gives
   - `A = 2x²+2f(y)²-(f(x)+y)² = (x-y)² - 2a(x+y) - a² + 2b² + 4by ≥ 0`
   - `B = (f(x)+y)²-4xf(y) = (x-y)² + 2a(x+y) + a² - 4bx ≥ 0`
   where a=h(x), b=h(y). These are two genuine, non-orbit constraints linking h(x) and h(y) for *every* pair x,y>0 (not just y=f(x) type pairs) — likely the right lever for a sup/inf argument (e.g. let s=sup h, take x with h(x) near s, then B bounds h(y) from above in terms of a,x,y; push y→ small or large to squeeze). I did not carry this to completion — flagging as the concrete next step, not solved.

### Candidate technique(s)
- **QM–AM–GM sandwich / functional-equation substitution** (knowledge_base.md "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM" + "Functional equations: test special values, check injectivity/surjectivity").
- Substituting `x=f(y)` to collapse a nested composite is exactly the crux move used in the analogous corpus problem below.
- The final gap (pin h constant) likely needs a **sup/inf extremal argument** (Pólya "specialize"/"extremal principle" from knowledge_base.md) combined with the two-variable inequality in point 7.

### Cheap-kill candidates
- Pure scaling f(x)=kx: killed for all k≠1 by the discriminant computation in point 5 (algebraic, not just numeric — `8(k²-1)²>0` discriminant of the quadratic-in-t form of inequality A).
- Piecewise-constant-shift f: killed numerically (point 6) — strong evidence (not yet a proof) that h must be constant, ruling out "any invariant-under-orbit h works" naively.
- f(x) < x anywhere: killed rigorously by the orbit/positivity argument (point 3).

### Knowledge-base entries to use
- **Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur** — the whole problem *is* a QM≥AM≥GM sandwich in disguise; recognizing the x=y case as the trivial instance of this is essential to avoid a false lead.
- **Functional equations: test special values, check injectivity/surjectivity** — directly used via x=f(y).
- **Pólya heuristics: Specialize / Introduce a substitution / Exploit symmetry** — for point 7's sup/inf finishing argument.

### Analogous past problems (cruxes)
- **`aimo-0255`** (BLR, algebra/functional-equations domain; prove ∃x,y with f(x-f(y)) > yf(x)+x): genuinely analogous *technique*, not statement. Its crux move: "substitute the argument so an inner nested term cancels... collapsing the composite value to the fixed constant f(0)," then "combine a two-sided sandwich on a composite value f(f(t)) — a lower bound from one substitution and the affine ceiling as the upper bound — to descend to a pointwise lower bound on f itself." This is structurally the same move as our x=f(y) substitution that produced the *exact* two-sided sandwich pinning `f(f(y))=2f(y)-y`. Worth reading in full as a template for how to convert "one bound from substitution X" + "one bound from substitution Y" into a pointwise global bound (they use it to finish their whole proof; we've used it to get the composite identity but still need an extra step for the additive constant).
- No other corpus entry found that matches the QM-AM-GM sandwich structure specifically; searched algebra/functional-equations (263 entries) and algebra/inequalities-related keywords (113 entries) — aimo-0255 is the standout match.

### Prior progress
None — this is round 1, fresh workspace, no `results/imo-2026-05/` directory existed before this round.

### Dead ends (do not retry)
- **x=y substitution**: proves nothing (identity holds automatically for every f — it's literally QM≥AM≥GM on the pair (x,f(x))). Do not build an approach around it.
- **Pure multiplicative scaling f(x)=kx, k≠1**: algebraically refuted (discriminant argument, point 5) — don't waste a slug conjecturing scaled-identity solutions.
- **Assuming f=identity is the unique answer**: refuted — f(x)=x+c works for all c≥0 (exact symbolic check: for f(x)=x+c, both `2x²+2f(y)²-(f(x)+y)²` and `(f(x)+y)²-4xf(y)` equal `(x-y-c)²`, manifestly ≥0). Any approach asserting uniqueness of identity without accounting for the shift family will be wrong.

### Small-case / intuition notes (labeled conjecture where appropriate)
- **Verified (not conjecture, exact symbolic computation)**: f(x)=x+c satisfies both inequalities for every c≥0, with equality in both simultaneously iff x-y=c.
- **Verified (rigorous derivation)**: f(f(y))=2f(y)-y for all y; f injective; f(x)≥x for all x.
- **Conjecture (strong numerical support)**: h(x):=f(x)-x is a single global constant c≥0, i.e. the complete solution set is exactly `{f(x)=x+c : c≥0}`. This is NOT yet proven — the gap is showing h can't vary across different orbits (only within-orbit invariance is proven). The outliner should treat "prove h is globally constant" as the single hard remaining lemma, and should use the cross-variable inequalities in point 7 (or another two-variable, non-orbit substitution) to close it.
- Numerically, grid search (400×400 log-spaced points, x,y∈[10⁻³,10³]) found no violation of either inequality for f(x)=x+c, c∈{1,0.5,2,-0.1}. Note c=-0.1 case is invalid on domain grounds (f(x)<0 for small x) even though the sampled grid missed it — this is a domain/codomain constraint, not an inequality failure, and should be stated explicitly in the final answer (c≥0 required so that f maps R_{>0}→R_{>0}).
