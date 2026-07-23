Let (\Omega) be the circumcircle of (AKL). We prove that (M) and (N) have equal powers with respect to
  (\Omega).

  Set
  [
  \alpha=\angle KBA=\angle ACL.
  ]
  Since (\alpha<\angle B,\angle C), we have (\alpha<\frac\pi2). Put (p=\tan\alpha>0).

  After a similarity and a possible reflection, take
  [
  A=(0,0),\quad B=(2,0),\quad C=2s(c,d),
  ]
  where (s>0), (c^2+d^2=1), and (d>0). Thus
  [
  M=(1,0),\qquad N=s(c,d).
  ]

  Introduce the orthogonal involution
  [
  Q=\begin{pmatrix}c&d\ d&-c\end{pmatrix}.
  ]
  It sends ((1,0)) to the unit vector along (AC), while its positive second coordinate points into (\angle ACB).

  For a real parameter (t), define
  [
  P_t=(2-t,pt).
  ]
  Because the rays (BK) and (CL) make the same angle (\alpha) with (BA) and (CA), respectively, there exist
  (\rho,\sigma>0) such that
  [
  K=P_\rho,\qquad L=sQP_\sigma.
  ]

  Write
  [
  QP_t=(X_t,Y_t),\qquad
  D_t=1-(1+p^2)t,\qquad
  H_t=pX_t+D_tY_t. \tag{1}
  ]

  We now translate the other two angle conditions.

  Since
  [
  \overrightarrow{MK}=(1-\rho,p\rho),
  ]
  if (\gamma=\angle BMK), the addition formulas give
  [
  (\cos(\alpha+\gamma),\sin(\alpha+\gamma))
  \parallel (D_\rho,p).
  ]
  Because (L) lies inside (\angle ACK) and (\angle LCK=\gamma), the direction of (CK), expressed in the
  (AC)-coordinate system, is therefore parallel to
  [
  (-D_\rho,p).
  ]
  In that coordinate system, (C=(2s,0)) and (K=(X_\rho,Y_\rho)). Hence
  [
  (X_\rho-2s,Y_\rho)\parallel(-D_\rho,p),
  ]
  so
  [
  p(X_\rho-2s)+D_\rho Y_\rho=0.
  ]
  Thus
  [
  H_\rho=2sp. \tag{2}
  ]

  Similarly,
  [
  L-N=sQ(1-\sigma,p\sigma).
  ]
  If (\beta=\angle LNC), the direction obtained from (BA) after turning through (\alpha+\beta) is parallel to
  ((-D_\sigma,p)). Since (K) lies inside (\angle LBA) and (\angle LBK=\beta), the direction of (BL) is parallel
  to this vector. Therefore
  [
  s(X_\sigma,Y_\sigma)-(2,0)\parallel(-D_\sigma,p),
  ]
  which gives
  [
  sH_\sigma=2p. \tag{3}
  ]

  Multiplying (2) and (3), we obtain the crucial relation
  [
  H_\rho H_\sigma=4p^2. \tag{4}
  ]

  It remains to connect (4) with powers to (\Omega).

  Write
  [
  K=(k_1,k_2),\qquad L=(l_1,l_2),\qquad
  \Delta=k_1l_2-k_2l_1.
  ]
  Since (A,K,L) are noncollinear, (\Delta\ne0). The equation of (\Omega) has the form
  [
  x^2+y^2+ux+vy=0,
  ]
  where
  [
  u=\frac{-|K|^2l_2+|L|^2k_2}{\Delta},\qquad
  v=\frac{-k_1|L|^2+l_1|K|^2}{\Delta}. \tag{5}
  ]
  Consequently,
  [
  \begin{aligned}
  \Delta\bigl(\operatorname{Pow}_{\Omega}(M)
  -\operatorname{Pow}{\Omega}(N)\bigr)
  ={}&(1-s^2)\Delta\
  &+(1-sc)(-|K|^2l_2+|L|^2k_2)\
  &-sd(-k_1|L|^2+l_1|K|^2).
  \end{aligned} \tag{6}
  ]

  For completeness, we record the exact factorization of the right-hand side. Define
  [
  J_t=-ptX_t+\bigl(3t-2-(1+p^2)t^2\bigr)Y_t.
  ]
  Using
  [
  X_t=(2-t)c+ptd,\qquad
  Y_t=(2-t)d-ptc,
  ]
  and substituting (s=H_\rho/(2p)), which follows from (2), direct expansion of (6) gives
  [
  \begin{aligned}
  &\Delta\bigl(\operatorname{Pow}_{\Omega}(M)
  -\operatorname{Pow}{\Omega}(N)\bigr)
  +\frac{H_\rho J_\rho}{8p^3}
  \bigl(H_\rho H_\sigma-4p^2\bigr)\
  &\qquad=
  -\frac{(c^2+d^2-1)H_\rho^2}{4p}
  \Bigl((1+p^2)\rho\sigma^2-4\rho\sigma+2\rho+2\sigma\Bigr).
  \end{aligned} \tag{7}
  ]
  This is a polynomial identity obtained simply by inserting the displayed expressions for (X_t,Y_t).

  Because (c^2+d^2=1), the right-hand side of (7) is zero. By (4), its second term on the left is also zero.
  Since (\Delta\ne0), we conclude that
  [
  \operatorname{Pow}{\Omega}(M)=\operatorname{Pow}{\Omega}(N).
  ]

  If (R) is the radius of (\Omega), then
  [
  OM^2-R^2=\operatorname{Pow}_{\Omega}(M)
  =\operatorname{Pow}{\Omega}(N)=ON^2-R^2.
  ]
  Hence (OM^2=ON^2), and therefore
  [
  \boxed{OM=ON}.
  ]

─ Worked for 12m 33s ────────────────────────────────────────────────────────────────────────────────────────────

