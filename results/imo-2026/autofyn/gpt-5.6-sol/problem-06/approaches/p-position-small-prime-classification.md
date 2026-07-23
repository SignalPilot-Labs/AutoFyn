## Status
solved

## Approaches tried
- Recast the greedy sequence as the increasing list of the P-positions of a decreasing coprimality game; use prime stripping and minimal-counterexample descent to prove that P-positions are classified by their prime-divisibility signatures up to the initial value — worked, and gives an exact period from the first term.

## Current best
The complete proof below shows that, with \(A=a_1\) and \(L=\prod_{p\le A}p\), membership in the set enumerated by the sequence is invariant under translation by \(L\). If \(T\) is the number of members in \([A,A+L)\), then \(a_{n+T}=a_n+L\) for every \(n\ge1\).

## Full proof
Put \(A=a_1\). We use the standard **P-position/N-position recursion for a finite impartial game**, proved below by strong induction (the strong-induction method is the entry “Induction” in the knowledge base).

Consider the following game on integers \(m\ge A\). From \(m\), a legal move consists of replacing \(m\) by an integer \(x\) such that
\[
 A\le x<m\qquad\text{and}\qquad \gcd(m,x)=1.
\]
Every move strictly decreases the displayed integer, so every play is finite. Call a position a P-position if the player whose turn it is has no winning strategy, and an N-position otherwise. Backward induction gives the following characterization:
\[
 m\text{ is a P-position}
 \quad\Longleftrightarrow\quad
 \text{there is no P-position }x\text{ with }A\le x<m\text{ and }\gcd(m,x)=1. \tag{1}
\]
Indeed, if such an \(x\) exists, the player to move goes to \(x\), after which the opponent is in a losing position, so \(m\) is an N-position. If no such \(x\) exists, then every legal move goes to an N-position, from which the next player has a winning strategy; hence every first move loses, and \(m\) is a P-position. This argument starts at \(A\), which has no legal move and is therefore a P-position, and determines all larger positions by strong induction.

Let \(G\) be the set of P-positions. Formula (1) immediately implies that any two distinct elements of \(G\) have greatest common divisor greater than \(1\): applying (1) to the larger one shows that it cannot be coprime to the smaller one. In particular, every element of \(G\) has a common prime divisor with \(A\).

We next verify that the given sequence is precisely the increasing enumeration of \(G\). Let
\[
 b_1<b_2<b_3<\cdots
\]
be that enumeration. It is infinite: if \(m\) is any multiple of \(A\), then every smaller P-position \(x\) has \(\gcd(x,A)>1\), and therefore \(\gcd(x,m)>1\); by (1), \(m\) is a P-position. We have \(b_1=A=a_1\). Suppose \(b_1,\ldots,b_n\) are the first \(n\) P-positions, and let \(c\) be the least integer \(m>b_n\) satisfying
\[
 \gcd(m,b_i)>1\quad(1\le i\le n).
\]
Such a \(c\) exists, for example because any multiple of \(b_1b_2\cdots b_n\) larger than \(b_n\) satisfies these inequalities. There cannot be a P-position \(y\) strictly between \(b_n\) and \(c\): any such \(y\), being noncoprime to each of the P-positions \(b_1,\ldots,b_n\), would itself satisfy the displayed inequalities and contradict the minimality of \(c\). Hence the only P-positions below \(c\) are \(b_1,\ldots,b_n\), and \(c\) is noncoprime to all of them. Characterization (1) therefore makes \(c\) a P-position, so \(c=b_{n+1}\). Thus the defining recursion for \((a_n)\), followed by induction on \(n\), gives \(a_n=b_n\) for every \(n\). It remains to describe \(G\).

Call a prime *small* if it is at most \(A\). For \(m\ge A\), define its small-prime signature to be
\[
 \sigma(m)=\{p:p\text{ is prime},\ p\le A,\ p\mid m\}.
\]
We first prove a prime-stripping lemma.

**Prime-stripping lemma.** If \(b\ge A\) has at least one small prime divisor, then there is an integer \(x\) such that
\[
 A\le x\le b,\qquad \sigma(x)=\sigma(b),
\]
and every prime divisor of \(x\) is small.

Let \(s\) be the product of the distinct small prime divisors of \(b\), and choose one such divisor \(p\). If \(b\) has no prime divisor greater than \(A\), take \(x=b\); all the required properties then hold.

Now suppose that \(b\) has a prime divisor \(q>A\). Choose the least integer \(e\ge0\) for which
\[
 x=p^e s\ge A.
\]
Such an \(e\) exists. The prime divisors of \(x\) are exactly those of \(s\), so they are all small and \(\sigma(x)=\sigma(b)\). It remains to prove \(x\le b\), treating both possible values of \(e\).

If \(e=0\), then \(x=s\). Since the distinct primes making up \(sq\) all divide \(b\), we have \(sq\mid b\), and hence
\[
 x=s<sq\le b.
\]
If \(e>0\), minimality of \(e\) gives \(p^{e-1}s<A\), and multiplication by \(p\) gives \(x=p^es<pA\). Also \(p\le s\), because \(p\) is a factor of \(s\), while \(A<q\). Consequently
\[
 x<pA\le sA<sq\le b.
\]
This proves the lemma in all cases.

We now prove the load-bearing strengthening.

**Small-common-prime lemma.** Every two P-positions have a common small prime divisor.

Suppose otherwise. Choose two distinct P-positions \(b,b'\) having no common small prime divisor, and order them so that \(b<b'\). Using the **extremal principle/minimal-counterexample descent** (the “Pigeonhole / extremal principle” and “Infinite descent” entries in the knowledge base), choose such a pair for which \(b'\), the larger member, is as small as possible.

Because \(b\) and \(A\) are distinct P-positions unless \(b=A\), they have a common prime divisor; if \(b=A\), it of course has a prime divisor at most \(A\). In either case \(b\) has a small prime divisor. Apply the prime-stripping lemma to \(b\), obtaining \(x\) with
\[
 A\le x\le b,
\]
a small-prime signature equal to that of \(b\), and no large prime divisors. Since \(b\) and \(b'\) have no common small prime divisor and every prime divisor of \(x\) is small, we have \(\gcd(x,b')=1\). Moreover, \(x\le b<b'\), so \(b'\to x\) is a legal move. As \(b'\) is a P-position, characterization (1) forces \(x\) to be an N-position.

By the other direction of (1), an N-position has a legal move to a P-position. Thus there is a P-position \(b^*\) such that
\[
 A\le b^*<x\qquad\text{and}\qquad \gcd(b^*,x)=1.
\]
No small prime divisor of \(b\) can divide \(b^*\), because every such prime divides \(x\) by \(\sigma(x)=\sigma(b)\), whereas \(b^*\) is coprime to \(x\). Hence the two P-positions \(b^*\) and \(b\) have no common small prime divisor. But
\[
 b^*<x\le b<b',
\]
so the larger member of this new violating pair is \(b\), strictly smaller than \(b'\). This contradicts the minimal choice of \(b'\), and proves the lemma.

We can now classify positions by their signatures.

**Signature-invariance lemma.** If \(u,v\ge A\) and \(\sigma(u)=\sigma(v)\), then either both \(u,v\) are P-positions or both are N-positions.

Assume first that \(u\) is an N-position and \(v\) is a P-position. By (1), there is a P-position \(w<u\) with \(\gcd(u,w)=1\). By the small-common-prime lemma, the P-positions \(v\) and \(w\) have a common small prime divisor \(p\). Since \(p\in\sigma(v)=\sigma(u)\), this prime also divides \(u\), contradicting \(\gcd(u,w)=1\). Thus the orientation “\(u\) N and \(v\) P” is impossible. If instead \(u\) is a P-position and \(v\) is an N-position, interchange \(u\) and \(v\) in the same argument. Both mixed orientations are impossible, proving signature invariance.

Let
\[
 L=\prod_{\substack{p\le A\\p\text{ prime}}}p.
\]
This is a positive integer. For every integer \(m\ge A\) and every prime \(p\le A\), modular arithmetic gives
\[
 p\mid m+L\quad\Longleftrightarrow\quad p\mid m,
\]
because \(p\mid L\). Therefore \(\sigma(m+L)=\sigma(m)\), and signature invariance yields the exact translation rule
\[
 m\in G\quad\Longleftrightarrow\quad m+L\in G \qquad(m\ge A). \tag{2}
\]
This is the modular-arithmetic step from the “Modular arithmetic, CRT” knowledge-base entry (only the elementary modular part is needed).

Finally, partition the integers from \(A\) onward into the half-open integer blocks
\[
 B_j=\{m\in\mathbb Z:A+jL\le m<A+(j+1)L\},
 \qquad j=0,1,2,\ldots.
\]
Translation by \(L\) is, by (2), an order-preserving bijection from \(G\cap B_j\) onto \(G\cap B_{j+1}\). Define
\[
 T=|G\cap B_0|.
\]
We have \(T\ge1\), since \(A\in G\cap B_0\), so \(T\) is a positive integer. Every block contains exactly \(T\) elements of \(G\).

For any \(n\ge1\), there are unique integers \(j\ge0\) and \(k\in\{1,\ldots,T\}\) such that \(n=jT+k\). The term \(a_n\), being the \(n\)-th element of \(G\), is the \(k\)-th element of \(G\cap B_j\): the preceding \(j\) blocks contain exactly \(jT\) elements. The order-preserving bijection \(m\mapsto m+L\) sends it to the \(k\)-th element of \(G\cap B_{j+1}\), whose global index is \((j+1)T+k=n+T\). Hence
\[
 a_{n+T}=a_n+L
\]
for every positive integer \(n\). Both \(T\) and \(L\) are positive, as required. ∎

## Promotable lemmas
- **Small-prime signature classification for the coprimality P-position game.** For fixed \(A>1\), in the decreasing game whose legal moves are \(m\to x\) with \(A\le x<m\) and \(\gcd(m,x)=1\), any two integers at least \(A\) divisible by exactly the same primes at most \(A\) have the same P/N status. Proved in the Full proof via the prime-stripping lemma, the small-common-prime minimal descent, and signature invariance.
- **Periodic-enumeration lemma.** If an infinite subset \(G\subseteq\{A,A+1,\ldots\}\) satisfies \(m\in G\iff m+L\in G\) for all \(m\ge A\), and \(T=|G\cap[A,A+L)|\), then its increasing enumeration \((g_n)\) satisfies \(g_{n+T}=g_n+L\) for all \(n\ge1\). Proved in the final block-counting paragraph of the Full proof.
