# proof-builder: growing-modulus-descent (round 2)

## Outcome: DEAD-END — retire (RETHINK candidate)

The `aimo-0678` min-of-a-set monovariant $w_n=\min\{q>M_1:q\in\bigcup\operatorname{MT}(\mathcal F_n)\}$ is **provably NON-MONOTONE in the real greedy sequence** — not only in the abstract hypergraph world the reviewer flagged. The "covered stays covered" mechanism is realized as FALSE by the greedy itself.

## The killing counterexample: $a_1=116=2^2\cdot 29$, $M_1=58$

The greedy steps by $2$: $a_n=2(57+n)$. Supports form a star $\{2\}\cup\operatorname{PF}(57+n)$. Tracking $\operatorname{MT}(\mathcal F_n)$:
- $n=1$: $\operatorname{MT}=\{\{2\},\{29\}\}$, $w_1=+\infty$.
- $n=2$: $a_2=118=2\cdot59$, $\operatorname{MT}=\{\{2\},\{29,59\}\}$, $w_2=59$. **Large prime $59>58=M_1$ enters MT.**
- $n=7$: $a_7=128=2^7$ (support $\{2\}$), $\operatorname{MT}=\{\{2\}\}$, $w_7=+\infty$ (lock).

So $w_n=(+\infty,59,59,59,59,59,+\infty)$: INCREASES from $+\infty$ to $59$, then DECREASES back to $+\infty$. Non-monotone under either convention for $+\infty$. The small covering $\{2\}$ is present at $n=1$, persists at $n=2$, survives to the lock — yet $59$ enters $\operatorname{MT}$ at $n=2$ via the new minimal transversal $\{29,59\}$. This is exactly the reviewer's abstract counterexample $\{\{1,2\},\{1,3\},\{2,3\}\}\to+\{1,100\}$, realized by the greedy.

## Systematic, not isolated

For every $a_1=p^e q$ ($p$ smallest prime factor, $e\ge 2$, $q>p$ prime), the greedy steps by $p$ (each $a_{n-1}+p$ is a $p$-multiple, hence admissible against the star family; no smaller step clears all constraints). Then $a_n=p(p^{e-1}q+n-1)$, supports $=\{p\}\cup\operatorname{PF}(p^{e-1}q+n-1)$. Any prime $r>M_1=pq$ dividing $a_n/p$ enters $\operatorname{MT}$ via the "all-other-primes" transversal. Confirmed computationally for $a_1\in\{68,76,92,116,148,164,172,188,212,63,117\}$ — every case has $w_n$ jumping $+\infty\to\text{finite}\to+\infty$.

## Alternative monovariants tested and killed

- **"Least multiplier" $m=a_i/p$** (dispatch suggestion): equals the large prime $r$ itself, strictly INCREASING across pull-in events ($a_1=68$: $37,41,43,47,53,59,61,67,71,73$; $a_1=116$: $59,61,67,71,73,79,83,89,97$). Ascends, never descends. Killed.
- **$P_1$-support-type count** (Phase 1 freeze): IS monotone (increasing, bounded by $2^{|P_1|}$, stabilizes) but only freezes the $P_1$-structure; does NOT bound large primes. After $\Sigma_n$ stabilizes, large primes still enter $\operatorname{MT}$ (the $a_1=116$ star family has $|P_1|=2$, $\Sigma$ stabilizes at $n=1$, yet $59$ enters at $n=2$). Insufficient.

## Why every non-vacuous case is a LOCK case

Every $a_1=p^e q$ case locks: the greedy steps by $p$ until $a_n/p=p^k$ (next power of $p$), at which point $a_n=p^{k+1}$ is a prime power and the certified `lock-lemma` applies ($T=1,L=p$). Lock indices: $a_1=116\to n=7$; $a_1=68\to n=31$; $a_1=92\to n=19$; $a_1=188\to n=35$; etc. The transient large primes (59, 61, ...) drop out of $\operatorname{MT}$ at the lock and are irrelevant — the governing primes are just $\{p\}$, all $\le M_1$.

For the non-LOCK starting values ($a_1\in\{385,77,715,2085,105,1001,\dots\}$), $w_n\equiv+\infty$ (vacuous — no large prime ever enters $\operatorname{MT}$). So the monovariant is either vacuous (non-LOCK) or non-monotone (LOCK). It never does useful work.

## Conclusion

The `aimo-0678` framing does not yield a provably-monotone quantity on the greedy sequence. The only viable path (minimal-criminal induction on the smallest governing prime $>M_1$) reduces to the `transversal-saturation` `aimo-0030` strip with the same load-bearing admissibility-transfer crux — a costume of the strip, not a rival framing.

**Recommend RETIRE next round** and ask the outliner for a genuinely-different framing (not a Gap-A monovariant variation).

## Promotable lemma proposed
"Monovariant non-monotonicity" — $w_n$ is provably non-monotone in the real greedy sequence (concrete witness $a_1=116$, structural family $a_1=p^e q$). For any approach tempted to use an MT-frontier monovariant, to rule it out. See `results/imo-2026-06/approaches/growing-modulus-descent.md`, Current best.

## File
`results/imo-2026-06/approaches/growing-modulus-descent.md` — updated in place. Status: partial (dead-end, RETHINK candidate).
