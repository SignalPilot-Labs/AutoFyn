## imo-2026-05

### Problem
Find all f: R_{>0} -> R_{>0} such that sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y > 0.

The double inequality is: QM(x, f(y)) >= AM(f(x), y) >= GM(x, f(y)).

---

### Conjectured Answer (from computation)
f(x) = x + c for any constant c >= 0.

This is a one-parameter family. Verified numerically for c in {0, 0.01, 0.1, 0.5, 1, 2, 5, 10, 100} with 1000 random pairs (x,y).

Algebraic verification: for f(x) = x+c, both inequalities reduce to the single condition (x - (y+c))^2 >= 0. Explicitly:
- Ineq1: 2(x^2+(y+c)^2) >= (x+c+y)^2 = (x+(y+c))^2, which expands to (x-(y+c))^2 >= 0. Always true.
- Ineq2: (x+c+y)^2 >= 4x(y+c), which also reduces to (x-(y+c))^2 >= 0. Always true.

ELEGANT OBSERVATION: For f(x) = x+c, the middle expression (f(x)+y)/2 = (x+c+y)/2 = (x+f(y))/2 = AM(x, f(y)). So both ineqs become the standard QM(x,f(y)) >= AM(x,f(y)) >= GM(x,f(y)), which is the standard power-mean chain for the pair (x, f(y)). Both equalities hold iff x = f(y) = y+c.

NON-SOLUTIONS VERIFIED:
- f(x) = cx (linear through origin): satisfies ineq2 always (AM-GM), but ineq1 reduces to (c^2-1)^2*y^2 >= 0 (the quadratic 2(x^2+c^2y^2)-(cx+y)^2 has discriminant 8y^2(c^2-1)^2); for c≠1 the form is indefinite, so ineq1 fails for some (x,y). Only c=1 (f=id) works.
- f(x) = x + sin^2(x): non-constant perturbation — FAILS both ineqs.
- Step functions with two different additive constants: FAIL.

---

### Distinct Openings

**Opening 1 (x = f(y) substitution):** Plug x = f(y) into both inequalities simultaneously.
- Ineq1 becomes: sqrt((f(y)^2+f(y)^2)/2) = f(y) >= (f(f(y))+y)/2.
- Ineq2 becomes: (f(f(y))+y)/2 >= sqrt(f(y)*f(y)) = f(y).
- COMBINED: f(f(y)) = 2f(y) - y for ALL y > 0. [KEY FUNCTIONAL EQUATION]
This is a complete derivation of a derived functional equation with no gap.

**Opening 2 (Setting h = f - id):** Let h(y) = f(y) - y >= 0. Then:
- f(f(y)) = 2f(y)-y becomes h(f(y)) = h(y), i.e., h is constant on each orbit {y, y+h(y), y+2h(y),...}.
- The orbit of any point is an arithmetic progression with step h(y).
- h(y) >= 0: forced because if h(y) < 0 for some y, then f^n(y) = y + n*h(y) -> -infinity, contradicting f: R_{>0} -> R_{>0}.

**Opening 3 (Ineq1 squared gives (u-v)^2 >= c(c+2(u+v))):** After the substitution h(x) = a, h(y) = b with u = x, v = f(y), ineq1 is equivalent to:
(u-v)^2 >= (a-b)((a-b) + 2(u+v)).
For c = a-b > 0: this forbids u and v from being "close" relative to their magnitude. But orbit elements of step-a and step-b progressions eventually become "close" (distance bounded by max(a,b)) while u+v grows without bound. CONTRADICTION.

**Opening 4 (Orbit density/growth argument):** If h takes two different values a > b >= 0 on points x_0 and y_0: for orbit elements u = x_0+ma (in A) and v = f(y_0)+kb (in B), with m=k=n (syncing iterates): u-v = x_0 - f(y_0) + n(a-b) (grows) while constraint requires it >= sqrt(c(c+2(u+v))) which grows faster. For SAME-speed traversal (rational a/b = p/q: take m=qn, k=pn so u-v = constant while u+v -> ∞): constant^2 >= 2c*(u+v) -> ∞. CONTRADICTION.

**Opening 5 (b=0 case via ineq2):** If h(y_0) = 0 (y_0 is a fixed point) and h(x) = a > 0 for some x: ineq2 with x=y_0 and y with h(y)=a gives (y_0+y)^2 >= 4*y_0*(y+a) which rearranges to (y-y_0)^2 >= 4*y_0*a. So all A-orbit points must be at distance >= 2*sqrt(y_0*a) from y_0. For y_0 in the middle of R+, this forces a "gap" that cascades through the whole domain, eventually ruling out any fixed points coexisting with non-trivial orbits.

**Opening 6 (Mean-value interpretation):** The condition is precisely that AM(f(x), y) lies between QM(x, f(y)) and GM(x, f(y)). The "natural" midpoint between QM and GM is AM(x, f(y)) = (x+f(y))/2. The condition AM(f(x),y) = AM(x,f(y)) is equivalent to f(x)-x = f(y)-y = constant. This suggests a direct algebraic derivation: show the middle term must equal the "natural" AM, hence h = constant.

---

### Candidate Technique(s)

Primary: **Functional equation over R_{>0} -- substitution + orbit analysis**. The substitution x = f(y) pins f(f(y)) = 2f(y)-y, then the orbit structure h(f(y))=h(y) reduces the problem to showing h = constant, which follows from the growth of the orbit constraint from ineq1.

Secondary: **Squeeze / sandwiching argument** — showing the middle expression must equal AM(x, f(y)) by squeezing from both sides (ineq1 gives upper, ineq2 gives lower), and AM(f(x),y) = AM(x,f(y)) forces h to be constant.

---

### Cheap-Kill Candidates

- **Substitution x = f(y):** Gives f(f(y)) = 2f(y)-y in one clean step. Cost: two lines.
- **Orbit argument for f(y)>=y:** If f(a)<a for any a, then f^n(a)->-inf, contradicting codomain. Cost: two lines.
- **Both ineqs reduce to (x-f(y))^2 >= 0 for f(x)=x+c:** Verification of the answer family is trivial.

---

### Knowledge-Base Entries to Use

- **"Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration."** — The whole problem is about when AM(f(x),y) is sandwiched between QM(x,f(y)) and GM(x,f(y)); QM >= AM >= GM is the engine, equality cases force x = f(y).
- **"Functional equations: test special values, check injectivity/surjectivity."** — Direct application: plug in x=f(y).
- **"Constructive vs. existence: 'find all / largest n' needs an upper bound AND a matching construction."** — Must prove ALL f(x)=x+c work AND no other function works.
- **"Specialize: plug in extreme or symmetric values."** — Key: x = f(y) is the decisive specialization.
- **"Direct proof: chain definitions and known results."** — The functional equation is derived directly, then the orbit analysis is direct.

---

### Analogous Past Problems (Cruxes)

**aimo-0008** (most analogous): Functional equation over positive reals where the key move is: "Amplify a lossy additive bound by feeding iterates through it until the error is negligible." The sandwiching/squeeze technique applies directly: one uses the functional inequality to get f(x)^n >= f(x^n) > x^n-1, then n-th root gives f(x) >= x. **Adaptation**: here the analogous move is plugging x=f(y) to get an EXACT equality f(f(y))=2f(y)-y, then analyzing orbits. The orbit arithmetic progression structure is the same "iterating the bound" idea.

**aimo-0234** (functional equation f(xy+f(x))=xf(y)+2 over R+, answer f(x)=x+1): Crux move — "Sandwich a monotone unknown function between the floor and ceiling step-functions generated by an additive shift relation." Very analogous: derived functional equation gives f(y+f(1)) = f(y)+2 (a shift relation), then use monotonicity + sandwich to pin f linear. **Adaptation**: here the derived equation f(f(y))=2f(y)-y is even stronger (pinning orbits exactly), and the "shift" is the orbit step h(y). The proof strategy of deriving a shift equation and then concluding f is affine is directly applicable.

**aimo-0190** (functional equation on R, answer f(x)=x): Crux move — "Pin a Cauchy-additive function to linear by exhibiting one-sided boundedness on a ray, obtained from a square identity." Very analogous: once you establish f is Cauchy-additive (here: h is constant), one-sided boundedness (h >= 0) pins f to a specific linear form. **Adaptation**: here h >= 0 is already established from the codomain constraint, and the orbit structure h(f(y))=h(y) replaces Cauchy-additivity.

---

### Prior Progress
None — first round, blank slate.

---

### Dead Ends (Do Not Retry)
None established yet.

---

### Small-Case / Intuition Notes

**Conjecture** (supported by extensive numeric evidence): The COMPLETE solution family is f(x) = x + c for any constant c >= 0.

Key structural observations (all computed, not proved):
1. f(x) = cx only works for c = 1 (verified algebraically: ineq1 discriminant = 8y^2(c^2-1)^2, indefinite for c≠1).
2. f(x) = x^alpha only works for alpha = 1.
3. Non-constant h = f - id (step-function perturbations, sin^2 perturbation) ALL FAIL numerically.
4. f(x) = x + c satisfies BOTH inequalities for any c >= 0 (all reduce to (x-(y+c))^2 >= 0).
5. Plugging x=f(y): forces exact equality f(f(y)) = 2f(y)-y. This pins orbits to arithmetic progressions.
6. h >= 0 forced by codomain.
7. The constraint from ineq1 (after squaring) gives (u-v)^2 >= c_0(c_0+2(u+v)) where c_0 = h(u)-h(v). For distinct orbit steps (a≠b, both positive), orbit elements eventually get "too close" relative to the orbit product constraint. Rational a/b: take m=qn, k=pn iterations, get CONSTANT left side vs growing right side. Irrational a/b: density of {ja-kb} mod 1 makes left side -> 0 while right grows. BOTH give contradictions (labeled conjecture pending full writeup).
8. For b=0 (fixed points): ineq2 gives (y-y_0)^2 >= 4*y_0*a for all A-orbit points y and fixed points y_0, creating cascading forbidden zones that prevent non-trivial mixed configurations.

**Verified clean non-existence**: Step functions with two different additive constants fail ineq1 or ineq2. Example: f(x)=x+1 for x<1, f(x)=x+2 for x>=1 — 28 ineq1 failures and 5 ineq2 failures in 11^2 test grid.
