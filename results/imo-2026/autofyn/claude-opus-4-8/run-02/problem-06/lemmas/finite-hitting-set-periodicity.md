# Certified lemma: finite hitting set ⇒ exact periodicity from n=1

Certified round 1 (proof-reviewer). This is the **periodicity machine** shared by
`admissible-set-periodicity` (Lemmas 4–6) and `essential-prime-counting` (Lemmas C–D).
Verified numerically (a1=15: L=30,T=8; a1=143: L=858,T=64; a1=1001: L=2002,T=282;
a1=858: L=2,T=1 — all reproduce the greedy sequence exactly from n=1).

Notation as in `enumeration-and-bounded-gaps.md`. For a finite prime set $S$ let
$A_S=\{x>1:\forall i\ \operatorname{supp}(x)\cap\operatorname{supp}(a_i)\cap S\ne\emptyset\}$.
Call $S$ a **hitting set** if every pair of terms shares a prime in $S$.

## Lemma (finite hitting set ⇒ exact periodicity)
If $S$ is a finite hitting set and $L=\prod_{p\in S}p$, then with $T=|A\cap[a_1,a_1+L)|\ge1$,
$$a_{n+T}=a_n+L\qquad\text{for every } n\ge 1.$$

*Proof.*
1. **$A\cap[a_1,\infty)=A_S\cap[a_1,\infty)$.** $A_S\subseteq A$ always. Conversely $x\in A$, $x\ge a_1$ is a term $a_k$ (Lemma 2); for each $i$ the hitting property on $\{a_k,a_i\}$ (or on $\{a_k,a_{k'}\}$, $k'\ne k$, when $i=k$) yields a prime of $S$ in $\operatorname{supp}(x)\cap\operatorname{supp}(a_i)$, so $x\in A_S$.
2. **$A_S$ is a union of residue classes mod $L$.** Whether $p\mid x$ ($p\in S$) depends only on $x\bmod L$ (as $L$ squarefree, $p\mid L$); membership in $A_S$ is a Boolean function of $\{p\in S:p\mid x\}$, hence of $x\bmod L$. So $x\in A_S\iff x+L\in A_S$.
3. **Exact periodicity of $E=A\cap[a_1,\infty)$.** By (1),(2): for $x\ge a_1$, $x\in E\iff x+L\in E$.
4. **Enumeration.** $\tau:x\mapsto x+L$ is an order-preserving bijection $E\to E\cap[a_1+L,\infty)$; the $T$ elements of $E\cap[a_1,a_1+L)$ are the $T$ smallest, so $e_{n+T}=e_n+L$. By Lemma 2, $e_n=a_n$. $\square$

**Reduction status.** This reduces the whole IMO 2026 P6 to: *there exists a finite hitting set*
(equivalently the min-common-prime set $\Pi=\{\min(\operatorname{supp}a_i\cap\operatorname{supp}a_j):i<j\}$ is finite —
$\Pi$ is automatically a hitting set). That finiteness (HS / MCL) remains **OPEN** as of round 1.
