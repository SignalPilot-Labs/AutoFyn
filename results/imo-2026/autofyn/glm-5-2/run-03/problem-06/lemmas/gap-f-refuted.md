# Dead-end record: same-type free-rider replacement (Gap F) is FALSE

**Claim tested (FALSE).** *If $q_1<q_2$ (in insertion order) are two non-redundant free-riders (primes $\notin P_1=S(a_1)$ that enter some minimal transversal) at step $n$ with the same type $\tau_n(q_1)=\tau_n(q_2)$ — where $\tau_n(q)=(A(q),B_n(q))\in 2^{P_1}\times 2^{P_1}$ — then $q_1$ becomes redundant after $q_2$'s insertion.*

**Refutation (verified by reviewer, round 1).** Take $a_1=385=5\cdot7\cdot11$, so $P_1=\{5,7,11\}$. The sequence begins
$$385,\ 390,\ 392,\ 396,\ 399,\ 406,\ 418,\ 420,\ 434,\ 448,\ 450,\ 462,\dots$$
Direct computation (prime-set-intersection criterion; verified against minimality) shows:

- The minimal-transversal family **stabilizes at $n=38$** to $7$ transversals
  $\{2,7\},\{2,3,5\},\{2,3,11\},\{2,11,19\},\{3,7,11\},\{3,7,19\},\{5,7,11\}$
  with $L=\operatorname{lcm}(\operatorname{rad})=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$ and $|A|=T=5088$.
- The sequence IS periodic from $n=1$ (pure-from-start holds): $a_{n+5088}=a_n+43890$, and the cyclic successor on $A$ predicts $a_{n+1}\bmod L$ with zero mismatches over 600 terms.
- The stabilized non-redundant prime set is $\{2,3,5,7,11,19\}$; the free-riders (primes $\notin P_1$) are $\{2,3,19\}$, stable through $n\ge600$.
- The free-riders $2$ and $3$ are **both non-redundant at every step $n\ge38$** and at every such step have the **identical type**
$$\tau(2)=\tau(3)=\bigl(A=\{5\},\ B=\{5,7,11\}\bigr)$$
  (witnessing term $a_2=390=2\cdot3\cdot5\cdot13$, so $A(2)=A(3)=\{5\}$; for both, every $p\in P_1$ is avoided by some minimal transversal containing the prime, so $B=\{5,7,11\}$).
- Yet **neither** makes the other redundant: both persist as non-redundant through $n\ge600$.

This directly falsifies Gap F. The two same-type free-riders are **complementary**, not mutually replacing: each is the unique hitter of a different collection of historical terms, so each is essential to a different minimal transversal. The type $(A,B)$ is too coarse to detect this — it records only the $P_1$-interaction pattern, identical for $2$ and $3$, even though the two primes hit genuinely different sets of historical terms.

**Further refutation on $a_1=715=5\cdot11\cdot13$.** Before this sequence locks (it eventually reaches $3125=5^5$, a prime power, and locks at $L=5$), the non-redundant free-rider set grows monotonically to $91$ members at $n=400$, *all of the single type* $(A=\{5\},B=\{5\})$, with distinct insertion times. No same-type replacement occurs at any point during the growth.

**Conclusion.** The "at most one free-rider per type" bound does not hold; no per-type finiteness argument is available from the type-competition framing. Do NOT retry this framing.

**Important note (corrects a round-1 compute-explorer error).** The compute-explorer report claimed $a_1=385$ is "aperiodic through 12000 terms" and that "free-rider primes keep entering minimal transversals." This is FALSE: the full minimal-transversal family (including the prime $19$, which the explorer missed by restricting to primes $\le Q=11$) stabilizes at $n=38$, and the sequence IS periodic from $n=1$. The explorer's autocorrelation test only checked $T\le3000$; the true period is $T=5088>3000$.

**Status.** Reviewer-certified negative result (round 1). Record only; not importable as a positive lemma.
