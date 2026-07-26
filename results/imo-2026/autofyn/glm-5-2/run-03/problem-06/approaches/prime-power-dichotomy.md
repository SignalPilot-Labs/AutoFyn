# prime-power-dichotomy

## Status
partial

## Approaches tried
- (round 1) lock vs no-lock dichotomy — lock branch certified; no-lock mechanism (Gap C) open and the proposed "P_1-prime recurs else lock" justification is INVALID.
- (round 1, build) LOCK branch fully and rigorously proved end-to-end ($T=1, L=p$) via the "global divisibility + next multiple" argument. NO-LOCK branch: transversal framework set up, conditional endgame written, but the load-bearing finiteness of minimal-transversal primes (Gap C) left open; the reviewer-flagged invalid "else lock" mechanism removed with no replacement found. Pure-from-start (Gap B) also left as a GAP.
- (round 2) LOCK branch re-presented as a clean import of the certified `lock-lemma` (no re-proof). **Fixed C.3**: deleted the FALSE "MT is a non-increasing antichain" claim (counterexample $F=\{\{1,2\}\}$, add $\{2,3\}$, gains $\{1,3\}$); replaced by the distinct-supports-stabilize argument (increasing bounded family in a finite Boolean lattice stabilizes; MT depends only on the distinct set-system, not on multiplicities or order — proved as a lemma). **Closed Gap B unconditionally** by importing the certified `greedy-equals-cyclic-successor`; the open Gap-B marker is deleted. **Endgame** imported cleanly via `cyclic-successor-bijection` (certified). **NO-LOCK strip (Gap C)** set up with the $|S(a_i)|\ge2$ sharpening (one extra small prime for admissibility transfer); the strip's load-bearing admissibility-transfer sub-lemma is NOT re-derived here — it is the SAME `aimo-0030` minimal-criminal crux as `transversal-saturation` Step 3, and is explicitly recorded as a shared dependency on that approach's certified admissibility-transfer lemma. The $|P_1|=2$ "dropout⇒lock" lemma is valid but subsumed by the LOCK branch; the "every $P_1$-prime recurs" claim for $|P_1|\ge3$ is NOT invoked (no mechanism — explorer-3 confirmed).

## Current best
- **(LOCK branch, fully proved — certified `lock-lemma`)** If some term $a_i=p^k$ is a prime power, then $a_{n+1}=a_n+p$ for every $n\ge1$; hence $T=1,\ L=p$.
- **(Foundation, certified)** Linchpin, gap bound $d_n\le M_1$, pairwise-intersecting support family — all imported from `lemmas/linchpin-and-gap-bound.md` and `lemmas/pairwise-intersecting-supports.md`.
- **(Pure-from-start, certified — Gap B CLOSED)** `greedy-equals-cyclic-successor`: $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for every $n\ge1$, unconditionally. No transient.
- **(Endgame, certified)** `cyclic-successor-bijection`: if $\mathcal B_\infty$ is $L$-periodic, then $a_{n+T}=a_n+L$ for every $n\ge1$.
- **(Stabilization lemma, proved this round — C.3 FIXED)** Once the MT-prime set is bounded (Gap C), distinct supports form an increasing bounded family in a finite Boolean lattice ⇒ stabilize; and MT depends only on the set-system ⇒ $\operatorname{MT}(\mathcal F_n)$ stabilizes ⇒ $\mathcal B_\infty$ is $L$-periodic.
- **(NO-LOCK strip, Gap C — OPEN, conditional on a shared lemma)** The $|S(a_i)|\ge2$ anchor sharpens admissibility transfer (a second small prime for the witness to share with each $a_j$); the strip's size bound, contradiction, and the admissibility-transfer sub-lemma are the SAME `aimo-0030` crux as `transversal-saturation` Step 3. The admissibility-transfer sub-lemma is **not proved here**; the approach is CONDITIONAL on its certification in `transversal-saturation`.

## Full proof

Notation. For an integer $m>1$ write $S(m)=\{$prime divisors of $m\}$ for its prime support, and write $P_1:=S(a_1)$, $M_1:=\prod_{p\in P_1}p=\operatorname{rad}(a_1)$. Call an integer $m>a_n$ **admissible at step $n$** if $\gcd(m,a_i)>1$ for every $i\le n$; the defining rule is $a_{n+1}=\min\{m>a_n:m\text{ admissible at step }n\}$.

The claim is the dichotomy **(LOCK)** some $a_i$ is a prime power, or **(NO-LOCK)** no $a_i$ is a prime power. The dichotomy is exhaustive.

---

### A. Foundation (certified; imported)

We import the following reviewer-certified lemmas verbatim (see `results/imo-2026-06/lemmas/`); they are not re-proved here.

**Lemma (Linchpin and gap bound)** [`lemmas/linchpin-and-gap-bound.md`]. *For every $n\ge1$, $a_n$ is divisible by some prime $p\in P_1$; and $d_n:=a_{n+1}-a_n\le M_1$ for every $n\ge1$.*

**Lemma (Pairwise-intersecting support family)** [`lemmas/pairwise-intersecting-supports.md`]. *$S(a_i)\cap S(a_j)\ne\emptyset$ for all $i,j$.*

**Lemma (Every term lies in $\mathcal B_\infty$)** [`lemmas/every-term-in-binfinity.md`]. *With $\mathcal B_n=\{m:S(m)\text{ meets every }S(a_i),\,i\le n\}$ and $\mathcal B_\infty:=\bigcap_n\mathcal B_n$, we have $a_k\in\mathcal B_\infty$ for every $k\ge1$.*

---

### B. LOCK branch (certified; imported)

**Lemma LOCK** [`lemmas/lock-lemma.md`, reviewer-certified]. *If some term $a_i=p^k$ is a prime power ($p$ prime, $k\ge1$), then $a_{n+1}=a_n+p$ for every $n\ge1$; equivalently $a_n=a_1+(n-1)p$ for all $n\ge1$. Consequently the required constants are $T=1,\ L=p$.*

*Proof sketch (full proof in `lemmas/lock-lemma.md`).* $a_i=p^k$ admissible against $a_1$ forces $p\mid a_1$; $a_i$ admissible against each earlier $a_j$ forces $p\mid a_j$ (the only prime of $a_i$ is $p$); every later $a_j$ is admissible against $a_i$ so $p\mid a_j$. Hence every term is a $p$-multiple; the lower bound $a_{n+1}\ge a_n+p$ (two $p$-multiples) and the upper bound $a_{n+1}\le a_n+p$ (every $p$-multiple is admissible) together give $a_{n+1}=a_n+p$ from $n=1$. ∎

**Coverage.** The LOCK branch covers, in particular: $a_1$ even (a power of $2$ is reached along $a_n=a_1+2(n-1)$, then LOCK); $a_1=p$ or $a_1=p^k$ (LOCK at once); $a_1$ divisible by an odd prime $p$ for which a power of $p$ is reached (LOCK).

---

### C. NO-LOCK branch: setup and conditional endgame

Assume henceforth that **no** $a_i$ is a prime power. Then $|S(a_i)|\ge2$ for every $i$; in particular $|P_1|=|S(a_1)|\ge2$ (since $a_1$ is not a prime power).

#### C.1 Transversal reformulation (standard)

Define the family of prime supports $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$ and the admissible set
$$\mathcal B_n=\{m>1:S(m)\text{ intersects every member of }\mathcal F_n\}.$$
A set $T$ of primes intersecting every $S(a_i)$ is a **transversal** of $\mathcal F_n$; it is **minimal** (an element of $\operatorname{MT}(\mathcal F_n)$) if no proper subset of $T$ is a transversal. Then
$$\mathcal B_n=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{m>1:\operatorname{rad}(T)\mid m\},\qquad \operatorname{rad}(T)=\prod_{p\in T}p.$$
*Justification.* "$\subseteq$": if $S(m)$ hits every $S(a_i)$ then $S(m)$ is a transversal; extend it to a *minimal* transversal $T\subseteq S(m)$, so $\operatorname{rad}(T)\mid m$. "$\supseteq$": if $\operatorname{rad}(T)\mid m$ for a transversal $T$ then $T\subseteq S(m)$, so $S(m)$ hits every $S(a_i)$. ∎

So $\mathcal B_n$ is a finite union of arithmetic progressions, and the greedy rule reads $a_{n+1}=\min(\mathcal B_n\cap(a_n,\infty))$.

**Lemma ($P_1$ is always a transversal).** *$P_1$ is a transversal of $\mathcal F_n$ for every $n$ (not necessarily minimal).*

*Proof.* By the linchpin, $S(a_i)\cap P_1\ne\emptyset$ for every $i$; i.e. $P_1$ meets every member of $\mathcal F_n$. ∎

So a transversal of size $\le|P_1|$ always exists; but minimal transversals may contain primes outside $P_1$.

#### C.2 GAP C — finiteness of minimal-transversal primes (the open wall)

**Conjecture (Gap C).** *In the NO-LOCK regime, the set*
$$\mathcal Q_\infty:=\bigcup_{n\ge1}\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}T$$
*of primes that ever enter a minimal transversal is finite (and, conjecturally, contained in $\{p:p\le M_1\}$).*

**Status: OPEN.** The reviewer correctly flagged the originally proposed mechanism as invalid. The invalid argument was: *"every $P_1$-prime recurs (else the terms avoiding it shrink to a singleton support $\Rightarrow$ lock)."* It fails because a $P_1$-prime $p$ can drop out without forcing a lock: future terms may hit $a_1$ via other $P_1$-primes, carrying a second prime $q\notin P_1$ to keep $|S|\ge2$. This is possible already for $|P_1|=2$ (terms of the form $p'\cdot q$ with $q\notin P_1$), so the "else lock" step has no valid justification.

**What is NOT invoked.**
- The "every $P_1$-prime recurs" claim is NOT used for $|P_1|\ge3$: explorer-3 confirmed there is no proof mechanism (a $P_1$-prime can go silent for hundreds of terms without forcing a lock; $a_1=2085$: prime $139$ silent for $\sim180$ terms, no lock through $6000$ terms).
- The "$|P_1|=2$ dropout$\Rightarrow$lock" lemma IS a theorem (if $p_{\rm lg}$ never recurs, every term is a $p_{\rm sm}$-multiple $\Rightarrow$ lock at $L=p_{\rm sm}$), but it is **subsumed by the LOCK branch** and gives no NO-LOCK progress.

**What the size-$\ge2$ hypothesis DOES give** is the following structural observation (recorded for use in the strip in C.4):

**Lemma (private-set structure, no-lock).** *Let $T\in\operatorname{MT}(\mathcal F_n)$ and $t\in T$. By minimality of $T$ there is a set $F\in\mathcal F_n$ with $F\cap T=\{t\}$ (a private set of $t$). In the NO-LOCK regime $|F|\ge2$, so $F$ contains a prime $t'\ne t$ with $t'\notin T$. If moreover $t\notin P_1$, then the linchpin forces $F\cap P_1\ne\emptyset$, and since $F\cap T=\{t\}$ with $t\notin P_1$, one has $F\cap P_1\subseteq P_1\setminus T$. So every large (non-$P_1$) prime $t$ in a minimal transversal is witnessed by a term whose $P_1$-part sits inside $P_1\setminus T$, a subset of the fixed finite set $P_1$.*

*Proof.* Every clause is definitional except the linchpin invocation. ∎

This bounds the *type* of a large transversal prime by a subset of $P_1$ (finitely many types); bounding the *number* of large primes per type is the wall.

#### C.3 Stabilization lemma (the C.3 fix) — PROVED

The round-1 file claimed "$\operatorname{MT}(\mathcal F_n)$ is a non-increasing antichain; adding a set can only remove elements." **This is FALSE.** Counterexample: $F=\{\{1,2\}\}$ has $\operatorname{MT}(F)=\{\{1\},\{2\}\}$; add $\{2,3\}$, and $\operatorname{MT}=\{\{1,3\},\{2\}\}$ — the new minimal transversal $\{1,3\}$ is *created*. (Recorded in the round-1 per-role rule.) The conclusion (stabilization once Gap C holds) is still correct, but via a different argument, which we now give rigorously.

**Lemma (MT depends only on the set-system).** *Let $\mathcal F,\mathcal F'$ be two finite families of sets. If $\mathcal F$ and $\mathcal F'$ have the same distinct member-sets (i.e. they are equal as set-systems, ignoring multiplicities and ordering), then $\operatorname{MT}(\mathcal F)=\operatorname{MT}(\mathcal F')$.*

*Proof.* A transversal of $\mathcal F$ is a set $T$ with $T\cap F\ne\emptyset$ for every $F\in\mathcal F$. Whether $T\cap F\ne\emptyset$ depends only on the set $F$, not on any multiplicity or position of $F$ in a list. Hence the family of transversals of $\mathcal F$ depends only on the set-system $\{F:F\in\mathcal F\}$ (the collection of distinct members). Minimality ("no proper subset is a transversal") is a property of the transversal family, so it too depends only on the set-system. Thus $\operatorname{MT}$ depends only on the distinct member-sets. ∎

**Lemma (distinct-supports-stabilize).** *Assume Gap C: there is a finite bound $B$ with $\mathcal Q_\infty\subseteq\{p\text{ prime}:p\le B\}$. Then there exists $N_0$ such that for all $n\ge N_0$, $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$, where $\mathcal F_\infty:=\{S(a_i):i\ge1\}$.*

*Proof.* Consider the sequence of distinct-support set-systems
$$\mathcal D_n:=\{S(a_i):1\le i\le n\}\subseteq 2^{\{p\le B\}}.$$
Each $\mathcal D_n$ is a subset of the finite power set $2^{\{p\le B\}}$ (which has $\le 2^{\pi(B)}$ elements, finite by the bound on $\mathcal Q_\infty$ — note every prime in every $S(a_i)$ is in $\mathcal Q_\infty\cup P_1\subseteq\{p\le B\}$, since $P_1\subseteq\mathcal Q_\infty$ as $P_1$ is itself a transversal member, or simply enlarge $B$ to include $P_1$). The sequence $(\mathcal D_n)$ is **increasing** ($\mathcal D_n\subseteq\mathcal D_{n+1}$, since adding a term only adds its support to the set-system). An increasing sequence in a finite poset stabilizes: there is $N_0$ with $\mathcal D_n=\mathcal D_{N_0}=:\mathcal D_\infty$ for all $n\ge N_0$.

By the previous lemma, $\operatorname{MT}(\mathcal F_n)$ depends only on $\mathcal D_n$ (the distinct member-sets of $\mathcal F_n$). Hence $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal D_n)$; for $n\ge N_0$ this equals $\operatorname{MT}(\mathcal D_\infty)=\operatorname{MT}(\mathcal F_\infty)$. ∎

**Corollary ($\mathcal B_\infty$ is $L$-periodic, conditional on Gap C).** *Assume Gap C. Let $G:=\mathcal Q_\infty\cup P_1$ (finite), and $L:=\prod_{p\in G}p$. Then $\mathcal B_\infty$ is $L$-periodic: $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$.*

*Proof.* By the stabilization lemma, for $n\ge N_0$ we have $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$, a fixed finite family of minimal transversals $T_1,\dots,T_s\subseteq G$. Thus
$$\mathcal B_\infty=\mathcal B_{N_0}=\bigcup_{j=1}^s\{m:\operatorname{rad}(T_j)\mid m\}.$$
Membership $m\in\mathcal B_\infty$ depends only on which primes of $G$ divide $m$, i.e. only on $m\bmod L$ (since $L=\prod_{p\in G}p$ and divisibility by each $p\in G$ is determined by $m\bmod L$). Hence $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$. ∎

#### C.4 The NO-LOCK strip (Gap C) — the shared `aimo-0030` crux

Gap C — equivalently the bound $\mathcal Q_\infty\subseteq\{p\le M_1\}$ — is the **single open wall** of this approach. We set up the strip cleanly and record its dependency on a shared lemma.

**Setup.** Suppose, for contradiction, that some prime $q>M_1$ enters a minimal transversal of $\mathcal F_n$ for some $n$. Take $q$ minimal with this property (the **minimal criminal**). By the private-set structure lemma (C.2), $q$ is private to some witness term $a_i$: there is $T\in\operatorname{MT}(\mathcal F_n)$ with $q\in T$ and $S(a_i)\cap T=\{q\}$. By the linchpin $S(a_i)\cap P_1\ne\emptyset$; since $q>M_1\ge\max P_1$ and $q\in T$, the $P_1$-prime $p\in S(a_i)\cap P_1$ lies in $P_1\setminus T$ (it cannot be $q$, and it cannot be in $T$ since $S(a_i)\cap T=\{q\}$). So the witness $a_i$ carries a small $P_1$-prime $p\le M_1<q$ outside $T$.

**The $|S(a_i)|\ge2$ sharpening.** In the NO-LOCK regime every $|S(a_i)|\ge2$. So besides $q$ (and possibly besides $p$), the witness $a_i$ carries at least one further prime, giving the strip an extra small prime available for admissibility transfer. Concretely: among the prime divisors of $a_i$ other than $q$, at least one lies in $P_1$ (the linchpin prime $p$ above); and because $|S(a_i)|\ge2$, the witness has a divisor outside $\{q\}$. This is a genuine minor strengthening over the bare strip (more small primes available to share with each $a_j$, $j<i$), but it does NOT by itself close the load-bearing sub-lemma.

**The strip (size bound, admissibility transfer, contradiction).** Let $A:=\prod_{r\mid a_i,\,r\le M_1}r$ (the small radical of $a_i$) and pick $p\in P_1\cap S(a_i)$; let $k$ be the least integer $\ge0$ with $x:=p^k\cdot A>a_{i-1}$.

- *Size bound.* $A\mid (a_i/q)$ (the small radical divides the small part of $a_i$, since $a_i=q\cdot(a_i/q)$ and every prime $\le M_1$ dividing $a_i$ divides $a_i/q$ — it cannot be $q$ as $q>M_1$). Replacing the large factor $q>M_1\ge\prod_{r\le M_1,\,r\mid a_i}r\ge A$ by the least power $p^k$ of a small prime just large enough to clear $a_{i-1}$ yields $x<a_i$ once $q$ exceeds the small-prime product — this is the `aimo-0030` "comparison of products of distinct prime factors" move.
- *Admissibility transfer (LOAD-BEARING, SHARED, NOT RE-PROVED HERE).* One must show $x$ is admissible against $\mathcal F_{i-1}$: for each $j<i$, $a_i$ shares some prime $r_j$ with $a_j$ (pairwise intersection); if $r_j\le M_1$ then $r_j\mid A\mid x$, so $x$ hits $a_j$. The obstruction: some $a_j$ might share ONLY $q$ with $a_i$. To rule this out one uses that $T\setminus\{q\}$ is a transversal of $\mathcal F_{i-1}$ (since $q$ is private to $a_i$) and the greedy coupling ($d_n\le M_1$, every term in $\mathcal B_\infty$, cyclic-successor structure from `greedy-equals-cyclic-successor`) to force the shared primes into the small regime.
- *Contradiction.* $x$ admissible, $a_{i-1}<x\le a_i$, and $x\ne a_i$ ( $x$ has only primes $\le M_1$, $a_i$ has $q>M_1$). Greedy minimality gives $a_i\le x$, contradicting $x<a_i$.

**Dependency declaration.** The size-bound, admissibility-transfer, and contradiction steps above are the **SAME `aimo-0030` minimal-criminal crux** that `transversal-saturation` Step 3 carries (the outliner and reviewer both flag this duplication explicitly). This approach's value-add is the LOCK/NO-LOCK dichotomy plus the $|S(a_i)|\ge2$ sharpening (one extra small prime for admissibility transfer), NOT a second independent copy of the strip. **The admissibility-transfer sub-lemma is NOT proved in this file.** The approach is therefore CONDITIONAL on the certification of the admissibility-transfer lemma in `transversal-saturation`; once that lemma is certified in `results/imo-2026-06/lemmas/`, it is to be imported here in lieu of C.4's load-bearing step. Until then, C.4 is an **open gap**, and the approach is `partial`.

---

### D. Endgame (certified; imported)

**Lemma (greedy $=$ cyclic successor in $\mathcal B_\infty$ from $n=1$)** [`lemmas/greedy-equals-cyclic-successor.md`, reviewer-certified]. *For every $n\ge1$, $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$. Unconditional — does NOT require $\mathcal B_\infty$ to be periodic.*

This **closes Gap B (pure-from-start) unconditionally**: there is no transient; once $\mathcal B_\infty$ is $L$-periodic, the sequence is the orbit of $a_1$ under the cyclic-successor map from $n=1$. The round-1 open Gap-B marker is deleted.

**Lemma (cyclic-successor bijection)** [`lemmas/cyclic-successor-bijection.md`, reviewer-certified]. *If $\mathcal B_\infty$ is $L$-periodic for some finite $L$, set $A:=\{r\in\mathbb Z/L\mathbb Z:r\text{ lies in }\mathcal B_\infty\}$. The cyclic successor $f:A\to A$ is a bijection, a single $|A|$-cycle. Consequently, with $T:=|A|$, $a_{n+T}=a_n+L$ for every $n\ge1$.*

**Assembly of the NO-LOCK branch (conditional on Gap C).** Assume Gap C. By the stabilization lemma (C.3), $\mathcal B_\infty$ is $L$-periodic. By `greedy-equals-cyclic-successor`, the greedy rule is the cyclic successor in $\mathcal B_\infty$ from $n=1$. By `cyclic-successor-bijection`, $a_{n+T}=a_n+L$ for every $n\ge1$. ∎ (conditional on Gap C)

---

### E. Summary

The dichotomy is exhaustive.

- **LOCK branch — SOLVED.** If some $a_i=p^k$ is a prime power, the certified `lock-lemma` gives $a_{n+1}=a_n+p$ for every $n\ge1$, so $T=1,\ L=p$. Complete and rigorous.

- **NO-LOCK branch — CONDITIONAL on Gap C.** Setup (C.1), the C.3 stabilization lemma (distinct-supports-stabilize, replacing the false MT-monotonicity), the Gap-B closure (imported `greedy-equals-cyclic-successor`), and the endgame (imported `cyclic-successor-bijection`) are all rigorous. The single open wall is **Gap C** (finiteness of minimal-transversal primes, equivalently $\mathcal Q_\infty\subseteq\{p\le M_1\}$). The strip set up in C.4 is the shared `aimo-0030` minimal-criminal crux (same as `transversal-saturation` Step 3), sharpened by the $|S(a_i)|\ge2$ anchor; its load-bearing admissibility-transfer sub-lemma is NOT re-proved here and the approach is **conditional on its certification in `transversal-saturation`**.

The approach therefore yields a complete proof in the LOCK regime and a complete conditional proof in the NO-LOCK regime, modulo the shared admissibility-transfer lemma.

## Promotable lemmas

- **Lemma (MT depends only on the set-system)** (proved in C.3 above): *if $\mathcal F,\mathcal F'$ have the same distinct member-sets, then $\operatorname{MT}(\mathcal F)=\operatorname{MT}(\mathcal F')$*. Standard fact, fully proved; useful for any approach that needs to deduce MT-stabilization from set-system stabilization.
- **Lemma (distinct-supports-stabilize)** (proved in C.3 above): *once the MT-prime set is bounded by $B$, the distinct-support set-systems $\mathcal D_n\subseteq 2^{\{p\le B\}}$ form an increasing bounded family, hence stabilize at some $N_0$; by the set-system lemma, $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$ for $n\ge N_0$*. This is the rigorous replacement for the false "MT is non-increasing" claim; importable by any approach that closes Gap A/C and needs to deduce $\mathcal B_\infty$ is $L$-periodic.
- **Lemma (private-set structure, no-lock)** (proved in C.2 above): every large prime $t$ in a minimal transversal is witnessed by a term whose $P_1$-part lies in $P_1\setminus T$.
- (Re-promoted, certified elsewhere: `lock-lemma`, `greedy-equals-cyclic-successor`, `cyclic-successor-bijection`, `linchpin-and-gap-bound`, `pairwise-intersecting-supports`, `every-term-in-binfinity` — all imported, not re-proved.)
