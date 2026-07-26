# Approach: crude-reduced-type

## Status
partial

## Approaches tried
- (round 1) Skeleton filed: crude modulus $L_0=\prod_{p\le a_1}p$, reduced types in $2^Q$, transversal-family stabilization, free-rider wall (Step 7) as the inherited crux. Steps 1–6 certified "standard and correct" by R1 reviewer; Step 7 flagged as the crux (= Lemma 4); "for all $n$ / no-transient" and "Step 10 gap-sum" flagged as required additions.
- (round 2) Built the full conditional-on-crux proof. Steps 1–6 written rigorously (cheap anchor; reduced types in finite lattice; nested-increasing seen-type family $F_n$ and nested-decreasing transversal family $H_n$ both stabilize on $2^Q$; fixed objects $F,H,V_0$ defined). Step 7 stated as the explicit free-rider wall [GAP] = Lemma 4, imported from `essential-monovariant` (one paragraph, not attacked). Steps 8–10 added mirroring `essential-monovariant`'s certified Theorem: deterministic residue walk $\varphi:V_0\to V_0$, $\varphi$ is the cyclic-successor bijection on the finite ordered set $V_0$ (single orbit of length $T=|V_0|$, hence no transient — the orbit is purely periodic from $n=1$), and the telescoping lift $\sum$ gaps over one full cycle $=L_0$ (exactly one wrap), giving $a_{n+T}=a_n+L_0$ for every $n\ge 1$. Output: a second complete conditional-on-crux proof with the free-rider wall as the single marked [GAP]. — partial (sole gap: the crux Lemma 4, inherited, not independently closed).

## Current best
A second complete conditional-on-crux bridge: assuming the crux Lemma 4 (every pair of terms $a_i,a_j$ shares a prime $\le a_1$, equivalently $E\subseteq Q:=\{p\text{ prime}:p\le a_1\}$), the greedy sequence of IMO 2026 P6 is translation-periodic with $a_{n+T}=a_n+L_0$ for **every** $n\ge 1$ (no transient), where $L_0=\prod_{p\le a_1}p$ and $T=|V_0|$. All machinery (finite-lattice stabilization, free-rider irrelevance, cyclic-permutation periodicity, telescoping lift) is rigorous; the sole open step is the crux itself, marked [GAP].

## Full proof (partial — the crux Lemma 4 is marked **[GAP]**)

### 0. Definitions and notation

Fix $a_1>1$. Let
$$Q:=\{p\text{ prime}:p\le a_1\},\qquad L_0:=\prod_{p\in Q}p.$$
$Q$ is finite (it is the set of primes up to the fixed integer $a_1$). $L_0$ is squarefree and finite (it is a finite primorial); its size is irrelevant to the argument — only finiteness is used.

For an integer $m>1$ write $P(m)$ for its set of prime divisors, and define the **$Q$-type** (reduced type) of $m$:
$$r(m):=P(m)\cap Q\subseteq 2^Q.$$
Because $p\mid L_0$ for every $p\in Q$, the type $r(m)$ depends only on the residue $m\bmod L_0$: a prime $p\in Q$ divides $m$ iff it divides $m\bmod L_0$ (with the convention that the residue $0$ is divisible by every $p\in Q$).

The sequence is greedy: $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \text{for every }i\le n\}$.

### 1. Lemma 1 (cheap structural anchor) — PROVED

**Lemma 1.** *For every $n\ge 1$, $r(a_n)\ne\varnothing$; equivalently every term $a_n$ has a prime divisor in $Q$.*

*Proof.* For $n=1$ this is tautological: every prime divisor of $a_1$ is $\le a_1$, hence lies in $Q$, so $P(a_1)\subseteq Q$ and $r(a_1)=P(a_1)\ne\varnothing$. For $n\ge 2$, the greedy rule applied at stage $n-1$ forces $\gcd(a_n,a_1)>1$; let $p$ be any prime with $p\mid\gcd(a_n,a_1)$. Then $p\mid a_1$, so $p\le a_1$, hence $p\in Q$; and $p\mid a_n$, so $p\in r(a_n)$. Thus $r(a_n)\ne\varnothing$. $\square$

### 2. Reduced types live in a finite lattice — PROVED

By Lemma 1, $r(a_n)\in 2^Q\setminus\{\varnothing\}$ for every $n\ge 1$. The ambient set $2^Q\setminus\{\varnothing\}$ is finite because $Q$ is finite. This is the entire content of this step: the "state space" of reduced types is finite.

### 3. Lemma 2 (stabilization on the finite lattice) — PROVED

Define the **seen-type family** at stage $n$:
$$F_n:=\{r(a_i):1\le i\le n\}\subseteq 2^Q.$$
The family is nested-increasing: $F_1\subseteq F_2\subseteq\cdots$, since each $F_{n+1}=F_n\cup\{r(a_{n+1})\}$. A monotone-nondecreasing sequence of subsets of a finite set is eventually constant (knowledge_base: "Invariants & monovariants" — a monotone quantity on a finite set stabilizes). Hence there exists $N$ with $F_n=F$ for all $n\ge N$, where
$$F:=\{r(a_i):i\ge 1\}$$
is the set of all $Q$-types ever appearing in the sequence.

A subset $S\subseteq Q$ is a **transversal** (hitting set) of a family $\mathcal{F}\subseteq 2^Q$ if $S\cap T\ne\varnothing$ for every $T\in\mathcal{F}$. Define the **transversal family** of $F_n$:
$$H_n:=\{S\in 2^Q:S\cap T\ne\varnothing\text{ for every }T\in F_n\}.$$
Because $F_n\subseteq F_{n+1}$, being a transversal of $F_{n+1}$ is a stronger condition than being a transversal of $F_n$; hence $H_{n+1}\subseteq H_n$. The family $\{H_n\}$ is nested-decreasing in the finite set $2^Q$, so by the same monotone-on-finite principle it is eventually constant: there exists $N'$ with $H_n=H$ for all $n\ge N'$, where
$$H:=\{S\in 2^Q:S\cap T\ne\varnothing\text{ for every }T\in F\}$$
is the transversal family of the stabilized seen-type set $F$. Set $N_0:=\max(N,N')$; for all $n\ge N_0$ we have $F_n=F$ and $H_n=H$. $\square$

### 4. Fixed valid-residue set $V_0$ — PROVED (definition)

Define the **valid-residue set** mod $L_0$:
$$V_0:=\{\rho\in\{0,1,\dots,L_0-1\}:\{p\in Q:p\mid\rho\}\in H\},$$
with the convention that $0$ is divisible by every $p\in Q$. Because $p\mid L_0$ for every $p\in Q$, the type $r(m)=\{p\in Q:p\mid m\}$ depends only on $m\bmod L_0$; thus $V_0$ is exactly the set of residues $\rho$ whose $Q$-type $r(\rho)$ is a transversal of $F$. Since $H$ is fixed (Lemma 2), $V_0$ is a fixed finite set, independent of $n$.

### 5. Step 7 — FREE-RIDER WALL (the crux, **[GAP]**)

The crux is the following statement, which is **Lemma 4 of the sibling approach `essential-monovariant`** (with $Q$ in place of $Q_R=\{p\le\operatorname{rad}(a_1)\}$; the present $Q=\{p\le a_1\}$ is a superset, so the statement is a priori weaker and is implied by that Lemma 4 — we **inherit** it, we do not independently prove it).

> **Lemma 4 (crux, inherited from `essential-monovariant`).** *For all $i<j$, $P(a_i)\cap P(a_j)\cap Q\ne\varnothing$: every pair of terms shares a prime in $Q$ (i.e. a prime $\le a_1$).*

Equivalently (the "free-rider dichotomy"): no prime $q>a_1$ is ever the *unique* shared prime of a pair of terms. A "free-rider" prime $q>a_1$ dividing some $a_j$ cannot by itself witness admissibility of a candidate $m$ against $a_j$ — the candidate must also share a $Q$-prime with $a_j$. This is exactly the wall that the skeleton's Step 7 names; the round-1 reviewer confirmed it is the inherited crux, not independently closed by this approach. The present approach does **not** attack Lemma 4; it imports it. **[GAP]**

**Why Lemma 4 is the wall.** The greedy rule only forces $\gcd(a_{n+1},a_i)>1$ (some shared prime, possibly a free rider $>a_1$). To conclude $a_{n+1}\bmod L_0\in V_0$ one must upgrade "shares a prime" to "shares a $Q$-prime" — which is precisely Lemma 4 applied to the pair $(a_{n+1},a_i)$. Without Lemma 4, Step 6 of the skeleton (membership in $V_0$) does not go through; with Lemma 4, it does, and moreover the *minimality* characterization $a_{n+1}=\min\{m>a_n:m\bmod L_0\in V_0\}$ follows. This is the content of the next section.

### 6. Free-rider irrelevance (conditional on Lemma 4) — PROVED given Lemma 4

**Claim.** *Assume Lemma 4. Then for every $n\ge 1$,*
$$a_{n+1}=\min\{m>a_n:m\bmod L_0\in V_0\}=:m_n^*.$$
*In particular $a_{n+1}\bmod L_0\in V_0$ (so the residue sequence stays in $V_0$ for all $n\ge 1$), and $a_1\bmod L_0\in V_0$.*

*Proof.* Two directions, mirroring `essential-monovariant`'s Section 5.

**(Transversal $\Rightarrow$ admissible.)** Suppose $m\bmod L_0\in V_0$. Then $r(m)\in H$, so $r(m)$ is a transversal of $F$. Since $F\supseteq F_n=\{r(a_i):i\le n\}$ (as $F$ is the union of all $F_n$), $r(m)\cap r(a_i)\ne\varnothing$ for every $i\le n$: pick $p\in r(m)\cap r(a_i)\subseteq Q$; then $p\mid m$ and $p\mid a_i$, so $\gcd(m,a_i)\ge p>1$. Thus $m$ is admissible at stage $n$. In particular $m_n^*$ (the least integer $>a_n$ whose residue lies in $V_0$) is admissible, so by greedy minimality $a_{n+1}\le m_n^*$.

**($a_{n+1}$ has transversal type.)** $a_{n+1}$ is admissible at stage $n$, so it shares *some* prime with every $a_i$ ($i\le n$). Apply **Lemma 4** to the pair of terms $(a_{n+1},a_i)$: they share a prime in $Q$, i.e. $r(a_{n+1})\cap r(a_i)\ne\varnothing$. (Note Lemma 4 applies to *every* pair of terms — not only $i\le n$ — but we only need $i\le n$ here.) Hence $r(a_{n+1})$ is a transversal of $F_n=F$ (for $n\ge N_0$; for $n<N_0$ we use that $F_n\subseteq F$ and the same argument shows $r(a_{n+1})$ is a transversal of $F_n$, hence — applying Lemma 4 to the finitely many later types — of $F$). So $r(a_{n+1})\in H$, i.e. $a_{n+1}\bmod L_0\in V_0$. Since $a_{n+1}>a_n$ and $a_{n+1}\bmod L_0\in V_0$, the minimum $m_n^*$ satisfies $m_n^*\le a_{n+1}$.

Combining both directions, $a_{n+1}=m_n^*$ for every $n\ge 1$. (The "for all $n\ge 1$" — including the pre-stabilization regime $n<N_0$ — holds because Lemma 4 is index-free: it is a statement about *every* pair of terms, and $F\supseteq F_n$ always, so the transversal-$\Rightarrow$-admissible direction uses the fixed $F$, and the admissible-$\Rightarrow$-transversal direction uses Lemma 4 directly. No stabilization threshold enters the claim; stabilization was only needed to define $F,H,V_0$ as fixed objects, which is the index-free backbone.) $\square$ (Claim)

A useful corollary: applying Lemma 4 to the pair $(a_1,a_j)$ for every $j\ge 1$ shows $r(a_1)\cap r(a_j)\ne\varnothing$ for all $j$, so $r(a_1)\in H$, i.e. $a_1\bmod L_0\in V_0$. Thus the residue sequence begins inside $V_0$.

### 7. Step 8 — Deterministic residue walk $\varphi:V_0\to V_0$ — PROVED given Lemma 4

By the Claim, for every $n\ge 1$ the next term's residue $a_{n+1}\bmod L_0$ is the least residue in $V_0$ strictly above $a_n$ (cyclically, wrapping by $+L_0$ if needed). Because $V_0$ and $L_0$ are fixed and the type $r(m)$ depends only on $m\bmod L_0$, this "next-$V_0$-residue above $a_n$" depends only on $a_n\bmod L_0$. Concretely, writing $r_n:=a_n\bmod L_0\in V_0$, define
$$\varphi(r):=\min\{s\in V_0:s>r\}\ \text{if this set is nonempty},\qquad \varphi(r):=\min V_0\ \text{otherwise}$$
(the cyclic successor of $r$ in the natural order on $\{0,\dots,L_0-1\}$, wrapping around to $\min V_0$ when $r$ is the largest element of $V_0$). Then
$$r_{n+1}=\varphi(r_n)\qquad\text{for every }n\ge 1.$$
$\varphi:V_0\to V_0$ is well-defined because $V_0$ is nonempty (it contains $a_1\bmod L_0$ by the corollary above). $\square$

### 8. Step 9 — $\varphi$ is a cyclic permutation; period $T=|V_0|$, no transient — PROVED given Lemma 4

Write the elements of $V_0$ in increasing order $v_1<v_2<\dots<v_T$, where $T:=|V_0|\ge 1$. Then $\varphi$ is the **cyclic successor**:
$$\varphi(v_i)=v_{i+1}\ (i<T),\qquad \varphi(v_T)=v_1.$$
This is a bijection $V_0\to V_0$ (its inverse is the cyclic predecessor), and its single orbit is all of $V_0$: starting from any $v_i$ and iterating $\varphi$ visits $v_{i+1},v_{i+2},\dots,v_T,v_1,\dots,v_i$, returning after exactly $T=|V_0|$ steps. In particular $\varphi$ is a **cyclic permutation of length $T$**, and
$$r_{n+T}=r_n\qquad\text{for every }n\ge 1.$$
(Reason: $r_{n+1}=\varphi(r_n)$ and $\varphi^T=\mathrm{id}_{V_0}$.) Crucially, because $\varphi$ is a **bijection** (not merely a function on a finite set), the orbit is **purely periodic from the start** — there is no pre-periodic transient. Knowledge_base: "Order of an element, Fermat/Euler" — eventual periodicity of an orbit on a finite set; here the stronger "bijective ⟹ no transient" applies, which is the round-1 reviewer's defusing of the "for all $n$" quantifier. The periodicity holds for **all** $n\ge 1$, not merely eventually. $\square$

### 9. Step 10 — Telescoping lift to translation-periodicity — PROVED given Lemma 4

It remains to lift the residue periodicity to the integer sequence. Over one full period of $T$ consecutive steps, the residues $r_n,r_{n+1},\dots,r_{n+T-1}$ traverse every element of $V_0$ exactly once (the orbit of $\varphi$ has length $T$ and is all of $V_0$); hence exactly one of the $T$ transitions wraps around, and the rest are non-wrapping successors.

The integer gaps are:
- $a_{k+1}-a_k=(\varphi(r_k)\bmod L_0)-r_k$ when $\varphi(r_k)>r_k$ (no wrap; both residues in $\{0,\dots,L_0-1\}$, the next residue exceeds the current, and $a_{k+1}=a_k-r_k+\varphi(r_k)$);
- $a_{k+1}-a_k=(\varphi(r_k)+L_0)-r_k$ when $\varphi(r_k)$ wraps (i.e. $r_k=v_T$, $\varphi(r_k)=v_1<r_k$); the term $+L_0$ accounts for the wrap.

Summing over the $T$ consecutive transitions of one full period, the residues (in cyclic order) are $v_{\sigma},v_{\sigma+1},\dots$ for some cyclic shift $\sigma$; the sum telescopes:
$$\sum_{k=0}^{T-1}(a_{n+1+k}-a_{n+k})=(v_2-v_1)+(v_3-v_2)+\dots+(v_T-v_{T-1})+(v_1+L_0-v_T)=L_0,$$
where the single $+L_0$ comes from the unique wrapping transition ($v_T\to v_1$). (Cyclic rotation of the starting point does not change the sum: the differences telescope to $L_0$ regardless of where in the cycle one starts, because the cycle is a single bijection-orbit of length $T$.) The left side is $a_{n+T}-a_n$. Therefore
$$a_{n+T}=a_n+L_0\qquad\text{for every }n\ge 1,$$
with $T=|V_0|$ and $L=L_0=\prod_{p\le a_1}p$. $\square$

This completes the conditional theorem: **assuming the crux Lemma 4, IMO 2026 P6 holds with $T=|V_0|$ and $L=L_0$ for every $n\ge 1$, with no transient.**

### 10. Sanity anchors (not load-bearing; the general machine subsumes them)

For completeness we record the degenerate sub-cases, which the general machine handles automatically (they are not separate proofs, just consistency checks):

- **$a_1$ prime power, say $a_1=p^k$.** Then $P(a_1)=\{p\}$, so Lemma 1 forces $p\mid a_n$ for every $n$ (every term is divisible by $p$). The transversal family $H$ contains exactly those $S\subseteq Q$ with $p\in S$; $V_0=\{\rho\in\{0,\dots,L_0-1\}:p\mid\rho\}$, the multiples of $p$ mod $L_0$; $|V_0|=L_0/p$. The walk $\varphi$ advances by $+p$ each step (the next multiple of $p$), $T=L_0/p$, and one full cycle advances the integer by $p\cdot T=L_0$. Consistent.
- **$2\mid a_1$.** Then $2\in Q$; $2$ is a prime divisor of $a_1$; by Lemma 1 every $a_n$ has *some* prime of $a_1$ (not necessarily $2$). The general machine applies; $V_0$ may have several residues. No shortcut; $L=L_0$ in general.

These are subsumed: the general machine produces a (possibly crude) $L$ in every case.

### Summary of rigour status

- Lemma 1 (cheap anchor): fully proved.
- Lemma 2 (stabilization of $F_n$ and $H_n$ on the finite lattice $2^Q$): fully proved.
- Step 4 ($V_0$ definition): definition, sound.
- Step 5 / **Lemma 4 (crux): unproved [GAP]** — imported from `essential-monovariant`; not independently closed by this approach.
- Steps 6–9 (free-rider irrelevance, deterministic walk $\varphi$, cyclic-permutation periodicity with no transient, telescoping lift to $a_{n+T}=a_n+L_0$ for all $n\ge 1$): fully proved **conditional on Lemma 4**, mirroring `essential-monovariant`'s certified Theorem.
- The whole theorem is proved conditional on the single crux Lemma 4.

## Promotable lemmas
- **Lemma 1 (cheap anchor).** For the greedy sequence of IMO 2026 P6 with $Q=\{p:p\le a_1\}$, every term $a_n$ has a prime divisor in $Q$; equivalently $r(a_n)=P(a_n)\cap Q\ne\varnothing$. Proved in Section 1. (Reusable: the universal small-prime anchor at the cruder $Q=\{p\le a_1\}$ threshold; same content as `essential-monovariant` Lemma 1 at the $Q_R$ threshold.)
- **Lemma 2 (finite-lattice stabilization).** The seen-type family $F_n=\{r(a_i):i\le n\}$ (nested-increasing) and the transversal family $H_n$ (nested-decreasing) both stabilize on the finite lattice $2^Q$; fixed limits $F,H$ exist. Proved in Section 3. (Reusable: the stabilization backbone for any finite-type framing of P6.)
- **Theorem (Lemma 4 $\Rightarrow$ $a_{n+T}=a_n+L_0$ for all $n\ge 1$, no transient).** Section 9. Second complete conditional-on-crux bridge (independent of `essential-monovariant`'s Theorem by using $Q=\{p\le a_1\}$ rather than $Q_R=\{p\le\operatorname{rad}(a_1)\}$). (Reusable: any approach that proves the crux — at either the $a_1$ or the $\operatorname{rad}(a_1)$ threshold — inherits a complete proof via the cyclic-successor bijection on $V_0$.)
