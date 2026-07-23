# Problem 2 — Solution

*Written: 2026-07-15 15:38 PDT (Claude Fable 5). Numerical/exact verification runs performed 2026-07-15 ~15:20–15:35 PDT; see the companion file `problem2_verification.md`.*

## Statement

Let $ABC$ be a triangle, and let $M$ and $N$ be the midpoints of $AB$ and $AC$, respectively.
Let $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies
inside $\angle LBA$, $L$ lies inside $\angle ACK$, and
$$
\angle KBA=\angle ACL,\qquad
\angle LBK=\angle LNC,\qquad
\angle LCK=\angle BMK .
$$
If $O$ is the circumcentre of triangle $AKL$, prove that $OM=ON$.

---

## Overview of the proof

We place the triangle in the complex plane. The seven hypotheses (three angle equalities, plus the
four positional conditions) are shown to be **exactly equivalent** to the following analytic data:
there exist real numbers $\varphi$, $\rho>0$, $\sigma>0$ such that

$$
K=c\left(1-\rho e^{-i\varphi}\right),\qquad
L=b\,e^{i\alpha}\left(1-\sigma e^{i\varphi}\right),
$$

(where $A=0$, $B=c>0$, $C=be^{i\alpha}$), together with **two real polynomial–trigonometric
equations** $E_1=0$ and $E_2=0$ in $(\rho,\sigma,\varphi)$ — one coming from
$\angle LCK=\angle BMK$, the other from $\angle LBK=\angle LNC$; the condition
$\angle KBA=\angle ACL$ is absorbed in the shared parameter $\varphi$.

The conclusion $OM=ON$ is likewise shown to be equivalent to a single real equation $F=0$ in the
same quantities. The proof is then completed by an explicit algebraic identity
$$
2\sin(\alpha+\varphi)\cdot F \;=\; \lambda\,E_1+\mu\,E_2
$$
with explicit polynomial multipliers $\lambda,\mu$, verified by comparing coefficients; since
$\sin(\alpha+\varphi)>0$ in the configuration, $E_1=E_2=0$ forces $F=0$.

---

## Notation and normalization

**Coordinates.** All hypotheses and the conclusion are statements about (undirected) angles and
distances, hence invariant under isometries of the plane. Applying a suitable isometry (including a
reflection if necessary), we may and do assume that in the complex plane
$$
A=0,\qquad B=c>0,\qquad C=b\,e^{i\alpha},\qquad b=CA>0,\quad \alpha=\angle BAC\in(0,\pi),
$$
so that $C$ lies in the open upper half-plane. Then
$$
M=\tfrac{c}{2},\qquad N=\tfrac{b}{2}e^{i\alpha}.
$$

For $z\neq 0$ we write $\arg z\in(-\pi,\pi]$; equalities of arguments below are understood
modulo $2\pi$ where indicated. The (undirected) angle at a vertex $P$ between rays $PQ$, $PR$
equals $\left|\arg\frac{Q-P}{R-P}\right|$.

**Angle names.** Set
$$
\varphi:=\angle KBA=\angle ACL,\qquad
\psi:=\angle LBK=\angle LNC,\qquad
\theta:=\angle LCK=\angle BMK,
$$
each lying in $(0,\pi)$ (the points are positioned so that none of these angles is $0$ or $\pi$;
see Step 0). Abbreviate
$$
s:=\sin\alpha,\quad t:=\sin\varphi,\quad \hat c:=\cos\varphi,\quad
s_1:=\sin(\alpha+\varphi),\quad s_2:=\sin(\alpha+2\varphi).
$$

---

## Step 0 — Position facts

**Lemma 0.** With the normalization above:

1. $K$ and $L$ lie in the open upper half-plane: $\operatorname{Im}K>0$, $\operatorname{Im}L>0$.
2. $K$ and $L$ lie strictly on the same side of line $AC$ as $B$; analytically,
   $\operatorname{Im}\!\big[(P-X)e^{-i\alpha}\big]<0$ for $P\in\{K,L\}$ and any point $X$ on line $AC$.
3. $K,L\notin\{A,B,C,M,N\}$.
4. $\varphi=\angle ACL<\angle ACB$, and consequently $0<\alpha+\varphi<\pi$, i.e. $s_1>0$.

*Proof.* A point $P$ interior to a triangle $XYZ$ is a convex combination
$P=w_XX+w_YY+w_ZZ$ with all weights positive; hence for any line $\ell$, the signed distance of
$P$ to $\ell$ is the same positive combination of the signed distances of $X,Y,Z$.

(1) For $K$ inside $\triangle BMC$: relative to line $AB$ (the real axis), $B$ and $M$ have signed
distance $0$ and $C$ has positive signed distance; the combination is $w_C\,d(C)>0$. For $L$
inside $\triangle BNC$: $d(B)=0$, $d(N),d(C)>0$, so the combination is positive.

(2) Fix line $AC$ and orient signed distance so that $B$ has positive sign. For
$K\in\operatorname{int}\triangle BMC$: $d(C)=0$ and $d(B),d(M)>0$ ($M$ is not on line $AC$,
and lies on segment $AB$ on $B$'s side), so $d(K)>0$. For
$L\in\operatorname{int}\triangle BNC$: $d(N)=d(C)=0$, $d(B)>0$, so $d(L)=w_B\,d(B)>0$.
Analytically, the $B$-side of line $AC$ is exactly
$\{z:\operatorname{Im}[(z-X)e^{-i\alpha}]<0\}$ for any $X$ on the line: the function
$z\mapsto\operatorname{Im}[(z-X)e^{-i\alpha}]$ is affine in $z$, vanishes exactly on the line
through $X$ with direction $e^{i\alpha}$ (which is line $AC$), hence has constant sign on each
open side; its value does not depend on the choice of $X$ on the line (changing $X$ shifts the
argument by a real multiple of $e^{i\alpha}$); and taking $X=A=0$, its value at $z=B$ is
$\operatorname{Im}[c\,e^{-i\alpha}]=-c\sin\alpha<0$.

(3) The interior of a triangle contains none of its vertices, so $K\neq B,M,C$ and
$L\neq B,N,C$; moreover $\triangle BMC$ meets line $AB$ in the segment $MB\not\ni A$ and
$\triangle BNC$ meets line $AC$ in the segment $NC\not\ni A$, so $A\notin\{K,L\}$. Finally
$K\neq N$ and $L\neq M$ hold because $K,L$ lie strictly off lines $AC$ and $AB$ respectively,
by (1)–(2).

(4) $L$ is interior to $\triangle BNC$; by the convex-combination argument applied to line $BC$
($d(B)=d(C)=0$, $d(N)>0$) $L$ is also strictly inside $\triangle ABC$. Hence ray $CL$ lies
strictly inside $\angle ACB$, so $\varphi=\angle ACL<\angle ACB=:\gamma$. Since
$\alpha+\gamma<\pi$, we get $\alpha+\varphi\in(0,\pi)$ and $s_1>0$. $\blacksquare$

---

## Step 1 — Analytic form of the hypotheses

**Lemma 1.** Under the hypotheses of the problem there exist
$\rho=\dfrac{BK}{c}>0$ and $\sigma=\dfrac{CL}{b}>0$ such that
$$
K=c\left(1-\rho e^{-i\varphi}\right),\qquad
L=b\,e^{i\alpha}\left(1-\sigma e^{i\varphi}\right),
\tag{1.1}
$$
and moreover
$$
E_1:=b\,t-c\,s_1+c\rho\,(2s+s_2)-2c\rho^2 s_1=0,
\tag{$E_1$}
$$
$$
E_2:=c\,t-b\,s_1+b\sigma\,(2s+s_2)-2b\sigma^2 s_1=0.
\tag{$E_2$}
$$

*Proof.* We first convert each hypothesis into a statement about arguments.

**(a) Rays from points of the real axis.** Since $\operatorname{Im}K>0$ and $B,M,A$ lie on the
real axis, we have $\arg(K-B),\ \arg(K-M)\in(0,\pi)$, and:

* $\angle KBA=\bigl|\arg\frac{K-B}{A-B}\bigr|=\bigl|\arg(K-B)-\pi\bigr|=\pi-\arg(K-B)$.
  Hence $\angle KBA=\varphi$ gives $\arg(K-B)=\pi-\varphi$, i.e.
  $K-B=-BK\,e^{-i\varphi}$, which is the first formula in (1.1).
* $\angle BMK=\bigl|\arg\frac{K-M}{B-M}\bigr|=\arg(K-M)$ (as $B-M=c/2>0$). Hence
  $$
  \arg(K-M)=\theta. \tag{1.2}
  $$
* Similarly $\operatorname{Im}L>0$ gives $\angle ABL=\pi-\arg(L-B)$, so, anticipating (c) below,
  $$
  \arg(L-B)=\pi-\angle ABL. \tag{1.3}
  $$

**(b) Rays from points of line $AC$.** Let $P\in\{K,L\}$ and let $X\in\{C,N\}$ be on line $AC$.
By Lemma 0(2), $w:=(P-X)e^{-i\alpha}$ has $\operatorname{Im}w<0$, i.e. $\arg w\in(-\pi,0)$.

* Ray $XA$ has direction $-e^{i\alpha}$ when $X=C$ (and ray $NC$ has direction $+e^{i\alpha}$).
  Thus
  $$
  \angle ACP=\Bigl|\arg\frac{P-C}{A-C}\Bigr| =\bigl|\arg(-w)\bigr| =\pi+\arg w
  \quad\text{for } w=(P-C)e^{-i\alpha},
  $$
  since $\arg w\in(-\pi,0)$ implies $\arg(-w)=\pi+\arg w\in(0,\pi)$. Hence
  $$
  \arg(P-C)=\alpha+\angle ACP-\pi,\qquad\text{i.e.}\qquad
  \arg(C-P)=\alpha+\angle ACP \pmod{2\pi}. \tag{1.4}
  $$
  Applying this to $P=L$ with $\angle ACL=\varphi$ gives
  $L=C-CL\,e^{i(\alpha+\varphi)}=be^{i\alpha}\bigl(1-\sigma e^{i\varphi}\bigr)$ — the second
  formula in (1.1).
* For $X=N$:
  $$
  \angle LNC=\Bigl|\arg\frac{L-N}{C-N}\Bigr|=\bigl|\arg[(L-N)e^{-i\alpha}]\bigr|
  =-\arg[(L-N)e^{-i\alpha}],
  $$
  so $\angle LNC=\psi$ gives
  $$
  \arg(L-N)=\alpha-\psi. \tag{1.5}
  $$

**(c) Angle additivity.** Because $K$ lies inside $\angle LBA$, ray $BK$ lies strictly between rays
$BA$ and $BL$, whence
$$
\angle ABL=\angle ABK+\angle KBL=\varphi+\psi .
$$
Because $L$ lies inside $\angle ACK$, ray $CL$ lies strictly between rays $CA$ and $CK$, whence
$$
\angle ACK=\angle ACL+\angle LCK=\varphi+\theta .
$$

**(d) The two equations.** Combining (1.4) (with $P=K$) and (1.2):
$$
\arg(C-K)=\alpha+\varphi+\theta,\qquad \arg(K-M)=\theta \pmod{2\pi},
$$
so that
$$
T_K:=(C-K)\,\overline{(K-M)}\,e^{-i(\alpha+\varphi)}
=CK\cdot MK\cdot e^{i(\alpha+\varphi+\theta)}e^{-i\theta}e^{-i(\alpha+\varphi)}=CK\cdot MK>0 .
$$
In particular
$$
\operatorname{Im}T_K=0. \tag{1.6}
$$
Similarly, combining (1.3) with $\angle ABL=\varphi+\psi$ (so $\arg(B-L)=-(\varphi+\psi)$
mod $2\pi$) and (1.5):
$$
T_L:=(B-L)\,\overline{(L-N)}\,e^{i(\alpha+\varphi)}
=BL\cdot NL\cdot e^{-i(\varphi+\psi)}e^{-i(\alpha-\psi)}e^{i(\alpha+\varphi)}=BL\cdot NL>0,
$$
so
$$
\operatorname{Im}T_L=0. \tag{1.7}
$$

**(e) Expansion of (1.6).** With (1.1), $K-M=c\bigl(\tfrac12-\rho e^{-i\varphi}\bigr)$ and
$C-K=be^{i\alpha}-c+c\rho e^{-i\varphi}$, so
$$
\frac{T_K}{c}
=\Bigl[b e^{i\alpha}-c+c\rho e^{-i\varphi}\Bigr]
 \Bigl[\tfrac12-\rho e^{i\varphi}\Bigr]e^{-i(\alpha+\varphi)} .
$$
Expanding the product in brackets:
$$
\tfrac b2 e^{i\alpha}-b\rho e^{i(\alpha+\varphi)}-\tfrac c2+c\rho e^{i\varphi}
+\tfrac{c\rho}2 e^{-i\varphi}-c\rho^2,
$$
and multiplying by $e^{-i(\alpha+\varphi)}$:
$$
\frac{T_K}{c}
=\tfrac b2 e^{-i\varphi}-b\rho-\tfrac c2 e^{-i(\alpha+\varphi)}
+c\rho e^{-i\alpha}+\tfrac{c\rho}2 e^{-i(\alpha+2\varphi)}-c\rho^2 e^{-i(\alpha+\varphi)} .
$$
Taking imaginary parts,
$$
\frac{\operatorname{Im}T_K}{c}
=-\tfrac b2 t+\tfrac c2 s_1-c\rho s-\tfrac{c\rho}2 s_2+c\rho^2 s_1 .
$$
Setting this to $0$ and multiplying by $-2$ yields exactly $(E_1)$.

**(f) Expansion of (1.7).** With (1.1), $L-N=be^{i\alpha}\bigl(\tfrac12-\sigma e^{i\varphi}\bigr)$
and $B-L=c-be^{i\alpha}+b\sigma e^{i(\alpha+\varphi)}$, so
$$
\frac{T_L}{b}
=\Bigl[c-be^{i\alpha}+b\sigma e^{i(\alpha+\varphi)}\Bigr]
 \Bigl[\tfrac12-\sigma e^{-i\varphi}\Bigr]e^{i\varphi} .
$$
Expanding the bracket product:
$$
\tfrac c2-c\sigma e^{-i\varphi}-\tfrac b2 e^{i\alpha}+b\sigma e^{i(\alpha-\varphi)}
+\tfrac{b\sigma}2 e^{i(\alpha+\varphi)}-b\sigma^2 e^{i\alpha},
$$
and multiplying by $e^{i\varphi}$:
$$
\frac{T_L}{b}
=\tfrac c2 e^{i\varphi}-c\sigma-\tfrac b2 e^{i(\alpha+\varphi)}
+b\sigma e^{i\alpha}+\tfrac{b\sigma}2 e^{i(\alpha+2\varphi)}-b\sigma^2 e^{i(\alpha+\varphi)} .
$$
Taking imaginary parts,
$$
\frac{\operatorname{Im}T_L}{b}
=\tfrac c2 t-\tfrac b2 s_1+b\sigma s+\tfrac{b\sigma}2 s_2-b\sigma^2 s_1 .
$$
Setting this to $0$ and multiplying by $2$ yields exactly $(E_2)$. $\blacksquare$

> **Remark (not needed below).** Conditions $(E_1)$, $(E_2)$ have a synthetic meaning: writing
> $K''$ for the reflection of $K$ in $M$ and $L''$ for the reflection of $L$ in $N$, the hypotheses
> are equivalent to: *$K''$ lies on the circle $(ACK)$, $L''$ lies on the circle $(ABL)$, and rays
> $AK''$, $AL''$ are reflections of each other in the internal bisector of $\angle BAC$.* We shall
> not use this.

---

## Step 2 — Analytic form of the conclusion

Since the problem speaks of the circumcentre $O$ of triangle $AKL$, the points $A,K,L$ are
not collinear; with $A=0$ this means
$$
d:=\operatorname{Im}\bigl(\overline K L\bigr)\neq 0 .
$$

**Lemma 2 (circumcentre formula).** The circumcentre of $\{0,K,L\}$ is
$$
O=\frac{|K|^2L-|L|^2K}{\overline K L-K\overline L}
=\frac{|K|^2L-|L|^2K}{2i\,d}.
\tag{2.1}
$$

*Proof.* The denominator is $2i\,d\neq0$. We check $|O-K|^2=|O|^2$ and $|O-L|^2=|O|^2$:
$$
|O-K|^2-|O|^2=|K|^2-2\operatorname{Re}\bigl(O\overline K\bigr),
\qquad
O\overline K=\frac{|K|^2\,\overline K L-|K|^2|L|^2}{2i\,d}
=-\,\frac{i}{2d}\Bigl(|K|^2\,\overline K L-|K|^2|L|^2\Bigr),
$$
so $\operatorname{Re}(O\overline K)=\frac1{2d}\operatorname{Im}\bigl(|K|^2\overline KL-|K|^2|L|^2\bigr)
=\frac{|K|^2 d}{2d}=\frac{|K|^2}2$, giving $|O-K|=|O|$. Likewise
$\operatorname{Re}(O\overline L)=\frac1{2d}\operatorname{Im}\bigl(|K|^2|L|^2-|L|^2K\overline L\bigr)
=\frac{|L|^2}2$ (using $\operatorname{Im}(K\overline L)=-d$), giving $|O-L|=|O|$. As
$|O-A|=|O|$ trivially, $O$ is equidistant from $A,K,L$, and such a point is unique because
$A,K,L$ are not collinear. $\blacksquare$

**Lemma 3.** With $P:=1-2\rho\hat c+\rho^2$ and $Q:=1-2\sigma\hat c+\sigma^2$,
$$
OM=ON
\iff
F:=c^2P\,(s-\sigma s_1)+bc\,t\,(\sigma P-\rho Q)+b^2Q\,(\rho s_1-s)
-\frac{c^2-b^2}{2}\Bigl(s-(\rho+\sigma)s_1+\rho\sigma s_2\Bigr)=0 .
\tag{2.2}
$$

*Proof.* First,
$$
OM^2-ON^2
=\Bigl(|O|^2-2\operatorname{Re}(O\overline M)+|M|^2\Bigr)
-\Bigl(|O|^2-2\operatorname{Re}(O\overline N)+|N|^2\Bigr)
=-2\operatorname{Re}\bigl[O(\overline M-\overline N)\bigr]+|M|^2-|N|^2 .
$$
Now $\overline M-\overline N=\overline{M-N}=\tfrac12\overline{(B-C)}$ and
$|M|^2-|N|^2=\tfrac{c^2-b^2}4$, so
$$
OM=ON\iff \operatorname{Re}\bigl[O\,\overline{(B-C)}\bigr]=\frac{c^2-b^2}{4}.
\tag{2.3}
$$
By (2.1), $O\,\overline{(B-C)}=\dfrac{G}{2i\,d}$ with
$G:=\bigl(|K|^2L-|L|^2K\bigr)\overline{(B-C)}$, hence
$\operatorname{Re}\bigl[O\overline{(B-C)}\bigr]=\dfrac{\operatorname{Im}G}{2d}$ and
$$
OM=ON\iff \operatorname{Im}G=\frac{c^2-b^2}{2}\,d .
\tag{2.4}
$$
It remains to expand both sides using (1.1). We have
$$
|K|^2=c^2\bigl(1-\rho e^{-i\varphi}\bigr)\bigl(1-\rho e^{i\varphi}\bigr)=c^2P,
\qquad
|L|^2=b^2Q,
$$
$$
\overline KL=c\bigl(1-\rho e^{i\varphi}\bigr)\cdot be^{i\alpha}\bigl(1-\sigma e^{i\varphi}\bigr)
=bc\,e^{i\alpha}\Bigl[1-(\rho+\sigma)e^{i\varphi}+\rho\sigma e^{2i\varphi}\Bigr],
$$
so
$$
d=\operatorname{Im}(\overline KL)=bc\Bigl[s-(\rho+\sigma)s_1+\rho\sigma s_2\Bigr].
\tag{2.5}
$$
Next, $\overline{(B-C)}=c-be^{-i\alpha}$ and
$$
G=bc\Bigl[cP\,e^{i\alpha}\bigl(1-\sigma e^{i\varphi}\bigr)-bQ\bigl(1-\rho e^{-i\varphi}\bigr)\Bigr]
\bigl(c-be^{-i\alpha}\bigr).
$$
Expanding into four terms and taking imaginary parts:
$$
\begin{aligned}
\operatorname{Im}\Bigl[c^2P\,e^{i\alpha}(1-\sigma e^{i\varphi})\Bigr]&=c^2P\,(s-\sigma s_1),\\
\operatorname{Im}\Bigl[-bcP\,(1-\sigma e^{i\varphi})\Bigr]&=bcP\,\sigma t,\\
\operatorname{Im}\Bigl[-bcQ\,(1-\rho e^{-i\varphi})\Bigr]&=-bcQ\,\rho t,\\
\operatorname{Im}\Bigl[b^2Q\,e^{-i\alpha}(1-\rho e^{-i\varphi})\Bigr]&=b^2Q\,(\rho s_1-s),
\end{aligned}
$$
so that
$$
\operatorname{Im}G=bc\Bigl[c^2P(s-\sigma s_1)+bct(\sigma P-\rho Q)+b^2Q(\rho s_1-s)\Bigr].
\tag{2.6}
$$
Substituting (2.5) and (2.6) into (2.4) and dividing by $bc>0$ gives exactly (2.2). $\blacksquare$

---

## Step 3 — The master identity

**Lemma 4.** As an identity of polynomials in $\rho,\sigma,b,c$ with coefficients depending on
$\alpha,\varphi$,
$$
\boxed{\;
2s_1\,F=\Bigl[(c\,s_1-b\,t)\,\sigma-c\,s\Bigr]E_1
+\Bigl[(c\,t-b\,s_1)\,\rho+b\,s\Bigr]E_2 .}
\tag{3.1}
$$

*Proof.* We need the two elementary identities
$$
\textbf{(A)}\quad s+s_2=2\hat c\,s_1,
\qquad\qquad
\textbf{(B)}\quad 4s\hat c\,s_1=s_1^2+s\,s_2+2s^2-t^2 .
$$

*(A)*: $2\cos\varphi\sin(\alpha+\varphi)=\sin(\alpha+2\varphi)+\sin\alpha$ (product-to-sum).

*(B)*: Using $2\sin\alpha\cos\varphi=\sin(\alpha+\varphi)+\sin(\alpha-\varphi)$ and
$2\sin(\alpha+\varphi)\sin(\alpha-\varphi)=\cos2\varphi-\cos2\alpha$,
$$
4s\hat c\,s_1=2s_1\bigl[s_1+\sin(\alpha-\varphi)\bigr]=2s_1^2+\cos2\varphi-\cos2\alpha .
$$
On the other hand, using $s\,s_2=\tfrac12[\cos2\varphi-\cos(2\alpha+2\varphi)]$,
$2s^2=1-\cos2\alpha$, $t^2=\tfrac12(1-\cos2\varphi)$, and
$\tfrac12-\tfrac12\cos(2\alpha+2\varphi)=s_1^2$:
$$
s_1^2+s\,s_2+2s^2-t^2
=s_1^2+\cos2\varphi-\cos2\alpha+\underbrace{\tfrac12-\tfrac12\cos(2\alpha+2\varphi)}_{=s_1^2}
=2s_1^2+\cos2\varphi-\cos2\alpha .
$$
Hence (B) holds.

Now expand $F$ from (2.2) as a polynomial in $\rho,\sigma$ (recall
$P=1-2\rho\hat c+\rho^2$, $Q=1-2\sigma\hat c+\sigma^2$). Collecting monomials:

$$
F=\frac{(c^2-b^2)s}{2}
+\rho\Bigl[-2c^2s\hat c-bct+b^2s_1+\tfrac{(c^2-b^2)s_1}{2}\Bigr]
+\sigma\Bigl[-c^2s_1+bct+2b^2s\hat c+\tfrac{(c^2-b^2)s_1}{2}\Bigr]
$$
$$
\qquad
+\rho^2\,c^2s
-\sigma^2\,b^2s
+\rho\sigma\,(c^2-b^2)\Bigl(2s_1\hat c-\tfrac{s_2}{2}\Bigr)
+\rho^2\sigma\,(bct-c^2s_1)
+\rho\sigma^2\,(b^2s_1-bct).
\tag{3.2}
$$

*(Details: $c^2P(s-\sigma s_1)$ contributes
$c^2s+c^2s\rho^2-2c^2s\hat c\rho-c^2s_1\sigma-c^2s_1\rho^2\sigma+2c^2s_1\hat c\rho\sigma$;
$bct\sigma P$ contributes $bct\sigma+bct\rho^2\sigma-2bct\hat c\rho\sigma$;
$-bct\rho Q$ contributes $-bct\rho-bct\rho\sigma^2+2bct\hat c\rho\sigma$;
$b^2Q(\rho s_1-s)$ contributes
$b^2s_1\rho+b^2s_1\rho\sigma^2-2b^2s_1\hat c\rho\sigma-b^2s-b^2s\sigma^2+2b^2s\hat c\sigma$;
and the subtracted term contributes
$-\tfrac{c^2-b^2}{2}(s-s_1\rho-s_1\sigma+s_2\rho\sigma)$. The $\pm2bct\hat c\rho\sigma$ terms
cancel; everything else is collected above.)*

Write the right-hand side of (3.1) as $\lambda'E_1+\mu'E_2$ with
$\lambda'=(cs_1-bt)\sigma-cs$ and $\mu'=(ct-bs_1)\rho+bs$, and expand using
$E_1=(bt-cs_1)+c(2s+s_2)\rho-2cs_1\rho^2$, $E_2=(ct-bs_1)+b(2s+s_2)\sigma-2bs_1\sigma^2$.
Comparing coefficients of each monomial with $2s_1\times$(3.2):

| monomial | coefficient in $\lambda'E_1+\mu'E_2$ | needs to equal $2s_1\times$ coefficient in (3.2) | check |
|---|---|---|---|
| $1$ | $-cs(bt-cs_1)+bs(ct-bs_1)=(c^2-b^2)s\,s_1$ | $(c^2-b^2)s\,s_1$ | ✓ |
| $\rho^2$ | $(-cs)(-2cs_1)=2c^2s\,s_1$ | $2s_1c^2s$ | ✓ |
| $\sigma^2$ | $(bs)(-2bs_1)=-2b^2s\,s_1$ | $-2s_1b^2s$ | ✓ |
| $\rho^2\sigma$ | $(cs_1-bt)(-2cs_1)$ | $2s_1(bct-c^2s_1)$ | ✓ (identical) |
| $\rho\sigma^2$ | $(ct-bs_1)(-2bs_1)$ | $2s_1(b^2s_1-bct)$ | ✓ (identical) |
| $\rho\sigma$ | $\bigl[(cs_1-bt)c+(ct-bs_1)b\bigr](2s+s_2)=(c^2-b^2)s_1(2s+s_2)$ | $2s_1(c^2-b^2)(2s_1\hat c-\tfrac{s_2}2)$ | reduces to **(A)** |
| $\rho$ | $-c^2s(2s+s_2)+(ct-bs_1)^2$ | $2s_1\bigl[-2c^2s\hat c-bct+b^2s_1\bigr]+(c^2-b^2)s_1^2$ | reduces to **(B)** |
| $\sigma$ | $-(cs_1-bt)^2+b^2s(2s+s_2)$ | $2s_1\bigl[-c^2s_1+bct+2b^2s\hat c\bigr]+(c^2-b^2)s_1^2$ | reduces to **(B)** |

The three nontrivial rows:

* **Row $\rho\sigma$.** Required: $(2s+s_2)=2\bigl(2s_1\hat c-\tfrac{s_2}2\bigr)$, i.e.
  $s+s_2=2\hat c s_1$, which is (A).
* **Row $\rho$.** Expanding both sides:
  LHS $=-2c^2s^2-c^2ss_2+c^2t^2-2bct\,s_1+b^2s_1^2$;
  RHS $=-4c^2s\hat cs_1-2bct\,s_1+2b^2s_1^2+(c^2-b^2)s_1^2
       =-4c^2s\hat cs_1-2bct\,s_1+b^2s_1^2+c^2s_1^2$.
  Cancelling $-2bct\,s_1+b^2s_1^2$ from both sides and dividing by $c^2$, the requirement becomes
  $-2s^2-ss_2+t^2=-4s\hat cs_1+s_1^2$, i.e. exactly (B).
* **Row $\sigma$.** Expanding both sides:
  LHS $=-c^2s_1^2+2bct\,s_1-b^2t^2+2b^2s^2+b^2ss_2$;
  RHS $=-2c^2s_1^2+2bct\,s_1+4b^2s\hat cs_1+(c^2-b^2)s_1^2
       =-c^2s_1^2-b^2s_1^2+2bct\,s_1+4b^2s\hat cs_1$.
  Cancelling $-c^2s_1^2+2bct\,s_1$ and dividing by $b^2$, the requirement becomes
  $-t^2+2s^2+ss_2=-s_1^2+4s\hat cs_1$, again exactly (B).

All eight coefficients match, proving (3.1). $\blacksquare$

---

## Step 4 — Conclusion

By Lemma 1, the hypotheses of the problem imply $E_1=0$ and $E_2=0$.
By Lemma 0(4), $s_1=\sin(\alpha+\varphi)>0$. Hence Lemma 4 gives
$$
2s_1F=\lambda'\cdot 0+\mu'\cdot 0=0
\quad\Longrightarrow\quad F=0 .
$$
By Lemma 3, $F=0$ is equivalent to $OM=ON$.

$$
\boxed{OM=ON}
$$
$\blacksquare$

---

## Remarks

1. **Where each hypothesis is used.** The equalities $\angle KBA=\angle ACL$ enter through the
   *shared* parameter $\varphi$ in the two parametrizations (1.1); $\angle LCK=\angle BMK$
   produces $E_1$; $\angle LBK=\angle LNC$ produces $E_2$. The positional conditions
   ($K\in\operatorname{int}\triangle BMC$, $L\in\operatorname{int}\triangle BNC$, $K$ inside
   $\angle LBA$, $L$ inside $\angle ACK$) are used only to pin down the sign conventions
   (Lemma 0 and the angle-additivity step); in fact only the *vanishing of imaginary parts* in
   (1.6)–(1.7) is needed, not the positivity of $T_K,T_L$.

2. **Geometric interpretation of the conclusion.** $OM=ON$ says that $O$ lies on the
   perpendicular bisector of the midline $MN\parallel BC$. Equivalently (see (2.3)–(2.4)), the
   circle $(AKL)$ satisfies
   $\operatorname{pow}(B)-\operatorname{pow}(C)=\tfrac12\,(AB^2-AC^2)$ — exactly half the
   corresponding difference for the circumcircle of $ABC$.

3. **Degrees of freedom.** For a fixed triangle, $(E_1)$ determines $\rho$ from $\varphi$ (a
   quadratic) and $(E_2)$ determines $\sigma$ from $\varphi$, so the admissible pairs $(K,L)$
   form (branches of) a one-parameter family parametrized by $\varphi$; the identity (3.1) shows
   $OM=ON$ holds on every branch, irrespective of which roots the configuration selects.
