## `p-position-small-prime-classification`

**Verdict: APPROVE**  
**True Status: solved** (the builder's recorded `solved` status is correct)

### Scores
- **Correctness:** 10/10
- **Completeness / rigor:** 10/10
- **Progress:** 10/10

### Adversarial verification

The proof answers the actual problem: for an arbitrary permitted initial value \(A=a_1>1\), it constructs positive integers
\[
L=\prod_{p\le A}p,
\qquad
T=|G\cap[A,A+L)|,
\]
and proves \(a_{n+T}=a_n+L\) for every \(n\ge1\).

1. **Game-theoretic implications.** The game is well founded because every move strictly lowers the integer and no position lies below \(A\). The displayed recursion
   \[
   m\text{ is P}\iff\text{there is no earlier P-position coprime to }m
   \]
   is exactly the finite impartial-game P/N recursion. Its negation also legitimately gives that every N-position has a legal move to a P-position. The induction identifying the greedy sequence with the increasing P-positions is sound: before the least candidate \(c\), there is no unlisted P-position, and \(c\) is noncoprime to every P-position below it, so it is P. Existence is also established, both for candidates and for infinitely many P-positions.

2. **Load-bearing stripping inequality, independently re-derived.** Let \(s\) be the squarefree product of the small primes dividing \(b\), choose \(p\mid s\), and let \(q>A\) divide \(b\). Since \(sq\mid b\): if the least \(e\) with \(p^es\ge A\) is zero, then \(x=s<sq\le b\). If \(e>0\), minimality gives \(p^{e-1}s<A\), hence
   \[
   x=p^es<pA\le sA<sq\le b,
   \]
   where \(p\le s\) and \(A<q\). Every inequality has the correct orientation, including strictness at \(x<pA\) and \(sA<sq\). Thus the stripping lemma really preserves precisely the small-prime signature while strictly reducing below \(b\) in the large-prime case.

3. **Descent strictness.** For a minimal violating pair \(b<b'\), stripping \(b\) gives \(x\le b<b'\) coprime to \(b'\). Since \(b'\) is P, \(x\) is N, so there is a P-position \(b^*<x\) coprime to \(x\). Signature preservation ensures that \(b^*\) shares no small prime with \(b\), while
   \[
   b^*<x\le b<b'.
   \]
   The larger member of the new violating pair is therefore exactly \(b\), strictly below the formerly minimal larger member \(b'\). There is no equality loophole.

4. **Signature-invariance orientation.** In the orientation \(u\) N and \(v\) P, an earlier P-position \(w\) is coprime to \(u\). The small-common-prime lemma gives a small prime dividing both \(v\) and \(w\); equal signatures make it divide \(u\), contradiction. Swapping the names \(u,v\) genuinely treats the opposite mixed orientation; the argument does not depend on their numerical order. Thus equal signatures imply equal status.

5. **Indexed blocks.** Because every small prime divides \(L\), \(m\) and \(m+L\) have identical small-prime signatures, giving the two-way membership equivalence. For each block, translation by \(L\) is an order-preserving bijection; surjectivity follows by subtracting \(L\), whose result remains at least \(A\). Since \(A\in G\), \(T\ge1\). Writing \(n=jT+k\) uniquely with \(j\ge0\), \(1\le k\le T\), places \(a_n\) in block \(j\), and translation increases its global index by exactly \(T\). The half-open endpoints introduce no omitted or duplicated terms.

Independent computation for \(2\le A\le12\) reproduced the claimed P-position signature classification and translation rule through three primorial blocks in every case.

### Promotable lemmas
- **Certified:** small-prime signature classification for the decreasing coprimality P-position game. Written to `results/imo-2026-06/lemmas/small-prime-signature-classification.md` with a self-contained proof.
- **Certified:** periodic-enumeration lemma. Written to `results/imo-2026-06/lemmas/periodic-enumeration.md` with the surjectivity and indexing details explicit.

### Record and workspace
- Recorded outcome `verified-milestone` for this slug in round 1. The ranker entry was already present; no consistency repair was needed.
- Updated `results/imo-2026-06/current.md` to `solved` and included the verified Full proof.

### Goal Progress
The problem is fully solved. The proof supplies explicit positive \(T,L\), establishes the exact recurrence for all positive indices, and leaves no unresolved case or lemma.
