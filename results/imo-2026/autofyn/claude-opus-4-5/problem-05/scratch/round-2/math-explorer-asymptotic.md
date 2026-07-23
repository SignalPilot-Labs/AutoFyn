## imo-2026-05 (Asymptotic/Limit Lens)

**Problem recap**: Find all f: R+ → R+ with √((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(xf(y)) for all x,y > 0.

---

### Structural Identity (model-independent)

Define the left surplus L(x,y) = 2(x²+f(y)²) − (f(x)+y)² ≥ 0 and right surplus R(x,y) = (f(x)+y)² − 4xf(y) ≥ 0. Then:

**L(x,y) + R(x,y) = 2(x − f(y))²   [always, for any f]**

This follows by expanding: 2x²+2f(y)²−4xf(y) = 2(x−f(y))². Both L and R are non-negative and bounded by 2(x−f(y))². Equality L=R=0 iff x=f(y).

For f(x) = x+c: **L = R = (x−y−c)²**. Both inequalities reduce to the SAME expression (x−y−c)² ≥ 0. This is the hallmark of f(x)=x+c.

---

### Distinct Openings

**Opening A — Regularity/Differentiability Route (cleanest)**

Both L and R achieve their minimum value 0 at x = f(y) for each y. If f is C¹:

- dL/dx|_{x=f(y)} = 4f(y) − 2(f(f(y))+y)·f'(f(y)) = 4f(y)·(1 − f'(f(y))) = 0  
  [using f(f(y)) = 2f(y)−y from the equality condition]

- dR/dx|_{x=f(y)} = 2(f(f(y))+y)·f'(f(y)) − 4f(y) = 4f(y)·(f'(f(y))−1) = 0

Both force **f'(f(y)) = 1 for all y > 0**. Since f(x) ≥ x (proved below) and f(x) → ∞ as x → ∞, the range of f on R+ contains all sufficiently large reals. By the connectedness of R+ and continuity of f', the range of f is an interval of the form (c, ∞) for some c ≥ 0, on which f' ≡ 1. Hence f(x) = x + K on that interval. The values on (0, c) are determined by f(f(y)) = 2f(y)−y, which forces f(x) = x+K everywhere. Conclude: **f(x) = x+c for constant c ≥ 0**.

**Opening B — Standard-Means Transform**

Substitute u = x, v = f(y) (valid if f is bijective). The inequality becomes:
QM(u,v) ≥ (f(u) + f⁻¹(v))/2 ≥ GM(u,v).

For f(x) = x+c: f⁻¹(v) = v−c, middle term = (u+c+v−c)/2 = (u+v)/2 = AM(u,v). The double inequality reduces to the standard QM ≥ AM ≥ GM, always true with equality iff u=v (i.e., x=f(y)). Conversely, any f for which AM(f(x),y) = AM(x,f(y)) for all x,y satisfies f(x)−x = f(y)−y = const. The inequality only requires the middle to LIE BETWEEN GM and QM — not be equal to AM — but the structural identity L=R forces the middle to sit exactly at the midpoint between the two surpluses, and this midpoint condition characterizes f(x)=x+c.

**Opening C — Asymptotic Growth Forcing f'/x → 1**

From x = f(y) substitution: equality throughout → **f(f(y)) = 2f(y) − y**.  
Writing f(y) = Ay^α + lower order for large y:
- f(f(y)) ~ A·(Ay^α)^α = A^{1+α}·y^{α²}  
- 2f(y)−y ~ 2Ay^α − y

Matching powers: if α > 1, 2Ay^α dominates so α²=α → α=1; if α=1, coefficient equation: A² = 2A−1 → **(A−1)² = 0 → A=1**.

So **f(x)/x → 1 as x → ∞**. Writing f(x) = x + g(x) with g ≥ 0:
- g(f(y)) = g(y) for all y (orbit-invariance from f(f(y))=2f(y)−y).
- Orbits of g=c>0 are {y₀, y₀+c, y₀+2c, ...} → ∞.
- g is constant on each orbit but may differ between orbits.
- Asymptotic analysis alone does not force g to be constant across orbits; the inequality at specific pairs must do this.

**Opening D — Left Inequality Forces g Constant (Orbit-Collision)**

For any pair (a,b) with g(a)=c₁, g(b)=c₂, the left inequality at (x=a, y=b) reads:
  L(a,b) = a² − 2(c₁+b)a + [2(b+c₂)² − (c₁+b)²] ≥ 0.

Treating this as a quadratic in a with fixed b,c₁,c₂:
- Vertex at a = c₁+b; minimum value = **2(b+c₂)² − 2(c₁+b)² = −2(c₁−c₂)(2b+c₁+c₂)**.
- For c₁ > c₂ ≥ 0 and b > 0: minimum value = **−2(c₁−c₂)(2b+c₁+c₂) < 0**.

Conclusion: **if the orbit of g=c₁ ever passes through x = c₁+b** (where b is any point with g(b)=c₂ < c₁), then L < 0 there. Whether the orbit passes through c₁+b depends on the starting point, but for orbits that "interact" (e.g., when c₁/c₂ is irrational, by Weyl equidistribution, the orbit of g=c₁ comes arbitrarily close to any real number, in particular to c₁+b), a violation is forced. For the competition proof, the differentiability route (Opening A) bypasses this complication.

Verified numerically: g(3)=1, g(2)=0 → L(3,2) = 2(9+4)−(4+2)² = 26−36 = −10 < 0. Any function with g non-constant and orbits that intersect the "dangerous zone" violates the inequality.

---

### Candidate Techniques

- **Standard inequalities** (QM≥AM≥GM): the problem is designed so f(x)=x+c collapses the double inequality to the standard chain.
- **Functional equation analysis**: substitution x=f(y) forces f(f(y))=2f(y)−y; this is the key first step.
- **Critical-point / extremal analysis**: L achieves its minimum 0 at x=f(y); if f is C¹, the zero-derivative condition forces f'≡1. This is the cleanest route.
- **Linear growth forcing**: from the functional equation A²=2A−1 forces the linear coefficient to be 1.

---

### Cheap-Kill Candidates

- **Structural identity L+R=2(x−f(y))²**: immediate, always true. Shows L and R are complementary and governed by (x−f(y))².
- **x=f(y) substitution**: equality throughout, immediately giving f(f(y))=2f(y)−y without any work.
- **f(x) ≥ x**: from right inequality optimized over y (max over y of 2√(xy)−y is x, achieved at y=x), gives f(x) ≥ x.
- **Differentiability short-cut**: if f is C¹ and x=f(y) is the minimum of L, then f'(f(y))=1. This is a one-line derivation once the minimum is identified.

---

### Knowledge-Base Entries to Use

- **Standard inequalities**: AM-GM, QM-AM. Equality cases pin down the configuration (x=f(y)).
- **Functional equations**: test special values (x=f(y)), check injectivity/surjectivity.
- **Sum of squares (SOS) / completing the square**: L = (x−y−c)² for f(x)=x+c is a perfect square.

---

### Analogous Past Problems (Cruxes)

No prior crux-corpus search performed (no read of crux_moves_documentation.md yet). For this problem, the crux move is: "use the equality condition at a special substitution to derive a functional equation for f, then use a minimum/derivative argument to force f to be linear." Standard for functional inequality problems.

---

### Prior Progress

None (Status: unsolved, no approaches built yet).

---

### Dead Ends (Do Not Retry)

- **f(x)/x → 1 alone does not force f(x)=x+c**: g can be non-constant and still satisfy g(f(y))=g(y) with g(x)/x→0. The asymptotic constraint is necessary but not sufficient; the full inequality for all (x,y) is needed.
- **Multiplying L and R does not give new information**: L·R ≤ (L+R)²/4 = (x−f(y))⁴ but this is not tight.
- **Symmetrizing (swapping x↔y) the right inequality**: gives a trivial factoring (x−y)²≥0 after multiplication, no new constraint.

---

### Small-Case / Intuition Notes

**Conjecture**: f(x) = x+c for any constant c ≥ 0. Evidence:
- f(x)=x+c satisfies both inequalities (both reduce to (x−y−c)²≥0, verified symbolically).
- The substitution u=x, v=f(y) transforms the double inequality to the standard QM≥AM≥GM exactly when f(x)=x+c.
- Numerical test: f(x)=x+1 satisfies all inequalities; f(x)=2x violates f(f(y))=2f(y)−y (gives 4y≠3y); g piecewise-constant violates left inequality at nearby points.
- f(x)=x² violates: f(f(y))=y⁴ but 2f(y)−y=2y²−y, not equal for general y.

**Key asymptotic finding**: f'(f(y))=1 for all y (from minimum-of-L argument, assuming C¹), which forces f'≡1 and f(x)=x+c. The constraint c≥0 comes from f:R+→R+ (need f(x)>0 for all x>0; f(x)=x+c>0 for x>0 iff c≥0). This is LABELED AS CONJECTURE until a rigorous proof is assembled.
