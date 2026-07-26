# Dead-end record — the MT-frontier monovariant is NON-MONOTONE

**Dead-end record** (reviewer-verified, round 2). The `aimo-0678`-style "min-of-a-set" monovariant on the large-prime frontier is provably non-monotone in the real greedy sequence. Future rounds need not re-try MT-frontier monovariants.

**The monovariant.** $w_n:=\min\{q>M_1:q\in\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}T\}$, with $w_n=+\infty$ if the set is empty (no large prime in any minimal transversal at step $n$).

**Lemma (non-monotonicity).** *$w_n$ is NOT monotone in $n$.*

**Killing counterexample ($a_1=116=2^2\cdot29$, $M_1=58$).** The greedy sequence is $a_n=116+2(n-1)=2(57+n)$ (steps by $2$ throughout — every $a_n+2$ is a $2$-multiple sharing the factor $2$ with every prior even term, and $a_n+1$ is odd hence coprime to $a_n$). It locks at $a_7=128=2^7$ (a prime power → `lock-lemma` with $L=2$).

Tracking $\operatorname{MT}(\mathcal F_n)$ (reviewer brute-force, round 2):
- $n=1$: $\mathcal F_1=\{\{2,29\}\}$, $\operatorname{MT}=\{\{2\},\{29\}\}$; large primes $>58$: none $\Rightarrow w_1=+\infty$.
- $n=2$: $\mathcal F_2=\{\{2,29\},\{2,59\}\}$, $\operatorname{MT}=\{\{2\},\{29,59\}\}$; large prime $59>58$ $\Rightarrow w_2=59$.
- $n=3,\dots,6$: $59$ persists in $\operatorname{MT}$ (via transversals like $\{3,61,59,29\}$) $\Rightarrow w_n=59$.
- $n=7$: $a_7=128$ has support $\{2\}$ (singleton). $\{2\}$ alone hits every support (every term is a $2$-multiple), so $\operatorname{MT}=\{\{2\}\}$; large primes: none $\Rightarrow w_7=+\infty$.

Thus $w_n=(+\infty,59,59,59,59,59,+\infty,\dots)$ — under EITHER convention ($+\infty$=best or $+\infty$=worst) $w_n$ is not monotone. The small covering $\{2\}$ — the "covered stays covered" anchor — is present at $n=1$, persists at $n=2$, and survives to the lock, yet the large prime $59$ ENTERS $\operatorname{MT}$ at $n=2$ via the new minimal transversal $\{29,59\}$.

**Structural reason (systematic).** For every $a_1=p^e\cdot q$ with $p$ the smallest prime factor, $e\ge2$, $q>p$ prime, the greedy steps by $p$, $a_n=p\cdot(p^{e-1}q+n-1)$, supports form the star $\{p\}\cup\operatorname{PF}(p^{e-1}q+n-1)$. Whenever $p^{e-1}q+n-1$ is a prime $r>M_1=pq$, that prime $r$ enters $\operatorname{MT}$ via the "all-other-primes" transversal while the small covering $\{p\}$ persists — exactly the abstract "covered-stays-covered" failure, realized by the greedy. Confirmed computationally for $a_1\in\{68,76,92,116,148,164,172,188,212,\dots\}$.

**Crucially, every non-vacuous case is a LOCK case** ($a_7=128$ for $a_1=116$; $a_{31}=128$ for $a_1=68$; …) handled unconditionally by the certified `lock-lemma`. For the non-LOCK starting values tested in round 1 ($a_1\in\{385,77,715,2085,\dots\}$) the monovariant is VACUOUS: $w_n\equiv+\infty$ (no large prime ever enters $\operatorname{MT}$), so there is nothing to descend. The monovariant is either vacuous (non-LOCK) or non-monotone (LOCK) — it never does useful work.

**Conclusion.** No MT-frontier monovariant of this form tames the large-prime frontier on the greedy sequence. The `aimo-0678` min-of-a-set framing is a dead-end for this problem.
