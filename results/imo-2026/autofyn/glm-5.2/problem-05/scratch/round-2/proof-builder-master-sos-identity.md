# Build report — master-sos-identity (IMO 2026 P5, round 2)

Approach file: `/home/agentuser/repo/results/imo-2026-05/approaches/master-sos-identity.md`
Status: **partial** (lemma proven & certifiable; direct kill honestly open).

## What was PROVED (certain deliverable)

**The Master Squeeze Lemma — fully rigorous, both directions.** Written in
place in the approach file under "PROVEN THIS ROUND". It comprises:

1. **SOS identity (completing the square).** By direct expansion with
   $f(x)=x+g(x)$, $f(y)=y+g(y)$:
   $$U+L=\frac{(x-f(y))^{2}}{2},\qquad
   U-L=-\frac{(g(x)-g(y))(g(x)+g(y)+2x+2y)}{2}.$$
   Verified symbolically (sympy): both residues identically zero. The written
   proof derives $U+L$ as the completed square $(x-y-g(y))^{2}/2$ explicitly;
   $U-L$ is then obtained by subtraction with the symmetric $g$-terms.

2. **Equivalence, both directions.** Uses the elementary biconditional
   (proved in-file): for real $a,b$, $a,b\ge0\iff a+b\ge0\ \&\ |a-b|\le a+b$.
   Applied with $a=U,b=L$: since $U+L=(x-f(y))^{2}/2\ge0$ automatically, the
   condition reduces to $|U-L|\le U+L$, which is exactly the master squeeze
   $|(g(x)-g(y))(g(x)+g(y)+2x+2y)|\le(x-f(y))^{2}$. The Fact is an iff, so
   both the forward (original $\Rightarrow$ master) and backward
   (master $\Rightarrow$ original) directions are covered — no one-way
   implication is left implicit.

3. **Reduced form under $g\ge0$.** Under $g\ge0$ (proven for solutions by the
   other approaches' orbit forward-positivity lemma), the second factor is
   $\ge2x+2y>0$, the absolute value drops, giving the boxed form
   $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^{2}$.

4. **Corollaries (PROVEN).** (a) Orbit invariance $g(f(y))=g(y)$ is the
   equality case $x=f(y)$ of the squeeze (RHS $=0\Rightarrow$ LHS $=0$).
   (b) Swapped two-window min:
   $|g(x)-g(y)|\le\min\{(x-f(y))^{2},(y-f(x))^{2}\}/(g(x)+g(y)+2x+2y)$, by
   applying the squeeze to $(x,y)$ and $(y,x)$ (symmetric denominator).

5. **Exhibit verification.** $f(x)=x+c$, $c\ge0$: classical QM-AM (left) and
   AM-GM (right) on $(x,y+c)$; squeeze reads $0\le(x-y-c)^{2}$, automatic.

**The lemma is self-contained, correctly stated, and ready for certification
into `results/imo-2026-05/lemmas/master-squeeze.md`.** It is load-bearing for
the other three approaches (orbit-monotonicity-sandwich,
density-contradiction, extremal-infimum), which import it as their squeeze
engine.

## Direct-kill status — HONESTLY OPEN (not overclaimed)

The kill seeks to prove, from $(\star)+g\ge0$ alone, that $g\equiv c$. Three
sub-routes were pursued; none closes:

- **(a) Swapped two-window intersection.** The refinement $(\dagger)$ is
  PROVEN, but turning it into a kill needs a parametric family of pairs
  approaching the two *distinct* roots $x=f(y)$ and $y=f(x)$ simultaneously.
  No such family is constructible without regularity (continuity/monotonicity)
  the problem does not give. Not a kill.
- **(b) Simultaneous-collapse fixed point.** Simultaneous collapse
  $\iff g(x)=g(y)=0$; near-collapse would yield contradiction, but existence
  needs IVT on $(x,y)\mapsto(f(y),f(x))$, and **no continuity of $f$ is
  hypothesized**. Conjectural; left open.
- **(c) Optimization "bound" — RETRACTED as a non-result.** The skeleton
  claimed $\min\{(x-f(y))^{2},(y-f(x))^{2}\}\le((g(x)+g(y))/2)^{2}$ universally.
  We checked: the two quadratics $(d-g(y))^{2}$, $(d+g(x))^{2}$ (with $d=x-y$)
  *intersect* at $d=(g(y)-g(x))/2$ at value $((g(x)+g(y))/2)^{2}$, but this is
  the min over a *free* parameter $d$; for a *fixed* given pair, $d=x-y$ is
  determined and may be far from the intersection (e.g. $g\equiv1$, $d=100$
  gives min $=9801\gg1$). The bound is therefore **not universal** and yields
  no disparity control on a fixed pair. Retracted. (The outline-reviewer
  verified the *intersection value*; that is correct but is not a universal
  bound, as shown.)

**Numerical rigidity (evidence, not proof).** Every non-constant perturbation
tested violates $(\star)$: periodic $g=c+\varepsilon\sin(2\pi x/c)$,
$\varepsilon\in\{0.01,0.05,0.1,0.3\}$ (violations $3.7$ to $118.8$, occurring at
large $x,y$ where the second factor $\sim2x$ amplifies a bounded disparity);
decaying $c+\varepsilon e^{-x}$, $c+\varepsilon/(1+x)$; growing
$c+\varepsilon x/(1+x)$ — all fail for $\varepsilon$ as small as $0.01$. The
rigidity is real and is what the structural approaches exploit; a pure
one-move algebraic kill is not found.

## Gaps
- Direct kill (step 4): open. (a) needs regularity; (b) needs continuity/IVT;
  (c) retracted.
- The approach does not use $g\circ f=g$ as a *kill* input (only as a derivable
  corollary). If the kill later folds in orbit structure, it converges toward
  `orbit-monotonicity-sandwich` — flagged to avoid silent field collapse.

## Spec concerns for the reviewer
- The outline-reviewer rated the optimization bound (4c) "correct and tight."
  It is correct *as an intersection value* but **not as a universal bound on a
  fixed pair**; the kill cannot use it. This is reported honestly in-file and
  above; please note the retraction when ranking.
- The master squeeze lemma is the approach's genuine value this round. Please
  certify it into `lemmas/master-squeeze.md` so the other three builders can
  import it.

## Lemma ready for certification
**Master Squeeze Lemma** — see "Promotable lemmas" section at the end of the
approach file. Self-contained; both directions proven; SOS identity verified
symbolically and derived in prose. Import target:
`results/imo-2026-05/lemmas/master-squeeze.md`.
