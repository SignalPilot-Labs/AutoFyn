# Lemma A — smallest-multiple structure of a large-prime witness

**Setting.** Greedy sequence as in the problem. $M_1=\operatorname{rad}(a_1)$. Suppose $q>M_1$ is a prime dividing $a_i$, and $q>M_1\ge d_{i-1}=a_i-a_{i-1}$ (the latter by the certified gap bound `linchpin-and-gap-bound`).

**Lemma A.** *$a_i$ is the smallest positive multiple of $q$ strictly greater than $a_{i-1}$; equivalently $a_i=q\lceil(a_{i-1}+1)/q\rceil$.*

*Proof.* The smallest multiple of $q$ strictly greater than $a_{i-1}$ is $\mu:=q\lceil(a_{i-1}+1)/q\rceil\in(a_{i-1},\,a_{i-1}+q]$. Since $a_i$ is a multiple of $q$ with $a_i>a_{i-1}$, $a_i\ge\mu$. By the gap bound $a_i-a_{i-1}=d_{i-1}\le M_1<q$, so $a_i\in(a_{i-1},\,a_{i-1}+q)$. The interval $(a_{i-1},\,a_{i-1}+q]$ has length $q$ and so contains exactly one multiple of $q$, namely $\mu$; as $a_i$ is a multiple of $q$ in this interval, $a_i=\mu$. ∎ *(Reviewer-verified, round 2.)*

**Corollary A1.** *$q\nmid a_{i-1}$.*

*Proof.* If $q\mid a_{i-1}$ and $q\mid a_i$, then $q\mid d_{i-1}\le M_1<q$, forcing $d_{i-1}=0$, contradicting $a_i>a_{i-1}$. ∎

**Corollary A2 (predecessor shares a small prime).** *Every prime shared between $a_{i-1}$ and $a_i$ is $\le M_1$ (is small, $\ne q$). In particular such a shared prime exists.*

*Proof.* By `pairwise-intersecting-supports`, $a_{i-1}$ and $a_i$ share a prime $t$. By A1, $q\nmid a_{i-1}$, so $t\ne q$. Now $t\mid a_i$ and $t\mid a_{i-1}$, so $t\mid d_{i-1}\le M_1$; as $t$ is prime and $t\mid d_{i-1}>0$, $t\le d_{i-1}\le M_1$. ∎

**Import.** Useful for any approach using the "witness $a_i$ is a multiple of a large prime $q>M_1$" structure: the witness is pinned to the *least* multiple of $q$ clearing $a_{i-1}$, and the predecessor never obstructs admissibility transfer (its shared prime is small).
