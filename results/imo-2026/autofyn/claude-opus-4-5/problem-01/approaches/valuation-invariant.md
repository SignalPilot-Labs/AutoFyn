## Status
solved

## Approaches tried
- valuation-invariant: p-adic valuation invariant + lexicographic (Omega, count) monovariant — worked; complete proof below

## Current best
Complete proof of both (a) and (b).

## Full proof

**Problem Statement.** There are 2026 integers greater than 1 on a blackboard. In a move, we choose two integers m > 1 and n > 1 from different places and replace them with gcd(m,n) and lcm(m,n)/gcd(m,n). We continue while possible.  
(a) Prove that after finitely many moves, exactly one integer M > 1 remains.  
(b) Prove that M does not depend on the sequence of moves.

---

### Preliminaries

**Notation.** For a prime p and integer x, let v_p(x) denote the p-adic valuation of x, i.e., the largest power of p dividing x. We set v_p(1) = 0 for all primes p.

**Prime factorization.** For any integer x > 1, we have x = prod_p p^{v_p(x)}, where only finitely many exponents are nonzero.

**gcd and lcm via valuations.** For integers m, n >= 1:
- gcd(m,n) = prod_p p^{min(v_p(m), v_p(n))}
- lcm(m,n) = prod_p p^{max(v_p(m), v_p(n))}

**Convention.** We adopt the standard convention gcd(a, 0) = a for all a >= 0.

---

### The Operation in Terms of Valuations

**Lemma 1 (Valuation decomposition).** Let m, n be positive integers. The operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on p-adic valuations as:

(v_p(m), v_p(n)) -> (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|)

*Proof.* Let alpha = v_p(m) and beta = v_p(n). Then:
- v_p(gcd(m,n)) = min(alpha, beta)
- v_p(lcm(m,n)) = max(alpha, beta)
- v_p(lcm(m,n)/gcd(m,n)) = max(alpha, beta) - min(alpha, beta) = |alpha - beta|

Thus the operation sends (alpha, beta) to (min(alpha, beta), |alpha - beta|). qed

---

### Part (b): Uniqueness of M

**Lemma 2 (Euclidean identity).** For non-negative integers alpha, beta:

gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta)

*Proof.* Without loss of generality, assume alpha <= beta. Then min(alpha, beta) = alpha and |alpha - beta| = beta - alpha. We must show gcd(alpha, beta - alpha) = gcd(alpha, beta).

By the Euclidean algorithm (knowledge base: Diophantine / parametric families, divisor analysis), for any integers a, b with a >= 0:

gcd(a, b) = gcd(a, b - a)

Setting a = alpha and b = beta (with beta >= alpha >= 0), we obtain gcd(alpha, beta - alpha) = gcd(alpha, beta). qed

**Definition.** For each prime p, define:

d_p = gcd(v_p(x_1), v_p(x_2), ..., v_p(x_{2026}))

where x_1, ..., x_{2026} are the integers currently on the board.

**Lemma 3 (Invariance of d_p).** For each prime p, the value d_p is preserved by every move.

*Proof.* Consider a move that replaces entries m and n with gcd(m,n) and lcm(m,n)/gcd(m,n). Let S = {v_p(x_1), ..., v_p(x_{2026})} be the multiset of p-adic valuations before the move.

Before the move, S contains alpha = v_p(m) and beta = v_p(n) (among other values).

After the move, S' differs from S only in that alpha and beta are replaced by min(alpha, beta) and |alpha - beta|.

By Lemma 2, gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta).

Now, the gcd of a finite multiset {a_1, ..., a_k} equals gcd(gcd(a_1, a_2), a_3, ..., a_k). Replacing two elements a_1, a_2 with two elements a'_1, a'_2 satisfying gcd(a'_1, a'_2) = gcd(a_1, a_2) does not change the overall gcd:

gcd(a'_1, a'_2, a_3, ..., a_k) = gcd(gcd(a'_1, a'_2), a_3, ..., a_k) = gcd(gcd(a_1, a_2), a_3, ..., a_k) = gcd(a_1, a_2, ..., a_k)

Therefore d_p (the gcd of all valuations in S) equals the gcd of all valuations in S'. qed

**Terminal State Characterization.** Suppose the process terminates with the board containing {M, 1, 1, ..., 1} where M > 1 (we will prove this happens in Part (a)). For each prime p:

v_p(M) = gcd(v_p(M), v_p(1), ..., v_p(1)) = gcd(v_p(M), 0, ..., 0) = v_p(M)

using the convention gcd(a, 0) = a.

But by Lemma 3, this gcd equals the initial d_p. Therefore:

v_p(M) = d_p (the initial value computed from x_1, ..., x_{2026})

**Theorem (Part b).** The terminal value M satisfies:

M = prod_p p^{d_p}

where d_p = gcd(v_p(x_1), ..., v_p(x_{2026})) is computed from the initial configuration. Since the d_p are determined solely by the initial board, M is independent of the sequence of moves. qed

---

### Part (a): Termination and Exactly One M > 1

**Definition.** Define:
- T = sum_{i=1}^{2026} Omega(x_i), where Omega(x) is the number of prime factors of x counted with multiplicity (Omega(1) = 0)
- N = |{i : x_i > 1}|, the count of entries greater than 1

**Lemma 4 (Monovariant).** The pair (T, N) strictly decreases in lexicographic order with each move.

*Proof.* Consider a move replacing (m, n) with (g, a) where g = gcd(m,n) and a = lcm(m,n)/gcd(m,n) = mn/g^2. Note that m, n >= 2.

We analyze three cases.

**Case 1: gcd(m,n) = 1 (coprime).**

Here g = 1 and a = mn.

Contribution to T:
- Before: Omega(m) + Omega(n)
- After: Omega(1) + Omega(mn) = 0 + Omega(m) + Omega(n) (since Omega is totally additive)

So T is unchanged.

Contribution to N:
- Before: m > 1 and n > 1 contribute 2 to N
- After: g = 1 does not contribute, a = mn >= 2*2 = 4 > 1 contributes 1

So N decreases by 1.

Since T is unchanged and N decreases, (T, N) strictly decreases lexicographically.

**Case 2: gcd(m,n) >= 2 and lcm(m,n)/gcd(m,n) >= 2.**

Here both g >= 2 and a >= 2.

Contribution to T:
- Before: Omega(m) + Omega(n)
- After: Omega(g) + Omega(a) = Omega(g) + Omega(mn/g^2) = Omega(g) + Omega(m) + Omega(n) - 2*Omega(g) = Omega(m) + Omega(n) - Omega(g)

Since g >= 2, we have Omega(g) >= 1, so T decreases by at least 1.

When T decreases, (T, N) strictly decreases lexicographically regardless of N.

**Case 3: gcd(m,n) >= 2 and lcm(m,n)/gcd(m,n) = 1.**

We have a = mn/g^2 = 1, so mn = g^2. Since g = gcd(m,n) divides both m and n, write m = gm', n = gn' with gcd(m', n') = 1. Then mn = g^2 m'n' = g^2 implies m'n' = 1, so m' = n' = 1, meaning m = n = g.

So this case occurs exactly when m = n. Here g = m and a = 1.

Contribution to T:
- Before: Omega(m) + Omega(n) = 2*Omega(m)
- After: Omega(g) + Omega(1) = Omega(m) + 0 = Omega(m)

T decreases by Omega(m) >= 1.

Again, (T, N) strictly decreases lexicographically.

**Conclusion.** In all cases, (T, N) strictly decreases in lexicographic order. Since T >= 0 and N >= 0 are non-negative integers, and lexicographic order on pairs of non-negative integers is a well-ordering, the process must terminate. qed

**Lemma 5 (Terminal condition).** The process terminates when N <= 1 (at most one entry > 1).

*Proof.* A move requires choosing two distinct entries m > 1 and n > 1. This is possible if and only if N >= 2. Therefore the process stops exactly when N <= 1. qed

**Lemma 6 (M > 1 at termination).** At termination, the unique entry M > 1 satisfies M >= 2. In particular, N = 1 (not N = 0).

*Proof.* We show that for some prime p, d_p >= 1, which implies M = prod_p p^{d_p} >= p >= 2.

Each initial x_i > 1 has at least one prime factor. Pick any i_0 in {1, ..., 2026} and let p be a prime dividing x_{i_0}. Then v_p(x_{i_0}) >= 1.

Now, d_p = gcd(v_p(x_1), ..., v_p(x_{2026})).

The gcd of a set of non-negative integers, at least one of which is positive, equals the gcd of all the positive ones (since gcd(a, 0) = a). In particular, v_p(x_{i_0}) >= 1 is included, so d_p >= 1 is possible unless the gcd somehow becomes 0.

More precisely: d_p = gcd(v_p(x_1), ..., v_p(x_{2026})) >= 0. If all v_p(x_i) = 0, then d_p = 0. But v_p(x_{i_0}) >= 1, and for any other j, v_p(x_j) >= 0. The gcd includes v_p(x_{i_0}) >= 1, and we have:

d_p = gcd(v_p(x_1), ..., v_p(x_{2026}))

Consider: gcd(1, k) = 1 for any k >= 0, so if v_p(x_{i_0}) = 1 and some other entry has v_p(x_j) = 0, then d_p = gcd(..., 1, ..., 0, ...) = 1.

Wait, we need to be more careful. gcd(0, a) = a, but gcd(1, 0) = 1, and gcd(1, 2) = 1. So if the multiset contains both 0 and positive values, the gcd is the gcd of all positive values (since gcd(a, 0) = a contributes nothing new).

Specifically: gcd(a_1, ..., a_k, 0, ..., 0) = gcd(a_1, ..., a_k) for positive a_i.

So d_p = gcd of all v_p(x_i) over i. At least one of these (namely v_p(x_{i_0})) is >= 1. The others are >= 0.

If we have d_p = gcd(S) where S is a multiset of non-negative integers containing at least one positive integer, then d_p >= 1 if all elements are positive, but d_p could equal 0 only if all elements are 0 (since gcd(0, 0, ..., 0) = 0).

But S contains v_p(x_{i_0}) >= 1 > 0, so not all elements are 0. If any element is 0 while another is positive, say gcd(0, 1) = gcd(1, 0) = 1 > 0.

Indeed, gcd(0, n) = n for n > 0, so gcd involving both 0s and positive integers is the gcd of the positive integers, which is at least 1.

Therefore d_p >= 1 for the prime p dividing x_{i_0}.

Hence M = prod_p p^{d_p} >= p^{d_p} >= p >= 2 > 1.

This shows N >= 1 at termination. Combined with N <= 1 from Lemma 5, we get N = 1. qed

**Theorem (Part a).** After finitely many moves, exactly one integer M > 1 remains on the blackboard.

*Proof.* By Lemma 4, the process terminates in finitely many moves. By Lemma 5, termination occurs when N <= 1. By Lemma 6, N = 1 at termination, meaning exactly one entry is > 1. qed

---

### Conclusion

We have proved:

**(a)** The process terminates after finitely many moves (Lemma 4), and at termination exactly one integer M > 1 remains (Lemmas 5 and 6).

**(b)** The terminal value is M = prod_p p^{d_p} where d_p = gcd(v_p(x_1), ..., v_p(x_{2026})) is the initial gcd of p-adic valuations (Lemma 3 and the terminal state characterization). This depends only on the initial configuration, not on the sequence of moves.

---

**Remark.** The number 2026 plays no special role; the proof works for any initial board of n >= 2 integers greater than 1. The terminal M equals the "greatest common gcd-divisor" of the initial numbers, computed prime-by-prime.

---

## Promotable lemmas

1. **Euclidean identity for valuation pairs:** gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta) for non-negative integers alpha, beta. Proved in Lemma 2.

2. **Valuation-gcd invariance:** For the operation (m,n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)), the quantity d_p = gcd of all p-adic valuations is preserved. Proved in Lemma 3.
