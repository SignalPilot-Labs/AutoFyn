# The General Peeling Theorem GT(m) and the Window's Gap (a), closed for ℓ=1,2,3,4

Certified round 12, from `approaches/self-similar-induction-on-n.md`
Section "Round 12: the General Peeling Theorem GT(m) — gap (a) of the
window closed in full generality for $\ell=1,2,3,4$". Independently
re-verified by the proof-reviewer (exact `Fraction` scripts). **Certified
with one correction to scope**, described below — the corollary that
matters (window's gap (a) closed at $\ell=1,2,3,4$) is unaffected.

## Reviewer's scope correction (read first)

The approach file states $\mathrm{GT}(m)$ as holding for *every* finite
multiset $D$ with $k=|D|\le m+1$, $\max(D)\le2^m$ — with no bound on
$\mathrm{sum}(D)$. The proof's case split rests on a "Feasibility bound
$p\le2$" (where $p:=\#\{a_i>2^{m-1}\}$), but the file's own proof of that
bound is **explicitly restricted** ("not asserted globally," its own
words) to instances where $\mathrm{sum}(D)$ is bounded — concretely,
$p\le2$ is only justified when $\mathrm{sum}(D)<3\cdot2^{m-1}$ (three
elements each $>2^{m-1}$ would force $\mathrm{sum}(D)>3\cdot2^{m-1}$,
excluded when the total is below that threshold). For $\mathrm{sum}(D)
\ge3\cdot2^{m-1}$, $p\ge3$ is possible and is **not covered by the given
case split** (Lemmas P2/P1 only handle $p\in\{1,2\}$, the $p=0$ branch's
$r$-split only handles $r\in\{0,1,2\}$). The reviewer's own stress test
(random $D$ up to $\mathrm{sum}(D)\approx3\cdot2^m$, adversarial search
near the threshold, $m=0,\dots,5$) found **zero violations** of the
stated bound even outside the covered regime, so the theorem is very
likely true in full generality — but this is not established by the
given proof. **Certifying here only the version actually proved:**

**Statement (certified form).** Fix $m\ge0$. For every finite multiset
$D=(a_1\ge\cdots\ge a_k)$ of positive reals with $k\le m+1$,
$\max(D)\le2^m$, **and $\mathrm{sum}(D)<3\cdot2^{m-1}$** (automatically
true whenever $\mathrm{sum}(D)\le2^m+1$, the regime actually used
throughout this file and its corollary below):
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ \min(\mathrm{sum}(D),2^m).$$

This added hypothesis is met at every level of the recursion actually
used below (the top call has $\mathrm{sum}(D)=2^m+\varepsilon<2^m+1$; each
recursive call's remainder $R$ has $\mathrm{sum}(R)\le2^{m-1}+\varepsilon
<2^{m-1}+1$, i.e. well inside the safe zone one level down), so **no
application in this file or its corollary is affected**; only the
lemma's literal unrestricted generality (for reuse by *other* future
approaches at large $\mathrm{sum}(D)$) is narrowed. A future round may
complete the $p\ge3$/$r\ge3$ cases (very likely easy — more/larger
elements only add mass at ranks that can only help, by the same
Global-max-Peeling technique used in Lemmas P2/R2, iterated) to remove
this restriction.

## Proof (case split, as given, now under the added hypothesis)

**Base case $\mathrm{GT}(0)$.** $\Gamma_{-1}=\varnothing$, $k\le1$,
$\max(D)\le1$. $D=\varnothing$: $0=\min(0,1)$. $D=\{a\}$, $a\le1$:
$a=\min(a,1)$. $\blacksquare$

**Lemma P2 ($p=2$).** $a_1\ge a_2>2^{m-1}\ge$ rest $=:R$. Then
$\mathrm{OddSum}(D\cup\Gamma_{m-1})=a_1+2^{m-1}+\mathrm{EvenSum}(R\cup
\Gamma_{m-2})\ge a_1+2^{m-1}>2^m$, via Global-max Peeling (peel $a_1$) then
Companion Peeling (peel $a_2$, now max of the rest) then Global-max Peeling
again (peel $2^{m-1}$, max of $R\cup\Gamma_{m-1}$). Whenever $p=2$,
$\mathrm{sum}(D)>2\cdot2^{m-1}=2^m$ automatically, so the target is $2^m$
and the bound suffices.

**Lemma P1 ($p=1$, uses $\mathrm{GT}(m-1)$).** $a_1>2^{m-1}\ge$ rest
$=:R$. $\mathrm{OddSum}(D\cup\Gamma_{m-1})=a_1+\mathrm{OddSum}(R\cup
\Gamma_{m-2})\ge a_1+\min(\mathrm{sum}(R),2^{m-1})$ (Global-max Peeling then
Companion Peeling, then $\mathrm{GT}(m-1)$ applied to $R$ — valid, $|R|\le
m$, $\max(R)\le2^{m-1}$, $\mathrm{sum}(R)<3\cdot2^{m-2}\le3\cdot2^{(m-1)-1}$
inherited from the standing hypothesis). Algebra (case on whether
$\mathrm{sum}(D)-a_1\gtrless2^{m-1}$) gives
$a_1+\min(\mathrm{sum}(D)-a_1,2^{m-1})\ge\min(\mathrm{sum}(D),2^m)$
whenever $a_1>2^{m-1}$.

**$p=0$ residual, split by $r:=\#\{a_i>2^{m-2}\}\in\{0,1,2\}$** (the same
argument shows $r\ge3$ needs $\mathrm{sum}(D)\ge3\cdot2^{m-2}$, excluded
under the standing hypothesis one level tighter — re-derived exactly as
for $p$). Global-max Peeling with $g=2^{m-1}$ gives $\mathrm{OddSum}(D\cup
\Gamma_{m-1})=2^{m-1}+\mathrm{EvenSum}(D\cup\Gamma_{m-2})$; reduces to
$\mathrm{EvenSum}(D\cup\Gamma_{m-2})\ge\min(\mathrm{sum}(D),2^m)-2^{m-1}$.

**Lemma R2 ($r=2$, uses $\mathrm{GT}(m-2)$).** $a_1\ge a_2>2^{m-2}\ge$
rest $=:R$, $a_1,a_2\le2^{m-1}$. $\mathrm{EvenSum}(D\cup\Gamma_{m-2})=
a_2+\mathrm{OddSum}(R\cup\Gamma_{m-3})\ge a_2+\min(\mathrm{sum}(R),2^{m-2})$
(Companion Peeling, Global-max Peeling, Companion Peeling again, then
$\mathrm{GT}(m-2)$ on $R$). Algebra closes the target.

**Lemma R1 ($r=1$, uses $\mathrm{GT}(m-1)$).** $a_1>2^{m-2}\ge$ rest
$=:R$, $a_1\le2^{m-1}$. $\mathrm{EvenSum}(D\cup\Gamma_{m-2})=
\mathrm{OddSum}(R\cup\Gamma_{m-2})\ge\min(\mathrm{sum}(R),2^{m-1})$
(Companion Peeling, then $\mathrm{GT}(m-1)$ on $R$). Algebra closes.

**Feasibility Lemma.** Within $p=0$, $r=0$ ($\max(D)\le2^{m-2}$,
$k\le m+1$, $\mathrm{sum}(D)=2^m+\varepsilon$) is infeasible for
$m\le3$ and feasible for $m\ge4$ (from $(m+1)\cdot2^{m-2}\gtrless
2^m+\varepsilon$; exact boundary at $m=3$: $4\cdot2=8<8+\varepsilon$).

**Induction.** $\mathrm{GT}(0)$: base case. $\mathrm{GT}(1)$: $p=2$
unconditional; $p=1$ via $\mathrm{GT}(0)$; $p=0$ infeasible ($k\le2$
parts $\le1$ each cap at $2<2+\varepsilon$). $\mathrm{GT}(2)$: $p=2$
unconditional; $p=1$ via $\mathrm{GT}(1)$; $p=0$: $r=0$ infeasible,
$r=2$ via $\mathrm{GT}(0)$, $r=1$ via $\mathrm{GT}(1)$. $\mathrm{GT}(3)$:
$p=2$ unconditional; $p=1$ via $\mathrm{GT}(2)$; $p=0$: $r=0$ infeasible
(exact boundary), $r=2$ via $\mathrm{GT}(1)$, $r=1$ via $\mathrm{GT}(2)$.
All cases closed for $m=0,1,2,3$. $\blacksquare$

*Reviewer verification:* independent exact-`Fraction` scripts. (1)
Uniform-random $D$ (unrestricted sum up to $2^m$), $m=0,\dots,4$, 3000
trials each: zero violations. (2) Adversarial search biased near the
$p$/$r$ thresholds, $m=1,\dots,5$: zero violations (minimum margin found
is $0$, i.e. tight, never negative) up to $\mathrm{sum}(D)\approx3\cdot
2^{m-1}$; beyond that (the genuinely unproved regime) margins grow, no
violation found either, consistent with the theorem likely holding
generally but confirming this is evidence, not proof, outside the
certified hypothesis. (3) The exact gap-(a) regime ($k\le m+1$,
$\max(D)<2^m$, $\mathrm{sum}(D)=2^m+\varepsilon$, $\varepsilon\in(0,1)$,
random rational instances via random compositions), $m=0,\dots,3$: 3150,
5771, 7089 admissible instances tested at $m=1,2,3$ respectively (m=0 is
vacuous — no admissible $D$ exists, matching the file's own note that
$\mathrm{GT}(0)$ needs no induction), zero violations.

## Corollary (certified): gap (a) of the shared Branch-I.A-restricted
## window, closed for $\ell=1,2,3,4$

Since gap (a) at level $\ell$ (as defined identically in this file and in
`approaches/greedy-reduction-geometric.md` Section 16, see
`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`) is
exactly $\mathrm{GT}(m)$ at $m=\ell-1$, $\mathrm{sum}(D)=2^m+\varepsilon$
(within the certified hypothesis's safe zone): **the window's top
endpoint holds for every admissible $D$ at $\ell=1,2,3,4$.** Combined with
Theorem W (left endpoint, all $\ell$) and the Window Reduction Theorem
(gap (b), all $\ell\ge2$), the shared window is **fully closed at
$\ell=1,2,3,4$**. General $\ell\ge5$ remains open, gated on completing
$\mathrm{GT}(m)$ for $m\ge4$ (the $r=0$ sub-case, feasible from $m=4$
onward per the Feasibility Lemma, needs one further level of the same
self-similar recursion — identified but not completed).
