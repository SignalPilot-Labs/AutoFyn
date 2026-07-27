# IMO 2026 P6 — approach `transversal-single-cycle-finish` (mechanism δ)

**Problem.** Let $a_1,a_2,\ldots$ be integers $>1$ with $a_{n+1}$ the smallest integer $>a_n$ such that $\gcd(a_{n+1},a_i)>1$ for every $i=1,\ldots,n$. Prove $\exists\,T,L>0$ with $a_{n+T}=a_n+L$ for all $n\ge 1$.

**Framing of this approach.** We leave the "finiteness of the minimal-support family" wall as an **explicit gap** (Hypothesis GAP below) and prove, rigorously and unconditionally, that *as soon as* that single hypothesis holds, the full conclusion $a_{n+T}=a_n+L$ (for **every** $n\ge 1$, no transient) follows. Along the way we dissolve two worries the outliner raised — the "single-cycle" worry and the "transient absorption" worry — by showing both rest on a misdefinition of the greedy map and on overlooking a universal-membership lemma, respectively. The distinctive importable output is the clean post-stabilization machine (Lemmas 1–5).

---

## Status
partial

## Approaches tried
- `transversal-single-cycle-finish` (round 1) — Built the complete conditional theorem "minimal-support family finite $\Longrightarrow$ $a_{n+T}=a_n+L$ for all $n$." Proved the transversal-residue characterization, the universal-membership lemma (every $a_n$'s support hits the full minimal-support family — this kills the transient), the greedy-equals-cyclic-successor identity, and the (trivial) single-cycle + period-sum-$=L$ step. Verified computationally on $a_1=15$ ($T=8,L=30$) and $a_1=429$ ($T=908,L=4290$, $|M|=5$). The only remaining gap is the stabilization hypothesis itself (GAP), which is the wall the density (α) and Dickson (β) approaches attack; this approach does not attempt it.

## Current best
The conditional theorem stated as Theorem A below: **if** the family $\mathcal M$ of minimal elements of $\{P(a_i):i\ge 1\}$ is finite, **then** $a_{n+T}=a_n+L$ for every $n\ge 1$, with $L=\prod_{p\in\bigcup\mathcal M}p$ (squarefree) and $T=|V|$ where $V\subseteq\mathbb Z/L\mathbb Z$ is the transversal-residue set. The proof is complete and rigorous except for the single hypothesis $\mathcal M$ finite (GAP). The two sub-worries the outliner flagged — single-cycle and transient absorption — are proved here to be *non-issues*: the cyclic successor on an ordered finite set is tautologically one cycle, and every $a_n$ already lies in $V$ (Lemma 2), so there is no transient.

**Open gap.** Prove that $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite. Equivalently: only finitely many primes are "load-bearing" and the minimal-support antichain stabilizes. This is the shared wall; it is attacked by `density-promotion-bound` (Mertens/$\sum 1/p$ transversal density) and `bertrand-dickson-eviction` (Bertrand + Dickson's lemma). Once either supplies a proof of GAP, Theorem A here closes the problem.

## Full proof

### Notation and the stabilization hypothesis

For an integer $m>1$ write $P(m)=\{p:p\text{ prime},\;p\mid m\}$ for its set of prime divisors. Write $\mathcal F=\{P(a_i):i\ge 1\}$ for the family of all term-supports and $\mathcal M=\min(\mathcal F)$ for its minimal elements under inclusion (the *minimal supports*). Set
$$P\;=\;\bigcup_{m\in\mathcal M} m\quad\text{(the structural primes)},\qquad L\;=\;\prod_{p\in P}p.$$
Because $P$ is a set of primes, $L$ is squarefree by construction (each prime appears to the first power). For a residue $r\in\{0,\ldots,L-1\}$ write $S_P(r)=\{p\in P:p\mid r\}$ (where $p\mid r$ means $r\equiv 0\pmod p$). Since $L$ is squarefree, the Chinese Remainder Theorem (KB: *Modular arithmetic, CRT*) identifies $\mathbb Z/L\mathbb Z\cong\prod_{p\in P}\mathbb Z/p\mathbb Z$, so $r$ is determined by $(r\bmod p)_{p\in P}$, equivalently by $S_P(r)$ together with the nonzero residues — but for the divisibility pattern $S_P(r)$ alone suffices. Define the **transversal-residue set**
$$V\;=\;\bigl\{r\in\{0,\ldots,L-1\}: S_P(r)\text{ is a transversal (hitting set) of }\mathcal M\bigr\}.$$

> **Hypothesis (GAP).** $\mathcal M$ is finite.
>
> (Equivalently: $P=\bigcup\mathcal M$ is finite, $L$ is a well-defined positive integer, and $V$ is a finite nonempty set. This is the only place finiteness is used. It is the stabilization wall, left to the density/Dickson approaches. Everything below is *unconditional on top of GAP*.)

Nonemptiness: $\mathcal F$ is nonempty ($a_1>1$), so $\mathcal M\neq\emptyset$. For $r=0$ we have $S_P(0)=P$, and $P\cap m=m\neq\emptyset$ for every $m\in\mathcal M$ (since $m\subseteq P$), so $0\in V$. Hence $V\neq\emptyset$ and, listing its elements increasingly,
$$V=\{v_0<v_1<\cdots<v_{k-1}\},\qquad v_0=0,\quad k=|V|\ge 1.$$

---

### Lemma 1 (free-rider invisibility / transversal characterization)
*Assume GAP. An integer $m>1$ satisfies $\gcd(m,a_i)>1$ for every $i\ge 1$ if and only if $m\bmod L\in V$ (equivalently $S_P(m)$ hits $\mathcal M$). In particular, admissibility against the whole past depends only on the residue of $m$ modulo $L$.*

**Proof.** The condition $\gcd(m,a_i)>1$ for every $i$ is equivalent to $P(m)\cap P(a_i)\neq\emptyset$ for every $i$, i.e. $P(m)$ is a transversal of $\mathcal F$. A set is a transversal of a family iff it is a transversal of the family's minimal elements, so this is equivalent to: $P(m)\cap m'\neq\emptyset$ for every $m'\in\mathcal M$.

Now $m'\in\mathcal M\subseteq 2^P$ (each minimal support is a subset of $P=\bigcup\mathcal M$). Hence $P(m)\cap m'=\bigl(P(m)\cap P\bigr)\cap m'=S_P(m)\cap m'$. A prime $q\mid m$ with $q\notin P$ lies in *no* minimal support (since $\bigcup\mathcal M=P$), so it is invisible to the hitting condition — it cannot help hit any $m'$. Therefore $P(m)$ hits $\mathcal M$ iff $S_P(m)$ hits $\mathcal M$, iff $m\bmod L\in V$ (CRT, since $S_P(m)$ depends only on $m\bmod L$). ∎

*Remark.* This is the rigorous "free-rider lemma" — but, under GAP, it is a one-liner, **not** the inductive claim the outliner feared. The inductive worry ("a non-structural prime might become structural later") concerns *stabilization* (i.e. GAP itself); once $\mathcal M$ is the full stabilized family, free-rider invisibility for admissibility is immediate because $\bigcup\mathcal M=P$ already contains every load-bearing prime.

---

### Lemma 2 (universal membership — every term already lies in $V$)
*Assume GAP. For every $n\ge 1$, $a_n\bmod L\in V$; equivalently $P(a_n)$ hits $\mathcal M$.*

This is the key lemma: it shows there is **no transient**. (The outliner flagged transient absorption as a gap; the lemma discharges it.)

**Proof.** Fix $n\ge 1$ and $m'\in\mathcal M$. Because $m'$ is minimal in $\mathcal F$, it is a *member* of $\mathcal F$: $m'=P(a_j)$ for some $j\ge 1$. We show $P(a_n)\cap m'\neq\emptyset$ by trichotomy on $j$ vs $n$.

- **$j<n$.** Then $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}\supseteq\{a_j\}$, so $\gcd(a_n,a_j)>1$, i.e. $P(a_n)\cap P(a_j)\neq\emptyset$. Since $P(a_j)=m'$, $P(a_n)\cap m'\neq\emptyset$.
- **$j>n$.** Then $a_j$ was chosen admissible against $a_1,\ldots,a_{j-1}\supseteq\{a_n\}$ (as $n<j$), so $\gcd(a_j,a_n)>1$, i.e. $P(a_j)\cap P(a_n)\neq\emptyset$; again $m'\cap P(a_n)\neq\emptyset$.
- **$j=n$.** Then $m'=P(a_n)$, and $P(a_n)\cap m'=P(a_n)\neq\emptyset$ (as $a_n>1$).

So $P(a_n)$ meets every $m'\in\mathcal M$; by Lemma 1, $a_n\bmod L\in V$. ∎

---

### Lemma 3 (greedy $=$ cyclic successor)
*Assume GAP. For every $n\ge 1$,*
$$a_{n+1}\;=\;\min\{m>a_n:\;m\bmod L\in V\}.$$
*Equivalently, with $r_n:=a_n\bmod L\in V$, the residue $r_{n+1}=a_{n+1}\bmod L$ equals the **cyclic successor** $\varphi(r_n)$, where $\varphi(r)=\min\{v\in V:v>r\}$ if such $v$ exists, else $\varphi(r)=v_0=0$ (wrap).*

**Proof.** Two containments, both under GAP.

**($\ge$).** By Lemma 1, $\{m:m\bmod L\in V\}\subseteq\{m:\gcd(m,a_i)>1\ \forall i\le n\}$: indeed $m\bmod L\in V$ means $S_P(m)$ hits $\mathcal M$; then for each $i\le n$, $P(a_i)$ contains some $m_i\in\mathcal M$ (every member of $\mathcal F$ contains a minimal element), and $S_P(m)\cap m_i\neq\emptyset\subseteq P(m)\cap P(a_i)$, so $\gcd(m,a_i)>1$. Hence the admissible set (against $a_1,\ldots,a_n$) contains the $V$-residue set; its minimum above $a_n$ is therefore $\le$ the minimum of the $V$-residue set above $a_n$:
$$a_{n+1}=\min\{m>a_n:\text{admissible}\}\;\le\;\min\{m>a_n:m\bmod L\in V\}.$$

**($\le$).** By Lemma 2, $a_{n+1}\bmod L\in V$, and $a_{n+1}>a_n$; so $a_{n+1}$ is a member of $\{m>a_n:m\bmod L\in V\}$, hence $a_{n+1}\ge\min\{m>a_n:m\bmod L\in V\}$.

Equality follows. Writing $a_n=q_nL+r_n$ ($r_n\in V$, $v_0=0\le r_n\le v_{k-1}$), the smallest $m>a_n$ with $m\bmod L\in V$ is $q_n L+v_{i+1}$ if $r_n=v_i<v_{k-1}$ (the next $V$-element above $r_n$ in the current block), and $(q_n+1)L+v_0=(q_n+1)L$ if $r_n=v_{k-1}$ (wrap to the next block). Thus $r_{n+1}=\varphi(r_n)$ as claimed, and $a_{n+1}=a_n+\bigl[(\varphi(r_n)-r_n)\bmod L\bigr]$ where the bracket is taken in $\{1,\ldots,L\}$. ∎

*Remark.* Bounded gaps are a corollary: $a_{n+1}\le a_n+L$, since the multiple of $L$ immediately above $a_n$ has residue $0\in V$ and is at most $a_n+L$ away.

---

### Lemma 4 (single cycle — the "distinctive" step, proved trivial)
*Assume GAP. The cyclic successor $\varphi:V\to V$ is a single $k$-cycle: $\varphi(v_i)=v_{i+1\!\pmod{\!k}}$. In particular every orbit of $\varphi$ is all of $V$, of period $k=|V|$.*

**Proof.** By definition $\varphi(v_i)=v_{i+1}$ for $0\le i<k-1$ (the next element of $V$ above $v_i$) and $\varphi(v_{k-1})=v_0$ (wrap). This is the cycle $(v_0\,v_1\,\cdots\,v_{k-1})$ — a single $k$-cycle. ∎

*Remark — dissolving the outliner's worry.* The outliner feared "the cyclic successor might split into several sub-cycles; pairwise-intersecting does not force a connected cyclic order." That fear rests on a *misdefinition*: it imagines $\varphi$ as a map built from pairwise prime-intersection ("jump to the next residue sharing a prime with the current"). But the greedy map $\varphi$ is the **plain cyclic successor in the ordered set $V$** (Lemma 3), which walks $V$ in increasing cyclic order and is tautologically one cycle. There is no second ingredient to add and no decomposition possible. The pairwise-intersection structure of $V$ (true: any two admissible residues both hit $\mathcal M$, though they need not share a prime of $P$) is irrelevant to cyclicity; it only shapes *which* residues are in $V$.

---

### Lemma 5 (period-sum $=L$ exactly)
*Assume GAP. Over one full period of $k=|V|$ steps, the total increment is exactly $L$:*
$$\sum_{i=0}^{k-1}\bigl[(\varphi(v_i)-v_i)\bmod L\bigr]\;=\;L.$$

**Proof.** The increments telescope around the cycle. Writing the wrap increment at $i=k-1$ as $L-v_{k-1}+v_0$:
$$\sum_{i=0}^{k-1} d_i=(v_1-v_0)+(v_2-v_1)+\cdots+(v_{k-1}-v_{k-2})+(L-v_{k-1}+v_0)$$
$$=(v_{k-1}-v_0)+(L-v_{k-1}+v_0)=L,$$
since $v_0=0$. ∎

---

### Theorem A (post-stabilization conclusion, for all $n$)
*Assume GAP (the family $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite). Then with $L=\prod_{p\in\bigcup\mathcal M}p$ (squarefree) and $T=|V|$ (the number of transversal residues of $\mathcal M$ modulo $L$),*
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1.$$

**Proof.** By Lemma 2 every $r_n=a_n\bmod L$ lies in $V$; by Lemma 3 the update is $r_{n+1}=\varphi(r_n)$; by Lemma 4 every orbit of $\varphi$ runs through all of $V$ in $T=|V|=k$ steps; by Lemma 5 the total increment over those $k$ steps is $L$. Hence $a_{n+k}=a_n+L$ for every $n\ge 1$. Setting $T=k$, this is the claimed relation. ∎

---

### Computational verification

The cyclic-structure claims (Lemmas 2–5) were verified exactly (python3 + sympy) on the two cases the dispatch requested.

**$a_1=15$.** $\mathcal M=\bigl\{\{2,3\},\{2,5\},\{3,5\}\bigr\}$, $P=\{2,3,5\}$, $L=30$, $V=\{0,6,10,12,15,18,20,24\}$, $T=|V|=8$. Checks (60 terms): every $a_n\bmod 30\in V$; the cyclic successor reproduces the sequence from $n=1$; $a_{n+8}=a_n+30$ for all $n$ in range. (Block $B$ as in the dispatch.)

**$a_1=429=3\cdot 11\cdot 13$.** $\mathcal M=\bigl\{\{2,3\},\{2,5,11\},\{2,5,13\},\{3,5\},\{3,11,13\}\bigr\}$ (5 minimal supports), $P=\{2,3,5,11,13\}$, $L=4290$, $|V|=908$. Checks (2000 terms): every $a_n\bmod 4290\in V$; cyclic successor reproduces the sequence from $n=1$; $a_{n+908}=a_n+4290$ for all $n$ in range. Note $P(a_1)=\{3,11,13\}\in\mathcal M$ and hits every member of $\mathcal M$ (consistent with Lemma 2): e.g. $\{3,11,13\}\cap\{2,3\}=\{3\}$, $\cap\{2,5,11\}=\{11\}$, $\cap\{2,5,13\}=\{13\}$, $\cap\{3,5\}=\{3\}$.

These checks confirm the lemmas; they are not proof steps (the proofs above stand on their own).

---

## Gaps

**GAP (the stabilization wall — the only gap).** Prove that $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite.

Unpacked, this asks: only finitely many primes are load-bearing (appear in some minimal support), and the minimal-support antichain stabilizes. It is the wall the whole field converges to:
- `density-promotion-bound` (α) attacks it via a Mertens / $\sum 1/p$ transversal-density bound (showing $S$-transversal composites become dense enough to outbid any would-be new structural prime).
- `bertrand-dickson-eviction` (β) attacks it via Bertrand eviction of large primes + Dickson's lemma on the bounded ambient prime set.

Either, once certified, combines with Theorem A here to solve the problem. The hypothesis is exactly "the minimal-support family of the full sequence is a finite antichain"; no stronger assumption (no "stabilizes from index $N_0$", no "transient length $0$") is needed — Lemma 2 delivers universal membership and hence zero transient for free.

**Sub-worries the outliner raised, now discharged (not gaps).**
- *Single-cycle:* dissolved by Lemma 4 — the cyclic successor on an ordered finite set is tautologically one cycle; the worry came from conflating it with a pairwise-intersection-based map.
- *Transient absorption:* dissolved by Lemma 2 — every $a_n$ already lies in $V$, so the cyclic dynamics hold from $n=1$.
- *Squarefree $L$:* dissolved by construction — $L=\prod_{p\in P}p$ for $P$ a set of primes.
- *Free-rider invisibility (inductive):* dissolved by Lemma 1 — under GAP it is the one-liner $\bigcup\mathcal M=P$; the inductive content lives in proving GAP itself.

---

## Promotable lemmas

Each is proved in full above under the single hypothesis GAP ($\mathcal M$ finite). Once GAP is certified elsewhere, these become importable by any approach.

1. **`transversal-residue-characterization`** (Lemma 1, this file). *Assume $\mathcal M$ finite. Then $m$ is admissible ($\gcd(m,a_i)>1\,\forall i$) iff $m\bmod L\in V$, where $L=\prod_{p\in\bigcup\mathcal M}p$ and $V=\{r:S_P(r)\text{ hits }\mathcal M\}$. Free-rider primes ($\notin\bigcup\mathcal M$) are invisible to admissibility.* — no induction; uses only $\bigcup\mathcal M=P$ and CRT over squarefree $L$.

2. **`universal-membership-no-transient`** (Lemma 2, this file). *Assume $\mathcal M$ finite. Then $a_n\bmod L\in V$ for every $n\ge 1$.* — key no-transient lemma; uses the trichotomy $j<n/j>n/j=n$ on the index $j$ with $P(a_j)=m'\in\mathcal M$ and the greedy admissibility of $a_n$ against earlier terms / of later terms against $a_n$.

3. **`greedy-equals-cyclic-successor`** (Lemma 3, this file). *Assume $\mathcal M$ finite. Then $a_{n+1}=\min\{m>a_n:m\bmod L\in V\}$; equivalently $r_{n+1}=\varphi(r_n)$, the cyclic successor in $V$.* — combines Lemmas 1–2 (containment both ways). Corollary: gaps $d_n\le L$.

4. **`cyclic-successor-single-cycle`** (Lemma 4, this file). *The cyclic successor $\varphi$ on the increasingly-listed finite set $V=\{v_0<\cdots<v_{k-1}\}$ is the single $k$-cycle $(v_0\,v_1\,\cdots\,v_{k-1})$; period-sum $=L$ (Lemma 5).* — tautological once $\varphi$ is correctly identified as the plain cyclic successor.

5. **`post-stabilization-theorem`** (Theorem A, this file). *Assume $\mathcal M$ finite. Then $a_{n+T}=a_n+L$ for every $n\ge 1$, with $T=|V|$ and $L=\prod_{p\in\bigcup\mathcal M}p$.* — the conditional closing theorem; assembles Lemmas 1–5.
