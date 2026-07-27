# Lemma: freeze-lock

**Statement (unconditional).** Let $p$ be a prime. Let $\mathcal M_n=\min_{\subseteq}\{P(a_1),\ldots,P(a_n)\}$ and $C_n=\bigcap_{M\in\mathcal M_n}M$ (the common primes at time $n$). Suppose $p\mid a_n$ and $p\in C_n$ ($p$ is common in $\mathcal M_n$). Then:

$$p\in C_{n+1}\ \Longrightarrow\ a_{n+1}=a_n+p.$$

In other words, **the greedy locks to difference $p$ whenever $p$ is a persistent common prime**: if $p\in C_n$ for every $n\ge1$ and $p\mid a_1$, then by induction $a_{n+1}=a_n+p$ for every $n\ge1$.

**Proof.** Since $p\in C_n$, every $M\in\mathcal M_n$ contains $p$; hence the singleton $\{p\}$ is a transversal of $\mathcal M_n$ (it meets every member). Therefore every multiple of $p$ lies in the valid set $V_n=\{m:P(m)\text{ hits }\mathcal M_n\}$, because $p\in P(m)\supseteq\{p\}$. In particular $a_n+p$ (the next multiple of $p$ above $a_n$, using $p\mid a_n$) is valid, so the greedy choice satisfies $a_{n+1}\le a_n+p$.

Assume for contradiction $a_{n+1}<a_n+p$. Then $a_{n+1}\in\{a_n+1,\ldots,a_n+p-1\}$. Because $a_n\equiv0\pmod p$ and $a_n+p\equiv0\pmod p$, every integer strictly between them is not divisible by $p$; so $p\nmid a_{n+1}$, i.e. $p\notin P(a_{n+1})$.

By admissibility, $P(a_{n+1})$ meets every $P(a_i)$, $i\le n$, hence meets every member of $\mathcal F_n=\{P(a_1),\ldots,P(a_n)\}$, hence is a transversal of $\mathcal M_n$ (a set hits every member of $\mathcal F_n$ iff it hits every minimal member). We claim $P(a_{n+1})$ is a **new** minimal in $\mathcal F_{n+1}=\mathcal F_n\cup\{P(a_{n+1})\}$:

- No $M\in\mathcal M_n$ is a subset of $P(a_{n+1})$: every such $M$ contains $p$ (as $p\in C_n$), but $p\notin P(a_{n+1})$, so $M\not\subseteq P(a_{n+1})$.
- No non-minimal $P(a_j)\in\mathcal F_n$ is a subset of $P(a_{n+1})$ either: if $P(a_j)\subsetneq P(a_{n+1})$, take the $\subseteq$-minimal member $\widetilde M\in\mathcal M_n$ with $\widetilde M\subseteq P(a_j)$ (exists by well-foundedness of $\subseteq$ on the finite family $\mathcal F_n$, since $\{S\in\mathcal F_n:S\subseteq P(a_j)\}$ is nonempty, containing $P(a_j)$). Then $\widetilde M\subseteq P(a_j)\subsetneq P(a_{n+1})$, contradicting the previous bullet.
- The only remaining element of $\mathcal F_{n+1}$ is $P(a_{n+1})$ itself.

So $P(a_{n+1})$ is minimal in $\mathcal F_{n+1}$, i.e. $P(a_{n+1})\in\mathcal M_{n+1}$. But $p\notin P(a_{n+1})$, so $P(a_{n+1})$ is a member of $\mathcal M_{n+1}$ not containing $p$ — contradicting $p\in C_{n+1}$.

The contradiction forces $a_{n+1}=a_n+p$. ∎

*Unconditional — uses only the greedy rule and the definition of $\mathcal M_n$. The contrapositive is the load-bearing half: if the lock breaks ($a_{n+1}\in(a_n,a_n+p)$), then $p$ ceases to be common (a new minimal not containing $p$ enters). **Note (reviewer, round 2):** only the forward direction "persistence $\Rightarrow$ lock" (and its contrapositive "lock-broken $\Rightarrow$ not-persistent") is proved here — these are a single implication, NOT a logical equivalence. The backward direction "lock $\Rightarrow$ persistence" ($a_{n+1}=a_n+p \Rightarrow p\in C_{n+1}$) is NOT proved and is not used by any importing argument (the freeze-regime induction supplies persistence as a hypothesis). No product bound on non-$p$ transversals is required for the proved direction.*

**Source.** Approach `density-promotion-bound` (round 2). Reviewer-certification pending.
