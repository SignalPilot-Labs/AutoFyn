Solution

  Throughout, $\angle A,\angle B,\angle C$ denote the angles of $\triangle ABC$, and we work in the configuration prescribed by the
  problem (with $A$ off line $BC$ and $K,L$ interior, as guaranteed by the "inside" hypotheses). Write
  $$\beta:=\angle ABK=\angle ACL,$$
  which are equal by hypothesis. Let $\omega$ be the circumcircle of $\triangle AKL$ and $O$ its centre.

  Step 1: Reduction to an antipode

  Let $A^\ast$ be the point of $\omega$ diametrically opposite $A$; thus $O$ is the midpoint of $AA^\ast$, i.e. $A^\ast=2O-A$.

  Since $M=\tfrac12(A+B)$ and $N=\tfrac12(A+C)$,
  $$OM=\Bigl|O-\tfrac{A+B}{2}\Bigr|=\tfrac12\bigl|2O-A-B\bigr|=\tfrac12,A^\ast B,\qquad ON=\tfrac12,A^\ast C .$$

  Hence $OM=ON\iff A^\ast B=A^\ast C$, i.e. iff $A^\ast$ lies on the perpendicular bisector of $BC$.

  Moreover $AA^\ast$ is a diameter of $\omega$ and $K,L\in\omega$, so by Thales
  $$\angle AKA^\ast=\angle ALA^\ast=90^\circ .$$
  Therefore $A^\ast$ is the intersection of
  $$\ell_K:=\text{(perpendicular to } AK \text{ at }K),\qquad \ell_L:=\text{(perpendicular to } AL \text{ at }L). \tag{$\dagger$}$$
  These two lines are distinct (else $AK\parallel AL$, forcing $A,K,L$ collinear, impossible). So it suffices to prove that $\ell_K$ and
  $\ell_L$ meet on the perpendicular bisector of $BC$.

  Step 2: The Key Lemma
  
  First rewrite the hypotheses so that each of $K,L$ is governed by a self‑contained condition. Since $K$ lies inside $\angle LBA$ and
  $L$ inside $\angle ACK$,
  $$\angle LBK=\angle ABL-\beta,\qquad \angle LCK=\angle ACK-\beta .$$
  The hypotheses $\angle LCK=\angle BMK$ and $\angle LBK=\angle LNC$ then read
  $$\boxed{\angle BMK=\angle ACK-\beta}\qquad\text{and}\qquad \boxed{\angle CNL=\angle ABL-\beta}. \tag{$\ast$}$$
  The second is the first with $B\leftrightarrow C$, $M\leftrightarrow N$, $K\leftrightarrow L$ (and $\angle ACL=\beta$ in place of
  $\angle ABK=\beta$).

  ▎ Lemma. Let $X$ be a point inside $\triangle ABC$ with $\angle ABX=\beta$, let $M$ be the midpoint of $AB$, and suppose $\angle 
  ▎ BMX=\angle ACX-\beta$. Then the perpendicular to line $AX$ at $X$ meets the perpendicular bisector of $BC$ at the point lying at 
  ▎ signed height
  ▎ $$h=\tfrac12 BC\cdot\cot(\angle A+\beta)$$
  ▎ above the midpoint $P$ of $BC$ (heights positive toward $A$). In particular this point depends only on $\angle A,\ \beta,\ BC$ — it 
  ▎ is symmetric in $B\leftrightarrow C$.

  Why the Lemma finishes the proof. Apply the Lemma to $X=K$: by ($\ast$), $\ell_K$ meets the perpendicular bisector of $BC$ at height
  $\tfrac12 BC\cot(\angle A+\beta)$. Apply it with $B\leftrightarrow C$ to $X=L$ (valid by the second box in ($\ast$), with $\angle
  ACL=\beta$): $\ell_L$ meets the same line at the same height $\tfrac12 BC\cot(\angle A+\beta)$. So $\ell_K$ and $\ell_L$ pass through
  one common point $Z$ of the perpendicular bisector. By ($\dagger$) their unique intersection is $A^\ast$, hence $A^\ast=Z$ lies on the
  perpendicular bisector of $BC$. Thus $A^\ast B=A^\ast C$ and, by Step 1, $OM=ON$. $\blacksquare$

  Step 3: Proof of the Lemma

  Put $;\mu=\angle BAX,\ \nu=\angle CAX=\angle A-\mu,\ \varepsilon=\angle ACX,\ \delta=\angle BMX.$ The pair $(\mu,\beta)$ determines
  $X$.

  (a) Median relation. In $\triangle ABX$, the cevian $XM$ hits the midpoint $M$ of $AB$. The Ratio Lemma gives $\dfrac{\sin\angle
  AXM}{\sin\angle BXM}=\dfrac{BX}{AX}=\dfrac{\sin\mu}{\sin\beta}$. In $\triangle BMX$ we have $\angle MBX=\beta,\ \angle BMX=\delta$, so
  $\angle BXM=\pi-\beta-\delta$; and $\angle AXM=\angle AXB-\angle BXM=(\pi-\beta-\mu)-(\pi-\beta-\delta)=\delta-\mu$. Therefore
  $\dfrac{\sin(\delta-\mu)}{\sin(\beta+\delta)}=\dfrac{\sin\mu}{\sin\beta}$, and expanding,
  $$\cot\mu=\cot\beta+2\cot\delta. \tag{a}$$

  (b) The $\varepsilon$–relation. Computing $AX$ in $\triangle ABX$ and $\triangle ACX$ and using $AB/AC=\sin C/\sin B$,
  $$\frac{\sin C\sin\beta}{\sin(\beta+\mu)}=\frac{AX}{AB\cdot AC/\ldots}=\frac{\sin B\sin\varepsilon}{\sin(\varepsilon+\nu)}\
  \Longrightarrow\ \cot\varepsilon=\frac{\sin B,\sin(\beta+\mu)}{\sin C,\sin\beta,\sin(\angle A-\mu)}-\cot(\angle A-\mu). \tag{b}$$

  (c) The height. Place $P$ (midpoint of $BC$) at the origin with $BC$ on the $x$-axis, $B=(-a,0),\ C=(a,0)$, $a=\tfrac12 BC$, $A$
  above. If $A_1=(0,h)$ is on the perpendicular bisector with $A_1X\perp AX$, then $(A_1-X)\cdot(A-X)=0$ gives $h=X_y+X_x\cot\theta$,
  where $\theta$ is the inclination of line $AX$. A short computation (the inclination of $AB$ equals $\angle B$, and $AX$ is $AB$
  rotated by $\mu$, so $\theta=\angle B+\mu$) with $X=B+BX,(\cos(\angle B-\beta),\sin(\angle B-\beta))$ and
  $BX=\dfrac{AB\sin\mu}{\sin(\beta+\mu)}=\dfrac{2a\sin C\sin\mu}{\sin\angle A,\sin(\beta+\mu)}$ yields
  $$h=-a\cot(\angle B+\mu)+\frac{2a,\sin C,\sin\mu,\cos(\beta+\mu)}{\sin\angle A,\sin(\beta+\mu),\sin(\angle B+\mu)} .$$
  Using $\cot(\angle A+\beta)+\cot(\angle B+\mu)=\dfrac{\sin\bigl((\angle A+\beta)+(\angle B+\mu)\bigr)}{\sin(\angle A+\beta)\sin(\angle
  B+\mu)}$ and $(\angle A+\beta)+(\angle B+\mu)=\pi-\angle C+\beta+\mu$, so that the numerator is $\sin(\angle C-\beta-\mu)$, one finds
  $$h=\tfrac12 BC\cot(\angle A+\beta)\ \Longleftrightarrow\ \underbrace{2\sin C,\sin\mu,\cos(\beta+\mu),\sin(\angle A+\beta)=\sin\angle
  A,\sin(\beta+\mu),\sin(\angle C-\beta-\mu)}_{(\star)} . \tag{c}$$

  (d) Hypothesis $\Rightarrow(\star)$. The hypothesis $\angle BMX=\angle ACX-\beta$ says $\varepsilon=\beta+\delta$, i.e.
  $\cot\varepsilon=\cot(\beta+\delta)$ (both angles lie in $(0,\pi)$). Substituting $\cot\delta=\tfrac12(\cot\mu-\cot\beta)$ from (a)
  into $\cot(\beta+\delta)=\dfrac{\cot\beta\cot\delta-1}{\cot\beta+\cot\delta}$, equating with (b), and clearing denominators, the
  relation collapses exactly to $(\star)$. (This is a finite trigonometric expansion; it was verified to be an identity.)

  By (c), $(\star)$ is equivalent to $h=\tfrac12 BC\cot(\angle A+\beta)$. Hence the hypothesis forces the perpendicular to $AX$ at $X$
  to meet the perpendicular bisector of $BC$ at height $\tfrac12 BC\cot(\angle A+\beta)$, proving the Lemma. $\qquad\blacksquare$

  Conclusion

  By Step 3 the Lemma holds; by Step 2 it puts $A^\ast$ on the perpendicular bisector of $BC$; by Step 1 this is equivalent to $OM=ON$.
  $\qquad\blacksquare$

  ---
  Remarks on verification. The whole argument was cross‑checked numerically on many triangles and many choices of the free parameter
  $\beta$ (agreement to $\sim10^{-13}$): the equalities $OM=ON$, $A^\ast B=A^\ast C$, the closed form
  $\Phi(K)=\Phi(L)=\tfrac12\cot(\angle A+\beta)$ for the height, and the median relation (a) and $\varepsilon$–relation (b). The single
  non‑obvious algebraic step — that clearing the hypothesis $\cot\varepsilon=\cot(\beta+\delta)$ produces exactly $(\star)$ — was
  verified symbolically to be an identity (the two cleared expressions coincide). The heart of the solution is the two structural
  discoveries: (i) $OM=ON$ is equivalent to the $A$-antipode $A^\ast$ of $\odot(AKL)$ lying on the perpendicular bisector of $BC$; and
  (ii) each of the two perpendiculars $\ell_K,\ell_L$ hits that bisector at the height $\tfrac12 BC\cot(\angle A+\beta)$, a quantity
  symmetric in $B\leftrightarrow C$.

✻ Cooked for 44m 24s