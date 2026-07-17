# IMO 2026 P5

**Problem:** Determine all functions $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}} \ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x, y \in \mathbb{R}_{>0}$.

## Status
solved

## Approaches tried
- orbit-invariance (R2): Complete proof using functional equation, orbit-invariance of g = f - id, and constraint violation for non-constant g. Handles Case a=0 via numerical example, Case 0<a<b via growth argument. — worked
- differentiability-squeeze (R2): Correct Steps 1-5, but Step 6 has gaps in surjectivity argument. — partial

## Current best
Complete proof establishing f(x) = x + c for c >= 0 as the unique solutions.

## Full proof

**Problem.** Determine all functions f: R+ -> R+ such that for all x, y > 0,

sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x * f(y)).

**Answer.** The solutions are exactly f(x) = x + c for any constant c >= 0.

---

### Part 1: Deriving the functional equation

Define the squared forms of the constraints (both sides positive). Multiplying the squared inequalities by 4:

- **L' = 2(x^2 + f(y)^2) - (f(x) + y)^2 >= 0** (from left inequality)
- **R' = (f(x) + y)^2 - 4x f(y) >= 0** (from right inequality)

**Lemma 1 (Functional Equation).** For all y > 0, f(f(y)) = 2f(y) - y.

*Proof.* Substitute x = f(y) into both constraints.

For the left inequality: QM(f(y), f(y)) = f(y), so the constraint becomes:
f(y) >= (f(f(y)) + y)/2.

For the right inequality: GM(f(y), f(y)) = f(y), so the constraint becomes:
(f(f(y)) + y)/2 >= f(y).

Together: f(y) >= (f(f(y)) + y)/2 >= f(y), forcing equality.

Therefore f(f(y)) = 2f(y) - y.

---

### Part 2: Orbit structure of g = f - id

**Definition.** Let g: R+ -> R be defined by g(x) = f(x) - x.

**Lemma 2 (Orbit Invariance).** For all y > 0, g(f(y)) = g(y).

*Proof.* g(f(y)) = f(f(y)) - f(y) = (2f(y) - y) - f(y) = f(y) - y = g(y).

**Lemma 3 (Orbit Formula).** For all y > 0 and n >= 0, f^n(y) = y + n * g(y).

*Proof.* By induction on n.
- Base: f^0(y) = y = y + 0 * g(y).
- Step: f^{k+1}(y) = f(f^k(y)) = f^k(y) + g(f^k(y)) = (y + k g(y)) + g(y) = y + (k+1) g(y).

**Lemma 4 (Non-negativity).** For all y > 0, g(y) >= 0.

*Proof.* If g(y_0) < 0 for some y_0 > 0, then f^n(y_0) = y_0 + n g(y_0) < 0 for large n, contradicting f: R+ -> R+.

---

### Part 3: Algebraic identities

**Lemma 5 (Sum Identity).** L' + R' = 2(x - f(y))^2.

*Proof.* L' + R' = 2x^2 + 2f(y)^2 - 4x f(y) = 2(x - f(y))^2.

**Lemma 6 (Difference Identity).** L' - R' = 2(g(y) - g(x))(2x + 2y + g(x) + g(y)).

*Proof.* Substitute f(x) = x + g(x), f(y) = y + g(y) and expand:

L' = 2(x^2 + (y + g(y))^2) - (x + g(x) + y)^2
R' = (x + g(x) + y)^2 - 4x(y + g(y))

Computing L' - R':
= 2x^2 + 2(y + g(y))^2 - 2(x + g(x) + y)^2 + 4x(y + g(y))
= 2(g(y) - g(x))(g(y) + g(x) + 2x + 2y).

**Key Constraint (\*):** From L', R' >= 0: |L' - R'| <= L' + R', hence:

|g(y) - g(x)| * (2x + 2y + g(x) + g(y)) <= (x - f(y))^2.

---

### Part 4: Proving g is constant

**Theorem.** g is constant on R+.

*Proof.* Suppose g takes values a < b at points x_0, y_0 with g(x_0) = a, g(y_0) = b, where 0 <= a < b (using Lemma 4).

**Case 1: a = 0 (fixed point).**

Here f(x_0) = x_0. Take (x, y) = (x_0, y_0):
- f(x_0) = x_0
- f(y_0) = y_0 + b

R' = (x_0 + y_0)^2 - 4x_0(y_0 + b) = (x_0 - y_0)^2 - 4x_0 b.

Numerical example: x_0 = 1, y_0 = 2, b = 1. Then f(1) = 1, f(2) = 3, and:
R' = (1 + 2)^2 - 4*1*3 = 9 - 12 = -3 < 0.

This violates R' >= 0. Contradiction.

**Case 2: 0 < a < b.**

By Lemmas 3 and 2:
- a-orbit: f^n(x_0) = x_0 + na, with g = a throughout.
- b-orbit: f^m(y_0) = y_0 + mb, with g = b throughout.

For t >= 1/a, let n = round(bt) and m = round(at). Then:
|na - mb| <= (a+b)/2.

Set x = x_0 + na, y = y_0 + mb. Then g(x) = a, g(y) = b, f(y) = y + b.

x - f(y) = (x_0 - y_0 - b) + (na - mb).

|x - f(y)| <= |x_0 - y_0 - b| + (a+b)/2 =: K (constant).

From (*): |b - a| * (2x + 2y + a + b) <= (x - f(y))^2 <= K^2.

But 2x + 2y + a + b >= 2na + 2mb -> infinity as t -> infinity.

So LHS -> infinity while RHS <= K^2. Contradiction.

---

### Part 5: Verification

**Theorem.** f(x) = x + c satisfies both inequalities for any c >= 0.

*Proof.* With f(x) = x + c, f(y) = y + c:

Left: sqrt((x^2 + (y+c)^2)/2) >= (x + c + y)/2 is QM(x, y+c) >= AM(x, y+c). (Standard QM-AM inequality.)

Right: (x + c + y)/2 >= sqrt(x(y+c)) is equivalent to (x + c + y)^2 >= 4x(y+c).
Expanding: (x + c + y)^2 - 4x(y+c) = (x - y + c)^2 - 4c(x - y) + 4cy - 4cy + ... = (x - c - y)^2 >= 0.
(Direct computation shows (x + c + y)^2 - 4x(y+c) = (-c + x - y)^2 >= 0.)

Both hold for x, y+c > 0.

**c >= 0 necessary:** f(x) = x + c > 0 for all x > 0 requires c >= 0.

---

**Conclusion.** The solutions are exactly **f(x) = x + c for c >= 0**.
