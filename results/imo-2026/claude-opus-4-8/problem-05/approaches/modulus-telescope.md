# Approach: modulus-telescope

## Status
solved

## Target (whole problem)
Determine all f: R_{>0} -> R_{>0} with
  sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y))   for all x,y>0.
Answer: exactly f(x) = x + c for constants c >= 0.

## Approaches tried
- modulus-telescope (round 1): SOS sufficiency + equality-pinch x=f(y) giving f(f(y))=2f(y)-y,
  then h:=f-id >= 0, a one-sided quadratic modulus bound h(t+p)-h(t) <= p^2/(4f(t)) from the RIGHT
  inequality, symmetrized to |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)), closed by a telescoping/Riemann-sum
  limit forcing h constant. All algebra verified with sympy. — WORKED; complete proof, no gaps.

## Current best
Complete proof of both directions (sufficiency and necessity). See Full proof.

## Full proof

We prove the answer is exactly the family **f(x) = x + c, c >= 0**.

Throughout, "(L)" and "(R)" denote the squared forms of the two given inequalities. Because every
quantity appearing under a square root, and every middle term (f(x)+y)/2, is positive, squaring a
stated inequality between nonnegative reals is an equivalence. Hence for all x,y>0 the hypothesis is
equivalent to:

  (L)  2(x^2 + f(y)^2) >= (f(x) + y)^2,
  (R)  (f(x) + y)^2 >= 4 x f(y).

---

### Part I. Sufficiency

Let c >= 0 be a constant and f(x) = x + c. Since x > 0 and c >= 0, we have f(x) = x + c > 0, so
f maps R_{>0} into R_{>0}. Also f(y) = y + c, so

  f(x) + y = x + c + y = x + (y + c) = x + f(y).

Thus the middle term equals the arithmetic mean (x + f(y))/2. We check (L) and (R).

**(L):** We must show 2(x^2 + f(y)^2) >= (x + f(y))^2. Expanding the difference,
  2(x^2 + f(y)^2) - (x + f(y))^2 = 2x^2 + 2f(y)^2 - x^2 - 2x f(y) - f(y)^2 = x^2 - 2x f(y) + f(y)^2 = (x - f(y))^2 >= 0.
This is the QM–AM inequality (knowledge_base.md, "Standard inequalities": QM-AM), verified as an
exact SOS ("Sum of squares (SOS)").

**(R):** We must show (x + f(y))^2 >= 4 x f(y). The difference is
  (x + f(y))^2 - 4x f(y) = x^2 - 2x f(y) + f(y)^2 = (x - f(y))^2 >= 0.
This is the AM–GM inequality (knowledge_base.md, "Standard inequalities": AM-GM), again an exact SOS.

Both slacks equal (x - f(y))^2 >= 0, so f(x) = x + c satisfies the hypothesis for every c >= 0.
(Both identities were verified symbolically with sympy: each slack minus (x - f(y))^2 simplifies to 0.)

This verifies the claimed answer by direct substitution.

---

### Part II. Necessity

Let f: R_{>0} -> R_{>0} satisfy (L) and (R) for all x, y > 0. We show f(x) = x + c for some c >= 0.

#### Step 1 (Equality pinch): f(f(y)) = 2 f(y) - y for all y > 0.

Fix y > 0. Since f(y) > 0, the value x = f(y) is admissible. Substitute x = f(y):

- Into (R): (f(f(y)) + y)^2 >= 4 f(y) · f(y) = 4 f(y)^2. Both f(f(y)) + y > 0 and 2 f(y) > 0, so
  taking positive square roots gives f(f(y)) + y >= 2 f(y), i.e. f(f(y)) >= 2 f(y) - y.
- Into (L): 2(f(y)^2 + f(y)^2) >= (f(f(y)) + y)^2, i.e. 4 f(y)^2 >= (f(f(y)) + y)^2. Taking positive
  square roots gives 2 f(y) >= f(f(y)) + y, i.e. f(f(y)) <= 2 f(y) - y.

Combining the two, **f(f(y)) = 2 f(y) - y** for all y > 0.

(The pinch works because x = f(y) makes QM(f(y), f(y)) = GM(f(y), f(y)) = f(y), collapsing the
sandwich to equalities.)

#### Step 2 (Positivity): with h := f - id, h(y) >= 0 for all y > 0.

Define h(y) = f(y) - y. The identity of Step 1 reads f(f(y)) - f(y) = f(y) - y, that is,

  (*)  h(f(y)) = h(y)   for all y > 0.

Let f^n denote the n-fold composite (f^1 = f, f^{n+1} = f ∘ f^n). We claim

  f^n(z) = z + n · h(z)   for all z > 0 and all integers n >= 1.

Induction on n. For n = 1, f^1(z) = f(z) = z + h(z). Assume the formula holds for n (for every
argument). Then, using it at the argument f(y) and then (*),
  f^{n+1}(y) = f^n(f(y)) = f(y) + n · h(f(y)) = f(y) + n · h(y) = (y + h(y)) + n · h(y) = y + (n+1) h(y).
This completes the induction.

Now suppose, for contradiction, that h(y) < 0 for some y > 0. Then f^n(y) = y + n h(y) -> -infinity
as n -> infinity, so f^n(y) < 0 for all sufficiently large n. But f maps R_{>0} into R_{>0}, so every
iterate f^n(y) is positive — contradiction. Hence **h(y) >= 0**, i.e. f(y) >= y > 0, for all y > 0.

#### Step 3 (Upper modulus bound, "(U)"): for all t > 0 and all p > -t,

  h(t + p) - h(t) <= p^2 / (4 f(t)).

Fix t > 0 and let s > 0 be arbitrary. Apply (R) at x = f(t) (admissible since f(t) > 0) and y = s:
  (f(f(t)) + s)^2 >= 4 f(t) f(s).
By Step 1, f(f(t)) = 2 f(t) - t, so
  (2 f(t) - t + s)^2 >= 4 f(t) f(s).
Now take s = t + p with p > -t (so that s = t + p > 0 is a legal argument). Then 2 f(t) - t + s = 2 f(t) + p, and
  (2 f(t) + p)^2 >= 4 f(t) f(t + p).
Since f(t) > 0, divide by 4 f(t):
  f(t + p) <= (2 f(t) + p)^2 / (4 f(t)) = f(t) + p + p^2 / (4 f(t)).
Subtracting (t + p) from both sides and using h(u) = f(u) - u:
  h(t + p) = f(t + p) - (t + p) <= (f(t) - t) + p^2 / (4 f(t)) = h(t) + p^2 / (4 f(t)),
which is exactly (U). (The rearrangement (2 f(t) - t + s)^2 = (2 f(t) + p)^2 at s = t + p and the
identity (2 f(t) + p)^2/(4 f(t)) = f(t) + p + p^2/(4 f(t)) were verified with sympy.)

Only the RIGHT inequality (R) and the identity of Step 1 were used, so there is no circularity.

#### Step 4 (Symmetrization): for all a, b > 0,

  |h(a) - h(b)| <= (a - b)^2 / (4 min(a, b)).

If a = b the statement is trivial (both sides 0). Suppose a != b. Apply (U) twice:

- With t = b, p = a - b (legal: p = a - b > -b since a > 0), t + p = a:  h(a) - h(b) <= (a - b)^2 / (4 f(b)).
- With t = a, p = b - a (legal: p = b - a > -a since b > 0), t + p = b:  h(b) - h(a) <= (a - b)^2 / (4 f(a)).

Whichever of h(a) - h(b), h(b) - h(a) is nonnegative equals |h(a) - h(b)|, and it is bounded above
by (a - b)^2 / (4 f(·)) with f(·) being f(b) or f(a) respectively; in both cases
  |h(a) - h(b)| <= (a - b)^2 / (4 min(f(a), f(b))).
By Step 2, f(a) >= a and f(b) >= b, so min(f(a), f(b)) >= min(a, b) > 0, giving
  |h(a) - h(b)| <= (a - b)^2 / (4 min(a, b)),
as claimed.

#### Step 5 (Telescoping limit): h is constant.

Fix any t0 > 0 and any L > 0. For each positive integer N, set the partition points
  t_i = t0 + i·(L/N),   i = 0, 1, ..., N,
so that t_0 = t0, t_N = t0 + L, each t_i >= t0 > 0, and consecutive gaps are t_{i+1} - t_i = L/N.
Apply Step 4 to each consecutive pair (with min(t_{i+1}, t_i) = t_i >= t0):
  |h(t_{i+1}) - h(t_i)| <= (L/N)^2 / (4 t_i) <= (L/N)^2 / (4 t0).
By the triangle inequality (telescoping the sum h(t_N) - h(t_0) = Σ_{i=0}^{N-1} (h(t_{i+1}) - h(t_i))),
  |h(t0 + L) - h(t0)| <= Σ_{i=0}^{N-1} |h(t_{i+1}) - h(t_i)| <= N · (L/N)^2 / (4 t0) = L^2 / (4 t0 N).

The left-hand side does not depend on N, while the right-hand side L^2/(4 t0 N) -> 0 as N -> infinity.
Therefore |h(t0 + L) - h(t0)| <= inf_{N>=1} L^2/(4 t0 N) = 0, hence h(t0 + L) = h(t0).

Since t0 > 0 and L > 0 were arbitrary, h takes the same value at any two points of R_{>0}: for
u > v > 0 put t0 = v, L = u - v to get h(u) = h(v). Thus **h is constant** on R_{>0}; write h ≡ c.

The minimum on [t0, t0+L] of f is >= t0 (from f >= id in Step 2), so the constant 1/(4 t0) is
uniform over the partition and the N-term sum genuinely vanishes; this is the crux that makes the
Riemann-sum bound work without any continuity or differentiability assumption on f.

#### Step 6 (Conclusion of necessity).

By Step 2, c = h(y) >= 0. Hence f(y) = y + h(y) = y + c with c >= 0, for all y > 0.

---

### Combining Parts I and II

Part II shows every solution has the form f(x) = x + c with c >= 0; Part I shows every such function
is a solution. Therefore the set of all functions satisfying the hypothesis is exactly

  { f(x) = x + c : c is a constant, c >= 0 }.

This is verified by substitution (Part I): for f(x) = x + c both inequality slacks equal
(x - f(y))^2 >= 0. ∎

## Promotable lemmas

- **Pinch identity.** If f: R_{>0} -> R_{>0} satisfies (L) 2(x^2+f(y)^2) >= (f(x)+y)^2 and
  (R) (f(x)+y)^2 >= 4x f(y) for all x,y>0, then substituting x = f(y) yields f(f(y)) = 2 f(y) - y for
  all y > 0. (Proved in Part II, Step 1.)
- **Nonnegativity of h = f - id.** Under the same hypotheses, f(y) >= y for all y > 0, via the orbit
  formula f^n(z) = z + n(f(z) - z) and positivity of iterates. (Part II, Step 2.)
- **Quadratic modulus of continuity.** Under the same hypotheses, |h(a) - h(b)| <= (a-b)^2/(4 min(a,b))
  for all a,b > 0, where h = f - id. (Part II, Steps 3–4.)
- **Telescoping rigidity.** If a function h on R_{>0} satisfies |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)),
  then h is constant. (Part II, Step 5; a self-contained real-analysis lemma, reusable.)
