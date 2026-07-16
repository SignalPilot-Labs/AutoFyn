# Small-witness theorem

## Statement
Fix $k\ge2$. Recursively classify the integers $m\ge k$ as good when no earlier good integer is coprime to $m$, and bad otherwise. Then every two good integers have a common prime divisor at most $k$.

## Proof
Any two good integers have gcd greater than $1$: if $u<v$ were good and coprime, then $u$ would make $v$ bad. Suppose nevertheless that some two good integers have no common prime at most $k$. Choose such a pair $b<b'$ with $b'$ least possible.

Because $b$ and $k$ are good, they have a common prime $p$, necessarily $p\le k$. Apply the small-prime compression lemma to $b$: there is $x\in[k,b]$ having the same prime divisors at most $k$ as $b$, with all prime divisors of $x$ at most $k$. Then $\gcd(x,b')=1$, for a common prime would be at most $k$ and, by equality of masks, would also divide $b$.

Since $x<b'$ and $b'$ is good, $x$ cannot be good; otherwise these would be two coprime good integers. Thus $x$ is bad and has a good witness $b^*\in[k,x-1]$ with $\gcd(b^*,x)=1$. The good integers $b^*$ and $b$ have no common prime at most $k$, since every such prime divisor of $b$ divides $x$. But $b^*<x\le b<b'$, so $(b^*,b)$ is a violating pair whose larger member is smaller than $b'$, contradicting minimality. $\square$
