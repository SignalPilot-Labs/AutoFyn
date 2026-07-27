# Lemma: two-q GAP-3 obstruction

**Statement (unconditional).** Fix any $p^*\ge2$. The family
$$\mathcal F_q\;:=\;\bigl\{\{2,q\}:q>p^*,\ q\text{ prime}\bigr\}$$
is an infinite pairwise-intersecting antichain of nonempty finite prime-sets, every member of which satisfies $\min M\le p^*$ (the SPT property), with unbounded essential-prime set $\bigcup\mathcal F_q=\{2\}\cup\{q:q>p^*\text{ prime}\}$.

**Proof.**
- *Pairwise-intersecting:* $\{2,q_i\}\cap\{2,q_j\}=\{2\}\neq\emptyset$ for $i\neq j$.
- *Antichain:* $\{2,q_i\}\not\subseteq\{2,q_j\}$ for $i\neq j$ (as $q_i\neq q_j$); the only proper nonempty subsets $\{2\},\{q_i\}$ are not in the family.
- *SPT:* $\min\{2,q\}=2\le p^*$ for every member.
- *Unbounded $P_{\mathrm{ess}}$:* $\bigcup\mathcal F_q=\{2\}\cup\{q:q>p^*\text{ prime}\}$, unbounded (infinitely many primes $>p^*$). ∎

*Consequence (the obstruction): SPT ("every minimal has a prime $\le p^*$") bounds $\mathrm{mtp}$ (closes GAP-1, since $S=P_{\mathrm{ess}}\cap\{p\le p^*\}$ is a transversal of product $\le\mathrm{primorial}(p^*)$) but does NOT bound $P_{\mathrm{ess}}$ (does NOT close GAP-3 / GAP-S). A pairwise-intersecting antichain all containing a small prime from a bounded set can still be infinite. Hence the wall (finiteness of $\mathcal M$) requires an additional mechanism beyond SPT — a crash-eviction / Cov-monovariant step. NOTE: this is an ABSTRACT obstruction showing SPT alone does not logically force finiteness; it is not claimed to arise from the greedy dynamics.*

**Source.** Approach `density-promotion-bound` (Lemma 9), round 129. Reviewer-certified.
