# transversal-saturation

## Status
partial

## Approaches tried
- (round 1) canonical antichain-monovariant route — outline seeded; gaps A and B open.
- (round 1, build) Rigorously closed Gap B (pure-from-start): proved the family $\mathcal F_\infty$ is pairwise-intersecting, hence every term lies in $\mathcal B_\infty$, hence the greedy rule *is* the cyclic-successor map of $\mathcal B_\infty$ from $n=1$ — no transient, unconditionally. Once $\mathcal B_\infty$ is $L$-periodic (Gap A), the cyclic-successor bijection gives $a_{n+T}=a_n+L$ for all $n\ge1$. Fully solved the prime-power / even-$a_1$ (lock) sub-case as a complete proof. Gap A (finiteness of governing primes) remains the single open wall.
- (round 2, build) Attempted the `aimo-0030` minimal-criminal prime-factor strip to close Gap A. **Two rigorous positive results obtained** (Lemma A: $a_i$ is the smallest multiple of $q$ above $a_{i-1}$; and "$a_{i-1}$ shares a small prime with $a_i$" via the gap argument). **However the strip's two load-bearing steps — the size bound $x<a_i$ and the admissibility transfer — are not merely unproven; they are empirically REFUTED in analogous small-prime cases** (governing prime $q=19$ of $a_1=385$, and $q=11$ of $a_1=77$): the obstruction "$a_j$ shares ONLY $q$ with $a_i$" genuinely occurs for smallest-index private witnesses, and a structural no-go shows the "smallest-multiple-of-$A$" strip is either vacuous ($x=a_i$) or yields inadmissible candidates. The `$p^kA$` strip blows up exponentially (size fails). Corrected Step 7's factual errors ($385$ IS periodic, $L=43890$; governing vs transient primes properly distinguished). Gap A remains open; the strip as formulated is a dead end and future rounds need a different mechanism for the taming step.

## Current best
**Whole theorem reduced to a single wall (Gap A).** Every step of the proof is rigorous except the assertion that $\mathcal B_\infty$ is $L$-periodic for some finite $L$ — equivalently, that only finitely many primes ever enter a minimal transversal of $\mathcal F_\infty$. The endgame (cyclic-successor bijection $\Rightarrow$ pure periodicity), the pure-from-start reduction, and the LOCK sub-case are complete and certified. Round 2 added two rigorous lemmas toward the `aimo-0030` strip (Lemma A and the $a_{i-1}$ small-shared-prime lemma) but also produced a **rigorous no-go result** showing the "smallest-multiple-of-$A$" version of the strip cannot close the gap, plus computational evidence that the obstruction underlying admissibility transfer is real (not merely unproven). The strip approach as currently formulated is a dead end; the open gap is now better understood (it is a real structural obstruction, not a missing detail).

## Full proof

### Notation and reformulation

Let $S(x)$ denote the set of prime divisors of $x$, and $P_1:=S(a_1)\subseteq\{p\text{ prime}\}$. For $n\ge1$ write
$$\mathcal F_n:=\{S(a_1),\dots,S(a_n)\},\qquad \mathcal B_n:=\{m\in\mathbb Z_{>0}:\; S(m)\text{ meets every }S(a_i),\, i\le n\}.$$
Equivalently $m\in\mathcal B_n\iff\gcd(m,a_i)>1\ \forall i\le n$. The greedy rule is
$$a_{n+1}=\min\bigl(\mathcal B_n\cap(a_n,\infty)\bigr).$$
A *transversal* (hitting set) of $\mathcal F_n$ is a set $T$ of primes with $T\cap S(a_i)\ne\varnothing$ for all $i\le n$; a *minimal transversal* is one no proper subset of which is a transversal. Write $\operatorname{MT}(\mathcal F_n)$ for the family of minimal transversals. As $\operatorname{rad}(T)=\prod_{p\in T}p$,
$$\mathcal B_n=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{m:\operatorname{rad}(T)\mid m\},$$
a finite union of divisibility classes. Finally set $\mathcal B_\infty:=\bigcap_{n\ge1}\mathcal B_n$, the admissible set against the whole sequence.

### Step 1 — Linchpin: every term is divisible by some prime of $a_1$

**Lemma 1.** For every $n\ge1$ there exists $p\in P_1$ with $p\mid a_n$.

*Proof.* The defining condition for $a_n$ ($n\ge2$) includes $i=1$, so $\gcd(a_n,a_1)>1$; hence some prime of $a_1$ divides $a_n$. For $n=1$ this is tautological. ∎

**Corollary (gap bound).** $d_n:=a_{n+1}-a_n\le M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$ for every $n$.

*Proof.* By Lemma 1, every $a_i$ ($i\le n$) is divisible by some $p\in P_1$; hence $M_1=\prod_{p\in P_1}p$ is itself a transversal of $\mathcal F_n$. So every multiple of $M_1$ lies in $\mathcal B_n$. The smallest multiple of $M_1$ strictly greater than $a_n$ is at most $a_n+M_1$, and it is admissible; greedy minimality gives $a_{n+1}\le a_n+M_1$. ∎

In particular $a_n$ grows at most linearly: $a_n\le a_1+(n-1)M_1$. *(Certified: `lemmas/linchpin-and-gap-bound.md`.)*

### Step 2 — $\mathcal F_\infty$ is pairwise intersecting

**Lemma 2 (pairwise intersecting).** For all $i\ne j$, $S(a_i)\cap S(a_j)\ne\varnothing$.

*Proof.* By induction on $\max(i,j)$. For the pair $(a_{n+1},a_i)$ with $i\le n$: by construction $a_{n+1}$ was chosen to satisfy $\gcd(a_{n+1},a_i)>1$, i.e. $S(a_{n+1})\cap S(a_i)\ne\varnothing$. Inductively all earlier pairs already intersect. Hence every pair intersects. ∎ *(Certified: `lemmas/pairwise-intersecting-supports.md`.)*

### Step 3 — Every term lies in $\mathcal B_\infty$ (the key reduction)

**Lemma 3.** For every $k\ge1$, $a_k\in\mathcal B_\infty$.

*Proof.* $\mathcal B_\infty=\{m:S(m)\text{ meets every }S(a_i),\,i\ge1\}$. Fix $k$. For $i\ne k$, Lemma 2 gives $S(a_k)\cap S(a_i)\ne\varnothing$. For $i=k$, $S(a_k)\cap S(a_i)=S(a_k)\ne\varnothing$ since $a_k>1$. Thus $S(a_k)$ meets every $S(a_i)$, i.e. $a_k\in\mathcal B_\infty$. ∎ *(Certified: `lemmas/every-term-in-binfinity.md`.)*

### Step 4 — The greedy rule *is* the cyclic-successor map of $\mathcal B_\infty$ from the start

**Lemma 4 (greedy $=$ cyclic successor in $\mathcal B_\infty$).** For every $n\ge1$,
$$a_{n+1}=\min\bigl(\mathcal B_\infty\cap(a_n,\infty)\bigr).$$

*Proof.* Since $\mathcal B_{n+1}\subseteq\mathcal B_n$ (more constraints), the family $(\mathcal B_n)$ is decreasing, so $\mathcal B_\infty=\bigcap_n\mathcal B_n\subseteq\mathcal B_n$. Hence $\mathcal B_\infty\cap(a_n,\infty)\subseteq\mathcal B_n\cap(a_n,\infty)$, giving
$$\min(\mathcal B_\infty\cap(a_n,\infty))\;\ge\;\min(\mathcal B_n\cap(a_n,\infty))=a_{n+1}.$$
By Lemma 3, $a_{n+1}\in\mathcal B_\infty$, and clearly $a_{n+1}>a_n$. So $a_{n+1}\in\mathcal B_\infty\cap(a_n,\infty)$, whence $a_{n+1}\ge\min(\mathcal B_\infty\cap(a_n,\infty))$. Combining the two inequalities yields equality. ∎ *(Certified: `lemmas/greedy-equals-cyclic-successor.md`.)*

**Remark.** Lemma 4 is unconditional — it does **not** require Gap A. It shows the sequence is the orbit of $a_1$ under the "cyclic successor in $\mathcal B_\infty$" dynamical system, starting at $n=1$. The only remaining question is whether $\mathcal B_\infty$ has enough periodic structure for this orbit to be eventually (hence, by Lemma 4, from the start) periodic.

### Step 5 — The cyclic-successor bijection (conditional on Gap A)

**Gap A (the wall).** *There exist a finite set of primes $G$ and a finite modulus $L$ such that $\mathcal B_\infty$ is $L$-periodic* (i.e. $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$). *Equivalently (see Step 6 below), the set of primes that enter some minimal transversal of $\mathcal F_\infty$ is finite.*

We record this as the single unproved assertion of the approach. Partial progress and the obstruction to naive bounds are in Step 7.

**Assuming Gap A**, let $L$ be a period and set
$$A:=\{r\in\mathbb Z/L\mathbb Z:\;\text{the residue class }r\text{ lies in }\mathcal B_\infty\}\subseteq\mathbb Z/L\mathbb Z.$$
$A\ne\varnothing$ because $a_1\bmod L\in A$ (Lemma 3). The *cyclic successor* $f:A\to A$ is $f(r):=$ the smallest element of $A$ strictly after $r$ on the circle $\mathbb Z/L\mathbb Z$ (wrapping through $0$).

**Lemma 5 (cyclic successor is a single cycle).** $f$ is a bijection of $A$; in fact $f$ is one cycle of length $|A|$.

*Proof.* The *cyclic predecessor* $g(r):=$ the element of $A$ strictly before $r$ on the circle is a well-defined two-sided inverse of $f$ (for $|A|=1$ both are the identity; for $|A|\ge2$ this is immediate from the cyclic order). Hence $f$ is a bijection. Moreover, starting at any $r$ and iterating $f$ walks once around the circle through *all* of $A$, returning to $r$ after exactly $|A|$ steps: $f$ is a single $|A|$-cycle. ∎

**Lemma 6 (per-period increment $=L$).** Let $T:=|A|$ and let $r_1:=a_1\bmod L\in A$, $r_{k+1}:=f(r_k)$. Then $a_{n+T}=a_n+L$ for every $n\ge1$.

*Proof.* By Lemma 4, $a_{n+1}$ is the smallest element of $\mathcal B_\infty$ strictly greater than $a_n$. By $L$-periodicity this depends only on $r_n=a_n\bmod L$: the increment $d_n:=a_{n+1}-a_n$ is the cyclic gap from $r_n$ to $f(r_n)$ on the circle, i.e.
$$d_n=\begin{cases}f(r_n)-r_n & \text{if }f(r_n)>r_n,\\ L-r_n+f(r_n) & \text{if }f(r_n)\le r_n\;\text{(wrap)}.\end{cases}$$
Summing over one full period $n,n+1,\dots,n+T-1$, the orbit traverses every point of $A$ once (Lemma 5), so the sum of cyclic gaps is exactly the circumference $L$. Thus $\sum_{k=0}^{T-1}d_{n+k}=L$, i.e. $a_{n+T}-a_n=L$. This holds for *every* $n\ge1$ (not just eventually), because the orbit is a single cycle with no tail and the dynamics runs on $\mathcal B_\infty$ from $n=1$ (Lemma 4). ∎ *(Lemmas 5–6 certified: `lemmas/cyclic-successor-bijection.md`.)*

Lemma 6 is the conclusion of the theorem (with $T=|A|$, $L=$ the period), conditional on Gap A. So:

> **The entire theorem is reduced to Gap A.**

### Step 6 — Equivalence of the two forms of Gap A

We asserted that "$\mathcal B_\infty$ is $L$-periodic for some finite $L$" is equivalent to "only finitely many primes enter a minimal transversal of $\mathcal F_\infty$." Justification:

*($\Leftarrow$)* Suppose the primes entering minimal transversals of $\mathcal F_\infty$ lie in a finite set $G$. Then every minimal transversal $T\subseteq G$; there are only finely many such $T$, so finitely many minimal transversals $T_1,\dots,T_s$. Set $L:=\operatorname{lcm}(\operatorname{rad}(T_1),\dots,\operatorname{rad}(T_s))=\prod_{p\in G}p$. Then $\mathcal B_\infty=\bigcup_j\{m:\operatorname{rad}(T_j)\mid m\}$, and membership $m\in\mathcal B_\infty$ depends only on which primes of $G$ divide $m$, i.e. only on $m\bmod L$. So $\mathcal B_\infty$ is $L$-periodic.

*($\Rightarrow$)* If $\mathcal B_\infty$ is $L$-periodic, take $G:=\{p\text{ prime}:p\mid L\}$ (finite). Suppose $q\notin G$ enters a minimal transversal $T$ of $\mathcal F_\infty$. By minimality of $T$, the prime $q$ has a *private* witness: there is $a_i$ with $S(a_i)\cap T=\{q\}$ (standard characterization of minimal transversals: every element is private). Now $\operatorname{rad}(T)\mid m\Rightarrow m\in\mathcal B_\infty$ for every multiple $m$ of $\operatorname{rad}(T)$; in particular every multiple of $\operatorname{rad}(T)$ shares the prime $q$ with $a_i$. But $q\nmid L$, so $L$-periodicity forces: $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$. Take $m$ a large multiple of $\operatorname{rad}(T)$ chosen with $m+L$ *not* divisible by $q$ (possible since $q\nmid L$: multiples of $\operatorname{rad}(T)$ occur in every residue class mod $q$ that is $0\bmod q$; shifting by $L\not\equiv0\bmod q$ moves off the $0\bmod q$ class). Then $m\in\mathcal B_\infty$ but $m+L$ is not divisible by $q$, so $S(a_i)\cap S(m+L)\subseteq S(a_i)\cap(\text{primes of }m+L)$; since $T\setminus\{q\}$ misses $S(a_i)$ and the only $T$-prime hitting $S(a_i)$ was $q\not\mid(m+L)$, we get $S(a_i)\cap S(m+L)=\varnothing$ once $m+L$ is chosen coprime to all primes of $S(a_i)\setminus\{q\}$ too — arrange this simultaneously for the finitely many primes of $S(a_i)\setminus\{q\}$ by CRT, since none of them divides $L$ unless they lie in $G$; for those in $G$ we instead pick $m$ with $m+L$ avoiding them, again possible by CRT. Hence $m+L\notin\mathcal B_\infty$, contradicting $L$-periodicity. Thus no prime $q\notin G$ enters a minimal transversal. ∎

(The CRT arrangement above is the standard "shift a witness off its private prime" trick; it shows $L$-periodicity forces every governing prime to divide $L$.)

### Step 7 — The minimal-criminal strip: setup, two rigorous lemmas, and a no-go

We collect what *can* be proved unconditionally toward Gap A, then record (honestly) where the `aimo-0030`-style strip stalls.

**Step 7.0 — Factual corrections to the round-1 narrative.** The round-1 writeup asserted "$a_1=385$ is aperiodic through 12000 terms" and "the naive bound $q\le M_1=\operatorname{rad}(a_1)$ is refuted." **Both assertions are FALSE and are retracted.** Verified computationally (Bash, round 2): for $a_1=385=5\cdot7\cdot11$, $M_1=385$, the sequence is periodic **from $n=1$** with $T=5088$, $L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$; all primes of $L$ (the *governing* primes) are $\le M_1=385$. Across $80+$ tested starting values ($385, 77, 715, 1309, 2431, 741, 145, 2085, 91, 143, 1001, \dots$), every governing prime $q$ (a prime divisor of $L$) satisfies $q\le M_1$.

**Governing vs transient primes (definition, no circularity).** A prime $q$ is *governing* iff $q$ divides $L$, equivalently (by Step 6) $q$ enters some $T\in\operatorname{MT}(\mathcal F_\infty)$ (a minimal transversal of the *limit* family). A prime is *transient* iff it appears in $\bigcup\operatorname{MT}(\mathcal F_n)$ for some finite $n$ but drops out of the limit (not governing). Transient primes can be large — e.g. $a_1=2085$ has term-primes up to $2621$ at finite stages (reviewer finding), and $a_1=145$ has transient primes up to $97$. The target bound $q\le M_1$ is on the **governing** set only; it is meaningless (and false) for transient primes. This distinction was missing from the round-1 narrative.

**Lemma 7.** $P_1$ is a transversal of $\mathcal F_n$ for every $n$. Hence for every $n$ there is a minimal transversal $T_0\subseteq P_1$; in particular a minimal transversal using only primes $\le Q:=\max P_1\le M_1$ exists at every stage.

*Proof.* Lemma 1: every $a_i$ is divisible by some $p\in P_1$, so $P_1$ hits every $S(a_i)$. A minimal transversal contained in the transversal $P_1$ exists by discarding redundant elements. ∎

**Lemma 8.** Every minimal transversal $T$ of $\mathcal F_\infty$ (or of any $\mathcal F_n$) satisfies $T\cap P_1\ne\varnothing$.

*Proof.* $T$ must hit $S(a_1)=P_1$. ∎

---

**The `aimo-0030` minimal-criminal strip (setup).** We attempt to close Gap A by contradiction:

> **Hypothesis (minimal criminal).** Suppose $q>M_1$ is a *governing* prime — the smallest such. Then $q$ enters some $T\in\operatorname{MT}(\mathcal F_\infty)$; by the private-element characterization of minimal transversals (Step 6), $q$ is *private* to some $a_i$: $S(a_i)\cap T=\{q\}$, i.e. $q\mid a_i$ and no other $T$-prime divides $a_i$. Choose $a_i$ to be the **smallest-index** private witness of $q$ in $T$.

By the linchpin (Lemma 1), $a_i$ carries some $p\in P_1\cap S(a_i)$; since $p\le\max P_1\le M_1<q$, we have $p\ne q$, hence $p\in S(a_i)\setminus T$ — *the witness has a small $P_1$-prime outside $T$*. The strip plan: remove the large factor $q$ from $a_i=q\cdot A'$ and replace it by a power of a small prime just large enough to clear $a_{i-1}$, producing $x$ with $a_{i-1}<x<a_i$ that is still admissible — contradicting greedy minimality of $a_i$.

Two rigorous positive results first.

---

**Lemma A (smallest-multiple structure).** *With $q>M_1\ge d_{i-1}=a_i-a_{i-1}$ and $q\mid a_i$, the term $a_i$ is the smallest positive multiple of $q$ strictly greater than $a_{i-1}$.*

*Proof.* The smallest multiple of $q$ strictly greater than $a_{i-1}$ is $\mu:=q\lceil(a_{i-1}+1)/q\rceil\in(a_{i-1},\,a_{i-1}+q]$. Since $a_i$ is a multiple of $q$ with $a_i>a_{i-1}$, we have $a_i\ge\mu$. On the other hand the gap bound (Lemma 1 corollary) gives $a_i=a_{i-1}+d_{i-1}\le a_{i-1}+M_1<a_{i-1}+q=\mu$ if $\mu=a_{i-1}+q$; more precisely $\mu-a_{i-1}\in[1,q]$ and $a_i-a_{i-1}=d_{i-1}\le M_1<q$, so $a_i-a_{i-1}<q$. As $a_i$ is a multiple of $q$ lying in the interval $(a_{i-1},\,a_{i-1}+q)$ and $\mu$ is the unique multiple of $q$ in $(a_{i-1},\,a_{i-1}+q]$, we conclude $a_i=\mu$. ∎

**Corollary A1.** $q\nmid a_{i-1}$. *Proof.* If $q\mid a_{i-1}$ and $q\mid a_i$, then $q\mid(a_i-a_{i-1})=d_{i-1}\le M_1<q$, forcing $d_{i-1}=0$, contradicting $a_i>a_{i-1}$. ∎

**Corollary A2 (the $a_{i-1}$ case is admissibility-obstruction-free).** *The term $a_{i-1}$ shares a prime $t\ne q$ with $a_i$, and every such shared prime satisfies $t\le M_1$ (is small).*

*Proof.* By pairwise intersection (Lemma 2), $a_{i-1}$ and $a_i$ share a prime $t$. By Corollary A1, $q\nmid a_{i-1}$, so $t\ne q$. Now $t\mid a_i$ and $t\mid a_{i-1}$, hence $t\mid(a_i-a_{i-1})=d_{i-1}\le M_1$; as $t$ is prime and $t\mid d_{i-1}>0$, we get $t\le d_{i-1}\le M_1$. ∎

So $a_{i-1}$ is never an obstruction to admissibility transfer: the shared prime is small, lies in $S(a_i)$, and divides any $x$ built from the small primes of $a_i$. The obstruction, if any, must come from $a_j$ with $j\le i-2$.

**Lemma B ($T\setminus\{q\}$ transverses $\mathcal F_{i-1}$, smallest-index witness).** *With $a_i$ chosen as the smallest-index private witness of $q$ in $T\in\operatorname{MT}(\mathcal F_\infty)$, the reduced set $T\setminus\{q\}$ is a transversal of $\mathcal F_{i-1}=\{S(a_1),\dots,S(a_{i-1})\}$: every $a_j$ with $j<i$ is hit by some prime of $T\setminus\{q\}$.*

*Proof.* $T$ is a transversal of $\mathcal F_\infty\supseteq\mathcal F_{i-1}$, so $T\cap S(a_j)\ne\varnothing$ for every $j\le i-1$. Suppose for some $j<i$ that $T\setminus\{q\}\cap S(a_j)=\varnothing$; then $T\cap S(a_j)\subseteq\{q\}$, and since $T$ hits $S(a_j)$, $T\cap S(a_j)=\{q\}$. This means $q$ is private to $a_j$ as well (i.e. $S(a_j)\cap T=\{q\}$) — but $j<i$, contradicting the *smallest-index* choice of $a_i$ as the private witness of $q$. Hence $T\setminus\{q\}$ hits every $a_j$, $j<i$. ∎

(The reviewer's "half-sound" half: $T\setminus\{q\}$ transverses $\mathcal F_{i-1}$ — confirmed. The gap is that the $T\setminus\{q\}$-prime hitting $a_j$ need not lie in $S(a_i)$, hence need not divide the stripped $x$.)

---

**Step 7.3 — The size-bound no-go and admissibility-transfer obstruction.**

Recall the strip plan: form $x$ from the *small* primes of $a_i$ (primes $\le M_1$, excluding the large $q$) plus possibly a small-prime power, with $a_{i-1}<x<a_i$, and prove $x$ admissible against $\mathcal F_{i-1}$. Let $A:=\prod_{r\in S(a_i),\,r\le M_1,\,r\ne q}r$ (the *small radical of $a_i$ minus $q$*). Note $A\mid a_i$ (every small prime of $a_i$ divides $a_i$).

**Lemma C (size-bound no-go for the multiple-of-$A$ strip).** *Consider $x_0:=$ the smallest multiple of $A$ strictly greater than $a_{i-1}$. Then:*
- *(i) If $d_{i-1}\le A$, then $x_0=a_i$ (no shrinking — the next multiple of $A$ above $a_{i-1}$ is $a_i$ itself).*
- *(ii) If $d_{i-1}>A$, then every multiple of $A$ in the open interval $(a_{i-1},a_i)$ is **inadmissible** against $\mathcal F_{i-1}$ (by greedy minimality of $a_i$).*
- *In either case, no admissible multiple of $A$ lies in $(a_{i-1},a_i)$.*

*Proof.* (i) $A\mid a_i$ and $a_i=a_{i-1}+d_{i-1}$. The residue $a_{i-1}\bmod A$ equals $a_{i-1}-(a_i-d_{i-1})\bmod A=(-d_{i-1})\bmod A=A-(d_{i-1}\bmod A)$ if $A\nmid d_{i-1}$, and $0$ if $A\mid d_{i-1}$. The smallest multiple of $A$ strictly above $a_{i-1}$ is $a_{i-1}+A$ if $A\mid a_{i-1}$ (i.e. $A\mid d_{i-1}$, giving residue $0$), else $a_{i-1}+(A-(a_{i-1}\bmod A))=a_{i-1}+(A-((A-d_{i-1})\bmod A))$. In the case $d_{i-1}\le A$: if $d_{i-1}<A$ then $a_{i-1}\bmod A=A-d_{i-1}\in[1,A-1]$ and the next multiple is $a_{i-1}+d_{i-1}=a_i$; if $d_{i-1}=A$ then $a_{i-1}\bmod A=0$ and the next multiple is $a_{i-1}+A=a_i$. Either way $x_0=a_i$. (ii) $a_i$ is by definition the *smallest admissible* integer exceeding $a_{i-1}$; any integer in $(a_{i-1},a_i)$ is inadmissible, so in particular every multiple of $A$ there is inadmissible. ∎

**Lemma C says: the "smallest-multiple-of-$A$" version of the strip is structurally incapable of producing an admissible $x<a_i$.** The obstruction is not a missing estimate; it is forced by the greedy rule itself.

**The $p^kA$ version (prime-power multiplier) blows up.** The outliner's alternative $x=p^kA$ with $p\in P_1\cap S(a_i)$ and $k$ least with $p^kA>a_{i-1}$: from $p^{k-1}A\le a_{i-1}<p^kA$ we get $x=p^kA\le p\cdot a_{i-1}$. For $x<a_i=a_{i-1}+d_{i-1}\le a_{i-1}+M_1$ this requires $p\cdot a_{i-1}<a_{i-1}+M_1$, i.e. $(p-1)a_{i-1}<M_1$, which fails for $a_{i-1}>M_1/(p-1)$ — i.e. for all sufficiently large witnesses (the sequence grows without bound, so eventually $a_{i-1}\gg M_1$). **Computational confirmation** (Bash): for $a_1=385$, stripping the governing prime $q=19$ explicitly (to simulate the $q>M_1$ regime) and forming $x=p^kA$ for the smallest-index private witnesses yields $x\in[686,4802]\gg a_i\in[399,1064]$ — the size bound fails by an order of magnitude. The prime-power multiplier grows exponentially in $a_{i-1}$, far outrunning the linear growth of $a_i$.

**The admissibility-transfer obstruction is real (not merely unproven).** The load-bearing step (Step 3e of the outliner) requires: for each $a_j$ ($j<i$), the stripped $x$ shares a prime with $a_j$. The obstruction is "$a_j$ shares ONLY $q$ with $a_i$" — then $x$ (built from $a_i$'s small primes) misses $a_j$. **Computational verification** (Bash): for $a_1=385$ with governing prime $q=19$ (a small analogue of the hypothetical $q>M_1$), there are $51$ pairs $(a_j,a_i)$ with $S(a_j)\cap S(a_i)=\{q\}$ in the first 700 terms. Computing the minimal-transversal family at $n=120$ and the smallest-index private witnesses of $19$ in each MT containing it:
- $T=\{2,11,19\}$: private witness $a_5=399=3\cdot7\cdot19$ — **no obstruction** (every earlier $a_j$ shares a small prime with $a_5$).
- $T=\{3,7,19\}$: private witness $a_7=418=2\cdot11\cdot19$ — **OBSTRUCTED** by $a_5=399$ (shares only $19$ with $a_7$).

So even with the smallest-index-witness choice (Lemma B's precondition), the obstruction **does** arise for some minimal transversals. One may hope to *choose* an obstruction-free $T$ (and the first $T$ above is obstruction-free), but no proof exists that such a $T$ must always exist in the hypothetical $q>M_1$ regime — and the abstract star counterexample $\{\{1,j\}:j\ge2\}$ (pairwise-intersecting family with unbounded transversal primes, no greedy coupling) shows the greedy coupling is the only thing that could force it, yet no mechanism taming the obstruction has been produced.

**Honest summary of the strip attempt.** Two positive lemmas (A and B above) are proved, plus the $a_{i-1}$ admissibility case (Corollary A2). But the strip's two load-bearing steps — the size bound $x<a_i$ and admissibility transfer for $j\le i-2$ — are **not closeable as formulated**:
- the size bound has a structural no-go (Lemma C) for the natural "multiple-of-$A$" construction, and the "$p^kA$" construction blows up exponentially;
- admissibility transfer is empirically obstructed in the small-prime analogue, even for smallest-index private witnesses.

> **Open sub-lemma (Gap A$'$, unchanged).** *Prove that the dynamics of $\operatorname{MT}(\mathcal F_n)$ as $n$ grows — coupled to the greedy choice and the gap bound $d_n\le M_1$ — admits only finitely many primes as members of any $\operatorname{MT}(\mathcal F_n)$. The `aimo-0030` minimal-criminal strip, in the formulations tried here (multiple-of-$A$ and $p^kA$), does NOT close this gap: the size bound has a no-go and admissibility transfer is genuinely obstructed. A viable route must use a different mechanism — not the one-shot prime-factor strip.*

---

**Step 7.4 — Fallback A (least-multiplier minimality) and Fallback B (witness recurrence) — sketched, open.**

*Fallback A.* Write $a_i=q\cdot m$ with $m=a_i/q$. By Lemma A, $m=\lceil(a_{i-1}+1)/q\rceil$, so $m$ is the least multiplier landing $qm$ above $a_{i-1}$. Since $q>M_1\ge d_{i-1}$ and $a_i\le a_{i-1}+M_1$, we have $m\le(a_{i-1}+M_1)/q< a_{i-1}/q+1$. The multiplier $m$ carries the small $P_1$-prime $p$ (linchpin, $p\ne q$). The idea: minimality of $m$ (not just of $a_i$) as "the least multiplier reaching the threshold $a_{i-1}$ with the required prime signature" may pin $q\mid a_i$ to $q\le M_1$. **Status: open.** The mechanism is not made rigorous here — "minimality of $m$" is not a greedy minimality (the greedy rule picks $a_i$, not $m$), and converting the strip's failures into a multiplier argument has not been achieved.

*Fallback B (witness recurrence + density).* A governing $q$ must be re-witnessed infinitely often (else transient). Consecutive re-witnesses $a_{i_k},a_{i_{k+1}}$ are distinct multiples of $q$, so $a_{i_{k+1}}-a_{i_k}\ge q>M_1\ge$ (per-step gap); the witness INDEX gap $i_{k+1}-i_k\ge q/M_1$. If $q>M_1$ then witnesses are non-adjacent and witness density $\le M_1/q<1$ per step. Combined with a covering-capacity bound (max distinct supports absorbable between witnesses without $q$ leaving $\operatorname{MT}$), one would derive $q\le M_1\cdot C$ for a $|P_1|$-bounded constant $C$. **Status: open.** The covering-capacity bound is circular as stated (bounding the primes in intermediate supports IS Gap A — the star counterexample $\{\{1,j\}\}$ shows the abstract family has unbounded covering capacity; the greedy coupling is essential but no non-circular $C$-bound is produced here). This fallback is the subject of the parallel `witness-density-recurrence` approach; we do not duplicate its (also open) crux.

---

### Step 8 — The lock case (prime power appears): a complete sub-proof

The theorem is *unconditionally* true whenever the sequence contains a prime power. This sub-case does not need Gap A, because $\mathcal B_\infty$ can be identified explicitly.

**Lemma 9 (lock).** If some $a_i=p^k$ is a prime power ($p$ prime, $k\ge1$), then $a_n=a_1+p(n-1)$ for every $n\ge1$. In particular $T=1$, $L=p$.

*Proof.* Since $a_i=p^k$ has $S(a_i)=\{p\}$ and $a_i$ was chosen admissible, $a_i$ shares a prime with every $a_j$ ($j<i$); the only such prime is $p$, so $p\mid a_j$ for all $j<i$. For $j>i$, $a_j$ must share a prime with $a_i$, so $p\mid a_j$. Hence **every** $a_n$ is a multiple of $p$. Consequently every multiple of $p$ shares the factor $p$ with every $a_n$, i.e. every positive multiple of $p$ lies in $\mathcal B_\infty$. Conversely, if $m\not\equiv0\bmod p$ then $S(m)\cap S(a_i)=\varnothing$ (as $\{p\}=S(a_i)$), so $m\notin\mathcal B_\infty$. Thus
$$\mathcal B_\infty=\{m\in\mathbb Z_{>0}:p\mid m\}=p\mathbb Z_{>0}.$$
This is $p$-periodic with $L=p$ and $A=\{0\}\subseteq\mathbb Z/p\mathbb Z$, $|A|=1$, so $T=1$. By Lemma 4 (greedy $=$ cyclic successor), $a_{n+1}=a_n+p$ for every $n\ge1$, i.e. $a_n=a_1+p(n-1)$. ∎ *(Certified: `lemmas/lock-lemma.md`.)*

**Corollary 10 (even $a_1$).** If $2\mid a_1$, then $a_n=a_1+2(n-1)$ for all $n\ge1$ ($T=1$, $L=2$).

*Proof.* Either $a_1$ is a power of $2$ (Lemma 9 with $p=2$), or $a_1$ has an odd prime factor $r$; in the latter case consider $a_1$ itself. Direct induction: assume $a_1,\dots,a_n$ are all the consecutive even integers $a_1,a_1+2,\dots,a_1+2(n-1)$ (true for $n=1$). Then $a_n+1$ is odd and $\gcd(a_n+1,a_n)=1$ (consecutive integers), so $a_n+1$ fails admissibility against $a_n$; $a_n+2$ is even and shares the factor $2$ with every prior (even) term, so $a_{n+1}=a_n+2$. The induction proceeds, giving $a_n=a_1+2(n-1)$. ∎

**Corollary 11 (prime-power $a_1$).** If $a_1=p^k$ is a prime power, then $a_n=a_1+p(n-1)$ ($T=1$, $L=p$), by Lemma 9 with $i=1$.

### Summary

- **Proved unconditionally (certified):** Lemmas 1–4 (linchpin + gap bound $d_n\le M_1$; pairwise intersection; every term in $\mathcal B_\infty$; greedy $=$ cyclic successor in $\mathcal B_\infty$ from $n=1$); Lemmas 5–6 (cyclic-successor bijection $\Rightarrow$ single cycle $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$, *conditional only* on $\mathcal B_\infty$ being $L$-periodic); Lemma 9 + Corollaries 10–11 (the lock / even / prime-power-$a_1$ cases, complete and unconditional).
- **Proved unconditionally (round 2, this build):** Lemma A (smallest-multiple structure of $a_i$); Corollaries A1, A2 ($q\nmid a_{i-1}$; $a_{i-1}$ shares a small prime with $a_i$); Lemma B ($T\setminus\{q\}$ transverses $\mathcal F_{i-1}$ for smallest-index witness); Lemma C (size-bound no-go for the multiple-of-$A$ strip).
- **Equivalence proved:** Gap A "$\mathcal B_\infty$ is $L$-periodic" $\iff$ "finitely many primes enter a minimal transversal of $\mathcal F_\infty$" (Step 6).
- **Factual corrections made:** $a_1=385$ IS periodic from $n=1$ ($L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$, $T=5088$); governing primes $\{2,3,5,7,11,19\}\le M_1=385$; governing vs transient primes properly distinguished; the false "aperiodic" / "$q\le M_1$ refuted" narrative retracted.
- **Open:** Gap A in the genuinely periodic regime (no prime power ever appears, every support has size $\ge2$). The `aimo-0030` minimal-criminal strip, in the formulations tried (multiple-of-$A$; $p^kA$), does **not** close Gap A: the size bound has a structural no-go (Lemma C) and the $p^kA$ version blows up exponentially; admissibility transfer is empirically obstructed even for smallest-index private witnesses in the small-prime analogue. Fallbacks A and B are sketched but open (Fallback B's covering-capacity bound is circular as stated). The abstract pairwise-intersecting structure is *insufficient* (star counterexample $\{\{1,j\}:j\ge2\}$ admits unbounded transversal primes); the greedy + bounded-gap coupling is ESSENTIAL but no mechanism taming the obstruction has been produced.

Thus the theorem holds in full once Gap A is established, and the reduction above shows exactly where the remaining difficulty lives — now sharpened by the knowledge that the one-shot prime-factor strip is not the right mechanism. ∎ (conditional on Gap A; unconditional in the lock sub-case)

## Promotable lemmas

- **Lemma A (smallest-multiple structure).** If $q>M_1\ge d_{i-1}$ and $q\mid a_i$, then $a_i$ is the smallest positive multiple of $q$ strictly greater than $a_{i-1}$; equivalently $a_i=q\lceil(a_{i-1}+1)/q\rceil$. Proved in Step 7.2. Importable by any approach using the "witness $a_i$ is a multiple of a large prime $q$" structure.
- **Corollary A2 (the predecessor shares a small prime).** If $q>M_1$ and $q\mid a_i$, then $q\nmid a_{i-1}$ and every prime shared between $a_{i-1}$ and $a_i$ is $\le M_1$. Proved in Step 7.2 (uses Lemma A + pairwise intersection). Importable for admissibility-transfer arguments that need to handle the $j=i-1$ case.
- **Lemma B ($T\setminus\{q\}$ transversal).** If $a_i$ is the smallest-index private witness of $q$ in $T\in\operatorname{MT}(\mathcal F_\infty)$, then $T\setminus\{q\}$ is a transversal of $\mathcal F_{i-1}$. Proved in Step 7.2. Importable for any strip/density argument relying on the private-witness structure.
- **Lemma C (size-bound no-go for the multiple-of-$A$ strip).** With $A=$ small radical of $a_i$ minus $q$ (so $A\mid a_i$): the smallest multiple of $A$ above $a_{i-1}$ is $a_i$ itself when $d_{i-1}\le A$, and every multiple of $A$ in $(a_{i-1},a_i)$ is inadmissible when $d_{i-1}>A$. Proved in Step 7.3. A *negative* lemma — records that the natural multiple-of-small-radical strip cannot work, saving future rounds from re-trying it.
- (Lemmas 1–6, 9 already certified in `lemmas/` from round 1; not re-listed.)
