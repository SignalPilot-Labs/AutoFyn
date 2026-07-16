# Small-prime compression lemma

## Statement
Fix an integer $k\ge2$. If $b\ge k$ has a prime divisor at most $k$, then there is an integer $x\in[k,b]$ which has exactly the same prime divisors at most $k$ as $b$ and has no prime divisor greater than $k$.

## Proof
If every prime divisor of $b$ is at most $k$, take $x=b$.

Otherwise, let $q>k$ be a prime divisor of $b$, and let $A$ be the product of all distinct prime divisors of $b$ that are at most $k$. This is a nonempty product. Choose a prime $p\mid A$, and let $e\ge0$ be least such that $x=p^eA\ge k$. The prime divisors of $x$ are exactly those of $A$, so the mask and support assertions hold.

If $e=0$, then $x=A\mid b$, hence $x\le b$. If $e>0$, minimality gives $p^{e-1}A<k$, so $x<pk$. Since $p\le A$ and $k<q$, while $Aq\mid b$, we obtain
\[
x<pk\le Ak<Aq\le b.
\]
Thus in every case $k\le x\le b$, proving the lemma. $\square$
