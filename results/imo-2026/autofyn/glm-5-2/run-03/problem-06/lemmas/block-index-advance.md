# Lemma: block-index advance

**Statement.** Let $a_1,a_2,\dots$ be the greedy sequence, $P_1=S(a_1)$, $M_1=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$. Define the block index
$$b_n:=\left\lfloor\frac{a_n-a_1}{M_1}\right\rfloor\qquad(n\ge1,\ b_1=0).$$
Then $b_{n+1}-b_n\in\{0,1\}$ for every $n\ge1$.

**Proof.** Write $a_n-a_1=b_nM_1+r_n$ with $r_n\in\{0,\dots,M_1-1\}$. By the certified gap bound (`linchpin-and-gap-bound`), $0\le d_n:=a_{n+1}-a_n\le M_1$. Hence
$$a_{n+1}-a_1=(a_n-a_1)+d_n=b_nM_1+(r_n+d_n),\qquad 0\le r_n+d_n\le (M_1-1)+M_1=2M_1-1.$$
So $b_nM_1\le a_{n+1}-a_1\le b_nM_1+2M_1-1<(b_n+2)M_1$, which gives $b_{n+1}\in\{b_n,b_n+1\}$. $\square$

**Depends on.** `linchpin-and-gap-bound` (the gap bound $d_n\le M_1$) only.

**Status.** Reviewer-certified (round 3). Unconditional. Verified computationally for $a_1\in\{6,15,35,77,91,105,143,175,385,847,1309,2085,116,145\}$ — in every case $b_{n+1}-b_n\subseteq\{0,1\}$. Importable by any approach that wants a block decomposition of the orbit. (Note: the block index is a *trivial* consequence of the gap bound; it carries no greedy-specific structure beyond $d_n\le M_1$, and in particular does not by itself yield eventual periodicity.)
