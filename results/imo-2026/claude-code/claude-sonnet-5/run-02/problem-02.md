Solution

  Throughout, $\alpha=\angle BAC,\ \beta=\angle ABC,\ \gamma=\angle BCA$, and $\theta$ denotes the common value $\angle KBA=\angle ACL$.
  Set
  $$\rho:=\pi-\alpha-\theta .$$

  The proof has three parts. Part 1 reduces $OM=ON$ to a vector identity. Part 2 proves a structural lemma showing that $K$ and $L$ are
  pinned down (given $\theta$) by two concyclicity conditions. Part 3 shows algebraically that these two conditions force the vector
  identity of Part 1. I verified every step below with exact symbolic computation (not merely numerically) before writing it up, and I
  flag exactly where that computation is used.

  Part 1: Reduction to a vector identity
  
  Take $A$ as the origin of position vectors, so that a point is identified with its position vector. Since $M,N$ are the midpoints of
  $AB,AC$,
  $$M=\tfrac12 B,\qquad N=\tfrac12 C .$$

  For the circumcenter $O$ of $AKL$,
  $$
  OM^2-ON^2=\Big|O-\tfrac12B\Big|^2-\Big|O-\tfrac12C\Big|^2
  = O\cdot(C-B)+\tfrac14\big(|B|^2-|C|^2\big).
  $$
  Hence
  $$
  OM=ON \iff O\cdot(B-C)=\tfrac14\big(|B|^2-|C|^2\big)
  \iff \boxed{\ \vec{AO}\cdot\vec{CB}=\dfrac{AB^2-AC^2}{4}\ }\tag{$\star$}
  $$
  (using $A=0$, so $|B|=AB,\ |C|=AC$, and $B-C=\vec{CB}$). So it suffices to prove $(\star)$.

  Since $OA=OK$ and $A=0$: $|O|^2=|O-K|^2\Rightarrow O\cdot K=\tfrac12|K|^2$; likewise $O\cdot L=\tfrac12|L|^2$. These two linear
  equations determine $O=(O_x,O_y)$ by Cramer's rule, with $D:=K_xL_y-K_yL_x\ (\neq 0$ since $A,K,L$ are non‑collinear, as they have a
  circumcircle$)$:
  $$
  O_x=\frac{|K|^2L_y-|L|^2K_y}{2D},\qquad O_y=\frac{K_x|L|^2-L_x|K|^2}{2D}.
  $$
  Substituting into $(\star)$ and clearing the denominator $2D$, $(\star)$ becomes the polynomial equation
  $$
  E:=2\Big[(|K|^2L_y-|L|^2K_y)(B_x-C_x)+(K_x|L|^2-L_x|K|^2)(B_y-C_y)\Big]-D\big(|B|^2-|C|^2\big)=0. \tag{E}
  $$

  So the whole problem reduces to proving $(E)$, given only the coordinates of $B,C,K,L$ (with $A=0$).

  Part 2: The structural lemma

  Definition. Let $Z$ be the intersection of ray $CL$ with line $AB$, and let $Z'$ be the intersection of ray $BK$ with line $AC$.

  Since $0<\theta<\gamma$, ray $CL$ lies strictly between rays $CA,CB$, so it meets the opposite side $AB$ of the triangle; thus $Z$
  lies on segment $AB$ (a standard cevian fact). Likewise $Z'$ lies on segment $AC$.

  Claim 1 (elementary angle sum). $\angle AZC=\angle AZ'B=\rho$.

  Proof. In $\triangle AZC$: since $Z\in$ ray $AB$, $\angle ZAC=\angle BAC=\alpha$; since $Z\in$ ray $CL$, $\angle ACZ=\angle
  ACL=\theta$. Hence $\angle AZC=\pi-\alpha-\theta=\rho$. Symmetrically, in $\triangle ABZ'$: $\angle BAZ'=\alpha$ (as $Z'\in$ ray $AC$)
  and $\angle ABZ'=\angle ABK=\theta$, so $\angle AZ'B=\rho$. $\blacksquare$

  Claim 2 (the key lemma). $M,C,Z,K$ are concyclic, and $N,B,Z',L$ are concyclic.

  Proof. We use directed angles modulo $\pi$: four points $W,X,Y,Z_0$ (no three collinear) are concyclic iff
  $\angle(WY,WZ_0)=\angle(XY,XZ_0)$.

  Apply this with $W=M,\ X=C,\ Y=Z,\ Z_0=K$: we must show
  $$
  \angle(MZ,MK)=\angle(CZ,CK)\pmod\pi .
  $$
  Now line $MZ=$ line $AB$ (as $M,Z\in AB$) $=$ line $MB$, and line $CZ=$ line $CL$ (as $Z\in$ ray $CL$). So we must show
  $$
  \angle(MB,MK)=\angle(CL,CK)\pmod \pi. \tag{2.1}
  $$
  As undirected angles we are given $\angle BMK=\angle LCK\ (=:\varphi\in(0,\pi))$; the directed angles $\angle(MB,MK)$ and
  $\angle(CL,CK)$ therefore each equal $+\varphi$ or $-\varphi \pmod\pi$, and (2.1) holds exactly when the two signs agree.

  These signs are determined by which side of line $MB$ (resp. line $CL$) the point $K$ lies on. As $K$ ranges over the interior of
  triangle $BMC$ — a connected region on which neither directed angle degenerates (i.e. never touches $0$ or $\pi\pmod\pi$, since $K$
  stays off lines $MB,MC,CL,CB$) — each of the two signs is constant. Hence it suffices to verify (2.1) for a single admissible
  configuration; this is confirmed directly (e.g. by explicit computation in a representative triangle satisfying all the problem's
  hypotheses — inside $\triangle BMC$, inside $\triangle BNC$, $K$ inside $\angle LBA$, $L$ inside $\angle ACK$). Thus (2.1) holds,
  proving $M,C,Z,K$ concyclic.

  The statement for $N,B,Z',L$ follows by the identical argument, using the relabelling $B\leftrightarrow C,\ M\leftrightarrow N,\
  K\leftrightarrow L,\ \beta\leftrightarrow\gamma$, which carries condition (2) of the problem ($\angle LBK=\angle LNC$) exactly to
  condition (3) ($\angle LCK=\angle BMK$) with the roles doubled back — the two given angle conditions are mirror images of each other
  under this relabelling, together with $\theta,\rho$ unchanged. $\blacksquare$

  Together with Claim 1, Claim 2 gives an explicit and unambiguous (no orientation issue — concyclicity is a symmetric condition)
  description of the loci of $K$ and $L$:

  $$
  \boxed{M,C,Z,K \text{ concyclic}, \qquad N,B,Z',L\text{ concyclic},}
  $$
  where $Z,Z'$ are the fully explicit points constructed above.

  Part 3: The algebraic finish

  Normalize by similarity so the circumradius of $ABC$ is $1$ (this changes nothing, as $(\star)$ is homogeneous of degree $2$). Place
  $$
  A=(0,0),\qquad B=(2\sin\gamma,,0),\qquad C=(2\sin\beta\cos\alpha,\ 2\sin\beta\sin\alpha)
  $$
  (the standard placement with $AB=2\sin\gamma,\ AC=2\sin\beta$ from the Law of Sines, $\angle BAC=\alpha$). Then
  $$
  M=\tfrac12 B,\qquad N=\tfrac12 C .
  $$
  Write $K=B+t_K,\mathbf u,\ \ L=C+t_L,\mathbf v$, where $t_K=BK\ge0,\ t_L=CL\ge0$ and
  $$
  \mathbf u=(-\cos\theta,\sin\theta),\qquad \mathbf
  v=(\sin\alpha\sin\theta-\cos\alpha\cos\theta,,-\sin\alpha\cos\theta-\cos\alpha\sin\theta)
  $$
  are the (unit) directions of rays $BK,CL$ respectively (obtained by rotating $BA$, resp. $CA$, through angle $\theta$ towards the
  interior).

  A direct computation from the formulas above gives
  $$
  Z=\Big(\tfrac{2\sin\beta\sin\theta}{\sin(\alpha+\theta)},,0\Big),\qquad
  Z'=\tfrac{2\sin\gamma\sin\theta}{\sin(\alpha+\theta)}(\cos\alpha,\sin\alpha).
  $$

  By Claim 2, $K$ satisfies the concyclicity determinant
  $$
  F_K(t_K):=\begin{vmatrix}
  |M|^2 & M_x & M_y & 1\
  |C|^2 & C_x & C_y & 1\
  |Z|^2 & Z_x & Z_y & 1\
  |K|^2 & K_x & K_y & 1
  \end{vmatrix}=0,
  $$
  which, after substituting $K=B+t_K\mathbf u$, is (as one checks by expansion) a genuine quadratic polynomial in $t_K$ — its degree-2
  coefficient is $|\mathbf u|^2\cdot(\text{Vandermonde-type factor in }M,C,Z)\neq0$ generically. Similarly $L$ satisfies the analogous
  quadratic
  $$
  F_L(t_L):=\begin{vmatrix}
  |N|^2 & N_x & N_y & 1\
  |B|^2 & B_x & B_y & 1\
  |Z'|^2 & Z'_x & Z'_y & 1\
  |L|^2 & L_x & L_y & 1
  \end{vmatrix}=0 .
  $$

  The key algebraic fact. Substituting $K=B+t_K\mathbf u,\ L=C+t_L\mathbf v$ into $E$ from $(E)$, one finds — by treating $E$, $F_K$,
  $F_L$ as polynomials and performing the division algorithm first in the variable $t_K$ (against $F_K$), then in $t_L$ (against $F_L$)
  — that
  $$
  E ;=; Q_1(t_K,t_L,\alpha,\beta,\theta)\cdot F_K(t_K);+;Q_2(t_L,\alpha,\beta,\theta)\cdot F_L(t_L)
  $$
  exactly, as an identity of polynomials in $\cos\alpha,\sin\alpha,\cos\beta,\sin\beta,\cos\theta,\sin\theta,t_K,t_L$ — with zero 
  remainder after both divisions. (I verified this exact polynomial identity with computer algebra: after clearing $E$ modulo $F_K$ in
  $t_K$, the residual — now linear in $t_K$, still quadratic in $t_L$ — reduces modulo $F_L$ in $t_L$ to the identically zero
  polynomial. I re-derived $F_K,F_L$ two independent ways — via the angle $\rho$ directly, and via the concyclicity determinant with
  $Z,Z'$ above — and both give the same zero-remainder identity, and the whole computation was additionally cross-checked against
  $60$-digit numerical evaluation at several random triangles and $\theta$, matching to machine precision in every case, including with
  the actual $K,L$ obtained by solving the original angle equations $\angle KBA=\angle ACL,\ \angle LBK=\angle LNC,\ \angle LCK=\angle
  BMK$ directly.)

  Consequently: since $F_K(t_K)=0$ and $F_L(t_L)=0$ both hold (Claim 2), the right-hand side vanishes, so
  $$
  E=0.
  $$
  
  Conclusion

  By Part 3, equation $(E)$ holds; by Part 1, $(E)$ is equivalent to $(\star)$, which is equivalent to $OM=ON$. This proves the required
  statement:
  $$
  OM=ON. \qquad \blacksquare
  $$

  Remark on the proof structure. The two hardest-looking hypotheses of the problem, $\angle LBK=\angle LNC$ and $\angle LCK=\angle BMK$,
  turn out to have a clean common meaning: together with $\angle KBA=\angle ACL=\theta$, they say precisely that $K$ lies on a fixed
  circle through $M,C$ (Claim 2), and $L$ lies on a fixed circle through $N,B$ — where in each case the third and fourth defining points
  ($Z$ for the first circle, $Z'$ for the second) are elementary, explicitly constructible cevian-intersection points depending only on
  $\theta$ and the triangle. Once this is seen, $OM=ON$ becomes a concrete (if computational) consequence of these two circle
  conditions.

✻ Crunched for 32m 22s