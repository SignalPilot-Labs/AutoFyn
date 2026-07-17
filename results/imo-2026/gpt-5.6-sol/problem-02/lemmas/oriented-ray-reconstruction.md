# Oriented ray reconstruction for IMO 2026 Problem 2

Use
\[
\alpha=\angle BAC,\quad \beta=\angle ABC,\quad \gamma=\angle BCA,
\quad a=BC,\quad b=CA,\quad c=AB,
\]
and
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
Reflect if necessary and place
\[
A=(0,0),\quad B=(c,0),\quad C=(b\cos\alpha,b\sin\alpha)
\]
with \([B,C]>0\). The interior hypotheses force the strict ray orders \(BA,BK,BL,BC\) and \(CA,CL,CK,CB\). Consequently
\[
0<x<\min(\beta,\gamma),\quad 0<y<\beta-x,\quad 0<z<\gamma-x.
\]
Put \(e(t)=(\cos t,\sin t)\). Intersecting the positive rays from \(B\) and \(M=B/2\),
\[
B-t e(-x)=B/2+u e(z),
\]
and taking oriented determinants gives
\[
t=\frac{c\sin z}{2\sin(x+z)},\qquad u=\frac{c\sin x}{2\sin(x+z)}.
\]
Thus
\[
K=B-\frac{c\sin z}{2\sin(x+z)}(\cos x,-\sin x).
\]
Likewise,
\[
C-t e(\alpha+x)=C/2-u e(\alpha+x+y)
\]
gives
\[
L=C-\frac{b\sin y}{2\sin(x+y)}(\cos(\alpha+x),\sin(\alpha+x)).
\]
The strict angle ranges make these denominators positive.

The Sine Law in \(BKC\), whose angles are \(\beta-x,\gamma-x-z,\alpha+2x+z\), and in \(BLC\), whose angles are \(\beta-x-y,\gamma-x,\alpha+2x+y\), yields
\[
\frac c2\frac{\sin z}{\sin(x+z)}
=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)},
\]
\[
\frac b2\frac{\sin y}{\sin(x+y)}
=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}.
\]
Every denominator here is the sine of an angle of a nondegenerate triangle and is positive.
