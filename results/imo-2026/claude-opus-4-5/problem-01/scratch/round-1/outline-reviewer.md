# Outline Review: imo-2026-01 (Round 1)

## Problem Summary

2026 integers > 1 on a blackboard. Move: pick m>1, n>1 from different places, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Prove (a) exactly one M > 1 remains after finitely many moves, (b) M is independent of choices.

---

## Approach: valuation-invariant

**Verdict: APPROVE**

The outline is sound and complete.

**Technique check:** The p-adic valuation decomposition is the natural framework for this problem. The observation that (v_p(m), v_p(n)) -> (min, |diff|) is exactly one step of the subtractive Euclidean algorithm is correct and well-known. This is the standard approach.

**Skeleton validity:**
- Step 1 (decomposition): Correct. gcd(m,n) = prod p^{min(v_p(m), v_p(n))}, and lcm(m,n)/gcd(m,n) = prod p^{|v_p(m) - v_p(n)|}.
- Step 2 (Euclidean identity): gcd(min(a,b), |a-b|) = gcd(a,b). Verified by standard Euclidean algorithm step.
- Step 3 (d_p invariance): Correct. Replacing (a,b) with a pair having the same gcd preserves the gcd of the whole multiset.
- Step 4 (terminal state): gcd(a, 0) = a is the correct convention. At termination {M, 1,...,1}, we have v_p(M) = gcd(v_p(M), 0, ..., 0) = v_p(M) = d_p (initial).
- Step 5 (part b): Follows immediately.
- Step 6 (monovariant): The lexicographic (T, N) monovariant is correct. T = total prime factors, N = count > 1.
  - gcd > 1: T decreases (gcd contributes at least 1 to Omega, which is removed).
  - gcd = 1: T unchanged, N decreases by 1.
- Step 7 (part a): N = 0 impossible because d_p >= 1 for some p (every initial x_i > 1 has a prime factor).

**Load-bearing lemmas:** All three stated with mechanism:
1. Euclidean identity - mechanism: gcd(a, b-a) = gcd(a, b)
2. d_p invariance - mechanism: Euclidean identity preserves gcd of pair
3. M > 1 - mechanism: each x_i > 1 contributes v_p >= 1 for some p

**Cases:** Three cases listed (gcd > 1 both outputs > 1; gcd > 1 one output = 1; gcd = 1). Complete and disjoint.

**Small-case sanity check:** Verified computationally. Board [6, 4, 3] terminates at M = 6, matching d_2 = 1, d_3 = 1.

**No gaps.** Builder can proceed to write the full proof.

---

## Approach: product-monovariant

**Verdict: APPROVE**

The outline is sound with minor gap identified.

**Technique check:** Q = P * 2^N as a single monovariant is a valid alternative. It provides a simpler termination argument (no lexicographic order needed) at the cost of being less elementary (combines product and count).

**Skeleton validity:**
- Step 1: Q = (prod x_i) * 2^{count > 1} is well-defined.
- Step 2-4 (case analysis): Verified. In all three cases Q decreases by at least factor 2.
  - Case 1 (gcd >= 2, ab >= 2): P -> P/gcd, N unchanged. Q -> Q/gcd.
  - Case 2 (gcd >= 2, ab = 1): m = n = gcd. P -> P/gcd, N -> N-1. Q -> Q/(2*gcd).
  - Case 3 (gcd = 1): P unchanged, N -> N-1. Q -> Q/2.
- Step 5: Termination in O(log Q) steps. Correct.
- Step 6: N >= 1 at termination. This relies on "no move produces two 1s", which is stated but needs explicit verification.

**Open gap (minor):** The claim "no move outputs two 1s" needs explicit proof. The outline notes this and provides a sketch: gcd = 1 means ab = mn >= 4 (since m, n >= 2), so ab > 1. If gcd >= 2, then gcd >= 2 > 1. The builder should write this out explicitly.

**Part (b):** Uses the same p-adic invariant as valuation-invariant. Correct.

**Cases:** Same three cases, complete.

**Load-bearing lemmas:** Stated with mechanisms. The "no two 1s" lemma mechanism is present but condensed.

---

## Diversity Assessment

Both approaches share the same invariant for part (b) - the p-adic d_p = gcd of valuations. This is essentially the only natural invariant for this problem; varying it would be contrived.

They differ in the termination argument for part (a):
- **valuation-invariant:** Lexicographic (T, N) monovariant
- **product-monovariant:** Single Q = P * 2^N monovariant

This is adequate diversity for a problem where the invariant is essentially forced. The approaches won't "hit the same wall" since the invariant is known to work.

---

## Ranking Rationale

**valuation-invariant > product-monovariant** because:
1. No gaps vs. one minor gap (the "no two 1s" verification)
2. More elementary (uses standard Omega count rather than combining product with exponential)
3. Cleaner separation of concerns (invariant for (b), monovariant for (a))

Both are viable and buildable.

---

## Registered Approaches

- `valuation-invariant`: p-adic valuation invariant + lexicographic (Omega, count) monovariant
- `product-monovariant`: Q = P * 2^N monovariant + p-adic invariant for uniqueness

---

**build set: valuation-invariant, product-monovariant**
