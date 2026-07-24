# Lemma: p2-cut-complement branch closure (Proposition 25)

**Source:** `approaches/greedy-halving-adversary.md`, round 10.

**Statement.** Fix $n\ge3$. Let $G'$ be a legal refinement of the tail
$\tau=\{p_2,\dots,p_{n+1}\}$ of the shape $G'=\{w'\}\cup P_2\cup\{p_3\}\cup
R'''$, where $\{w'\}\cup P_2$ is a split of $p_2$ with $\ell=1$ (in the
sense of `single-residual-indicator`: $P_2$ pairs up exactly, $w'\in(0,p_2)$
the residual), $p_3$ is left completely untouched, and $R'''$ is any legal
refinement of $\{p_4,\dots,p_{n+1}\}$ whatsoever. If $w'\ge p_3$, then
$$A(G') \ \le\ p_2-f(n) \qquad\text{unconditionally (no induction
hypothesis needed).}$$

Consequently, combined with `v-geq-p2-budget-reduction`'s exact identity
$A(F\cup G')=v-A(G')$ (valid for every $F=\{v\}\cup P$ with $\ell(F)=1$,
$v\ge p_2$): for every such $F$ and every $G'$ of the above shape,
$A(F\cup G')\ge f(n)$.

**Proof.** Write $F_2:=\{w'\}\cup P_2$, $R'':=\{p_3\}\cup R'''$
(total $s=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})$). By
`single-residual-indicator`, $u_{F_2}(x)=\mathbb1[x<w']$, $A(F_2)=w'$. Apply
`cross-term-identity-threshold` to $F_2,R''$ at threshold $s$:
$$A(G')=w'+A(R'')-2\int_0^{\min(w',s)}v_{R''}(x)\,dx.$$
By `safe-window-lemma`'s proof technique applied to the base set
$\{p_3,\dots,p_{n+1}\}$ instead of $\{p_2,\dots,p_{n+1}\}$, every element of
$R''$ is $\le p_3$, so $v_{R''}\equiv0$ for $x\ge p_3$. Since $w'\ge p_3$
and $s\ge p_3$, $\min(w',s)\ge p_3$, so the interaction integral truncates
exactly to $A(R'')$ (the full defining integral of $A(R'')$, since
$v_{R''}$ vanishes past $p_3$). Hence $A(G')=w'-A(R'')$.

By `general-ladder-dominance` ($i=3$), $p_3>\mathrm{Total}(\{p_4,\dots,
p_{n+1}\})=:s_2$, so $p_3$ dominates $R'''$ in $R''=\{p_3\}\cup R'''$; by
`dominant-element-removal-identity` (Lemma 7), $A(R'')=p_3-A(R''')$. So
$A(G')=w'-p_3+A(R''')$. By the certified integral-alternating-sum-formula
bound $A(R''')\le\mathrm{Total}(R''')=s_2=s-p_3$ (no induction hypothesis),
$$A(G')\le w'-p_3+(s-p_3)=w'-2p_3+s=w'-p_2+s$$
(using $p_2=2p_3$, `general-ladder-dominance`). Since $w'<p_2$
(`single-residual-indicator`'s cut-count fact applied to $p_2$ in place of
$p_1$), $A(G')<s=p_2-f(n)$ (`level-2-dominance-identity`), giving the
(strict) claimed bound. $\blacksquare$

**Status.** Proved in full, unconditionally, for every $n\ge3$. Independently
verified: $3000$ exact-`Fraction` random trials per $n\in\{3,4,5,6\}$
(script `check_prop25.py`), zero violations.

**Scope.** Closes exactly the branch of `v-geq-p2-budget-reduction`'s open
bound $(\dagger)$ where the tail's own top piece $p_2$ is cut with an
$\ell=1$ split whose residual $w'$ is at least the tail's second-largest
piece $p_3$, and $p_3$ itself is left uncut. Does not cover $w'<p_3$
(recurses one level down into an unresolved sub-case), $p_3$ itself cut
(recurses into the same shape of problem one level down again), or the
induced split of $p_2$ having $\ell\ge2$.

**Certified by:** proof-reviewer, round 10 - independently re-verified (fresh exact-Fraction scripts, corrected for legal-refinement piece-boundary/cut-budget coupling): CERTIFIED.
