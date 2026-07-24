## Statement

Fix $n\ge2$, one asymmetric cut on $p_1$ (fragments $x,p_1-x$,
$\Delta:=2x-p_1\ge0$), and an arbitrary legal tail refinement $G'$ of
$T=\{p_2,\dots,p_{n+1}\}$. Write $W:=[p_1-x,x)$, $W_L:=[p_1-x,p_2)$,
$W_R:=[p_2,x)$ (both length $\Delta/2$, using the ladder identity
$p_1=2p_2$), $r:=\mathrm{Total}(G')$, $v(t):=\mathbb1[N_{G'}(t)\text{ odd}]$.
Then the already-certified `half-window-vanishing-lemma` ($(\star\star)$)
decomposes as an explicit **nonnegative-combination certificate with a term
count independent of $|G'|$**:
$$\frac\Delta2-\int_{W\cap[0,r)}v(t)\,dt \;=\; 1\cdot g_1,\qquad
g_1:=\int_{W_L}(1-v(t))\,dt\ \ge0,$$
where the right-half contribution $\int_{W_R\cap[0,r)}v\,dt$ is *exactly*
$0$ (not merely bounded), licensed by the fact that no element of $G'$
exceeds $p_2$ (the content of `half-window-vanishing-lemma`).

This exhibits $(\star\star)$ as a sum of: one "window-monotonicity" atom
($g_1=\int_{W_L}(1-v)\ge0$, a manifestly nonnegative integral) plus one
exactly-zero "support-vanishing" atom — a fixed term count of $2$,
independent of $n$, of how many cuts $G'$ uses, and of how the tail's mass
is distributed among fragments.

## Proof

Split the target at $p_2$ (using $W_L\subseteq[0,r)$, since $p_1-x\ge0$
and $p_2\le r$):
$$\frac\Delta2-\int_{W\cap[0,r)}v = \left(\frac\Delta2-\int_{W_L}v\right)
-\int_{W_R\cap[0,r)}v.$$
The first parenthesis equals $\int_{W_L}(1-v)\,dt$ (using $|W_L|=\Delta/2$),
manifestly $\ge0$ (integral of a nonnegative integrand). The second term is
exactly $0$ by `half-window-vanishing-lemma` ($v\equiv0$ on
$[p_2,\infty)\supseteq W_R$). Summing gives the stated identity; since the
LHS equals $g_1\ge0$, $(\star\star)$ follows. $\blacksquare$

## What this is (and isn't)

A **repackaging**, not a new inequality: it is algebraically equivalent to
`half-window-vanishing-lemma`, restated in a "sum of manifestly nonnegative
atoms" vocabulary. Its value is structural: it demonstrates this
vocabulary can express an *unbounded* family of instances (all legal $G'$)
with a *fixed* term budget — a property tested (and found to fail, for a
precise, diagnosed reason) when mechanically extended to $c_1\ge2$; see
`results/imo-2026-03/approaches/lp-duality-certificate.md` §7 for the
failure witness ($n=3$, $c_1=2$, $F=\{4,2,2\}/15$, tail untouched: the
mechanical extension needs $\int uv\le2/15$ but the actual value is
$3/15$).

## Verification (proof-reviewer, round 7)

Re-derived the split-at-$p_2$ algebra by hand (identical to
`half-window-vanishing-lemma`'s own proof, just relabeled into the
Type-III/Type-IV atom vocabulary) — no gap. Independently re-verified the
underlying $(\star\star)$ numerically (5,000 fresh exact-`Fraction` trials,
$n=2,\dots,6$, random asymmetric cuts and tail refinements): zero
violations, consistent with `half-window-vanishing-lemma`'s own
certification. Not independently re-run the builder's specific 80-trial
"Type-IV atom is exactly zero" check, but this is subsumed by the general
$(\star\star)$ re-verification (the Type-IV atom's exact vanishing is the
same fact as the right-half integral being exactly $0$, checked above).

## Origin

`results/imo-2026-03/approaches/lp-duality-certificate.md`, §6.2 (round 7).

## Certification note (proof-reviewer, round 7)

**CERTIFIED** as a correct repackaging of `half-window-vanishing-lemma`.
Not a new mathematical result beyond that lemma, but reusable in its own
right for any sibling approach working in the certificate/atom vocabulary.
