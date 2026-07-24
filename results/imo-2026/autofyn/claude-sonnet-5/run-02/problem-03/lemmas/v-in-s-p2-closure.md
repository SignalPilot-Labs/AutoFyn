# Lemma: v-in-[s,p2) closure (Proposition 24)

**Source:** `approaches/greedy-halving-adversary.md`, round 10.

**Statement.** Fix $n\ge3$ and suppose the theorem's lower-bound direction
holds for $n-2$: $(\star_{n-2})$ (every legal Xiang-Yu response, $\le n-2$
cuts, to the $(n-2)$-ladder has $A\ge f(n-2)$). Let $F=\{v\}\cup P$ with
$\ell(F)=1$, $s\le v<p_2$ where $s:=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})$,
and let $G'=\{p_2\}\cup R'$ where $R'$ is any legal refinement of
$\{p_3,\dots,p_{n+1}\}$ using $\le n-2$ cuts. Then
$$A(F\cup G')\ \ge\ f(n)$$
(in fact the strict inequality $A(F\cup G')>f(n)$).

**Proof.** Since $p_2$ dominates $R'$ (`general-ladder-dominance`, $i=2$),
`dominant-element-removal-identity` gives $A(G')=p_2-A(R')$. Since $v<p_2$,
for every $x<v$, $p_2$ is counted in $N_{G'}(x)$, so
$v_{G'}(x)=1-u_{R'}(x)$ on $[0,v)$, giving
$\int_0^v v_{G'}=v-\int_0^v u_{R'}$. Since $v\ge s\ge\mathrm{Total}(R')$
(every element of $R'$ is $\le s$), $u_{R'}$'s entire support lies in
$[0,v)$, so $\int_0^v u_{R'}=A(R')$. By `cross-term-identity-threshold`
(truncated via `single-residual-indicator`'s indicator for $F$),
$$A(F\cup G')=v+A(G')-2\big(v-A(R')\big)=p_2-v+A(R').$$
By `tail-self-similarity` and the induction hypothesis $(\star_{n-2})$
applied to $R'/s$, $A(R')\ge s\cdot f(n-2)$; by the cross-level identity
(chaining `tail-self-similarity`'s constant at levels $n-1$ and $n$),
$s\cdot f(n-2)=f(n)$, so $A(R')\ge f(n)$. Since $v<p_2$,
$A(F\cup G')=p_2-v+A(R')\ge p_2-v+f(n)>f(n)$ (as $p_2-v>0$). $\blacksquare$

**Status.** Proved in full, conditional on $(\star_{n-2})$; unconditional
for $n\le4$ (since $(\star_0),(\star_1),(\star_2)$ are trivial or already
fully certified). Independently verified: $3000$ exact-`Fraction` random
trials per $n\in\{3,4,5,6\}$ with the cut budget on $R'$ correctly capped at
$n-2$, zero violations (script `check_prop24b.py`). An earlier uncapped
version of the check *did* find violations at $n=3,4$, confirming the
$\le n-2$ cut-budget hypothesis is load-bearing.

**Scope.** Closes the $v\in[s,p_2)$ sub-branch of the previously fully-open
$v<p_2$ case of restricted Claim (B), for $F$ with $\ell(F)=1$ and $G'$
leaving $p_2$ untouched. Does not cover $v<s$ (recurses into the same shape
of obstruction one level down) or any case where $G'$ cuts $p_2$.

**Certified by:** proof-reviewer, round 10 - independently re-verified (fresh exact-Fraction scripts, corrected for legal-refinement piece-boundary/cut-budget coupling): CERTIFIED.
