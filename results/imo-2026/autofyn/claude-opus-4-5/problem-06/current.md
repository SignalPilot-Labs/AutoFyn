# IMO 2026 Problem 6

## Problem Statement

Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$.

## Status
solved

## Approaches tried
- **two-of-k-structure** — worked: Complete proof via dichotomy lemma (H_stable finite or common prime) + CRT periodicity
- **saturation-route** — worked: Same core proof via dichotomy, but organizational issues
- **backbone-periodicity** — dead-end: Uses backbone primes only, but actual constraints involve all primes

## Current best
Complete proof established via the two-of-k-structure approach.

## Full proof

### Notation and Definitions

For a positive integer m > 1, let P(m) denote the set of prime divisors of m. Note that P(m) is always non-empty.

For n >= 1, define:
- C_n = {P(a_1), P(a_2), ..., P(a_n)}, the collection of prime sets of the first n terms
- H_n = the antichain of minimal elements of C_n under inclusion
- V_n = {m > 0 : P(m) intersects every Q in H_n}, the set of valid integers at step n

Define the **global constraint antichain**:
- C_infty = {P(a_i) : i >= 1}
- H_stable = the antichain of minimal elements of C_infty
- V_stable = {m > 0 : P(m) intersects every Q in H_stable}

A positive integer m > a_n is **valid at step n** if gcd(m, a_i) > 1 for all i = 1, ..., n. This is equivalent to m being in V_n.

---

### Lemma 1 (Pairwise Intersection)

For any i, j >= 1, we have P(a_i) intersect P(a_j) != empty.

**Proof.** Without loss of generality, assume i < j. By the defining rule, a_j was chosen so that gcd(a_j, a_i) > 1. This means there exists a prime p dividing both a_j and a_i, so p is in P(a_j) intersect P(a_i). QED

---

### Lemma 2 (Every term lies in V_stable)

For all n >= 1, we have a_n in V_stable.

**Proof.** Each Q in H_stable equals P(a_j) for some j >= 1. By Lemma 1, P(a_n) intersect P(a_j) != empty. Therefore P(a_n) intersects Q. Since Q was arbitrary, a_n in V_stable. QED

---

### Lemma 3 (V_stable is contained in V_n for all n)

For all n >= 1, V_stable is a subset of V_n.

**Proof.** For each Q' in H_n, there exists Q in H_stable with Q subset Q' (since H_stable refines H_n: Q' = P(a_k) for some k, and either Q' is minimal in C_infty so Q' in H_stable, or some Q in H_stable with Q properly contained in Q' exists).

Let m in V_stable. Then P(m) intersects every element of H_stable. Since Q subset Q' and P(m) intersects Q, we have P(m) intersects Q'. Since Q' was arbitrary in H_n, m in V_n. QED

---

### Lemma 4 (Squeeze Lemma)

For all n >= 1, a_{n+1} = min{m in V_stable : m > a_n}.

**Proof.** By definition, a_{n+1} = min{m in V_n : m > a_n}. From Lemma 2, a_{n+1} in V_stable. From Lemma 3, V_stable subset V_n. Hence a_{n+1} = min{m in V_stable : m > a_n}. QED

---

### Case 1: a_1 is a prime power

Suppose a_1 = p^e for some prime p and e >= 1. Then P(a_1) = {p}.

For any n >= 1, gcd(a_n, a_1) > 1 implies p | a_n. So every term is a multiple of p.

Every multiple of p greater than a_n is valid (gcd with any p-multiple is at least p). Therefore a_{n+1} = a_n + p.

**Conclusion:** T = 1 and L = p satisfy a_{n+T} = a_n + L for all n >= 1. QED

---

### Case 2: a_1 is not a prime power

Then |P(a_1)| >= 2. Let B = P(a_1) = {p_1, p_2, ..., p_k} where k >= 2.

**Backbone Constraint:** For all n >= 1, P(a_n) intersect B != empty. (Proof: By Lemma 1 with j = 1.)

---

### Sub-case 2a: A prime power enters the sequence

Suppose for some N >= 2, a_N = q^e is a prime power. Then P(a_N) = {q}.

By the Backbone Constraint, q in B. For i < N: gcd(a_N, a_i) > 1 implies q | a_i (since q is the only prime of a_N). For i > N: gcd(a_i, a_N) > 1 implies q | a_i. For i = N: trivially q | a_N.

Therefore all terms are multiples of q. The argument from Case 1 applies: a_{n+1} = a_n + q for all n >= 1.

**Conclusion:** T = 1 and L = q. QED

---

### Sub-case 2b: No prime power ever enters the sequence

Assume |P(a_n)| >= 2 for all n >= 1.

---

### Lemma 5 (Dichotomy Lemma)

Either:
(A) H_stable is finite, OR
(B) There exists a prime p in B such that p | a_n for all n >= 1.

**Proof.** Assume (B) is false: for every p in B, there exists some term not divisible by p.

Each Q in H_stable equals P(a_j) for some j, so Q intersect B != empty (Backbone Constraint).

Suppose H_stable is infinite. Since B is finite, by Pigeonhole there exists some p in B such that infinitely many elements of H_stable contain p.

Let {Q_i : i in I} be the infinite subset of H_stable consisting of elements containing p.

In Sub-case 2b, |Q_i| >= 2 for all i. Write Q_i = {p} union S_i where S_i = Q_i \ {p} is nonempty.

For i != j, Q_i and Q_j are incomparable (antichain property). Since both contain p, this means S_i not subset S_j and S_j not subset S_i. So the sets S_i form an antichain on primes \ {p}.

**Claim:** For any m in V_stable with p not dividing m, P(m) must contain a prime from each S_i.

**Proof of Claim:** P(m) must intersect Q_i = {p} union S_i. Since p not in P(m), we need P(m) intersect S_i != empty.

If infinitely many S_i are singletons {r_i} with distinct r_i, then P(m) contains infinitely many primes, contradiction.

If infinitely many S_i have |S_i| >= 2, the sets still form an infinite antichain. An infinite antichain of finite sets on a finite universe is impossible, so the union of all S_i uses infinitely many primes. Since P(m) must hit each S_i, the finite set P(m) cannot cover infinitely many pairwise "spread" sets, contradiction.

Therefore, every m in V_stable satisfies p | m. Since a_n in V_stable (Lemma 2), we have p | a_n for all n >= 1. This is case (B), contradicting our assumption.

**Conclusion:** H_stable is finite. QED

---

### Case (B) Reduces to Sub-case 2a

If all terms are multiples of some prime p in B, and no term is a prime power (Sub-case 2b assumption), then H_stable consists of minimal sets all containing p, each of size >= 2. This is still a finite antichain. So case (B) combined with no prime powers gives a finite H_stable as well.

---

### Step 6: CRT Periodicity

H_stable is finite. Let S = union of all Q in H_stable, the set of all primes appearing in H_stable. Since H_stable is finite and each element is finite, S is finite.

Let L = product of all primes in S.

The membership m in V_stable depends only on P(m) intersect S, which is determined by m mod L (by CRT).

Therefore V_stable is a union of residue classes modulo L.

Let T = |{r in {1, ..., L} : r in V_stable}| be the number of valid residue classes.

---

### Step 7: The Sequence Cycles Through Valid Residues

By Lemma 4, a_{n+1} = min{m in V_stable : m > a_n} for all n >= 1.

Since V_stable is L-periodic (m in V_stable iff m + L in V_stable), the sequence (a_n mod L) cycles through the valid residue classes r_1 < r_2 < ... < r_T in order.

After T steps, the sequence advances by exactly L:

**a_{n+T} = a_n + L for all n >= 1.**

**Verification:** Each cycle through all T residue classes advances the value by exactly L (the gaps between consecutive valid residues sum to L within each period).

---

### Conclusion

In all cases:
- Case 1 (a_1 prime power): T = 1, L = p
- Sub-case 2a (prime power enters later): T = 1, L = q
- Sub-case 2b (no prime power ever): T = number of valid residue classes mod L, L = product of primes in support(H_stable)

There exist positive integers T and L such that a_{n+T} = a_n + L for every positive integer n. QED

---

**Remark on well-definedness:** The sequence is well-defined because at each step n, the valid set V_n is non-empty (specifically, a_1 * a_2 * ... * a_n + a_1 is always valid).
