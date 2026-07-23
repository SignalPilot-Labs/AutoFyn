## imo-2026-05

- **Distinct openings:**

  1. **Substitution x = f(y) forces f(f(y)) = 2f(y) - y (exact).** The left inequality at x = f(y) gives f(y) ≥ (f(f(y)) + y)/2 (since QM(f(y), f(y)) = f(y)), and the right inequality at x = f(y) gives (f(f(y)) + y)/2 ≥ f(y) (since √(f(y)·f(y)) = f(y)). Together: f(f(y)) = 2f(y) − y exactly. This pins g = f − id to satisfy g(f(y)) = g(y) (g is constant on orbits of f). This is the entry point for most further argument.

  2. **Descent from orbit structure forces f(x) ≥ x.** From f(f(y)) = 2f(y) − y: if g(y₀) = f(y₀) − y₀ < 0 for some y₀, then f^n(y₀) = y₀ + n·g(y₀) → −∞, leaving ℝ₊. Contradiction. So f(x) ≥ x for all x > 0 — this is rigorous without any regularity assumption.

  3. **The right inequality forces g to be non-decreasing (and hence constant on orbits → constant).** Expanding the right inequality (f(x) + y)² ≥ 4x·f(y) with g(x) = p and g(y) = q gives the quadratic in g(x): g(x)² + 2(x+y)g(x) + (x−y)² − 4xq ≥ 0. The binding root (lower root for g ≥ 0) is r₂ = q − (√x − √(y+q))². Choosing y such that √(y + q) = √x (i.e., y = x − q, if x > q) gives r₂ = q. So the right inequality requires g(x) ≥ g(y) whenever f(y) ≤ x, meaning g is "non-decreasing along the f-preimage" order. Since the orbit {y + nd : n ≥ 0} is unbounded and g = d on the entire orbit, while g must be ≥ d everywhere beyond the orbit, this forces g to equal d everywhere (constant).

  4. **Reduction to standard QM ≥ AM ≥ GM.** For f(x) = x + c, note that AM(f(x), y) = (x + c + y)/2 = AM(x, f(y)). So the chain becomes QM(x, f(y)) ≥ AM(x, f(y)) ≥ GM(x, f(y)), which is just the standard chain for the pair (x, y + c) — always true. This confirms f(x) = x + c works for ALL c ≥ 0.

  5. **Equality analysis.** Both inequalities are equalities simultaneously iff x = f(y) = y + c (i.e., x − y = c). For c = 0, this is x = y; for c > 0, it is the line x − y = c in the (x,y)-plane. This confirms neither inequality is vacuously satisfied.

- **Candidate technique(s):** Functional equation via strategic substitution + inequality squeezing; AM-GM equality case analysis; orbit-invariant argument for g = f − id.

- **Cheap-kill candidates:**
  - Set x = f(y): both inequalities instantly become equalities and force f(f(y)) = 2f(y) − y in ONE move.
  - From f(f(y)) = 2f(y) − y and positivity: descent kills all f(x) < x.
  - The right inequality quadratic in g(x) forces g non-decreasing; orbit condition forces g constant.

- **Knowledge-base entries to use:**
  - "Functional equations: test special values, check injectivity/surjectivity" (KB: Algebra & Polynomials)
  - "Standard inequalities: AM-GM, QM-AM" (KB: Algebra & Polynomials — equality cases pin extremal configuration)
  - "Direct proof: chain definitions" (KB: General Proof Methods)
  - "Work backward: assume the goal" (KB: Problem-Solving Heuristics)

- **Analogous past problems (cruxes):**
  - **aimo-0368** (f(f(f(n))) + f(f(n)) + f(n) = 3n → f = id): crux move = "When a sum of terms each bounded below by the same value equals that many copies of the bound, force every term to equal the bound." Analogous: our x = f(y) substitution squeezes both upper and lower bound into equality, forcing f(f(y)) = 2f(y) − y exactly.
  - **aimo-0399** (f(x+y) ≤ yf(x) + f(f(x)) → f(x) = 0 for x ≤ 0): crux move = "Feed the function's own outputs as the free argument for two anchor points, then add to cancel nested terms." Analogous: plugging x = f(y) is exactly "feeding the function's output back as the primary variable."
  - No direct match for double-sided inequality + positive-reals functional equation.

- **Prior progress:** None (status: unsolved, no prior approaches).

- **Dead ends (do not retry):** None recorded yet.

- **Small-case / intuition notes (CONJECTURED):**
  - f(x) = x (c = 0): verified for many (x, y) pairs. Both inequalities collapse to QM ≥ AM ≥ GM for (x, y). ✓
  - f(x) = x + 1 (c = 1): verified. AM(f(x), y) = AM(x, f(y)), so standard chain. ✓
  - f(x) = x + 5 (c = 5): verified. ✓
  - f(x) = 2x: FAILS at (x,y) = (10, 0.1). ✗
  - f(x) = 1/x: FAILS. ✗
  - Non-constant g (f(1)=1, f(2)=4): LEFT inequality fails at x=2, y=1. ✗
  - Non-constant g (f(1)=1, f(1.1)=1.2): RIGHT inequality fails at x=1, y=1.1. ✗
  - **CONJECTURE (strong):** The answer is f(x) = x + c for constant c ≥ 0. The key structural reason: (1) x = f(y) forces f(f(y)) = 2f(y) − y; (2) positivity forces g ≥ 0; (3) the right inequality forces g to be non-decreasing along f-preimages; (4) orbit structure forces g constant.

- **Proof gap remaining:** The argument that g must be EXACTLY constant (not just "non-decreasing in some sense") needs to be made rigorous without a measurability assumption. The clean route: from the right inequality at (x, y) = (z, z − g(z)) (when z > g(z)), g(z) ≥ g(z − g(z)) for any z; and the left inequality gives an upper bound. Combined with orbit invariance g(z + g(z)) = g(z), these force g to be constant without any regularity hypothesis.
