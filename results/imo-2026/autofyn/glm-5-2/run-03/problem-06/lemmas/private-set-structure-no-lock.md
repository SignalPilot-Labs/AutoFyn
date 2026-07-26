# Lemma — private-set structure (NO-LOCK regime)

**Setting.** Greedy sequence in the NO-LOCK regime (no term $a_i$ is a prime power, so $|S(a_i)|\ge2$ for every $i$). $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$, $P_1=S(a_1)$, $M_1=\operatorname{rad}(a_1)$. By `linchpin-and-gap-bound`, $S(a_i)\cap P_1\ne\varnothing$ for every $i$.

**Lemma (private-set structure, no-lock).** *Let $T\in\operatorname{MT}(\mathcal F_n)$ and $t\in T$. By minimality of $T$ there is a set $F\in\mathcal F_n$ with $F\cap T=\{t\}$ (a private set of $t$). In the NO-LOCK regime $|F|\ge2$, so $F$ contains a prime $t'\ne t$ with $t'\notin T$. If moreover $t\notin P_1$, then the linchpin forces $F\cap P_1\ne\varnothing$, and since $F\cap T=\{t\}$ with $t\notin P_1$, one has $F\cap P_1\subseteq P_1\setminus T$. So every large (non-$P_1$) prime $t$ in a minimal transversal is witnessed by a term whose $P_1$-part sits inside $P_1\setminus T$, a subset of the fixed finite set $P_1$.*

*Proof.* Every clause is definitional except the linchpin invocation. ∎ *(Reviewer-verified, round 2.)*

**Import.** Bounds the *type* of a large transversal prime by a subset of $P_1$ (finitely many types). Importable for arguments that classify large transversal primes by their $P_1$-interaction pattern. (Bounding the *number* of large primes per type remains the open wall — this lemma does NOT close it.)
