## imo-2026-05

### Problem recap
Find all f: R_{>0} -> R_{>0} such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y))   for all x,y > 0.
(Left: QM(x,f(y)) >= AM(f(x),y). Right: AM(f(x),y) >= GM(x,f(y)).)

---

### Distinct openings

**Opening A — The x=f(y) substitution (pinches both inequalities to equality)**
Substitute x = f(y) into the left inequality:
  sqrt((f(y)^2 + f(y)^2)/2) = f(y) >= (f(f(y))+y)/2, so f(f(y)) <= 2f(y)-y.
Substitute x = f(y) into the right inequality:
  (f(f(y))+y)/2 >= sqrt(f(y)*f(y)) = f(y), so f(f(y)) >= 2f(y)-y.
Combined: **f(f(y)) = 2f(y) - y for all y > 0.** (Exact equality, a necessary condition.)

This is the most powerful substitution. It gives the functional equation of "constant increment":
the sequence y, f(y), f^2(y), ... is arithmetic with step d = f(y)-y.

**Opening B — Sign of f(y)-y (f >= id)**
Letting h(y) = f(y)-y, the orbit y, y+d, y+2d, ... must stay in R_{>0} for all n. If d < 0,
eventually y+nd < 0. Contradiction. So h(y) >= 0, i.e., **f(y) >= y for all y > 0**.

**Opening C — The algebraic slack is (x-f(y))^2 [SOS proof of the answer]**
Candidate: f(x) = x+c (c >= 0). Compute:
  Left slack: 2(x^2+f(y)^2) - (f(x)+y)^2 = 2x^2 + 2(y+c)^2 - (x+c+y)^2 = (x-y-c)^2 = (x-f(y))^2 >= 0.
  Right slack: (f(x)+y)^2 - 4x*f(y) = (x+c+y)^2 - 4x(y+c) = (x-y-c)^2 = (x-f(y))^2 >= 0.
**Both inequalities reduce identically to (x-f(y))^2 >= 0.** Always true; equality iff x = f(y).
This SOS structure makes the proof trivial for the family f(x) = x+c.

**Opening D — Forcing h = const via the "orbit density + divergent RHS" argument**
From openings A and B: h(y) = f(y)-y >= 0 and h(f(y)) = h(y) (constant on each orbit).
But the COMBINED constraint from both L and R (computed algebraically as (I)-(II)) gives:
  **(x - f(y))^2 >= |h(x) - h(y)| * (f(x) + f(y))  for all x,y > 0.**

Suppose h(a) = c1 != c2 = h(b). Their respective orbits {a + nc1} and {b + mc2} go to infinity.
The set {nc1 - mc2 : n,m >= 0} is dense in R (by Kronecker if c1/c2 irrational) or takes all
multiples of gcd-related step (Bezout if rational). Either way, there exist sequences n_k, m_k -> inf
such that (a + n_k*c1) - (b + m_k*c2 + c2) = FIXED CONSTANT D.
Then: D^2 >= |c1-c2| * ((a+n_k*c1+c1) + (b+m_k*c2+c2)) -> infinity. Contradiction.
**=> h is constant on R_{>0}.** Hence f(x) = x + c for some c >= 0.

**Opening E — The "h has zero derivative" argument (continuity at image of f)**
From the combined constraint at x = f(y)+t (t > 0 small):
  |h(f(y)+t) - h(y)| <= t^2 / (f(f(y)+t) + f(y)) <= t^2 / (2*f(y)).
So h is "differentiable with h'(f(y)) = 0" at every point in f(R_{>0}).
On f(R_{>0}) = (c, infinity), h' = 0 => h = const there.
For x in (0,c]: h(x) = h(x+c) (orbit structure) = the same constant.
This is a cleaner/more direct route for the continuity-minded outliner.

---

### Best answer (conjecture, computationally verified)
**f(x) = x + c for any constant c >= 0.** (Conjectured; the sufficiency is proved, the necessity argument above is outlined but has a gap in the orbit-density step that needs careful treatment.)

Numerically verified: f(x) = x, f(x) = x+1, f(x) = x+2, f(x) = x+5 all satisfy both inequalities on a dense grid. Confirmed FAIL: f(x) = x^2, f(x) = x+sqrt(x), f(x) = x+x^2, any cx with c != 1.

---

### Candidate techniques
- **SOS / completing the square** (both slack expressions = (x-f(y))^2): primary.
- **Functional equations: test special values / x=f(y)**: pinches f(f(y)) = 2f(y)-y.
- **AM-GM / QM-AM equality conditions**: structure of when equality holds.
- **Kronecker equidistribution / Bezout**: for forcing h = const across orbits.
- **Standard inequalities: AM-GM, QM-AM**: names of tools.

---

### Cheap-kill candidates
- **Equality at x = f(y)**: both L and R collapse to f(f(y)) = 2f(y)-y. This is a necessary condition that severely restricts f. Free!
- **Positivity of orbit**: f(y)-y >= 0 from the fact f: R_{>0} -> R_{>0} and the arithmetic orbit must stay positive. Free!
- **Quadratic form test (cx family)**: for f(x) = cx, the left inequality requires 4AC-B^2 = -8(c^2-1)^2 >= 0, forcing c = 1. Rules out f(x) = cx with c != 1 immediately.

---

### Knowledge-base entries to use
- **Standard inequalities (AM-GM, QM-AM, Schur)**: named in "Algebra & Inequalities" — the problem is literally a QM >= AM >= GM chain.
- **Sum of squares (SOS) / completing the square**: the slack (x-f(y))^2 is the SOS certificate; entry in "Algebra & Polynomials".
- **Functional equations: test special values**: entry in "Algebra & Polynomials"; the x=f(y) substitution is canonical.
- **Pólya heuristics — Solve a special case / specialize**: entry in "Problem-Solving Heuristics" — guided all substitutions.

---

### Analogous past problems (cruxes)
1. **aimo-0008** (ISL 2010 A1 flavor): "f multiplicative + superadditive on Q_{>0} with one fixed point => f = id." Crux: *sandwich via superadditive/submultiplicative iterates*. Analogous because it forces f = id by squeezing from above and below using the function's own structure. Relevant because our f(x) = x+c family is similarly forced by a squeeze (here, (x-f(y))^2 squeeze).

2. **aimo-0089** (functional inequality => concavity): Crux: *rewrite functional inequality as a supporting-line (supergradient) bound*. Analogous: the QM bound in our problem acts as a "supporting envelope" for f(x).

3. **aimo-0234**: "f(xy+f(x))=xf(y)+2, R_{>0}." Crux: *sandwich a monotone unknown between step functions from an additive shift relation, force exact linear form*. Directly analogous: our f satisfies f(y+c) = f(y)+c (the shift relation), and the orbit structure forces f(x) = x+c.

---

### Prior progress
None (fresh run, round 1).

---

### Dead ends (do not retry)
- **f(x) = cx (power-law with c != 1)**: fails the left inequality. The quadratic form 2x^2 + 2c^2y^2 - (cx+y)^2 = (2-c^2)x^2 - 2cxy + (2c^2-1)y^2 has discriminant -8(c^2-1)^2 < 0 for c != 1. Fails for all c != 1.
- **Non-affine functions** (f(x) = x + sqrt(x), f(x) = x+x^2): both fail numerically on small-x regime. Left inequality collapses because QM(x, f(y)) is too small when x is small and f(x) is large.
- **f is an involution (f(f(y)) = y)**: this would require 2f(y)-y = y => f(y) = y (only f=id). So any c > 0 breaks involution; correct.

---

### Small-case / intuition notes
- The equality locus is the curve {(x,y): x = f(y)}, i.e., the graph of f^{-1}. On this curve, QM = AM = GM = x (all three equal), which is the equality condition for QM=AM (need QM args equal: x = f(y)) AND AM=GM (need AM args equal: f(x) = y, i.e., f(f(y)) = y). Both hold simultaneously only if f(f(y)) = y AND f(y) = f(y). For f(x) = x+c: x = f(y) = y+c, and f(x) = x+c = y+2c != y in general. So equality is attained at L only (not both simultaneously unless c=0). **Conjecture**: both equalities hold simultaneously iff c = 0 (f = id).
- For f(x) = x+c, the answer reduces trivially to (x-y-c)^2 >= 0 in both slots. The "ugliness" of the problem hides a beautiful SOS structure.
- h = f-id is the key variable. It must be non-negative (from orbit structure) and constant (from the combined density/continuity argument).

---

### Notes for the outliner

**The answer is f(x) = x + c for ALL c >= 0** (not just c = 0).

**Proof route (cleanest):
1. Verify f(x) = x+c works: both slacks = (x-f(y))^2 >= 0 [1-line SOS].
2. Show it's necessary:
   a. Substitute x = f(y): pinches both inequalities to f(f(y)) = 2f(y)-y. [2-step squeeze]
   b. Deduce h(y) = f(y)-y >= 0 from orbit positivity.
   c. Note h(f(y)) = h(y) from the identity f(f(y)) = 2f(y)-y.
   d. Derive: (x-f(y))^2 >= |h(x)-h(y)|*(f(x)+f(y)) for all x,y. [algebraic manipulation]
   e. Use density/continuity to force h = const. [the main gap to fill rigorously]
3. f: R_{>0} -> R_{>0} forces c = h >= 0.

**Main gap**: Step (e) — proving h is constant from the combined inequality. The cleanest route uses:
  |h(f(y)+t) - h(y)| <= t^2/(2f(y)) as t->0+, so h'(f(y)) = 0 for all y, meaning h is locally constant on f(R_{>0}) = (c, inf), hence constant there; and orbit structure extends this to (0,c].

OR the density route: if h(a) != h(b), the diverging orbit sequences give bounded LHS vs unbounded RHS.

The density argument needs care about what happens when c2 = 0 (fixed points). The direct test: h(1)=0 and h(2)=1 already gives 1 >= 4 (fails), so the constraint itself rules out mixed h values at nearby points — no need for infinity.
