## Status
solved

## Approaches tried
- `quadratic-difference-chaining` — worked. Full necessity+sufficiency proof: equality-forcing
  substitution x=f(y) gives f(f(y))=2f(y)-y; orbit argument gives f(y)>=y; second-order
  substitution X=f(x) into the GM-side inequality gives a two-sided quadratic bound (KEY) on
  S(x)-S(y) where S=f-id; an n-fold subdivision/telescoping argument on an arbitrary interval
  [min(x,y),max(x,y)] forces S constant; sufficiency of f(x)=x+c, c>=0, checked directly.
  Reviewed and verified correct — see Full proof below.
- `monotonicity-first` — worked, independently. Same core mechanism (equality-forcing
  substitution, orbit AP argument, KEY quadratic bound, subdivision), reached the same
  answer and re-derived (KEY) via a different intermediate algebraic path. Additionally
  proves (as a real negative/structural result, not hand-waving) that three "cheap"
  order-theoretic routes to monotonicity (cross-substitution of (B) alone at two different
  pairs, same-pair mixing of (A) and (B), and pure orbit-disjointness combinatorics from a
  new "S constant along each orbit" lemma) are each individually insufficient, with explicit
  numeric witnesses. Reviewed and verified correct.
- `cauchy-boundedness`, `extremal-supinf` — not part of this round's build set; not reviewed
  this round.

## Current best
Solved (see Full proof).

## Full proof

(Copied from `quadratic-difference-chaining.md`, verified independently by the reviewer,
including symbolic recomputation of every algebraic identity used.)

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
(A) and (B). This is a use of the "equality cases pin down the extremal configuration"
technique for standard inequalities (knowledge_base.md, Standard inequalities).

In (A): $2f(y)^2 + 2f(y)^2 \ge (f(f(y))+y)^2$, i.e.
$$4f(y)^2 \ge \big(f(f(y))+y\big)^2. \tag{A$'$}$$

In (B): $(f(f(y))+y)^2 \ge 4f(y)\cdot f(y) = 4f(y)^2$, i.e.
$$\big(f(f(y))+y\big)^2 \ge 4f(y)^2. \tag{B$'$}$$

Combining (A$'$) and (B$'$): $\big(f(f(y))+y\big)^2 = 4f(y)^2$. Both
$f(f(y))+y$ and $2f(y)$ are positive reals, and their squares are equal, so (taking the
unique nonnegative square root of both sides) they are equal:
$$f(f(y)) + y = 2f(y), \qquad\text{i.e.}\qquad f(f(y)) = 2f(y) - y \quad\text{for all } y>0. \tag{$*$}$$

### Step 2: $f(y) \ge y$ for every $y>0$

Fix $y>0$ and define a sequence $(y_n)_{n\ge 0}$ by $y_0 := y$ and
$y_{n+1} := f(y_n)$. Since $f:\mathbb R_{>0}\to\mathbb R_{>0}$, an easy induction shows
$y_n > 0$ for every $n\ge 0$.

Apply $(*)$ with $y$ replaced by $y_n$: $f(f(y_n)) = 2f(y_n)-y_n$, i.e.
$$y_{n+2} = 2y_{n+1} - y_n \qquad \text{for all } n \ge 0,$$
the recursion for an arithmetic progression, so
$$y_n = y + n\big(f(y)-y\big) \qquad \text{for all } n\ge 0.$$
If $f(y) < y$, the common difference $d:=f(y)-y<0$ gives $y_n\to-\infty$, contradicting
$y_n>0$ for all $n$. Hence
$$f(y) \ge y \qquad \text{for all } y > 0. \tag{2}$$

### Step 3: Injectivity of $f$ (not needed later, recorded for completeness)

If $f(a)=f(b)$, then by $(*)$, $2f(a)-a=2f(b)-b$, and since $f(a)=f(b)$, $a=b$. (KB:
Functional equations — test special values, check injectivity.)

### Step 4: The key two-sided quadratic bound on $S(x) := f(x)-x$

Define $S(t):=f(t)-t\ge0$ (by Step 2). Fix $x,y>0$. Apply (B) with first argument
$f(x)$ and second argument $y$:
$$\big(f(f(x))+y\big)^2 \ge 4f(x)f(y).$$
By $(*)$, $f(f(x))=2f(x)-x=x+2S(x)$. Substituting and expanding (verified symbolically
by the reviewer; the identity
$(x+y+2S(x))^2-4(x+S(x))(y+S(y)) = (x-y)^2+4f(x)(S(x)-S(y))$
was independently re-derived and confirmed with sympy):
$$(x-y)^2 + 4f(x)\big(S(x)-S(y)\big) \;\ge\; 0 \qquad \text{for all } x,y>0. \tag{**}$$
Swapping the roles of $x,y$ (apply (B) with first argument $f(y)$, second argument $x$)
gives the companion bound
$$(x-y)^2 + 4f(y)\big(S(y)-S(x)\big) \;\ge\; 0 \qquad \text{for all } x,y>0. \tag{***}$$
Combining $(**)$ and $(***)$:
$$-\frac{(x-y)^2}{4f(x)} \;\le\; S(x)-S(y) \;\le\; \frac{(x-y)^2}{4f(y)}
\qquad \text{for all } x,y>0. \tag{KEY}$$

### Step 5: (KEY) forces $S$ to be globally constant

Fix $x,y>0$; WLOG $x<y$ (case $x=y$ trivial, case $x>y$ symmetric). Let $m:=x>0$. For
$n\ge1$, subdivide $[x,y]$ into $n$ equal parts $t_i:=x+i(y-x)/n$, $i=0,\dots,n$, with
step $\Delta=(y-x)/n$. Since $t_i\ge x=m$, Step 2 gives $f(t_i)\ge t_i\ge m$ for every
$i$. Applying (KEY) to each consecutive pair $(t_i,t_{i+1})$ and using $f(t_i),
f(t_{i+1})\ge m$:
$$|S(t_i)-S(t_{i+1})| \le \frac{\Delta^2}{4m} = \frac{(y-x)^2}{4n^2m}.$$
Telescoping over $i=0,\dots,n-1$:
$$|S(x)-S(y)| \le \sum_{i=0}^{n-1}|S(t_i)-S(t_{i+1})| \le \frac{(y-x)^2}{4mn} \xrightarrow[n\to\infty]{} 0,$$
so $S(x)=S(y)$. Since $x,y>0$ were arbitrary, $S$ is a global constant $c\ge0$ (using
(2) at any point, e.g. $x=1$).

### Step 6: Necessity conclusion

Every solution $f$ of $(\star)$ has the form $f(x)=x+c$ for all $x>0$, for some
constant $c\ge0$.

### Step 7: Sufficiency

Let $c\ge0$, $f(x):=x+c$. Then $f(x)>0$ for all $x>0$ (uses $c\ge0$). Direct
computation (verified symbolically by the reviewer):
$$2x^2+2f(y)^2-(f(x)+y)^2 = (x-y-c)^2 \ge 0 \quad\text{[gives (A)]},$$
$$(f(x)+y)^2 - 4xf(y) = (x-y-c)^2 \ge 0 \quad\text{[gives (B)]},$$
both with equality iff $x=y+c$. By Step 0, (A) and (B) together are equivalent to
$(\star)$, so every $f(x)=x+c$, $c\ge0$, satisfies $(\star)$.

### Conclusion

$$\boxed{f(x) = x+c \quad \text{for a constant } c \ge 0}$$
is exactly the solution set. $\blacksquare$
