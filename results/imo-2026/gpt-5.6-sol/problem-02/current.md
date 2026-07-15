## Status
solved

## Approaches tried
- Oriented determinant elimination — worked. After correcting the directed sign to `K=B-r e_{-\alpha}`, direct expansion gives the corrected residual coefficients below. A tangent-half-angle polynomial certificate factors that residual by the second incidence equation and completes the proof.
- Antipode and quarter-turn telescoping — partial: the antipode and Thales reductions are correct, but no quarter-turn cancellation proving `XB=XC` was supplied.
- Antipode and directed sine-product cancellation — partial: the antipode reduction is correct, but the proposed sine-product cancellation was not established.

## Current best
A complete oriented-coordinate proof is now certified. Its load-bearing algebraic identity is (14) below; after clearing denominators, both sides have the same explicitly displayed coefficients in the auxiliary variable `v`.

## Full proof
We use the **Coordinates / complex / barycentric**, **Trig identities**, and **Cramer's rule** methods from the Geometry section of the Knowledge Base, followed by the polynomial-identity certificate method described under **Resultants / “transform the roots”**.

Apply a direct similarity and, if necessary, a reflection so that
\[
 A=(0,0),\qquad B=(1,0),\qquad C=q e_\gamma,
 \qquad e_t=(\cos t,\sin t),
\]
where `q>0` and `0<\gamma<\pi`. Put
\[
 \alpha=\angle KBA=\angle ACL,\quad
 \beta=\angle LBK=\angle LNC,\quad
 \delta=\angle LCK=\angle BMK.
\]
All three angles are strictly positive because the relevant points lie strictly inside the stated angles and triangles.

We first record all directed rays. At `B`, the ray `BA` has direction `\pi`. Turning from `BA` into the interior of `ABC` gives `BK` direction `\pi-\alpha`; because `K` lies inside `\angle LBA`, the ray `BL` is farther from `BA` by `\beta`, so it has direction `\pi-\alpha-\beta`. At `C`, the ray `CA` has direction `\gamma+\pi`; turning into the triangle gives `CL` direction `\gamma+\pi+\alpha`, and then `CK` direction `\gamma+\pi+\alpha+\delta`. At the midpoint `M=B/2`, the ray `MB` has direction `0`, so `MK` has direction `\delta`. At the midpoint `N=C/2`, the ray `NC` has direction `\gamma`, so `NL` has direction `\gamma-\beta`.

Consequently there are positive real parameters `r,s,w,u,v_0,z` such that
\[
\begin{aligned}
 K&=e_0-r e_{-\alpha}=\tfrac12e_0+s e_\delta
   =q e_\gamma-w e_{\gamma+\alpha+\delta},\\
 L&=q e_\gamma-u e_{\gamma+\alpha}
   =e_0-v_0e_{-(\alpha+\beta)}
   =\tfrac q2e_\gamma+z e_{\gamma-\beta}.
\end{aligned}                                                    \tag{1}
\]
Here and below `[X,Y]=X_xY_y-X_yY_x`, so `[e_s,e_t]=\sin(t-s)`.
Taking determinants of the first two expressions for `K`, and of the first and last expressions for `L`, yields
\[
 r=\frac{\sin\delta}{2\sin(\alpha+\delta)},
 \qquad
 v:=\frac uq=\frac{\sin\beta}{2\sin(\alpha+\beta)}.             \tag{2}
\]
Every ray parameter in (1) is positive. Since `0<\beta,\delta<\pi`, the numerators in (2) are positive, and hence both displayed denominators are positive as well. Thus no zero sine has been divided out.

Taking the determinant in the remaining `CK` incidence gives
\[
 \sin(\gamma+\alpha+\delta)
 -r\sin(\gamma+2\alpha+\delta)
 -q\sin(\alpha+\delta)=0.
\]
The analogous determinant in the `BL` incidence gives the corresponding equation with `\beta`. Define
\[
 S_t=\sin(\alpha+t),\qquad
 P_t=\sin(\gamma+\alpha+t)
 -\frac{\sin t\sin(\gamma+2\alpha+t)}{2S_t}.
\]
The two incidences are therefore
\[
 qS_\delta=P_\delta,
 \qquad qP_\beta=S_\beta.                                      \tag{3}
\]
Product-to-sum gives
\[
\begin{aligned}
2S_tP_t
 &=2\sin(\alpha+t)\sin(\gamma+\alpha+t)
   -\sin t\sin(\gamma+2\alpha+t)\\
 &=\cos\gamma-\cos(\gamma+2\alpha+2t)
   -\tfrac12\bigl(\cos(\gamma+2\alpha)
                   -\cos(\gamma+2\alpha+2t)\bigr)\\
 &=\cos\gamma-\cos t\cos(\gamma+2\alpha+t).
\end{aligned}
\]
Thus, for
\[
 F(t)=\frac{\cos\gamma-
       \cos t\cos(\gamma+2\alpha+t)}{2\sin^2(\alpha+t)},
\]
equations (3) become
\[
 q=F(\delta),\qquad qF(\beta)=1.                               \tag{4}
\]

We next translate the desired equality into a determinant identity. The circle through `A=0,K,L` has equation
\[
 Y\mathbin\cdot Y-UY_x-VY_y=0
\]
and centre `O=(U/2,V/2)`. The phrase “circumcentre of triangle `AKL`” entails that `A,K,L` are noncollinear, so `[K,L]\ne0`. Passage through `K` and `L` gives
\[
 UK_x+VK_y=|K|^2,
 \qquad UL_x+VL_y=|L|^2.                                       \tag{5}
\]
Since `M=B/2` and `N=C/2`, direct expansion gives
\[
 OM^2-ON^2=O\mathbin\cdot(C-B)+\frac{1-q^2}{4}.                 \tag{6}
\]
Cramer's rule in (5), followed by (6), shows that `OM=ON` is equivalent to
\[
 R:=2\bigl(|K|^2[C-B,L]+|L|^2[K,C-B]\bigr)
 -(q^2-1)[K,L]=0.                                               \tag{7}
\]

Put
\[
 c=\cos\alpha,\quad h=\sin\alpha,
 \quad x=\cos\gamma,\quad y=\sin\gamma.
\]
By (1) and (2),
\[
 K=(1-rc,rh),
 \qquad
 L=q\bigl((1-vc)x+vhy,(1-vc)y-vhx\bigr).                       \tag{8}
\]
The five source expansions needed in (7) are
\[
\begin{aligned}
 |K|^2&=1-2rc+r^2,\\
 |L|^2/q^2&=1-2vc+v^2,\\
 [C-B,L]/q&=cvy+hvx-y-qhv,\\
 [K,C-B]&=hr+q(y-cry-hrx),\\
 [K,L]/q&=c^2rvy+2chrvx-cry-cvy-h^2rvy-hrx-hvx+y.
\end{aligned}                                                   \tag{9}
\]
Substitution into (7), collecting powers of `q`, and using only
`c^2+h^2=x^2+y^2=1`, gives
\[
 R=q(P_0+qP_1+q^2P_2),                                         \tag{10}
\]
where
\[
\begin{aligned}
P_0={}&-2c^2rvy-2chrvx+2cr^2vy+3cry+cvy+2hr^2vx\\
     &-hrx+hvx-2r^2y-rvy-y,\\
P_1={}&-2h(r-v)(rv-1),\\
P_2={}&2c^2rvy+2chrvx-2crv^2y-cry-3cvy-2hrv^2x\\
     &-hrx+hvx+rvy+2v^2y+y.
\end{aligned}                                                   \tag{11}
\]

It remains to use (4). Set
\[
 a=\tan(\alpha/2),\qquad g=\tan(\gamma/2).
\]
Because `0<\alpha,\gamma<\pi`, both numbers are finite and positive. For
\[
 z=\frac{\sin t}{2\sin(\alpha+t)},
\]
substitution in the formula for `F(t)` gives
\[
 \Phi(z)=(1-2zc+2z^2)x+
 \frac{c-2zc^2+2z^2c-z}{h}\,y.                                \tag{12}
\]
In particular, by (2) and (4),
\[
 q=\Phi(r),\qquad \Phi(r)\Phi(v)=1.                            \tag{13}
\]
This step does not divide by a possibly vanishing coefficient; indeed `q>0` already shows that the relevant values of `\Phi` are nonzero.

For a finite polynomial certificate, put
\[
 D=a(1+a^2)(1+g^2),\qquad \Phi(z)=\frac{f(z)}D,
\]
where direct tangent-half-angle substitution in (12) gives
\[
\begin{aligned}
f(z)&=f_0+f_1z+f_2z^2,\\
f_0&=-(a+g)(1+a^2)(ag-1),\\
f_1&=-3a^4g-2a^3g^2+2a^3+2a^2g+2ag^2-2a-3g,\\
f_2&=2f_0.
\end{aligned}
\]
Define
\[
\begin{aligned}
T={}&2ar^2(g^2-1)\bigl(a^2(r+1)+r-1\bigr)+gW,\\
W={}&2a^4r^3+5a^4r^2+4a^4r+a^4+2a^2r^2+2a^2\\
   &-2r^3+5r^2-4r+1.
\end{aligned}
\]
Then the exact identity
\[
 P_0+\Phi(r)P_1+\Phi(r)^2P_2
 =\bigl(\Phi(r)\Phi(v)-1\bigr)
   \frac{2T}{(1+a^2)^2(1+g^2)}                                \tag{14}
\]
holds. Here is a direct coefficient check. Substitute
\[
 c=\frac{1-a^2}{1+a^2},\quad h=\frac{2a}{1+a^2},\quad
 x=\frac{1-g^2}{1+g^2},\quad y=\frac{2g}{1+g^2}
\]
into (11), multiply both sides of (14) by
`D^2(1+a^2)^2(1+g^2)`, and collect in `v`. Both sides are quadratic in `v`, and their coefficients of `v^0,v^1,v^2`, respectively, are
\[
 2T\bigl(f(r)f_0-D^2\bigr),
 \qquad 2Tf(r)f_1,
 \qquad 2Tf(r)f_2.
\]
This verifies (14) coefficient by coefficient.

Now (13) makes the right-hand side of (14) zero. Since `q=\Phi(r)`, equations (10) and (14) give `R=0`. By (7), this is equivalent to `OM^2=ON^2`; distances are nonnegative, so `OM=ON`, as required.
