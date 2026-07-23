## Lemma (KEY two-sided quadratic bound, and its consequence: $S$ globally constant)

Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfy the sandwich inequality of imo-2026-05,
hence the equality-forcing identity $f(f(y))=2f(y)-y$ and $f(y)\ge y$ for all $y>0$
(see the two companion lemmas). Let $S(t):=f(t)-t\ge0$. Then:

**(KEY).** For all $x,y>0$,
$$-\frac{(x-y)^2}{4f(x)} \;\le\; S(x)-S(y) \;\le\; \frac{(x-y)^2}{4f(y)}.$$

**Consequence.** $S$ is constant on $\mathbb R_{>0}$: there is $c\ge0$ with
$f(x)=x+c$ for all $x>0$.

**Proof of (KEY).** Fix $x,y>0$. Apply the GM-side squared inequality
$(f(x)+y)^2\ge4xf(y)$ with $x$ replaced by $f(x)$ (legitimate, $f(x)>0$):
$(f(f(x))+y)^2\ge4f(x)f(y)$. Using $f(f(x))=2f(x)-x=x+2S(x)$ and expanding
(direct algebraic identity, checked symbolically):
$(x+y+2S(x))^2-4(x+S(x))(y+S(y)) = (x-y)^2+4f(x)(S(x)-S(y))$, this gives
$(x-y)^2+4f(x)(S(x)-S(y))\ge0$. Swapping $x,y$ (apply the same inequality with $y$'s
value substituted) gives $(x-y)^2+4f(y)(S(y)-S(x))\ge0$. Combining the two and dividing
by the positive quantities $4f(x)$, $4f(y)$ gives (KEY).

**Proof of consequence.** Fix $x,y>0$, WLOG $x<y$ (case $x=y$ trivial, case $x>y$
symmetric); let $m:=x$. Subdivide $[x,y]$ into $n$ equal steps $t_i$, $i=0,\dots,n$;
since $t_i\ge m$, $f(t_i)\ge t_i\ge m$. Apply (KEY) to each consecutive pair to get
$|S(t_i)-S(t_{i+1})|\le(y-x)^2/(4mn^2)$, then telescope over $i=0,\dots,n-1$:
$|S(x)-S(y)|\le(y-x)^2/(4mn)\to0$ as $n\to\infty$. Since the left side doesn't depend
on $n$, $S(x)=S(y)$. As $x,y$ were arbitrary, $S$ is a global constant $c$, and
$c=S(1)\ge0$ by the previous lemma. $\blacksquare$

Certified by proof-reviewer, round 1, imo-2026-05. This is the load-bearing lemma of
both `quadratic-difference-chaining.md` and `monotonicity-first.md`; independently
re-derived by both approaches and by the reviewer (sympy check of the key expansion
identity). The subdivision argument is fully general — it applies to arbitrary
$x,y>0$ with any real ratio, not just special/dense sequences.
