# Lemma: 2-entry for $|P_1|=2$ NON-LOCK

**Statement.** Consider the greedy sequence of `imo-2026-06` in the **$|P_1|=2$ NON-LOCK** regime: $a_1$ has exactly two distinct prime factors $P_1=\{p_{\rm sm},p_{\rm lg}\}=\{p,q\}$ with $p<q$ both odd (NON-LOCK $\Rightarrow$ $a_1$ odd, since $2\mid a_1\Rightarrow$ LOCK by `lock-lemma`), and no term is a prime power. Write $a_1=p^kq$ ($k\ge1$). Then
$$a_2=a_1+p_{\rm sm}=a_1+p=p(p^{k-1}q+1),$$
and $a_2$ is **even**; equivalently $2\in S(a_2)$, i.e. the prime $2$ enters the active support at index $n=2$.

This lever is **unavailable for $|P_1|\ge3$**: no single prime enters at $n=2$ with density $1/2$ when three or more distinct odd primes divide $a_1$.

**Proof.** At $n=1$ the only admissibility constraint is $\gcd(a_2,a_1)>1$, i.e. $S(a_2)\cap P_1\ne\varnothing$. So $a_2$ is the smallest $m>a_1$ divisible by $p$ or by $q$.
- Smallest multiple of $p$ strictly above $a_1$: $a_1+p$ (since $p\mid a_1$, the next $p$-multiple is $a_1+p$).
- Smallest multiple of $q$ strictly above $a_1$: $a_1+q>a_1+p$ (since $q>p$).
- Any $m\in(a_1,a_1+p)$ has $m=a_1+j$, $1\le j<p$. Then $m\bmod p=j\bmod p\ne0$ (as $0<j<p$), so $p\nmid m$; and $m\bmod q=j\bmod q\ne0$ (as $0<j<p<q$), so $q\nmid m$. Hence $S(m)\cap P_1=\varnothing$, inadmissible.

Therefore $a_2=a_1+p=p^kq+p=p(p^{k-1}q+1)$. Since $p,q$ are odd, $p^{k-1}q$ is odd, so $p^{k-1}q+1$ is even. Hence $2\mid a_2$, i.e. $2\in S(a_2)$. $\square$

**Depends on.** Definitions + `lock-lemma` (only to delimit the NON-LOCK regime: $2\mid a_1\Rightarrow$ LOCK).

**Status.** Reviewer-certified (round 3). Unconditional (within the $|P_1|=2$ NON-LOCK regime). Verified computationally for $a_1\in\{15,35,65,77,91,143,175,847\}$: in every case $a_2=a_1+p_{\rm sm}$ and $2\mid a_2$. Importable by any approach attacking the $|P_1|=2$ base case.
