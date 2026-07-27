Solution

  Answer. The solutions are exactly the functions
  $$f(x) = x + c \qquad\text{for a constant } c \ge 0 .$$

  Throughout write the two hypotheses as
  $$\textbf{(A)}\quad \sqrt{\tfrac{x^2+f(y)^2}{2}}\ \ge\ \tfrac{f(x)+y}{2},\qquad\qquad \textbf{(B)}\quad \tfrac{f(x)+y}{2}\ \ge\
  \sqrt{x,f(y)} .$$

  ---
  1. These functions work

  Let $f(x)=x+c$ with $c\ge 0$. For any $x,y>0$ apply the QM–AM–GM inequalities to the two positive numbers $x$ and $y+c$:
  $$\sqrt{\tfrac{x^2+(y+c)^2}{2}}\ \ge\ \frac{x+(y+c)}{2}\ \ge\ \sqrt{x(y+c)} .$$
  Since $f(y)=y+c$ and $\tfrac{f(x)+y}{2}=\tfrac{(x+c)+y}{2}=\tfrac{x+(y+c)}{2}$, the left inequality is (A) and the right is (B). Both
  hold. $\checkmark$

  (Note both become equalities exactly when $x=y+c=f(y)$.)

  ---
  2. Only these work
  
  Assume $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfies (A) and (B).

  Step 1 — A key functional equation and $f(y)\ge y$.

  Put $x=f(y)$.
  - In (B): $\ \tfrac{f(f(y))+y}{2}\ge\sqrt{f(y)^2}=f(y)$, so $f(f(y))\ge 2f(y)-y$.
  - In (A): $\ \sqrt{\tfrac{f(y)^2+f(y)^2}{2}}=f(y)\ge\tfrac{f(f(y))+y}{2}$, so $f(f(y))\le 2f(y)-y$.

  Hence
  $$\boxed{f(f(y))=2f(y)-y}\qquad\text{for all }y>0. \tag{1}$$

  Define the orbit $y_0=y,\ y_{n+1}=f(y_n)$. By $(1)$, $y_{n+2}=2y_{n+1}-y_n$, i.e. the second differences vanish, so $y_n=y+n,c(y)$
  where $c(y):=f(y)-y$. Since every iterate $y_n=f^{(n)}(y)$ is positive, $y+n,c(y)>0$ for all $n\ge0$, which forces
  $$c(y)=f(y)-y\ \ge\ 0 . \tag{2}$$
  Also $c(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=f(y)-y=c(y)$, so $c$ is constant along each forward orbit; in particular $c(y+n,c(y))=c(y)$
  for all $n\ge0$. $\tag{3}$

  Step 2 — A width inequality.

  Fix $x,y$ and set $p=x,\ q=f(y)$. Both $\tfrac{f(x)+y}{2}$ (by (A),(B)) and the arithmetic mean $\tfrac{p+q}{2}$ lie in the interval
  $\big[\sqrt{pq},,\sqrt{\tfrac{p^2+q^2}{2}}\big]$. Therefore their difference is at most the length of that interval:
  $$\Big|\tfrac{f(x)+y}{2}-\tfrac{x+f(y)}{2}\Big|\ \le\ \sqrt{\tfrac{p^2+q^2}{2}}-\sqrt{pq}
  =\frac{(p-q)^2/2}{\sqrt{\tfrac{p^2+q^2}{2}}+\sqrt{pq}}\ \le\ \frac{(p-q)^2}{4\sqrt{pq}} .$$
  The left side equals $\tfrac12|c(x)-c(y)|$, so for all $x,y>0$:
  $$|c(x)-c(y)|\ \le\ \frac{(x-f(y))^2}{2\sqrt{x,f(y)}} . \tag{$\star$}$$

  Step 3 — $c$ is constant on the "moving set" $M={y:c(y)>0}$.

  Let $a,a'\in M$ with $d=c(a)>0,\ d'=c(a')>0$. By $(3)$:
  - the points $a_n:=a+nd\ (n\ge0)$ satisfy $c(a_n)=d$;
  - the progression $A':={a'+j d':j\ge1}$ consists of image points $f(a'+(j-1)d')$, each with $c$-value $d'$.

  $A'$ is an arithmetic progression of spacing $d'$, unbounded above. Since $a_n\to\infty$, for all large $n$ there is $v\in A'$ with
  $|a_n-v|\le d'/2$ (nearest point of the progression). Applying $(\star)$ with $x=a_n$ and the $y$ for which $f(y)=v$:
  $$|d-d'|=|c(a_n)-c(y)|\ \le\ \frac{(a_n-v)^2}{2\sqrt{a_n v}}\ \le\ \frac{(d'/2)^2}{2\sqrt{a_n v}}\xrightarrow[n\to\infty]{}0,$$
  because $v\ge a_n-d'/2\to\infty$. Hence $d=d'$: $c\equiv d$ (some constant $d>0$) on $M$. $\tag{4}$

  Step 4 — The zero set $Z={y:c(y)=0}$ is closed.

  Let $b_n\in Z$, $b_n\to b>0$. Since $c(b_n)=0$, $f(b_n)=b_n$. Apply (A) with $x=b,\ y=b_n$:
  $$\sqrt{\tfrac{b^2+b_n^2}{2}}\ \ge\ \tfrac{f(b)+b_n}{2}=\tfrac{b+c(b)+b_n}{2}
  \ \Longrightarrow\ c(b)\le 2\sqrt{\tfrac{b^2+b_n^2}{2}}-b-b_n .$$
  As $b_n\to b$ the right side tends to $2\sqrt{b^2}-2b=0$, so $c(b)\le0$, i.e. $c(b)=0$ and $b\in Z$. Thus $Z$ is closed. $\tag{5}$

  Step 5 — $M$ and $Z$ cannot both be nonempty.

  Suppose both are nonempty. Then $\mathbb R_{>0}=Z\sqcup M$ with $Z$ closed and nonempty proper. As $\mathbb R_{>0}$ is connected, $M$
  is not closed, so $\overline{M}\cap Z\neq\varnothing$; pick $b\in Z$ and $x_n\in M$ with $x_n\to b$. Then $f(b)=b$, and by $(4)$,
  $c(x_n)=d$. Applying (A) with $x=x_n,\ y=b$:
  $$\sqrt{\tfrac{x_n^2+b^2}{2}}\ \ge\ \tfrac{f(x_n)+b}{2}=\tfrac{x_n+d+b}{2}
  \ \Longrightarrow\ d\le 2\sqrt{\tfrac{x_n^2+b^2}{2}}-x_n-b\xrightarrow[x_n\to b]{}0,$$
  forcing $d\le0$ — contradicting $d>0$.

  Conclusion.

  Hence exactly one of the following holds:
  - $M=\varnothing$: then $c\equiv0$, i.e. $f(x)=x$;
  - $Z=\varnothing$: then by $(4)$, $c\equiv d>0$, i.e. $f(x)=x+d$.

  In every case $f(x)=x+c$ for a constant $c\ge0$. Together with Part 1 (and $c\ge0$ being necessary for $f>0$), this proves:

  $$\boxed{,f(x)=x+c,\quad c\ge 0\ \text{constant},}$$

  are precisely all functions satisfying the given inequalities. $\blacksquare$

  ---
  Remarks / self-check. The two hypotheses squeeze $\tfrac{f(x)+y}{2}$ between the GM and QM of the pair $(x,f(y))$; since the AM
  $\tfrac{x+f(y)}{2}$ lies there too, the two "means" can differ by at most the QM–GM gap — this is exactly $(\star)$, and it is the
  engine of the proof. Equation $(1)$ makes every orbit an arithmetic progression, which is why the entire affine family survives (each
  shift is internally consistent: on its own orbit the middle term equals the AM). A spot check confirms rigidity: $f(x)=2x$ fails (A)
  at $(x,y)=(2,1)$ ($2\ge 2.5$ is false), while $f(x)=x+1$ satisfies both everywhere.

✻ Brewed for 21m 35s