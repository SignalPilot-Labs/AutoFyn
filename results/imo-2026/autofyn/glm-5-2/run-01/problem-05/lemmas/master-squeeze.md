# Lemma: Master Squeeze (certified)

> **Certified** by proof-reviewer, round 2. Originally proven in
> `approaches/master-sos-identity.md` (both directions) and independently
> re-derived in `approaches/orbit-monotonicity-sandwich.md` Section 4.
> Symbolically verified by sympy (both identities expand to zero residue).

## Statement

Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ and put $g(t)=f(t)-t$. For $x,y>0$ define
$$U(x,y)=\frac{x^{2}+f(y)^{2}}{2}-\Bigl(\frac{f(x)+y}{2}\Bigr)^{2},
\qquad
L(x,y)=\Bigl(\frac{f(x)+y}{2}\Bigr)^{2}-x\,f(y).$$
(Thus the original chain
$\sqrt{(x^{2}+f(y)^{2})/2}\ge(f(x)+y)/2\ge\sqrt{xf(y)}$ is exactly
$U(x,y)\ge0\land L(x,y)\ge0$ for all $x,y>0$.)

**(i) SOS identity.**
$$U+L=\frac{(x-f(y))^{2}}{2},\qquad
U-L=-\frac{(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)}{2}.$$

**(ii) Equivalence (both directions).** For every $x,y>0$,
$$U(x,y)\ge0\ \text{and}\ L(x,y)\ge0
\iff
\bigl|(g(x)-g(y))\bigl(g(x)+g(y)+2x+2y\bigr)\bigr|\le(x-f(y))^{2}.$$
In particular, the master squeeze is **equivalent** to the original chain:
every $f$ satisfying the chain satisfies the squeeze, and conversely.

**(iii) Reduced form under $g\ge0$.** If additionally $g\ge0$ on $\mathbb R_{>0}$
(every solution enjoys this — proven separately via orbit forward-positivity),
then $g(x)+g(y)+2x+2y\ge2x+2y>0$, the absolute value on the second factor
drops, and the equivalence becomes
$$\text{original chain}\ \iff\
|g(x)-g(y)|\bigl(g(x)+g(y)+2x+2y\bigr)\le(x-f(y))^{2},$$
in particular
$$|g(x)-g(y)|\le\frac{(x-f(y))^{2}}{2x+2y}\qquad\forall x,y>0.$$

## Proof

**(i)** Direct polynomial expansion with $f(x)=x+g(x)$, $f(y)=y+g(y)$.
Sympy-verified: $U+L-(x-f(y))^{2}/2\equiv0$ and
$U-L+(g(x)-g(y))(g(x)+g(y)+2x+2y)/2\equiv0$. (Completing the square.)

**(ii)** Elementary biconditional: for $a,b\in\mathbb R$,
$$a\ge0\land b\ge0\iff a+b\ge0\land|a-b|\le a+b.$$
$(\Rightarrow)$ $a,b\ge0\Rightarrow a+b\ge0$ and $-a\le b,\,-b\le a$ give
$|a-b|\le a+b$. $(\Leftarrow)$ $a+b\ge0$ and $|a-b|\le a+b$: from
$a-b\le a+b$ get $b\ge0$; from $b-a\le a+b$ get $a\ge0$.
Apply with $a=U$, $b=L$. Since $U+L=(x-f(y))^{2}/2\ge0$ automatically (a
square), the condition $a+b\ge0$ is free, reducing to
$U,L\ge0\iff|U-L|\le U+L=(x-f(y))^{2}/2$. Substituting (i) gives (ii). Both
directions are the two directions of the Fact; no implication is left
implicit.

**(iii)** Under $g\ge0$, $g(x)+g(y)+2x+2y\ge2x+2y>0$, so
$|g(x)+g(y)+2x+2y|=g(x)+g(y)+2x+2y$, and (ii) specialises. Dividing by the
positive second factor and bounding it below by $2x+2y$ gives the weaker but
useful $|g(x)-g(y)|\le(x-f(y))^{2}/(2x+2y)$.

## Corollaries (proven)

- **Orbit invariance.** Setting $x=f(y)$ in (ii): RHS $=(f(y)-f(y))^{2}=0$,
  hence LHS $=0$; the second factor is $>0$ under $g\ge0$, so $g(f(y))=g(y)$.
- **Swapped two-window min.** Applying (iii) to $(x,y)$ and $(y,x)$:
  $|g(x)-g(y)|\le\min\{(x-f(y))^{2},(y-f(x))^{2}\}/(g(x)+g(y)+2x+2y)$.

## Note

A pure algebraic kill from (iii) plus $g\ge0$ alone (without structural input
such as orbit arithmetic) is **not** established; the squeeze is numerically
rigid but the one-move kill remains open. The squeeze is intended as an
importable engine for approaches that add structural input.
