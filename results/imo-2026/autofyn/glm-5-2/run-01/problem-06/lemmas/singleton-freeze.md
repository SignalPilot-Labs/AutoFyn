# Lemma: singleton-freeze

**Statement (unconditional).** If $\{p\}\in\mathcal M_n$ for some $n$ (a singleton minimal support appears), then $\mathcal M_m=\mathcal M_n$ for all $m\ge n$ (the minimal-support family is frozen from time $n$ on).

**Proof.** The singleton $\{p\}$ has no proper nonempty subset, so it can never be refined away: it remains in $\mathcal M_m$ for all $m\ge n$. For any future term $a_{m+1}$ ($m\ge n$), admissibility (Lemma 1 logic) forces $P(a_{m+1})$ to be a transversal of $\mathcal M_m$, hence to hit $\{p\}$, i.e. $p\in P(a_{m+1})$, i.e. $\{p\}\subseteq P(a_{m+1})$. Thus $P(a_{m+1})$ is dominated by $\{p\}$ and is not a new minimal. No new minimal is added after $n$, and no existing minimal is removed (removal requires a proper subset to appear, which would be a new minimal — impossible). So $\mathcal M$ is constant from $n$. ∎

*Unconditional. Example: $a_1=p^k$ gives $\mathcal M_1=\{\{p\}\}$ frozen, $L=p$, $T=1$.*

**Source.** Approach `bertrand-dickson-eviction` (Lemma 2), round 1. Reviewer-certified.
