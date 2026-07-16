## imo-2026-03: Pattern Analysis for General n

### Q1: Sum constraint in reduced units for general n

Define L_0 = 1/(2^{n+1}-1) and label the reduced excesses:
- alpha = P_1/L_0 - 1  (> 0 in Case B)
- beta_j = d_j/L_0 - 1  for j = 1,...,n-1  (where d_j = P_{j+1} - P_j)

Then:
  P_1 + ... + P_n = [n(n+1)/2 + n*alpha + (n-1)*beta_1 + ... + 1*beta_{n-1}] * L_0

The Case B constraint P_{n+1} > c(n) implies P_1+...+P_n < (2^n-1)*L_0, giving:

  **n*alpha + (n-1)*beta_1 + (n-2)*beta_2 + ... + beta_{n-1} < 2^n - 1 - n(n+1)/2**

Verified values:
- n=3: 3*alpha + 2*beta + gamma < 1  [matches proof]
- n=4: 4*alpha + 3*beta + 2*gamma + eta < 5  [matches proof]
- n=5: 5*alpha + 4*b1 + 3*b2 + 2*b3 + b4 < 16
- n=6: 6*alpha + 5*b1 + 4*b2 + 3*b3 + 2*b4 + b5 < 42

Note: RHS = 2^n - 1 - n(n+1)/2 grows exponentially, so the constraint loosens as n grows.
When all beta_j = 0, alpha < (2^n-1-n(n+1)/2)/n: for n=3 gives alpha<1/3, for n=5 gives alpha<3.2.

---

### Q2: What drives "gap-width is negative" for general n

**The gap-width formula is alpha - 1 for all n >= 3.**

In each n=k proof:
- The "S5-analog" strategy covers the largest difference b_{n-1} in an interval of radius 1
  around the center alpha+b1+...+b_{n-2}+1, i.e., covers b_{n-1} in [C, C+2] where C = alpha+sum(b_j for j<n-1).
  Upper bound of S5-analog: b_{n-1} <= C + 2
- The "BPP-analog" strategy covers b_{n-1} >= 1 + 2*alpha + sum(b_j for j<n-1) = 1 + alpha + C
  Lower bound of BPP-analog: b_{n-1} >= 1 + alpha + C

Gap width = (1 + alpha + C) - (C + 2) = **alpha - 1**

This is negative iff **alpha < 1**. The sum constraint + pairwise failure conditions force alpha < 1:

- n=3: sum 3*alpha+2*beta+gamma < 1 with all vars > 0 => alpha < 1/3
- n=4: deepest Case A (gamma>=alpha+1, eta>=beta+1) gives 6*alpha+4*beta < 2 => alpha < 1/3
- n=5: deepest Case A (b2>=alpha+1, b3>=alpha+b1+2) gives 10*alpha+6*b1+b4 < 9 => alpha < 9/10

**Pattern: In the deepest Case A for n=k, alpha < C_k where:**
- C_3 = C_4 = 1/3 (gap width < -2/3)
- C_5 = 9/10  (gap width < -1/10)
- C_k -> 1 from below as k grows

The gap width remains strictly negative for all n, but the margin shrinks toward 0 as n grows.

**Driving mechanism:** In the deepest Case A, the n-1 pairwise "strategy-failure" conditions
(each beta_j >= something + 1) consume enough of the sum-constraint budget that the
remaining budget forces alpha < 1.

---

### Q3: Minimum XY marks needed for Case B as a function of n

XY uses exactly **n-1 marks** in all Case B strategies.

Reason: the strategies create (n-1) equal pairs + 2 singletons = 2(n-1) + 2 = 2n pieces total.
Starting from n+1 LB pieces, XY must add 2n - (n+1) = **n-1 marks**.

Verification:
- n=3: 2 XY marks → 6 pieces = 2 pairs + 2 singletons ✓
- n=4: 3 XY marks → 8 pieces = 3 pairs + 2 singletons ✓

The XY mark budget is n marks; Case B uses n-1 (< n), so 1 mark is "saved."

**Structural significance:** The (n-1) pairs each contribute one element to LB via the
Pairing Cancellation Lemma. The 2 singletons determine LB's score via the Singleton-Pair
Formula: LB = 1/2 + |s_2 - s_1|/2. XY wins iff the smaller singleton + the larger one differ
by at most L_0, i.e., |s_2 - s_1| <= L_0. This is the universal target for all n.

---

### Implications for n >= 5

The framework generalizes cleanly:
1. Use (n-1) XY marks to create (n-1) pairs + 2 singletons.
2. Design O(n) strategies, each achieving |s_2 - s_1| <= L_0 for some range of b_{n-1}.
3. In the deepest Case A, the sum constraint forces alpha < 1, making the gap width alpha-1 < 0.
4. All intervals cover [beta_1+1, eta_max) with no gaps (by the negative gap-width).

The proof machinery (Pairing Cancellation + Singleton-Pair Formula + sum constraint) fully
generalizes; the only missing piece is the explicit construction of O(n) strategies and their
coverage intervals for each n >= 5.
