# Lemma: Every term lies in $\mathcal B_\infty$ (pure-from-start foundation)

**Statement.** Define $\mathcal B_n:=\{m\in\mathbb Z_{>0}:\gcd(m,a_i)>1\ \forall i\le n\}$ (the admissible set at step $n$) and $\mathcal B_\infty:=\bigcap_{n\ge1}\mathcal B_n$. Then for every $k\ge1$, $a_k\in\mathcal B_\infty$.

Equivalently: $S(a_k)$ meets $S(a_i)$ for every $i\ge1$.

**Proof.** $\mathcal B_\infty=\{m:S(m)\text{ meets every }S(a_i),\,i\ge1\}$. Fix $k$. For $i\ne k$, the pairwise-intersecting-supports lemma gives $S(a_k)\cap S(a_i)\ne\varnothing$. For $i=k$, $S(a_k)\cap S(a_i)=S(a_k)\ne\varnothing$ since $a_k>1$. Thus $S(a_k)$ meets every $S(a_i)$, i.e. $a_k\in\mathcal B_\infty$. $\square$

(Depends on: pairwise-intersecting-supports.)

**Status.** Reviewer-certified (round 1). Unconditional. Verified computationally for $a_1=385$ over 700 terms (every term lies in the stabilized admissible set $\mathcal B_{38}$). Importable by any approach.
