Crunched for 1h 6m 12s
⏺ Answer

$$\boxed{f(x) = x + c \quad\text{for an arbitrary constant } c \ge 0.}$$

Throughout write the two hypotheses as, for all $x,y>0$:
$$\textbf{(1)}\quad \sqrt{\tfrac{x^2+f(y)^2}{2}}\ \ge\ \tfrac{f(x)+y}{2}, \qquad\qquad \textbf{(2)}\quad
\tfrac{f(x)+y}{2}\ \ge\ \sqrt{x,f(y)} .$$

These functions work

Let $f(x)=x+c$ with $c\ge0$. Then $f$ maps $\mathbb R_{>0}\to\mathbb R_{>0}$, and the middle term equals
$\frac{x+(y+c)}{2}$, the arithmetic mean of the two positive numbers $x$ and $y+c=f(y)$. Hence:

- (2) is AM–GM for $x,,f(y)$: $\ \frac{x+f(y)}{2}\ge\sqrt{x,f(y)}$. ✓
- (1) is QM–AM for $x,,f(y)$: $\ \sqrt{\frac{x^2+f(y)^2}{2}}\ge\frac{x+f(y)}{2}$. ✓

Both hold for all $x,y>0$ (with equality exactly when $x=f(y)=y+c$).

No other functions work

Set $M(x):=f(x)-x$. We show $M$ is a nonnegative constant.

Lemma 1: $f(x)\ge x$ for all $x$.

Put $x=f(y)$ in (2): $\ \frac{f(f(y))+y}{2}\ge\sqrt{f(y)^2}=f(y)$, so $f(f(y))\ge 2f(y)-y$.
Put $x=f(y)$ in (1): $\ \sqrt{f(y)^2}\ge\frac{f(f(y))+y}{2}$, so $f(f(y))\le 2f(y)-y$.
Therefore
$$f(f(y))=2f(y)-y \qquad\text{for all }y>0. \tag{$\star$}$$
Fix $y_0>0$ and iterate: $y_{n+1}:=f(y_n)$. Since $f$ takes positive values, every $y_n>0$. By $(\star)$,
$y_{n+2}=2y_{n+1}-y_n$, so ${y_n}$ is arithmetic with common difference $d=f(y_0)-y_0$, giving $y_n=y_0+nd$. If
$d<0$ then $y_n\to-\infty$, contradicting $y_n>0$. Hence $d\ge0$, i.e. $f(y_0)\ge y_0$. So $M\ge 0$
everywhere. $\qquad\blacksquare$

Lemma 2: $\displaystyle M(u)-M(v)\le\frac{(u-v)^2}{4v}$ for all $u,v>0$.

From (2): $f(x)\ge 2\sqrt{x,f(u)}-u$. From (1): $f(x)\le\sqrt{2x^2+2f(v)^2}-v$. Both bound the same value
$f(x)$, so for all $x,u,v>0$,
$$2\sqrt{x,f(u)}-u\ \le\ \sqrt{2x^2+2f(v)^2}-v .$$
Choose $x=f(u)$. The left side becomes $2f(u)-u$, and
$$2f(u)-u+v\ \le\ \sqrt{2f(u)^2+2f(v)^2}.$$
The left side is positive (it equals $u+2M(u)+v>0$), so squaring is valid. With $\delta:=v-u$ and $a:=f(u)$,
The left side is positive (it equals $u+2M(u)+v>0$), so squaring is valid. With $\delta:=v-u$ and $a:=f(u)$,
$$\big(2a+\delta\big)^2\le 2a^2+2f(v)^2\ \Longrightarrow\ 2f(v)^2-2(a+\delta)^2\ge \delta^2 .$$
Since $a+\delta=f(u)+v-u=v+M(u)$ and $f(v)=v+M(v)$, the left side is
$$2\big[(v+M(v))^2-(v+M(u))^2\big]=2\big(M(v)-M(u)\big)\big(2v+M(u)+M(v)\big).$$
Thus $2\big(M(v)-M(u)\big)\big(2v+M(u)+M(v)\big)\ge -,\delta^2$, i.e.
$$2\big(M(u)-M(v)\big)\big(2v+M(u)+M(v)\big)\ \le\ (u-v)^2 .$$
By Lemma 1, $M(u),M(v)\ge0$, so $2v+M(u)+M(v)\ge 2v>0$. If $M(u)\ge M(v)$, dividing gives $M(u)-M(v)\le
\frac{(u-v)^2}{4v}$; if $M(u)<M(v)$ the inequality holds trivially. $\qquad\blacksquare$

Lemma 3: $M$ is constant.

Fix $u,v>0$ and let $m:=\min(u,v)>0$. Split into $n$ equal steps: $z_k=u+\frac{k}{n}(v-u)$, $k=0,\dots,n$, so
consecutive gaps are $\frac{|v-u|}{n}$ and every $z_k\ge m$. Applying Lemma 2 to each consecutive pair and
telescoping,
$$M(u)-M(v)=\sum_{k=0}^{n-1}\big(M(z_k)-M(z_{k+1})\big)\le\sum_{k=0}^{n-1}\frac{(v-u)^2/n^2}{4z_{k+1}}\le
n\cdot\frac{(v-u)^2}{4mn^2}=\frac{(v-u)^2}{4mn}.$$
Letting $n\to\infty$ gives $M(u)-M(v)\le0$. Swapping $u,v$ gives $M(v)-M(u)\le0$. Hence $M(u)=M(v)$.
$\qquad\blacksquare$

Conclusion

So $M\equiv c$ for a constant $c$, i.e. $f(x)=x+c$. Since $f(x)>0$ for all $x>0$ forces $x+c>0$ as $x\to0^+$,
we need $c\ge0$ (consistent with Lemma 1).

Combined with the verification above, the complete solution set is
$$f(x)=x+c,\qquad c\ge 0 .$$

Remarks on the proof's integrity

- The substitution $x=f(y)$ makes both (1) and (2) tight (QM = AM = GM), forcing the identity $(\star)$, which
drives Lemma 1.
- Every pairwise algebraic combination of (1) and (2) collapses to a perfect square (no information); the
decisive step is combining the lower bound from (2) with the upper bound from (1) at the single well-chosen
point $x=f(u)$, producing the quadratic modulus of continuity in Lemma 2. Quadratic control kills all variation
under telescoping (Lemma 3) — this is why $M$ must be exactly constant rather than merely bounded.

I sanity‑checked $f(x)=x+c$ numerically at generic points and at the equality locus $x=y+c$ (both inequalities
become equalities there), and verified each algebraic reduction above.

