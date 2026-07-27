# Lemma: common-primes-bounded

**Statement (unconditional).** Let $C_n=\bigcap_{M\in\mathcal M_n}M$ be the set of common primes at time $n$ (primes present in every minimal support). Then $C_n\subseteq P(a_1)$ for every $n\ge1$: every common prime divides $a_1$.

**Proof.** $\mathcal M_n$ is the family of $\subseteq$-minimal members of $\mathcal F_n=\{P(a_1),\ldots,P(a_n)\}$. Since $P(a_1)\in\mathcal F_n$, the subfamily $\{S\in\mathcal F_n:S\subseteq P(a_1)\}$ is nonempty (contains $P(a_1)$); by well-foundedness of $\subseteq$ on the finite family $\mathcal F_n$, it contains a $\subseteq$-minimal element $M_1\in\mathcal M_n$ with $M_1\subseteq P(a_1)$. If $q\in C_n$, then $q\in M$ for every $M\in\mathcal M_n$, in particular $q\in M_1\subseteq P(a_1)$, so $q\mid a_1$. ∎

*Consequence: only factors of $a_1$ can ever be permanently common. This pins the case split (F)/(S) — freeze vs saturated — on the prime factors of $a_1$ alone. Verified 14 seeds (round 2).*

**Source.** Approach `density-promotion-bound` (Lemma 2), round 2. Reviewer-certified (extracted to file round 129).
