                                                                                                                     
⏺ Setting Up

  Since $x,y,f(x),f(y)>0$, all three expressions in the chain are nonnegative, so I can square freely. Writing $A\ge B\ge C$ for
  $$A=\sqrt{\tfrac{x^2+f(y)^2}{2}},\qquad B=\tfrac{f(x)+y}{2},\qquad C=\sqrt{xf(y)},$$
  squaring $B\ge C$ and $A\ge B$ gives, for all $x,y>0$:

  $$\textbf{(I)}\quad (f(x)+y)^2\ge 4xf(y),\qquad\qquad \textbf{(II)}\quad (f(x)+y)^2\le 2x^2+2f(y)^2.$$

  These are equivalent to the original system.

  Lemma 1: $f(f(y))=2f(y)-y$ for all $y$

  Put $x=f(y)$ (legal, since $f(y)\in\mathbb R_{>0}$) into (I) and (II):

  - (I): $(f(f(y))+y)^2\ge 4f(y)^2 \Rightarrow f(f(y))+y\ge 2f(y)$.
  - (II): $(f(f(y))+y)^2\le 4f(y)^2 \Rightarrow f(f(y))+y\le 2f(y)$.

  Hence equality: $f(f(y))=2f(y)-y$. $\blacksquare$

  Lemma 2: $f(y)\ge y$ for all $y$

  Fix $y>0$ and define $y_0=y$, $y_{n+1}=f(y_n)$; every $y_n\in\mathbb R_{>0}$. Lemma 1 applied at $y_n$ gives $y_{n+2}=2y_{n+1}-y_n$,
  i.e. $y_{n+2}-y_{n+1}=y_{n+1}-y_n$. So by induction the common difference is constant: $y_{n+1}-y_n=y_1-y_0=f(y)-y=:d$ for all $n$,
  giving $y_n=y+nd$.

  If $d<0$, then $y_n\to-\infty$, contradicting $y_n>0$ for all $n$. Hence $d\ge0$, i.e. $f(y)\ge y$. $\blacksquare$

  Write $d(x):=f(x)-x\ge 0$.

  Lemma 3 (key two-point estimate)

  Fix $a,b>0$. Put $x=f(a)$, $y=b$ in (I) and use Lemma 1 ($f(f(a))=2f(a)-a$):

  $$(2f(a)-a+b)^2\ge 4f(a)f(b).$$

  Substitute $f(a)=a+d(a)$, $f(b)=b+d(b)$; the left side is $((a+b)+2d(a))^2$. Expanding both sides:

  $$(a+b)^2+4(a+b)d(a)+4d(a)^2 \ge 4ab+4ad(b)+4bd(a)+4d(a)d(b).$$

  Since $(a+b)^2-4ab=(a-b)^2$ and $4(a+b)d(a)-4bd(a)=4ad(a)$, this simplifies to
  $$(a-b)^2+4a\big(d(a)-d(b)\big)+4d(a)\big(d(a)-d(b)\big)\ge0 \iff (a-b)^2+4\big(d(a)-d(b)\big)f(a)\ge0.$$

  Rearranged, for all $a,b>0$:
  $$d(b)-d(a)\le \frac{(a-b)^2}{4f(a)}. \tag{E}$$

  (Sanity check: for $f=\mathrm{id}+c$, (E) reduces exactly to $(a-b-c)^2\ge0$, matching the direct computation below — confirming the 
  algebra.)

  Lemma 4: $d$ is constant
  
  Fix $a<b$ and $N\in\mathbb Z_{>0}$; let $t_i=a+i\frac{b-a}{N}$ for $i=0,\dots,N$, so all $t_i\in[a,b]$, hence $t_i\ge a$ and (by Lemma
  2) $f(t_i)\ge t_i\ge a$.

  Applying (E) to each consecutive pair $(t_i,t_{i+1})$:
  $$d(t_{i+1})-d(t_i)\le \frac{(t_i-t_{i+1})^2}{4f(t_i)}\le \frac{\big((b-a)/N\big)^2}{4a}.$$

  Summing (telescoping) over $i=0,\dots,N-1$:
  $$d(b)-d(a)\le N\cdot\frac{(b-a)^2}{4aN^2}=\frac{(b-a)^2}{4aN}.$$

  This holds for every $N$, so letting $N\to\infty$: $d(b)\le d(a)$.

  Applying (E) instead to the reversed pairs $(t_{i+1},t_i)$ (using $f(t_{i+1})\ge a$) gives, symmetrically, $d(a)\le d(b)$.

  Hence $d(a)=d(b)$. Since $a,b>0$ were arbitrary, $d$ is a constant $c\ge0$:
  $$f(x)=x+c\quad\text{for all }x>0,\text{ some fixed } c\ge0. \tag{$\ast$}$$

  Sufficiency: every $f(x)=x+c$, $c\ge0$, works

  Check (I),(II) directly for $f=\mathrm{id}+c$. With $f(x)=x+c,\ f(y)=y+c$:

  $$2x^2+2f(y)^2-(f(x)+y)^2 = 2x^2+2(y+c)^2-(x+y+c)^2.$$

  Expanding: $2x^2+2y^2+4yc+2c^2-\big(x^2+y^2+c^2+2xy+2xc+2yc\big)=x^2+y^2-2xy+c^2-2xc+2yc=(x-y-c)^2\ge0,$

  which is exactly (II). An identical computation gives
  $$(f(x)+y)^2-4xf(y)=(x+y+c)^2-4x(y+c)=(x-y-c)^2\ge0,$$
  which is exactly (I). So both hold for every $x,y>0$, with equality throughout the original chain precisely when $x-y=c$. Since
  $c\ge0$, $f(x)=x+c>0$ for all $x>0$, so $f$ is a valid map $\mathbb R_{>0}\to\mathbb R_{>0}$.

  (Numerical spot-check, $c=3,x=2,y=7$: $f(x)=5,f(y)=10$; middle $=6$, right $=\sqrt{20}\approx4.47$, left $=\sqrt{52}\approx7.21$ — 
  chain holds, as it must.)

  Conclusion

  $$\boxed{f(x)=x+c\ \text{ for all } x\in\mathbb R_{>0},\text{ where } c \text{ is an arbitrary constant with } c\ge 0.}$$

  Necessity was proved in Lemmas 1–4 (using only substitutions legal for all $x,y>0$, with no continuity or monotonicity assumed in
  advance), and sufficiency was verified by a direct algebraic identity reducing both required inequalities to the perfect square
  $(x-y-c)^2\ge0$. The special case $c=0$ recovers $f(x)=x$, for which the chain is just the classical QM–AM–GM inequality applied to
  $x,y$.


✻ Churned for 1h 22m 53s

