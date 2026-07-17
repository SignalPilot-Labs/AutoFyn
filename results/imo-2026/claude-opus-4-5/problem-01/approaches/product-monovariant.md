## Status
solved

## Approaches tried
- product-monovariant: Q = P * 2^N monovariant for termination + p-adic invariant for uniqueness — worked

## Current best
Complete proof of both (a) and (b).

## Full proof

**Problem.** There are 2026 integers greater than 1 on a blackboard. In a move, pick two integers m > 1 and n > 1 from different places and replace them with gcd(m,n) and lcm(m,n)/gcd(m,n). Continue while possible.
(a) Prove that after finitely many moves, exactly one integer M > 1 remains.
(b) Prove that M does not depend on the choices made.

---

### Notation and Setup

Let the board be a multiset B = {x_1, ..., x_k} of positive integers (initially k = 2026, all x_i > 1). Define:
- P = product of all entries = x_1 * x_2 * ... * x_k
- N = count of entries greater than 1 = #{i : x_i > 1}

For the move (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)), write d = gcd(m,n) and note that lcm(m,n) = mn/d, so lcm(m,n)/gcd(m,n) = mn/d^2. Setting m = da, n = db where gcd(a,b) = 1, we have d = gcd(m,n), and the operation becomes:
  (da, db) -> (d, ab).

---

### Part (a): Termination and Exactly One M > 1

**Step 1: Define the monovariant.**

Define Q = P * 2^N. We claim Q strictly decreases by at least a factor of 2 with each move.

**Step 2: Case analysis.**

Write m = da, n = db with d = gcd(m,n) and gcd(a,b) = 1. The move replaces (da, db) with (d, ab).

**Case 1: d >= 2 and ab >= 2** (both outputs > 1).

The product changes by a factor of (d * ab)/(da * db) = 1/d. So:
- P' = P / d <= P / 2
- N' = N (unchanged, since both inputs were > 1 and both outputs are > 1)
- Q' = P' * 2^{N'} = (P/d) * 2^N = Q / d <= Q / 2

**Case 2: d >= 2 and ab = 1** (i.e., a = b = 1, meaning m = n = d).

Since ab = 1 and a, b are positive integers, we must have a = b = 1. Thus m = d * 1 = d and n = d * 1 = d, so the inputs are m = n = d. The outputs are (d, 1).

The product changes by a factor of (d * 1)/(d * d) = 1/d. So:
- P' = P / d <= P / 2
- N' = N - 1 (we replaced two entries > 1 with one entry > 1 and one entry = 1)
- Q' = P' * 2^{N'} = (P/d) * 2^{N-1} = Q / (2d) <= Q / 4

**Case 3: d = 1** (coprime inputs, so ab = mn).

The outputs are (1, mn). Since m >= 2 and n >= 2, we have mn >= 4 > 1.

The product changes by a factor of (1 * mn)/(m * n) = 1. So:
- P' = P (unchanged)
- N' = N - 1 (we replaced two entries > 1 with one entry = 1 and one entry > 1)
- Q' = P' * 2^{N'} = P * 2^{N-1} = Q / 2

**Conclusion from cases:** In all three cases, Q' <= Q / 2. Since Q is a positive integer and decreases by at least half each step, the process terminates in at most log_2(Q_initial) moves.

**Step 3: Exactly one M > 1 remains.**

**Lemma (No move produces two 1s):** A single move never outputs two copies of 1.

*Proof.* The outputs of the move are (d, ab) where d = gcd(m,n), m = da, n = db, and gcd(a,b) = 1.

Suppose for contradiction that both outputs equal 1, i.e., d = 1 and ab = 1.

From ab = 1 with a, b positive integers: a = b = 1.
From a = b = 1: m = da = 1 * 1 = 1 and n = db = 1 * 1 = 1.

But the move requires m > 1 and n > 1. This is a contradiction.

Therefore, at least one output is > 1 in every move. **QED**

**Step 4: Termination condition.**

The process stops when no move is possible. A move requires at least two entries > 1 (from different places). So the process stops when N <= 1.

By the lemma, each move produces at least one output > 1. Therefore N >= 1 throughout the process. (We never reach N = 0.)

Initially N = 2026 >= 1. After the process terminates, N >= 1 and no move is possible, so N < 2. Hence N = 1 at termination.

This proves Part (a): after finitely many moves, exactly one integer M > 1 remains (along with 2025 copies of 1).

---

### Part (b): Uniqueness of M

**Step 5: Valuation decomposition.**

For any prime p and positive integer x, let v_p(x) denote the p-adic valuation (the exponent of p in the prime factorization of x; v_p(1) = 0).

For any m, n > 0:
- v_p(gcd(m,n)) = min(v_p(m), v_p(n))
- v_p(lcm(m,n)) = max(v_p(m), v_p(n))
- v_p(lcm(m,n)/gcd(m,n)) = max(v_p(m), v_p(n)) - min(v_p(m), v_p(n)) = |v_p(m) - v_p(n)|

So the operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on p-adic valuations as:
  (v_p(m), v_p(n)) -> (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|)

Denote alpha = v_p(m), beta = v_p(n). The operation becomes (alpha, beta) -> (min(alpha, beta), |alpha - beta|).

**Step 6: Euclidean identity (Lemma).**

**Lemma:** For non-negative integers alpha, beta: gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta).

*Proof.* Without loss of generality assume alpha <= beta (symmetry). Then min(alpha, beta) = alpha and |alpha - beta| = beta - alpha.

By the fundamental property of gcd: gcd(alpha, beta) = gcd(alpha, beta - alpha).

This is exactly gcd(min(alpha, beta), |alpha - beta|). **QED**

**Step 7: Invariance of d_p.**

For each prime p, define:
  d_p = gcd(v_p(x_1), v_p(x_2), ..., v_p(x_k))
where {x_1, ..., x_k} is the current board.

**Lemma:** d_p is invariant under each move.

*Proof.* Consider a move replacing (m, n) with (g, h) where g = gcd(m,n) and h = lcm(m,n)/gcd(m,n).

Let alpha = v_p(m) and beta = v_p(n). By Step 5:
- v_p(g) = min(alpha, beta)
- v_p(h) = |alpha - beta|

Let S be the multiset of p-valuations of all other entries on the board (excluding m and n). Then:
- Before the move: d_p = gcd(alpha, beta, S) = gcd(gcd(alpha, beta), S)
- After the move: d_p' = gcd(min(alpha, beta), |alpha - beta|, S) = gcd(gcd(min(alpha, beta), |alpha - beta|), S)

By Step 6: gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta).

Therefore d_p' = gcd(gcd(alpha, beta), S) = d_p. **QED**

**Step 8: Terminal state determines M.**

At termination, the board is {M, 1, 1, ..., 1} where M > 1.

For each prime p:
  d_p = gcd(v_p(M), v_p(1), ..., v_p(1)) = gcd(v_p(M), 0, ..., 0) = v_p(M)

(using the convention that gcd(a, 0) = a for any a >= 0).

Since d_p is invariant, v_p(M) equals the initial value of d_p, which depends only on the initial board.

Therefore:
  M = product over all primes p of p^{v_p(M)} = product over all primes p of p^{d_p^{(initial)}}

This expression depends only on the initial configuration, not on any choices made during the process.

This proves Part (b). **QED**

---

### Verification

**Sanity check with small example:** Board = {6, 4, 3}.

Initial d_2 = gcd(v_2(6), v_2(4), v_2(3)) = gcd(1, 2, 0) = 1.
Initial d_3 = gcd(v_3(6), v_3(4), v_3(3)) = gcd(1, 0, 1) = 1.
For p >= 5: d_p = 0.

Predicted M = 2^1 * 3^1 = 6.

Let us verify by running the operations:
- Move on (6, 4): gcd = 2, lcm/gcd = 24/2 = 12. Board becomes {2, 12, 3}.
- Move on (12, 3): gcd = 3, lcm/gcd = 12/1 = 4. Wait, let me recalculate: gcd(12, 3) = 3, lcm(12, 3) = 12, lcm/gcd = 12/3 = 4. Board becomes {2, 3, 4}.
- Move on (4, 2): gcd = 2, lcm/gcd = 4/2 = 2. Board becomes {3, 2, 2}.
- Move on (2, 2): gcd = 2, lcm/gcd = 2/2 = 1. Board becomes {3, 2, 1}.
- Move on (3, 2): gcd = 1, lcm/gcd = 6/1 = 6. Board becomes {1, 6, 1}.

Final M = 6. Matches prediction.

---

## Promotable lemmas

1. **Euclidean identity for gcd:** gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta) for non-negative integers alpha, beta. Proved in Step 6.

2. **No-two-ones lemma:** The operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) with m, n > 1 never produces two outputs equal to 1. Proved in Step 3 Lemma.
