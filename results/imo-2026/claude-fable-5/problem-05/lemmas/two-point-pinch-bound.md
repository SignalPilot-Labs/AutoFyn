# Lemma: two-point-pinch-bound

**Status: CERTIFIED (proof-reviewer, round 1) — proved in `approaches/two-point-pinch.md`, Step 3. The exact identity was re-verified symbolically (sympy): $(y+y'+2u)^2 - 4(y'+u)(y+v) = (y-y')^2 + 4(y'+u)(u-v)$ with $u=d(y')$, $v=d(y)$.**

## Statement

Let $f\colon \mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfy, for all $x,y>0$,

$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x\,f(y)}. \tag{$\ast$}$$

Write $d := f - \mathrm{id}$. Then

$$|d(a)-d(b)| \;\le\; \frac{(a-b)^2}{4\min(a,b)} \qquad \text{for all } a,b>0.$$

## Proof

Uses the certified lemma `core-identity-ap-orbits` ($f(f(y))=2f(y)-y$ and $f\ge\mathrm{id}$).

Fix $y,y'>0$. Substituting $x=f(y')$ (legal: $f(y')>0$) into the right inequality of $(\ast)$ gives $\frac{f(f(y'))+y}{2}\ge\sqrt{f(y')f(y)}$. Both sides are nonnegative, so squaring is equivalent: $(f(f(y'))+y)^2\ge 4f(y')f(y)$. By the core identity, $f(f(y'))=y'+2d(y')$. Writing $u=d(y')$, $v=d(y)$, the exact identity

$$(y+y'+2u)^2-4(y'+u)(y+v) = (y-y')^2 + 4(y'+u)(u-v) = (y-y')^2+4f(y')\,(d(y')-d(y))$$

turns the squared inequality into $(y-y')^2+4f(y')(d(y')-d(y))\ge 0$, i.e.

$$d(y)-d(y') \;\le\; \frac{(y-y')^2}{4f(y')} \;\le\; \frac{(y-y')^2}{4y'},$$

using $f(y')\ge y'>0$. Applying this for both orderings of $\{a,b\}$ and using $\min(a,b)\le a,b$ yields the claim. $\square$

## Remarks

- No sign or size assumption on $d$ is needed beyond $f\ge\mathrm{id}$ (which always holds).
- Telescoping over a $k$-fold subdivision of $[a,b]$ gives $|d(a)-d(b)|\le (b-a)^2/(4ak)\to 0$, so $d$ is constant — this closes the full problem (see `approaches/two-point-pinch.md`, Step 4).
