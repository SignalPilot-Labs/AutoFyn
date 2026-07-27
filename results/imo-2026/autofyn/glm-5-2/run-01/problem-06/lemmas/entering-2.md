# Lemma: entering-2

**Statement (unconditional).** Let $a_1$ be odd with at least two distinct prime factors, and let $p^*=\min P(a_1)$. Then $a_2=a_1+p^*$, and $a_1+p^*$ is even, so $2\in P(a_2)\setminus P(a_1)$: the prime $2$ enters $P_{\mathrm{ess}}$ at step $2$.

**Proof.** $a_2$ is the smallest integer $m>a_1$ with $\gcd(m,a_1)>1$, i.e. with some prime of $P(a_1)$ dividing $m$. Since $a_1$ is divisible by every $p\in P(a_1)$, the next multiple of any fixed $p\in P(a_1)$ above $a_1$ is $a_1+p$; the smallest over all $p\in P(a_1)$ is $a_1+p^*$ (as $p^*\le p$ for all $p\in P(a_1)$), so $a_2\le a_1+p^*$.

No $m\in\{a_1+1,\ldots,a_1+p^*-1\}$ is admissible: set $d=m-a_1\in\{1,\ldots,p^*-1\}$; $\gcd(m,a_1)=\gcd(d,a_1)$. Any prime $q\mid\gcd(d,a_1)$ has $q\in P(a_1)$ (so $q\ge p^*$) and $q\mid d<p^*\le q$, impossible (a prime dividing $d\ge1$ satisfies $q\le d$). So $\gcd(d,a_1)=1$, no such $m$ is admissible, and $a_2=a_1+p^*$.

Since $a_1$ is odd (all prime factors $\ge3$) and $p^*\ge3$ is odd, $a_1+p^*$ is even: $2\mid a_2$. As $2\notin P(a_1)$, $2$ enters at step 2. ∎

*Verified 41/41 saturated seeds. Foundation of the 2-core framing and the SPT/W1 machinery (the prime $2\le p^*$ is present in $P_{\mathrm{ess},n}$ for all $n\ge2$, so any minimal containing $2$ satisfies "contains a prime $\le p^*$").*

**Source.** Approaches `smooth-window-crash` (Lemma E1) and `pstar-core-straggler` (Lemma A), round 129 (independent proofs). Reviewer-certified.
