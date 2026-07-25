# Elementwise Monotonicity, Transfer Monotonicity, and the Window Reduction Theorem

Certified round 12, from `approaches/greedy-reduction-geometric.md` Section
16. Independently re-verified by the proof-reviewer (exact `Fraction`
scripts, thousands of trials per fact, zero violations; see verification
notes below each result).

## Elementwise Monotonicity Lemma (general-purpose)

**Statement.** Let $N$ be any finite multiset of positive reals (possibly
empty). Then $x\mapsto\mathrm{OddSum}(N\cup\{x\})$ is non-decreasing on
$(0,\infty)$.

**Proof.** Fix $0<x_1<x_2$, sort $N$ descending $y_1\ge\cdots\ge y_n$. For
$x\in(0,\infty)$ let $r(x):=|\{i:y_i\ge x\}|$; in $N\cup\{x\}$ sorted
descending, $x$ occupies rank $r(x)+1$, elements $y_1,\dots,y_{r(x)}$ keep
ranks $1,\dots,r(x)$, and the rest shift down by one. On each open interval
$(y_{r+1},y_r)$ where $r(x)\equiv r$ is constant, $\mathrm{OddSum}(N\cup\{x\})$
is linear in $x$ with slope $[\,r+1\text{ odd}\,]\in\{0,1\}\ge0$. The map is
continuous (sort-and-sum-odd-ranks is a continuous, well-defined function of
the multiset, and ties are harmless since $\mathrm{OddSum}$ depends only on
the multiset of values, not tie-breaking). A continuous, piecewise-linear
function with non-negative slope on every piece of a locally finite
partition is non-decreasing on the whole domain, by chaining across the
finitely many breakpoints $y_1,\dots,y_n$ between $x_1$ and $x_2$.
$\blacksquare$

*Reviewer verification:* independent exact-`Fraction` script, 5000 random
trials, $|N|=0,\dots,8$, zero violations.

## Transfer Monotonicity Theorem

**Statement.** Fix a finite multiset $T_0$ of positive reals with
$\max(T_0)=\mu$, and a finite multiset $D$ of positive reals with every
element $<\mu$. Fix $c\ge\mu$, $\delta\ge0$, and $w_0\ge0$ equal either (a)
the value of a chosen element $x\in D$, or (b) $0$ (a fresh slot to be
created). Assume $\delta\le c-\mu$ and $\delta\le\mu-w_0$. Let $D_t$ be $D$
with the chosen element replaced by $w_0+t$ (case (a)) or $D\cup\{t\}$ for
$t>0$ (case (b)), $t\in[0,\delta]$. Then $t\mapsto\mathrm{OddSum}(D_t\cup
\{c-t\}\cup T_0)$ is non-increasing on $[0,\delta]$; equivalently, writing
$c':=c-\delta$,
$$\mathrm{OddSum}(D_0\cup\{c\}\cup T_0)\ \ge\ \mathrm{OddSum}(D_\delta\cup\{c'\}\cup T_0).$$

**Proof.** For $t\in[0,\delta]$, $c-t\ge\mu$ (first hypothesis) and every
element of $D_t$ is $\le\mu\le c-t$ (second hypothesis plus the standing
bound on $D$'s untouched elements), so $c-t=\max(D_t\cup\{c-t\}\cup T_0)$
weakly. By the Global-max Peeling Lemma (`lemmas/dominant-piece-lower-bound.md`),
$\mathrm{OddSum}(D_t\cup\{c-t\}\cup T_0)=(c-t)+\mathrm{EvenSum}(D_t\cup T_0)$.
With $N$ the fixed remainder ($D\setminus\{x\})\cup T_0$ in case (a), or
$D\cup T_0$ in case (b)), $D_t\cup T_0=N\cup\{w_0+t\}$, so by the
Elementwise Monotonicity Lemma $\mathrm{OddSum}(N\cup\{w_0+t\})$ is
non-decreasing with slope in $\{0,1\}$ a.e.; since
$\mathrm{EvenSum}=\mathrm{sum}(N)+w_0+t-\mathrm{OddSum}$, its slope in $t$
is in $\{0,1\}$ a.e. too. Hence
$\frac{d}{dt}[(c-t)+\mathrm{EvenSum}(D_t\cup T_0)]\in\{-1,0\}$ a.e., so the
whole expression is continuous, piecewise-linear, non-increasing.
$\blacksquare$

*Reviewer verification:* independent exact-`Fraction` script, both
mechanisms (a)/(b), 2000 trials each built from the window setting, zero
violations.

## Window Reduction Theorem

**Setting.** Fix $\ell\ge2$, $\varepsilon\in(0,1)$; $\mathrm{cap}:=2^{\ell-1}$,
$T:=\Gamma_{\ell-1}$. $C=D\cup\{c_1\}$ is *admissible* if $D$ is a finite
multiset of positive reals with $\max(D)<\mathrm{cap}$, $c_1\in[\mathrm{cap},
\mathrm{cap}+1-\varepsilon)$, $|D|\le\ell$, $\mathrm{sum}(C)=2^\ell+
\varepsilon$.

**Statement.** If the **Endpoint Statement** holds — for every finite
multiset $D_0$ with $|D_0|\le\ell$, every element $<\mathrm{cap}$, and
$\mathrm{sum}(D_0)=\mathrm{cap}+\varepsilon$,
$\mathrm{OddSum}(D_0\cup\{\mathrm{cap}\}\cup\Gamma_{\ell-1})\ge2^\ell$ —
then $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$ for **every**
admissible $C$.

**Proof.** For admissible $C=D\cup\{c_1\}$, $k:=|D|\ge1$ (the $D=\varnothing$
case is excluded by admissibility since it would force
$c_1=2^\ell+\varepsilon\ge\mathrm{cap}+1-\varepsilon$, contradiction). If
$c_1=\mathrm{cap}$, apply the Endpoint Statement directly. If
$c_1>\mathrm{cap}$: with $\Delta:=c_1-\mathrm{cap}$, headroom
$H:=\sum_{d\in D}(\mathrm{cap}-d)$ satisfies $H-\Delta=(k-1)\mathrm{cap}-
\varepsilon$. For $k\ge2$, $(k-1)\mathrm{cap}\ge\mathrm{cap}\ge2>1>
\varepsilon$, so $H\ge\Delta$ and mechanism (a) of Transfer Monotonicity
(grow existing $D$-coordinates, one at a time, using each one's own
headroom until $\Delta$ is absorbed) reduces $(D,c_1)$ to an admissible
endpoint $(D_0,\mathrm{cap})$ without ever needing more than $D$'s total
headroom. For $k=1$ (the tight case: a single element has headroom exactly
$\mathrm{cap}-\varepsilon$ but the empty $(k-1)\mathrm{cap}$ term vanishes,
so $H-\Delta=-\varepsilon<0$ and mechanism (a) alone is genuinely
insufficient), use mechanism (b) instead: insert $\Delta$ as a fresh
element ($D_0:=D\cup\{\Delta\}$, valid since $\Delta<\mathrm{cap}$ and
$|D_0|=2\le\ell$ as $\ell\ge2$). More generally mechanism (b) alone
suffices whenever $k<\ell$ (room for one more slot, no headroom check
needed); only the saturated case $k=\ell\ge2$ needs mechanism (a), exactly
where the headroom bound above is ample. Either way, $(D,c_1)$ reduces via
a finite sequence of valid Transfer Monotonicity steps to an admissible
endpoint $(D_0,\mathrm{cap})$, and chaining
$$\mathrm{OddSum}(D\cup\{c_1\}\cup\Gamma_{\ell-1})\ge\mathrm{OddSum}
(D_0\cup\{\mathrm{cap}\}\cup\Gamma_{\ell-1})\ge2^\ell$$
gives the claim. $\blacksquare$

**Corollary (equivalence with the sibling file's gap-(a) target).** The
Endpoint Statement is, via Peel-the-Max and the certified Companion
Peeling Lemma, exactly $\mathrm{OddSum}(D_0\cup\Gamma_{\ell-2})\ge
2^{\ell-1}$ — symbol-for-symbol the target certified closed (for
$\ell=1,2,3,4$, i.e. $m=\ell-1=0,1,2,3$) by the General Theorem $\mathrm{GT}(m)$
in `lemmas/general-peeling-theorem-and-window-endpoint-closure.md`.

*Reviewer verification:* independent exact-`Fraction` script generating
2259 random admissible window instances ($\ell=2,\dots,6$), constructing
the reduction sequence per the mechanism-selection rule above and directly
checking $\mathrm{OddSum}(D\cup\{c_1\}\cup\Gamma_{\ell-1})\ge\mathrm{OddSum}
(D_0\cup\{\mathrm{cap}\}\cup\Gamma_{\ell-1})$: zero violations.

## Consequence for the shared Branch-I.A-restricted window

Combining the Window Reduction Theorem (gap (b), both piece-cap-unsaturated
**and** piece-cap-saturated sub-cases, i.e. (b)(i) and (b)(ii), fully
closed — this **strictly subsumes** the previously-certified Lemma TPI,
which only handled (b)(i)) with the General Theorem $\mathrm{GT}(m)$'s
corollary (gap (a) closed for $\ell=1,2,3,4$) and Theorem W (the left
endpoint, all $\ell$, `lemmas/theorem-w-window-endpoint-witness.md`): **the
shared Branch-I.A-restricted window is fully closed — every gap: left
endpoint, top endpoint, piece-cap-unsaturated monotonicity, and
piece-cap-saturated monotonicity — at $\ell=1,2,3,4$.** This is a
genuinely stronger statement than either contributing file claims alone
(`self-similar-induction-on-n`'s own round-12 corollary explicitly leaves
gap (b)(ii) open; the Window Reduction Theorem above closes it). General
$\ell\ge5$ remains open, gated on $\mathrm{GT}(m)$ for $m\ge4$ (see the
companion lemma file for the precise open sub-case).
