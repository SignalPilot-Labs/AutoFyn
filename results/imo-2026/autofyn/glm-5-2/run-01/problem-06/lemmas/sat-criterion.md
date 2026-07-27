# Lemma: sat-criterion (self-blocking ⟹ frozen)

**Statement (unconditional).** Call $\mathcal M_n$ *self-blocking* if every transversal (hitting set) of $\mathcal M_n$ contains some member of $\mathcal M_n$ as a subset (equivalently, there is no *avoiding* transversal — no transversal that contains no member). If $\mathcal M_n$ is self-blocking, then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$ (the family is frozen from $n$ on; hence $\mathcal M=\mathcal M_n$ is finite).

**Proof.** By induction on $m\ge n$. Base $m=n$ trivial. Step: assume $\mathcal M_m=\mathcal M_n$ (hence self-blocking). Consider $a_{m+1}$. By admissibility, $P(a_{m+1})$ meets every $P(a_i)$ for $i\le m$, hence meets every member of $\mathcal F_m$, hence $P(a_{m+1})$ is a transversal of $\mathcal M_m$. By self-blocking, $P(a_{m+1})$ contains some $M\in\mathcal M_m$ as a subset, so $P(a_{m+1})$ is dominated by $M$ and is **not** a new minimal. No new minimal enters at step $m+1$; existing minimals cannot be removed (removal requires a proper-subset new minimal to appear). So $\mathcal M_{m+1}=\mathcal M_m=\mathcal M_n$. ∎

*A clean sufficient condition for finiteness: reaching ANY self-blocking configuration freezes the family. Importable as the terminal step of any saturated-regime argument. Verified (e.g. $a_1=35$ terminal $\{\{2,3,7\},\{2,5\},\{3,5\},\{5,7\}\}$ is self-blocking, frozen).*

**Source.** Approach `density-promotion-bound` (Lemma 7), round 2. Reviewer-certified (extracted to file round 129).
