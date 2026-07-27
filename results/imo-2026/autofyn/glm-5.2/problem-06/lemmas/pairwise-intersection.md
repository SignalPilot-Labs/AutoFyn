# Lemma: pairwise-intersection

**Statement (unconditional).** For all $i,j\ge1$, $P(a_i)\cap P(a_j)\neq\emptyset$. Hence the family $\{P(a_i):i\ge1\}$ is pairwise intersecting, and every $a_n$'s support hits every member of $\mathcal M=\min\{P(a_i):i\ge1\}$.

**Proof.** Take $i\ne j$, WLOG $i<j$. When $a_j$ was chosen, the rule required $\gcd(a_j,a_i)>1$ (as $i\le j-1$), i.e. $P(a_j)\cap P(a_i)\neq\emptyset$. The case $i=j$ is trivial. Each $M\in\mathcal M$ equals $P(a_j)$ for some $j$ (minimal elements are members of the family), so $P(a_n)\cap M=P(a_n)\cap P(a_j)\neq\emptyset$. ∎

*Unconditional — no finiteness hypothesis. The load-bearing fact behind `universal-membership-no-transient`.*

**Source.** Approach `density-promotion-bound` (Lemma 1), round 1. Reviewer-certified.
