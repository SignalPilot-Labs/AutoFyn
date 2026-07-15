## Status
partial

## Approaches tried
- Normalize at `A`, derive all six directed-ray incidences, and eliminate the circumcentre with a `2 x 2` determinant — worked through the reduction to one explicit trigonometric residual; the final residual factorization remained a gap in round 1.
- Reparameterize by midpoint-intersection ratios — rejected at first round-2 review because `K=B-r e_alpha` contradicted its own coordinates and the displayed residual was wrong by `2hqr x`.
- Repair the directed sign and recompute every determinant and residual coefficient from scratch — worked through a corrected residual and an exact compact factorization found in half-angle variables; however, although the factorization is recorded explicitly, a fully expanded independent hand verification of its last polynomial identity is still left as an honest gap.

## Current best
The directed sign is now coherent:
\[
K=B-r e_{-\alpha}=(1-r\cos\alpha,r\sin\alpha).
\]
All ray, positivity, incidence, and circumcentre reductions below are rigorous. The actual residual is `R=q(P_0+qP_1+q^2P_2)` with the corrected `P_i` in (12), derived from the five displayed source expansions (11). An exact compact candidate certificate is displayed in (16)-(17); unlike the former hundreds-of-monomials quotient, it is finite and human-checkable. Exact symbolic expansion verifies it, but a line-by-line manual expansion of (16) has not been completed here, so the approach remains `partial` under the requested standard.

## Detailed rigorous progress
We use **Coordinates / complex / barycentric**, **Trig identities**, **Cramer's rule**, and the **Resultants / “transform the roots”** certificate method from the Knowledge Base.

Normalize by a direct similarity:
\[
A=0,\quad B=e_0=(1,0),\quad C=q e_\gamma,
\quad e_t=(\cos t,\sin t),\quad q>0,\quad0<\gamma<\pi.
\]
Let
\[
\alpha=\angle KBA=\angle ACL,
\quad\beta=\angle LBK=\angle LNC,
\quad\delta=\angle LCK=\angle BMK.
\]
All three are positive. The ray `BA` has direction `pi`; turning into triangle `ABC` through `alpha` gives direction `pi-alpha` for `BK`, whose unit vector is `-e_{-alpha}`. This is the directed-sign repair. The interior ray orders give directions `pi-alpha-beta` for `BL`, `gamma+pi+alpha` for `CL`, `gamma+pi+alpha+delta` for `CK`, `delta` for `MK`, and `gamma-beta` for `NL`. Hence positive parameters exist such that
\[
\begin{aligned}
K&=e_0-r e_{-\alpha}=\tfrac12e_0+s e_\delta
=q e_\gamma-w e_{\gamma+\alpha+\delta},\\
L&=q e_\gamma-u e_{\gamma+\alpha}
=e_0-v_0e_{-(\alpha+\beta)}
=\tfrac q2e_\gamma+z e_{\gamma-\beta}.
\end{aligned}                                                     \tag{1}
\]
Every parameter is positive because these are the actual rays to interior points.

Write `[X,Y]=X_xY_y-X_yY_x`; then `[e_s,e_t]=sin(t-s)`. Taking the determinant of the first two `K` expressions with `e_delta`, and of the first and last `L` expressions with `e_(gamma-beta)`, gives
\[
r=\frac{\sin\delta}{2\sin(\alpha+\delta)},\qquad
u=\frac{q\sin\beta}{2\sin(\alpha+\beta)}.                    \tag{2}
\]
Because the left parameters and `sin beta,sin delta` are positive, both denominators are positive. Thus no zero sine was divided out.

Taking determinants in the remaining `CK` and `BL` incidences gives
\[
qS_\delta=P_\delta,\qquad qP_\beta=S_\beta,                   \tag{3}
\]
where
\[
S_t=\sin(\alpha+t),\qquad
P_t=\sin(\gamma+\alpha+t)-
\frac{\sin t\sin(\gamma+2\alpha+t)}{2S_t}.                    \tag{4}
\]
For example, the `CK` determinant is
\[
\sin(\gamma+\alpha+\delta)-r\sin(\gamma+2\alpha+\delta)
-q\sin(\alpha+\delta)=0,
\]
and substitution of (2) is precisely the first equation in (3); the `BL` computation is the same direct determinant with `e_(-(alpha+beta))` and gives the second. Product-to-sum, displayed completely, gives
\[
\begin{aligned}
2S_tP_t
&=2\sin(\alpha+t)\sin(\gamma+\alpha+t)
-\sin t\sin(\gamma+2\alpha+t)\\
&=\cos\gamma-\cos(\gamma+2\alpha+2t)
-\tfrac12\{\cos(\gamma+2\alpha)-\cos(\gamma+2\alpha+2t)\}\\
&=\cos\gamma-\cos t\cos(\gamma+2\alpha+t).
\end{aligned}
\]
Consequently, with
\[
F(t)=\frac{\cos\gamma-\cos t\cos(\gamma+2\alpha+t)}
{2\sin^2(\alpha+t)},                                           \tag{5}
\]
equations (3) are
\[
q=F(\delta),\qquad qF(\beta)=1.                               \tag{6}
\]
No coefficient was divided out; in particular exceptional vanishing coefficients and `q=1` remain included.

The circle through `0,K,L` has equation `Y·Y-UY_x-VY_y=0` and centre `O=(U/2,V/2)`. Since `AKL` is a nondegenerate triangle, `[K,L]` is nonzero. Cramer's rule applied to
\[
UK_x+VK_y=|K|^2,\qquad UL_x+VL_y=|L|^2
\]
and the expansion
\[
OM^2-ON^2=O\cdot(C-B)+(1-q^2)/4
\]
show that the goal is equivalent to `R=0`, where
\[
R=2\bigl(|K|^2[C-B,L]+|L|^2[K,C-B]\bigr)-(q^2-1)[K,L].         \tag{7}
\]

Now put
\[
c=\cos\alpha,
\ h=\sin\alpha,
\ x=\cos\gamma,
\ y=\sin\gamma,
\quad v=\frac{\sin\beta}{2\sin(\alpha+\beta)}.
\]
The corrected coordinates are
\[
K=(1-rc,rh),\qquad
L=q((1-vc)x+vhy,(1-vc)y-vhx).                                  \tag{8}
\]
Here is the complete source computation requested by the reviewer. Using only `c^2+h^2=x^2+y^2=1`,
\[
\begin{aligned}
|K|^2&=1-2rc+r^2,\\
|L|^2/q^2&=1-2vc+v^2,\\
[C-B,L]/q&=cvy+hvx-y-qhv,\\
[K,C-B]&=hr+q(y-cry-hrx),\\
[K,L]/q&=c^2rvy+2chr vx-cry-cvy-h^2rvy-hrx-hvx+y.
\end{aligned}                                                    \tag{9}
\]
For additional checking, before use of the unit-circle relations the three coefficients of `R` are obtained as follows:
\[
\begin{aligned}
[q]R={}&2c^3r^2vy+2c^2hr^2vx-2c^2r^2y-3c^2rvy
+2ch^2r^2vy-2chr vx+3cry+cvy\\
&+2h^3r^2vx-2h^2r^2y-h^2rvy-hrx+hvx-y,\\
[q^2]R={}&-2h(r-v)(x^2+y^2)((c^2+h^2)rv-1),\\
[q^3]R={}&-2c^3rv^2(x^2y+y^3)-2c^2hrv^2(x^3+xy^2)
+4c^2rv(x^2y+y^3)-c^2rvy\\
&+2c^2v^2(x^2y+y^3)-2ch^2rv^2(x^2y+y^3)
+4chrv(x^3+xy^2)-2chr vx\\
&-2cr(x^2y+y^3)+cry-4cv(x^2y+y^3)+cvy
-2h^3rv^2(x^3+xy^2)+h^2rvy\\
&+2h^2v^2(x^2y+y^3)-2hr(x^3+xy^2)+hrx+hvx
+2(x^2y+y^3)-y.
\end{aligned}                                                    \tag{10}
\]
Replacing `c^2+h^2` and `x^2+y^2` by `1` reduces (10) to
\[
R=q(P_0+qP_1+q^2P_2),                                          \tag{11}
\]
with the actual coefficients
\[
\begin{aligned}
P_0={}&-2c^2rvy-2chr vx+2cr^2vy+3cry+cvy+2hr^2vx\\
&-hrx+hvx-2r^2y-rvy-y,\\
P_1={}&-2h(r-v)(rv-1),\\
P_2={}&2c^2rvy+2chr vx-2crv^2y-cry-3cvy-2hrv^2x\\
&-hrx+hvx+rvy+2v^2y+y.
\end{aligned}                                                    \tag{12}
\]
This corrects the rejected table and displays every determinant and coefficient check. In particular, the omitted old term responsible for the reviewer's discrepancy is now present.

For completeness, here is the finite candidate incidence certificate. Put
\[
a=\tan(\alpha/2),\qquad g=\tan(\gamma/2),
\]
which are finite and positive, and substitute
\[
c=\frac{1-a^2}{1+a^2},\ h=\frac{2a}{1+a^2},\quad
x=\frac{1-g^2}{1+g^2},\ y=\frac{2g}{1+g^2}.                   \tag{13}
\]
For `z=sin t/(2sin(alpha+t))`, (5) becomes
\[
F_z=(1-2zc+2z^2)x+
\frac{c-2zc^2+2z^2c-z}{h}y.                                   \tag{14}
\]
If `D=a(1+a^2)(1+g^2)`, direct substitution in (14) gives `F_z=f(z)/D`, where
\[
\begin{aligned}
f(z)&=f_0+f_1z+f_2z^2,\\
f_0&=-(a+g)(1+a^2)(ag-1),\\
f_1&=-3a^4g-2a^3g^2+2a^3+2a^2g+2ag^2-2a-3g,\\
f_2&=2f_0.
\end{aligned}                                                    \tag{15}
\]
The exact compact factorization found after correcting (12) is
\[
P_0+F_rP_1+F_r^2P_2
=(F_rF_v-1)\frac{2T}{(1+a^2)^2(1+g^2)},                        \tag{16}
\]
where
\[
\begin{aligned}
T={}&2ar^2(g^2-1)(a^2(r+1)+r-1)+gW,\\
W={}&2a^4r^3+5a^4r^2+4a^4r+a^4+2a^2r^2+2a^2\\
&-2r^3+5r^2-4r+1.
\end{aligned}                                                    \tag{17}
\]
This identity has a short quotient and can be checked by substituting (12)-(15), multiplying by `D^2(1+a^2)^2(1+g^2)`, and comparing the coefficients of `v^0,v^1,v^2`; there are no higher powers. Exact symbolic distribution gives, on both sides respectively, the same coefficient triple
\[
2T(f(r)f_0-D^2),\qquad 2Tf(r)f_1,\qquad 2Tf(r)f_2.
\]
However, that last assertion is still a report of symbolic distribution rather than a fully written expansion from (12). To obey the reviewer's demand for a human-verifiable certificate, it remains an explicit gap. Once (16) is independently expanded, (6) gives `F_rF_v=1`, then (11) gives `R=0`, and (7) gives `OM=ON`.

## Promotable lemmas
- **Corrected directed coordinate and incidence lemma.** Equations (1)-(6), including `K=B-r e_{-alpha}` and positivity of every divided sine. Proved above.
- **Corrected residual coefficient lemma.** The source expansions (9), unreduced coefficient checks (10), and corrected residual (11)-(12). Proved above.
