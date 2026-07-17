# Small-prime signature classification for a coprimality game

Fix an integer \(A>1\). Consider the finite decreasing impartial game on integers \(m\ge A\), in which a legal move from \(m\) is to an integer \(x\) satisfying \(A\le x<m\) and \(\gcd(m,x)=1\). Define
\[
\sigma(m)=\{p:\ p\text{ is prime},\ p\le A,\ p\mid m\}.
\]
If \(u,v\ge A\) and \(\sigma(u)=\sigma(v)\), then \(u\) and \(v\) have the same P/N status.

## Proof

Backward induction gives
\[
m\text{ is P}\quad\Longleftrightarrow\quad
\text{there is no P-position }x<m\text{ with }x\ge A\text{ and }\gcd(m,x)=1. \tag{1}
\]
Consequently, any two distinct P-positions have gcd greater than \(1\). In particular, every P-position has a prime divisor at most \(A\): this is immediate for \(A\), while every other P-position has a common prime divisor with the P-position \(A\).

We first establish a stripping fact. If \(b\ge A\) has a prime divisor at most \(A\), there is an \(x\) with \(A\le x\le b\), \(\sigma(x)=\sigma(b)\), and no prime divisor exceeding \(A\). Let \(s\) be the product of the distinct primes in \(\sigma(b)\), and choose \(p\mid s\). If \(b\) has no prime divisor greater than \(A\), use \(x=b\). Otherwise choose a prime \(q>A\) dividing \(b\), and let \(e\ge0\) be least such that \(x=p^e s\ge A\). If \(e=0\), then \(x=s<sq\le b\). If \(e>0\), then \(p^{e-1}s<A\), whence
\[
x=p^es<pA\le sA<sq\le b.
\]
The asserted signature and prime-divisor properties follow from the definition of \(x\).

We next prove that every two P-positions share a prime at most \(A\). If not, choose a violating pair \(b<b'\) with \(b'\) minimal. Apply the stripping fact to \(b\), obtaining \(A\le x\le b\). Since all prime divisors of \(x\) are small and \(b,b'\) share no small prime, \(\gcd(x,b')=1\). Thus \(b'\to x\) is legal. Because \(b'\) is P, (1) implies that \(x\) is N, so (1) supplies a P-position \(b^*<x\) coprime to \(x\). Every small prime divisor of \(b\) divides \(x\), hence no such prime divides \(b^*\). Therefore \(b^*,b\) are another violating pair, but its larger member is \(b<b'\), a contradiction.

Finally, suppose \(u\) is N and \(v\) is P. By (1), some P-position \(w<u\) is coprime to \(u\). The preceding result gives a prime \(p\le A\) dividing both P-positions \(v,w\). Since \(\sigma(u)=\sigma(v)\), the prime \(p\) also divides \(u\), contradicting \(\gcd(u,w)=1\). Thus this mixed orientation is impossible. Interchanging \(u,v\) excludes the other mixed orientation, proving the claim. ∎
