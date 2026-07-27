# Lemma: star-straggler self-blocking

**Statement (unconditional).** Let $S$ be a nonempty finite set of primes with $2\notin S$. The family
$$\mathcal F_S\;:=\;\{S\}\cup\bigl\{\{2,p\}:p\in S\bigr\}$$
is *self-blocking*: every transversal (hitting set) $T$ of $\mathcal F_S$ contains some member of $\mathcal F_S$ as a subset.

**Proof.** Let $T$ be a transversal of $\mathcal F_S$. Split on whether $2\in T$.
- $2\in T$: to meet the member $S$ (which lacks $2$), $T$ must contain some $p\in S$; then $\{2,p\}\subseteq T$ and $\{2,p\}\in\mathcal F_S$.
- $2\notin T$: to meet each member $\{2,p\}$ (for every $p\in S$) without using $2$, $T$ must contain $p$ for every $p\in S$, i.e. $S\subseteq T$; and $S\in\mathcal F_S$.

Either way $T$ contains a member. ∎

*Consequence (with `Sat-criterion`): if at some time $n$ the minimal-support family equals $\mathcal F_S$ for some $S\subseteq P(a_1)\setminus\{2\}$ (in particular the "full star" for odd $a_1$, realized e.g. by $a_1\in\{15,77,91,105,1001\}$), then $\mathcal M$ is frozen and finite from $n$ on. This is a SUFFICIENT terminal, not necessary: actual greedy terminals may be richer self-blocking families (verified: $a_1=35,175,323,385,4199$ terminate self-blocking with $\mathrm{Cov}\subsetneq P(a_1)$, not of the star+straggler form).*

**Source.** Approach `pstar-core-straggler` (Lemma D), round 129. Reviewer-certified.
