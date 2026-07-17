# Approach: two-point-pinch

## Status
solved

## Approaches tried
- Substitution x = f(y') into the ORIGINAL right inequality (after establishing f(f(y)) = 2f(y) − y) — worked: yields a clean two-point quadratic pinch |d(y) − d(y')| ≤ (y − y')²/(4·min(y,y')) for ALL unrelated pairs, verified symbolically (sympy) in round 1. Chaining/subdivision then forces d constant.
- Round 1 build: wrote the full rigorous proof below (sufficiency by two perfect-square identities; uniqueness via core identity → orbit AP → f ≥ id → two-point pinch → telescoping subdivision). All algebra derived by hand in the text; every squaring justified by positivity; the step-3 induction written out explicitly. — worked; Status set to solved, pending proof-reviewer verdict.

## Current best
Complete proof written (see Full proof). Answer: exactly the family f(x) = x + c with c ≥ 0 constant. No open gaps known.

## Target
Determine all f: R_{>0} → R_{>0} with sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y)) for all x,y > 0.
**Answer to prove: exactly the family f(x) = x + c, c ≥ 0 a constant.**

## Technique
Squeeze-to-equality substitution (x = f(y) collapses QM and GM to force f∘f = 2f − id), then a SECOND substitution x = f(y') into the original right inequality to obtain a two-point quadratic pinch on d = f − id, closed by a subdivision/chaining (telescoping) argument. KB: "Standard inequalities (QM-AM-GM equality cases)", "Functional equations: test special values", "Linear recurrences" (for the orbit-AP step), "Sum of squares / completing the square".

## Full proof

**Problem.** Determine all functions f: ℝ_{>0} → ℝ_{>0} such that

  √((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y))  for all x, y > 0.  (★)

**Answer.** Exactly the functions f(x) = x + c, where c ≥ 0 is a constant.

Throughout, we use the fact that for real numbers A, B ≥ 0, the inequality A ≥ B is equivalent to A² ≥ B² (squaring is monotone on [0, ∞); this is the equality/monotonicity fact underlying the QM–AM–GM chain, cf. knowledge base entry "Standard inequalities (QM-AM-GM equality cases)"). We will invoke this each time we square, after checking both sides are nonnegative.

---

### Part I. Sufficiency: every f(x) = x + c with c ≥ 0 satisfies (★)

First, f is well defined as a map ℝ_{>0} → ℝ_{>0}: for x > 0 and c ≥ 0 we have f(x) = x + c > 0. (This is where c ≥ 0 is needed for membership in the family: if c < 0, then for 0 < x ≤ −c we would have f(x) = x + c ≤ 0, violating the codomain ℝ_{>0}; so no f(x) = x + c with c < 0 is even a candidate. This is a domain/codomain fact, independent of (★).)

Fix x, y > 0 and write f(y) = y + c, f(x) = x + c.

**Left inequality.** Both sides of √((x² + (y+c)²)/2) ≥ (x + c + y)/2 are positive (the right side because x, y > 0, c ≥ 0), so the inequality is equivalent to its square:

  (x² + (y+c)²)/2 ≥ (x + y + c)²/4, i.e. 2(x² + (y+c)²) ≥ (x + y + c)².

Expand both sides:

  2(x² + (y+c)²) = 2x² + 2y² + 4yc + 2c²,
  (x + y + c)² = x² + y² + c² + 2xy + 2xc + 2yc.

Subtracting:

  2(x² + (y+c)²) − (x + y + c)² = x² + y² + c² − 2xy − 2xc + 2yc = (x − (y + c))² ≥ 0,

where the last identity is checked by expanding (x − y − c)² = x² + y² + c² − 2xy − 2xc + 2yc. Hence the left inequality holds.

**Right inequality.** Both sides of (x + y + c)/2 ≥ √(x(y+c)) are nonnegative (the left is positive, the right is the square root of a positive number), so it is equivalent to its square:

  (x + y + c)² ≥ 4x(y + c).

Compute the difference, writing t = y + c > 0:

  (x + t)² − 4xt = x² + 2xt + t² − 4xt = x² − 2xt + t² = (x − t)² = (x − (y + c))² ≥ 0.

Hence the right inequality holds. So every f(x) = x + c with c ≥ 0 satisfies (★), with equality throughout exactly when x = y + c. This proves sufficiency. ∎(Part I)

---

### Part II. Uniqueness: any f satisfying (★) equals x ↦ x + c for some constant c ≥ 0

Let f: ℝ_{>0} → ℝ_{>0} satisfy (★). Define d: ℝ_{>0} → ℝ by d(y) := f(y) − y.

**Step 1 (Core identity): f(f(y)) = 2f(y) − y for all y > 0.**

Fix y > 0. Since f(y) > 0, we may substitute x = f(y) into (★). With this substitution:

- the leftmost term is √((f(y)² + f(y)²)/2) = √(f(y)²) = f(y) (as f(y) > 0);
- the rightmost term is √(f(y)·f(y)) = f(y).

So (★) reads

  f(y) ≥ (f(f(y)) + y)/2 ≥ f(y).

(Note f(f(y)) is defined because f(y) > 0 lies in the domain of f.) A chain of inequalities with equal endpoints forces equality throughout (squeeze/equality-case collapse, KB "Standard inequalities (QM-AM-GM equality cases)"):

  (f(f(y)) + y)/2 = f(y), i.e. **f(f(y)) = 2f(y) − y**.  (1)

**Step 2 (f ≥ id): d(y) ≥ 0 for all y > 0.**

Fix y > 0 and define the forward orbit y₀ := y, y_{n+1} := f(y_n) for n ≥ 0.

*Claim A: y_n > 0 for every n ≥ 0.* Induction on n. Base: y₀ = y > 0. Step: if y_n > 0, then y_n is in the domain of f, and y_{n+1} = f(y_n) > 0 by the codomain. So each y_n is a positive real and f may be applied to it.

*Claim B: y_{n+2} = 2y_{n+1} − y_n for every n ≥ 0.* By Claim A, y_n > 0, so identity (1) applies at the point y_n:

  y_{n+2} = f(f(y_n)) = 2f(y_n) − y_n = 2y_{n+1} − y_n.

*Claim C: y_n = y + n·d(y) for every n ≥ 0.* This is the solution of the linear recurrence of Claim B with characteristic polynomial (λ − 1)² — a double root at 1, giving arithmetic progressions (KB "Linear recurrences") — verified by induction on n: for n = 0, y₀ = y; for n = 1, y₁ = f(y) = y + d(y). Assuming the formula for n and n + 1,

  y_{n+2} = 2y_{n+1} − y_n = 2(y + (n+1)d(y)) − (y + n·d(y)) = y + (n+2)d(y),

completing the induction (strong two-step base as required by the second-order recurrence).

Now suppose, for contradiction, that d(y) < 0. By the Archimedean property of ℝ, choose an integer n > y / (−d(y)). Then

  y_n = y + n·d(y) < y + (y / (−d(y)))·d(y) = y − y = 0,

contradicting Claim A. Hence **d(y) ≥ 0, i.e. f(y) ≥ y, for all y > 0**.  (2)

**Step 3 (Two-point pinch): |d(a) − d(b)| ≤ (a − b)² / (4·min(a, b)) for all a, b > 0.**

Fix y, y′ > 0. Since f(y′) > 0, substitute x = f(y′) into the right inequality of (★):

  (f(f(y′)) + y)/2 ≥ √(f(y′)·f(y)).

Both sides are nonnegative: the right side is the square root of a positive number, and the left side is positive because f(f(y′)) > 0 (it is a value of f) and y > 0. Hence squaring is legitimate and gives the equivalent

  (f(f(y′)) + y)² ≥ 4 f(y′) f(y).  (3)

By (1), f(f(y′)) = 2f(y′) − y′ = 2(y′ + d(y′)) − y′ = y′ + 2d(y′). Substituting into (3) and writing u := d(y′), v := d(y):

  (y + y′ + 2u)² ≥ 4(y′ + u)(y + v).  (4)

We now derive by hand the exact identity for the difference of the two sides. Expand the left side:

  (y + y′ + 2u)² = (y + y′)² + 4u(y + y′) + 4u² = (y + y′)² + 4uy + 4uy′ + 4u².

Expand the right side:

  4(y′ + u)(y + v) = 4y′y + 4y′v + 4uy + 4uv.

Subtract:

  LHS − RHS = (y + y′)² + 4uy + 4uy′ + 4u² − 4y′y − 4y′v − 4uy − 4uv
       = [(y + y′)² − 4yy′] + 4uy′ + 4u² − 4y′v − 4uv
       = (y − y′)² + 4u(y′ + u) − 4v(y′ + u)
       = (y − y′)² + 4(y′ + u)(u − v),

using (y + y′)² − 4yy′ = (y − y′)² (KB "Sum of squares / completing the square"). Since y′ + u = f(y′), inequality (4) says exactly

  (y − y′)² + 4 f(y′)·(d(y′) − d(y)) ≥ 0.  (5)

Because f(y′) > 0, we may divide by 4f(y′) and rearrange:

  d(y) − d(y′) ≤ (y − y′)² / (4 f(y′)).

By (2), f(y′) ≥ y′ > 0, so 1/f(y′) ≤ 1/y′, and since (y − y′)² ≥ 0,

  d(y) − d(y′) ≤ (y − y′)² / (4 y′).  (6)

Inequality (6) holds for ALL pairs y, y′ > 0. Applying it with the roles of y and y′ exchanged gives

  d(y′) − d(y) ≤ (y − y′)² / (4 y).  (7)

For arbitrary a, b > 0, combining (6) and (7) (with {y, y′} = {a, b} in the two orders) yields both d(a) − d(b) and d(b) − d(a) bounded above by (a − b)²/(4·min(a, b)) — in each of (6),(7) the denominator is 4 times one of a, b, and min(a,b) ≤ each of them, so 1/(4a), 1/(4b) ≤ 1/(4 min(a,b)) — hence

  **|d(a) − d(b)| ≤ (a − b)² / (4·min(a, b))**  for all a, b > 0.  (8)

(Remark: (8) required no assumption on the sign or size of d(y′) beyond f(y′) ≥ y′ > 0, which always holds by (2); in particular d(y′) = 0 is allowed.)

**Step 4 (Subdivision kills the quadratic error): d is constant.**

Fix 0 < a < b and let k ≥ 1 be an integer. Set t_i := a + i(b − a)/k for i = 0, 1, …, k, so t₀ = a, t_k = b, each t_i ≥ a > 0, and t_{i+1} − t_i = (b − a)/k for each i. By the triangle inequality (telescoping the sum d(a) − d(b) = Σ_{i=0}^{k−1} (d(t_i) − d(t_{i+1}))) and then (8) applied to each consecutive pair:

  |d(a) − d(b)| ≤ Σ_{i=0}^{k−1} |d(t_i) − d(t_{i+1})| ≤ Σ_{i=0}^{k−1} (t_{i+1} − t_i)² / (4·min(t_i, t_{i+1})).

For each i, min(t_i, t_{i+1}) = t_i ≥ a, so each summand is at most ((b − a)/k)² / (4a). There are k summands, hence

  |d(a) − d(b)| ≤ k · ((b − a)/k)² / (4a) = (b − a)² / (4ak).  (9)

Inequality (9) holds for every positive integer k, while its left side does not depend on k. Suppose |d(a) − d(b)| = ε > 0. By the Archimedean property, choose an integer k > (b − a)²/(4aε); then (9) gives ε ≤ (b − a)²/(4ak) < ε, a contradiction. Hence ε = 0, i.e. **d(a) = d(b)**.

Since a < b were arbitrary in ℝ_{>0}, d is constant: d ≡ c for some real c. By (2), c = d(1) ≥ 0. Therefore

  f(x) = x + c for all x > 0, with c ≥ 0 a constant.

∎(Part II)

---

### Conclusion

Part II shows every solution of (★) is of the form f(x) = x + c with c ≥ 0; Part I verifies that every such function is a solution (both inequalities reduce to the perfect square (x − y − c)² ≥ 0), and functions x + c with c < 0 fail the codomain requirement. Hence the set of all solutions is exactly

  **{ f(x) = x + c : c ≥ 0 constant }.**  ∎

---

## Promotable lemmas
- **Lemma (core identity).** Any f: ℝ_{>0} → ℝ_{>0} satisfying (★) satisfies f(f(y)) = 2f(y) − y for all y > 0. *Proved in Part II, Step 1 (substitution x = f(y), QM/GM collapse).*
- **Lemma (f dominates identity).** Any f: ℝ_{>0} → ℝ_{>0} satisfying (★) satisfies f(y) ≥ y for all y > 0. *Proved in Part II, Step 2 (orbit is an arithmetic progression y + n·d(y) contained in ℝ_{>0}).*
- **Lemma (two-point pinch).** Any f: ℝ_{>0} → ℝ_{>0} satisfying (★) has d := f − id obeying |d(a) − d(b)| ≤ (a − b)²/(4·min(a, b)) for all a, b > 0. *Proved in Part II, Step 3 (substitution x = f(y′) into the right inequality plus the exact identity (5)).*

## Cases to cover
None beyond the above — the pinch argument is case-free (no dichotomy on fixed points needed). Every squaring in the proof is performed on explicitly nonnegative quantities and stated as such.

## Watch out for
- In step 3, do NOT drop the possibility d(y′) = 0; the bound uses f(y′) ≥ y′ > 0 only, which always holds. (Handled: remark after (8).)
- Squaring the original inequalities: both middle terms (f(x)+y)/2 are positive, and 2f(y′) − y′ + y = f(f(y′)) + y > 0, so all squarings are reversible — stated at each use.
- Step 2 needs "for all n", i.e. the identity of step 1 applied at f^{(n)}(y), which is a positive real; the induction (Claims A–C) is explicit.
- The target is the FAMILY x + c, not f = id; proving "f = id" is a recorded false target. (The proof establishes the full family.)
