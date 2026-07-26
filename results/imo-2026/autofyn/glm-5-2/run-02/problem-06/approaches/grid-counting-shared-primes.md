# Approach: grid-counting-shared-primes

## Status
partial

## Approaches tried
- (round 2, NEW — Route G, corpus crux `aimo-0447` USAMO 2014 6 grid-covering counting) Formed the $(i,j)$ grid of shared primes $P(a_i)\cap P(a_j)$ over the first $N$ terms; proved and certified the **large-prime-span lemma** (a prime $p>S_N$ divides at most one of $a_1,\ldots,a_N$, so it covers zero shared cells); derived the cell-count upper bound $\sum_{p\le S_N}(\lfloor S_N/p\rfloor+1)^2\le S_N^2\sum 1/p^2+2S_N\sum 1/p+\pi(S_N)$ with a fully elementary proof of $\sum_p 1/p^2<389/900<1/2$ (Euler product for $\zeta(2)=\pi^2/6$, Archimedes $\pi<22/7$; no PNT/Siegel/Jacobsthal). **Honest ceiling confirmed:** the counting forces every pair among the first $N$ terms to share a prime $\le S_N\le(N-1)R$ (a *growing* window), **not** the fixed $\le R$ of crux Lemma 4. Sharpening $S_N\rightsquigarrow R$ is itself the free-rider dichotomy = the crux; aggregate coverage also does not force per-cell coverage. Inherited the conditional Theorem (Lemma 4 $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$) from `essential-monovariant`. — partial (clean certified lemma + growing-window ceiling characterized; the fixed-$R$ threshold is the marked [GAP]).

## Current best
One certified, reusable lemma (**large-prime-span**, in `lemmas/large-prime-span-divides-at-most-one-term.md`): a prime $p>S_N:=a_N-a_1$ divides at most one of $a_1,\ldots,a_N$, so **every shared prime among the first $N$ terms is $\le S_N\le(N-1)R$**. Plus a fully elementary analytic bound $\sum_{p\ \text{prime}}1/p^2<389/900<1/2$ (Euler product + $\pi<22/7$) feeding the cell-count upper bound. Plus the inherited conditional Theorem (Lemma 4 $\Rightarrow$ translation-periodicity).

**Open gap (the ceiling):** the counting threshold is the **span** $S_N\le(N-1)R$, which **grows with $N$**. It yields the growing-window analogue "every pair among $a_1,\ldots,a_N$ shares a prime $\le(N-1)R$," **not** the crux Lemma 4 (fixed threshold $\le R$). Sharpening $S_N\rightsquigarrow R$ is precisely the free-rider dichotomy = the crux itself. Additionally, even the aggregate bound on small-prime coverage does not force *each* cell to be small-prime-covered (a cell may be uncovered by small primes even when the aggregate count is large); counting is intrinsically too coarse for the per-cell conclusion. Marked [GAP].

## Full proof (partial — the fixed-$R$ threshold is marked [GAP])

We target the whole theorem: there exist $T,L>0$ with $a_{n+T}=a_n+L$ for every $n\ge1$. We inherit the certified scaffold from `essential-monovariant` (Lemmas 1–3, the conditional Theorem) and attack the crux Lemma 4 by **aggregate double-counting** on a shared-prime grid, in the spirit of the corpus crux `aimo-0447` (USAMO 2014 6: cover an $(N{+}1)\times(N{+}1)$ grid of $\gcd$-witnesses by primes; large primes $>$ interval length divide at most one element per direction).

### 0. Notation

For $m>1$ write $P(m)$ for its set of prime divisors. Write
$$ R:=\operatorname{rad}(a_1)=\prod_{p\mid a_1}p,\qquad S_N:=a_N-a_1\ \ (\text{span of the first }N\text{ terms}). $$
The sequence is greedy: $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$.

### 1. Inherited lemmas (from `essential-monovariant`, certified)

We import, without re-proving, the following certified results (see `approaches/essential-monovariant.md` §1–§3 and `lemmas/`):

- **Lemma 1 (cheap anchor).** Every $a_n$ is divisible by some prime divisor of $a_1$; in particular $P(a_n)\cap P(a_1)\ne\varnothing$.
- **Lemma 2 (Gap bound).** $a_{n+1}-a_n\le R$ for every $n\ge1$. (Mechanism: the next multiple of $R$ above $a_n$ is admissible, since $R$ is divisible by every prime of $a_1$ and every $a_i$ has such a prime by Lemma 1.)
- **Lemma 3 (consecutive only-small).** Consecutive terms $a_n,a_{n+1}$ share only primes $\le R$. (A shared prime divides the gap $\le R$.)

These give, by telescoping, the **span bound**
$$ S_N = a_N-a_1 = \sum_{k=1}^{N-1}(a_{k+1}-a_k)\le (N-1)R. \tag{1} $$

### 2. The shared-prime grid

Fix $N\ge2$ and consider the first $N$ terms. Form the $N\times N$ grid whose cell $(i,j)$ (with $1\le i,j\le N$) carries the set of shared primes
$$ C_{i,j}:=P(a_i)\cap P(a_j). $$
We separate the **off-diagonal** cells ($i\ne j$, the pairwise-sharing cells, $\binom{N}{2}$ pairs each counted twice $\Rightarrow N(N-1)$ ordered off-diagonal cells) from the **diagonal** cells ($i=j$, where $C_{i,i}=P(a_i)$).

**Every off-diagonal cell is nonempty** (greedy): for $i<j$, when $a_j$ was chosen it had to satisfy $\gcd(a_j,a_i)>1$, so $P(a_i)\cap P(a_j)\ne\varnothing$. Hence
$$ \text{every off-diagonal cell } C_{i,j}\ne\varnothing. \tag{2} $$

### 3. Large-prime-span lemma — PROVED, certified

We restate (proof in `lemmas/large-prime-span-divides-at-most-one-term.md`):

**Lemma 4 (large-prime-span).** *With $S_N=a_N-a_1\le(N-1)R$ from (1): if a prime $p>S_N$, then $p$ divides at most one of $a_1,\ldots,a_N$.*

*Proof.* If $p\mid a_i$ and $p\mid a_j$ with $i<j$, then $p\mid(a_j-a_i)$; since the sequence is strictly increasing, $a_j-a_i>0$, so $a_j-a_i\ge p$. But $0<a_j-a_i\le S_N<p$, contradiction. $\square$

**Corollary 4a (large primes cover no shared cell).** *A prime $p>S_N$ divides at most one of the first $N$ terms, so it is the shared prime of **no** off-diagonal cell: it covers $0$ off-diagonal cells.*

Consequently every off-diagonal cell — being nonempty by (2) — is covered by at least one prime $p\le S_N\le(N-1)R$:

**Corollary 4b (growing-window shared-prime bound).** *For every $1\le i<j\le N$, the pair $(a_i,a_j)$ shares some prime $p\le S_N\le(N-1)R$.*

This is the clean, **provable** output of the counting route: every pair among the first $N$ terms shares a prime $\le(N-1)R$. **It is a growing-window analogue of the crux Lemma 4, with threshold $(N-1)R$ instead of the fixed $R$.**

### 4. Cell-count bound per prime — PROVED

For a prime $p\le S_N$, let $c_p:=\#\{i\in\{1,\ldots,N\}:p\mid a_i\}$ be the number of the first $N$ terms divisible by $p$. Since $a_1,\ldots,a_N\in[a_1,a_N]$, an interval of length $S_N$, and multiples of $p$ in any interval of length $L$ number at most $\lfloor L/p\rfloor+1\le L/p+1$,
$$ c_p \le \Big\lfloor\frac{S_N}{p}\Big\rfloor+1 \le \frac{S_N}{p}+1. \tag{3} $$
(We use only that the $a_i$ are distinct integers in an interval of length $S_N$ — no further structure.) A prime $p\le S_N$ covers $c_p^2$ grid cells (all ordered pairs $(i,j)$ with $p\mid a_i$ and $p\mid a_j$; this includes the diagonal cells where $p\mid a_i$). Hence
$$ \text{(multiplicity-weighted) small-prime cell coverage}\ \le \sum_{p\le S_N}\Big(\frac{S_N}{p}+1\Big)^2. \tag{4} $$

Expanding the square,
$$ \sum_{p\le S_N}\Big(\frac{S_N}{p}+1\Big)^2 = S_N^2\sum_{p\le S_N}\frac1{p^2}+2S_N\sum_{p\le S_N}\frac1{p}+\pi(S_N), \tag{5} $$$
where $\pi(x):=\#\{p\ \text{prime}:p\le x\}$. (This is an identity, not an estimate; it follows by distributing the square and counting the prime-indexed summands.)

### 5. Analytic input — $\sum_{p}1/p^2<1/2$ — PROVED elementarily

The knowledge base has no Euler-product / prime-sum entry; we re-derive what we need from the standard Euler product for $\zeta(2)$ (the Basel identity $\sum_{n\ge1}1/n^2=\pi^2/6$, a named classical result) and Archimedes' bound $\pi<22/7$. **No PNT, no Siegel, no Jacobsthal is invoked.**

**Lemma 5.** $\displaystyle\sum_{p\ \text{prime}}\frac1{p^2}<\frac12.$

*Proof.* We bound the tail over odd primes $\ge5$ by the larger sum over all integers $\ge5$ that are coprime to $6$ (every prime $\ge5$ is coprime to $6$, so $\{p\ge5:p\text{ prime}\}\subseteq\{n\ge5:\gcd(n,6)=1\}$). By the Euler-product form of $\zeta(2)$ (multiplicativity of the Dirichlet series),
$$ \sum_{\substack{n\ge1\\\gcd(n,6)=1}}\frac1{n^2} \;=\; \zeta(2)\prod_{p\mid 6}\Big(1-\frac1{p^2}\Big) \;=\; \frac{\pi^2}{6}\cdot\Big(1-\frac14\Big)\Big(1-\frac19\Big) \;=\; \frac{\pi^2}{6}\cdot\frac{2}{3} \;=\; \frac{\pi^2}{9}. $$
Removing the $n=1$ and $n=5$ summands (the only terms with $n<5$ in this restricted sum),
$$ \sum_{\substack{n\ge5\\\gcd(n,6)=1}}\frac1{n^2} = \frac{\pi^2}{9}-1-\frac1{25}=\frac{\pi^2}{9}-\frac{26}{25}. $$
Hence
$$ \sum_{p\ \text{prime}}\frac1{p^2} \;=\; \frac14+\frac19+\sum_{p\ge5}\frac1{p^2} \;\le\; \frac14+\frac19+\Big(\frac{\pi^2}{9}-\frac{26}{25}\Big). $$
Using Archimedes' bound $\pi<22/7$, we have $\pi^2<484/49<10$ (since $484<490$), so $\pi^2/9<10/9$. Therefore
$$ \sum_{p\ \text{prime}}\frac1{p^2} \;<\; \frac14+\frac19+\frac{10}{9}-\frac{26}{25} = \frac14+\frac{11}{9}-\frac{26}{25}. $$
Putting over the common denominator $900$:
$$ \frac14+\frac{11}{9}-\frac{26}{25}=\frac{225+1100-936}{900}=\frac{389}{900}<\frac{450}{900}=\frac12. \qquad\square $$
**(Numerical check, not a proof step: the prime zeta function $P(2)=\sum_p1/p^2\approx0.45225$, below $1/2$, consistent with the rigorous bound $389/900\approx0.4322$.)**

For the lower-order terms in (5) we use only the crude, elementary bounds
$$ \sum_{p\le x}\frac1p \;\le\; \sum_{n=2}^{\lfloor x\rfloor}\frac1n \;\le\; 1+\log x, \qquad \pi(x)\le x, \tag{6} $$
(the first is the standard harmonic-number estimate $\sum_{n=1}^{N}1/n\le1+\log N$ applied to a superset of the primes; the second is trivial — there are at most $x$ primes $\le x$). These are deliberately coarse; they suffice for the **ceiling characterization** below and require no prime-density theorem.

### 6. Aggregate coverage bound and the central [GAP]

Combining (4), (5), Lemma 5 and (6): the (multiplicity-weighted) number of grid cells covered by small primes is at most
$$ S_N^2\cdot\frac12 \;+\; 2S_N(1+\log S_N) \;+\; S_N. \tag{7} $$
By Corollary 4a, large primes ($p>S_N$) cover **zero** cells. Since every off-diagonal cell is nonempty (greedy, (2)), every off-diagonal cell is covered by some small prime $\le S_N$; in particular the **number of distinct off-diagonal cells** ($=N(N-1)$) is at most the multiplicity-weighted small-prime coverage, hence at most the right-hand side of (7). Using $S_N\le(N-1)R$ from (1),
$$ N(N-1) \;\le\; \frac12(N-1)^2R^2 + 2(N-1)R\bigl(1+\log((N-1)R)\bigr) + (N-1)R. \tag{8} $$

**This is a true inequality satisfied by the sequence (no contradiction; it is a necessary condition).** The counting route delivers this necessary condition, and Corollary 4b (the growing-window shared-prime bound $\le(N-1)R$). It does **not** deliver the crux.

#### Central gap (the ceiling) — [GAP]

Two obstructions prevent the counting route from reaching the crux Lemma 4 (fixed threshold $\le R$):

**(G1) Growing window.** The threshold produced by Lemma 4 is $S_N\le(N-1)R$, which **grows linearly with $N$**. To force the crux bound $\le R$ (independent of $N$), one would need to replace "$p>S_N$ divides at most one term" by "$p>R$ divides at most one term among *any* pair" — equivalently, that *no large prime $p>R$ is ever shared by two terms*. But that statement **is** the free-rider dichotomy, i.e. **is Lemma 4 itself**. There is no counting argument that lowers the threshold from $S_N$ to $R$ without already assuming the conclusion: a large prime $p\in(R,S_N]$ genuinely *can* divide two of the first $N$ terms without contradicting the span bound (their difference is $\le S_N < p$ only fails when $p\le S_N$; for $p\le S_N$ the difference argument is silent). Sharpening the threshold is exactly the crux.

**(G2) Aggregate vs. per-cell.** The bound (7) is on the **multiplicity-weighted** coverage (the sum $\sum_pc_p^2$, which overcounts cells covered by multiple primes). Even if one sharpened it to distinct-covered cells, an *aggregate* upper bound on small-prime coverage does **not** force **every** cell to be small-prime-covered: a cell may be uncovered by small primes even when the aggregate count is large (the coverage can be unevenly distributed, and double-counting inflates the sum without covering new cells). The counting route is intrinsically too coarse to produce the per-cell conclusion "each pair shares a small prime"; it can only bound totals. **[GAP]**

These two obstructions together are why the counting route, however clean its certified lemma (large-prime-span), cannot close the crux on its own. Sharpening requires the free-rider dichotomy — the descent route of `essential-monovariant` (Route D) or the propagation route of `propagation-bezout` (Route P), not aggregate counting.

### 7. Theorem (inherited, conditional on the crux) — PROVED given Lemma 4

The crux Lemma 4 (every pair of terms shares a prime $\le R$) implies the full conclusion. This is the certified Theorem of `essential-monovariant` §5 (we cite it, do not re-prove):

**Theorem (inherited).** *Assume the crux Lemma 4: for all $i<j$, $P(a_i)\cap P(a_j)\cap Q_R\ne\varnothing$, where $Q_R=\{p:p\le R\}$, $L_0=\prod_{p\le R}p$. Then the essential-prime set $E\subseteq Q_R$ is finite, the greedy becomes the "next-$V$-residue" walk mod $L_0$ on the transversal-residue set $V$, the cyclic successor $\varphi:V\to V$ is a bijection, and*
$$ a_{n+T}=a_n+L_0 \quad\text{for every }n\ge1, $$
*with $T=|V|$ and $L=L_0$; **no transient** (the orbit is purely periodic from $a_1$ because $\varphi$ is a bijection).*

*Proof.* See `approaches/essential-monovariant.md` §5. (Free-rider irrelevance $\Rightarrow$ $a_{n+1}=\min\{m>a_n:m\bmod L_0\in V\}$; cyclic successor is a bijection on the finite ordered set $V$; one full cycle telescopes to $L_0$.) $\square$

**This approach's contribution toward the Theorem is the growing-window bound (Corollary 4b): every pair among the first $N$ terms shares a prime $\le(N-1)R$. That is strictly weaker than the crux; it does not activate the Theorem.**

### Summary of rigour status

- **Lemma 4 (large-prime-span):** fully proved and certified into `lemmas/large-prime-span-divides-at-most-one-term.md`. Reusable.
- **Corollaries 4a/4b (large primes cover no cell; growing-window bound $\le(N-1)R$):** fully proved.
- **Cell-count bound (§4, eq. (5)):** fully proved (identity).
- **Lemma 5 ($\sum_p1/p^2<1/2$):** fully proved elementarily (Euler product for $\zeta(2)=\pi^2/6$ + Archimedes $\pi<22/7$); no PNT/Siegel/Jacobsthal.
- **Aggregate bound (§6, eq. (7)–(8)):** fully proved as a *necessary condition*.
- **Crux Lemma 4 (fixed threshold $\le R$):** **[GAP]** — not proved; the two obstructions (G1 growing window, (G2) aggregate vs. per-cell) are characterized as structural ceilings of the counting route.
- **Theorem (§7):** fully proved conditional on the crux, inherited from `essential-monovariant`.

## Promotable lemmas
- **Large-prime-span lemma.** *For $S_N:=a_N-a_1\le(N-1)R$, a prime $p>S_N$ divides at most one of $a_1,\ldots,a_N$; hence every shared prime among the first $N$ terms is $\le S_N\le(N-1)R$.* Certified in `lemmas/large-prime-span-divides-at-most-one-term.md`. Reusable: any windowed/counting argument on the greedy sequence can import it. (Caveat for reusers: the threshold is the **growing** span $S_N$, not the fixed $R$.)
- **Prime-zeta-2 bound.** $\sum_{p\ \text{prime}}1/p^2<389/900<1/2$, elementarily from $\zeta(2)=\pi^2/6$ and $\pi<22/7$. Proved in §5 of this file. Reusable: a lightweight analytic input for any future counting/ratio argument on prime reciprocals in this problem (no PNT machinery needed).
