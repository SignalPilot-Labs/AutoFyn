# Approach: two-sided-orbit

## Status
solved

## Target (whole problem)
Find all $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ with
$$\sqrt{\tfrac{x^2+f(y)^2}{2}}\ \ge\ \tfrac{f(x)+y}{2}\ \ge\ \sqrt{x\,f(y)}\qquad\text{for all }x,y>0.$$
**Answer:** exactly the functions $f(x)=x+c$ for a constant $c\ge 0$.

## Route (spine)
Easy prefix shared with the sibling approaches (SOS sufficiency; the $x=f(y)$ pinch giving
$f(f(y))=2f(y)-y$; the orbit identity $f^n(y)=y+n\,h(y)$ with $h:=f-\mathrm{id}\ge 0$), then a
**genuinely different closing** of the hard "$h$ constant" step: a two-sided modulus bound whose
LOWER half comes from the LEFT inequality (independent of the right-inequality bound), fed into an
**orbit-interleaving** contradiction. No telescoping and no differentiation. The flagged $c_1=0$
(fixed-point) sub-case is closed by continuity of $h$ (a free consequence of the modulus bound) plus
the Intermediate Value Theorem, keeping the finish independent of the telescope route.

## Approaches tried
- two-sided-orbit (round 1): full build. Prefix (SOS + pinch + $h\ge0$), two-sided modulus
  $|h(a)-h(b)|\le (a-b)^2/(2\min(a,b))$ (upper from RIGHT ineq, lower from LEFT ineq), orbit
  interleaving forces $h$ to take a single positive value, and the $c_1=0$ gap is closed via
  continuity + IVT. **Outcome: complete proof (Status solved).** All algebra sympy-verified.

## Current best
Complete proof below. The previously open $c_1=0$ sub-case is closed independently (Step 7, Case 2)
using that the modulus bound makes $h$ continuous and IVT then forbids a second value.

## Full proof

Throughout write the two hypotheses, valid for all $x,y>0$, as
$$\text{(L)}\quad 2\bigl(x^2+f(y)^2\bigr)\ \ge\ \bigl(f(x)+y\bigr)^2,
\qquad
\text{(R)}\quad \bigl(f(x)+y\bigr)^2\ \ge\ 4\,x\,f(y),$$
obtained by squaring the (nonnegative) two sides of the given chain; this is equivalent since all
quantities are positive. Set $h:=f-\mathrm{id}$, i.e. $h(x)=f(x)-x$.

### Part I — Sufficiency: every $f(x)=x+c$ with $c\ge 0$ works.

Let $c\ge 0$ and $f(x)=x+c$. Then $f(x)+y=x+c+y=x+f(y)$, so the middle term is
$\tfrac{f(x)+y}{2}=\tfrac{x+f(y)}{2}$, the **arithmetic mean** of the two positive numbers $x$ and
$f(y)$. By the **QM–AM–GM inequality** (`knowledge_base.md`: "Standard inequalities — QM-AM, AM-GM"),
$$\sqrt{\tfrac{x^2+f(y)^2}{2}}\ \ge\ \tfrac{x+f(y)}{2}\ \ge\ \sqrt{x\,f(y)},$$
which is exactly the required chain. Explicitly, both slacks are perfect squares:
$$2\bigl(x^2+f(y)^2\bigr)-\bigl(x+f(y)\bigr)^2=(x-f(y))^2\ge 0,\qquad
\bigl(x+f(y)\bigr)^2-4x\,f(y)=(x-f(y))^2\ge 0,$$
both identities being elementary expansions (verified symbolically). Since $c\ge 0$ and $x>0$ give
$f(x)=x+c>0$, indeed $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$. Hence every such $f$ satisfies the
hypotheses. $\quad\square$

### Part II — Necessity: any solution has the form $f(x)=x+c$, $c\ge 0$.

Fix a solution $f$. We prove $h\equiv c$ for some constant $c\ge 0$.

#### Step 1 (Pinch): $f(f(y))=2f(y)-y$ for all $y>0$.

Put $x=f(y)$ (a positive real) in the chain. The outer terms coincide:
$$\sqrt{\tfrac{f(y)^2+f(y)^2}{2}}=\sqrt{f(y)^2}=f(y)=\sqrt{f(y)\cdot f(y)}.$$
Thus the chain reads $f(y)\ \ge\ \tfrac{f(f(y))+y}{2}\ \ge\ f(y)$, forcing
$\tfrac{f(f(y))+y}{2}=f(y)$, i.e.
$$\boxed{\,f(f(y))=2f(y)-y\,}\qquad\text{for all }y>0. \tag{1}$$

#### Step 2 (Orbit): $f^n(y)=y+n\,h(y)$ and $h(f^n(y))=h(y)$ for all integers $n\ge 0$.

From (1), $h(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=f(y)-y=h(y)$: **$h$ is invariant along orbits.**
Now induct on $n$. For $n=0,1$ the claim $f^n(y)=y+n\,h(y)$ is trivial. If $f^n(y)=y+n\,h(y)$, then
$$f^{n+1}(y)=f\bigl(f^n(y)\bigr)=f^n(y)+h\bigl(f^n(y)\bigr)=\bigl(y+n\,h(y)\bigr)+h(y)=y+(n+1)h(y),$$
using $h(f^n(y))=h(y)$, which follows by iterating $h(f(\cdot))=h(\cdot)$. This proves both claims. $\tag{2}$

#### Step 3 ($h\ge 0$): $h(y)\ge 0$ for all $y>0$.

By (2), $f^n(y)=y+n\,h(y)$. Since $f$ maps $\mathbb{R}_{>0}$ into $\mathbb{R}_{>0}$, every iterate
$f^n(y)>0$. If $h(y)<0$ then $y+n\,h(y)\to-\infty$ as $n\to\infty$, so $f^n(y)$ would eventually be
negative — a contradiction. Hence
$$h(y)\ge 0\quad\text{for all }y>0,\qquad\text{equivalently } f(y)\ge y. \tag{3}$$

#### Step 4 (Upper modulus, from the RIGHT inequality (R)).

Let $t>0$ and $p>0$. Apply (R) with $x=f(t)$ and $y=t+p$; using $f(f(t))=2f(t)-t$ from (1),
$$\bigl(f(f(t))+(t+p)\bigr)^2=\bigl(2f(t)-t+t+p\bigr)^2=\bigl(2f(t)+p\bigr)^2\ \ge\ 4\,f(t)\,f(t+p).$$
Hence $f(t+p)\le \dfrac{(2f(t)+p)^2}{4f(t)}$. Subtracting $(t+p)+h(t)=f(t)+p$ and expanding (a direct
computation, verified symbolically):
$$\frac{(2f(t)+p)^2}{4f(t)}-\bigl(f(t)+p\bigr)=\frac{4f(t)^2+4f(t)p+p^2-4f(t)^2-4f(t)p}{4f(t)}=\frac{p^2}{4f(t)},$$
so, since $h(t+p)-h(t)=f(t+p)-\bigl(f(t)+p\bigr)$,
$$h(t+p)-h(t)\ \le\ \frac{p^2}{4\,f(t)}\qquad(t,p>0). \tag{4}$$

#### Step 5 (Lower modulus, from the LEFT inequality (L)).

Let $t>0$ and $p>0$. Apply (L) with $x=f(t)$ and $y=t+p$; again $f(f(t))=2f(t)-t$ gives
$$2\bigl(f(t)^2+f(t+p)^2\bigr)\ \ge\ \bigl(f(f(t))+(t+p)\bigr)^2=\bigl(2f(t)+p\bigr)^2.$$
Solving for $f(t+p)^2$ (elementary, verified symbolically):
$$f(t+p)^2\ \ge\ \frac{(2f(t)+p)^2-2f(t)^2}{2}=f(t)^2+2f(t)p+\frac{p^2}{2}=\bigl(f(t)+p\bigr)^2-\frac{p^2}{2}.$$
Write $A:=f(t)+p>0$. The right side $A^2-\tfrac{p^2}{2}$ is positive (indeed $A\ge p$ since
$f(t)>0$, so $A^2\ge p^2>\tfrac{p^2}{2}$), and $f(t+p)>0$, so we may take square roots:
$f(t+p)\ge\sqrt{A^2-\tfrac{p^2}{2}}$. Therefore, using $h(t+p)-h(t)=f(t+p)-A$ and rationalizing,
$$h(t+p)-h(t)\ \ge\ \sqrt{A^2-\tfrac{p^2}{2}}-A
=\frac{\bigl(A^2-\tfrac{p^2}{2}\bigr)-A^2}{\sqrt{A^2-\tfrac{p^2}{2}}+A}
=\frac{-\tfrac{p^2}{2}}{\sqrt{A^2-\tfrac{p^2}{2}}+A}\ \ge\ \frac{-\tfrac{p^2}{2}}{A},$$
the last step because $\sqrt{A^2-\tfrac{p^2}{2}}\ge 0$ makes the denominator $\ge A>0$. Hence
$$h(t+p)-h(t)\ \ge\ -\frac{p^2}{2\bigl(f(t)+p\bigr)}\qquad(t,p>0). \tag{5}$$

#### Step 6 (Two-sided control): $\displaystyle |h(b)-h(a)|\le\frac{(b-a)^2}{2\min(a,b)}$ for all $a,b>0$.

By symmetry it suffices to treat $a<b$; put $t=a$, $p=b-a>0$, so $\min(a,b)=a$ and $f(t)=f(a)\ge a$
by (3). From (4),
$$h(b)-h(a)\ \le\ \frac{p^2}{4f(a)}\ \le\ \frac{p^2}{4a}\ \le\ \frac{p^2}{2a}=\frac{(b-a)^2}{2\min(a,b)}.$$
From (5), since $f(a)+p\ge a$ (indeed $f(a)\ge a$),
$$h(b)-h(a)\ \ge\ -\frac{p^2}{2\bigl(f(a)+p\bigr)}\ \ge\ -\frac{p^2}{2a}=-\frac{(b-a)^2}{2\min(a,b)}.$$
Combining the two one-sided bounds,
$$|h(b)-h(a)|\ \le\ \frac{(b-a)^2}{2\min(a,b)}\qquad\text{for all }a,b>0. \tag{6}$$
(Each bound uses only one of (L), (R); the two are never subtracted or combined jointly.)

#### Step 7 (Finish): $h$ is constant.

First, **(6) makes $h$ continuous** on $(0,\infty)$: fix $a>0$; for $b\to a$ we have
$\min(a,b)\to a>0$ and $(b-a)^2\to 0$, so the right side of (6) tends to $0$, giving $h(b)\to h(a)$.

**Interleaving Lemma.** *If $h(a)>0$ and $h(b)>0$ then $h(a)=h(b)$.*

*Proof.* Suppose not; write $c_1:=h(a)>0$, $c_2:=h(b)>0$ and, WLOG, $c_1<c_2$. By (2) the orbit
points
$$a_n:=a+n\,c_1=f^n(a)\ \ (n\ge0),\qquad b_m:=b+m\,c_2=f^m(b)\ \ (m\ge0)$$
satisfy $h(a_n)=h(a)=c_1$ and $h(b_m)=h(b)=c_2$ for all $n,m\ge0$. Fix $n$ large enough that
$a_n>b$, and set $m=m(n):=\big\lfloor \tfrac{a_n-b}{c_2}\big\rfloor\ge 0$. Then $b_m\le a_n<b_{m+1}=b_m+c_2$, so
$$0\ \le\ a_n-b_m\ <\ c_2 ,\qquad\text{hence}\qquad b_m\ >\ a_n-c_2=a+n\,c_1-c_2 .$$
Since $b_m\le a_n$ we have $\min(a_n,b_m)=b_m\ge a+n\,c_1-c_2\to\infty$ as $n\to\infty$. Applying (6)
to the pair $(a_n,b_m)$,
$$|c_1-c_2|=|h(a_n)-h(b_m)|\ \le\ \frac{(a_n-b_m)^2}{2\min(a_n,b_m)}\ <\ \frac{c_2^2}{2\,b_m}\ \xrightarrow[n\to\infty]{}\ 0 .$$
The left side is a fixed positive number while the right side $\to0$; contradiction. Hence
$c_1=c_2$. $\quad\square$

Now let $S_+:=\{x>0:\ h(x)>0\}$. By (3), $h\ge0$, so on the complement $h=0$.

**Case 1: $S_+=\varnothing$.** Then $h\equiv 0$, i.e. $f(x)=x$ (this is $c=0$).

**Case 2: $S_+\ne\varnothing$.** By the Interleaving Lemma, $h$ takes the *same* positive value on all
of $S_+$; call it $c_0>0$. Thus $h$ takes values only in the two-point set $\{0,c_0\}$. We claim
$S_+=(0,\infty)$, i.e. $h$ has no zero. Suppose instead $h(a_0)=0$ for some $a_0$, and pick any
$b_0\in S_+$, so $h(b_0)=c_0$. Since $h$ is continuous, the **Intermediate Value Theorem**
(`knowledge_base.md`: continuity on an interval — the domain $(0,\infty)$ is an interval, and IVT is
the standard consequence that a continuous function attains every intermediate value) applied to $h$
on the closed interval between $a_0$ and $b_0$ yields a point $p_0$ there with
$$h(p_0)=\tfrac{c_0}{2}\in(0,c_0).$$
But $h(p_0)>0$ forces $p_0\in S_+$, whence $h(p_0)=c_0\ne\tfrac{c_0}{2}$ — contradiction. Therefore
$h$ has no zero, $S_+=(0,\infty)$, and $h\equiv c_0$.

In every case $h\equiv c$ for a constant $c\ge0$ (Case 1 gives $c=0$; Case 2 gives $c=c_0>0$).
Hence
$$f(x)=x+c\qquad\text{for all }x>0,\ \text{some constant }c\ge 0. \tag{7}$$

### Conclusion and verification

Part I shows every $f(x)=x+c$ with $c\ge0$ satisfies the hypotheses; Part II shows every solution is
of this form. **Verification of the answer** (substitution, as in Part I): for $f(x)=x+c$,
$c\ge0$, the middle term equals $\tfrac{x+f(y)}{2}$ and QM–AM–GM gives the chain, both slacks being
$(x-f(y))^2\ge0$; and $f(x)=x+c>0$ for $x>0$. Conversely no $c<0$ can occur, since $c<0$ would give
$h\equiv c<0$, violating (3). Therefore the complete set of solutions is
$$\boxed{\,f(x)=x+c,\quad c\ge 0\,.}$$
$\blacksquare$

## Promotable lemmas
- **Pinch identity (Lemma P).** Any $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfying the given
  sandwich obeys $f(f(y))=2f(y)-y$ for all $y>0$. Proved in Part II, Step 1 (set $x=f(y)$; outer
  terms both equal $f(y)$).
- **Orbit linearity (Lemma O).** With $h=f-\mathrm{id}$, one has $h(f(y))=h(y)$ and
  $f^n(y)=y+n\,h(y)$, hence $h\ge 0$. Proved in Part II, Steps 2–3.
- **Two-sided quadratic modulus (Lemma M).** $|h(b)-h(a)|\le\dfrac{(b-a)^2}{2\min(a,b)}$ for all
  $a,b>0$; upper half from (R), lower half from (L). Proved in Part II, Steps 4–6. (This bound alone
  yields continuity of $h$.)
- **Interleaving Lemma.** If $h(a)>0$ and $h(b)>0$ then $h(a)=h(b)$ (arithmetic-orbit floor
  interleaving squeezed by Lemma M). Proved in Part II, Step 7.
