All verifications pass to machine precision, and the end-to-end chain is confirmed. I now have a complete, rigorous proof. Let me
  write it up.

  ---
  Solution

  Throughout, let $\omega$ denote the circumcircle of $\triangle AKL$, with centre $O$ and radius $R$, and set
  $$\varphi=\angle KBA=\angle LCA .$$

  Step 1 — Reduction to a metric relation

  Since $A\in\omega$ we have $OA=R$. As $M$ is the midpoint of $AB$, the median-length (Apollonius) relation in $\triangle OAB$ gives
  $$OM^2=\tfrac12 OA^2+\tfrac12 OB^2-\tfrac14 AB^2=\tfrac12 R^2+\tfrac12 OB^2-\tfrac14 AB^2 ,$$
  and likewise $ON^2=\tfrac12 R^2+\tfrac12 OC^2-\tfrac14 AC^2 .$ Subtracting,
  $$OM^2-ON^2=\tfrac12\bigl(OB^2-OC^2\bigr)-\tfrac14\bigl(AB^2-AC^2\bigr).$$
  Hence
  $$\boxed{OM=ON}\iff OB^2-OC^2=\tfrac12\bigl(AB^2-AC^2\bigr).\tag{$\star$}$$

  (Equivalently, $(\star)$ says the antipode $A^{}=2O-A$ of $A$ on $\omega$ satisfies $A^{}B=A^{}C$, i.e. $A^{}$ lies on the 
  perpendicular bisector of $BC$; we prove $(\star)$ directly.)

  Step 2 — Coordinates

  Place
  $$A=(0,0),\quad B=(1,0)\ (\text{so } AB=1),\quad C=(b\cos\alpha,\ b\sin\alpha),$$
  where $b=AC>0$ and $\alpha=\angle BAC\in(0,\pi)$. Then $M=(\tfrac12,0)$, $N=(\tfrac12 b\cos\alpha,\tfrac12 b\sin\alpha)$.

  The ray $BK$ makes angle $\varphi$ with $BA=(-1,0)$ on the interior side, i.e. it has direction $(-\cos\varphi,\sin\varphi)$; and $CL$
  makes angle $\varphi$ with $CA$. Thus for some $t,s>0$,
  $$K=(1-t\cos\varphi,\ t\sin\varphi),\qquad L=\bigl(b\cos\alpha-sb\cos(\alpha+\varphi),\ b\sin\alpha-sb\sin(\alpha+\varphi)\bigr).$$
  Since $\varphi<\angle ABC$ and $\alpha+\angle ABC<\pi$, we have $0<\alpha+\varphi<\pi$, so $\sin(\alpha+\varphi)>0$.

  Step 3 — The angle conditions as polynomial equations

  Because $L$ lies inside $\angle ACK$, $\ \angle KCA=\angle LCA+\angle LCK=\varphi+\angle LCK$; with the hypothesis $\angle LCK=\angle
  BMK$,
  $$\angle KCA=\varphi+\angle BMK.\tag{I}$$
  Because $K$ lies inside $\angle LBA$, $\ \angle LBA=\angle KBA+\angle LBK=\varphi+\angle LBK$; with $\angle LBK=\angle LNC$,
  $$\angle LBA=\varphi+\angle LNC.\tag{II}$$

  Using directed angles modulo $\pi$, for which $\tan\angle(u,v)=\dfrac{u\times v}{u\cdot v}$, compute from the coordinates (with
  $MB=(\tfrac12,0),\ MK=K-M,\ CK=K-C,\ CA=A-C$):
  $$CK\cdot CA=b\bigl(b-\cos\alpha+t\cos(\alpha+\varphi)\bigr),\qquad CK\times CA=b\bigl(t\sin(\alpha+\varphi)-\sin\alpha\bigr),$$
  $$\tan\angle BMK=\frac{t\sin\varphi}{\tfrac12-t\cos\varphi},\qquad \tan\angle
  KCA=\frac{t\sin(\alpha+\varphi)-\sin\alpha}{,b-\cos\alpha+t\cos(\alpha+\varphi),}.$$
  Substituting into $\tan\angle KCA=\tan(\varphi+\angle BMK)$ (tangent addition formula) and clearing denominators, condition (I)
  becomes
  $$P(t):=2\sin(\alpha+\varphi),t^2-\bigl(3\sin\alpha+2\sin\varphi\cos(\alpha+\varphi)\bigr)t+\bigl(\sin(\alpha+\varphi)-b\sin\varphi\bi
  gr)=0.\tag{K}$$
  The identical computation for (II) yields
  $$Q(s):=2\sin(\alpha+\varphi),s^2-\bigl(3\sin\alpha+2\sin\varphi\cos(\alpha+\varphi)\bigr)s+\Bigl(\sin(\alpha+\varphi)-\tfrac{\sin\var
  phi}{b}\Bigr)=0.\tag{L}$$

  Step 4 — Rewriting $(\star)$
  
  For $A=(0,0)$, $K=(k_x,k_y)$, $L=(l_x,l_y)$ the circumcentre is $O=(P_x/D,\ P_y/D)$ with
  $$D=2(k_xl_y-k_yl_x),\quad P_x=l_x^{,2}!+!l_y^{,2}\text{-terms:}\ \ P_x=l_y|K|^2-k_y|L|^2,\quad P_y=k_x|L|^2-l_x|K|^2,$$
  where $|K|^2=k_x^2+k_y^2,\ |L|^2=l_x^2+l_y^2$. Since $AB=1,\ AC=b$,
  $$OB^2-OC^2=|B|^2-|C|^2+2,O\cdot(C-B)=(1-b^2)+2,O\cdot(C-B),$$
  so $(\star)$ becomes $2,O\cdot(C-B)+\tfrac12(1-b^2)=0$. As $A,K,L$ are not collinear, $D\neq0$; multiplying by $2D$ turns $(\star)$
  into
  $$TT:=4\bigl[P_x(b\cos\alpha-1)+P_y,b\sin\alpha\bigr]+(1-b^2)D=0.\tag{$\star'$}$$

  Step 5 — The algebraic identity

  Writing $\cos(\alpha+\varphi)=\cos\alpha\cos\varphi-\sin\alpha\sin\varphi$,
  $\sin(\alpha+\varphi)=\sin\alpha\cos\varphi+\cos\alpha\sin\varphi$ and expanding, one verifies the polynomial identity
  $$
  \sin(\alpha+\varphi)\cdot TT=-2b\bigl(bs\sin\varphi-s\sin(\alpha+\varphi)+\sin\alpha\bigr),P(t);+;2b^2\bigl(b\sin\alpha+t\sin\varphi-b
  t\sin(\alpha+\varphi)\bigr),Q(s).\tag{$\ddagger$}
  $$

  At our configuration, $P(t)=0$ by (K) and $Q(s)=0$ by (L), so the right–hand side of $(\ddagger)$ vanishes. Since
  $\sin(\alpha+\varphi)\neq0$, we conclude $TT=0$. By $(\star')$ this is exactly $(\star)$, and by Step 1,
  $$OM=ON. \qquad \blacksquare$$

  ---
  Remarks on verification

  The two non‑trivial computations — the translation of conditions (I),(II) into equations (K),(L), and the master identity $(\ddagger)$
  — are routine polynomial/trigonometric expansions. I confirmed every link independently:

  - Configuration exists & statement holds: solving the exact system numerically for many triangles gives $OM-ON\approx 10^{-16}$.
  - Equations (K),(L): the geometric $t,s$ of the true configuration satisfy $P(t)=0,\ Q(s)=0$ (the smaller positive roots), matching
  the directly-constructed $K,L$.
  - Identity $(\ddagger)$: verified symbolically (CAS reduces $\sin(\alpha+\varphi),TT+2b(\cdots)P-2b^2(\cdots)Q$ to $0$) and
  numerically at 40 random non-solution points (residual $<10^{-13}$).

  The elegant content is Step 1: the whole problem collapses to showing the antipode of $A$ on $(AKL)$ is equidistant from $B$ and $C$;
  the remaining steps establish that single equidistance $(\star)$ by an explicit computation whose engine is the identity $(\ddagger)$.

✻ Crunched for 49m 11s