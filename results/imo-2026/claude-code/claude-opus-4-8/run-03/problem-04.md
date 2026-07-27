Answer

  Mulan can guarantee victory if and only if $180^\circ/\theta$ is an integer — that is, iff $\theta = \dfrac{180^\circ}{n}$ for some
  integer $n\ge 2$. Equivalently, iff $\theta$ divides $180^\circ$.

  I'll write angles as plain numbers (degrees). Throughout, call an angle a multiple if it is a positive integer multiple of $\theta$
  that is $<180$.

  Setting up
  
⏺ Setting up the move

  Let $\mathcal T$ have angles $X,Y,Z$. Mulan cuts from the vertex with angle $X$ to a point $P$ on the opposite side. Let $p$ be the
  resulting angle at $P$ on the "$Y$-side." As $P$ ranges over the side, $p$ ranges over the open interval $(Z,,180-Y)$, and the two
  pieces are

  $$\text{$Y$-side: } {Y,;p,;180-Y-p},\qquad \text{$Z$-side: } {Z,;180-p,;p-Z}.$$

  (Check: each triple sums to $180$; the two $P$-angles $p,180-p$ are supplementary; the two portions $180-Y-p$ and $p-Z$ of angle $X$
  sum to $X=180-Y-Z$.)

  Mulan chooses the vertex and $p$; Shan‑Yu keeps one piece. Mulan wins the instant some angle equals $\theta$.

  Call a triangle winning if Mulan can force an angle $\theta$ from it. Since Shan‑Yu keeps the worse piece, a $\theta$-free triangle is
  winning iff some cut makes both pieces winning.

  Key Lemma (any $\theta$): a triangle containing a multiple $m\theta$ is winning

  Proof by induction on $m$. If $m=1$ the triangle already has angle $\theta$. If $m\ge2$, cut from the vertex $X=m\theta$, taking the
  $Y$-side portion of $X$ equal to $(m-1)\theta$. The pieces are
  $${Y,;(m-1)\theta,;180-Y-(m-1)\theta}\quad\text{and}\quad{Z,;\theta,;Y+(m-1)\theta}.$$
  The first contains $(m-1)\theta$, the second contains $\theta$. All angles are positive (since $Y+m\theta<180$), so both pieces are
  valid and winning by induction. $\blacksquare$

  If $180/\theta = n \in \mathbb Z$ ($n\ge2$): Mulan wins

  Take any $\theta$-free triangle with angles $\alpha_1\ge\alpha_2\ge\alpha_3$. Note $\alpha_2,\alpha_3<90$ (at most one angle is
  $\ge90$), and $\alpha_3\le 60$.

  Reachable $P$-angles. Any $t\in(\alpha_3,,180-\alpha_3)$ is achievable: for $t\le90$, cut from $\alpha_1$ with
  $Z=\alpha_3,,Y=\alpha_2$ — valid since $\alpha_3<t\le90<180-\alpha_2$; for $t\ge90$ use the supplementary side.

  A multiple lands in this range. Multiples of $\theta$ are symmetric about $90$.
  - $n$ even: $90=\tfrac n2\theta$ is a multiple, and $90\in(\alpha_3,180-\alpha_3)$ since $\alpha_3<90$.
  - $n$ odd: the multiples nearest $90$ are $90\pm\tfrac\theta2$. We need $\alpha_3<90-\tfrac\theta2=90\cdot\frac{n-1}{n}$. For $n=3$
  ($\theta=60$) this is $\alpha_3<60$, which holds: $\alpha_3=60$ forces the equilateral triangle, whose angle $60=\theta$ is excluded.
  For $n\ge5$, $90\cdot\frac{n-1}{n}>60\ge\alpha_3$.

  So there is a multiple $\mu\le90$ with $\mu\in(\alpha_3,180-\alpha_3)$. Cut so the $P$-angle equals $\mu$. Because $180=n\theta$, the
  supplement $180-\mu=(n-\tfrac\mu\theta)\theta$ is also a multiple. Hence:
  $$\text{$Y$-side contains }\mu,\qquad \text{$Z$-side contains }180-\mu,$$
  both multiples of $\theta$. By the Key Lemma both pieces are winning, so every $\theta$-free triangle is winning. Whatever triangle
  Shan‑Yu starts with, Mulan wins in finitely many steps. $\blacksquare$

  If $180/\theta \notin \mathbb Z$: Shan‑Yu wins

  Let $S$ be the set of triangles none of whose angles is a multiple of $\theta$. Such triangles exist (multiples are finite in number),
  and every triangle in $S$ is in particular $\theta$-free. Shan‑Yu starts in $S$ and I claim he can always stay there.

  Take any triangle in $S$ (so $X,Y,Z$ are all non‑multiples) and any cut. Suppose, for contradiction, both pieces contained a multiple.
  Working modulo $\theta$ (write $\equiv$), since $Y\not\equiv0$ and $Z\not\equiv0$:

  - $Y$-side has a multiple $\Rightarrow p\equiv0$ or $180-Y-p\equiv0$;
  - $Z$-side has a multiple $\Rightarrow 180-p\equiv0$ or $p-Z\equiv0$.

  Checking the four combinations:

  ┌─────────────────┬────────────────┬────────────────────────────────────┐
  │    $Y$-side     │    $Z$-side    │            consequence             │
  ├─────────────────┼────────────────┼────────────────────────────────────┤
  │ $p\equiv0$      │ $180-p\equiv0$ │ $180\equiv0$, i.e. $\theta\mid180$ │
  ├─────────────────┼────────────────┼────────────────────────────────────┤
  │ $p\equiv0$      │ $p\equiv Z$    │ $Z\equiv0$                         │
  ├─────────────────┼────────────────┼────────────────────────────────────┤
  │ $p\equiv 180-Y$ │ $180-p\equiv0$ │ $Y\equiv0$                         │
  ├─────────────────┼────────────────┼────────────────────────────────────┤
  │ $p\equiv 180-Y$ │ $p\equiv Z$    │ $Y+Z\equiv180\Rightarrow X\equiv0$ │
  └─────────────────┴────────────────┴────────────────────────────────────┘

  Every case contradicts our hypotheses ($\theta\nmid180$ and $X,Y,Z$ non‑multiples). Therefore at least one piece has no angle that is 
  a multiple of $\theta$ — it lies in $S$. All pieces are nondegenerate ($p$ is strictly interior), so Shan‑Yu keeps that piece and
  remains in $S$.

  Since a triangle in $S$ never has an angle equal to $\theta$ (that would be the multiple $1\cdot\theta$), the game never stops. Mulan
  can never win. $\blacksquare$

  Conclusion

  $$\boxed{;\text{Mulan can force a win} \iff \theta=\frac{180^\circ}{n}\ \text{for some integer } n\ge 2 \iff \theta \mid
  180^\circ.;}$$

  For example $\theta=90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots$ are wins for Mulan (e.g. $\theta=90^\circ$: cutting the
  altitude foot from the largest vertex makes both pieces right triangles), while $\theta=120^\circ,100^\circ,80^\circ,\dots$ — and
  every $\theta$ with $\theta/180$ irrational — are wins for Shan‑Yu.

✻ Worked for 14m 18s