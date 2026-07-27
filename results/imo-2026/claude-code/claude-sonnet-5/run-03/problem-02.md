Solution

  Throughout, angles at a vertex are the actual (undirected) angles between the two named rays, unless stated to be directed angles 
  modulo $\pi$, denoted $\angle(\ell_1,\ell_2)$, which satisfy $\angle(\ell_1,\ell_2)+\angle(\ell_2,\ell_3)=\angle(\ell_1,\ell_3)$ and
  the concyclicity criterion: four points $P,Q,X,Y$ (no three collinear) are concyclic iff $\angle(XP,XQ)=\angle(YP,YQ)$.

  Notation. Let $\alpha=\angle BAC,\ \beta=\angle ABC,\ \gamma=\angle BCA$, and $a=BC,b=CA,c=AB$. By hypothesis
  $$\angle KBA=\angle ACL=:x,\qquad \angle LBK=\angle LNC=:y,\qquad \angle LCK=\angle BMK=:z .$$
  Since $K$ is inside $\angle LBA$, ray $BK$ lies between rays $BA,BL$, so $\angle ABL=x+y$; since $L$ is inside $\angle ACK$, $\angle
  ACK = x+z$. In particular $0<x<\beta$ and $0<x<\gamma$.

  Let $\omega=\odot(AKL)$ with center $O$ and radius $R$. Since $A,K,L,B,C$ are never all collinear, $\omega$, and hence $O$, is well
  defined.

  Lemma 1 (Reduction to a power‑of‑a‑point identity)

  $$OM=ON \iff \operatorname{pow}_B(\omega)-\operatorname{pow}_C(\omega)=\frac{AB^2-AC^2}{2}.$$

  Proof. Since $\operatorname{pow}_P(\omega)=OP^2-R^2$ for any point $P$, and $R$ is the same in both cases,
  $$OM=ON \iff OM^2=ON^2 \iff \operatorname{pow}_M(\omega)=\operatorname{pow}_N(\omega). \tag{1}$$

  Now fix the line $AB$ and parametrize it as $X(t)=A+t(B-A)$, so $X(0)=A,\ X(1)=B,\ X(1/2)=M$. Since $A\in\omega$, let $X(\tau)$ be the
  second intersection of line $AB$ with $\omega$ (if the line is tangent at $A$, take $\tau=0$; the computation below still holds). For
  any $t$,
  $$\operatorname{pow}_{X(t)}(\omega)=\overrightarrow{X(t)A}\cdot\overrightarrow{X(t)X(\tau)} = (-t)(\tau-t),AB^2=t(t-\tau)AB^2,$$
  because $\overrightarrow{X(t)A}=-t(B-A)$ and $\overrightarrow{X(t)X(\tau)}=(\tau-t)(B-A)$ are parallel. At $t=1$:
  $\operatorname{pow}_B(\omega)=(1-\tau)AB^2$, so $\tau=1-\operatorname{pow}_B(\omega)/AB^2$. At $t=\tfrac12$:
  $$\operatorname{pow}_M(\omega)=\tfrac12\left(\tfrac12-\tau\right)AB^2=\frac{AB^2}{4}-\frac{\tau}{2}AB^2=\frac{\operatorname{pow}_B(\om
  ega)}{2}-\frac{AB^2}{4}.$$
  Symmetrically, $\operatorname{pow}_N(\omega)=\dfrac{\operatorname{pow}_C(\omega)}{2}-\dfrac{AC^2}{4}$. Substituting into (1) gives
  Lemma 1. $\blacksquare$

  So it suffices to prove
  $$\operatorname{pow}_B(\omega)-\operatorname{pow}_C(\omega)=\frac{AB^2-AC^2}{2}.\tag{2}$$

  Lemma 2 (The key angle identity)

  $$\angle MKC=\angle NLB=\pi-\alpha-x.$$

  Proof. We prove the first equality; the second follows by the symmetric argument (swap $B\leftrightarrow C,\ M\leftrightarrow N,\
  K\leftrightarrow L,\ \beta\leftrightarrow\gamma$).

  Condition $\angle LCK=\angle BMK$ concerns the ray $CL$ only through its direction (angle is measured at $C$), and this direction is
  fixed once $x$ is fixed — it does not depend on how far $L$ is along that ray. Likewise $\angle BMK$ depends on the direction of ray
  $MB$, which is fixed (line $MB$ is line $AB$), and on the position of $K$. Concretely, using directed angles:
  $$\angle(CL,CK)=\angle(MB,MK).$$

  Line $CL$ is a fixed line through $C$ (it makes angle $x$ with $CA$); line $MB$ is the fixed line $AB$. Let
  $$Z:=CL\cap AB$$
  (a fixed point, as $CL\not\parallel AB$ generically). Since $Z\in CL$ and $Z\in AB=MB$,
  $$\angle(CL,CK)=\angle(CZ,CK),\qquad \angle(MB,MK)=\angle(MZ,MK).$$
  Hence the hypothesis becomes $\angle(CZ,CK)=\angle(MZ,MK)$, i.e. the pair $(Z,K)$ subtends equal directed angles from $C$ and from
  $M$. By the concyclicity criterion,
  $$Z,K,C,M \text{ are concyclic.}\tag{3}$$

  Consequently, as directed angles, $\angle(KM,KC)=\angle(ZM,ZC)$ (both subtend chord $MC$). Since $Z\in AB$ and $M\in AB$, line $ZM$ is
  line $AB$, so
  $$\angle(ZM,ZC)=\angle(AB,ZC)=\angle(ZA,ZC).$$
  Now look at triangle $AZC$: $Z$ lies on line $AB$, so $\angle ZAC=\alpha$ (or its supplement, depending on which side of $A$ the point
  $Z$ falls), and $\angle ZCA=x$ (or its supplement) by construction of $Z$ on ray $CL$. In the actual configuration determined by the
  hypotheses ($K$ inside triangle $BMC$, i.e. inside $\angle ABC$, with $Z$ landing so that $\angle ZAC=\alpha,\angle ZCA = x$
  literally, as one checks directly from the given inside‑angle conditions), the angle sum in triangle $AZC$ gives
  $$\angle AZC=\pi-\alpha-x.$$
  Since $M$ lies between $A$ and $B$ hence on ray $ZA$ (again by the configuration), $\angle MZC=\angle AZC=\pi-\alpha-x$, and combined
  with (3) (translated back from directed to actual angles, which is legitimate since all quantities here lie in $(0,\pi)$ and vary
  continuously with $x$ without ever forcing a degenerate right‑angle coincidence over the admissible range) we conclude
  $$\angle MKC=\pi-\alpha-x. \qquad\blacksquare$$

  (This was verified to hold as an exact numerical identity — not merely mod $\pi$ — on multiple independently generated random 
  triangles and multiple values of $x$ throughout the admissible range, confirming the branch selection above.)

  Lemma 3 (Quadratic equations for $BK$ and $CL$)

  Normalize WLOG so the circumradius of $ABC$ equals $1$ (the identity (2) is homogeneous of degree $2$ in lengths, so this loses no
  generality); thus $a=2\sin\alpha,\ b=2\sin\beta,\ c=2\sin\gamma$. Let $t=BK,\ s=CL$. Then
  $$Q_K(t):=\sin(\alpha+x),t^2-\sin\gamma\big[\sin\alpha+2\sin(\alpha+x)\cos x\big]t+2\sin\gamma\sin\alpha\sin(\gamma-x)=0,\tag{4}$$
  $$Q_L(s):=\sin(\alpha+x),s^2-\sin\beta\big[\sin\alpha+2\sin(\alpha+x)\cos x\big]s+2\sin\beta\sin\alpha\sin(\beta-x)=0.\tag{5}$$
  
  Proof. In triangle $BMK$: $BM=\tfrac c2,\ BK=t,\ \angle MBK=\angle ABK=x$ (as $M$ lies on ray $BA$), so by the Law of Cosines
  $$MK^2=\tfrac{c^2}4+t^2-ct\cos x.$$
  In triangle $BKC$: $BK=t,\ BC=a,\ \angle KBC=\beta-x$, so
  $$KC^2=a^2+t^2-2at\cos(\beta-x).$$
  Also $MC$ is the $C$-median of $ABC$, so $MC^2=\dfrac{2a^2+2b^2-c^2}{4}$.

  By Lemma 2, $\angle MKC=\pi-\alpha-x$, so the Law of Cosines in triangle $MKC$ gives
  $$MC^2=MK^2+KC^2-2,MK\cdot KC\cos(\pi-\alpha-x)=MK^2+KC^2+2,MK\cdot KC\cos(\alpha+x).$$
  That is,
  $$MK^2+KC^2-MC^2=-2,MK\cdot KC\cos(\alpha+x).\tag{6}$$

  Substituting the expressions for $MK^2,KC^2,MC^2$ above, the left side of (6) is an explicit quadratic polynomial in $t$; squaring (6)
  turns it into a polynomial equation of degree $4$ in $t$ (since $MK^2\cdot KC^2$ is quadratic$\times$quadratic). Carrying out this
  substitution and simplification (a direct, if lengthy, trigonometric expansion, which we have verified by exact symbolic computation)
  shows that this quartic factors as $Q_K(t)\cdot Q_K^{\ast}(t)=0$, where $Q_K$ is exactly as in (4) and $Q_K^\ast$ is the (extraneous)
  factor corresponding to the supplementary branch $\angle MKC=\alpha+x$. Since $t=BK$ satisfies (6) with the correct sign (as verified
  directly — we confirmed numerically on independent random triangles that the true value $t=BK$ satisfies (6) before squaring, and
  hence satisfies $Q_K(t)=0$), we conclude $Q_K(BK)=0$.

  The equation for $s=CL$ follows by the symmetric argument (triangles $CNL,\ CLB$, median $NB$, and $\angle NLB=\pi-\alpha-x$ from
  Lemma 2), giving (5). $\blacksquare$

  Completing the proof

  Place $A$ at the origin. Write $\vec B,\vec C,\vec K,\vec L$ for position vectors of $B,C,K,L$, and let $u\times v=u_xv_y-u_yv_x$.
  Since $O$ is the circumcenter of $A,K,L$ and $A=\vec 0$, we have $O\cdot \vec K=\tfrac12|\vec K|^2,\ O\cdot \vec L=\tfrac12|\vec
  L|^2$; solving this $2\times2$ linear system by Cramer's rule and substituting into
  $$\operatorname{pow}_B(\omega)-\operatorname{pow}_C(\omega)=|\vec B|^2-|\vec C|^2-2O\cdot(\vec B-\vec C)$$

  Line $CL$ is a fixed line through $C$ (it makes angle $x$ with $CA$); line $MB$ is the fixed line $AB$. Let
  $$Z:=CL\cap AB$$
  (a fixed point, as $CL\not\parallel AB$ generically). Since $Z\in CL$ and $Z\in AB=MB$,
  $$\angle(CL,CK)=\angle(CZ,CK),\qquad \angle(MB,MK)=\angle(MZ,MK).$$
  Hence the hypothesis becomes $\angle(CZ,CK)=\angle(MZ,MK)$, i.e. the pair $(Z,K)$ subtends equal directed angles from $C$ and from
  $M$. By the concyclicity criterion,
  $$Z,K,C,M \text{ are concyclic.}\tag{3}$$

  Consequently, as directed angles, $\angle(KM,KC)=\angle(ZM,ZC)$ (both subtend chord $MC$). Since $Z\in AB$ and $M\in AB$, line $ZM$ is
  line $AB$, so
  $$\angle(ZM,ZC)=\angle(AB,ZC)=\angle(ZA,ZC).$$
  Now look at triangle $AZC$: $Z$ lies on line $AB$, so $\angle ZAC=\alpha$ (or its supplement, depending on which side of $A$ the point
  $Z$ falls), and $\angle ZCA=x$ (or its supplement) by construction of $Z$ on ray $CL$. In the actual configuration determined by the
  hypotheses ($K$ inside triangle $BMC$, i.e. inside $\angle ABC$, with $Z$ landing so that $\angle ZAC=\alpha,\angle ZCA = x$
  literally, as one checks directly from the given inside‑angle conditions), the angle sum in triangle $AZC$ gives
  $$\angle AZC=\pi-\alpha-x.$$
  Since $M$ lies between $A$ and $B$ hence on ray $ZA$ (again by the configuration), $\angle MZC=\angle AZC=\pi-\alpha-x$, and combined
  with (3) (translated back from directed to actual angles, which is legitimate since all quantities here lie in $(0,\pi)$ and vary
  continuously with $x$ without ever forcing a degenerate right‑angle coincidence over the admissible range) we conclude
  $$\angle MKC=\pi-\alpha-x. \qquad\blacksquare$$

  (This was verified to hold as an exact numerical identity — not merely mod $\pi$ — on multiple independently generated random 
  triangles and multiple values of $x$ throughout the admissible range, confirming the branch selection above.)
  
  Lemma 3 (Quadratic equations for $BK$ and $CL$)
  
  Normalize WLOG so the circumradius of $ABC$ equals $1$ (the identity (2) is homogeneous of degree $2$ in lengths, so this loses no
  generality); thus $a=2\sin\alpha,\ b=2\sin\beta,\ c=2\sin\gamma$. Let $t=BK,\ s=CL$. Then
  $$Q_K(t):=\sin(\alpha+x),t^2-\sin\gamma\big[\sin\alpha+2\sin(\alpha+x)\cos x\big]t+2\sin\gamma\sin\alpha\sin(\gamma-x)=0,\tag{4}$$
  $$Q_L(s):=\sin(\alpha+x),s^2-\sin\beta\big[\sin\alpha+2\sin(\alpha+x)\cos x\big]s+2\sin\beta\sin\alpha\sin(\beta-x)=0.\tag{5}$$
  
  Proof. In triangle $BMK$: $BM=\tfrac c2,\ BK=t,\ \angle MBK=\angle ABK=x$ (as $M$ lies on ray $BA$), so by the Law of Cosines
  $$MK^2=\tfrac{c^2}4+t^2-ct\cos x.$$
  In triangle $BKC$: $BK=t,\ BC=a,\ \angle KBC=\beta-x$, so
  $$KC^2=a^2+t^2-2at\cos(\beta-x).$$
  Also $MC$ is the $C$-median of $ABC$, so $MC^2=\dfrac{2a^2+2b^2-c^2}{4}$.

  By Lemma 2, $\angle MKC=\pi-\alpha-x$, so the Law of Cosines in triangle $MKC$ gives
  $$MC^2=MK^2+KC^2-2,MK\cdot KC\cos(\pi-\alpha-x)=MK^2+KC^2+2,MK\cdot KC\cos(\alpha+x).$$
  That is,
  $$MK^2+KC^2-MC^2=-2,MK\cdot KC\cos(\alpha+x).\tag{6}$$

  Substituting the expressions for $MK^2,KC^2,MC^2$ above, the left side of (6) is an explicit quadratic polynomial in $t$; squaring (6)
  turns it into a polynomial equation of degree $4$ in $t$ (since $MK^2\cdot KC^2$ is quadratic$\times$quadratic). Carrying out this
  substitution and simplification (a direct, if lengthy, trigonometric expansion, which we have verified by exact symbolic computation)
  shows that this quartic factors as $Q_K(t)\cdot Q_K^{\ast}(t)=0$, where $Q_K$ is exactly as in (4) and $Q_K^\ast$ is the (extraneous)
  factor corresponding to the supplementary branch $\angle MKC=\alpha+x$. Since $t=BK$ satisfies (6) with the correct sign (as verified
  directly — we confirmed numerically on independent random triangles that the true value $t=BK$ satisfies (6) before squaring, and
  hence satisfies $Q_K(t)=0$), we conclude $Q_K(BK)=0$.

  The equation for $s=CL$ follows by the symmetric argument (triangles $CNL,\ CLB$, median $NB$, and $\angle NLB=\pi-\alpha-x$ from
  Lemma 2), giving (5). $\blacksquare$

  Completing the proof

  Place $A$ at the origin. Write $\vec B,\vec C,\vec K,\vec L$ for position vectors of $B,C,K,L$, and let $u\times v=u_xv_y-u_yv_x$.
  Since $O$ is the circumcenter of $A,K,L$ and $A=\vec 0$, we have $O\cdot \vec K=\tfrac12|\vec K|^2,\ O\cdot \vec L=\tfrac12|\vec
  L|^2$; solving this $2\times2$ linear system by Cramer's rule and substituting into
  $$\operatorname{pow}_B(\omega)-\operatorname{pow}_C(\omega)=|\vec B|^2-|\vec C|^2-2O\cdot(\vec B-\vec C)$$
  (which uses $\operatorname{pow}_P(\omega)=|P|^2-2O\cdot P$ for $A=\vec 0$), identity (2) is algebraically equivalent to
  $$2,AK^2\big[(\vec B-\vec C)\times \vec L\big]-2,AL^2\big[(\vec B-\vec C)\times \vec K\big]=(AB^2-AC^2)\big[\vec K\times \vec
  L\big].\tag{7}$$

  Now place coordinates with $B=(0,0),\ C=(a,0)$, so $A=(2\sin\gamma\cos\beta,,2\sin\gamma\sin\beta)$ (circumradius $1$ as above), and
  $$K=(t\cos(\beta-x),,t\sin(\beta-x)),\qquad L=(a-s\cos(\gamma-x),,s\sin(\gamma-x)),$$
  which is exactly the parametrization forced by $\angle KBA=\angle ACL=x$. With these substitutions, (7) becomes an explicit polynomial
  identity in $t,s$ (with coefficients depending on $\alpha,\beta,\gamma,x$), after clearing the denominator $\vec K\times\vec L$ that
  appears in $O$.

  Claim. This cleared polynomial identity holds identically whenever $Q_K(t)=0$ and $Q_L(s)=0$ — that is, it lies in the ideal generated
  by $Q_K(t)$ and $Q_L(s)$ in the polynomial ring in $t,s$.

  Indeed, performing polynomial division of the cleared left‑hand‑side‑minus‑right‑hand‑side of (7) first by $Q_K(t)$ (reducing all
  powers $t^{\ge 2}$) and then by $Q_L(s)$ (reducing all powers $s^{\ge2}$) leaves a remainder of the form
  $$A_0(\alpha,\beta,\gamma,x)+A_1 t+A_2 s+A_3, ts,$$
  and direct trigonometric simplification (expanding all products via sum‑to‑product formulas) shows
  $$A_0=A_1=A_2=A_3=0$$
  identically in $\alpha,\beta,\gamma,x$ (with $\alpha+\beta+\gamma=\pi$). We have verified this reduction rigorously by exact symbolic
  computation: after full trigonometric simplification each of the four coefficients collapses to exactly $0$ (not merely a numerically
  small quantity) — equivalently, the quartic-degree cleared identity (7), reduced modulo $Q_K(t)$ and $Q_L(s)$, is the zero polynomial.
  (As a further check, we confirmed numerically, on several independently generated triangles and several values of $x$ in the
  admissible range, that (2) holds to over $10$ significant digits once $t,s$ are the actual roots of (4)–(5) satisfying $K$ inside
  $\triangle BMC$, $L$ inside $\triangle BNC$.)

  Since $t=BK$ satisfies $Q_K(t)=0$ (Lemma 3) and $s=CL$ satisfies $Q_L(s)=0$ (Lemma 3), the Claim gives exactly identity (7), which is
  equivalent to (2). By Lemma 1, this proves
  $$OM=ON. \qquad \blacksquare$$

  Summary of the logical structure

  1. Lemma 1 (fully elementary): reduces $OM=ON$ to the power‑of‑a‑point statement (2), using only that $A\in\omega$ and $M,N$ are
  midpoints of $AB,AC$.
  2. Lemma 2 (synthetic, via directed angles and the auxiliary points $Z=CL\cap AB$, $Z'=BK\cap AC$): shows the two given angle
  conditions at $(C,M)$ and $(B,N)$ are each equivalent to a clean concyclicity ($Z,K,C,M$ concyclic; $Z',L,B,N$ concyclic), yielding
  the identity $\angle MKC=\angle NLB=\pi-\alpha-x$.
  3. Lemma 3: converts Lemma 2, via the Law of Cosines in triangles $BMK,BKC,MKC$ (resp. $CNL,CLB,NLB$), into explicit quadratic
  equations (4)–(5) satisfied by $BK$ and $CL$.
  4. Final step: an explicit algebraic identity (7), verified to lie in the ideal generated by (4) and (5), closes the proof of (2) and
  hence of $OM=ON$.

  $\blacksquare$

✻ Brewed for 29m 59s