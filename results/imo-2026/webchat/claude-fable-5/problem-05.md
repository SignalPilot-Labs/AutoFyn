## Answer

$$f(x) = x + c \quad\text{for an arbitrary constant } c \ge 0.$$

**Verification.** If $f(x)=x+c$ with $c\ge 0$, then $f$ maps $\mathbb{R}^{>0}$ to $\mathbb{R}^{>0}$, and the three quantities in the problem become
$$\sqrt{\frac{x^2+(y+c)^2}{2}},\qquad \frac{x+(y+c)}{2},\qquad \sqrt{x(y+c)},$$
which are exactly the quadratic mean, arithmetic mean, and geometric mean of the two positive numbers $x$ and $y+c$. The chain QM $\ge$ AM $\ge$ GM gives both inequalities.

## Proof that no other functions work

Since all quantities are positive, squaring shows the hypothesis is equivalent to: for all $x,y>0$,

$$\text{(1)}\quad 2x^2+2f(y)^2 \ \ge\ (f(x)+y)^2, \qquad\qquad \text{(2)}\quad (f(x)+y)^2 \ \ge\ 4x\,f(y).$$

**Step 1: The identity $f(f(y)) = 2f(y)-y$.**
Fix $y$ and substitute $x=f(y)$ (a legitimate positive value). Inequality (1) gives $4f(y)^2 \ge (f(f(y))+y)^2$, i.e. $2f(y)\ge f(f(y))+y$. Inequality (2) gives $(f(f(y))+y)^2\ge 4f(y)^2$, i.e. $f(f(y))+y\ge 2f(y)$. Hence
$$f(f(y)) = 2f(y)-y \qquad \text{for all } y>0.$$

**Step 2: $f(y)\ge y$, and orbits are arithmetic progressions.**
Fix $y$ and define $y_0=y$, $y_{n+1}=f(y_n)>0$. Applying Step 1 at $y_n$ gives $y_{n+2}=2y_{n+1}-y_n$, so $(y_n)$ is arithmetic: $y_n = y+n\,g(y)$, where $g(y):=f(y)-y$. If $g(y)<0$ then $y_n<0$ for large $n$, impossible. Hence $g(y)\ge 0$ for all $y$, and
$$f\big(y+n\,g(y)\big) = y+(n+1)\,g(y)\qquad (n\ge 0). \tag{$\ast$}$$

**Step 3: If $g(q)=e>0$ for some $q$, then $f(x)=x+e+O(1/x)$.** Precisely, for every $x\ge q+e$ (note $x>e$, so denominators below are positive):
$$x+e-\frac{e^2}{4(x-e)} \ \le\ f(x)\ \le\ x+e+\frac{e^2}{2(2x-e)}. \tag{$\dagger$}$$

*Lower bound.* Let $q_n=q+ne$, so $f(q_n)=q_{n+1}$ by $(\ast)$. Pick the largest $n\ge0$ with $q_{n+1}\le x$ (it exists since $q_1\le x$ and $q_n\to\infty$). Write $A=q_{n+1}$ and $s=x-A\in[0,e)$. Inequality (2) with $y=q_n=A-e$ gives $f(x)\ge 2\sqrt{xA}-(A-e)=2\sqrt{A(A+s)}-A+e$. Since $2\sqrt{A(A+s)} = 2A+s-\big(\sqrt{A+s}-\sqrt A\big)^2 \ge 2A+s-\frac{s^2}{4A}$, we get $f(x)\ge x+e-\frac{s^2}{4A}$. As $s<e$ and $A=x-s> x-e$, the lower bound in $(\dagger)$ follows.

*Upper bound.* Pick the largest $m\ge 0$ with $q_m\le x-e$ (it exists since $q_0\le x-e$), and write $s'=(x-e)-q_m\in[0,e)$, so $q_m = x-e-s'$ and $f(q_m)=x-s'$. Inequality (1) with $y=q_m$ gives
$$(f(x)+q_m)^2 \le 2x^2+2(x-s')^2 = (2x-s')^2+s'^2.$$
Using $\sqrt{B^2+r}\le B+\frac{r}{2B}$ with $B=2x-s'>0$:
$$f(x)\ \le\ (2x-s')+\frac{s'^2}{2(2x-s')}-(x-e-s') \ =\ x+e+\frac{s'^2}{2(2x-s')},$$
and since $s'<e$, the upper bound in $(\dagger)$ follows.

**Step 4: $g$ takes at most one positive value, and $g\equiv e$ on a ray.**
Suppose $g(q)=e>0$. If $g(b)=e'>0$ for any $b$, then by $(\ast)$ the points $b_n=b+ne'\to\infty$ satisfy $g(b_n)=e'$; applying $(\dagger)$ at $x=b_n$ for large $n$ and letting $n\to\infty$ forces $e'=e$. Hence
$$g(x)\in\{0,e\}\ \text{ for every } x>0.$$
Moreover, for $x\ge \max(q+e,\,2e)$ we have $x-e\ge e$, so $(\dagger)$ gives $g(x)\ge e-\tfrac{e^2}{4e}=\tfrac{3e}{4}>0$, hence
$$g(x)=e \quad\text{for all } x\ge \max(q+e,\,2e). \tag{$\ddagger$}$$

**Step 5: If some $g$-value is positive, there is no fixed point.**
Suppose, in the situation of Step 4, that $f(p)=p$ for some $p$. I claim every $t\in[p,\,p+2e]$ satisfies $g(t)=0$. Indeed, if $g(t)=e$ (the only alternative by Step 4), then inequality (1) with $x=t$, $y=p$ reads $(t+e+p)^2\le 2t^2+2p^2$, which after expansion is equivalent to
$$(t-p)^2 \ \ge\ 2e(t+p)+e^2.$$
But writing $t=p+u$ with $0\le u\le 2e$,
$$2e(t+p)+e^2-(t-p)^2 \;=\; 4ep+e^2+u(2e-u)\;\ge\; 4ep+e^2\;>\;0,$$
a contradiction. So $[p,\,p+2e]\subseteq \{g=0\}$; in particular $p+2e$ is again a fixed point. By induction, $[p+2ke,\,p+2(k+1)e]\subseteq\{g=0\}$ for every $k\ge 0$, hence
$$[p,\infty)\subseteq\{g=0\}.$$
Taking $x^\*=\max(p,\,q+e,\,2e)$, this says $g(x^\*)=0$, while $(\ddagger)$ says $g(x^\*)=e>0$ — a contradiction. Hence no fixed point exists.

**Conclusion.**
Either $g$ never takes a positive value, in which case $g\equiv 0$ and $f(x)=x$; or $g$ takes a positive value, in which case by Step 4 its only possible values are $0$ and $e$, and by Step 5 the value $0$ never occurs, so $g\equiv e$ and $f(x)=x+e$. In both cases $f(x)=x+c$ with a constant $c\ge0$, and by the verification above every such function indeed satisfies both inequalities. $\blacksquare$

A remark on why the whole family appears: for $f(x)=x+c$ the given chain is *exactly* the QM–AM–GM chain for the pair $(x,\,y+c)$, so the problem's inequalities are tight along $x=y+c$; the proof above essentially shows that this forced tightness (Step 1) rigidifies $f$ into a translation.

time: 8 mins