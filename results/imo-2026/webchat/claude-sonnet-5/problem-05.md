start 02:07pm end 02:50pm
# Solution

**Answer.** The solutions are exactly
$$f(x) = x + c, \qquad c \ge 0 \text{ a constant}.$$

Throughout, write the two inequalities as
$$\text{(A): } \sqrt{\tfrac{x^2+f(y)^2}{2}} \ge \tfrac{f(x)+y}{2}, \qquad \text{(B): } \tfrac{f(x)+y}{2} \ge \sqrt{xf(y)}, \qquad \forall x,y>0.$$

## Step 0: These functions work

Fix $c\ge 0$ and let $f(x)=x+c$. For $x,y>0$ set $p=x,\ q=f(y)=y+c>0$. Then
$$f(x)+y = (x+c)+y = x+(y+c)=p+q,$$
so $\dfrac{f(x)+y}{2}=\dfrac{p+q}{2}$ is *exactly* the arithmetic mean of $p,q$. The classical QM–AM–GM inequality, valid for **all** positive reals $p,q$,
$$\sqrt{\tfrac{p^2+q^2}{2}} \ge \tfrac{p+q}{2} \ge \sqrt{pq},$$
becomes precisely (A) and (B). Hence every such $f$ satisfies the condition.

## Step 1: A functional equation

Fix $y>0$ and put $x=f(y)$ in (A) and (B). Since then $x=f(y)$, we get $\sqrt{\tfrac{f(y)^2+f(y)^2}{2}}=f(y)$, so both bounds collapse:

- (A) gives $f(y) \ge \dfrac{f(f(y))+y}{2}$, i.e. $f(f(y)) \le 2f(y)-y$.
- (B) gives $\dfrac{f(f(y))+y}{2}\ge f(y)$, i.e. $f(f(y)) \ge 2f(y)-y$.

Hence
$$f(f(y)) = 2f(y)-y \qquad \text{for all } y>0. \tag{1}$$

## Step 2: A local quadratic bound

Let $d(x):=f(x)-x$. Fix $t>0$ and set $x=f(t)$, $y=z$ (any $z>0$) in (A), (B). By (1), $f(f(t))=2f(t)-t$, so
$$\frac{f(f(t))+z}{2}=f(t)+\frac{z-t}{2}=:P.$$

**Bound (U) from (B).** Since $P\ge \sqrt{f(t)f(z)}\ge 0$ (automatically, as the right side is nonnegative), squaring is valid:
$$P^2 \ge f(t)f(z) \implies f(z) \le \frac{P^2}{f(t)} = f(t)+(z-t)+\frac{(z-t)^2}{4f(t)}. \tag{U}$$
This holds for **all** $z,t>0$.

**Bound (L) from (A).** Now restrict to $|z-t|\le f(t)/2$. Then $P=f(t)+\tfrac{z-t}{2}\ge f(t)/2>0$, so squaring (A) is valid:
$$\frac{f(t)^2+f(z)^2}{2}\ge P^2 \implies f(z)^2 \ge \big(f(t)+(z-t)\big)^2 - \frac{(z-t)^2}{2}.$$
Let $Q=f(t)+(z-t)$. In our range $Q\ge f(t)/2>0$, and one checks $Q^2 \ge (z-t)^2/2$, so
$$f(z)\ge\sqrt{Q^2-\tfrac{(z-t)^2}{2}} = Q\sqrt{1-\tfrac{(z-t)^2}{2Q^2}} \ge Q\Big(1-\tfrac{(z-t)^2}{2Q^2}\Big)= Q-\frac{(z-t)^2}{2Q},$$
using $\sqrt{1-u}\ge 1-u$ for $u\in[0,1]$. Since $Q\ge f(t)/2$,
$$f(z) \ge f(t)+(z-t) - \frac{(z-t)^2}{f(t)}. \tag{L}$$

**Combining.** Subtracting $z$ from (U) and (L), for $|z-t|\le f(t)/2$:
$$d(t) - \frac{(z-t)^2}{f(t)} \le d(z) \le d(t)+\frac{(z-t)^2}{4f(t)},$$
so
$$|d(z)-d(t)| \le \frac{(z-t)^2}{f(t)}. \tag{2}$$

## Step 3: $d$ is constant

From (2), for $z\ne t$ with $|z-t|\le f(t)/2$:
$$\left|\frac{d(z)-d(t)}{z-t}\right| \le \frac{|z-t|}{f(t)} \xrightarrow[z\to t]{} 0.$$
Thus $d$ is differentiable at every $t>0$ with $d'(t)=0$.

Since $(0,\infty)$ is an interval and $d'\equiv 0$ on it, the Mean Value Theorem gives $d(t_2)-d(t_1)=d'(\xi)(t_2-t_1)=0$ for all $t_1,t_2>0$. Hence $d$ is **constant**: there is $c\in\mathbb{R}$ with
$$f(x)=x+c \qquad \text{for all } x>0.$$

## Step 4: Determining the sign of $c$

Since $f$ maps into $\mathbb{R}_{>0}$, we need $x+c>0$ for all $x>0$. If $c<0$, taking $x=|c|/2>0$ gives $f(x)=x+c<0$, a contradiction. Hence $c\ge 0$.

## Conclusion

Combining Steps 0–4:
$$\boxed{f(x) = x + c \text{ for some constant } c \ge 0}$$
are exactly the functions satisfying the given inequalities.