# Approach: bertrand-dickson-eviction (mechanism β — WQO + Bertrand eviction)

Problem: greedy sequence $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$. Prove $\exists\,T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

## Status
partial

## Approaches tried
- **Round 1 (this build).** Mechanism β. Built the full conditional pipeline: transversal characterization → refinement monotonicity → pairwise-intersection of ever-minimal supports → gap bound at promotion (Lemma 5, the β-attack) → conditional on stabilization, the free-rider/CRT reduction to a residue cycle, single-cycle, and period-sum $=L$, with transient provably $0$ (every term is a transversal of $\mathcal M^*$, so the greedy equals the cyclic successor from $n=1$). The conditional pipeline is COMPLETE and gives the theorem for all $n\ge1$ assuming stabilization. The Bertrand/gap-bound eviction of large primes does NOT close: the bound $a_i-a_{i-1}\le\prod O$ depends on $a_{i-1}$, so it bounds neither the size nor the count of essential primes. The stabilization wall (finiteness of the essential-prime set / ever-minimal supports) remains the single open gap. Honest partial.

## Current best
The entire theorem reduces, with a complete rigorous proof, to the single wall **"the set of ever-minimal supports is finite"** (equivalently, $\mathcal M_n$ stabilizes, equivalently the essential-prime set $P_{\mathrm{ess}}$ is finite). Everything downstream of that wall is proved in full here, including the two steps the field had flagged as separate gaps — the single-cycle/period-sum-$=L$ lemma and the transient-absorption (transient is provably $0$). The wall itself is attacked by the gap bound (Lemma 5) but the attack does not close; the precise obstruction is identified below.

Key proven facts:
- $a_{n+1}$ is the smallest $m>a_n$ whose prime-divisor set is a transversal of $\mathcal M_n$ (Lemma 1).
- $\operatorname{Tr}(\mathcal M_n)$ is nested decreasing (Lemma 3).
- Ever-minimal supports are pairwise intersecting and the inclusion order on them is well-founded (no infinite descending chains); see Lemma 4.
- New essential primes enter ONLY at "promotion" steps (steps where $P(a_{n+1})$ is a new minimal); at such a step, the gap $a_{n+1}-a_n\le\prod O$ where $O$ is the set of old essential primes in $P(a_{n+1})$ (Lemma 5).
- [Conditional on stabilization] every term's support is a transversal of $\mathcal M^*$, so $a_n\bmod L\in R$ for all $n$ (Lemma 7), and the greedy equals the $R$-cyclic-successor from $n=1$ (Lemma 8). Hence NO transient.
- [Conditional] the cyclic-successor map on $R$ is a single cycle of length $|R|$, gap-sum $=L$ (Lemma 9), giving $a_{n+T}=a_n+L$ for ALL $n\ge1$ with $T=|R|$, $L=\prod_{p\in P_{\mathrm{ess}}}p$ (Theorem).

Open gap: finiteness of $P_{\mathrm{ess}}$ / stabilization of $\mathcal M$ (the eviction wall). The Bertrand postulate does not evict; the gap bound is the strongest available partial result and it is insufficient (see Gaps).

## Full proof
Not present — Status is `partial`. The conditional pipeline (a complete proof modulo the wall) is written out under "Partial proof" below; the wall is under "Gaps."

---

## Partial proof (rigorous lemmas)

### Notation

- $P(m)$: set of prime divisors of $m$.
- $\mathcal F_n=\{P(a_1),\dots,P(a_n)\}$ (a set of finite prime-sets).
- $\mathcal M_n$: the inclusion-minimal elements of $\mathcal F_n$ (the **minimal supports**).
- $\operatorname{Tr}(\mathcal A)$: the transversals (hitting sets) of a family $\mathcal A$.
- A support is **ever-minimal** if it lies in $\mathcal M_n$ for some $n$. Write $\mathbb M=\bigcup_{n\ge1}\mathcal M_n$.
- $P_{\mathrm{ess},n}=\bigcup\mathcal M_n$ (primes appearing in a minimal support through time $n$); $P_{\mathrm{ess}}=\bigcup_{n\ge1}P_{\mathrm{ess},n}=\bigcup_{M\in\mathbb M}M$ (essential primes).
- "Promotion at step $i$": $P(a_i)\in\mathcal M_i\setminus\mathcal M_{i-1}$ (a new minimal support is introduced).

### Lemma 1 (Transversal characterization of admissibility)
For $m>a_n$, $m$ is admissible ($\gcd(m,a_i)>1$ for all $i\le n$) iff $P(m)$ is a transversal of $\mathcal M_n$.

*Proof.* $\gcd(m,a_i)>1\iff P(m)\cap P(a_i)\neq\emptyset$. This holds for every $i\le n$ iff $P(m)$ intersects every member of $\mathcal F_n$. A set intersects every member of $\mathcal F_n$ iff it intersects every **minimal** member: if $M\in\mathcal M_n$ then $M\in\mathcal F_n$ so it is hit; conversely every $S\in\mathcal F_n$ contains some $M\in\mathcal M_n$ (by definition of minimal), and hitting $M$ hits $S$. ∎

**Corollary (greedy = smallest transversal-support).** $a_{n+1}=\min\{m>a_n: P(m)\in\operatorname{Tr}(\mathcal M_n)\}$.

### Lemma 2 (Singleton freeze)
If $\{p\}\in\mathcal M_n$ for some $n$ (a singleton minimal support), then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$ (the family is frozen).

*Proof.* The singleton $\{p\}$ has no proper nonempty subset, so it can never be refined away: it remains in $\mathcal M_m$ for all $m\ge n$. Now any future term $a_{m+1}$ ($m\ge n$) is admissible, hence by Lemma 1 $P(a_{m+1})$ is a transversal of $\mathcal M_m$, so it hits $\{p\}$, i.e. $p\in P(a_{m+1})$, i.e. $\{p\}\subseteq P(a_{m+1})$. Thus $P(a_{m+1})$ is dominated by $\{p\}$ and is not a new minimal. No new minimal is ever added after $n$, and no existing minimal can be removed (removal requires a proper subset to appear, which would be a new minimal — impossible). So $\mathcal M$ is constant. ∎

(For example $a_1=p^k$ gives $\mathcal M_1=\{\{p\}\}$, frozen immediately, $L=p$, $T=1$: the "collapse" case.)

### Lemma 3 (Refinement; transversals shrink)
$\mathcal F_{n+1}\supseteq\mathcal F_n$. Hence every $M\in\mathcal M_n$ contains some $M'\in\mathcal M_{n+1}$, and consequently $\operatorname{Tr}(\mathcal M_{n+1})\subseteq\operatorname{Tr}(\mathcal M_n)$.

*Proof.* The family grows, so its minimal elements refine: a set minimal in $\mathcal F_n$ either stays minimal in $\mathcal F_{n+1}$ or is superseded by a minimal subset (which must be $P(a_{n+1})$ itself, the only new member). Transversals of a refined family are transversals of the coarser family: hitting every minimal of $\mathcal F_{n+1}$ implies hitting every minimal of $\mathcal F_n$ (each former minimal contains a new minimal). ∎

So the valid set $V_n:=\{m:P(m)\in\operatorname{Tr}(\mathcal M_n)\}$ is nested decreasing: $V_1\supseteq V_2\supseteq\cdots$.

### Lemma 4 (Pairwise intersection and well-foundedness of $\mathbb M$)
The set $\mathbb M$ of ever-minimal supports is pairwise intersecting ($A\cap B\neq\emptyset$ for all $A,B\in\mathbb M$), and the inclusion order on $\mathbb M$ is well-founded (no infinite strictly descending chain).

*Proof.* **Pairwise intersection.** Let $A,B\in\mathbb M$ with $A$ first appearing in $\mathcal M_i$, $B$ in $\mathcal M_j$, WLOG $i\le j$. At time $j$, $B=P(a_j)$ is admissible, so $P(a_j)=B$ is a transversal of $\mathcal M_{j-1}$ (Lemma 1). Either $A\in\mathcal M_{j-1}$ (if $A$ has not been refined away by time $j-1$), in which case $B$ hits $A$ directly; or $A\notin\mathcal M_{j-1}$, meaning some proper subset $A'\subsetneq A$ became minimal during $(i,j)$ — but then $A'\in\mathbb M$ and $A'\in\mathcal M_{j-1}$, so $B$ hits $A'\subseteq A$, hence $B\cap A\neq\emptyset$. (The refinement chain starting from $A$ terminates because sizes are $\ge1$; at its bottom the current minimal subset of $A$ is in $\mathcal M_{j-1}$ and is hit by $B$.) The case $j<i$ is symmetric. So $A\cap B\neq\emptyset$.

**Well-foundedness.** If $A\subsetneq B$ with both ever-minimal, then $A$ must be introduced strictly after $B$: at the moment $B$ is introduced (new minimal), no member of $\mathcal F$ so far is a proper subset of $B$, so $A$ (a proper subset of $B$) is not yet in the family. Thus inclusion among ever-minimal supports is **time-reversing**: subsets are introduced later. A strictly descending chain $A_1\supsetneq A_2\supsetneq\cdots$ has $|A_1|>|A_2|>\cdots\ge1$, hence is finite. ∎

**Remark (this is not enough).** Pairwise intersection + well-foundedness do **not** force finiteness: the family $\{\{2,p\}:p\text{ prime},\,p>2\}$ is pairwise intersecting (shares $2$), well-founded (an antichain, no chains), and infinite. So Lemma 4 alone does not bound $P_{\mathrm{ess}}$. (Ever-minimal supports are in general **not** an inclusion-antichain — refinement creates subset pairs; e.g. $a_1=30=2\cdot3\cdot5$ gives $\{2,3,5\}\in\mathcal M_1$ then $\{2\}\in\mathcal M_2$, both ever-minimal, $\{2\}\subset\{2,3,5\}$.)

### Lemma 5 (Gap bound at promotion — the β-attack on the wall)
Suppose a promotion occurs at step $i$ ($i\ge2$): $P(a_i)\in\mathcal M_i\setminus\mathcal M_{i-1}$. Partition $P(a_i)=O\sqcup N$ where $N=P(a_i)\setminus P_{\mathrm{ess},i-1}$ (the **new** primes, entering essentiality now) and $O=P(a_i)\cap P_{\mathrm{ess},i-1}$ (old essential primes). Then:
(i) $O\neq\emptyset$ and $O$ is a transversal of $\mathcal M_{i-1}$;
(ii) the gap satisfies $a_i-a_{i-1}\le\prod_{p\in O}p$.

*Proof.* (i) $P(a_i)$ is a transversal of $\mathcal M_{i-1}$ (admissibility, Lemma 1). A prime $q\in N$ lies in no member of $\mathcal M_{i-1}$ (since $q\notin P_{\mathrm{ess},i-1}=\bigcup\mathcal M_{i-1}$), so $q$ contributes nothing to hitting any minimal. Therefore all the hitting is done by $O$: $O$ intersects every $M\in\mathcal M_{i-1}$, i.e. $O$ is a transversal. Since $\mathcal M_{i-1}\neq\emptyset$ (it contains $\mathcal M_1=\{P(a_1)\}$), the empty set is not a transversal, so $O\neq\emptyset$.

(ii) Let $L_O=\prod_{p\in O}p$ (squarefree). Any positive multiple $m$ of $L_O$ has $O\subseteq P(m)$, so $P(m)\supseteq O$; since $O$ is a transversal and supersets of transversals are transversals, $P(m)$ is a transversal of $\mathcal M_{i-1}$, i.e. $m\in V_{i-1}$. The smallest multiple of $L_O$ strictly above $a_{i-1}$ is at most $a_{i-1}+L_O$ and is a valid candidate. The greedy choice $a_i$ is the smallest valid integer above $a_{i-1}$, so $a_i\le a_{i-1}+L_O$. ∎

**Corollary (new primes divide a bounded-above term).** At a promotion introducing new primes $N$, every $q\in N$ divides $a_i$, so $q\le a_i\le a_{i-1}+\prod_{p\in O}p\le a_{i-1}+\prod_{p\in P_{\mathrm{ess},i-1}}p$.

**This is the precise point where the β-attack stalls.** The bound involves $a_{i-1}$, which grows without limit (the sequence is strictly increasing and unbounded — it contains infinitely many distinct integers, since the greedy is injective). So Lemma 5 bounds neither the values of new essential primes nor their number. See Gaps.

### Lemma 6 (Dickson's lemma — the WQO completing half)
**Dickson's lemma.** For every fixed $k$, the poset $(\mathbb N^k,\le_{\mathrm{prod}})$ with $(x_1,\dots,x_k)\le(y_1,\dots,y_k)\iff x_j\le y_j\ \forall j$ is a well-quasi-order: every infinite sequence has an increasing pair, equivalently there is no infinite antichain.

*Standard proof (sketch, for completeness).* Induct on $k$. $k=1$: $\mathbb N$ is well-ordered. For $k\ge2$, given an infinite sequence $v^{(1)},v^{(2)},\dots\in\mathbb N^k$, project to the last coordinate and use the infinite-pigeonhole/Ramsey argument to extract an infinite subsequence on which the last coordinate is non-decreasing; apply the $k-1$ induction to the projections onto the first $k-1$ coordinates within that subsequence to find an increasing pair. (This is the standard Maclagan/Higman-style induction; cf. the WQO entry of the knowledge base under "Invariants & monovariants"/"Pigeonhole".) ∎

**How Dickson would complete the eviction (conditional).** Suppose a uniform finite bound $C$ on the essential primes is known, so $P_{\mathrm{ess}}\subseteq\{p:p\le C\}$, a finite universe of size $k=\pi(C)$. Encode each support $M\in\mathbb M$ as its characteristic vector $\mathbf 1_M\in\{0,1\}^k\subseteq\mathbb N^k$. By Dickson, $\{0,1\}^k$ (indeed $\mathbb N^k$) has no infinite antichain. But this is moot: once $P_{\mathrm{ess}}\subseteq\{p\le C\}$ is finite, there are only $2^k$ possible supports altogether, so $\mathbb M$ is automatically finite and $\mathcal M_n$ stabilizes trivially (refinement on a finite Boolean lattice terminates). Thus **Dickson is conditional on the universe bound and is not itself the hard half**; the hard half is bounding the universe of essential primes. The knowledge-base entry "Invariants & monovariants" and "Pigeonhole/extremal" support this finite-state termination step.

---

### Conditional pipeline (assumes the wall is fallen)

For the remainder, **assume**:

> **(WALL)** $\mathbb M$ is finite. Equivalently $P_{\mathrm{ess}}$ is finite and $\mathcal M_n$ stabilizes: there is $n_0$ with $\mathcal M_n=\mathcal M^*$ for all $n\ge n_0$.

(The equivalence: if $\mathbb M$ is finite, refinement on the finite set $\mathbb M$ terminates since each support is removed at most once and added at most once; conversely stabilization trivially makes $\mathbb M$ finite.)

Define, under (WALL):
- $\mathcal M^*=\lim_n\mathcal M_n$ (the stabilized minimal-support family; an inclusion-antichain).
- $P_{\mathrm{ess}}=\bigcup\mathcal M^*$ (finite), $L=\prod_{p\in P_{\mathrm{ess}}}p$ (squarefree).
- $R=\{r\in\mathbb Z/L\mathbb Z:\{p\in P_{\mathrm{ess}}:p\mid r\}\in\operatorname{Tr}(\mathcal M^*)\}$ (valid residues).

### Lemma 7 (Free-rider invisibility / admissibility depends only on residue mod $L$)
For any integer $m$, $m$ is admissible w.r.t. $\mathcal M^*$ (i.e. $P(m)\in\operatorname{Tr}(\mathcal M^*)$) iff $m\bmod L\in R$.

*Proof.* Since $L$ is squarefree and $P_{\mathrm{ess}}$ is exactly the set of primes dividing $L$, CRT (knowledge base "Modular arithmetic, CRT") gives: for $p\in P_{\mathrm{ess}}$, $p\mid m\iff p\mid(m\bmod L)$. For $q\notin P_{\mathrm{ess}}$ (a free-rider prime), $q$ lies in no member of $\mathcal M^*$, so $q$'s presence or absence in $P(m)$ does not affect whether $P(m)$ hits every member of $\mathcal M^*$. Thus transversality of $P(m)$ depends only on $\{p\in P_{\mathrm{ess}}:p\mid m\}=\{p\in P_{\mathrm{ess}}:p\mid(m\bmod L)\}$, i.e. on $m\bmod L$, and equals membership in $R$. ∎

### Lemma 8 (Every term is a transversal of $\mathcal M^*$; greedy = cyclic successor; transient is $0$)
Under (WALL): for every $n\ge1$, $P(a_n)$ is a transversal of $\mathcal M^*$, hence $a_n\bmod L\in R$. Moreover the greedy step coincides with the cyclic successor on $R$:
$$a_{n+1}=a_n+\delta_n,\qquad \delta_n=(\operatorname{succ}_R(a_n\bmod L)-(a_n\bmod L))\bmod L,$$
where $\operatorname{succ}_R(r)=\min\{r'\in R:r'>r\}$ if that set is nonempty, else $\min R$. This holds for **all** $n\ge1$ (no transient).

*Proof.* **Every term is a transversal of $\mathcal M^*$.** Every member $M^*\in\mathcal M^*$ is a minimal element of $\{P(a_1),P(a_2),\dots\}$, hence $M^*=P(a_j)$ for some $j$ (minimal elements are members of the family). For any $n\neq j$, $\gcd(a_n,a_j)>1$: if $n<j$ this holds because $a_j$ was chosen admissible to all earlier terms (including $a_n$); if $n>j$ symmetrically. So $P(a_n)\cap P(a_j)\supseteq P(a_n)\cap M^*\neq\emptyset$. For $n=j$ trivially $P(a_n)\supseteq M^*\neq\emptyset$. Hence $P(a_n)$ intersects every $M^*\in\mathcal M^*$: $P(a_n)\in\operatorname{Tr}(\mathcal M^*)$, i.e. $a_n\bmod L\in R$ (Lemma 7).

**Greedy = cyclic successor.** By Lemma 1, $a_{n+1}$ is the smallest $m>a_n$ with $P(m)\in\operatorname{Tr}(\mathcal M_n)$. By Lemma 3, $\operatorname{Tr}(\mathcal M_n)\supseteq\operatorname{Tr}(\mathcal M^*)$, i.e. $R(\mathcal M_n)\supseteq R$ (fewer constraints so far $\Rightarrow$ larger valid set). The smallest integer $m_*>a_n$ with $m_*\bmod L\in R$ is valid at time $n$ (since $R\subseteq R(\mathcal M_n)$), so the greedy choice satisfies $a_{n+1}\le m_*$. Conversely, by the first part applied to $n+1$, $a_{n+1}\bmod L\in R$ and $a_{n+1}>a_n$, so $a_{n+1}\ge m_*$ (it is an $R$-residue integer above $a_n$, at least the smallest such). Hence $a_{n+1}=m_*=a_n+\delta_n$. ∎

(This closes the transient-absorption gap that the field had flagged: the relation holds from $n=1$, not merely eventually. Verified computationally for $a_1\in\{15,35,77\}$ — residues follow $\operatorname{succ}_R$ from the first term even though $\mathcal M$ stabilizes only later.)

### Lemma 9 (Single cycle; period-sum $=L$)
$R\neq\emptyset$. The map $\operatorname{succ}_R:R\to R$ is a single cycle of length $|R|$ visiting every element of $R$ in increasing cyclic order. Consequently the orbit of any $r\in R$ has period $T=|R|$, and the sum of the gap increments over one full period equals $L$.

*Proof.* $R\neq\emptyset$ because $a_1\bmod L\in R$ (Lemma 8). Order $R=\{r_0<r_1<\cdots<r_{T-1}\}$ with $T=|R|$. By definition $\operatorname{succ}_R(r_j)=r_{j+1}$ for $j<T-1$ and $\operatorname{succ}_R(r_{T-1})=r_0$. This is the cyclic-successor permutation, a single cycle $r_0\to r_1\to\cdots\to r_{T-1}\to r_0$ visiting all of $R$; every orbit has period $T$. The gap from $r_j$ to $r_{j+1}$ is $\delta_j=r_{j+1}-r_j$ (for $j<T-1$) and $\delta_{T-1}=r_0+L-r_{T-1}$ (the wrap). Summing:
$$\sum_{j=0}^{T-1}\delta_j=(r_T-r_0\text{ telescoping, with }r_T:=r_0+L)=L.$$
(Each residue appears once as a "from" and once as a "to" in the cyclic order; the running total advances by exactly $L$ around the circle.) ∎

### Theorem (conditional on WALL)
Under (WALL), set $T=|R|$ and $L=\prod_{p\in P_{\mathrm{ess}}}p$. Then for every $n\ge1$,
$$a_{n+T}=a_n+L.$$

*Proof.* By Lemma 8 the residues $r_n=a_n\bmod L\in R$ evolve as $r_{n+1}=\operatorname{succ}_R(r_n)$. By Lemma 9, $\operatorname{succ}_R$ is a single cycle of length $T=|R|$, so $r_{n+T}=r_n$ for all $n\ge1$. The increments $a_{n+1}-a_n=\delta_n$ are the cyclic gaps, which are $T$-periodic in $n$; their sum over one period is $L$ (Lemma 9). Therefore
$$a_{n+T}-a_n=\sum_{k=0}^{T-1}(a_{n+k+1}-a_{n+k})=\sum_{k=0}^{T-1}\delta_{n+k}=L,$$
for every $n\ge1$. ∎

---

## Gaps

### GAP 1 (the wall): finiteness of $P_{\mathrm{ess}}$ / stabilization of $\mathcal M$.
This is the single load-bearing open step. The β-attack (Lemma 5) gives, at each promotion step $i$ introducing new essential primes $N$ alongside old essential primes $O$,
$$a_i-a_{i-1}\le\prod_{p\in O}p,\qquad q\le a_i\le a_{i-1}+\prod_{p\in O}p\quad(q\in N).$$
The bound depends on $a_{i-1}$, and $a_{i-1}\to\infty$ (the sequence is strictly increasing, injective, unbounded — injectivity: each $a_{n+1}>a_n$). So neither the size of a newly promoted prime nor the total number of promotions is bounded. **Why the bound cannot be sharpened by a Bertrand-type dyadic argument:** the cleanest "small composite transversal" already available is a multiple of $L_O=\prod O$ within $L_O$ of $a_{i-1}$ (Lemma 5); Bertrand's postulate (KB "Bertrand's postulate") guarantees a prime in every dyadic interval $(x,2x]$, but there is no point at which a dyadic interval is forced to contain a *new* essential prime — new primes, if any, are forced by the *absence* of valid numbers in a gap, and the gap structure is exactly what Lemma 5 bounds (with the $a_{i-1}$ dependence). So Bertrand does not evict large primes here.

**Reviewer's circularity flag (addressed).** The bound in Lemma 5 uses $O\subseteq P_{\mathrm{ess},i-1}$ (old essential primes), i.e. only primes already known essential — it does **not** assume $P_{\mathrm{ess}}$ finite. The argument is non-circular as far as it goes; it simply is too weak to bound the count of future promotions. The obstruction is genuine growth of $a_{i-1}$, not a hidden circularity.

**What would close the gap (routes not taken here):**
- An analytic-density argument showing that once enough small primes are essential, the transversal residues $R$ become so dense (relative to $L$) that no promotion can be forced — this is mechanism α (`density-promotion-bound`), the natural partner attack.
- A direct bounded-gap argument ($d_n\le G$ uniformly) implying large primes appear too sparsely to be unique connectors — mechanism γ.
- A structural induction bounding $|P_{\mathrm{ess}}|$ in terms of $\omega(a_1)$ — mechanism ε.

The present approach contributes Lemma 5 (the sharp form of the β-attack) and a complete conditional pipeline; it leaves the wall to a mechanism that can bound promotions without invoking $a_{i-1}$.

### GAP 2 (minor): none beyond GAP 1.
Once GAP 1 is closed, the Theorem above is unconditional and proves the required statement for all $n\ge1$ (transient is $0$ by Lemma 8, single-cycle by Lemma 9, both proved in full). In particular the two steps the outline-reviewer and the explorer flagged as separate shared gaps — single-cycle/period-sum-$=L$ and transient absorption — are **closed here** (each proved in full, conditional only on (WALL)).

## Promotable lemmas
- **Lemma 5 (gap bound at promotion).** Stated and proved in full above (non-circular; the sharp β-attack). At a promotion step $i$ with old essential primes $O\subseteq P(a_i)$, one has $a_i-a_{i-1}\le\prod_{p\in O}p$. Reusable by any approach needing a gap bound at the moment a new essential prime is introduced.
- **Lemma 7 + Lemma 8 (free-rider invisibility and "every term is a transversal of $\mathcal M^*$; greedy = cyclic successor; transient $0$").** Proved in full, conditional on stabilization. These are importable by approaches α/δ/ε as the post-stabilization machinery: they make the residue-cycle reduction rigorous and remove the transient-absorption gap.
- **Lemma 9 (single cycle; period-sum $=L$).** Proved in full. The cyclic-successor map on the valid-residue set $R$ is a single cycle of length $|R|$ with gap-sum $L$. This closes the "single-cycle / period-sum $=L$" gap that the field had isolated as distinctive.
