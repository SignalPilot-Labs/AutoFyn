# Lemma: cofactor-P1-divisibility (POSITIVE, $|P_1|=2$-specific; STRENGTHENED round 7)

*Certified: round 4 (reviewer); STRENGTHENED round 7 (reviewer). Source: `approaches/p1-equals-2-direct.md`, Step 10. The round-7 strengthening relaxes the hypothesis from "hypothetical governing $r>M_1$" to "ANY governing $r\notin P_1$" and DROPS the round-4 "minimality of $r$ as smallest governing prime $>M_1$" crutch — incomparability with $\{p,q\}\in\operatorname{MT}$ ALONE suffices. Reviewer independently verified (corrected naive $O(N^2)$ gcd-greedy, bit-exact vs `/tmp/round-6/mt_greedy.py`): for $a_1=375=3\cdot5^3$ (the refutation witness, governing $G=\{2,3,5,7,19\}$), $r\in\{2,7,19\}\setminus\{3,5\}=P_1$ gives $2517/550/210$ $r$-multiples respectively over $N=3000$ terms, with $0$ cofactor-fails in each (cofactor $k=a_n/r$ divisible by $p=3$ or $q=5$ in every case). The lemma correctly FAILS for $r\in P_1$ ($r=3$: $1257$ fails; $r=5$: $141$ fails) — confirming the hypothesis $r\notin P_1$ is essential.*

## Statement (strengthened)

In the **$|P_1|=2$ NON-LOCK** regime ($a_1=p^kq$ or $a_1=pq$, $p<q$ odd primes, no prime-power term reached), let $r$ be **ANY** governing prime with $r\notin P_1$ (equivalently $r$ is prime and $\gcd(r,pq)=1$, i.e. $r\ne p,q$ — NOT only the minimal-criminal hypothetical $r>M_1$). Then for every $r$-multiple term $a_n$ (i.e. every term, since every $a_n\in\mathcal B_\infty$ by `every-term-in-binfinity`), the cofactor $k=a_n/r$ is **divisible by $p$ or by $q$**.

This **strengthens** the round-4 version in two ways: (a) the hypothesis relaxes from "hypothetical governing $r>M_1$" to "any governing $r\notin P_1$" — in particular it now applies to ACTUAL governing primes (e.g. $r=2,7,19$ for $a_1=375$), not only the minimal-criminal hypothetical; (b) the proof uses ONLY incomparability with $\{p,q\}\in\operatorname{MT}$, with NO minimal-criminal hypothesis (the round-4 "smallest governing $r>M_1$" was an unused crutch).

## Proof (corrected round 7)

Let $m=a_n\in\mathcal B_\infty$ with $r\mid m$ (so $m=rk$, $k=m/r$). By `binfinity-divisibility-progression-structure`, there exists $T\in\operatorname{MT}(\mathcal F_\infty)$ with $\operatorname{rad}(T)\mid m$, i.e. $T\subseteq S(m)$. Since $r\mid m$ and $r$ is prime, $r\in S(m)$.

**At least one of $\{p,q\}$ lies in $T$.** By `P1-minimal-transversal-lemma`, $\{p,q\}\in\operatorname{MT}(\mathcal F_\infty)$. $T\in\operatorname{MT}(\mathcal F_\infty)$ must hit $S(a_1)=\{p,q\}$ (transversality of $\mathcal F_\infty$, which contains $S(a_1)$), so $T\cap\{p,q\}\ne\varnothing$. Pick any $p^*\in T\cap\{p,q\}$ (so $p^*\in\{p,q\}$, hence $p^*\mid k$ will imply "$p\mid k$ or $q\mid k$"). *(Note: $T$ may equal $\{p,q\}$ itself — then both $p,q\in T$ and we pick either; or $T\ne\{p,q\}$, in which case incomparability of distinct minimal transversals forces $\{p,q\}\not\subseteq T$, so exactly one of $\{p,q\}$ lies in $T$. Either way, at least one is present, which is all we need.)* Since $r\notin\{p,q\}$ (hypothesis $r\notin P_1$), we have $p^*\ne r$.

Now split on whether $r\in T$:

- **$r\notin T$.** Then $\operatorname{rad}(T)\mid m=rk$ and $\gcd(r,\operatorname{rad}(T))=1$ (as $r$ is prime and $r\notin T$, so $r\nmid\operatorname{rad}(T)$). Hence $r\cdot\operatorname{rad}(T)\mid m=rk$, so $\operatorname{rad}(T)\mid k$. Since $p^*\in T$, $p^*\mid\operatorname{rad}(T)\mid k$. ✓

- **$r\in T$.** Write $T=\{r\}\cup T_0$ with $T_0=T\setminus\{r\}$ (a set of primes, $r\notin T_0$). $\operatorname{rad}(T)=r\cdot\operatorname{rad}(T_0)\mid m=rk$ gives $\operatorname{rad}(T_0)\mid k$. Since $p^*\in T$ and $p^*\ne r$, we have $p^*\in T_0$; hence $p^*\mid\operatorname{rad}(T_0)\mid k$. ✓

In both cases $p^*\mid k$ with $p^*\in\{p,q\}$, i.e. $p\mid k$ or $q\mid k$. $\square$

*(Round-7 correction: the round-4 proof asserted "$T$ contains exactly one of $\{p,q\}$", which fails for $T=\{p,q\}$ (then both are in $T$); the round-7 strengthening replaces this with the weaker "at least one of $\{p,q\}$ in $T$" — valid for $T=\{p,q\}$ and $T\ne\{p,q\}$ alike — which suffices for the divisibility transfer. The conclusion is unchanged.)*

## Scope and limitation (unchanged, explicit)

- **Genuine $|P_1|=2$-specific structural fact** (uses `P1-minimal-transversal-lemma`'s incomparability, unavailable for $|P_1|\ge3$).
- **Weak — a floor, not a ceiling.** Forces only $k\ge\min(p,q)\ge3$ (a single small-prime factor of the cofactor). Gives NO upper bound on $k$, NO bound on the prime factorization of $k$, NO bound on $|G|$. Does NOT close Gap A. The cofactor $k$ ranges over the infinite set $\{pj:j\ge1\}\cup\{qj:j\ge1\}$. Consumers must not over-claim.
- The hypothesis $r\notin P_1$ (equivalently $\gcd(r,pq)=1$) is essential: for $r\in P_1$ the lemma fails (e.g. $a_1=375$, $r=3$: $1257$ cofactor-fails in $3000$ terms; $r=5$: $141$ fails). The proof breaks at "$\gcd(r,p^*)=1$" when $r=p^*$.

## Computational verification (reviewer-reproduced, $N=3000$)

| $a_1$ | $P_1$ | $M_1$ | governing $G$ | $r\notin P_1$ tested | $r$-multiples | cofactor-fails |
|---|---|---|---|---|---|---|
| 15 | $\{3,5\}$ | 15 | $\{2,3,5\}$ | $r=2$ | $175$ (over $200$) | $0$ |
| **375** | $\{3,5\}$ | 15 | $\{2,3,5,7,19\}$ | $r=2,7,19$ | $2517/550/210$ | $0/0/0$ |
| 375 | $\{3,5\}$ | 15 | — | $r=3$ (in $P_1$, expect fails) | $2824$ | $1257$ |
| 375 | $\{3,5\}$ | 15 | — | $r=5$ (in $P_1$, expect fails) | $1113$ | $141$ |

## Tools

`binfinity-divisibility-progression-structure` ($m\in\mathcal B_\infty\Leftrightarrow\operatorname{rad}(T)\mid m$ for some $T\in\operatorname{MT}$). `P1-minimal-transversal-lemma` ($\{p,q\}\in\operatorname{MT}(\mathcal F_\infty)$ for $|P_1|=2$ NON-LOCK; both $p,q$ governing). Incomparability of distinct minimal transversals. `every-term-in-binfinity` (every $a_n\in\mathcal B_\infty$). Reviewer-certified (round 4; strengthened round 7).
