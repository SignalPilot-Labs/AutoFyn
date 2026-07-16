## imo-2026-05

### Problem restatement
Find all f: R_{>0} -> R_{>0} such that sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y > 0.
Left inequality: QM(x, f(y)) >= (f(x)+y)/2. Right inequality: (f(x)+y)/2 >= GM(x, f(y)).

---

### Answer (strongly supported by computation)

**f(x) = x + c for every constant c >= 0.**

NOT just f(x) = x. The entire one-parameter family f(x) = x + c (c >= 0) satisfies the system. Verified numerically for c in {0, 0.01, 0.1, 0.5, 1, 2, 5, 100} with 10,000 random (x,y) pairs each — zero violations.

---

### Algebraic identity for the solution family

For f(x) = x + c, BOTH margins equal the same expression:

  LHS^2 - MID^2 = (x^2 + (y+c)^2)/2 - (x+c+y)^2/4 = (x - (y+c))^2/4 = (x - f(y))^2/4 >= 0

  MID^2 - RHS^2 = (x+c+y)^2/4 - x(y+c) = (x - (y+c))^2/4 = (x - f(y))^2/4 >= 0

Both equalities hold simultaneously when x = f(y), i.e., x = y + c.

---

### Key substitution: x = f(y) forces f(f(y)) = 2f(y) - y

At x = f(y):
- LEFT ineq: sqrt(f(y)^2) = f(y) >= (f(f(y)) + y)/2, so **f(f(y)) <= 2f(y) - y**
- RIGHT ineq: (f(f(y)) + y)/2 >= sqrt(f(y)*f(y)) = f(y), so **f(f(y)) >= 2f(y) - y**

Combined: **f(f(y)) = 2f(y) - y exactly for all y > 0.** (Both inequalities are simultaneously tight here.)

---

### Derived structural facts

1. **f is injective.** If f(a) = f(b), then f(f(a)) = 2f(a) - a and f(f(b)) = 2f(b) - b. Since f(a) = f(b), these give 2f(a) - a = 2f(a) - b, so a = b.

2. **f(y) >= y for all y > 0.** If f(y_0) < y_0 for some y_0, the orbit y_0, y_0 + d, y_0 + 2d, ... (with d = f(y_0) - y_0 < 0, arithmetic progression from f(f(y)) = 2f(y)-y) eventually becomes negative, contradicting f: R>0 -> R>0.

3. **f(x) + f^{-1}(x) = 2x for all x in range(f).** Apply f^{-1} to f(f(y)) = 2f(y) - y: substitute z = f(y), get f(z) + f^{-1}(z) = 2z.

4. **d = f - id is constant on orbits.** Let d(y) = f(y) - y >= 0. Then d(y+d(y)) = d(y) for all y (from f(f(y)) = 2f(y)-y).

---

### The key argument that d is constant (for differentiable f)

From d(y + d(y)) = d(y), differentiate with respect to y:
  d'(y + d(y)) * (1 + d'(y)) = d'(y).

The orbit {y, y+d(y), y+2d(y), ...} has d CONSTANT at value d(y). So along the orbit, d is constant, hence d' = 0 at y + d(y). Thus:
  0 * (1 + d'(y)) = d'(y) => d'(y) = 0.

This holds for ALL y > 0, so d is constant. Hence **f(x) = x + c** for some c = d >= 0.

---

### Critical point argument (alternative)

For fixed x, the function g(y) = (f(x)+y)/2 - sqrt(x*f(y)) achieves its MINIMUM value of 0 at y = y_0 where f(y_0) = x (from the equality case). So y_0 is a minimizer of g, and if f is differentiable:

  g'(y_0) = 1/2 - x*f'(y_0)/(2*sqrt(x*f(y_0))) = 1/2 - f(y_0)*f'(y_0)/(2*f(y_0)) = (1 - f'(y_0))/2 = 0

=> **f'(y_0) = 1 for all y_0 > 0** (since x = f(y_0) ranges over all of range(f)) => **f(y) = y + c.**

---

### Witnesses that kill non-solution candidates

**f(x) = cx (c != 1):** LEFT violated, RIGHT always holds.
- Discriminant of the quadratic form (in t = x/y) for the LEFT ineq: 8(c^2-1)^2 > 0 for c ≠ 1.
- c = 2, x = 2, y = 1: LHS = sqrt((4+4)/2) = 2.0, MID = (4+1)/2 = 2.5. LEFT VIOLATED by 0.5.
- c = 2, x = 20, y = 10: LHS = 20.0, MID = 25.0. LEFT VIOLATED by 5.0.
- The right ineq (cx-y)^2/4 >= 0 is NEVER violated for f(x)=cx.

**f(x) = x^a (a != 1):** BOTH violated.
- a = 0.5, x = 100, y = 8.7: RIGHT violated by 7.8.
- a = 1.5, x = 100, y = 7.2: LEFT violated by 431.6.

**f(x) = x + 1/x:** BOTH violated.
- f(f(y)) - (2f(y)-y) = -1/(y^3+y) ≠ 0, so the key constraint fails.
- x = 0.01, y = 1.93: LEFT violated by 49.2; x = 100, y = 0.01: RIGHT violated by 50.0.

**Non-constant d satisfying functional equation:** Impossible.
- The orbit condition d(y + d(y)) = d(y) combined with the right inequality at (x=1, y=2) with d(1)=0.5, d(2)=3: (f(1)+2)^2 = (1.5+2)^2 = 12.25 < 4*1*5 = 20. VIOLATED.
- General: large d(y) relative to d(x) violates (f(x)+y)^2 >= 4x*f(y).

---

### Distinct openings

1. **Substitution-equality route (algebraic):** Substitute x = f(y) to force f(f(y)) = 2f(y) - y. Then argue f(y) >= y (orbit argument). Then use the derivative condition g'(y_0) = 0 at the equality point to force f'(y) = 1 everywhere (requires assuming f differentiable or proving it). Conclude f(x) = x + c.

2. **Algebraic identity route:** Show directly that for f(x) = x+c both margins = (x-f(y))^2/4. Verify (direction 1: sufficiency). For necessity: any function where one margin can be written as (x-f(y))^2/4 must satisfy f(x) + y = x + f(y) for all x,y, forcing d = const.

3. **Orbit + monotonicity route (avoids differentiability):** Prove f(y) >= y; prove d is constant on orbits; then show d must be constant globally using: from the right ineq at (x, x-d(x)), the "optimal" bound gives d(x-d(x)) = d(x) (equality). Combined with d(x+d(x)) = d(x), deduce d is invariant under both +d(x) and -d(x), which for a continuous function on R>0 forces d to be constant.

4. **Squeeze route:** Both inequalities give simultaneously: f(x) >= sup_y[2*sqrt(x*f(y)) - y] and f(x) <= inf_y[sqrt(2(x^2+f(y)^2)) - y]. For f(x) = x+c, both extremes equal x+c exactly (at y = x-c). The outliner should check whether these "Legendre-type" bounds alone force f(x) = x+c without differentiability.

---

### Candidate technique(s)

- Functional equations: substitution forcing equality conditions (x = f(y) is the key substitution).
- Standard inequalities: AM-GM, QM-AM (but applied to the equality conditions, not to prove the main ineqs — those are weaker than AM-GM applied directly).
- Differentiation of functional equation (if assuming smooth f).
- Orbit analysis: the arithmetic progression structure.

---

### Cheap-kill candidates

- **Injectivity:** Immediate from f(f(y)) = 2f(y) - y (proved in 2 lines, no computation).
- **f(y) >= y:** 3-line orbit stability argument — if f(y_0) < y_0, the arithmetic orbit leaves R>0.
- **Discrimination of f(x) = cx:** The quadratic form discriminant 8(c^2-1)^2 > 0 for c ≠ 1.

---

### Knowledge-base entries to use

- **Standard inequalities (AM-GM, QM-AM):** Named explicitly. The left ineq is QM >= (f(x)+y)/2 and the right is (f(x)+y)/2 >= GM. At x = f(y), QM(x,x) = AM(x,x) = GM(x,x) = x, so all three collapse.
- **Functional equations:** "test special values, check injectivity/surjectivity."
- **Problem-Solving Heuristics (Pólya):** "Specialize: plug in extreme or symmetric values."
- **Sum of squares (SOS):** Both margins = (x-f(y))^2/4 (a perfect SOS identity).

---

### Analogous past problems (cruxes)

1. **aimo-0234** (problem_id: aimo-0234): "Sandwich a monotone unknown function between the floor and ceiling step-functions generated by an additive shift relation." The problem is f(xy + f(x)) = xf(y) + 2 with solution f(x) = Kx + const. Crux: the substitution gives f(y + f(1)) = f(y) + 2, an additive shift; then sandwich using monotonicity to pin f exactly. Analogous here because our x = f(y) substitution gives f(f(y)) = 2f(y) - y, a "shift-type" recurrence, and we need to extract f from it.

2. **aimo-0255** (problem_id: aimo-0255): "Combine a two-sided sandwich on f(f(t)) — lower bound from one substitution and affine ceiling as upper bound — to descend to a pointwise lower bound on f." Analogous because we derive f(f(y)) = 2f(y) - y as a two-sided constraint (one from each inequality).

3. **aimo-0008** (problem_id: aimo-0008): "Convert a one-sided bound into equality by sandwiching against a known exact value." The problem has two inequalities on f (submultiplicative + superadditive); the crux: knowing f(a) = a, use the two bounds to sandwich and extract f(x) = x for all x. Highly analogous: our two inequalities together force equality at x = f(y), and from that equality we pin down f.

---

### Prior progress

None (round 1, no prior approaches).

---

### Dead ends (do not retry)

None yet established (round 1).

---

### Small-case / intuition notes (all labeled as conjectural until proved)

- **Conjecture (strongly supported):** The answer is f(x) = x + c for all c >= 0, not just f(x) = x.
- **Evidence:** Numerically verified for c in {0, 0.01, 0.1, 0.5, 1, 2, 5, 100}, all pass with zero violations.
- **Algebraic identity (PROVED, not conjectural):** For f(x) = x+c, both margins = (x - f(y))^2/4.
- **Functional equation (PROVED from substitution x=f(y)):** f(f(y)) = 2f(y) - y for any solution.
- **f(y) >= y (PROVED):** Orbit stability argument is rigorous.
- **Injectivity (PROVED):** 2-line argument from f(f(y)) = 2f(y)-y.
- **Conjectural (not yet fully proved):** That the right ineq forces d to be constant without assuming differentiability. The differentiability argument is clean: d'(y+d(y)) * (1+d'(y)) = d'(y) + d is constant on orbits + d'(y+d(y)) = 0 => d'(y) = 0.

### Gap for the builder

The main gap is the NON-DIFFERENTIABILITY case: can we prove f(x) = x + c for a general (possibly discontinuous) f: R>0 -> R>0 satisfying the system? The differentiable case is settled. If the problem intends to allow discontinuous f, more work is needed (e.g., the Legendre-type squeeze argument or the orbit-shift argument for continuous f).
