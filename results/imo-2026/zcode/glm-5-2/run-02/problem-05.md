worked for 1h 13min

## Solution

**Answer.** All functions of the form $\boxed{f(x)=x+c}$ for a constant $c\ge 0$.

---

### Verification that $f(x)=x+c$ works

For $f(t)=t+c$, the chain becomes
$$\sqrt{\tfrac{x^{2}+(y+c)^{2}}{2}}\;\ge\;\tfrac{x+(y+c)}{2}\;\ge\;\sqrt{x(y+c)},$$
which is exactly $\mathrm{QM}(x,y+c)\ge \mathrm{AM}(x,y+c)\ge \mathrm{GM}(x,y+c)$, the classical mean inequality for the pair $(x,y+c)$.

---

### Necessity

Write the two inequalities (all quantities are positive, so we may square):
$$\bigl(f(x)+y\bigr)^{2}\le 2\bigl(x^{2}+f(y)^{2}\bigr)\quad\text{...(U)},\qquad \bigl(f(x)+y\bigr)^{2}\ge 4\,x\,f(y)\quad\text{...(L)}.$$

**Step 1. The identity $f(f(y))=2f(y)-y$.** Substitute $x=f(y)$:
- (U) gives $(f(f(y))+y)^{2}\le 2(f(y)^{2}+f(y)^{2})=4f(y)^{2}$, hence $f(f(y))+y\le 2f(y)$.
- (L) gives $(f(f(y))+y)^{2}\ge 4f(y)\cdot f(y)=4f(y)^{2}$, hence $f(f(y))+y\ge 2f(y)$.

So $f(f(y))=2f(y)-y$ for every $y>0$.

**Step 2. The "drift" $c(x):=f(x)-x$ is nonnegative and invariant under $f$.** From Step 1, $f(y)+c(f(y))=f(f(y))=2f(y)-y=f(y)+c(y)$, so $c(f(y))=c(y)$. Iterating, $c$ is constant along each forward orbit $y,f(y),f^{2}(y),\dots=y,y+c(y),y+2c(y),\dots$ Since every iterate lies in $\mathbb R_{>0}$, we must have $c(y)\ge 0$, i.e. $f(y)\ge y$.

**Step 3. Reducing (U).** With $p=c(x),\,q=c(y)$, inequality (U) rewrites as
$$p^{2}+2p(x+y)\le (x-y)^{2}+2q^{2}+4yq.\qquad\text{...(U')}$$

**Step 4. $c$ is constant.** Suppose not. Then $c$ takes two distinct values. Pick $a,b$ with $p:=c(a)>q:=c(b)$.

*Case A: $q>0$ (both values positive).* The forward orbit of $a$ is $\{x_{n}=a+np:n\ge 0\}$ (with $c\equiv p$), and that of $b$ is $\{y_{m}=b+mq:m\ge 0\}$ (with $c\equiv q$). Fix $m$ and view the left–minus–right side of (U') at $(x_{n},y_{m})$ as a quadratic in $x_{n}=a+np$; it is minimized at $x_{n}=y_{m}+p$ with minimum value $2(q-p)(p+q+2y_{m})<0$. Thus (U') is violated whenever $x_{n}$ lies in the interval
$$I_{m}:=\bigl(y_{m}+p-w_{m},\;y_{m}+p+w_{m}\bigr),\qquad w_{m}:=\sqrt{2(p-q)(p+q+2y_{m})}.$$
Now take $m$ large enough that (i) $2w_{m}>p$ and (ii) $y_{m}+p-w_{m}>a$. Then $I_{m}-a\subset(0,\infty)$ has length $2w_{m}>p$, so it contains a positive multiple $np$ of $p$; for that $n\ge 0$, $x_{n}=a+np\in I_{m}$, contradicting (U').

*Case B: $q=0$ (i.e. $c$ takes the value $0$ and some value $p>0$).* Let $Z=\{c=0\}$, $P=\{c=p\}$ (both nonempty). Since $c(f(y))=c(y)$, $P$ is closed under $+p$: $y\in P\Rightarrow y+p\in P$, so every $y_{0}\in P$ generates a ray $\{y_{0}+np:n\ge 0\}\subset P$. For any $z\in Z$, (U') applied to $x\in P,\,y=z$ forces $x$ outside the interval $J(z):=\bigl(z+p-\sqrt{2p(p+2z)},\,z+p+\sqrt{2p(p+2z)}\bigr)$, whose length $2\sqrt{2p(p+2z)}>p$. A $+p$-ray can avoid such an interval only by lying entirely to its right, so each ray in $P$ starts at $\ge z+p+\sqrt{2p(p+2z)}$. If $Z$ were unbounded above, the right endpoint $\to\infty$, forcing $P=\varnothing$ — contradiction. Hence $\alpha:=\inf P<\infty$.

Pick $y_{n}\in Z$ with $y_{n}\to\alpha^{-}$ (such points exist, since otherwise $P$ would extend below $\alpha$). Apply (U') at $x=\alpha+\varepsilon\in P$ (or $x=\alpha\in P$) and $y=y_{n}$: the right side $(x-y_{n})^{2}+2p^{2}+4y_{n}p\to 0\!+\!2p^{2}\!+\!4\alpha p>0$ while the left side $p^{2}+2p(x+y_{n})\to p^{2}+4\alpha p$ is bounded — more precisely $(\alpha+\varepsilon-y_{n})^{2}\to 0$ yet $p^{2}+2p(\alpha+\varepsilon+y_{n})\to p^{2}+4\alpha p>0$, so (U') reads $p^{2}+4\alpha p\le(\text{tiny})$, impossible for $n$ large. Contradiction.

Both cases are impossible, so $c$ is constant.

---

Combining Steps 2 and 4, $f(x)=x+c$ for some constant $c\ge 0$, and these all work. $\blacksquare$