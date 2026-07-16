# IMO 2026 Problem 1

## Status
solved

## Approaches tried
- p-adic-gcd-invariant (Round 1) -- worked. Lexicographic monovariant (P, k) proves termination; p-adic invariant G_p = gcd(v_p(a_i)) proves uniqueness via M = product of p^{G_p}.
- omega-monovariant (Round 1) -- worked. Omega(n) = sum of prime exponents is a monovariant; combined with p-adic invariant G_p gives complete proof.

## Current best
Complete proof of both parts (a) and (b).

## Full proof

### Problem Statement

There are 2026 integers greater than 1 written on a blackboard, not necessarily different. In a move, Confucius chooses two integers m > 1 and n > 1 from different places on the blackboard and replaces these two integers with gcd(m,n) and lcm(m,n)/gcd(m,n). He continues to make moves while it is possible to do so.

(a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer M on the blackboard is greater than 1.

(b) Prove that the value of M does not depend on the choices of Confucius.

---

### Notation and Setup

Let the 2026 integers on the board be a_1, a_2, ..., a_{2026}, each > 1 initially.

**Definition.** For a prime p and integer n >= 1, define v_p(n) to be the p-adic valuation of n, i.e., the largest integer e >= 0 such that p^e divides n. By convention, v_p(1) = 0 for all primes p.

**Definition.** At any stage of the game, let:
- k = #{i : a_i > 1} be the count of board entries strictly greater than 1.
- P = product of all 2026 board entries (counting multiplicity).

**Observation on the operation.** When we pick m > 1 and n > 1 from different places and replace them with (gcd(m,n), lcm(m,n)/gcd(m,n)), we are replacing two numbers with two numbers. Write g = gcd(m,n). Then:
- The first output is g.
- The second output is lcm(m,n)/g = (mn/g)/g = mn/g^2.

Note that g * (mn/g^2) = mn/g, which differs from mn unless g = 1. Thus the product of the two outputs is mn/g.

---

### Part (a): Termination with Exactly One M > 1

**Step 1. Case Analysis of a Move**

We analyze what happens to (P, k) when we perform a move (m, n) -> (g, mn/g^2) where g = gcd(m,n).

The three cases partition all possibilities: either m = n, or m != n with gcd(m,n) = 1, or m != n with gcd(m,n) > 1. These are mutually exclusive and exhaustive.

---

**Case A: m = n (Equal pair)**

Since m > 1 and m = n, we have g = gcd(m, m) = m. The outputs are:
- First output: g = m.
- Second output: mn/g^2 = m^2/m^2 = 1.

Effect on k: We replace two entries > 1 with one entry = m > 1 and one entry = 1. The count k decreases by 1.

Effect on P: The product changes from having factors m and m (contributing m^2) to having factors m and 1 (contributing m). So P decreases by a factor of m > 1. That is, P_new = P_old / m < P_old.

**Conclusion for Case A:** P strictly decreases, and k decreases by 1.

---

**Case B: m != n and gcd(m,n) = 1 (Coprime, unequal pair)**

Here g = 1. The outputs are:
- First output: g = 1.
- Second output: mn/g^2 = mn/1 = mn > 1 (since m > 1 and n > 1 implies mn > 1).

Effect on k: We replace two entries > 1 with one entry = 1 and one entry = mn > 1. The count k decreases by 1.

Effect on P: The product changes from having factors m and n (contributing mn) to having factors 1 and mn (contributing mn). So P_new = P_old (unchanged).

**Conclusion for Case B:** P is unchanged, and k decreases by 1.

---

**Case C: m != n and gcd(m,n) > 1 (Non-coprime, unequal pair)**

Here g = gcd(m,n) > 1. Write m = g * a and n = g * b where gcd(a, b) = 1 and a, b >= 1.

**Claim.** Since m != n and m = ga, n = gb with gcd(a,b) = 1, we have a != b.

*Proof of Claim.* If a = b, then m = ga = gb = n, contradicting m != n. So a != b.

**Claim.** We have ab >= 2.

*Proof of Claim.* Since a, b >= 1 and gcd(a,b) = 1, if ab = 1 then a = b = 1, which contradicts a != b. Therefore ab >= 2.

The outputs are:
- First output: g > 1.
- Second output: mn/g^2 = (ga)(gb)/g^2 = g^2 ab / g^2 = ab >= 2 > 1.

Effect on k: Both outputs are > 1, so the count of entries > 1 is unchanged.

Effect on P: P_new = P_old / g (since the product of outputs is mn/g, not mn). Since g > 1, we have P_new < P_old.

**Conclusion for Case C:** P strictly decreases, and k is unchanged.

---

**Step 2. The Lexicographic Monovariant**

Define the pair (P, k) where P is the product of all board entries and k is the count of entries > 1.

We order pairs lexicographically: (P', k') < (P, k) if either P' < P, or P' = P and k' < k.

**Claim.** Every move strictly decreases (P, k) in the lexicographic order.

*Proof.* 
- In Case A and Case C, P strictly decreases, so (P, k) strictly decreases regardless of what happens to k.
- In Case B, P is unchanged but k decreases by 1, so (P, k) strictly decreases.

In all cases, (P, k) strictly decreases. The claim is proved.

**Step 3. Termination**

The lexicographic order on (P, k) is a well-order when restricted to P >= 1 (positive integers) and k >= 0 (non-negative integers). Since (P, k) strictly decreases with each move and is bounded below (P >= 1, k >= 0), the process must terminate after finitely many moves.

**Step 4. Terminal Condition: At Most One M > 1**

The game continues while it is possible to do so. A move requires choosing two integers > 1 from *different places*. At termination, it must be impossible to make a move. This means there are not two distinct positions on the board both containing integers > 1.

Therefore, at termination, k <= 1 (at most one entry is > 1).

**Step 5. Terminal Condition: At Least One M > 1**

We now show that k >= 1 at termination, i.e., not all entries become 1. This will follow from the invariant analysis in Part (b), but we can also see it directly:

**Claim.** At least one entry remains > 1 at termination.

*Proof.* Since all initial values are > 1, there exists a prime p and an initial entry a_i such that v_p(a_i) >= 1. We will show in Part (b) that for each prime p, the quantity G_p = gcd(v_p(a_1), ..., v_p(a_{2026})) is invariant under the operation. Since at least one initial v_p(a_i) >= 1, we have G_p >= 1 for that prime p.

At termination, the board is {M, 1, 1, ..., 1} for some M >= 1. We have:
G_p = gcd(v_p(M), v_p(1), ..., v_p(1)) = gcd(v_p(M), 0, ..., 0) = v_p(M).

(Here we use the convention that gcd(k, 0) = k for k >= 0, since every integer divides 0.)

Since G_p >= 1, we have v_p(M) >= 1, which implies p | M, hence M > 1.

**Conclusion of Part (a):** At termination, exactly one integer M > 1 remains on the blackboard.

---

### Part (b): M Does Not Depend on the Choices

**Step 6. The p-adic Invariant**

**Definition.** For each prime p, define G_p = gcd(v_p(a_1), ..., v_p(a_{2026})) to be the greatest common divisor of the p-adic valuations of all board entries.

**Lemma (Euclidean Identity).** For non-negative integers a and b:
gcd(min(a, b), |a - b|) = gcd(a, b).

*Proof.* Without loss of generality, assume a >= b >= 0. Then min(a, b) = b and |a - b| = a - b.

We need to show gcd(b, a - b) = gcd(a, b).

By the defining property of gcd: for any integer d > 0,
d | a and d | b if and only if d | b and d | (a - b).

This is because:
- If d | a and d | b, then d | (a - b).
- If d | b and d | (a - b), then d | (b + (a - b)) = a.

Therefore the set of common divisors of {a, b} equals the set of common divisors of {b, a - b}, which equals the set of common divisors of {min(a,b), |a-b|}. The greatest common divisor is therefore the same.

(This is precisely the subtraction step of the Euclidean algorithm for computing gcd.)

**Step 7. Proving G_p is Invariant**

**Claim.** The move (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) preserves G_p for every prime p.

*Proof.* Let g = gcd(m, n). The outputs are g and lcm(m,n)/g = mn/g^2.

For each prime p, we analyze the effect on the multiset {v_p(a_i) : i = 1, ..., 2026}.

Let a = v_p(m) and b = v_p(n). We need to compute v_p(g) and v_p(mn/g^2).

From the standard formulas:
- gcd(m, n) = product over all primes q of q^{min(v_q(m), v_q(n))}.
- lcm(m, n) = product over all primes q of q^{max(v_q(m), v_q(n))}.

Therefore:
- v_p(gcd(m, n)) = min(v_p(m), v_p(n)) = min(a, b).
- v_p(lcm(m, n)) = max(v_p(m), v_p(n)) = max(a, b).
- v_p(mn/g^2) = v_p(m) + v_p(n) - 2 * v_p(g) = a + b - 2 * min(a, b) = |a - b|.

(The last equality: a + b - 2*min(a,b) = max(a,b) + min(a,b) - 2*min(a,b) = max(a,b) - min(a,b) = |a - b|.)

So the operation on the p-adic valuations replaces (a, b) in the multiset with (min(a, b), |a - b|).

By the Euclidean Identity Lemma:
gcd(min(a, b), |a - b|) = gcd(a, b).

The other entries of the board are unchanged. Therefore:

G_p (after) = gcd({all v_p(a_i) after move})
           = gcd(min(a, b), |a - b|, {v_p(a_j) : j != the two positions})
           = gcd(gcd(a, b), {v_p(a_j) : j != the two positions})
           = gcd(a, b, {v_p(a_j) : j != the two positions})
           = gcd({all v_p(a_i) before move})
           = G_p (before).

(We use associativity and commutativity of gcd, and the fact that gcd(gcd(a, b), c) = gcd(a, b, c).)

Therefore G_p is invariant under any move.

**Step 8. Terminal Value of G_p**

At termination, the board is {M, 1, 1, ..., 1} with exactly one M > 1 and 2025 ones.

For each prime p:
v_p(1) = 0.

So:
G_p = gcd(v_p(M), 0, 0, ..., 0) = gcd(v_p(M), 0) = v_p(M).

(Here we use the standard convention: gcd(k, 0) = k for any k >= 0. This is correct because every integer divides 0, so the greatest common divisor of k and 0 is k itself. Note also gcd(0, 0) = 0 by convention, which is consistent since 0 = v_p(1) when M = 1, but we have established M > 1.)

**Step 9. M is Uniquely Determined**

Since G_p is an invariant determined by the initial configuration, and v_p(M) = G_p at termination, we have:

M = product over all primes p of p^{v_p(M)} = product over all primes p of p^{G_p}.

This is a finite product because G_p = 0 for all primes p that do not divide any initial a_i (if p does not divide a_i, then v_p(a_i) = 0, so G_p <= 0, but G_p >= 0 by definition, hence G_p = 0).

Explicitly:
**M = product over all primes p of p^{gcd(v_p(a_1), v_p(a_2), ..., v_p(a_{2026}))}.**

This depends only on the initial configuration (a_1, ..., a_{2026}), not on the choices made during the game.

**Conclusion of Part (b):** The final value M does not depend on the choices of Confucius.

---

### Summary

**(a)** The lexicographic pair (P, k) = (product of board, count of entries > 1) strictly decreases with each move. Since it is bounded below, the process terminates. At termination, k = 0 or k = 1. The invariant G_p ensures k >= 1. Hence exactly one M > 1 remains.

**(b)** The p-adic invariant G_p = gcd(v_p(a_1), ..., v_p(a_{2026})) is preserved by every move. At termination, v_p(M) = G_p for all p. Therefore:
M = product over all primes p of p^{gcd(v_p(a_1), ..., v_p(a_{2026}))}.
This depends only on the initial configuration.
