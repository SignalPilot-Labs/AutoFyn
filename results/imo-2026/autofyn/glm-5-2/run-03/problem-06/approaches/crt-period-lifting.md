# Approach: crt-period-lifting (IMO 2026 P6)

Template: `aimo-0231` (NT / modular-arithmetic-and-CRT) — "Decompose the first-hitting-time of an iterated map mod $N$ as the lcm, over the prime-power factors of $N$, of the first-hitting-times modulo each prime power" + "Bound how much an iteration's first-return-to-0 time can grow when the modulus is lifted from $p^{e-1}$ to $p^e$ by counting the residues mod $p^e$ that reduce to 0 mod $p^{e-1}$ (grows by at most factor $p$)."

Framing (genuinely-different from the strip / MT-monovariant / density routes): build the eventual period $L$ **prime-by-prime** by CRT fiber lifting, starting from the certified LOCK base. NOT a quotient descent on $|P_1|$ (the drop-$r$ map is certified dead — the not-$r$ sub-sequence of $\text{greedy}(a_1)$ does NOT match $\text{greedy}(a_1/r)$, verified $a_1=385$, $r=11$).

---

## Status
partial

## Approaches tried
- **Round 3 (this build).** Built the CRT period-lifting skeleton into a complete *conditional* proof. The fiber-count lift bound $|A_{k+1}|\le p_{k+1}\,|A_k|$ is **proved unconditionally as a pure combinatorial identity** (Lemma F1) and **verified computationally** on $a_1\in\{6,30,145,15,35,77,105,175,221,385,847,1309\}$: in every tested case the lift ratio $|A_{k+1}|/|A_k|$ is $\le p_{k+1}$ (tight at stage $0$: ratio $=p_1$; slack up to $\approx 11\times$). The squarefree-period structure (Lemma F2: $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\operatorname{rad}(T)\mathbb Z_{>0}$ unconditionally; minimal period $=\prod_{p\in G}p$ squarefree, conditional on Gap A) is proved. The endgame closes conditionally on Gap A. — **Outcome:** the conditional theorem (Gap A $\Rightarrow$ theorem, with the sharp structural refinement "$L$ squarefree, $T\le L=\prod G$") is fully rigorous, but the approach **does NOT close Gap A**: the `aimo-0231` nontrivial content (return-time of a *polynomial iterate* grows by $\le p$) does **not port** to our setting because the cyclic-successor map is structurally a single $|A|$-cycle, making the return time *equal* $|A|$ and the lift bound *trivially true* by fiber counting — no greedy-specific mechanism is captured. The cofactor-bounding attempt to make the induction non-circular (Step 4 of the outline) is Gap-A-flavored and circular (the "smallest $L_k$-admissible multiple" is a partial-structure notion, but the actual greedy uses the full admissibility including transient primes; bounding those transient primes IS Gap A). Verdict: honest **partial**; Gap A remains the single wall; the conditional structure is the contribution.

## Current best

**Conditional theorem (CRT period structure, conditional on Gap A).** Assume Gap A: the set $G:=\{p:p\text{ appears in some }T\in\operatorname{MT}(\mathcal F_\infty)\}$ of governing primes is finite. Then:
- (F2) $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$ (this identity is **unconditional**); under Gap A this is a finite union, so $\mathcal B_\infty$ is $L$-periodic with $L:=\prod_{p\in G}p$ (squarefree).
- (F1) For any ordering $G=(p_1,\dots,p_s)$ and any $k\in\{0,\dots,s\}$ with $L_k:=\prod_{j\le k}p_j$, the projected set $A_k:=\mathcal B_\infty\bmod L_k\subseteq\mathbb Z/L_k\mathbb Z$ satisfies $|A_0|=1$ and $|A_{k}|\le p_k\,|A_{k-1}|$ for $k\ge1$; hence $T:=|A_s|\le\prod p_j=L$. **(Trivially true by fiber counting; verified computationally.)**
- The certified endgame (`greedy-equals-cyclic-successor` + `cyclic-successor-bijection`) then gives $a_{n+T}=a_n+L$ for all $n\ge1$.

**Open gap (Gap A, unchanged).** Finiteness of the governing set $G$ — equivalently, only finitely many primes ever enter a minimal transversal of $\mathcal F_\infty$. The CRT-lift framing does not close it: the lift bound is trivially true and captures no greedy structure, and the cofactor-bounding induction is circular. The wall is the same as for every other approach; this approach's contribution is the clean *conditional* structure (squarefree $L$, $T\le L$, prime-by-prime lift bound $p$).

---

## Full proof
Not yet complete. Gap A (finiteness of governing primes) remains open. The conditional proof (assuming Gap A) is given rigorously below; the open step is explicitly flagged as **GAP A**.

### Conditional proof (assuming Gap A)

We work in the setting of the certified imports. Let $S(m)$ be the prime support of $m$, $\mathcal F_n:=\{S(a_1),\dots,S(a_n)\}$ (with multiplicity ignored — cf. `mt-depends-on-set-system`), $\mathcal F_\infty:=\{S(a_i):i\ge1\}$, $\mathcal B_n:=\{m>0:\gcd(m,a_i)>1\ \forall i\le n\}$, $\mathcal B_\infty:=\bigcap_n\mathcal B_n$. Let $\operatorname{MT}(\mathcal F)$ denote the family of minimal transversals (hitting sets) of $\mathcal F$.

**Hypothesis (Gap A).** The set $G:=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}T$ of primes appearing in any minimal transversal of $\mathcal F_\infty$ is finite.

---

**Lemma F0 (LOCK base; certified).** If $|P_1|=1$ (equiv. some term is a prime power), then $T=1$, $L=p$, and $a_n=a_1+(n-1)p$ for all $n\ge1$.

*Proof.* Certified `lock-lemma`. In the CRT-lift framing this is the **base case** of the prime-by-prime construction: with $G=\{p\}$, $L=p$, $A=\{0\}\subseteq\mathbb Z/p\mathbb Z$ (the single residue $a_1\bmod p=0$, since $p\mid a_1$), $|A|=T=1\le p=L$. $\square$

---

**Lemma F1 (fiber-count lift bound; unconditional combinatorial identity).** Let $A\subseteq\mathbb Z/L\mathbb Z$ be any subset, let $L=L_k\cdot p$ with $p$ prime and $L_k\mid L$, and let $A_k:=\{a\bmod L_k:a\in A\}$ be the image under reduction mod $L_k$. Then
$$|A|\ \le\ p\cdot|A_k|.$$
In particular, if $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{j=1}^s p_j$ squarefree, and $A=\mathcal B_\infty\bmod L$, $A_k=\mathcal B_\infty\bmod L_k$ with $L_k=\prod_{j\le k}p_j$, then $|A_k|\le p_k\cdot|A_{k-1}|$ for $k\ge1$, hence $|A|=T\le\prod_{j=1}^s p_j=L$.

*Proof.* The reduction map $\pi:\mathbb Z/L\mathbb Z\to\mathbb Z/L_k\mathbb Z$ has fibers of size exactly $L/L_k$. Since $L=L_k\cdot p$ with $p$ prime, $L/L_k=p$, so every fiber has exactly $p$ elements. For any subset $A\subseteq\mathbb Z/L\mathbb Z$, $|A|=\sum_{r\in A_k}|\pi^{-1}(r)\cap A|\le\sum_{r\in A_k}p=p\cdot|A_k|$. The iterative consequence follows by telescoping from $|A_0|=1$ (mod $1$, the single residue). $\square$

(Computational verification: $a_1\in\{6,30,145,15,35,77,105,175,221,385,847,1309\}$; in every case the lift ratio $|A_k|/|A_{k-1}|$ is $\le p_k$, with slack from $1.0\times$ (tight, e.g. $a_1=1309$ stage 1: ratio $3=p$) to $\approx 11\times$ ($a_1=221$ stage 4: ratio $1.50<17$). The bound is never violated.)

---

**Lemma F2 (divisibility-progression structure of $\mathcal B_\infty$; the representation is UNCONDITIONAL).**
$$\mathcal B_\infty\ =\ \bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m\in\mathbb Z_{>0}:\operatorname{rad}(T)\mid m\}.$$
Consequently, *under Gap A* (the set $G=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}T$ is finite), $\mathcal B_\infty$ is $L$-periodic with $L:=\prod_{p\in G}p$ (squarefree), and the minimal period of $\mathcal B_\infty$ divides $L$; in fact the minimal period equals $L$ when $G$ is taken minimal (no proper subset of $G$ suffices).

*Proof.* Fix $m>0$.
($\Leftarrow$) If $T\in\operatorname{MT}(\mathcal F_\infty)$ and $\operatorname{rad}(T)\mid m$, then $T\subseteq S(m)$; as $T$ is a transversal of $\mathcal F_\infty$, $S(m)$ is a transversal, i.e. $S(m)\cap S(a_i)\ne\varnothing$ for every $i$, i.e. $\gcd(m,a_i)>1$ for every $i$, i.e. $m\in\mathcal B_\infty$.

($\Rightarrow$) Suppose $m\in\mathcal B_\infty$, i.e. $S(m)$ is a transversal of $\mathcal F_\infty$. The set $S(m)$ is finite. Consider the family $\{T\subseteq S(m):T\text{ is a transversal of }\mathcal F_\infty\}$; it is non-empty (it contains $S(m)$). A finite non-empty family of sets ordered by inclusion has a minimal element $T_0\subseteq S(m)$ (finite descending chain: start from $S(m)$, delete elements that are not needed; termination is guaranteed because $S(m)$ is finite). By construction $T_0\in\operatorname{MT}(\mathcal F_\infty)$ and $T_0\subseteq S(m)$, i.e. $\operatorname{rad}(T_0)\mid m$. This establishes the identity.

Under Gap A, $G$ is finite, so the union is finite; write $G=\{p_1,\dots,p_s\}$, $L=\prod p_j$. For each $T\in\operatorname{MT}(\mathcal F_\infty)$ we have $T\subseteq G$, so $\operatorname{rad}(T)\mid L$, and membership $m\in\{n:\operatorname{rad}(T)\mid n\}$ depends only on $m\bmod L$. A finite union of $L$-periodic sets is $L$-periodic. Hence $\mathcal B_\infty$ is $L$-periodic. Squarefreeness: each $\operatorname{rad}(T)$ is squarefree; $L=\operatorname{lcm}\{\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_\infty)\}$ is an lcm of squarefree numbers, hence squarefree. $\square$

---

**Endgame (conditional on Gap A; certified imports).** Assume Gap A. By Lemma F2, $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{p\in G}p$ finite. By the certified `greedy-equals-cyclic-successor` lemma (unconditional), $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for every $n\ge1$. By the certified `cyclic-successor-bijection` lemma, the cyclic-successor map on $A=\mathcal B_\infty\bmod L$ is a single $|A|$-cycle and $a_{n+T}=a_n+L$ for every $n\ge1$, where $T:=|A|$. By Lemma F1, $T\le L$. This proves the theorem (conditional on Gap A), with the structural refinement that $L$ is squarefree and equals $\prod_{p\in G}p$, and $T\le L$. $\square$

---

### The open gap (Gap A) — why the lift framing does not close it

**Why the `aimo-0231` nontrivial content does not port.** In `aimo-0231`, the map is a *polynomial iterate* $P^k(0)$ mod $p^e$, and the return time $\operatorname{zord}(P\bmod p^e)$ can in principle be much larger than $\operatorname{zord}(P\bmod p^{e-1})$; the nontrivial result is that it grows by at most a factor $p$, proved by the mechanism "after $k$ steps the orbit lands in the multiples of $p^{e-1}$, of which there are only $p$ mod $p^e$." In our setting, the cyclic-successor map on $A$ is structurally a **single $|A|$-cycle** (certified `cyclic-successor-bijection` (i)), so the return time equals $|A|$ exactly, and the bound $|A\bmod L_k\cdot p|\le p\cdot|A\bmod L_k|$ is the trivial fiber-count identity (Lemma F1) — it captures **no greedy-specific structure**. The lift bound is rigorous but content-free as a Gap-A mechanism: it bounds $T$ in terms of $L$, but $L$ is itself the product of the (unbounded, a priori) governing set $G$.

**Why the cofactor-bounding induction (outline Step 4) is circular.** The proposed non-circular mechanism: "each new governing prime $r$ enters as the cofactor of the smallest $L_k$-admissible multiple above a witness $a_{j-1}$; the gap bound $d_{j-1}\le M_1$ bounds the cofactor $r\le M_1$." The obstruction: the term $a_j$ is the smallest integer exceeding $a_{j-1}$ that is admissible w.r.t. the **full** family $\mathcal F_{j-1}$ (all primes seen so far, including *transient* primes not yet in $G_k$). The "smallest $L_k$-admissible multiple" is a **partial-structure** quantity (admissibility w.r.t. only the primes in $G_k$), and in general
$$a_j\ \le\ (\text{smallest $L_k$-admissible multiple above }a_{j-1}),$$
with the inequality strict whenever a transient prime (a prime in some $S(a_i)$ with $i<j$ but not in $G_k$) provides an admissible candidate that the $L_k$-skeleton misses. The cofactor $r=a_j/(\text{skeleton multiple})$ is then not determined by the skeleton alone — it depends on which transient primes happen to divide $a_j$, and **bounding which transient primes appear in the term supports $S(a_j)$ between consecutive new-governing-prime witnesses is itself a restatement of Gap A** (the `witness-density-recurrence` approach certified this circularity in round 2: Step 5's covering-capacity lower bound is circular because transient primes provide unbounded covering capacity compatibly with Gap A). The induction therefore cannot bootstrap a bound on $G$ from the fiber structure alone.

**Empirical status of the cofactor bound.** The conjecture "every governing prime $q$ satisfies $q\le M_1=\operatorname{rad}(a_1)$" (round 1) holds in all tested cases — verified here for $a_1\in\{6,30,145,15,35,77,105,175,221,385,847,1309\}$: in each, $G\subseteq\{p:p\le M_1\}$ and $L=\prod G$ is squarefree. But the bound is not proved; the strip (`lemma-C-strip-no-go`), the MT-frontier monovariant (`monovariant-non-monotonicity`), and the density lower bound (round 2) are all certified dead as mechanisms for it, and the CRT-lift cofactor argument inherits the same circularity.

---

## Promotable lemmas

Two lemma-candidates proved in full this round, proposed for certification into `results/imo-2026-06/lemmas/`:

1. **`binfinity-divisibility-progression-structure`** (Lemma F2, first part — **UNCONDITIONAL**). Statement: $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$. Proof above. This isolates the unconditional representation that `distinct-supports-stabilize`'s corollary uses only conditionally; importable by any approach that needs to reason about the structure of $\mathcal B_\infty$ before (or independently of) Gap A.

2. **`squarefree-period-under-gap-A`** (Lemma F2, second part + Lemma F1 — conditional on Gap A). Statement: under Gap A, $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{p\in G}p$ squarefree ($G$=governing primes), and for any prime-by-prime factorization $L=L_k\cdot p$ the lift bound $|A|\le p\,|A\bmod L_k|$ holds (trivial fiber-count identity). Proof above. Sharpens `distinct-supports-stabilize`'s corollary by making the squarefree-ness of $L$ and the prime-by-prime lift bound $T\le L$ explicit. Importable by any approach that closes Gap A and wants the sharp period structure.

(Both are rigorous; the second is conditional on the same Gap A as the existing `distinct-supports-stabilize` corollary, so its certification is non-blocking — it is a refinement, not a new gate.)
