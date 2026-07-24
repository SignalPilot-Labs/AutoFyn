# Cross-Term Vanishing Lemma

**Certified:** round 8, from `greedy-halving-adversary.md` Lemma 18.
Reviewer independently re-verified with a fresh 3000-trial exact-`Fraction`
script (`/tmp/round-8/verify_greedy.py`, built independently of the
approach's own script): zero mismatches.

**Statement.** Let $F$ be any **fully-paired** partition of $p_1$ (the
$n$-ladder, $n\ge2$): $F=\{a_1,a_1,\dots,a_t,a_t\}$, $t\ge1$, $2\sum a_i=p_1$
(so $A(F)=0$ by the degenerate case of `leftover-formula`). Then for
**every** legal refinement $G'$ of the tail $\tau=\{p_2,\dots,p_{n+1}\}$
(any number of cuts, any pattern):
$$A(F\cup G')\ =\ A(G')\qquad\text{exactly}.$$

**Proof sketch.** Show every pair-value $a_i\le p_2$ (with equality only if
$t=1$, the symmetric bisection). This forces the odd-parity indicator
$u_F(x)\equiv0$ for $x\in[0,p_2)$ (each pair contributes $0$ or $2$ to the
count there). By `safe-window-lemma.md`, every element of $G'$ is $\le p_2$,
so $v_{G'}(x)\equiv0$ for $x\ge p_2$. Applying the certified
`cross-term-identity-threshold` at threshold $r=\mathrm{Total}(G')$ and
splitting the cross-term integral at $p_2$: both halves vanish (one because
$u_F\equiv0$ there, the other because $v_{G'}\equiv0$ there), so the cross
term is $0$ and $A(F\cup G')=A(F)+A(G')-0=A(G')$.

**Depends on:** `safe-window-lemma.md`, `cross-term-identity-threshold`,
`leftover-formula`.

**Scope.** Requires $F$ fully-paired (an even multiplicity structure with
$A(F)=0$); does **not** cover a general $F$ with an unpaired residual — in
particular does not cover Claim (A)'s own optimal witness $F^\ast$ (which is
not fully-paired and additionally uses the entire cut budget, so no tail
refinement is even legal there — see `claim-a-full-closure.md`). Combined
with `tail-self-similarity` this gives Proposition 16 in
`greedy-halving-adversary.md` (conditional on the same lower bound one level
down, unconditional only for $n\le3$) — Proposition 16 itself is NOT
certified here, only this lemma, since Proposition 16 is conditional.
