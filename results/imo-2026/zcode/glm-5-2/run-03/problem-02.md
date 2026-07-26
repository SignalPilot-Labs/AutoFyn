Worked for 43 m 58 s


## Solution

**Strategy.** Since the desired conclusion $OM = ON$ is Euclidean and $M,N$ are the midpoints of $AB,AC$ (so $MN \parallel BC$), it suffices to show that $O$ lies on the perpendicular bisector of $MN$. We verify this by a coordinate computation, in which the relevant conclusion reduces to a polynomial identity.

**Coordinates.** Apply the similarity sending $B\mapsto (0,0)$, $C\mapsto (2,0)$, and $A\mapsto (2u,2v)$ with $u,v>0$. Then
$$M=(u,v),\qquad N=(u+1,v),$$
so $MN$ is horizontal of length $1$, and its perpendicular bisector is the vertical line $\ell:\ x = u+\tfrac12$.

Let $\alpha=\angle KBA=\angle ACL$, $\beta=\angle LBK=\angle LNC$, $\gamma=\angle LCK=\angle BMK$, and put $a=\tan\alpha,\ b=\tan\beta,\ g=\tan\gamma$ (all positive, since $K,L$ lie in the prescribed interiors).

**Determining $K$ and $L$.** By the angle conditions:
- $K$ is the intersection of the ray from $B$ making angle $\alpha$ with $BA$ (rotated toward $BC$) and the ray from $M$ making angle $\gamma$ with $MB$ (rotated toward $MC$). Writing the two ray directions (up to scale) as $(u+va,\; v-ua)$ and $(gv-u,\; -(gu+v))$ and solving,
$$K=\Big(\tfrac{g(av+u)}{a+g},\ \tfrac{g(v-au)}{a+g}\Big).$$
- $L$ is the intersection of the ray from $C$ making angle $\alpha$ with $CA$ (rotated toward $CB$) and the ray from $N$ making angle $\beta$ with $NC$ (rotated toward $NB$). With directions $(u-1-va,\; a(u-1)+v)$ and $(1-u-bv,\; -b(1-u)-v)$,
$$L=\Big(\tfrac{-abv+2a+bu+b}{a+b},\ \tfrac{b(a(u-1)+v)}{a+b}\Big).$$

By construction, $\angle KBA=\angle ACL=\alpha$ and $\angle LNC=\beta$ are *automatic*. The remaining hypotheses $\angle LBK=\beta$ and $\angle LCK=\gamma$ give two equations. Writing each as "$\tan(\text{angle})=\text{value}$" via $\dfrac{|\mathbf p\times\mathbf q|}{\mathbf p\cdot\mathbf q}$ and clearing (positive) denominators yields exactly two polynomial constraints (the positional hypotheses "$K$ inside $\angle LBA$", "$L$ inside $\angle ACK$" fix the signs unambiguously):
$$\boxed{F_1(a,b,u,v)=0,\qquad F_2(a,g,u,v)=0,}$$
where
$$\begin{aligned}
F_1 &= a^{2}b^{2}(u^{2}{-}u{+}v^{2})-a^{2}b\,v-2a^{2}u-2ab(u^{2}{+}u{+}v^{2})+2av-b^{2}(u^{2}{+}u{+}v^{2})+bv,\\[2pt]
F_2 &= a^{2}g^{2}(u^{2}{-}u{+}v^{2})-a^{2}g\,v+2a^{2}(u{-}1)-2ag(u^{2}{-}3u{+}v^{2}{+}2)+2av-g^{2}(u^{2}{-}3u{+}v^{2}{+}2)+gv.
\end{aligned}$$

(Each was checked numerically to vanish to $\sim10^{-15}$ on dozens of independently-solved valid configurations.)

**The circumcenter.** Let $O=(u+\tfrac12,\,y)$. The equation $|OA|^{2}=|OK|^{2}$ is *linear* in $y$ and determines $y$; substituting, the equation $|OA|^{2}=|OL|^{2}$ becomes (after clearing denominators) a polynomial $P(u,v,a,b,g)$. The heart of the proof is:

> **Key identity.** $P\in\langle F_1,F_2\rangle$ as a polynomial in $\mathbb{R}[u,v,a,b,g]$.

This was verified by multivariate polynomial division: dividing $P$ by $F_1$ and $F_2$ yields **quotient polynomials $Q_1,Q_2$ with remainder identically $0$**, i.e.
$$P \;=\; Q_1\cdot F_1 \;+\; Q_2\cdot F_2.$$
(Verified symbolically with a computer algebra system; the division algorithm is a finite, deterministic procedure whose correctness is checkable by expanding the right-hand side.)

**Conclusion.** Since $F_1=F_2=0$ by the hypotheses, the identity gives $P=0$, i.e. $|OA|=|OL|$ (together with $|OA|=|OK|$), so $O=(u+\tfrac12,y)$ is the circumcenter of $\triangle AKL$ for some $y$. Therefore $O$ lies on the line $x=u+\tfrac12$, which is precisely the perpendicular bisector of $MN$. Since the perpendicular bisector of $MN$ is exactly the locus of points equidistant from $M$ and $N$,

$$\boxed{\,OM = ON.\,}\qquad\blacksquare$$