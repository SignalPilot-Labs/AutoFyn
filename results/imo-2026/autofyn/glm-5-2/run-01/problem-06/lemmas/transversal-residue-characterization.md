# Lemma: transversal-residue-characterization (free-rider invisibility)

**Hypothesis (GAP).** $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite. Let $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree), $V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ hits }\mathcal M\}$.

**Statement.** An integer $m>1$ satisfies $\gcd(m,a_i)>1$ for every $i\ge1$ iff $m\bmod L\in V$. In particular, admissibility against the entire past depends only on $m\bmod L$; primes $q\mid m$ with $q\notin P$ ("free-riders") are invisible to the hitting condition.

**Proof.** $\gcd(m,a_i)>1\ \forall i\iff P(m)\cap P(a_i)\neq\emptyset\ \forall i\iff P(m)$ is a transversal of $\mathcal F\iff P(m)$ is a transversal of $\mathcal M=\min\mathcal F$ (a set hits every member of $\mathcal F$ iff it hits every minimal member). Since each $M'\in\mathcal M$ lies in $2^P$ (as $\bigcup\mathcal M=P$), $P(m)\cap M'=(P(m)\cap P)\cap M'=\{p\in P:p\mid m\}\cap M'$. A prime $q\mid m$, $q\notin P$, lies in no $M'$, so it cannot help hit anything; transversality of $P(m)$ over $\mathcal M$ depends only on $\{p\in P:p\mid m\}$, which by CRT over squarefree $L$ depends only on $m\bmod L$. Hence iff $m\bmod L\in V$. ∎

*Conditional on GAP. Uses CRT (knowledge_base.md "Modular arithmetic, CRT") and $\bigcup\mathcal M=P$.*

**Source.** Approaches `transversal-single-cycle-finish` (Lemma 1), `density-promotion-bound` (Lemma 2 / §0), `bertrand-dickson-eviction` (Lemma 7). Reviewer-certified.
