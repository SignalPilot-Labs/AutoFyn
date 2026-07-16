# Approach: omega-monovariant

## Status
solved

## Approaches tried
- omega-monovariant (Round 1) — solved; Omega(n) = sum of prime exponents is a monovariant; combined with p-adic invariant G_p gives complete proof.

## Current best
Complete proof of both parts (a) and (b).

## Full proof

**Problem statement:** There are 2026 integers greater than 1 on a blackboard. In a move, Confucius chooses two integers m > 1 and n > 1 from different places on the blackboard and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). He continues while it is possible.

(a) Prove that, regardless of choices, after finitely many moves, exactly one integer M > 1 remains on the blackboard.

(b) Prove that M does not depend on the choices.

---

### Definitions and Setup

Let the board state be a multiset of 2026 positive integers. A move is possible when at least two entries are greater than 1.

**Definition.** For a positive integer n with prime factorization n = p_1^{e_1} p_2^{e_2} ... p_r^{e_r}, define:
- v_p(n) = exponent of prime p in n (equals 0 if p does not divide n).
- Omega(n) = sum over all primes p of v_p(n) = total number of prime factors counted with multiplicity.

**Key properties of Omega:**

**Lemma 1 (Omega is fully additive).** For any positive integers a and b, Omega(ab) = Omega(a) + Omega(b).

*Proof.* For any prime p, v_p(ab) = v_p(a) + v_p(b). Therefore:
Omega(ab) = sum_p v_p(ab) = sum_p (v_p(a) + v_p(b)) = sum_p v_p(a) + sum_p v_p(b) = Omega(a) + Omega(b).

**Lemma 2.** For any positive integers a and b with a | b, Omega(b/a) = Omega(b) - Omega(a).

*Proof.* Since a | b, we have b = a * (b/a), so by Lemma 1: Omega(b) = Omega(a) + Omega(b/a), which gives Omega(b/a) = Omega(b) - Omega(a).

**Note:** Omega(1) = 0 (the empty sum), Omega(p) = 1 for any prime p, and Omega(p^k) = k.

---

### Part (a): Termination with exactly one M > 1

**Define the state variables:**
- S = sum over all board entries x of Omega(x).
- k = number of entries on the board that are greater than 1.

Initially, S >= 2026 (since each initial entry a_i > 1 satisfies Omega(a_i) >= 1), and k = 2026.

**Analysis of a single move.**

Suppose we pick entries m > 1 and n > 1. Let g = gcd(m,n). The move replaces (m, n) with (g, mn/g^2).

Note that mn/g^2 = lcm(m,n)/gcd(m,n), which we verify: lcm(m,n) = mn/gcd(m,n), so lcm(m,n)/gcd(m,n) = mn/gcd(m,n)^2 = mn/g^2.

**Claim 1.** After the move, S_new = S_old - Omega(g).

*Proof.* 
Before the move, the contribution to S from m and n is Omega(m) + Omega(n).
After the move, the contribution from g and mn/g^2 is Omega(g) + Omega(mn/g^2).

Using Lemma 1 and Lemma 2:
- Omega(mn) = Omega(m) + Omega(n).
- Omega(g^2) = 2 * Omega(g).
- Since g^2 | mn (as g | m and g | n, and the g from m and the g from n contribute g^2 to the product), we have:
  Omega(mn/g^2) = Omega(mn) - Omega(g^2) = Omega(m) + Omega(n) - 2*Omega(g).

Therefore:
Omega(g) + Omega(mn/g^2) = Omega(g) + Omega(m) + Omega(n) - 2*Omega(g) = Omega(m) + Omega(n) - Omega(g).

So S_new = S_old - Omega(g).

**Case analysis:**

**Case 1: gcd(m,n) = g > 1.**

Then Omega(g) >= 1, so S_new = S_old - Omega(g) < S_old. The value of S strictly decreases.

**Case 2: gcd(m,n) = 1.**

Then g = 1, so Omega(g) = 0, and S_new = S_old (S is unchanged).

However, in this case:
- The outputs are (gcd(m,n), mn/gcd(m,n)^2) = (1, mn).
- Since m > 1 and n > 1, we have mn > 1.
- Before the move, we had two entries > 1 (namely m and n).
- After the move, we have one entry = 1 and one entry = mn > 1.

**Claim 2.** When gcd(m,n) = 1, the number k of entries > 1 decreases by exactly 1.

*Proof.* The two entries m, n (both > 1) are removed. The entries 1 and mn are added. Since 1 is not > 1 and mn > 1, the count changes from having m and n as "> 1" entries to having only mn as a "> 1" entry. Net change: 2 removed, 1 added, so k decreases by 1.

**Summary of monovariant behavior:**

Consider the pair (S, k) with the lexicographic order (decreasing on S, then decreasing on k).

- If g > 1: S strictly decreases. (S, k) strictly decreases lexicographically regardless of k.
- If g = 1: S stays the same, but k decreases by 1. (S, k) strictly decreases lexicographically.

In all cases, (S, k) strictly decreases.

**Claim 3.** The process terminates in finitely many moves.

*Proof.* Both S and k are non-negative integers. S is bounded below by 0, and k is bounded below by 0. The pair (S, k) lies in the well-ordered set N x N with lexicographic order. Since each move strictly decreases (S, k), the process must terminate after at most S_initial * 2026 + k_initial moves (a crude upper bound). More precisely, at most S_initial + k_initial moves, since each move decreases at least one of S or k by at least 1.

**Claim 4.** At termination, k <= 1.

*Proof.* The process can continue if and only if there exist at least two entries > 1. When k >= 2, a move is possible. Therefore, the process terminates only when k <= 1.

**Claim 5.** At termination, k >= 1 (that is, M > 1 exists).

*Proof.* This follows from the invariant established in Part (b). For each prime p, define G_p = gcd of v_p over all board entries. We will prove G_p is invariant. Since at least one initial entry a_i > 1, there exists a prime p dividing some a_i, hence v_p(a_i) >= 1. Initially G_p >= 1 for such a prime p.

At termination, the board is {M, 1, 1, ..., 1} with one entry M and 2025 entries equal to 1. The G_p value at termination is gcd(v_p(M), 0, 0, ..., 0). Since gcd(a, 0) = a for any a >= 0 (every integer divides 0), we have G_p = v_p(M).

By invariance (proved below), G_p at termination equals G_p at the start. Since G_p >= 1 for some prime p dividing an initial entry, we have v_p(M) >= 1 for that p, hence M >= p >= 2, so M > 1.

Therefore k = 1 at termination.

**Conclusion for Part (a):** The process terminates with exactly one entry M > 1 (and 2025 entries equal to 1). This completes the proof of part (a).

---

### Part (b): M does not depend on choices

**Definition.** For each prime p, define:
G_p = gcd(v_p(a_1), v_p(a_2), ..., v_p(a_{2026}))
where a_1, ..., a_{2026} are the current board entries.

**Claim 6 (Euclidean identity).** For non-negative integers a and b:
gcd(min(a,b), |a-b|) = gcd(a, b).

*Proof.* Without loss of generality, assume a >= b. Then min(a,b) = b and |a-b| = a - b.
We need to show gcd(b, a-b) = gcd(a, b).

By the fundamental property of gcd: gcd(a, b) = gcd(a - b, b) for any integers with a >= b >= 0 and not both zero. This is the subtraction step of Euclid's algorithm.

Proof of the subtraction identity: Let d = gcd(a, b). Then d | a and d | b, so d | (a - b). Hence d | gcd(a-b, b).
Conversely, let d' = gcd(a-b, b). Then d' | (a-b) and d' | b, so d' | ((a-b) + b) = a. Hence d' | gcd(a, b) = d.
Since d | d' and d' | d, we have d = d' (both are positive when not both zero; if b = 0, then gcd(a,0) = a = gcd(a,a) is consistent).

This establishes gcd(b, a-b) = gcd(a, b), which is gcd(min(a,b), |a-b|) = gcd(a, b).

**Claim 7.** The operation on valuations is: replacing (v_p(m), v_p(n)) with (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|).

*Proof.* Let a = v_p(m) and b = v_p(n).

For the gcd output: v_p(gcd(m,n)) = min(v_p(m), v_p(n)) = min(a, b). (Standard property of valuations: v_p(gcd(x,y)) = min(v_p(x), v_p(y)).)

For the lcm/gcd output: 
v_p(lcm(m,n)) = max(v_p(m), v_p(n)) = max(a, b). (Standard property: v_p(lcm(x,y)) = max(v_p(x), v_p(y)).)
Therefore:
v_p(lcm(m,n)/gcd(m,n)) = v_p(lcm(m,n)) - v_p(gcd(m,n)) = max(a, b) - min(a, b) = |a - b|.

So the move transforms (a, b) to (min(a, b), |a - b|).

**Claim 8 (G_p is invariant).** The value G_p = gcd over all board entries of v_p is unchanged by any move.

*Proof.* Let the multiset of v_p-values before the move be V = {v_1, v_2, ..., v_{2026}}. Choose two entries with v_p-values a and b (corresponding to the integers m and n chosen for the move).

After the move, the multiset becomes V' = V \ {a, b} union {min(a,b), |a-b|}.

We need to show gcd(V) = gcd(V').

Let G = gcd(V) = gcd over all elements of V.
Let G' = gcd(V') = gcd over all elements of V'.

Note that V' = V \ {a,b} union {min(a,b), |a-b|}.

First, gcd(min(a,b), |a-b|) = gcd(a, b) by Claim 6.

Now, V = (V \ {a,b}) union {a, b}, so:
G = gcd(V) = gcd(gcd(V \ {a,b}), gcd(a,b)) = gcd(gcd(V \ {a,b}), gcd(a,b)).

Similarly, V' = (V \ {a,b}) union {min(a,b), |a-b|}, so:
G' = gcd(V') = gcd(gcd(V \ {a,b}), gcd(min(a,b), |a-b|)) = gcd(gcd(V \ {a,b}), gcd(a,b)).

Since gcd(min(a,b), |a-b|) = gcd(a, b), we have G' = G.

Therefore G_p is invariant under any move.

**Claim 9.** At termination, v_p(M) = G_p for all primes p.

*Proof.* At termination, the board is {M, 1, 1, ..., 1}. For any prime p:
G_p = gcd(v_p(M), v_p(1), v_p(1), ..., v_p(1)) = gcd(v_p(M), 0, 0, ..., 0).

Since gcd(x, 0) = x for any x >= 0 (because every integer divides 0), we have gcd(v_p(M), 0) = v_p(M).
Iterating, gcd(v_p(M), 0, 0, ..., 0) = v_p(M).

Therefore G_p = v_p(M).

**Claim 10.** M is uniquely determined by the initial configuration.

*Proof.* At termination, v_p(M) = G_p for all primes p. Since G_p is invariant (Claim 8), G_p equals its initial value for all p.

The initial value of G_p is:
G_p^{(init)} = gcd(v_p(a_1^{(0)}), v_p(a_2^{(0)}), ..., v_p(a_{2026}^{(0)}))
where a_1^{(0)}, ..., a_{2026}^{(0)} are the initial board entries.

Since M is a positive integer, M is determined by its prime factorization:
M = product over all primes p of p^{v_p(M)} = product over all primes p of p^{G_p^{(init)}}.

Note: G_p^{(init)} = 0 for all but finitely many primes p (specifically, for primes not dividing any initial entry), so this is a finite product.

Since G_p^{(init)} depends only on the initial configuration, M depends only on the initial configuration.

**Conclusion for Part (b):** M = product_p p^{G_p} where G_p is the gcd of p-adic valuations of the initial entries. This is independent of the sequence of moves. This completes the proof of part (b).

---

### Summary

(a) The pair (Omega-sum S, count k of entries > 1) strictly decreases lexicographically with each move. Since (S, k) is bounded below by (0, 0), the process terminates. At termination, k <= 1 (else a move is possible) and k >= 1 (by the invariant G_p >= 1 for some prime p). Hence exactly one M > 1 remains.

(b) For each prime p, the quantity G_p = gcd of v_p-valuations over all board entries is invariant (by the Euclidean identity on valuations). At termination, v_p(M) = G_p. Therefore M = product_p p^{G_p} depends only on the initial configuration.

---

## Promotable lemmas

1. **Euclidean identity on pairs:** For non-negative integers a, b: gcd(min(a,b), |a-b|) = gcd(a,b). Proved in Claim 6 via the subtraction step of Euclid's algorithm.

2. **G_p invariant under the move:** If V is a multiset of non-negative integers and (a,b) in V is replaced by (min(a,b), |a-b|), then gcd(V) is unchanged. Proved in Claim 8.
