## Status
solved

## Approaches tried
- orbit-interleaving — **solved**. (★) f(f(y))=2f(y)−y from x=f(y); orbits are APs, g:=f−id≥0 and
  orbit-invariant; off-diagonal lever (∗) + interleaving two orbits at ∞ forces all positive defects
  equal; cross-constraint (b−z)²≥4cz makes zero-set and defect-set both open, so connectedness of
  (0,∞) kills coexistence. Answer f(x)=x+c, c≥0.
- convex-duality — **solved**. Same core via a Legendre support-line framing; identical rigor.
- monotone-continuity — **solved**. Same core plus an (unused-in-the-close) squeeze (♦) giving
  order/continuity at image points; the rigidity is routed through (∗), not continuity.

## Current best
Complete proof below (orbit-interleaving, the cleanest of the three verified proofs). All key
identities were re-derived independently in sympy (each reduces to 0), the solution family and the
failure of non-affine perturbations were checked numerically, and the openness inequality chains in
the closing argument were stress-tested.

## Full proof

We determine all functions f:(0,∞)→(0,∞) satisfying, for all x,y>0,
$$\sqrt{\frac{x^2+f(y)^2}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}.\qquad(\dagger)$$

**Answer.** The solutions are exactly the functions $f(x)=x+c$ with $c$ a constant $\ge 0$.

All quantities $x,y,f(x),f(y)$ are positive, so every expression under a root is positive and both
sides of each inequality are positive; squaring a comparison of two positive numbers is an
equivalence, so $(\dagger)$ is equivalent to the pair (for all $x,y>0$)
$$2\bigl(x^2+f(y)^2\bigr)\ge(f(x)+y)^2\ \ (\mathrm{L}^2),\qquad (f(x)+y)^2\ge 4x\,f(y)\ \ (\mathrm{R}^2).$$

### Part (a): Sufficiency
Let $c\ge 0$ and $f(x)=x+c$. Then $f(x)=x+c>0$ for $x>0$, so $f$ maps into $(0,\infty)$. With
$u=y+c=f(y)$:
$$(f(x)+y)^2-4x\,f(y)=(x+c+y)^2-4x(y+c)=(x-y-c)^2\ge 0\quad(\mathrm{R}^2),$$
$$2(x^2+f(y)^2)-(f(x)+y)^2=2x^2+2u^2-(x+u)^2=(x-u)^2=(x-y-c)^2\ge 0\quad(\mathrm{L}^2).$$
Both identities are exact (expand both sides). Hence $f(x)=x+c$ satisfies $(\dagger)$ for every
$c\ge 0$. If $c<0$, then for $0<x<-c$ we get $f(x)<0\notin(0,\infty)$, so $c\ge0$ is necessary for an
affine solution.

### Part (b): Necessity
Let $f$ be any solution; set $g(y):=f(y)-y$.

**Step 1 — (★).** Put $x=f(y)$. In $(\mathrm{R}^2)$: $(f(f(y))+y)^2\ge 4f(y)^2$, so
$f(f(y))+y\ge 2f(y)$. In $(\mathrm{L}^2)$: $(2f(y))^2\ge (f(f(y))+y)^2$, so $f(f(y))+y\le 2f(y)$.
Hence
$$f(f(y))=2f(y)-y\qquad(y>0).\qquad(\star)$$

**Step 2 — orbits, $g\ge0$, orbit-invariance.** Fix $y$, set $a_0=y$, $a_{n+1}=f(a_n)$; all
$a_n>0$. By $(\star)$ at $a_n$, $a_{n+2}=2a_{n+1}-a_n$, so $a_n=y+n\,g(y)$. If $g(y)<0$ then
$a_n\to-\infty$, contradicting $a_n>0$; hence $g(y)\ge 0$. Also
$g(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=g(y)$, so $g$ is constant on the orbit
$\mathcal O(y)=\{y+n\,g(y):n\ge0\}$.

**Step 3 — off-diagonal lever (∗).** Writing $f=\mathrm{id}+g$ in $(\mathrm{R}^2)$ at $(a,b)$,
$$(a+g(a)+b)^2-4a(b+g(b))=(a-b)^2+2(a+b)g(a)+g(a)^2-4a\,g(b)$$
(exact identity). Since the left side is $\ge0$,
$$(a-b)^2+2(a+b)\,g(a)+g(a)^2\ge 4a\,g(b)\qquad(a,b>0).\qquad(\ast)$$

**Step 4 — all positive defects equal.** Suppose $g(a)=s_a>0$, $g(b)=s_b>0$. Set
$A_k=a+k\,s_a\in\mathcal O(a)$ (so $g(A_k)=s_a$, $A_k\to\infty$). For $k$ with $A_k\ge b+s_b$, let
$j=\lfloor(A_k-b)/s_b\rfloor\ge1$ and $B_k=b+j\,s_b\in\mathcal O(b)$ (so $g(B_k)=s_b$); then
$0\le A_k-B_k<s_b$. Applying $(\ast)$ at $(A_k,B_k)$:
$$(A_k-B_k)^2+2(A_k+B_k)s_a+s_a^2\ge 4A_k\,s_b.$$
Using $(A_k-B_k)^2<s_b^2$ and $A_k+B_k\le 2A_k$, $\ 4A_k s_b<s_b^2+4A_k s_a+s_a^2$, i.e.
$s_b<s_a+\frac{s_a^2+s_b^2}{4A_k}$. Let $k\to\infty$: $s_b\le s_a$. By symmetry $s_a\le s_b$, so
$s_a=s_b$. Hence there is one constant $c\ge0$ with $g(y)\in\{0,c\}$ for all $y$.

**Step 5 — no coexistence.** If $c=0$, $f=\mathrm{id}$. Assume $c>0$ and set $Z=\{g=0\}$,
$P=\{g=c\}$, so $(0,\infty)=Z\sqcup P$. For $z\in Z,\ b\in P$, $(\mathrm{R}^2)$ at $(z,b)$ gives
$(z+b)^2\ge 4z(b+c)$, i.e.
$$(b-z)^2\ge 4cz.\qquad(\mathrm C)$$
*$P$ open:* for $b\in P$, $\varepsilon=\min(b/2,\sqrt{cb})$; any $t$ with $|t-b|<\varepsilon$ has
$t>b/2$; if $t\in Z$ then $(\mathrm C)$ gives $(b-t)^2\ge4ct>2cb$, but $(b-t)^2<\varepsilon^2\le cb<2cb$
— contradiction, so $t\in P$. *$Z$ open:* for $z\in Z$, $\varepsilon=\min(z/2,2\sqrt{cz})$; if
$t\in P$ with $|t-z|<\varepsilon$ then $(\mathrm C)$ gives $|t-z|\ge2\sqrt{cz}\ge\varepsilon$ —
contradiction, so $t\in Z$. Thus $(0,\infty)=Z\sqcup P$ is a partition into two open sets; by
connectedness of $(0,\infty)$ one is empty. Hence $g\equiv0$ ($f=\mathrm{id}$) or $g\equiv c$
($f=\mathrm{id}+c$).

### Conclusion
Every solution is $f(x)=x+c$ with $c\ge0$ (Part b), and every such $f$ is a solution (Part a). Thus
$$\boxed{\,f(x)=x+c,\quad c\ge 0.\,}\qquad\blacksquare$$
