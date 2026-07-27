# Lemma: greedy-equals-cyclic-successor

**Hypothesis (GAP).** $\mathcal M=\min\{P(a_i):i\ge1\}$ finite; $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$, $V=\{r:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}$. Let $\varphi:V\to V$ be the cyclic successor: $\varphi(r)=\min\{v\in V:v>r\}$ if nonempty, else $\min V$ (wrap).

**Statement.** For every $n\ge1$,
$$a_{n+1}=\min\{m>a_n:m\bmod L\in V\},\qquad r_{n+1}=\varphi(r_n)$$
where $r_n=a_n\bmod L\in V$. Corollary: $a_{n+1}-a_n\le L$ (the next multiple of $L$ above $a_n$ has residue $0\in V$).

**Proof.** Let $V_n=\{m:P(m)\text{ hits }\mathcal M_n\}$ be the time-$n$ valid set; $a_{n+1}=\min\{m\in V_n:m>a_n\}$.
- $V\subseteq V_n$: hitting $\mathcal M$ (final) implies hitting $\mathcal M_n$. Take $M'\in\mathcal M_n$. In $\mathcal F$, either $M'$ stays minimal (so $M'\in\mathcal M$, hit) or some $M\in\mathcal M$ has $M\subsetneq M'$; hitting $M$ hits $M'$. So $\min(V_n\cap(a_n,\infty))\le\min(V\cap(a_n,\infty))$, i.e. $a_{n+1}\le\min\{m>a_n:m\bmod L\in V\}$.
- By `universal-membership-no-transient`, $a_{n+1}\bmod L\in V$ and $a_{n+1}>a_n$, so $a_{n+1}\ge\min\{m>a_n:m\bmod L\in V\}$.

Equality. The smallest $m>a_n$ with $m\bmod L\in V$ is the cyclic successor of $r_n$ in the natural order (next $V$-element in the current block, or wrap to $0$ in the next block). ∎

*Conditional on GAP. Verified on $a_1=15,429$.*

**Source.** Approaches `transversal-single-cycle-finish` (Lemma 3), `density-promotion-bound` (Lemma 3), `bertrand-dickson-eviction` (Lemma 8 part 2). Reviewer-certified.
