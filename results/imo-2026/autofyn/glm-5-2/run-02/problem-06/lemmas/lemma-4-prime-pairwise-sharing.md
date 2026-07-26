# Lemma 4' (crux): pairwise small-prime intersection at threshold $a_1$

**Statement.** Let $a_1,a_2,\ldots$ be the greedy sequence of IMO 2026 P6 (each $a_{n+1}$ is the smallest integer $>a_n$ non-coprime to every earlier term). Then for every $i<j$, the pair $(a_i,a_j)$ shares a prime $p\le a_1$. Equivalently, with $Q=\{p\text{ prime}:p\le a_1\}$ and $\tau(m)=P(m)\cap Q$, we have $\tau(a_i)\cap\tau(a_j)\ne\varnothing$ for all $i<j$.

**Proof.** Introduce the auxiliary *game of numbers* (aimo-0030 / IMO-SL 2013 N5, adapted and re-proved from scratch): fix $k\ge 2$ (take $k=a_1$); two players Ana, Banana alternate (Ana first) starting from $n\ge k$; a move replaces $m$ by $m'$ with $k\le m'<m$, $\gcd(m,m')=1$; first unable to move loses. Call $n$ good if Banana (second player) wins. The game terminates (numbers strictly decrease), so every $n\ge k$ is good or bad.

- **G3.** $k$ is good (no move from $k$; Ana loses first move).
- **G4.** Any two good numbers share a prime: if $m<n$ good and coprime, $m$ is a good coprime predecessor of $n$, so $n$ is bad — contradiction. (Uses the good/bad dichotomy G1/G2: $n$ is bad iff a good $x$ with $k\le x<n$, $\gcd(n,x)=1$ exists.)
- **G5 (stripping).** If $b\ge k$ has a small prime divisor, $x$ exists with $k\le x\le b$, similar to $b$ (same small primes), no big prime. (Let $p$ small, $q$ big prime of $b$; $a=$ product of small prime divisors of $b$; $\alpha$ least with $x=p^\alpha a\ge k$. Then $P(x)$ = small primes of $b$. Bound $x\le b$: $\alpha=0\Rightarrow x=a\mid b$; $\alpha\ge1\Rightarrow x<pk\le ak<aq\le b$ since $p\le a$, $k<q$, $aq\mid b$.)
- **G6 (descent).** Any two good numbers share a *small* prime $\le k$. Minimal counterexample $(b,b')$ good, $b'\ge b$, sharing only big primes, $b'$ minimal. $b,k$ good $\Rightarrow$ shared small prime $p$ (G4); $p\nmid b'\Rightarrow b'>b$. Strip $b\to x$ (G5): $x$ coprime to $b'$, so $x$ bad (else $x,b'$ good coprime, contradict G4). Bad $\Rightarrow$ move $x\to b^*$, $b^*$ good (G2'). Small primes of $b$ all divide $x$ (similarity), miss $b^*$; shared primes of $(b^*,b)$ are big; G4 forces a shared prime, big; so $(b^*,b)$ is a smaller counterexample (larger element $b<b'$). Contradiction.
- **Theorem GC (greedy = good).** For $k=a_1$, the increasing enumeration $g_0<g_1<\cdots$ of good numbers satisfies $g_0=a_1$ and $g_{n+1}=\min\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$ (induction: $g_0=a_1$ by G3; for the step, $M=\min\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$ is well-defined — large multiples of $k$ are admissible by G4 — and $M$ is good by the good/bad dichotomy + G4, with no good number in $(g_n,M)$ by G4; so $M=g_{n+1}$). Hence $a_n=g_{n-1}$.

By Theorem GC, P6's sequence is the good numbers of the game with $k=a_1$. By G6, any two good numbers share a small prime $\le k=a_1$. Hence any two terms $a_i,a_j$ share a prime $\le a_1$. $\square$

**Where proved.** `results/imo-2026-06/approaches/essential-monovariant.md` §1–§7 (round 2). Re-proves the game-of-numbers analysis of aimo-0030 (IMO-SL 2013 N5) from scratch; the crux is not cited but adapted and re-derived.

**Note.** This is the load-bearing crux of IMO 2026 P6. Combined with the round-1 periodicity machinery (`essential-monovariant` §8 / `crude-reduced-type` §6–9), it yields $a_{n+T}=a_n+L_0$ for all $n\ge 1$ with $L_0=\prod_{p\le a_1}p$, $T=|V|$.

## Promotable lemmas (sub-results, certified within this proof)
- **Lemma G6** (small-prime sharing for good numbers): any two good numbers of the game (parameter $k$) share a prime $\le k$. Reusable by any approach attacking P6 via the game equivalence.
- **Theorem GC** (greedy = good): P6's sequence with $a_1=A$ is the increasing enumeration of the good numbers of the game with $k=A$. Reusable: identifies P6's greedy with the good numbers, enabling transfer of any game-theoretic fact.
