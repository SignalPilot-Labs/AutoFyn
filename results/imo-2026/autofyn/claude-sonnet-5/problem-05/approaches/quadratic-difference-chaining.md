## Status
solved

## Approaches tried
- Round 1 (this round): filled in the outline in full. Derived the equality-forcing
  identity f(f(y)) = 2f(y) - y from the equality case x = f(y) of the sandwich; used the
  induced exact arithmetic progression to prove f(y) >= y for all y; derived a genuinely
  new two-variable quadratic estimate (KEY) on S(x) := f(x) - x by substituting X = f(x)
  into the geometric-mean-side inequality and using the exact identity; closed the
  remaining gap (promoting the local quadratic bound to global constancy of S) with an
  explicit n-fold subdivision / telescoping-sum argument, written out with full
  epsilon/n bookkeeping. Verified all algebraic identities used (the expansion in the
  derivation of (KEY), and both sufficiency identities) symbolically with sympy as a
  computational check; the written proof below re-derives each identity by hand as a
  proof step, not merely by citing the numeric check. Outcome: complete proof, both
  necessity and sufficiency, with the final answer f(x) = x + c, c >= 0, verified by
  direct substitution into both halves of the original inequality. No gaps remain.

## Current best
Complete: see Full proof below.

## Full proof

**Problem.** Determine all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ such that for all
$x,y\in\mathbb R_{>0}$,
$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x f(y)}. \tag{$\star$}$$

**Answer.** The solutions are exactly the functions $f(x) = x + c$ for a constant
$c\ge 0$.

Throughout, all quantities $x,y,f(x),f(y),\dots$ that appear are positive reals (since
$f$ maps $\mathbb R_{>0}\to\mathbb R_{>0}$), so every squaring step below is an
if-and-only-if step (for $u,v\ge 0$, $u\ge v \iff u^2\ge v^2$), and every square root
extraction from an equality of squares of nonnegative numbers is valid.

### Step 0: Squaring the sandwich

Since every term in $(\star)$ is a nonnegative real (all of $x, f(x), y, f(y)$ are
positive), and $t\mapsto t^2$ is increasing on $[0,\infty)$, squaring both halves of
$(\star)$ is equivalent to the original statement. This yields two inequalities, for all
$x,y>0$:
$$2x^2 + 2f(y)^2 \;\ge\; \big(f(x)+y\big)^2, \tag{A}$$
$$\big(f(x)+y\big)^2 \;\ge\; 4x f(y). \tag{B}$$

### Step 1: The equality-forcing substitution $x = f(y)$

Fix $y > 0$ and substitute $x = f(y)$ (legitimate since $f(y) \in \mathbb R_{>0}$) into
(A) and (B).

In (A): $2f(y)^2 + 2f(y)^2 \ge (f(f(y))+y)^2$, i.e.
$$4f(y)^2 \ge \big(f(f(y))+y\big)^2. \tag{A$'$}$$

In (B): $(f(f(y))+y)^2 \ge 4f(y)\cdot f(y) = 4f(y)^2$, i.e.
$$\big(f(f(y))+y\big)^2 \ge 4f(y)^2. \tag{B$'$}$$

Combining (A$'$) and (B$'$): $\big(f(f(y))+y\big)^2 = 4f(y)^2$. Both
$f(f(y))+y$ and $2f(y)$ are positive reals, and their squares are equal, so (taking the
unique nonnegative square root of both sides) they are equal:
$$f(f(y)) + y = 2f(y), \qquad\text{i.e.}\qquad f(f(y)) = 2f(y) - y \quad\text{for all } y>0. \tag{$*$}$$

This is the "equality case pins down the extremal configuration" mechanism: for the
specific choice $x=f(y)$, the QM-side upper bound and the GM-side lower bound coincide
(both equal $f(y)$), which forces the sandwiched middle term $\frac{f(x)+y}{2}$ to equal
$f(y)$ exactly, i.e. forces $(\star)$'s inequalities to become equalities at this point.

### Step 2: $f(y) \ge y$ for every $y>0$

Fix $y>0$ and define a sequence $(y_n)_{n\ge 0}$ by $y_0 := y$ and
$y_{n+1} := f(y_n)$. Since $f:\mathbb R_{>0}\to\mathbb R_{>0}$, an easy induction shows
$y_n > 0$ for every $n\ge 0$: $y_0=y>0$ by hypothesis, and if $y_n>0$ then
$y_{n+1}=f(y_n)$ is well-defined and positive because $f$'s codomain is
$\mathbb R_{>0}$.

Apply $(*)$ with $y$ replaced by $y_n$ (valid since $y_n>0$): $f(f(y_n)) = 2f(y_n)-y_n$,
i.e.
$$y_{n+2} = 2y_{n+1} - y_n \qquad \text{for all } n \ge 0.$$
This is exactly the recursion characterizing an arithmetic progression: the second
difference $y_{n+2}-2y_{n+1}+y_n$ vanishes identically. Solving the recursion (or
proving by induction on $n$) gives the closed form
$$y_n = y_0 + n(y_1-y_0) = y + n\big(f(y)-y\big) \qquad \text{for all } n\ge 0.$$
(Induction check: true for $n=0$; if $y_n = y+n(f(y)-y)$ and
$y_{n-1}=y+(n-1)(f(y)-y)$ for $n\ge1$, then $y_{n+1}=2y_n-y_{n-1}
= 2y+2n(f(y)-y) - y - (n-1)(f(y)-y) = y+(n+1)(f(y)-y)$, closing the induction; the base
case $n=1$ is immediate from $y_1=f(y)=y+(f(y)-y)$.)

Suppose, for contradiction, that $f(y) < y$, i.e. the common difference
$d := f(y)-y$ is negative. Then $y_n = y + nd \to -\infty$ as $n\to\infty$, so for
$n$ large enough $y_n \le 0$. But we showed $y_n>0$ for every $n$ — contradiction.
Hence $d \ge 0$, i.e.
$$f(y) \ge y \qquad \text{for all } y > 0. \tag{2}$$

### Step 3: Injectivity of $f$ (recorded for completeness; not needed later)

If $f(a) = f(b)$ for some $a,b>0$, then $f(f(a))=f(f(b))$ trivially. By $(*)$,
$2f(a)-a = 2f(b)-b$. Since $f(a)=f(b)$, this gives $-a=-b$, i.e. $a=b$. So $f$ is
injective. (This fact is not used in the argument below; it is recorded because it
falls out of $(*)$ for free.)

### Step 4: The key two-sided quadratic bound on $S(x) := f(x)-x$

Define $S:\mathbb R_{>0}\to\mathbb R$ by $S(t) := f(t)-t$; by Step 2, $S(t)\ge 0$ for
all $t>0$, and $f(t) = t+S(t)$.

Fix $x,y>0$. Apply inequality (B) with its free "first argument" set to $f(x)$ (this is
legitimate: (B) holds for *every* pair of positive reals, and $f(x)>0$) and second
argument $y$:
$$\big(f(f(x))+y\big)^2 \;\ge\; 4f(x)f(y).$$
By $(*)$, $f(f(x)) = 2f(x)-x = (x+S(x)) \cdot 2 - x = x + 2S(x)$. Substituting,
$$\big(x+2S(x)+y\big)^2 \;\ge\; 4f(x)f(y),$$
i.e., writing the left side as $(x+y+2S(x))^2$,
$$(x+y+2S(x))^2 \;-\; 4(x+S(x))(y+S(y)) \;\ge\; 0. \tag{4}$$

**Expanding the left side of (4).** Expand $(x+y+2S(x))^2$:
$$(x+y+2S(x))^2 = (x+y)^2 + 4S(x)(x+y) + 4S(x)^2.$$
Expand $4(x+S(x))(y+S(y))$:
$$4(x+S(x))(y+S(y)) = 4xy + 4xS(y) + 4yS(x) + 4S(x)S(y).$$
Subtracting,
$$(x+y+2S(x))^2 - 4(x+S(x))(y+S(y))
= \underbrace{(x+y)^2-4xy}_{=(x-y)^2} + \big(4S(x)(x+y)-4yS(x)\big) - 4xS(y) + 4S(x)^2 - 4S(x)S(y).$$
Now $4S(x)(x+y)-4yS(x) = 4S(x)\cdot x$, so the middle terms combine to
$4xS(x) - 4xS(y) = 4x\big(S(x)-S(y)\big)$, and the last two terms combine to
$4S(x)^2-4S(x)S(y) = 4S(x)\big(S(x)-S(y)\big)$. Altogether,
$$(x+y+2S(x))^2 - 4(x+S(x))(y+S(y)) = (x-y)^2 + 4\big(x+S(x)\big)\big(S(x)-S(y)\big)
= (x-y)^2 + 4f(x)\big(S(x)-S(y)\big).$$
(This algebraic identity was independently verified by symbolic expansion; it is
re-derived here from scratch by direct expansion, term by term.) Combined with (4),
this gives
$$(x-y)^2 + 4f(x)\big(S(x)-S(y)\big) \;\ge\; 0 \qquad \text{for all } x,y>0. \tag{**}$$

**The companion (swapped) bound.** Now apply (B) with first argument $f(y)$ and second
argument $x$ (again legitimate, since $f(y)>0$ and $x>0$):
$$\big(f(f(y))+x\big)^2 \ge 4f(y)f(x).$$
By $(*)$, $f(f(y)) = 2f(y)-y = y+2S(y)$, so $f(f(y))+x = x+y+2S(y)$, and the inequality
reads
$$(x+y+2S(y))^2 - 4(x+S(x))(y+S(y)) \ge 0.$$
This is *literally the same computation as above with the roles of $x$ and $y$
interchanged* (replace $x\leftrightarrow y$ everywhere in the derivation of $(**)$: the
substitution $X=f(y)$ instead of $X=f(x)$, then $f(f(y))=2f(y)-y$ instead of
$f(f(x))=2f(x)-x$). Running the identical expansion with $x,y$ swapped gives
$$(y-x)^2 + 4f(y)\big(S(y)-S(x)\big) \;\ge\; 0,$$
i.e., since $(y-x)^2=(x-y)^2$,
$$(x-y)^2 + 4f(y)\big(S(y)-S(x)\big) \;\ge\; 0 \qquad \text{for all } x,y>0. \tag{***}$$
(No extra hypothesis was used beyond $f(y)>0$, which holds unconditionally since $f$
maps into $\mathbb R_{>0}$.)

**Combining $(**)$ and $(***)$.** From $(**)$: $4f(x)(S(x)-S(y)) \ge -(x-y)^2$, so since
$f(x)>0$,
$$S(x)-S(y) \;\ge\; -\frac{(x-y)^2}{4f(x)}.$$
From $(***)$: $4f(y)(S(y)-S(x)) \ge -(x-y)^2$, i.e. $4f(y)(S(x)-S(y)) \le (x-y)^2$, so
since $f(y)>0$,
$$S(x)-S(y) \;\le\; \frac{(x-y)^2}{4f(y)}.$$
Together:
$$-\frac{(x-y)^2}{4f(x)} \;\le\; S(x)-S(y) \;\le\; \frac{(x-y)^2}{4f(y)}
\qquad \text{for all } x,y>0. \tag{KEY}$$

### Step 5: (KEY) forces $S$ to be globally constant

Fix $x,y>0$. If $x=y$ then trivially $S(x)=S(y)$, so assume without loss of generality
$x<y$ (the case $x>y$ is symmetric, since (KEY) is symmetric in the sense that swapping
$x,y$ throughout Steps 4–5 gives the same conclusion $S(x)=S(y)$). Let
$m := \min(x,y) = x > 0$.

For an integer $n\ge 1$, subdivide $[x,y]$ into $n$ equal parts: set
$$t_i := x + \frac{i(y-x)}{n}, \qquad i=0,1,\dots,n,$$
so $t_0=x$, $t_n=y$, and $t_{i+1}-t_i = \frac{y-x}{n} =: \Delta$ for every
$i=0,\dots,n-1$. Since $y>x$, each $t_i \ge t_0 = x = m > 0$, so $t_i \in \mathbb R_{>0}$
and by Step 2 (inequality (2)),
$$f(t_i) \;\ge\; t_i \;\ge\; m \qquad \text{for every } i=0,\dots,n.$$

Apply (KEY) to the pair $(t_i, t_{i+1})$ for each $i=0,\dots,n-1$:
$$-\frac{\Delta^2}{4f(t_i)} \;\le\; S(t_i)-S(t_{i+1}) \;\le\; \frac{\Delta^2}{4f(t_{i+1})}.$$
Since $f(t_i)\ge m$ and $f(t_{i+1})\ge m$, we have $\frac{1}{4f(t_i)} \le \frac{1}{4m}$
and $\frac{1}{4f(t_{i+1})}\le \frac{1}{4m}$, so
$$-\frac{\Delta^2}{4m} \;\le\; S(t_i)-S(t_{i+1}) \;\le\; \frac{\Delta^2}{4m},
\qquad\text{i.e.}\qquad
\big|S(t_i)-S(t_{i+1})\big| \;\le\; \frac{\Delta^2}{4m} = \frac{(y-x)^2}{4n^2 m}.$$

Telescoping the differences over $i=0,\dots,n-1$:
$$S(x)-S(y) = S(t_0)-S(t_n) = \sum_{i=0}^{n-1}\Big(S(t_i)-S(t_{i+1})\Big),$$
so by the triangle inequality,
$$\big|S(x)-S(y)\big| \;\le\; \sum_{i=0}^{n-1}\big|S(t_i)-S(t_{i+1})\big|
\;\le\; n\cdot\frac{(y-x)^2}{4n^2 m} \;=\; \frac{(y-x)^2}{4mn}.$$

This bound holds for **every** positive integer $n$, and the left side
$|S(x)-S(y)|$ does not depend on $n$. Since $x,y,m$ are fixed and
$\frac{(y-x)^2}{4mn}\to 0$ as $n\to\infty$, and $|S(x)-S(y)|$ is a fixed nonnegative
real number bounded above by a sequence tending to $0$, we conclude
$$|S(x)-S(y)| = 0, \qquad\text{i.e.}\qquad S(x)=S(y).$$

Since $x,y>0$ were arbitrary (the case $x=y$ was trivial and the case $x>y$ is symmetric
to $x<y$ by relabeling), $S$ is constant on $\mathbb R_{>0}$: there is a constant $c$
such that
$$S(x) = c \qquad \text{for all } x>0,$$
and by inequality (2) of Step 2 (applied at any single point, e.g. $x=1$),
$c = S(1) = f(1)-1 \ge 0$.

### Step 6: Necessity conclusion

Since $S(x)=f(x)-x=c$ for all $x>0$ with $c\ge 0$ constant, every solution $f$ of
$(\star)$ has the form
$$f(x) = x+c \qquad \text{for all } x>0, \text{ for some constant } c \ge 0.$$

### Step 7: Sufficiency — every $f(x)=x+c$, $c\ge0$, is a solution

Let $c \ge 0$ and $f(x) := x+c$ for $x>0$. First, $f$ maps $\mathbb R_{>0}$ into
$\mathbb R_{>0}$: for $x>0$, $f(x)=x+c \ge x > 0$. (This uses $c\ge 0$; if $c<0$ then
$f(x)=x+c \le 0$ for $0<x\le -c$, so $f$ would not map into $\mathbb R_{>0}$ — this is
exactly why the domain/codomain constraint forces $c\ge 0$ and not merely $c\in\mathbb
R$.)

We verify $(\star)$ directly by checking (A) and (B) — equivalent to $(\star)$ by Step
0 — for this $f$.

**Checking (A).** Compute
$$2x^2+2f(y)^2-\big(f(x)+y\big)^2 = 2x^2+2(y+c)^2-(x+c+y)^2.$$
Set $a:=x,\ b:=y+c$; then $f(x)+y = a+b$ and the expression is
$$2a^2+2b^2-(a+b)^2 = 2a^2+2b^2-a^2-2ab-b^2 = a^2-2ab+b^2 = (a-b)^2 = (x-y-c)^2 \ge 0.$$
Hence $2x^2+2f(y)^2 \ge (f(x)+y)^2$ for all $x,y>0$, i.e. (A) holds, with equality iff
$x=y+c$.

**Checking (B).** Compute
$$\big(f(x)+y\big)^2 - 4xf(y) = (x+c+y)^2 - 4x(y+c).$$
Expand $(x+y+c)^2 = x^2+y^2+c^2+2xy+2xc+2yc$, so
$$(x+y+c)^2-4x(y+c) = x^2+y^2+c^2+2xy+2xc+2yc-4xy-4xc = x^2+y^2+c^2-2xy-2xc+2yc.$$
On the other hand,
$$(x-y-c)^2 = x^2+y^2+c^2-2xy-2xc+2yc,$$
which matches term by term. Hence
$$(f(x)+y)^2-4xf(y) = (x-y-c)^2 \ge 0,$$
i.e. (B) holds for all $x,y>0$, with equality iff $x=y+c$.

By Step 0, (A) and (B) together are equivalent to $(\star)$, so $f(x)=x+c$ satisfies
$(\star)$ for every $c\ge 0$. This proves sufficiency.

### Conclusion

Combining Steps 6 (necessity: every solution has the form $f(x)=x+c$ for some $c\ge0$)
and 7 (sufficiency: every such $f$ is indeed a solution), the complete solution set of
$(\star)$ is
$$\boxed{f(x) = x+c \quad \text{for a constant } c \ge 0.}$$
$\blacksquare$

## Promotable lemmas

- **Lemma (equality-forcing identity).** Any $f:\mathbb R_{>0}\to\mathbb R_{>0}$
  satisfying $(\star)$ satisfies $f(f(y))=2f(y)-y$ for all $y>0$. *Proved in Step 1
  above*, via the substitution $x=f(y)$ collapsing the QM-side and GM-side bounds in
  (A)/(B) to the same value $f(y)^2$, forcing equality.

- **Lemma ($f(y)\ge y$).** Any $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $(\star)$
  satisfies $f(y)\ge y$ for all $y>0$. *Proved in Step 2 above*, via the exact
  arithmetic-progression structure of the orbit $y_{n+1}=f(y_n)$ forced by the identity
  $f(f(y))=2f(y)-y$, combined with positivity of every iterate.

- **Lemma (KEY two-sided quadratic bound).** For $S(t):=f(t)-t$ and any solution $f$ of
  $(\star)$,
  $$-\frac{(x-y)^2}{4f(x)} \le S(x)-S(y) \le \frac{(x-y)^2}{4f(y)} \quad\text{for all } x,y>0.$$
  *Proved in Step 4 above*, by substituting $X=f(x)$ (resp. $X=f(y)$) into inequality
  (B) and using the identity $f(f(x))=2f(x)-x$ (resp. its $y$-analogue) to expand into
  an explicit quadratic bound on $S(x)-S(y)$.

- **Lemma (subdivision forces global constancy).** If $S:\mathbb R_{>0}\to\mathbb R$
  satisfies the KEY bound above (with $f(t)\ge t$ for all $t>0$), then $S$ is constant
  on $\mathbb R_{>0}$. *Proved in Step 5 above*, via $n$-fold equal subdivision of
  $[\min(x,y),\max(x,y)]$ and telescoping the pairwise $O(1/n^2)$ bounds, which sum to
  an $O(1/n)$ bound on $|S(x)-S(y)|$ that vanishes as $n\to\infty$.
