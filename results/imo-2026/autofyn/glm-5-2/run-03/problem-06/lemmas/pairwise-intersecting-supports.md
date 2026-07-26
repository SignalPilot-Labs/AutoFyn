# Lemma: Pairwise-intersecting prime-support family

**Statement.** Let $S(m)$ denote the set of prime divisors of $m$. For the sequence $(a_n)$ of the problem, the family $\mathcal F_n:=\{S(a_1),\dots,S(a_n)\}$ is pairwise-intersecting: for all $i,j\le n$, $S(a_i)\cap S(a_j)\ne\varnothing$.

**Proof.** For $i<j$, the term $a_j$ was chosen admissible at step $j-1$, so in particular $\gcd(a_j,a_i)>1$, i.e. $S(a_i)\cap S(a_j)\ne\varnothing$. $\square$

**Status.** Reviewer-certified (round 1). Unconditional. Importable by any approach.
