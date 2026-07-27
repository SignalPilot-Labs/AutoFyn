Solution

  Answer. The solutions are exactly
  $$f(x) = x + c, \qquad \text{for an arbitrary constant } c \ge 0.$$
  (This includes $f(x)=x$, the case $c=0$.)

  Throughout, write the hypothesis in squared form. Since $x,f(y)>0$ imply $\frac{f(x)+y}{2}>0$, squaring is reversible, so the hypothesis is equivalent to the pair of inequalities holding for all $x,y>0$:
  $$
  2x^2+2f(y)^2 \ge (f(x)+y)^2 \tag{A}
  $$
  $$
  (f(x)+y)^2 \ge 4xf(y) \tag{B}
  $$

  Step 1: A functional equation

  Put $x=f(y)$ (legitimate since $f(y)>0$) into (A):
  $$4f(y)^2 \ge (f(f(y))+y)^2 \implies 2f(y)\ge f(f(y))+y \implies f(f(y))\le 2f(y)-y.$$
  Put $x=f(y)$ into (B):
  $$(f(f(y))+y)^2 \ge 4f(y)^2 \implies f(f(y))+y\ge 2f(y) \implies f(f(y))\ge 2f(y)-y.$$
  Hence for all $y>0$:
  $$f(f(y)) = 2f(y)-y. \tag{E}$$

  Step 2: $f(y)\ge y$ for all $y$

  Fix $y$, let $a_0=y,\ a_{n+1}=f(a_n)$. Applying (E) at $y=a_n$ gives $a_{n+2}=2a_{n+1}-a_n$, so $(a_n)$ is an arithmetic progression: $a_n = y+nd$ where $d=f(y)-y$. Since every $a_n=f^{(n)}(y)>0$, if $d<0$ then $a_n\to-\infty$,
  a contradiction. So $d\ge0$, i.e.
  $$f(y)\ge y \quad \text{for all } y>0. \tag{2}$$

  Step 3: Two auxiliary inequalities

  For any $y,z>0$, apply (A) with $x=f(y)$ and second variable $z$, then use (E):
  $$2f(y)^2+2f(z)^2 \ge (f(f(y))+z)^2 = \big(2f(y)+(z-y)\big)^2,$$
  which simplifies to
  $$f(z)^2 \ge f(y)^2 + 2f(y)(z-y) + \tfrac12(z-y)^2. \tag{I}$$

  Similarly, apply (B) with $x=f(y)$, second variable $z$:
  $$\big(2f(y)+(z-y)\big)^2 \ge 4f(y)f(z),$$
  i.e.
  $$4f(y)^2+4f(y)(z-y)+(z-y)^2 \ge 4f(y)f(z). \tag{II}$$

  Dividing (II) by $4f(y)>0$:
  $$f(z) \le f(y)+(z-y)+\frac{(z-y)^2}{4f(y)}.$$
  Swapping $y\leftrightarrow z$ in (II) and dividing by $4f(z)>0$ gives (after rearranging):
  $$f(z) \ge f(y)+(z-y)-\frac{(z-y)^2}{4f(z)}.$$

  Combining these two bounds, for all $y,z>0$:
  $$-\frac{(z-y)^2}{4f(z)} ;\le; f(z)-f(y)-(z-y) ;\le; \frac{(z-y)^2}{4f(y)}. \tag{III}$$

  Step 4: $f(y)-y$ is constant

  Fix $0<y_1<y_2$ and an integer $N$. Let $\delta=\frac{y_2-y_1}{N}$ and $t_k=y_1+k\delta$ for $k=0,\dots,N$. Apply (III) to each consecutive pair $(t_k,t_{k+1})$:
  $$-\frac{\delta^2}{4f(t_{k+1})} \le f(t_{k+1})-f(t_k)-\delta \le \frac{\delta^2}{4f(t_k)}.$$
  Sum over $k=0,\dots,N-1$; the middle terms telescope to $f(y_2)-f(y_1)-(y_2-y_1)$ (a quantity independent of $N$):
  $$-\sum_{k=0}^{N-1}\frac{\delta^2}{4f(t_{k+1})} \le f(y_2)-f(y_1)-(y_2-y_1) \le \sum_{k=0}^{N-1}\frac{\delta^2}{4f(t_k)}.$$
  By Step 2, every $t_k\ge y_1$ implies $f(t_k)\ge t_k\ge y_1$, so each of the $N$ terms in either sum is at most $\frac{\delta^2}{4y_1}$, making both sums at most
  $$N\cdot\frac{\delta^2}{4y_1} = \frac{(y_2-y_1)^2}{4y_1 N} \xrightarrow[N\to\infty]{} 0.$$
  Since the middle quantity does not depend on $N$, it is squeezed to exactly $0$:
  $$f(y_2)-f(y_1) = y_2-y_1.$$

  As $y_1<y_2>0$ were arbitrary, $f(y)-y$ takes the same value for all $y>0$; call it $c$. By (2), $c\ge 0$. Thus
  $$f(x) = x+c, \qquad c\ge 0.$$

  Step 5: Verification
  
  For $f(x)=x+c$ with $c\ge0$, check (A) and (B) directly. With $s=y+c$:
  $$2x^2+2f(y)^2-(f(x)+y)^2 = 2x^2+2s^2-(x+s)^2=(x-s)^2\ge0,$$
  so (A) holds, with equality iff $x=y+c$. Also
  $$(f(x)+y)^2-4xf(y) = (x+y+c)^2-4x(y+c) = \big((x-y)-c\big)^2\ge 0,$$
  so (B) holds, with equality iff $x=y+c$. Hence $f(x)=x+c$ satisfies the original inequality for every $x,y>0$, for any constant $c\ge0$.

  Conclusion

  $$\boxed{f(x) = x+c \text{ for an arbitrary constant } c\ge 0}$$
  are exactly the functions satisfying the given inequality.

✻ Cooked for 18m 19s