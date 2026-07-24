## Band-Parity Fact

**Source:** `approaches/greedy-halving-adversary.md`, round 21.
**Status:** CERTIFIED (proof-reviewer, round 21). General, fully proved,
no ladder structure or legality assumption needed.

### Statement

Let $S=\{r_1\ge r_2\ge\dots\ge r_k\ge0\}$ be a finite multiset sorted
descending (with multiplicity; ties permitted), with conventions
$r_0:=+\infty$, $r_{k+1}:=0$. For $v\ge0$ write $N_S(v):=|S_{>v}|$
(strict-$>$ convention) and $\epsilon(v):=\mathbb1[N_S(v)\text{ odd}]$.
Then for every $j\in\{0,1,\dots,k\}$ and every $v$ in the half-open band
$[r_{j+1},r_j)$ (empty if $r_{j+1}=r_j$), $N_S(v)=j$ exactly, hence
$\epsilon(v)=\mathbb1[j\text{ odd}]$.

### Corollary (parity flip under prepending a dominant element)

If $M\ge\max(S)$ and $v<M$, then $N_{\{M\}\cup S}(v)=1+N_S(v)$, so
$\epsilon_{\{M\}\cup S}(v)=1-\epsilon_S(v)$.

### Proof

Fix $j$ and $v\in[r_{j+1},r_j)$. Since $r_1\ge\dots\ge r_j>v$ (each
$r_i\ge r_j>v$ for $i\le j$), all $j$ indices $1,\dots,j$ contribute to
$S_{>v}$. For $i>j$, $r_i\le r_{j+1}\le v$, so none contribute. Hence
$N_S(v)=j$ exactly, for every $v$ in the stated band; the $j=0$ and $j=k$
boundary extremes (both $k$-even and $k$-odd) are covered by the same
argument. For the corollary: sorting $\{M\}\cup S$ descending places $M$
first (since $M\ge\max(S)$), so its band structure is $S$'s own band
structure with every index shifted up by 1; applying the Fact to both $S$
and $\{M\}\cup S$ gives $N_{\{M\}\cup S}(v)=1+N_S(v)$ for $v<M$, and
consecutive integers have opposite parity. $\blacksquare$

### Verification

Proof-reviewer independently re-derived and confirmed both the Fact and
its corollary by hand (elementary sorted-order argument, two paragraphs).
Used downstream in Theorem 35a$'$ (`greedy-halving-adversary`) and §7.5.0$'$
(`rank-pigeonhole-budget`) — both downstream uses independently
cross-checked by the reviewer via exact-`Fraction` scripts, consistent
with this lemma's statement.

### Scope note

This lemma is purely combinatorial (sorted-multiset truncation counting)
and carries no dependency on the ladder construction, game legality, or
any other problem-specific structure — safe to reuse in any future context
needing the parity of a truncation count.
