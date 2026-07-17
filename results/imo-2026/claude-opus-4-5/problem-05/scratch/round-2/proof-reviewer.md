# Proof Review: IMO 2026 P5

**Problem:** Determine all functions f: R+ -> R+ such that sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x*f(y)) for every x, y > 0.

**Answer claimed:** f(x) = x + c for c >= 0.

---

## Approach 1: orbit-invariance

### Verdict: APPROVE
### Status: solved

### Correctness Score: 10/10
### Completeness/Rigor Score: 9/10
### Progress Score: Complete

### Analysis

**Independently verified key claims:**

1. **Functional equation f(f(y)) = 2f(y) - y (Lemma 1):** At x = f(y), both L' = 4f(y)^2 - (f(f(y)) + y)^2 and R' = (f(f(y)) + y)^2 - 4f(y)^2, so L' + R' = 0. Since L', R' >= 0, both equal 0. This forces f(f(y)) + y = 2f(y). Verified correct.

2. **Algebraic identities (Lemmas 5 & 6):**
   - L' + R' = 2(x - f(y))^2: Verified by computer algebra.
   - L' - R' = 2(g(y) - g(x))(2x + 2y + g(x) + g(y)): Verified by computer algebra.

3. **Orbit invariance g(f(y)) = g(y) (Lemma 2):** From f(f(y)) = 2f(y) - y, g(f(y)) = f(f(y)) - f(y) = (2f(y) - y) - f(y) = f(y) - y = g(y). Correct.

4. **Non-negativity g >= 0 (Lemma 4):** If g(y_0) < 0, then f^n(y_0) = y_0 + n*g(y_0) -> -infinity, contradicting f: R+ -> R+. Correct.

5. **Case 1 (a = 0, b > 0) - Numerical example:** The proof gives x_0 = 1, y_0 = 2, g(x_0) = 0, g(y_0) = 1. Then f(1) = 1, f(2) = 3, and R' = (1+2)^2 - 4*1*3 = 9 - 12 = -3 < 0. This is a direct constraint violation. **Verified by independent calculation.**

6. **Case 2 (0 < a < b) - Growth argument:** For n = round(bt), m = round(at), we have |na - mb| <= (a+b)/2 (verified numerically for multiple a, b values). Then x - f(y) = (x_0 - y_0 - b) + (na - mb) is bounded by a constant K, while LHS = |b-a|*(2x + 2y + a + b) -> infinity with n, m. This violates the constraint (*). **Verified by independent calculation.**

7. **Verification f(x) = x + c works:** Left inequality is QM(x, y+c) >= AM(x, y+c), which is standard QM-AM. Right inequality: (x + c + y)^2 - 4x(y+c) = (x - y + c)^2 + 4c(y-x) + ... verified to equal (x + c - y)^2 - 4c(x-y) + 4cy = (x - y - c)^2 >= 0. **Verified by computer algebra: the factorization is (-c + x - y)^2 >= 0.**

### Minor notes:
- The Case 1 discussion is lengthy with some false starts before the "numerical proof" gives a clean direct contradiction. This is acceptable for a proof document.
- The proof correctly handles all cases: a = 0 with b > 0, and 0 < a < b.

### Conclusion
The proof is complete and correct. Every key step has been independently verified. The answer f(x) = x + c for c >= 0 is correct: the family is shown to satisfy both inequalities, and no other functions work.

---

## Approach 2: differentiability-squeeze

### Verdict: CHANGES REQUESTED
### Status: partial

### Correctness Score: 8/10
### Completeness/Rigor Score: 6/10
### Progress Score: Substantial but incomplete

### Analysis

**Verified claims:**
1. Steps 1-5 are correct: functional equation, orbit invariance, g >= 0, L + R = 2(x - f(y))^2, and the quadratic bound |delta - h| = O(h^2) at x = f(y) + h.

**Gap in Step 6:**
The proof attempts to show g is constant by chaining quadratic bounds. The argument contains several false starts and incomplete sub-claims:

1. The claim "S = f(R+) contains (c, infinity)" is asserted but not rigorously proven. The proof says "As y varies over (0, infinity), the values y + g(y) cover all of (c, infinity)" but this assumes some form of continuity or surjectivity that is not established.

2. The "Lemma (Quadratic regularity implies constancy)" requires the bound to hold for ALL u, u+h > M, but the quadratic bound was only derived for u in Range(f).

**The argument CAN be completed** by noting:
- For Case 0 < a < b: Take t = x_0 + na and s = y_0 + mb both in Range(f) (for n, m >= 1). For large m, choose n so that |t - s| < a. Apply the quadratic bound at s to get |a - b| <= (a^2)/(4(y_0 + mb)) -> 0.
- For Case a = 0, b > 0: The forbidden zone where the constraint fails has length 4*sqrt(b^2 + b*x_0) > b, so the b-orbit must hit it.

But these arguments are not present in the submitted proof. The Step 6 discussion meanders and ends with incomplete reasoning about surjectivity.

### Conclusion
The approach is valid and substantial progress has been made (Steps 1-5 are solid), but Step 6 has gaps. The orbit-invariance proof provides a cleaner, complete solution to the same problem.

---

## Summary

| Approach | Verdict | Status | Key Finding |
|----------|---------|--------|-------------|
| orbit-invariance | APPROVE | solved | Complete, rigorous proof. All steps verified. |
| differentiability-squeeze | CHANGES REQUESTED | partial | Steps 1-5 correct; Step 6 has gaps in surjectivity argument. |

---

## Promotable Lemmas

### From orbit-invariance
**Lemma (Orbit formula for affine functional equations):** If f: R+ -> R+ satisfies f(f(y)) = 2f(y) - y, then g = f - id satisfies g(f(y)) = g(y) and f^n(y) = y + n*g(y).

**Certification:** ACCEPTED. The proof is complete and the statement is correct. This lemma is reusable for similar functional equations.

### From differentiability-squeeze
**Lemma (Quadratic regularity implies constancy):** If g: (M, infinity) -> R satisfies |g(u+h) - g(u)| <= Ch^2 for all u, u+h > M, then g is constant on (M, infinity).

**Certification:** ACCEPTED. The lemma is correct and proved. Note: the issue in the differentiability-squeeze proof is not with this lemma, but with showing the hypothesis applies (that all points are in Range(f)).
