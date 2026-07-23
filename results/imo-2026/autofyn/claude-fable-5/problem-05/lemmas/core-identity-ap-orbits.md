# Lemma: core-identity-ap-orbits

**Status: CERTIFIED (proof-reviewer, round 1) — proved in `approaches/marching-orbits.md`, Part 2 (Lemmas 1–2); identical content independently proved in `approaches/two-point-pinch.md`, Steps 1–2. All steps re-verified: squaring legality, the x=f(y) collapse, the induction, and the Archimedean contradiction.**

## Statement

Let $f\colon \mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfy, for all $x,y>0$,

$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x\,f(y)}. \tag{$\ast$}$$

Write $d(y):=f(y)-y$. Then:

1. **(Core identity)** $f(f(y)) = 2f(y)-y$ for all $y>0$.
2. **(Orbit invariance)** $d(f(y))=d(y)$ for all $y>0$.
3. **(AP orbits)** For every $y>0$, the forward orbit $y_0=y$, $y_{n+1}=f(y_n)$ satisfies $y_n = y+n\,d(y)>0$ and $d(y_n)=d(y)$ for all integers $n\ge 0$.
4. **($f\ge\mathrm{id}$)** $d(y)\ge 0$ for all $y>0$.

## Proof

Since $x^2+f(y)^2>0$, $\frac{f(x)+y}{2}>0$, $xf(y)>0$, the chain $(\ast)$ is equivalent (squaring, strictly increasing on $\mathbb{R}_{\ge0}$) to
$$\text{(L)}\ \ 2(x^2+f(y)^2)\ge(f(x)+y)^2, \qquad \text{(R)}\ \ (f(x)+y)^2\ge 4xf(y).$$

**1.** Substitute $x=f(y)$ (legal: $f(y)>0$) into $(\ast)$. The outer terms both become $\sqrt{f(y)^2}=f(y)$ and $\sqrt{f(y)\cdot f(y)}=f(y)$, so $f(y)\ge \frac{f(f(y))+y}{2}\ge f(y)$, forcing $f(f(y))=2f(y)-y$.

**2.** $d(f(y)) = f(f(y))-f(y) = (2f(y)-y)-f(y) = f(y)-y = d(y)$.

**3.** Induction on $n$. Base $n=0$: $y_0=y>0$, $d(y_0)=d(y)$, $y_0=y+0\cdot d(y)$. Step: if $y_n>0$, $d(y_n)=d(y)$, $y_n=y+nd(y)$, then $y_{n+1}=f(y_n)>0$ (codomain), $d(y_{n+1})=d(f(y_n))=d(y_n)=d(y)$ by 2, and $y_{n+1}=y_n+d(y_n)=y+(n+1)d(y)$.

**4.** If $d(y)<0$ for some $y>0$, choose an integer $n>y/|d(y)|$ (Archimedean property); then $y_n=y+n\,d(y)<y-y=0$, contradicting $y_n>0$ from 3. $\square$
