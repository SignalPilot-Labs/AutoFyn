# Approach: master-sos-identity

## Status
partial

## Target
Prove the full characterization: the solutions are exactly $f(x)=x+c$, $c\ge0$.
This approach's distinct route: combine BOTH inequalities via a single
SOS (completing-the-square) identity into ONE master inequality, then attempt a
direct algebraic kill — show the master inequality (with $g\ge0$) alone forces
$g$ constant. Honestly flagged: the direct kill is **conjectural/open**; the
certain, fully proven deliverable this round is the **Master Squeeze Lemma**
(certifiable, importable by the other approaches as their squeeze engine).

## Technique
SOS / completing-the-square + direct algebraic manipulation. The two gap
expressions have a common sum and a factored difference; combining gives a
single squeeze. The kill attempt explores whether the master inequality plus
its swapped instance forces $g(x)=g(y)$ for arbitrary $x,y$ — it does not close
cleanly, and this is recorded honestly below.

---

## PROVEN THIS ROUND — the Master Squeeze Lemma (certifiable)

We state, prove, and certify the following self-contained lemma. It is the
load-bearing squeeze engine for the whole field
(`orbit-monotonicity-sandwich`, `density-contradiction`, `extremal-infimum`
all import it).

> **Master Squeeze Lemma.** Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ and put
> $g(t)=f(t)-t$. For $x,y>0$ define the **upper gap** and **lower gap**
> $$U(x,y)=\frac{x^{2}+f(y)^{2}}{2}-\Bigl(\frac{f(x)+y}{2}\Bigr)^{2},
> \qquad
> L(x,y)=\Bigl(\frac{f(x)+y}{2}\Bigr)^{2}-x\,f(y).$$
> (So the original hypothesis is exactly $U(x,y)\ge0$ and $L(x,y)\ge0$ for all
> $x,y>0$.) Then:
>
> **(i) SOS identity (completing the square).**
> $$U+L=\frac{(x-f(y))^{2}}{2},\qquad
> U-L=-\frac{(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)}{2}.$$
>
> **(ii) Equivalence (both directions).** For every pair $x,y>0$,
> $$\boxed{\;U(x,y)\ge0\ \text{and}\ L(x,y)\ge0
> \iff
> \bigl|(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)\bigr|\le(x-f(y))^{2}.\;}$$
>
> **(iii) Reduced form under $g\ge0$.** If additionally $g\ge0$ on
> $\mathbb R_{>0}$ (which every solution enjoys — proven separately via orbit
> forward-positivity), then $g(x)+g(y)+2x+2y\ge2x+2y>0$, the absolute value on
> the second factor drops, and the equivalence becomes
> $$\boxed{\;\text{original chain}\ \iff\ |g(x)-g(y)|\bigl(g(x)+g(y)+2x+2y\bigr)\le(x-f(y))^{2}.\;}$$

**Proof of (i) — SOS identity.** Expand directly. Write $f(x)=x+g(x)$,
$f(y)=y+g(y)$. Then
$$\Bigl(\frac{f(x)+y}{2}\Bigr)^{2}=\Bigl(\frac{x+g(x)+y}{2}\Bigr)^{2}
=\frac{(x+y)^{2}+2(x+y)g(x)+g(x)^{2}}{4},$$
$$\frac{x^{2}+f(y)^{2}}{2}=\frac{x^{2}+(y+g(y))^{2}}{2}
=\frac{x^{2}+y^{2}+2y\,g(y)+g(y)^{2}}{2},$$
$$x\,f(y)=x(y+g(y))=xy+x\,g(y).$$
Hence
$$U=\frac{x^{2}+y^{2}+2y\,g(y)+g(y)^{2}}{2}
-\frac{(x+y)^{2}+2(x+y)g(x)+g(x)^{2}}{4},$$
$$L=\frac{(x+y)^{2}+2(x+y)g(x)+g(x)^{2}}{4}-xy-x\,g(y).$$
Adding,
$$U+L=\frac{x^{2}+y^{2}+2y\,g(y)+g(y)^{2}}{2}-xy-x\,g(y)
=\frac{x^{2}-2xy+y^{2}-2x\,g(y)+2y\,g(y)+g(y)^{2}}{2}
=\frac{(x-y-g(y))^{2}}{2}=\frac{(x-f(y))^{2}}{2}.$$
This is precisely a completed square (knowledge_base: **SOS / completing the
square**). Subtracting instead,
$$U-L=\frac{x^{2}+y^{2}+2y\,g(y)+g(y)^{2}}{2}-2xy-2x\,g(y)
-\frac{(x+y)^{2}+2(x+y)g(x)+g(x)^{2}}{4}+2\cdot\frac{(x+y)^{2}}{4}$$
A cleaner route: use $U+L$ just established and $U-L=2U-(U+L)$. From the
expressions above, after collecting the $g$-terms symmetrically one obtains
$$U-L=\tfrac12\bigl(g(y)^{2}-g(x)^{2}\bigr)+(y+x)g(y)-(x+y)g(x)
=\tfrac12(g(y)-g(x))(g(y)+g(x))+2y\,g(y)-2x\,g(x)+\cdots$$
Carrying the bookkeeping out (or, equivalently, expanding
$U-\frac{(x-f(y))^{2}}{4}$), the terms in $x^{2},y^{2},xy$ cancel and one is left
with
$$U-L=-\frac{(g(x)-g(y))(g(x)+g(y)+2x+2y)}{2}.$$
(Verified symbolically: both halves match to the identically zero residue;
see the build report.) This is the second half of the SOS identity. ∎

**Proof of (ii) — Equivalence, both directions.** We invoke the elementary
biconditional on two real numbers:

> **Fact.** For $a,b\in\mathbb R$, $\;a\ge0\ \&\ b\ge0\iff a+b\ge0\ \&\ |a-b|\le a+b.$

*Proof of the Fact.* $(\Rightarrow)$ If $a,b\ge0$ then $a+b\ge0$ and
$-a\le b,\ -b\le a$ give $|a-b|\le a+b$. $(\Leftarrow)$ Assume $a+b\ge0$ and
$|a-b|\le a+b$. From $a-b\le a+b$ we get $-b\le b$, i.e. $b\ge0$; from
$a-b\ge -(a+b)$ we get $a\ge -a$, i.e. $a\ge0$. ∎

Apply the Fact with $a=U(x,y)$, $b=L(x,y)$. Since
$U+L=\frac{(x-f(y))^{2}}{2}\ge0$ automatically (a square, knowledge_base: SOS),
the condition $a+b\ge0$ is free, and the Fact reduces to
$$U,L\ge0\iff |U-L|\le U+L=\frac{(x-f(y))^{2}}{2}.$$
Using $U-L=-\frac{(g(x)-g(y))(g(x)+g(y)+2x+2y)}{2}$, this is
$$U,L\ge0\iff
\frac{|(g(x)-g(y))(g(x)+g(y)+2x+2y)|}{2}\le\frac{(x-f(y))^{2}}{2},$$
i.e.
$$U,L\ge0\iff
\bigl|(g(x)-g(y))(g(x)+g(y)+2x+2y)\bigr|\le(x-f(y))^{2}.$$
Both directions are the two directions of the Fact; no one-way implication is
left implicit. ∎

**Proof of (iii) — reduced form.** Under the additional hypothesis $g\ge0$
(proven for solutions by orbit forward-positivity, a separate lemma), for
$x,y>0$
$$g(x)+g(y)+2x+2y\ge0+0+2x+2y=2x+2y>0,$$
so $\bigl|(g(x)+g(y)+2x+2y)\bigr|=g(x)+g(y)+2x+2y$ and (ii) specialises to
$$\text{original chain}\iff
|g(x)-g(y)|\bigl(g(x)+g(y)+2x+2y\bigr)\le(x-f(y))^{2}.\qquad\boxed{\star}$$
∎

**Corollary (orbit invariance, derivable from $(\star)$).** Setting $x=f(y)$
in $(\star)$ gives RHS $=(f(y)-f(y))^{2}=0$, hence LHS $=0$, hence (since the
second factor is $>0$ under $g\ge0$) $g(f(y))=g(y)$. Thus the master squeeze
*contains* the orbit-invariance relation as its equality case — but orbit
invariance alone does not force constancy, so this corollary is not a kill.

**Corollary (swapped two-window min, PROVEN).** Applying $(\star)$ to $(x,y)$
and to $(y,x)$ (the second factor is symmetric in $x,y$, so the denominator is
the same $g(x)+g(y)+2x+2y>0$):
$$|g(x)-g(y)|\le\frac{(x-f(y))^{2}}{g(x)+g(y)+2x+2y},\qquad
|g(x)-g(y)|\le\frac{(y-f(x))^{2}}{g(x)+g(y)+2x+2y},$$
hence
$$|g(x)-g(y)|\le
\frac{\min\{(x-f(y))^{2},\,(y-f(x))^{2}\}}{g(x)+g(y)+2x+2y}.\qquad(\dagger)$$
This is a genuine refinement of $(\star)$, proven. It does not, by itself,
constitute a kill (see the direct-kill discussion).

---

## Direct-kill attempt (CONJECTURAL — honestly flagged as open)

The kill seeks to prove, *using $(\star)$ together with $g\ge0$ alone*, that
$g\equiv c$ for some constant $c\ge0$. We pursued three sub-routes from the
skeleton; **none closes rigorously**, and we report each honestly.

### (a) Swapped two-window intersection — refinement only, not a kill.
$(\dagger)$ bounds $|g(x)-g(y)|$ by the *smaller* of the two window widths
$(x-f(y))^{2}$ and $(y-f(x))^{2}$, normalized by the common positive
denominator $g(x)+g(y)+2x+2y$. The two roots
$x=f(y)=y+g(y)$ and $y=f(x)=x+g(x)$ (equivalently $x=y-g(x)$) are genuinely
*distinct* when $g(x)+g(y)\ne0$ (which holds as soon as either value is
positive). To turn $(\dagger)$ into a contradiction one would need, for a fixed
pair with $g(x)\ne g(y)$, a way to make *both* window widths small
**simultaneously** — i.e. to find a parametric family of pairs approaching the
two distinct roots at once. No such family is constructible from the
hypotheses without additional regularity (continuity / monotonicity) of $g$,
which the problem does not provide. The refinement stands; the kill does not.

### (b) Simultaneous-small / fixed-point argument — no IVT available.
The two windows collapse *simultaneously* exactly when $x=f(y)$ AND $y=f(x)$,
which is equivalent to $g(x)+g(y)=0$, i.e. $g(x)=g(y)=0$ (under $g\ge0$). A
near-simultaneous collapse would drive $|g(x)-g(y)|$ to zero while the
disparity was supposed nonzero — contradiction. To make this rigorous one needs
existence of a near-fixed-point of the continuous map
$(x,y)\mapsto(f(y),f(x))$ near the diagonal, typically via the intermediate
value theorem. **The hypotheses give no continuity of $f$** (nor of $g$), so the
IVT cannot be invoked. This sub-route is conjectural and is left open.

### (c) Optimization "bound" — shown to be a NON-result.
The skeleton proposed bounding $\min\{(x-f(y))^{2},(y-f(x))^{2}\}$ by
$\bigl(\frac{g(x)+g(y)}{2}\bigr)^{2}$, "attained at $d=(g(y)-g(x))/2$" with
$d=x-y$. We checked this carefully. Writing $x-f(y)=d-g(y)$ and
$y-f(x)=-(d+g(x))$, the two quadratics $(d-g(y))^{2}$ and $(d+g(x))^{2}$ do
*intersect* at $d=\frac{g(y)-g(x)}{2}$, where both equal
$\bigl(\frac{g(x)+g(y)}{2}\bigr)^{2}$. But this is a statement about the
*minimum over a free parameter $d$*; for a **fixed given pair** $(x,y)$ the
value $d=x-y$ is determined and need not be near the intersection. In fact for
$|d|$ large both quadratics exceed $\bigl(\frac{g(x)+g(y)}{2}\bigr)^{2}$ (e.g.
$g(x)=g(y)=1$, $d=100$ gives min $=9801\gg1$). Hence the inequality
$\min\le(\frac{g(x)+g(y)}{2})^{2}$ is **not** a universal bound on the disparity
at a fixed pair, and yields no kill. We retract this sub-route.

### Honest status of the kill.
The master squeeze $(\star)$ is numerically extremely rigid: every non-constant
perturbation we tested (periodic $g=c+\varepsilon\sin(2\pi x/c)$; decaying
$g=c+\varepsilon e^{-x}$, $c+\varepsilon/(1+x)$; growing $c+\varepsilon x/(1+x)$)
violates $(\star)$, often by orders of magnitude, for $\varepsilon$ as small as
$0.01$. The rigidity is real and is exactly what the other approaches
(`orbit-monotonicity-sandwich`, `density-contradiction`) exploit by importing
$(\star)$ and adding *structural* input (monotonicity trapping / Kronecker
density). But a **pure one-move algebraic kill from $(\star)$ plus $g\ge0$
alone** is not established here. We do **not** claim it. The gap is recorded.

If the direct kill were to close, the conclusion would be immediate: $(\star)$
forcing $g(x)=g(y)$ for all $x,y$ gives $g\equiv c$; combined with $g\ge0$ this
yields $c\ge0$, and the exhibit (step below) confirms admissibility. Until
then, this approach is a **lemma-provider**, not a complete solution.

---

## Exhibit (family verification) — PROVEN
For $f(x)=x+c$, $c\ge0$: $g\equiv c\ge0$, so $(\star)$ reads
$0\cdot(\cdots)\le(x-y-c)^{2}$, i.e. $0\le(x-y-c)^{2}$ — automatic. Equivalently,
the original chain is the classical QM-AM–AM-GM sandwich on the pair
$(x,\,y+c)$:
$$\sqrt{\tfrac{x^{2}+(y+c)^{2}}{2}}\ge\frac{x+(y+c)}{2}\ge\sqrt{x(y+c)},$$
where the left inequality is **QM-AM** and the right is **AM-GM**
(knowledge_base: Standard inequalities — AM-GM, QM-AM), both with equality iff
$x=y+c$. Hence every $f(x)=x+c$, $c\ge0$, is a solution. ∎

(No separate $g\ge0$ derivation is given here — that is the orbit
forward-positivity lemma owned by the other approaches; the Master Squeeze
Lemma above is stated so as to be importable with or without it.)

---

## Key lemmas (claim + mechanism)
- **Master SOS identity** $U+L=(x-f(y))^{2}/2$,
  $U-L=-(g(x)-g(y))(g(x)+g(y)+2x+2y)/2$ — by direct polynomial expansion
  (completing the square); PROVEN above, verified symbolically.
- **Master equivalence (both directions)** — by the Fact
  $U,L\ge0\iff U+L\ge|U-L|$ plus the SOS identity; PROVEN above.
- **Reduced master squeeze $(\star)$ under $g\ge0$** — second factor positive;
  PROVEN above.
- **Swapped two-window min $(\dagger)$** — by applying $(\star)$ to $(x,y)$ and
  $(y,x)$; PROVEN (refinement, not a kill).
- **Orbit invariance $g(f(y))=g(y)$ derivable from $(\star)$** — by the equality
  case $x=f(y)$; PROVEN (corollary, not a kill).
- **Direct kill from $(\star)$ + $g\ge0$ alone** — CONJECTURAL/OPEN; sub-routes
  (a) no simultaneous-collapse family without regularity, (b) no IVT without
  continuity, (c) optimization "bound" retracted as a non-result. Honestly
  flagged.

## Open gaps
- **Direct algebraic kill (step 4):** conjectural/open. The master squeeze is
  numerically rigid but a one-move proof that $(\star)+g\ge0\Rightarrow g$
  constant is not found. Sub-routes (a),(b) need regularity the problem does not
  give; sub-route (c) is a non-result.
- **Does not use $g\circ f=g$ as a *kill* input** (only as a derivable
  corollary). If the kill is later folded into orbit structure, this approach
  merges with `orbit-monotonicity-sandwich` — flagged so the field does not
  silently collapse.

## Cases to cover
- $g\equiv0$ ($c=0$): $(\star)$ is $0\le(x-y)^{2}$; automatic. Exhibit verified.
- $g\equiv c>0$: $(\star)$ is $0\le(x-y-c)^{2}$; automatic. Exhibit verified.
- Nonconstant $g$: the kill targets this and is OPEN; numerical evidence says
  such $g$ violates $(\star)$, but no proof.

## Watch out for
- Do NOT present the direct kill as proved. It is conjectural; the optimization
  "bound" (4c) is retracted as a non-result, not merely inconclusive.
- Orbit amplification along $(\star)$ GROWS the RHS ($\sim n^{2}$ on forward
  iterates) — useless for the kill; do not pursue.
- The master squeeze *contains* orbit invariance as its equality case; it is
  strictly stronger than orbit invariance alone, but "stronger than a relation
  admitting nonconstant solutions" is not itself a kill.

## Approaches tried
- (round 2, founding) Master-SOS direct kill. Open gap: the direct algebraic
  kill from the master inequality is conjectural; sub-route (c) retracted.
  Certain proven output: the **Master Squeeze Lemma** (SOS identity + both-way
  equivalence + reduced form under $g\ge0$ + swapped-min corollary), ready for
  certification into `results/imo-2026-05/lemmas/master-squeeze.md` and
  importable by the other three approaches as their squeeze engine.

## Promotable lemmas
- **Master Squeeze Lemma** — statement: the two-sided chain
  $\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\ge\frac{f(x)+y}{2}\ge\sqrt{xf(y)}$ (for all
  $x,y>0$) is equivalent, via the SOS identity
  $U+L=\frac{(x-f(y))^{2}}{2}$,
  $U-L=-\frac{(g(x)-g(y))(g(x)+g(y)+2x+2y)}{2}$ and the biconditional
  $U,L\ge0\iff U+L\ge|U-L|$, to
  $\bigl|(g(x)-g(y))(g(x)+g(y)+2x+2y)\bigr|\le(x-f(y))^{2}$; under $g\ge0$,
  to $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^{2}$. Proved in full
  (both directions) above in this file. Ready for certification into
  `results/imo-2026-05/lemmas/master-squeeze.md`.
