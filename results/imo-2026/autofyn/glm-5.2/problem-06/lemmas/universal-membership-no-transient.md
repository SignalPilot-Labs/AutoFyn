# Lemma: universal-membership-no-transient

**Hypothesis (GAP).** $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite. Let $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$, $V=\{r:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}$.

**Statement.** For every $n\ge1$, $a_n\bmod L\in V$; equivalently $P(a_n)$ is a transversal of $\mathcal M$. (No transient: the cyclic dynamics hold from $n=1$.)

**Proof.** Fix $M'\in\mathcal M$. Since $M'$ is minimal in $\mathcal F=\{P(a_i):i\ge1\}$, it is a member of $\mathcal F$: $M'=P(a_j)$ for some $j\ge1$. By trichotomy on $j$ vs $n$:
- $j<n$: $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}\ni a_j$, so $\gcd(a_n,a_j)>1$, i.e. $P(a_n)\cap M'\neq\emptyset$.
- $j>n$: $a_j$ was chosen admissible against $a_1,\ldots,a_{j-1}\ni a_n$, so $\gcd(a_j,a_n)>1$, i.e. $M'\cap P(a_n)\neq\emptyset$.
- $j=n$: $P(a_n)\cap M'=P(a_n)\neq\emptyset$ (as $a_n>1$).

So $P(a_n)$ meets every $M'\in\mathcal M$; by `transversal-residue-characterization`, $a_n\bmod L\in V$. ∎

*Conditional on GAP (only to define $L,V$); the pairwise-intersection property is unconditional. Verified on $a_1=15,429,30$.*

**Source.** Approaches `transversal-single-cycle-finish` (Lemma 2), `density-promotion-bound` (Lemma 1 corollary), `bertrand-dickson-eviction` (Lemma 8 part 1). Reviewer-certified.
