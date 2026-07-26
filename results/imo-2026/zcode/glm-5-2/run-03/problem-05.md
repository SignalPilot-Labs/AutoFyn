Worked for 1h 32 mins

## Solution

**Answer.** All functions of the form $\boxed{f(x)=x+c}$ for a constant $c\ge 0$.

---

### Verification (sufficiency)

For $f(t)=t+c$, both sides of each inequality differ by the same perfect square:
$$\frac{x^{2}+f(y)^{2}}{2}-\left(\frac{f(x)+y}{2}\right)^{2}=\frac{(x-y-c)^{2}}{4}\ge 0,\qquad \left(\frac{f(x)+y}{2}\right)^{2}-xf(y)=\frac{(x-y-c)^{2}}{4}\ge 0.$$
Hence every $f(x)=x+c$ with $c\ge 0$ works.

### Necessity

Assume $f$ satisfies the conditions.

**Step 1 (key identity).** Substitute $x=f(y)$. The right inequality gives $\frac{f(f(y))+y}{2}\ge\sqrt{f(y)^{2}}=f(y)$, so $f(f(y))\ge 2f(y)-y$. The left inequality gives $\sqrt{\frac{f(y)^{2}+f(y)^{2}}{2}}=f(y)\ge\frac{f(f(y))+y}{2}$, so $f(f(y))\le 2f(y)-y$. Therefore
$$f(f(y))=2f(y)-y\quad\text{for all }y>0.\tag{E1}$$

**Step 2 ($f\ge\mathrm{id}$).** Let $u(t)=f(t)-t$. From (E1), $u(f(t))=f(f(t))-f(t)=f(t)-t=u(t)$, so $u$ is constant on forward orbits. By induction $f^{n}(t)=t+n\,u(t)$. Every iterate is positive, so $t+n\,u(t)>0$ for all $n\ge 0$; if $u(t)<0$, taking $n>t/|u(t)|$ gives a contradiction. Thus $u(t)\ge 0$, i.e. $f(t)\ge t$. Forward orbits partition $(0,\infty)$ into disjoint sets $O_{t}=\{t+n\,u(t):n\ge 0\}$.

**Step 3 (reformulation).** Writing $f(x)=x+u(x)$, $f(y)=y+u(y)$, the right inequality $(f(x)+y)^{2}\ge 4xf(y)$ becomes
$$(\alpha):\qquad 4\bigl(x\,u(y)-y\,u(x)\bigr)\le (x-y+u(x))^{2}\quad\text{for all }x,y>0.$$

**Step 4 (positive displacements are all equal).** Let $O=\{a+nd:n\ge 0\}$ (with $u\equiv d>0$) and $O'=\{a'+nd':n\ge 0\}$ (with $u\equiv d'>0$) be two orbits; suppose $d'>d$. Take $x\in O$ very large and choose $y\in O'$ nearest to $x$; since $O'$ has spacing $d'$, $|x-y|\le d'/2$. Applying $(\alpha)$:
$$4(xd'-yd)\le(x-y+d)^{2}\le(d'/2+d)^{2}\quad(\text{bounded}).$$
Yet $xd'-yd=x(d'-d)+(x-y)d\to+\infty$ as $x\to\infty$. Contradiction. By symmetry $d>d'$ is impossible too, so $d=d'$.

**Step 5 (no fixed point coexists with a positive displacement).** Suppose $a$ is a fixed point ($u(a)=0$) and some point has $u>0$; by Step 4 all such points share one value $d'>0$. Set $S=\{t:u(t)=d'\}$, $F=\{t:u(t)=0\}$. Putting $x=a$, $y\in S$ in $(\alpha)$: $4a\,d'\le(a-y)^{2}$, so $|a-y|\ge 2\sqrt{ad'}$ for every $y\in S$. Hence $(a-2\sqrt{ad'},\,a+2\sqrt{ad'})\cap(0,\infty)\subseteq F$.

*Propagation.* For $t\in F$ with $t>0$, the point $\varphi(t)=t+\sqrt{td'}\in(t,\,t+2\sqrt{td'})\subseteq F$. The sequence $a_{n+1}=\varphi(a_{n})$ lies in $F$, is strictly increasing, and is unbounded (each increment $\sqrt{a_{n}d'}\ge\sqrt{ad'}>0$). Thus $(a,\infty)\subseteq F$. Any $s\in S$ has an unbounded orbit $\{s+md'\}$ that enters $(a,\infty)\subseteq F$, contradicting $u=d'$ on $S$. So $S=\varnothing$, and $u\equiv 0$.

**Conclusion.** Either $u\equiv 0$, or $u$ never vanishes and is constant (equal to some $c>0$) by Step 4. In all cases $f(x)=x+c$ with $c\ge 0$. $\blacksquare$