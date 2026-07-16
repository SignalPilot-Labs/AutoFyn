## imo-2026-05

### Problem restatement
Find all f: R_{>0} -> R_{>0} such that sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y > 0.

This is QM(x, f(y)) >= middle >= GM(x, f(y)), where the middle is (f(x)+y)/2 — not the standard AM(x, f(y)).

---

### Answer conjecture (strong computational evidence)
**f(x) = x + c for any constant c >= 0.**

Tested numerically: f(x)=x+c satisfies both inequalities for c = 0, 0.1, 0.5, 1, 2, 10, 100 — zero violations over 2500 test pairs. Every other form tested fails:
- f(x) = cx (c ≠ 1): fails left inequality (left violations: 435/2500)
- f(x) = x^k (k ≠ 1): fails both
- f(x) = x + exp(-x), x + 1/x, sqrt(x)+1: all fail
- f(x) = x + 1 + eps*sin(10x) for ANY eps > 0: fails immediately (both violations)

---

### Distinct openings

**Opening 1: f(x)+y = x+f(y) forced (algebraic reduction)**
For f(x) = x+c: f(x)+y = (x+c)+y = x+(y+c) = x+f(y). So middle = (f(x)+y)/2 = (x+f(y))/2 = AM(x,f(y)). The inequality chain becomes QM(x,f(y)) >= AM(x,f(y)) >= GM(x,f(y)), which is the standard QM-AM-GM chain — always true. Both slacks are identical:
- 2(x^2+f(y)^2) - (f(x)+y)^2 = (x-f(y))^2
- (f(x)+y)^2 - 4x*f(y) = (x-f(y))^2

Both equal (x-f(y))^2 >= 0, with equality exactly at x = f(y) (i.e., y = x-c).

**Opening 2: Necessary condition f(f(y)) = 2f(y)-y**
Setting x = f(y_0) in the full inequality: LHS = QM(f(y_0), f(y_0)) = f(y_0) and RHS = GM(f(y_0), f(y_0)) = f(y_0), so both outer terms equal f(y_0). This forces the middle f(y_0) too: (f(f(y_0))+y_0)/2 = f(y_0), hence **f(f(y)) = 2f(y) - y** for all y > 0. In terms of g = f - id: g(y+g(y)) = g(y) (g is constant on f-orbits).

**Opening 3: Differentiability argument forcing f' = 1**
From x = f(t): the right inequality at (x=f(t), y=s) gives (2f(t)-t+s)^2 >= 4f(t)*f(s) for all s, with equality at s=t (since f(f(t)) = 2f(t)-t). So s=t minimizes h(s) = (2f(t)-t+s)^2 - 4f(t)*f(s) >= 0. Differentiating at the minimum: h'(t) = 0 gives 2(2f(t)) - 4f(t)*f'(t) = 0, hence **f'(t) = 1 for all t**, so f(t) = t+c.

**Opening 4: Finite-difference squeezing (avoids differentiability assumption)**
Applying the left inequality at (x=f(t), y=s) AND (x=f(s), y=t), with u=f(s), v=f(t), p=t-s>0:
- p(4u+p) <= 2(v-u)(v+u) <= p(4v-p)
Since f(x) >= 2*sqrt(x*f(y0))-y0 -> infty as x -> infty, f is unbounded. For large u, the bounds squeeze (v-u)/p -> 1, giving f(t)-f(s) = t-s for all t > s. Combined with constraint A, this forces g(y) = f(y)-y = constant.

**Opening 5: Fixed-point / iteration approach**
The right inequality at x=f(t) gives: f(s) <= (2f(t)-t+s)^2/(4f(t)) for all s, with equality at s=t. So f(y) = inf_{t>0} (2f(t)-t+y)^2/(4f(t)) for all y. This is a self-referential fixed-point equation that pins f. For f(y)=y+c, the infimum over t is achieved at t=y giving value y+c=f(y) exactly. Proving uniqueness of the fixed point (e.g., by the iterate approach as in aimo-0234) gives f(x)=x+c.

---

### Candidate techniques
- Standard QM-AM-GM chain (sufficiency is trivial once f(x)+y = x+f(y) is recognized)
- Functional equation methods: pinning via tightness/equality case + differentiating at minimum
- Cauchy-type: once g = f-id satisfies g(y+g(y)) = g(y) and g >= 0, force g = constant by the finite-difference squeezing or by unboundedness + the sandwich bound

### Cheap-kill candidates
- Setting x = f(y) in the original inequality squeezes the middle to equal both sides, immediately giving f(f(y)) = 2f(y)-y. This is the foundational step — cheap and key.
- The observation that f(x)+y = x+f(y) iff f(x)-x = constant; any deviation from this is ruled out computationally (oscillation kills both inequalities at once).

### Knowledge-base entries to use
- **Standard inequalities: AM-GM, QM-AM, QM-AM-GM chain** (sufficiency proof)
- **Functional equations: test special values, check injectivity/surjectivity** (setting x=f(y))
- **SOS / completing the square**: both slacks are perfect squares (x-f(y))^2
- **Problem-solving heuristics: specialize** (x = f(y) is the killer substitution)

### Analogous past problems (cruxes)

1. **aimo-0234** (f(xy+f(x)) = xf(y)+2): The crux move "drive a free variable to infinity to force an approximate affine bound to be exact" is analogous. Once a periodic shift f(y+c)=f(y)+2 is established, monotonicity + sandwich between step functions pins f exactly. Analogous to our squeeze approach. Problem_id: aimo-0234.

2. **aimo-0097**: Swap variables in a two-variable identity and equate to force h(x)/x = constant (extract that a ratio is constant from a symmetric identity). Analogous to our step where swapping x and y in the right inequality and combining gives the finite-difference bound forcing slope = 1. Problem_id: aimo-0097.

3. **aimo-0089** (inequality-based FE): "reinterpret a functional inequality as a supporting-line bound, then differentiate at the interior maximizer to get f'(midpoint) = secant slope." Analogous to our differentiating h(s) at s=t (the minimizer) to get f'=1. Problem_id: aimo-0089.

### Prior progress
None (fresh run).

### Dead ends (do not retry)
- f(x) = cx (c ≠ 1): fails the left inequality (QM(x,cy) >= (cx+y)/2 requires c = 1/sqrt(something), but doesn't work globally).
- f(x) = x^k (k ≠ 1): fails both inequalities for large/small x.
- f(x) = x + non-constant g(x): all tested forms fail immediately. Even tiny sinusoidal perturbations (eps*sin(10x) with eps=0.001) produce violations.

### Small-case / intuition notes (all labeled as conjecture or evidence)

**Conjecture (strong numerical evidence):** The answer set is exactly {f(x) = x + c : c >= 0, c constant}.

**Key computed identities (exact, not conjectures):**
- For f(x)=x+c: (f(x)+y)^2 - 4x*f(y) = (x - f(y))^2 (right slack is perfect square)
- For f(x)=x+c: 2(x^2+f(y)^2) - (f(x)+y)^2 = (x - f(y))^2 (left slack same perfect square)
- Both equalities hold iff x = f(y), i.e., y = x-c (for x > c).

**Equality structure:**
- Both LHS=MID=RHS simultaneously iff x = f(y). From x=f(y) and the constraint f(f(y))=2f(y)-y: this forces the equality in the constraint but NOT simultaneously f(x)=y (that would force f(y)=y, c=0).
- The right inequality is tight at x = f(y); the left inequality is also tight at x = f(y).
- For c > 0, the equality locus is the curve x = y+c (a translation of the diagonal), not the diagonal itself.

**Why f must satisfy g=constant:** The orbit argument: f^n(y) = y + n*g(y) for all n >= 1 (iterated from f(f(y))=2f(y)-y). For f: R_{>0} -> R_{>0}, we need f(y) = y + g(y) > 0. Since f(x) is unbounded (from right ineq: f(x) >= 2*sqrt(x*f(y0))-y0 grows as sqrt(x)), and g(y+g(y)) = g(y), if g is non-constant the finite-difference squeeze forces a contradiction. (Conjecture — need formal proof.)

**Proof route for necessity (most promising, for outliner):**
1. From x=f(y): f(f(y)) = 2f(y)-y. [RIGOROUS — just squeeze the chain]
2. Right ineq at x=f(t): (2f(t)-t+s)^2 >= 4f(t)*f(s) with equality at s=t. So t minimizes this. [RIGOROUS]
3a. If differentiable: h'(t) = 0 gives f'(t) = 1 everywhere. [RIGOROUS given differentiability]
3b. Without differentiability: finite-difference bounds p(4u+p) <= 2(v-u)(v+u) <= p(4v-p) + unboundedness argument -> f(t)-f(s) = t-s. [Gap — needs closure]
4. f(y) = y+c with c >= 0 from domain requirement. [RIGOROUS given f'=1 or finite-diff result]
