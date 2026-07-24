# Lemma: Budget reduction of the $\ell(F)=1$, $v\ge p_2$ sub-case (Proposition 21)

**Source:** `approaches/greedy-halving-adversary.md`, round 9.

**Statement.** In the setting of `single-residual-exact-peel-identity`,
suppose $F$ (with $\ell(F)=1$) uses $c$ cuts on $p_1$, so $G'$ uses at most
$n-c$ cuts on the tail. If $v<p_1$ (i.e. $F\ne\{p_1\}$), then a minimal-cut
count argument forces $c\ge2$ (a single cut on $p_1$ produces exactly two
fragments, which are either equal — the $\ell(F)=0$ case — or unequal
singletons — $\ell(F)=2$, not $1$), so $G'$ uses at most $n-2$ cuts.
Consequently, to prove $A(F\cup G')\ge f(n)$ (with $f(n):=1/(2^{n+1}-1)$,
so the target $a_n=2^nf(n)=p_1$) for every legal $F$ with $\ell(F)=1$,
$v\ge p_2$, and every legal $G'$, it suffices to prove
$$(\dagger)\qquad \max\{A(G') : G'\text{ legal refinement of }\tau,\
\le n-2\text{ cuts}\}\ \le\ p_2-f(n).$$

**Proof of sufficiency.** By `single-residual-exact-peel-identity`,
$A(F\cup G')=v-A(G')$. If $(\dagger)$ holds, $A(G')\le p_2-f(n)\le v-f(n)$
(using $v\ge p_2$), so $A(F\cup G')\ge v-(v-f(n))=f(n)$, for every such $v$
simultaneously (the bound only depends on $A(G')\le p_2-f(n)$, evaluated
at the smallest relevant $v=p_2$). The remaining case $F=\{p_1\}$
($c=0$, $\ell(F)=1$ degenerately with $P=\varnothing$, $v=p_1$) is already
settled unconditionally by `untouched-top-piece-lower-bound` without
appeal to $(\dagger)$ (its true tail budget is $n$, not $n-2$, so
$(\dagger)$ does not transfer to it — but no gap arises since it needs no
help from $(\dagger)$). $\blacksquare$

**Status.** Proved in full, unconditionally, general $n\ge2$. Reduces the
entire $v\ge p_2$ sub-case of $\ell(F)=1$ to the single statement
$(\dagger)$. Elementary case-count/monotonicity argument, independently
checked by the reviewer for logical validity (algebra is straightforward
once `single-residual-exact-peel-identity` is granted).

**Certified by:** proof-reviewer, round 9.
