# Lemma: cov-monovariant (Cov monovariant)

**Statement (conditional on regime (S); unconditional within (S)).** Let $a_1$ have $\ge2$ distinct prime factors. In regime (S) (no factor of $a_1$ is permanently common), define the *coverage*
$$\mathrm{Cov}(\mathcal M_n):=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}\subseteq P(a_1).$$
Then:
1. $\mathrm{Cov}(\mathcal M_n)$ is monotone non-decreasing in $n$ (once $\{2,p\}\in\mathcal M_n$ for $p\in P(a_1)$, it persists: $\{2,p\}\in\mathcal M_m$ for all $m\ge n$).
2. $\mathrm{Cov}$ stabilizes after at most $|P(a_1)|$ $\{2,p\}$-crashes; the number of $\{2,p\}$-crashes (for $p\in P(a_1)$) is $\le|P(a_1)|$, and every such crash prime lies in $P(a_1)$.

**Proof.** *Refinement obstruction.* In regime (S), the member $\{2,p\}$ (for $p\in P(a_1)$) can never be refined away: a proper nonempty subset of the two-element set $\{2,p\}$ is $\{2\}$ or $\{p\}$; each is a singleton, so `singleton-freeze` would freeze $\mathcal M$ to $\{\{p\}\}$ from that time on, making that prime permanently common — contradicting regime (S). (When $2\notin P(a_1)$, $\{2\}$ is additionally excluded by `common-primes-bounded`.) By the refinement dynamics (a member is removed only when a proper subset appears as a new minimal), $\{2,p\}$ is never removed. This proves (1). For (2): $\mathrm{Cov}\subseteq P(a_1)$ is finite (size $\le|P(a_1)|$) and monotone non-decreasing, hence stabilizes (KB *Invariants & monovariants*); each increase is a distinct $\{2,p\}$-crash for a distinct $p\in P(a_1)$. ∎

*SPT-free and value-free: uses only the factorization of $a_1$ and the refinement obstruction (a $\subseteq$-structural fact about two-element sets), not any prime-value bound. Computationally verified: Cov monotone (0 violations) on 17 saturated seeds; crash primes $\subseteq P(a_1)$. NOTE: this bounds only $\{2,p\}$-crashes with $p\in P(a_1)$, NOT all crashes — straggler refinements and $\{2,p,q\}$-type core crashes (carrying free-rider primes $q\notin P(a_1)$) remain unbounded by this invariant.*

**Source.** Approach `pstar-core-straggler` (Lemma B), round 129. Reviewer-certified.
