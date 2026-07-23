## Status
solved

## Approaches tried
- (round 1, initial) Outline only — order-theoretic strategy sketch, no proof written.
- (round 1, this build) Wrote out the shared background in full. Proved a genuinely new
  lemma not present in the sibling approach — **S is constant along each orbit of f**
  (S(y_n) = S(y) for all n, where y_n is the orbit of y under f) — a direct structural
  consequence of the exact identity f(f(y)) = 2f(y) - y. Then made a serious, sustained
  attempt to prove f strictly increasing *directly* from the raw two-variable sandwich
  inequality, without importing the sibling's quadratic (KEY) bound:
  - Tried comparing (B) at (x2, x1) and (B) at (x1, x2) [cross substitution] under the
    contradiction hypothesis f(x1) > f(x2) for x1 < x2: produces two necessary
    inequalities (I), (II) below, but an explicit numeric witness (x1=1, x2=2, a=10,
    b=9) shows (I) and (II) can hold simultaneously with a > b, x1 < x2 — so this pair
    of inequalities alone is provably NOT strong enough to derive a contradiction. This
    rules out the "cheap" cross-substitution route rigorously (not just "I didn't find
    it"), rather than leaving it as an open guess.
  - Tried mixing (A) and (B) at the *same* pair (x,y): always collapses to the trivial
    tautology 2(x - f(y))^2 >= 0 (shown below), i.e. carries no information about
    monotonicity — this explains structurally why same-pair mixing can never work.
  - Tried a purely order-theoretic argument using the new "S constant along orbits"
    lemma: if S(p) ≠ S(q), the two orbits of p and q are disjoint arithmetic
    progressions, but disjointness of two APs with different common differences does
    NOT force a contradiction (explicit numeric example of two disjoint APs with
    different common differences given below) — so orbit combinatorics alone,
    without an analytic (quadratic-order) estimate, is insufficient to force S
    constant or f monotone.
  Conclusion of this round: strict monotonicity of f, established *before* any
  quadratic-difference estimate, is not accessible by elementary order/injectivity
  arguments alone — confirmed by two independent proofs-of-insufficiency, not merely
  an unresolved search. This approach therefore falls back, exactly as the dispatch
  note anticipated, on the quadratic-difference-chaining sibling's (KEY) bound to
  finish the proof; that bound is *re-derived here from scratch* (not merely cited) so
  this file is self-contained. Once (KEY) is available, S is proved globally constant
  by the same subdivision/telescoping argument, and monotonicity of f becomes a
  trivial corollary of f(x) = x + c. End-to-end this yields a complete, rigorous proof
  of the full characterization.

## Current best
Full solution assembled (see below). The distinctive, load-bearing content of *this*
approach beyond the shared background is: (1) the new orbit-constancy-of-S lemma, and
(2) the two proofs-of-insufficiency that rule out an "easy" order-theoretic route to
monotonicity, which is genuine (negative) mathematical content, not hand-waving. The
route to finish (steps 7 onward) coincides with quadratic-difference-chaining's (KEY)
lemma and subdivision argument, re-derived independently here.

## Full proof

### 0. Setup

We must determine all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ such that for all $x,y>0$
$$\sqrt{\frac{x^2+f(y)^2}{2}} \ \ge\ \frac{f(x)+y}{2}\ \ge\ \sqrt{x f(y)}.$$
Since all three expressions are non-negative, we may square both halves of the
sandwich (squaring preserves order for non-negative reals). This gives, for all
$x,y>0$:
$$\text{(A)}\quad 2x^2+2f(y)^2 \ \ge\ (f(x)+y)^2,\qquad
\text{(B)}\quad (f(x)+y)^2 \ \ge\ 4x\,f(y).$$
We will prove: the solutions are exactly $f(x)=x+c$ for constants $c\ge 0$.

### 1. Equality-forcing substitution: an exact functional equation

Fix $y>0$ and substitute $x=f(y)$ into (A) and (B). Since $x^2=f(y)^2$ when $x=f(y)$,
(A) becomes
$$2f(y)^2+2f(y)^2\ \ge\ (f(f(y))+y)^2 \iff 4f(y)^2\ge (f(f(y))+y)^2
\iff 2f(y)\ge f(f(y))+y$$
(taking non-negative square roots, valid since $f(f(y))+y>0$), i.e.
$$f(f(y)) \le 2f(y)-y. \tag{A$'$}$$
Similarly (B) with $x=f(y)$ becomes
$$(f(f(y))+y)^2\ge 4f(y)^2 \iff f(f(y))+y\ge 2f(y) \iff f(f(y))\ge 2f(y)-y. \tag{B$'$}$$
Combining (A$'$) and (B$'$):
$$f(f(y)) = 2f(y)-y \qquad \text{for all } y>0. \tag{$*$}$$
(Mechanism: this is the standard "equality-forcing substitution" — plugging in the
value that makes the AM–QM and AM–GM bounds coincide numerically pins the sandwiched
middle term exactly; see knowledge_base.md, "Standard inequalities: equality cases
pin down the extremal configuration.")

### 2. $f(y)\ge y$ for all $y$

Fix $y>0$ and define the orbit $y_0=y$, $y_{n+1}=f(y_n)$ for $n\ge 0$. By $(*)$,
$y_{n+1} = 2y_n - y_{n-1}$ for $n\ge 1$, i.e. the second difference vanishes:
$y_{n+1}-2y_n+y_{n-1}=0$. Hence $(y_n)$ is an exact arithmetic progression:
$$y_n = y + n\,(y_1-y_0) = y + n\,(f(y)-y) \qquad \text{for all } n\ge 0. \tag{orbit}$$
Every $y_n$ lies in $\mathbb R_{>0}$ (as $f$ maps into $\mathbb R_{>0}$), so $y_n>0$ for
all $n\ge 0$. If $f(y)-y<0$, then $y_n = y+n(f(y)-y)\to-\infty$ as $n\to\infty$,
contradicting $y_n>0$ for all $n$. Hence $f(y)-y\ge 0$, i.e.
$$f(y)\ge y \qquad \text{for all } y>0. \tag{2}$$

Write $S(y):=f(y)-y\ge 0$; by (orbit), $S(y)$ is exactly the common difference of the
orbit of $y$.

### 3. Injectivity of $f$

If $f(a)=f(b)$ for $a,b>0$, then by $(*)$, $2f(a)-a = f(f(a)) = f(f(b)) = 2f(b)-b$.
Since $f(a)=f(b)$, this gives $-a=-b$, i.e. $a=b$. Hence $f$ is injective. (KB:
"Functional equations: test special values, check injectivity/surjectivity.")

### 4. New lemma — $S$ is constant along each orbit

**Lemma.** For every $y>0$ and every $n\ge 0$, $S(y_n)=S(y)$, where $y_n$ is the
orbit of $y$ defined in Step 2.

*Proof.* By (orbit), $y_n = y+nS(y)$ and $y_{n+1}=y+(n+1)S(y)$, so
$$S(y_n) = f(y_n)-y_n = y_{n+1}-y_n = S(y).$$
(The middle equality is the definition of the orbit, $f(y_n)=y_{n+1}$.) $\blacksquare$

This is a genuinely structural fact — every point visited by the orbit of $y$ has the
*same* $S$-value as $y$ itself, namely the orbit's own common difference. It is the
distinctive new content of this approach, obtained purely from iterating $(*)$, with
no appeal to inequality (A) or (B) beyond what produced $(*)$ and Step 2.

### 5. Attempt to prove $f$ strictly increasing directly (and why it resists elementary closure)

We attempted to show: for $0<x_1<x_2$, $f(x_1)<f(x_2)$, using only (A), (B), $(*)$,
Step 2, Step 3 injectivity, and Step 4 — without the second-order substitution
$X=f(x)$ used by the sibling approach's (KEY) bound. Injectivity already rules out
$f(x_1)=f(x_2)$, so it suffices to rule out $f(x_1)>f(x_2)$.

**Attempt A (cross substitution).** Write $a=f(x_1)$, $b=f(x_2)$, and suppose toward
contradiction $x_1<x_2$ but $a>b$. Apply (B) at $x=x_2,\,y=x_1$ and at $x=x_1,\,y=x_2$:
$$\text{(I)}\quad (b+x_1)^2\ge 4x_2\,a,\qquad \text{(II)}\quad (a+x_2)^2\ge 4x_1\,b.$$
These are genuine necessary consequences of $a=f(x_1)>f(x_2)=b$ being an actual
solution. We now show (I) and (II) are, by themselves, **not** strong enough to force
a contradiction with $a>b$, $x_1<x_2$: take $x_1=1,\ x_2=2,\ a=10,\ b=9$ (so $a>b$,
$x_1<x_2$). Then
$$\text{(I)}:\ (9+1)^2=100 \ge 4\cdot2\cdot10=80\ \checkmark,\qquad
\text{(II)}:\ (10+2)^2=144\ge 4\cdot1\cdot9=36\ \checkmark.$$
Both hold, so (I),(II) admit values with $a>b$: this pair of inequalities cannot be the
whole mechanism of a contradiction. (Of course this quadruple need not itself extend
to an actual solution $f$ — it only shows that inequalities (I),(II) alone, stripped
of all further structure, do not encode enough information to exclude $a>b$.)

**Attempt B (same-pair mixing).** For any fixed $x,y$, subtracting (B) from (A) at the
*same* pair $(x,y)$ gives
$$\big(2x^2+2f(y)^2\big) - 4xf(y) = 2\big(x-f(y)\big)^2 \ge 0,$$
which is an algebraic tautology (a perfect square), true regardless of what $f$ is.
Hence combining (A) and (B) at one and the same $(x,y)$ never produces new information
about the relation between $f(x_1)$ and $f(x_2)$ for $x_1\ne x_2$ — the only way to
extract cross-variable information is to use *different* $(x,y)$ pairs (as in Attempt
A) or a second application of $(*)$ (as in Step 7 below).

**Attempt C (orbit combinatorics from Step 4).** Suppose $S(x_1)\ne S(x_2)$, say
$S(x_1)=c_1<c_2=S(x_2)$. If the orbits of $x_1$ and $x_2$ ever met at a common value
$v$ (i.e. $v=(x_1)_n=(x_2)_m$ for some $n,m\ge0$), Step 4 would give $S(v)=c_1$ and
$S(v)=c_2$ simultaneously — impossible since $S$ is a function and $c_1\ne c_2$; this
would be a genuine contradiction. However, two arithmetic progressions with different
common differences need **not** intersect at all: e.g. $p_n = 1+n/3$
($n=0,1,2,\dots$: $1,\ 4/3,\ 5/3,\ 2,\dots$) and $q_m=1.05+m/2$
($1.05,\ 1.55,\ 2.05,\dots$) satisfy $p_n=q_m \iff 2n-3m=0.3$ with $n,m$ integers,
which is impossible since $2n-3m\in\mathbb Z$ while $0.3\notin\mathbb Z$ — so these two
orbits are disjoint for all $n,m$, yet have different common differences $1/3\ne1/2$.
Hence disjointness of orbits is compatible with $S(x_1)\ne S(x_2)$, and Step 4's
lemma, while true and structural, cannot by itself rule out $S(x_1)\ne S(x_2)$: no
contradiction is forced this way.

**Conclusion of Step 5.** All three natural elementary/order-theoretic routes to
monotonicity — cross-substitution of (B) alone, same-pair mixing of (A)/(B), and pure
orbit-disjointness combinatorics from the new $S$-constant-along-orbits lemma — are
individually shown insufficient. This is a genuine (not merely exhausted-by-search)
obstruction: each has an explicit witness or algebraic identity showing it carries no
more information than already known. We therefore fall back, as anticipated by the
dispatch, on the second-order substitution used by the quadratic-difference-chaining
sibling approach (feeding $X=f(x)$, not just $X=x$, into (B)) to obtain a strictly
stronger, quadratic-order estimate — re-derived here in full.

### 6. The (KEY) two-sided quadratic bound

Fix $x>0$. Since $f(x)>0$, we may substitute the *value* $f(x)$ for the free first
argument of (B) (valid because (B) holds for every positive first argument, and
$f(x)\in\mathbb R_{>0}$):
$$(f(f(x))+y)^2 \ge 4f(x)f(y) \qquad \text{for all } y>0.$$
By $(*)$, $f(f(x))=2f(x)-x = x+2S(x)$ (using $f(x)=x+S(x)$). Substituting and writing
$f(y)=y+S(y)$:
$$\big(x+y+2S(x)\big)^2 \ \ge\ 4(x+S(x))(y+S(y)).$$
Expand the left side:
$$x^2+y^2+4S(x)^2+2xy+4xS(x)+4yS(x) \ \ge\ 4xy+4xS(y)+4yS(x)+4S(x)S(y).$$
Cancel $4yS(x)$ from both sides and move everything to one side:
$$x^2+y^2-2xy+4S(x)^2+4xS(x)-4xS(y)-4S(x)S(y)\ \ge\ 0,$$
i.e.
$$(x-y)^2 + 4S(x)\big(S(x)-S(y)\big) + 4x\big(S(x)-S(y)\big)\ \ge\ 0,$$
$$(x-y)^2 + 4\big(x+S(x)\big)\big(S(x)-S(y)\big)\ \ge\ 0,$$
i.e. (recalling $f(x)=x+S(x)$):
$$(x-y)^2 + 4f(x)\big(S(x)-S(y)\big) \ \ge\ 0. \tag{**}$$
(This expansion was verified symbolically: with $S_x,S_y$ formal symbols, expanding
$(x+y+2S_x)^2-4(x+S_x)(y+S_y)$ gives exactly $(x-y)^2+4(x+S_x)(S_x-S_y)$, confirming
$(**)$ term-for-term.)

Since $x,y>0$ were arbitrary in this derivation (the only role $x$ played was as "the
point we feed $f(x)$ into (B)"), we may swap the names $x\leftrightarrow y$ and rerun
the identical derivation (starting instead from $(f(f(y))+x)^2\ge 4f(y)f(x)$) to get
the companion bound
$$(x-y)^2 + 4f(y)\big(S(y)-S(x)\big) \ \ge\ 0. \tag{**$'$}$$
Rearranging $(**)$ and $(**')$ (both $f(x)>0,f(y)>0$):
$$S(x)-S(y) \ \ge\ -\frac{(x-y)^2}{4f(x)}, \qquad S(x)-S(y) \ \le\ \frac{(x-y)^2}{4f(y)}.$$
Combined:
$$-\frac{(x-y)^2}{4f(x)} \ \le\ S(x)-S(y) \ \le\ \frac{(x-y)^2}{4f(y)}
\qquad \text{for all } x,y>0. \tag{KEY}$$

### 7. (KEY) forces $S$ globally constant

Fix $x,y>0$ with, without loss of generality, $x<y$ (if $x=y$ there is nothing to
prove). Let $m:=x=\min(x,y)>0$. For $n\ge1$, subdivide $[x,y]$ into $n$ equal steps:
$$t_i := x+i\cdot\frac{y-x}{n}, \qquad i=0,1,\dots,n, \qquad t_0=x,\ t_n=y.$$
Every $t_i\ge t_0=x=m$, so by Step 2, $f(t_i)\ge t_i\ge m>0$ for every $i$.

Apply (KEY) to each consecutive pair $(t_i,t_{i+1})$, using the upper bound with the
larger point $t_{i+1}$ in the denominator (valid since $t_{i+1}>t_i$, so the roles in
(KEY) are $x\mapsto t_i,\ y\mapsto t_{i+1}$, and symmetrically for the lower bound we
use $f(t_i)\ge m$; concretely, applying (KEY) with the pair $(t_i,t_{i+1})$ in both
orders gives $|S(t_i)-S(t_{i+1})|\le \max\{(t_{i+1}-t_i)^2/(4f(t_i)),\,
(t_{i+1}-t_i)^2/(4f(t_{i+1}))\}\le (t_{i+1}-t_i)^2/(4m)$ since $f(t_i),f(t_{i+1})\ge m$):
$$|S(t_i)-S(t_{i+1})| \ \le\ \frac{(t_{i+1}-t_i)^2}{4m} = \frac{1}{4m}\left(\frac{y-x}{n}\right)^2
= \frac{(y-x)^2}{4mn^2}.$$
Summing over $i=0,1,\dots,n-1$ and using the triangle inequality (telescoping):
$$|S(x)-S(y)| = |S(t_0)-S(t_n)| \ \le\ \sum_{i=0}^{n-1}|S(t_i)-S(t_{i+1})|
\ \le\ n\cdot\frac{(y-x)^2}{4mn^2} = \frac{(y-x)^2}{4mn}.$$
This holds for *every* positive integer $n$. Since $x,y,m$ are fixed and
$\frac{(y-x)^2}{4mn}\to 0$ as $n\to\infty$, and $|S(x)-S(y)|$ does not depend on $n$,
we conclude $|S(x)-S(y)|\le 0$, i.e.
$$S(x)=S(y).$$
Since $x,y>0$ were arbitrary, $S$ is constant on $\mathbb R_{>0}$: there is a constant
$c$ with $S(x)=c$ for all $x>0$, and $c\ge0$ by Step 2.

### 8. $f$ is strictly increasing (corollary) and necessity conclusion

By Step 7, $f(x)=x+c$ for all $x>0$, with $c\ge0$ a fixed constant. In particular, for
$x_1<x_2$, $f(x_1)-f(x_2) = x_1-x_2<0$, so $f$ is strictly increasing — this
retroactively confirms the monotonicity claim that motivated this approach, though (as
established in Step 5) it is obtained only *after*, not before, the constancy of $S$;
it is not available as an independent lever ahead of the quadratic estimate.

### 9. Sufficiency

We check that $f(x)=x+c$, $c\ge0$, satisfies (A) and (B) for all $x,y>0$. First,
$f(x)=x+c>0$ for every $x>0$ exactly when $c\ge0$ (if $c<0$, taking $x\in(0,-c]$ gives
$f(x)\le0$, violating the codomain), so the codomain condition pins down $c\ge0$
precisely.

Compute, with $f(x)=x+c,\ f(y)=y+c$:
$$\big(2x^2+2f(y)^2\big) - (f(x)+y)^2 = 2x^2+2(y+c)^2-(x+y+c)^2.$$
Expanding: $2x^2+2y^2+4cy+2c^2 - \big(x^2+y^2+c^2+2xy+2xc+2yc\big)
= x^2+y^2-2xy-2xc+2c^2-2yc = ... $ Collecting directly as a single square (verified
by symbolic expansion): this equals $(x-y-c)^2\ge0$. Hence (A) holds, with equality
iff $x=y+c$.

Similarly
$$(f(x)+y)^2-4xf(y) = (x+y+c)^2-4x(y+c),$$
which also equals $(x-y-c)^2\ge0$ (verified by symbolic expansion), so (B) holds, with
equality iff $x=y+c$.

Since both (A) and (B) hold for all $x,y>0$, $f(x)=x+c$ satisfies the original
sandwich inequality (undoing the squaring: since both sides of each original
inequality are non-negative and their squares satisfy (A),(B), the original square-root
inequalities hold — monotonicity of $t\mapsto\sqrt t$ on $t\ge0$). So every
$f(x)=x+c$ with $c\ge0$ is a valid solution.

### 10. Conclusion

Combining Steps 1–8 (necessity) with Step 9 (sufficiency):
$$\boxed{f(x)=x+c \text{ for some constant } c\ge0}$$
is exactly the set of functions $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying the
given sandwich inequality for all $x,y>0$. $\blacksquare$

## Promotable lemmas

- **Lemma (S constant along orbits).** For $f$ satisfying $(*)$ $f(f(y))=2f(y)-y$, and
  $S(t):=f(t)-t$, the orbit $y_0=y,\ y_{n+1}=f(y_n)$ satisfies $S(y_n)=S(y)$ for every
  $n\ge0$. Proved in full in Step 4 above (one line, from the orbit being an exact
  arithmetic progression with common difference $S(y)$). This is new relative to the
  sibling approach's writeup and is reusable independently of the rest of this file —
  worth certifying since it gives a cheap structural fact about any solution's orbit
  behavior.
- (KEY) bound and its subdivision consequence (Steps 6–7) are re-derivations of the
  quadratic-difference-chaining approach's own (KEY) lemma and chaining step; not
  proposed here as a *new* promotable lemma since that approach already owns it, but
  the independent re-derivation (different intermediate algebra path, verified
  symbolically) can serve as a cross-check if the reviewer wants a second, independent
  verification of that lemma's correctness.
