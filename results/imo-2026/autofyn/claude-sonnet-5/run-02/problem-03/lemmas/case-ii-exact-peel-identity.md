## Statement

Fix $n\ge2$ and the $n$-ladder $p_1>\dots>p_{n+1}$ (so $p_1=2p_2$, by
`ladder-self-similarity-constant`/`tail-self-similarity`). Suppose Xiang Yu
fragments $p_1$ into $c_1+1\ge2$ positive parts (any $c_1\ge1$), and let
$z:=\max(\text{these parts})$. Suppose $z\ge p_2$ (equivalently, by Lemma 1
below, $z$ is the *unique* fragment of $p_1$ that is $\ge p_2$, i.e. this is
the "dominant-fragment" case). Let $F'':=(\text{the other }c_1\text{
fragments of }p_1)$ (summing to $w:=p_1-z\le p_2$), and let $G_T$ be *any*
legal refinement of the tail $T=\{p_2,\dots,p_{n+1}\}$ using at most the
remaining cut budget. Write $G':=F''\cup G_T$. Then, **exactly** (no
inequality, no error term):
$$A\big(\{z\}\cup G'\big) \;=\; z - A(G').$$

## Lemma 1 (at most one fragment of $p_1$ reaches $p_2$; re-derived from
scratch, not imported)

If $f_i,f_j$ are two *distinct* fragments of $p_1$ with $f_i,f_j\ge p_2$ and
$f_i+f_j=2p_2$ is not forced, we in fact show strictly more cannot happen:
if $f_i>p_2$ and $f_j>p_2$ then $f_i+f_j>2p_2=p_1$, but $f_i+f_j\le\sum_k
f_k=p_1$ (all fragments are positive), a contradiction. If instead
$f_i=f_j=p_2$ exactly (both attaining, not exceeding, the boundary), then
$f_i+f_j=2p_2=p_1$ exactly, forcing every other fragment to be $0$ — impossible
since fragments are required to be strictly positive, unless $c_1+1=2$ (no
other fragments to force to $0$). Hence: for $c_1+1\ge3$ (i.e. $c_1\ge2$), at
most one fragment can be $\ge p_2$; for $c_1+1=2$ (i.e. $c_1=1$, the case
already fully closed elsewhere) two fragments can both equal $p_2$
(the symmetric split), which is consistent since there $z$ is still
well-defined as "the" (either) copy of $p_2$. In every case, $z:=\max$ is
well-defined and $w:=p_1-z\le p_2$ whenever $z\ge p_2$. $\blacksquare$

## Proof of the exact identity

**Step 1 (every element of $G'$ is $\le p_2$).** Fragments in $F''$ sum to
$w\le p_2$ (shown above) and each is a positive part of a partition of $w$,
hence each is $<w\le p_2$ (or, if $F''=\{w\}$ is a single unsplit part,
exactly $w\le p_2$) — in either case $\le p_2$. Fragments in $G_T$: for each
tail piece $p_i$ ($i\ge2$), any legal fragment of $p_i$ is $\le p_i\le p_2$
(the ladder is decreasing), exactly the argument already used in the
certified Half-Window Vanishing Lemma
(`rank-tie-vertex-reduction.md`, §5.2). So every element of
$G'=F''\cup G_T$ is $\le p_2$.

**Step 2 ($v$ vanishes on $[p_2,\infty)$, and hence on all of $[0,\infty)$
outside $[0,p_2)$).** By Step 1, no element of $G'$ exceeds $p_2$, so for
$t\ge p_2$, $N_{G'}(t)=0$ (even), i.e. $v(t):=\mathbb1[N_{G'}(t)\text{ odd}]
=0$ for every $t\ge p_2$.

**Step 3 (the window integral collapses to the full integral).** By the
Peel Decomposition Identity (`peel-decomposition-identity.md`) applied to
$S=\{z\}\cup G'$ with the distinguished maximal element $z$ (note: $z$ is
indeed $\ge$ every element of $G'$, since $z\ge p_2\ge$ every element of
$G'$ by Step 1, so $z$ is a valid choice of "the maximal element of $S$"):
$$A(S) = z + A(G') - 2\int_0^{\min(z,r')} v(t)\,dt,\qquad
r':=\mathrm{Total}(G')=w+r,\ \ r:=\mathrm{Total}(T).$$
Since $r=\mathrm{Total}(T)\ge p_2$ (a sum of $n\ge1$ positive terms
including $p_2$ itself) and $w\ge0$, $r'\ge p_2$; and $z\ge p_2$ by
hypothesis. So $\min(z,r')\ge p_2$, hence
$$\int_0^{\min(z,r')}v = \int_0^{p_2}v + \int_{p_2}^{\min(z,r')}v
= \int_0^{p_2}v + 0$$
(the second integral vanishes by Step 2, since $[p_2,\min(z,r'))\subseteq
[p_2,\infty)$). Moreover $v\equiv0$ also for $t\ge p_2$ trivially covers
everything past $p_2$, so $\int_0^{p_2}v=\int_0^{\infty}v=A(G')$ directly by
`integral-alternating-sum-formula` applied to the multiset $G'$ itself
(the integrand is zero outside $[0,p_2)\supseteq[0,\max G')$, so truncating
at $p_2$ loses nothing). Hence $\int_0^{\min(z,r')}v = A(G')$ **exactly**.

**Step 4 (substitute).** $A(S) = z + A(G') - 2A(G') = z - A(G')$.
$\blacksquare$

## What this does and does not establish

This is an **exact algebraic identity**, not an inequality — it converts
"$A(S)\ge f(n)$" (the domination goal, dominant-fragment sub-case of
general $c_1\ge2$) into the *logically equivalent* statement
"$A(G')\le z-f(n)$." Because the identity is exact, this equivalence gives
**no reduction in difficulty by itself**: proving one is exactly as hard as
proving the other, unless $A(G')$ can be bounded above by some argument
that does not just re-derive $A(S)$ from scratch (e.g. an inductive
hypothesis on $c_1-1$, or a genuinely new upper-bound lemma). This
distinction — an exact reformulation vs. a genuine reduction — is the
central honest finding of this file's origin round; see
`rank-tie-vertex-reduction.md` §6 for the full discussion of why no such
independent bound was found this round.

**Boundary between cases.** The hypothesis $z\ge p_2$ is essential: Step 1
fails when $z<p_2$ (then $w=p_1-z>p_2$, so fragments of $w$ need not be
$\le p_2$, and $v$ need not vanish anywhere near $p_2$) — this is exactly
the complementary "no dominant fragment" case (Case I in the sense of
`rank-pigeonhole-budget.md`'s Lemma 1), for which this identity does **not**
apply and was numerically confirmed to fail in the vast majority of random
instances tested (see certification note).

## Certification note (self-check, this round; not yet reviewer-certified)

Verified exactly (`fractions.Fraction`, no floats):
- By hand, symbolically, on two independent worked vertices: $n=3$,
  fragments $(p_2,p_3,p_3)$ of $p_1$ ($z=p_2=4/15$, tail untouched,
  $A(G')=3/15$, giving $z-A(G')=1/15=f(3)$ — matches direct computation of
  $A(S)$ exactly); and $n=4$, fragments $(p_2,p_3,p_3)$ of $p_1$ with the
  real $p_3$ additionally split into $(p_4,p_4)$ ($z=p_2=8/31$,
  $A(G')=7/31$, giving $z-A(G')=1/31=f(4)$ — again matches).
- By a random exact-`Fraction` script (`/tmp/verify_peel2.py`): $5{,}957$
  random legal trials (respecting the true cut budget $\le n$) across
  $n=2,\dots,7$, $c_1\in\{2,\dots,n\}$, random fragmentations of $p_1$ and
  random legal tail refinements, restricted to the dominant-fragment case
  ($z\ge p_2$): the identity $A(S)=z-A(G')$ held in **every** trial, zero
  mismatches, and (consistent with, but not a substitute for, the population's
  prior domination results) $A(S)\ge f(n)$ held in every one of these trials
  too.
- A separate control run of $6{,}840$ trials with $z<p_2$ (Case I, outside
  this lemma's hypothesis) found the identity **failed** in $6{,}465$ of
  them — confirming the $z\ge p_2$ hypothesis is not a technicality but the
  actual boundary where the mechanism (Step 1's vanishing fact) breaks down.

## Origin

`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, round 7
(peel-induction-on-$c_1$ task, in response to the round-7 outliner's and
round-6 explorer's request to extend the Half-Window Vanishing mechanism
to general $c_1$).

## Certification note (proof-reviewer, round 7)

**CERTIFIED.** Re-derived the proof line by line (Lemma 1's "at most one
fragment $\ge p_2$" case split, Steps 1–4 of the exact-identity proof, all
check out — Step 3's use of the certified `peel-decomposition-identity`
and `half-window-vanishing-lemma`'s element-bound fact is correctly
applied). Independently re-verified numerically with a freshly-written
exact-`Fraction` script (not the builder's): 10,138 random legal trials in
the dominant-fragment regime ($z\ge p_2$), $n=2,\dots,7$, $c_1\in\{2,
\dots,n\}$ — the identity $A(S)=z-A(G')$ held exactly in every trial, zero
mismatches; a control of 9,862 trials outside the hypothesis ($z<p_2$)
found the identity fails in the large majority (consistent with, not
identical in exact rate to, the builder's own $6,840$-trial control —
different random distribution, same qualitative conclusion: the $z\ge p_2$
hypothesis is the genuine boundary). The honest scope claim — this is an
exact reformulation, not a reduction, since "$A(S)\ge f(n)$" and
"$A(G')\le z-f(n)$" are logically equivalent — is correct and was checked
by hand (the trivial universal bound $A(G')\le\mathrm{Total}(G')$ is
indeed too weak, verified by direct algebra: needs $w\le0$).
