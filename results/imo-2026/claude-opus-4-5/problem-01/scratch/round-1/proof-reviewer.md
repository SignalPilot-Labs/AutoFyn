# Proof Review: IMO 2026-01

## Problem Statement
2026 integers > 1 on a blackboard. Move: pick m>1, n>1 from different places, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Continue while possible.
(a) Prove: after finitely many moves, exactly one M > 1 remains.
(b) Prove: M does not depend on choices.

---

## Approach 1: `valuation-invariant`

**Builder's Status:** solved

### Load-Bearing Step Verification

The key mathematical claim is **Lemma 2 (Euclidean identity):**
> gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta) for non-negative integers alpha, beta.

**Independent verification:** WLOG assume alpha <= beta. Then min = alpha, |diff| = beta - alpha.
By the Euclidean algorithm: gcd(alpha, beta) = gcd(alpha, beta - alpha) (since gcd(a, b) = gcd(a, b mod a) and here alpha <= beta).
This equals gcd(alpha, beta - alpha) = gcd(min(alpha, beta), |alpha - beta|). Verified.

**Tested computationally** for all 0 <= alpha, beta < 20: passed.

### Case Completeness

**Lemma 4 (Monovariant):** Three cases analyzed:
1. Case 1 (gcd = 1): T unchanged, N decreases by 1. Verified.
2. Case 2 (gcd >= 2 and lcm/gcd >= 2): T decreases by Omega(g) >= 1. Verified.
3. Case 3 (gcd >= 2 and lcm/gcd = 1, i.e., m = n): T decreases by Omega(m) >= 1. Verified.

All cases are disjoint and exhaustive. No gaps.

### Lemma 6 (M > 1)

The proof claims d_p >= 1 for some prime p. The argument:
- Pick any initial entry x_{i_0} > 1; it has a prime factor p with v_p(x_{i_0}) >= 1.
- d_p = gcd of all v_p(x_i). Some might be 0, but gcd(0, a) = a.
- Since v_p(x_{i_0}) >= 1 is included, and gcd of a multiset containing at least one positive integer is >= 1, we have d_p >= 1.

**Verified:** gcd([0, 0, 1, 2]) = 1, gcd([0, 2, 4]) = 2, etc. Correct.

### Rigor Assessment

- **No hand-waving:** All steps justified explicitly.
- **No skipped cases:** All three cases in Lemma 4 covered.
- **Theorems named:** Euclidean algorithm cited.
- **Convention stated:** gcd(a, 0) = a stated explicitly.

### Verdict

**Status: solved**
**Verdict: APPROVE**

The proof is complete and rigorous. Every step is valid.

---

## Approach 2: `product-monovariant`

**Builder's Status:** solved

### Load-Bearing Step Verification

Same Euclidean identity as above - verified.

The alternative monovariant Q = P * 2^N:
- Case 1 (d >= 2, ab >= 2): P' = P/d, N' = N, so Q' = Q/d <= Q/2. Verified.
- Case 2 (d >= 2, ab = 1, i.e., m = n = d): P' = P/d, N' = N-1, so Q' = Q/(2d) <= Q/4. Verified.
- Case 3 (d = 1): P' = P, N' = N-1, so Q' = Q/2. Verified.

**Tested computationally** for 2 <= m, n < 30: all moves decrease Q by factor >= 2.

### No-Two-Ones Lemma

Claim: outputs (d, ab) can't both be 1.
Proof: If d = 1 and ab = 1, then a = b = 1, so m = da = 1 and n = db = 1.
But move requires m > 1 and n > 1. Contradiction. Verified.

### N >= 1 Argument

The proof says: "each move produces at least one output > 1. Therefore N >= 1 throughout."

This is slightly informal but correct. Rigorous version:
- Process runs only when N >= 2 (need two entries > 1).
- Each move replaces two > 1 with at least one > 1 (by no-two-ones lemma).
- So N decreases by at most 1 per move.
- Starting from N = 2, after the move N >= 1.
- Process stops when N < 2, i.e., N <= 1, and we've shown N >= 1.
- Hence N = 1 at termination.

The logic is sound despite informal presentation.

### Small Example Verification

Board = {6, 4, 3}:
- d_2 = gcd(1, 2, 0) = 1
- d_3 = gcd(1, 0, 1) = 1
- Predicted M = 2^1 * 3^1 = 6

Traced operation sequence ends with M = 6. Verified.

### Rigor Assessment

- **No hand-waving:** Steps are explicit, though N >= 1 argument could be slightly more formal.
- **No skipped cases:** All three cases covered.
- **Theorems named:** Euclidean algorithm referenced.
- **Verification:** Small example worked out.

### Verdict

**Status: solved**
**Verdict: APPROVE**

The proof is complete and rigorous. The N >= 1 argument is slightly informal but mathematically sound.

---

## Summary

| Approach | Builder Status | True Status | Verdict |
|----------|---------------|-------------|---------|
| valuation-invariant | solved | solved | APPROVE |
| product-monovariant | solved | solved | APPROVE |

Both approaches provide complete, rigorous proofs of parts (a) and (b). Either can be used as the canonical solution. The valuation-invariant proof has slightly cleaner presentation of the M > 1 argument; the product-monovariant proof includes a helpful verification example.

**Recommendation:** Use valuation-invariant as the canonical proof in current.md due to its cleaner structure.

---

## Promotable Lemmas

### From valuation-invariant:
1. **Euclidean identity for valuation pairs:** Approved. Statement correct, proof complete.
2. **Valuation-gcd invariance:** Approved. Statement correct, proof complete.

### From product-monovariant:
1. **Euclidean identity for gcd:** Same as above, already captured.
2. **No-two-ones lemma:** Approved. Statement correct, proof complete.
