# Lemma: minimal-support-direction-b (Direction B)

**Setting.** The greedy gcd sequence. Let $\mathcal F=\{P(a_i):i\ge1\}$ be the family of term prime-supports and $\mathcal M=\min(\mathcal F)$ its $\subseteq$-minimal elements (the *minimal-support family*). Let $a_m\prec a_n\iff m<n\wedge P(a_m)\subseteq P(a_n)$; "$\prec$-minimal" as in `appears-criterion-unconditional`.

**Statement (Direction B; unconditional).** Every $M\in\mathcal M$ is the support $P(a_i)$ of some $\prec$-minimal term $a_i$. Equivalently $\mathcal M\subseteq\{P(a_i):a_i\text{ is $\prec$-minimal}\}$.

**Proof.** Let $M\in\mathcal M\subseteq\mathcal F$, so $M=P(a_j)$ for some $j$. Let $i$ be the *smallest* index with $P(a_i)=M$ (well-defined). Suppose $a_i$ is not $\prec$-minimal: then some $m<i$ has $a_m\prec a_i$, i.e. $P(a_m)\subseteq P(a_i)=M$. Since $M\in\mathcal M$ is $\subseteq$-minimal in $\mathcal F$ and $P(a_m)\in\mathcal F$ with $P(a_m)\subseteq M$, we must have $P(a_m)=M$, contradicting the minimality of $i$ (as $m<i$ also has support $M$). So $a_i$ is $\prec$-minimal, with $P(a_i)=M$. ∎

**Remark (Direction A is FALSE; not provable).** The reverse inclusion — every $\prec$-minimal support lies in $\mathcal M$ — is false in general: a later term can appear with a *strictly smaller* support, demoting an earlier $\prec$-minimal support out of $\mathcal M$. Verified violations at $a_1=30,429,273,210,46189,323,385$. The descent's transfer to $\mathcal M$ uses Direction B **only**.

*Source.* Approach `large-prime-descent` (§3), round 130. Reviewer-certified (Direction B holds 0 violations across 9 seeds).
