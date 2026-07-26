# Lemma: Cyclic-successor bijection ⇒ periodicity

**Statement.** Suppose $\mathcal B_\infty=\bigcap_n\mathcal B_n$ is $L$-periodic for some finite $L$ (i.e. $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$). Set $A:=\{r\in\mathbb Z/L\mathbb Z:\text{the residue class }r\text{ lies in }\mathcal B_\infty\}$. Then:

(i) The cyclic-successor map $f:A\to A$, $f(r)=$ the smallest element of $A$ strictly after $r$ in the cyclic order on $\mathbb Z/L\mathbb Z$, is a bijection; in fact it is a single $|A|$-cycle.

(ii) Consequently, if the greedy rule equals the cyclic successor in $\mathcal B_\infty$ from $n=1$ (see the lemma "greedy-equals-cyclic-successor"), then with $T:=|A|$ and $L$ the period, $a_{n+T}=a_n+L$ for every $n\ge1$.

**Proof.** (i) $A\ne\varnothing$ (e.g. $a_1\bmod L\in A$ by the every-term-in-$\mathcal B_\infty$ lemma). The cyclic predecessor $g(r):=$ the greatest element of $A$ strictly before $r$ cyclically is a well-defined two-sided inverse of $f$ (for $|A|=1$ both are the identity; for $|A|\ge2$ immediate from the cyclic order). Hence $f$ is a bijection. Starting at any $r\in A$ and iterating $f$ walks once around the circle through all of $A$, returning to $r$ after exactly $|A|$ steps: $f$ is a single $|A|$-cycle.

(ii) By the greedy-equals-cyclic-successor lemma, $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$. By $L$-periodicity the increment $d_n:=a_{n+1}-a_n$ depends only on $r_n=a_n\bmod L$: it is the cyclic gap from $r_n$ to $f(r_n)$. Summing over one full period $n,n+1,\dots,n+T-1$ (with $T=|A|$), the orbit traverses every point of $A$ once, so the sum of cyclic gaps equals the circumference $L$. Thus $\sum_{k=0}^{T-1}d_{n+k}=L$, i.e. $a_{n+T}-a_n=L$, for every $n\ge1$. $\square$

**Status.** Reviewer-certified (round 1). Conditional on $\mathcal B_\infty$ being $L$-periodic (the open "Gap A"). Importable by any approach that closes Gap A. Verified computationally for $a_1=385$: $L=43890$, $|A|=T=5088$, and the cyclic successor predicts $a_{n+1}\bmod L$ for all 600 terms tested (zero mismatches).
