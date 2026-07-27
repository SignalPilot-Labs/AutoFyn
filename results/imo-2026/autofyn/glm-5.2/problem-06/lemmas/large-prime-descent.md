# Lemma: large-prime-descent

**Setting.** The greedy gcd sequence. Let $a_m\prec a_n\iff m<n\wedge\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$. Call a prime **large** if $p>a_1^2$, **small** otherwise; set $P_0=\{p:p\le a_1^2\}$. An integer is **$a_1^2$-smooth** if all its prime divisors are $\le a_1^2$.

**Statement (unconditional).** If $a_n$ is divisible by a large prime $p>a_1^2$, then $a_n$ is **not** $\prec$-minimal. Equivalently (contrapositive): **every $\prec$-minimal term is $a_1^2$-smooth.**

**Corollary.** $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite: every $M\in\mathcal M$ is the support of a $\prec$-minimal term (by `minimal-support-direction-b`), hence $M\subseteq P_0$; so $\bigcup\mathcal M\subseteq P_0$ (finite) and $\mathcal M\subseteq 2^{P_0}$ (finite). This is the wall-closer: it makes any GAP-conditional finish (e.g. `post-stabilization-theorem`) unconditional.

**Proof (induction on $n$).** Induction hypothesis:
> **(IH$_n$)** Every $\prec$-minimal term $a_i$ with $i<n$ is $a_1^2$-smooth (equivalently, divisible by no large prime).

**Base $n=1$.** (IH$_1$) is vacuous. The conclusion is also vacuous: if $p\mid a_1$ then $p\le a_1<a_1^2$ (as $a_1\ge2$), so $a_1$ carries no large prime.

**Inductive step.** Assume (IH$_n$); suppose $a_n=p\,c$ with $p>a_1^2$ large; we show $a_n$ is not $\prec$-minimal. (For $n=1$ the premise never holds; assume $n>1$.)

*Step 1 (choose $q$; land $q^k c\in[a_1,a_n)$).* By `appears-criterion-unconditional` (Piece A) applied to $x=a_n$, $\gcd(a_n,a_1)>1$ (as $a_1<a_n$); pick any prime $q\mid\gcd(a_1,a_n)$. Then $q\le a_1$ (as $q\mid a_1$); $q\neq p$ (as $p>a_1^2\ge a_1\ge q$, using $a_1\ge2$); and $q\mid c$ (as $q\mid a_n=pc$ and $q$ is prime with $q\neq p$). Because
$$\frac{a_n}{a_1}=\frac{pc}{a_1}\ge\frac{p}{a_1}>a_1\ge q$$
(the strict step $p/a_1>a_1$ is exactly $p>a_1^2$), we have $a_n/a_1>q$. Let $k$ be the smallest nonnegative integer with $q^k c\ge a_1$. If $k=0$: $c\ge a_1$, and $c<a_n=pc$ (as $p>1$), so $q^k c=c\in[a_1,a_n)$. If $k\ge1$: by minimality $q^{k-1}c<a_1$, so $q^k c=q\cdot q^{k-1}c<q\,a_1\le a_1^2<a_n$ (as $a_n=pc\ge p>a_1^2$). In both cases $q^k c\in[a_1,a_n)$.

*Step 2 (shared-prime transfer: $q^k c$ appears).* By Piece A it suffices to show $\gcd(q^k c,a_i)>1$ for every $\prec$-minimal $a_i<q^k c$. Since $q^k c<a_n$, strict increase gives $a_i<q^k c<a_n\Rightarrow i<n$, so (IH$_n$) applies: $a_i$ is $a_1^2$-smooth, hence $p\nmid a_i$ (as $p>a_1^2$). Now $a_n$ appears after $a_i$ ($i<n$), so by the greedy admissibility $\gcd(a_n,a_i)>1$; pick a prime $r\mid\gcd(a_n,a_i)$. Since $p\nmid a_i$ while $p\mid a_n$, $r\neq p$; as $r\mid a_n=pc$ and $r$ is prime, $r\mid c\mid q^k c$. So $\gcd(q^k c,a_i)\ge r>1$. Hence $q^k c$ appears.

*Step 3 (index descent + rad-divisibility).* Let $\mathrm{idx}(q^k c)$ be the index of $q^k c$ in the sequence. Since $q^k c<a_n$ and the sequence is strictly increasing, $\mathrm{idx}(q^k c)<n$. For radicals: $q\mid c$ (Step 1) so $P(q^k c)=P(c)$, and $P(a_n)=P(pc)=P(c)\cup\{p\}$; hence $\mathrm{rad}(q^k c)=\mathrm{rad}(c)\mid\mathrm{rad}(pc)=\mathrm{rad}(a_n)$.

*Step 4 (conclude).* $\mathrm{idx}(q^k c)<n$ and $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$ give $a_{\mathrm{idx}(q^k c)}\prec a_n$. So $a_n$ is not $\prec$-minimal. Contrapositively, if $a_n$ is $\prec$-minimal then $a_n$ is $a_1^2$-smooth — extending (IH$_n$) to (IH$_{n+1}$). ∎

**Non-circularity.** The descent's only membership criterion is `appears-criterion-unconditional` (Piece A), which is unconditional. It does NOT invoke the GAP-conditional `universal-membership-no-transient` / `transversal-residue-characterization` (which define $L,V$ from $\mathcal M$ and would be circular inside a finiteness proof). The descent establishes $\mathcal M$ finite; the finish (`post-stabilization-theorem`) is conditional on $\mathcal M$ finite and is applied ONLY after.

*Source.* Approach `large-prime-descent` (§4), round 130, reproducing the published IMO 2026 P6 solution (Evan Chen's notes, 2026-07-23). Reviewer-certified: descent conclusion (all $\prec$-minimal terms $a_1^2$-smooth, in fact $\le a_1$) holds 0 violations across 9 seeds; the witness mechanism ($q^k c$ lands in $[a_1,a_n)$, rad-divides $\mathrm{rad}(a_n)$, appears earlier) verified on all 612 large-prime-carrying terms at $a_1=15$ and 264 at $a_1=30$.
