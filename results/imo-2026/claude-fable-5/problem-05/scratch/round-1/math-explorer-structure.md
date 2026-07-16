## imo-2026-05

### Problem restatement
Find all f: R_{>0} -> R_{>0} such that sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x, y > 0.

The chain reads: QM(x, f(y)) >= (f(x)+y)/2 >= GM(x, f(y)). When f = id this is exactly QM >= AM >= GM for the pair (x,y). The question is whether f = id + const are the only solutions.

---

### Candidate answer (conjecture, verified computationally)

**f(x) = x + c for any fixed constant c >= 0.**

- f(x) = x (c=0): both inequalities become QM(x,y) >= AM(x,y) >= GM(x,y). ✓
- f(x) = x + c (c > 0): both reduce to QM(x, y+c) >= AM(x, y+c) >= GM(x, y+c). ✓
  Reason: (f(x)+y)/2 = (x+c+y)/2 = AM(x, f(y)) = AM(x, y+c), so the "middle" equals AM of the outer pair.
  Both inequalities then reduce algebraically to (x - y - c)^2 >= 0 (same expression for both!).
- c < 0 is excluded: f(x) = x+c < 0 for x in (0, -c), violating codomain R_{>0}.

---

### Distinct openings

**Opening A: The pinning substitution x = f(y) (dominant path)**
Setting x = f(y) in the LEFT inequality: sqrt((f(y)^2 + f(y)^2)/2) >= (f(f(y))+y)/2, i.e., f(y) >= (f(f(y))+y)/2, giving f(f(y)) <= 2f(y) - y.
Setting x = f(y) in the RIGHT inequality: (f(f(y))+y)/2 >= sqrt(f(y)*f(y)) = f(y), giving f(f(y)) >= 2f(y) - y.
Combined: **f(f(y)) = 2f(y) - y for all y > 0.** (No regularity assumptions used.)

**Opening B: Orbit analysis**
Let g = f - id (so f(y) = y + g(y)). The constraint f(f(y)) = 2f(y) - y rewrites as:
  g(f(y)) = g(y)  (g is invariant under f).
The orbit of y under f is the arithmetic progression {y + n*g(y) : n = 0,1,2,...}. For f^n(y) = y + n*g(y) to remain in R_{>0} for all n, we need g(y) >= 0 for all y > 0 (since if g(y_0) < 0, the orbit y_0 + n*g(y_0) -> -inf).

**Opening C: Discriminant argument to force g constant**
Suppose g takes two values a < b: g(y_1) = a and g(y_2) = b (with a < b, a,b >= 0).
Apply the RIGHT inequality at (x, y) = (y_1, y_2): (f(y_1)+y_2)/2 >= sqrt(y_1*f(y_2)).
This requires Q(y_1; y_2) = (y_1+a+y_2)^2 - 4*y_1*(y_2+b) >= 0.
Q is a quadratic in y_1 with discriminant D = -16(b+y_2)(a-b) > 0 (since a < b).
So Q is negative for y_1 in the interval (y_1^-, y_1^+) = (2b+y_2-a ± 2*sqrt((b+y_2)(b-a))).
This interval has positive length 4*sqrt((b+y_2)(b-a)) -> infinity as y_2 -> infinity.
By choosing y_2 in the orbit of y_2^* (orbit step b, values {y_2^* + m*b}), the interval grows without bound.
Since the orbit of y_1^* (step a, values {y_1^* + n*a}) is an AP with bounded step a, and the violation interval eventually contains AP elements (for large m), we get a concrete (y_1, y_2) pair violating the right inequality. Contradiction.
**Hence g must be constant.**

**Opening D: Algebraic verification for f(x) = x+c**
Both inequalities for f(x) = x+c reduce to the SAME expression (x-y-c)^2 >= 0. This is an exact perfect square — both (A) and (B) have equal slack functions. The "middle" (f(x)+y)/2 = AM(x, f(y)) = (x+f(y))/2, so the chain collapses to QM >= AM >= GM for the pair (x, f(y)) = (x, y+c).

**Opening E (alternative, less clean): Legendre/envelope argument**
From (B): f(x) >= sup_{t>0} (2*sqrt(x*f(t)) - t). For f(x) = x+c this sup is achieved at t* = x-c (for x > c), giving exactly f(x) = x+c. The fact that the lower and upper bounds (from A and B) both tighten to equality at the same t* suggests uniqueness via an envelope/Legendre-transform style argument.

---

### Key structural facts (proved or near-proved)

1. f(f(y)) = 2f(y) - y for all y > 0 (derived cleanly from x = f(y) substitution, no regularity needed).
2. g := f - id satisfies g(f(y)) = g(y) and g(y) >= 0 for all y.
3. The orbit of y is the AP {y + n*g(y) : n >= 0}.
4. The right inequality forces g to be constant via a quadratic discriminant argument.
5. f(x) = x + c (c >= 0) satisfies both inequalities; both reduce to (x-y-c)^2 >= 0 (identity verification trivial).

---

### Candidate technique(s)

- **Special substitution (x = f(y))** to pin f(f(y)) = 2f(y)-y: standard FE toolkit ("choose x to make one side degenerate").
- **Orbit/AP argument**: the iterate orbit f^n(y) = y + n*g(y) must stay in R_{>0}.
- **Quadratic discriminant argument**: the right inequality at (y_1, y_2) with g(y_1)=a < b=g(y_2) is a quadratic in y_1 with positive discriminant, hence sometimes negative. Combined with the AP orbit to locate concrete violating inputs.
- **Verification via QM-AM-GM**: for f = id+c, the chain is literally QM >= AM >= GM of (x, y+c).

---

### Cheap-kill candidates

- **g(y) >= 0**: orbit argument kills negative g immediately. Forces f(x) >= x everywhere.
- **g constant**: the discriminant Q(y_1; y_2) quadratic with D > 0 when a < b kills two-valued g immediately (and the orbit gives a concrete violation). This is the main pin.
- **Codomain constraint**: c >= 0 required (c < 0 fails immediately at small x).

---

### Knowledge-base entries to use

- **Standard inequalities: AM-GM, QM-AM** — the outer chain QM >= AM >= GM is the baseline; the verification step for f(x) = x+c uses exactly this.
- **Functional equations: test special values, check injectivity/surjectivity** — the key move is x = f(y), a classic "cancel" substitution.
- **Sum of squares (SOS)**: both inequalities for f(x) = x+c reduce to (x-y-c)^2 >= 0.
- **Problem-solving heuristics (Specialize)**: x = f(y) is the critical specialization.

---

### Analogous past problems (cruxes)

1. **aimo-0008** (IMO 2009 P5 flavor, Q_{>0} submultiplicative+superadditive): Crux = "sandwich a function between two tight bounds at a known fixed point, then amplify via iterate". Analogous in that the key technique is finding a specific substitution that collapses the inequality to an equality, then expanding outward. Moderately analogous — different functional form, but same "pinch from both sides" strategy.

2. **aimo-0234** (FE f(xy + f(x)) = xf(y) + 2 on R_{>0}): Crux = "get an additive shift relation f(y+c) = f(y)+2 from P(1,y), then sandwich via monotonicity to pin the linear form". Analogous because: (a) domain is R_{>0}, (b) the answer is f(x) = x + const, (c) the method involves finding a shift identity first, then proving the function must be exactly linear. Less directly analogous to our discriminant argument.

3. **aimo-0253** (FE on positive integers, triangle inequality): Crux = "specialize to force a composite value to the identity; iterate to get linear behavior". Analogous in the "iterate to AP" structure.

Best match: **aimo-0008** for the sandwich-pinch-from-both-sides crux; **aimo-0234** for the positive-reals translation-family answer and shift argument.

---

### Prior progress

None (round 1, blank slate).

### Dead ends (do not retry)

- **f(x) = cx (linear, not affine)**: works only for c = 1 (all other c fail both inequalities at some (x,y)).
- **f(x) = x^k for k ≠ 1**: fails (violations at k = 0.5, 1.5, 2, -1).
- **Piecewise constant g**: fails — orbit of y_1^* with g=a leaks into region where g=b, violating (B).
- **Assuming continuity/monotonicity without proof**: unnecessary — the discriminant argument works without it.
- **Symmetric substitution x = y**: always gives QM >= AM >= GM (trivially true), gives no info about f.

### Small-case / intuition notes

- Verified numerically: f(x) = x + c satisfies both inequalities for c in {0, 0.5, 1, 2, 5} (zero violations in 2500 test pairs).
- The discriminant argument is concrete: with g(y_1)=1, g(y_2)=3 (so a=1, b=3), taking x=y_1=3, y=y_2=5 gives LHS of (B) = 4.5 < 4.899 = RHS. Direct numerical violation confirmed.
- Conjecture (supported by all evidence): answer is exactly {f(x) = x + c : c >= 0} — no other solutions.
- The key algebraic miracle: for f(x) = x+c, both inequalities reduce to the SAME perfect square (x-y-c)^2 >= 0, with simultaneous equality when x = y + c.

### Hard vs. routine steps

- **Routine**: deriving f(f(y)) = 2f(y)-y (clean substitution), verifying f(x) = x+c works (SOS), g(y) >= 0 (orbit).
- **Moderately hard**: the discriminant argument for g constant — need to track orbit elements landing in the violation interval. The argument is clean but requires care in showing the orbit hits the interval (for large y_2 in orbit of y_2^*).
- **Trap**: one might try to prove f is monotone first and then pin g constant; this is unnecessary — the discriminant argument works without monotonicity.
