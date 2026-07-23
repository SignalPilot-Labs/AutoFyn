# imo-2026-05 — tracking file (reviewer-owned)

## Status
solved

## Approaches tried
- **two-point-pinch** — worked (round 1, APPROVED). Core identity f(f(y)) = 2f(y) − y from x = f(y); orbit AP gives f ≥ id; second substitution x = f(y′) into the right inequality gives the pinch |d(a) − d(b)| ≤ (a−b)²/(4·min(a,b)); telescoping subdivision forces d constant. Every algebraic identity re-verified symbolically by the reviewer.
- **marching-orbits** — worked (round 1, APPROVED as an independent second proof). Same core identity and AP orbits; mismatched positive d-values p < q refuted by marching the p-orbit to within p of a far q-orbit point where the right inequality's slack Δ = 4y_n(p−q) + (S+p)² − 4Sq < 0; mixed {0,c} case killed by fixed-point propagation (Lemma 5 interval, quadratic root computation verified) and an exclusion zone |s−a| ≥ 2√(ac) that the c-orbit (step c < interval length 4√(a′c)) must enter. All constants and inductions checked.
- **tangent-envelope** — not built in round 1 (reserve; open structural gap on density of range(f) anchors). Superseded by the solve.

## Current best
Problem solved. Answer: **exactly the functions f(x) = x + c, c ≥ 0 a constant.** Two independent complete proofs exist (`approaches/two-point-pinch.md`, `approaches/marching-orbits.md`). Certified shared lemmas: `lemmas/core-identity-ap-orbits.md`, `lemmas/two-point-pinch-bound.md`.

## Full proof

**Problem.** Determine all functions f: ℝ_{>0} → ℝ_{>0} such that

  √((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y))  for all x, y > 0.  (★)

**Answer.** Exactly the functions f(x) = x + c, where c ≥ 0 is a constant.

Throughout, we use the fact that for real numbers A, B ≥ 0, the inequality A ≥ B is equivalent to A² ≥ B² (squaring is strictly increasing on [0, ∞); cf. knowledge base entry "Standard inequalities (QM-AM-GM equality cases)"). We invoke this each time we square, after checking both sides are nonnegative.

---

### Part I. Sufficiency: every f(x) = x + c with c ≥ 0 satisfies (★)

First, f is well defined as a map ℝ_{>0} → ℝ_{>0}: for x > 0 and c ≥ 0 we have f(x) = x + c > 0. (If c < 0, then for 0 < x ≤ −c we would have f(x) ≤ 0, violating the codomain; so no f(x) = x + c with c < 0 is even a candidate — a domain/codomain fact, independent of (★).)

Fix x, y > 0 and write f(y) = y + c, f(x) = x + c.

**Left inequality.** Both sides of √((x² + (y+c)²)/2) ≥ (x + c + y)/2 are positive, so the inequality is equivalent to its square: 2(x² + (y+c)²) ≥ (x + y + c)². Expanding,

  2(x² + (y+c)²) − (x + y + c)² = x² + y² + c² − 2xy − 2xc + 2yc = (x − (y + c))² ≥ 0,

where the last identity is checked by expanding (x − y − c)². Hence the left inequality holds.

**Right inequality.** Both sides of (x + y + c)/2 ≥ √(x(y+c)) are nonnegative, so it is equivalent to its square: (x + y + c)² ≥ 4x(y + c). Writing t = y + c > 0,

  (x + t)² − 4xt = (x − t)² = (x − (y + c))² ≥ 0.

So every f(x) = x + c with c ≥ 0 satisfies (★), with equality throughout exactly when x = y + c. ∎(Part I)

---

### Part II. Uniqueness: any f satisfying (★) equals x ↦ x + c for some constant c ≥ 0

Let f: ℝ_{>0} → ℝ_{>0} satisfy (★). Define d: ℝ_{>0} → ℝ by d(y) := f(y) − y.

**Step 1 (Core identity): f(f(y)) = 2f(y) − y for all y > 0.**

Fix y > 0. Since f(y) > 0, we may substitute x = f(y) into (★). Then the leftmost term is √((f(y)² + f(y)²)/2) = √(f(y)²) = f(y) (as f(y) > 0), and the rightmost term is √(f(y)·f(y)) = f(y). So (★) reads

  f(y) ≥ (f(f(y)) + y)/2 ≥ f(y)

(f(f(y)) is defined because f(y) > 0). A chain of inequalities with equal endpoints forces equality throughout:

  (f(f(y)) + y)/2 = f(y), i.e. **f(f(y)) = 2f(y) − y**.  (1)

**Step 2 (f ≥ id): d(y) ≥ 0 for all y > 0.**

Fix y > 0 and define the forward orbit y₀ := y, y_{n+1} := f(y_n) for n ≥ 0.

*Claim A: y_n > 0 for every n ≥ 0.* Induction on n. Base: y₀ = y > 0. Step: if y_n > 0, then y_n is in the domain of f, and y_{n+1} = f(y_n) > 0 by the codomain.

*Claim B: y_{n+2} = 2y_{n+1} − y_n for every n ≥ 0.* By Claim A, y_n > 0, so identity (1) applies at the point y_n: y_{n+2} = f(f(y_n)) = 2f(y_n) − y_n = 2y_{n+1} − y_n.

*Claim C: y_n = y + n·d(y) for every n ≥ 0.* Two-step induction (KB "Linear recurrences": characteristic polynomial (λ − 1)², arithmetic progressions): for n = 0, y₀ = y; for n = 1, y₁ = f(y) = y + d(y). Assuming the formula for n and n + 1,

  y_{n+2} = 2y_{n+1} − y_n = 2(y + (n+1)d(y)) − (y + n·d(y)) = y + (n+2)d(y).

Now suppose, for contradiction, that d(y) < 0. By the Archimedean property of ℝ, choose an integer n > y / (−d(y)). Then

  y_n = y + n·d(y) < y + (y / (−d(y)))·d(y) = 0,

contradicting Claim A. Hence **d(y) ≥ 0, i.e. f(y) ≥ y, for all y > 0**.  (2)

**Step 3 (Two-point pinch): |d(a) − d(b)| ≤ (a − b)² / (4·min(a, b)) for all a, b > 0.**

Fix y, y′ > 0. Since f(y′) > 0, substitute x = f(y′) into the right inequality of (★):

  (f(f(y′)) + y)/2 ≥ √(f(y′)·f(y)).

Both sides are nonnegative (the left side is positive because f(f(y′)) > 0 and y > 0), so squaring gives the equivalent

  (f(f(y′)) + y)² ≥ 4 f(y′) f(y).  (3)

By (1), f(f(y′)) = 2f(y′) − y′ = y′ + 2d(y′). Substituting into (3) and writing u := d(y′), v := d(y):

  (y + y′ + 2u)² ≥ 4(y′ + u)(y + v).  (4)

Expanding both sides,

  (y + y′ + 2u)² = (y + y′)² + 4uy + 4uy′ + 4u²,  4(y′ + u)(y + v) = 4y′y + 4y′v + 4uy + 4uv,

so, using (y + y′)² − 4yy′ = (y − y′)²,

  LHS − RHS = (y − y′)² + 4uy′ + 4u² − 4y′v − 4uv = (y − y′)² + 4(y′ + u)(u − v).

Since y′ + u = f(y′), inequality (4) says exactly

  (y − y′)² + 4 f(y′)·(d(y′) − d(y)) ≥ 0.  (5)

Because f(y′) > 0, dividing by 4f(y′) and rearranging gives d(y) − d(y′) ≤ (y − y′)² / (4 f(y′)). By (2), f(y′) ≥ y′ > 0, so

  d(y) − d(y′) ≤ (y − y′)² / (4 y′).  (6)

Inequality (6) holds for ALL pairs y, y′ > 0. Exchanging roles,

  d(y′) − d(y) ≤ (y − y′)² / (4 y).  (7)

For arbitrary a, b > 0, applying (6) and (7) with {y, y′} = {a, b} in the two orders bounds both d(a) − d(b) and d(b) − d(a) above by (a − b)²/(4·min(a, b)) — in each case the denominator is 4 times one of a, b, and min(a,b) ≤ each — hence

  **|d(a) − d(b)| ≤ (a − b)² / (4·min(a, b))**  for all a, b > 0.  (8)

(No assumption on the sign or size of d(y′) is used beyond f(y′) ≥ y′ > 0, which always holds by (2).)

**Step 4 (Subdivision kills the quadratic error): d is constant.**

Fix 0 < a < b and let k ≥ 1 be an integer. Set t_i := a + i(b − a)/k for i = 0, 1, …, k, so t₀ = a, t_k = b, each t_i ≥ a > 0, and t_{i+1} − t_i = (b − a)/k. By the triangle inequality (telescoping d(a) − d(b) = Σ_{i=0}^{k−1} (d(t_i) − d(t_{i+1}))) and (8) applied to each consecutive pair:

  |d(a) − d(b)| ≤ Σ_{i=0}^{k−1} (t_{i+1} − t_i)² / (4·min(t_i, t_{i+1})).

For each i, min(t_i, t_{i+1}) = t_i ≥ a, so each of the k summands is at most ((b − a)/k)² / (4a), hence

  |d(a) − d(b)| ≤ k · ((b − a)/k)² / (4a) = (b − a)² / (4ak).  (9)

(9) holds for every positive integer k, while its left side does not depend on k. If |d(a) − d(b)| = ε > 0, choose (Archimedean property) an integer k > (b − a)²/(4aε); then (9) gives ε ≤ (b − a)²/(4ak) < ε, a contradiction. Hence **d(a) = d(b)**.

Since 0 < a < b were arbitrary (and a = b is trivial), d is constant: d ≡ c for some real c. By (2), c = d(1) ≥ 0. Therefore

  f(x) = x + c for all x > 0, with c ≥ 0 a constant.  ∎(Part II)

---

### Conclusion

Part II shows every solution of (★) is of the form f(x) = x + c with c ≥ 0; Part I verifies that every such function is a solution (both inequalities reduce to the perfect square (x − y − c)² ≥ 0), and functions x + c with c < 0 fail the codomain requirement. Hence the set of all solutions is exactly

  **{ f(x) = x + c : c ≥ 0 constant }.**  ∎

---

*Reviewer note (round 1): every load-bearing identity above — the two sufficiency slacks, the pinch identity (5), and Step 1's collapse — was re-verified symbolically (sympy). An independent second complete proof of the same characterization, by asymptotic orbit-marching plus fixed-point exclusion zones, is in `approaches/marching-orbits.md` and was also verified in full.*
