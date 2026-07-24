## Statement

Fix $n\ge2$ and the $n$-ladder. Suppose Xiang Yu spends exactly one cut on
$p_1$, splitting it into fragments $x\ge p_1-x>0$, and spends his remaining
$\le n-1$ cuts on the tail $T=\{p_2,\dots,p_{n+1}\}$ arbitrarily, producing
$G'$ with $\mathrm{Total}(G')=r=1-p_1$. Write $\Delta:=2x-p_1\ge0$ and
$W:=[p_1-x,x)$ (length $\Delta$). Then
$$A(\{x,p_1-x\}\cup G') = \Delta + A(G') - 2\int_{W\cap[0,r)}v(t)\,dt,\qquad
v(t):=\mathbb1[N_{G'}(t)\text{ odd}].$$
Consequently, assuming the inductive hypothesis $(\star_{n-1})$ (every legal
Xiang Yu response to the $(n-1)$-ladder gives $A\ge f(n-1)$) so that (via
`tail-self-similarity`) $A(G')\ge f(n)$ unconditionally,
$$A(\{x,p_1-x\}\cup G')\ge f(n) \text{ is implied by } (\star\star):\quad
\int_{W\cap[0,r)}v(t)\,dt\le\Delta/2.$$
At $\Delta=0$ (symmetric split) $(\star\star)$ is vacuous, recovering
`symmetric-split-c1-lower-bound` as the special case $\Delta=0$.

## Proof

Direct application of `cross-term-identity-threshold` to $F=\{x,p_1-x\}$
and $G'$ at threshold $r$, combined with the elementary computation that
$F$'s odd-parity indicator is $\mathbb1_W$ (for $t<p_1-x$ both fragments
exceed $t$: even; for $p_1-x\le t<x$ only $x$ exceeds $t$: odd; for $t\ge x$
neither: even), so $A(F)=\Delta$ and $\int_0^r u\,v=\int_{W\cap[0,r)}v$. The
implication follows by substituting $A(G')\ge f(n)$ into the identity.

## Verification (proof-reviewer, round 5)

Independently re-derived the window-formula proof and cross-checked the
full identity by exact-`Fraction` computation (20 random trials at $n=3$,
random asymmetric $x$ and random single-piece tail splits): zero mismatches
between the identity's RHS and a direct sort-and-alternate-sum on
$\{x,p_1-x\}\cup G'$.

## Status of $(\star\star)$

$(\star\star)$ itself (the tail's odd-parity indicator cannot average more
than density $1/2$ over the window straddling $p_1/2$) is **not proved** —
this is honestly recorded in
`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md` §5.2 as
recognizably the same obstruction independently reached by
`greedy-halving-adversary`'s claim (B) and `rank-pigeonhole-budget`'s
band-occupancy minimization. This lemma is a genuine, correctly-proved
*reduction*, not a closed result.

## Origin / usage

Derived in `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`
§5.1 (round 5), generalizing `symmetric-split-c1-lower-bound` to arbitrary
(not just symmetric) single cuts on $p_1$.

## Certification note (proof-reviewer, round 5)
**CERTIFIED as a reduction** (the identity and implication are both fully
proved and independently re-verified). The target inequality $(\star\star)$
it reduces to remains open and is NOT certified — future builders should
cite this lemma for the reduction only, not treat $(\star\star)$ as proved.
