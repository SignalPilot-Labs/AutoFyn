# Lemma: Single-residual exact peel identity (Proposition 20)

**Source:** `approaches/greedy-halving-adversary.md`, round 9.

**Statement.** Fix $n\ge2$, the $n$-ladder $p_1,\dots,p_{n+1}$, and let
$F=\{v\}\cup P$ have $\ell(F)=1$ as in `single-residual-indicator`
($v\in(0,p_1]$, $P$ pairs up exactly). Let $G'$ be *any* legal refinement
of the tail $\tau=\{p_2,\dots,p_{n+1}\}$ (any number of cuts, any pattern),
with $\mathrm{Total}(G')=r=1-p_1$. If $v\ge p_2$, then
$$A(F\cup G') = v - A(G')\qquad\text{exactly.}$$

**Proof.** By `cross-term-identity-threshold`,
$A(F\cup G')=A(F)+A(G')-2\int_0^r u_F v_{G'}\,dx$. By
`single-residual-indicator`, $A(F)=v$, $u_F(x)=\mathbb1[x<v]$, so
$\int_0^r u_F v_{G'} = \int_0^{\min(v,r)} v_{G'}$. Since $r\ge p_2$
(the tail's total includes $p_2$ itself) and $v\ge p_2$,
$\min(v,r)\ge p_2$. By `safe-window-lemma`, every element of $G'$ is
$\le p_2$, so $v_{G'}\equiv0$ on $[p_2,\infty)$; hence
$\int_0^{\min(v,r)}v_{G'} = \int_0^{p_2}v_{G'} = A(G')$ (the last equality
because $A(G')$'s defining integral is entirely supported on $[0,p_2)$).
Substituting, $A(F\cup G')=v+A(G')-2A(G')=v-A(G')$. $\blacksquare$

**Status.** Proved in full, unconditionally, for every $n\ge2$, every legal
$F$ with $\ell(F)=1$ and $v\ge p_2$, every legal tail refinement $G'$.
Strictly generalizes `untouched-top-piece-lower-bound`/Lemma 6's identity
(recovered at $v=p_1$) to the whole range $v\in[p_2,p_1]$. Independently
re-verified by the reviewer with an exact-`Fraction` script (300 random
trials per $n\in\{2,3,4,5\}$, random $v\in[p_2,p_1]$ and random tail
refinements with up to $n-2$ cuts), zero mismatches.

**Note (correction of a related outline claim).** A separate, weaker
"$\int_0^{p_2}v_{G'}\le p_2/2$" bound proposed in the round-9 outline as a
route to closing this case was checked and found **false** in general (at
$n=3$, the untouched-tail value already exceeds $p_2/2$). This exact
identity, not that bound, is the correct tool; it is unaffected by that
finding.

**Certified by:** proof-reviewer, round 9.
