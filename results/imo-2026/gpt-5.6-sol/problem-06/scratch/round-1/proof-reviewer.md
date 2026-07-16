# Proof review: imo-2026-06

## Goal Progress
The original problem asks only for existence of positive integers $T,L$ satisfying $a_{n+T}=a_n+L$ for every $n\ge1$. Both built approaches prove this with
\[
L=\prod_{p\le a_1}p,
\qquad
T=|G\cap[a_1,a_1+L-1]|,
\]
where $G$ is the recursively defined set of integers having no smaller good coprime witness. Both candidates are complete. The reviewer-owned `results/imo-2026-06/current.md` has been created with Status `solved` and a certified full proof.

Independent checks of the load-bearing mathematics:

1. **Recursive identification.** If $g_1<g_2<\cdots$ enumerate the good integers, every integer strictly between $g_n$ and $g_{n+1}$ is bad and has a smaller good coprime witness. Because no good integer lies in that interval, this witness belongs to $g_1,\dots,g_n$. Therefore exactly $g_{n+1}$ is the least integer after $g_n$ non-coprime to all previous terms. This reproduces the greedy recursion without circularity.
2. **Compression inequality.** For $A$ the squarefree product of the small prime divisors of $b$, $q>k$ a large prime divisor, $p\mid A$, and $e>0$ least with $x=p^eA\ge k$, minimality yields $x<pk$. Since $p\le A$, $k<q$, and $Aq\mid b$, independently one gets
   \[
   x<pk\le Ak<Aq\le b.
   \]
   The cases with no large prime and with $e=0$ are separately covered. No exponent or divisibility case is omitted.
3. **Extremal descent.** A violating good pair $b<b'$ with least larger member compresses to $x\le b$ coprime to $b'$. Hence $x$ is bad, producing good $b^*<x$. Every small prime of $b$ divides $x$, so $(b^*,b)$ is another violating good pair with larger member $b<b'$. The descent parameter strictly decreases.
4. **Mask periodicity.** Every prime $p\le k$ divides $L$, so $m+L\equiv m\pmod p$ and the small-prime masks agree in both directions. Similarity invariance therefore gives exact, not merely eventual, periodicity on all $m\ge k$.
5. **Indexing.** Translation by $L$ is an order-preserving bijection $G\to G\cap[k+L,\infty)$. Precisely the $T$ elements in the inclusive block $[k,k+L-1]$ precede the tail, so the $n$th element maps to the $(n+T)$th. The endpoints and off-by-one count are correct.
6. **Small-case computation.** Directly generating the recursion for $2\le k\le12$ verified mask invariance, period $L$, and $g_{n+T}=g_n+L$ across the computed ranges. This corroborates rather than replaces the proofs.

## small-prime-mask-compression

**Verdict: APPROVE**

**True Status: solved.** The builder's recorded Status `solved` is correct.

### Scores
- Correctness: **10/10**
- Completeness / rigor: **10/10**
- Progress: **10/10**

### Adversarial assessment
The candidate's load-bearing step is the minimal-counterexample proof of similarity invariance. It is valid. The bad member $a$ supplies a good $r<a$ coprime to $a$; compression gives $r'\le r$ with only small prime factors. If $r'<r$ were bad, $(r',r)$ would be an oppositely classified similar pair with maximum $r<a\le\max(a,b)$, contradicting minimality; if $r'=r$, goodness is immediate. Pairwise non-coprimality of the good $r'$ and $b$ then supplies a common prime, which is small because all factors of $r'$ are small. The two similarity relations force that prime to divide both $r$ and $a$, contradicting their coprimality. Numerical ordering of the original similar pair is not assumed, and the strict descent remains valid in either ordering.

The recursion-to-greedy argument is also complete: existence of each next eligible integer is explicitly supplied by a sufficiently large multiple of the finite product $a_1\cdots a_n$. The periodic-mask and order-enumeration steps are exact and have no missing boundary case.

### Promotable lemmas
- **Small-prime compression lemma:** certified as `results/imo-2026-06/lemmas/small-prime-compression.md`.
- **Small-prime-mask invariance:** certified as `results/imo-2026-06/lemmas/small-prime-mask-invariance.md` (using the independently certified small-witness theorem for a concise shared formulation).
- **Periodic-set enumeration lemma:** certified as `results/imo-2026-06/lemmas/periodic-set-enumeration.md`.

### Ranking outcome
Recorded `verified-milestone`: complete proof verified, including recursion, compression bound, minimal-counterexample invariance, periodicity, and index shift.

## small-witness-kernel

**Verdict: APPROVE**

**True Status: solved.** The builder's recorded Status `solved` is correct.

### Scores
- Correctness: **10/10**
- Completeness / rigor: **10/10**
- Progress: **10/10**

### Adversarial assessment
The candidate's load-bearing step is the small-witness theorem. Its extremal pair exists by well-ordering of the larger member. Ordering it as $b\le b'$ cannot leave equality: the common small prime of the good integers $b$ and $k$ does not divide $b'$ in a violating pair, so $b\ne b'$, hence $b<b'$. Compression gives $x\le b$ with the same small mask and no large factors; thus $x$ and $b'$ are coprime. If $x$ were good, this would contradict pairwise non-coprimality of good integers, so the recursion supplies good $b^*<x$ coprime to $x$. Every small divisor of $b$ is a divisor of $x$, proving that $(b^*,b)$ is a genuine violating pair; moreover its maximum is exactly $b$ because $b^*<x\le b$, and this is strictly below $b'$. The descent is therefore rigorous.

The proof that all multiples of $k$ are good is valid: a bad multiple would have a good witness coprime to the multiple and hence to $k$, contradicting pairwise non-coprimality of good integers. This establishes infinitude before enumeration. Similarity invariance correctly labels the bad and good members without presuming their numerical order. Finally, translation and the count of the initial block establish the claimed identity for every positive $n$.

### Promotable lemmas
- **Small-witness theorem:** certified as `results/imo-2026-06/lemmas/small-witness-theorem.md`.
- **Small-prime compression lemma:** certified as `results/imo-2026-06/lemmas/small-prime-compression.md`.
- **Similarity invariance:** certified as `results/imo-2026-06/lemmas/small-prime-mask-invariance.md`.

### Ranking outcome
Recorded `verified-milestone`: complete proof verified, including the compression/descent theorem, mask invariance, exact periodicity, and index shift.
