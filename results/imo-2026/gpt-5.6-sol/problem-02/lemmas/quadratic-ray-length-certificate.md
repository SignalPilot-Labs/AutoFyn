# Quadratic ray-length certificate for IMO 2026 Problem 2

Let
\[
\alpha=\angle BAC,\quad \beta=\angle ABC,\quad \gamma=\angle BCA,
\qquad a=BC,\quad b=CA,\quad c=AB,
\]
and let
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
Assume the strict ranges from the oriented-ray reconstruction lemma, and put
\[
t=BK=\frac{c\sin z}{2\sin(x+z)},\qquad
s=CL=\frac{b\sin y}{2\sin(x+y)}.
\]
The closure equations
\[
t=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)},\qquad
s=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}
\]
imply
\[
Q_t:=bc\sin x-c^2\sin(\alpha+x)
+ct\{2\sin\alpha+\sin(\alpha+2x)\}
-2t^2\sin(\alpha+x)=0,
\]
\[
Q_s:=bc\sin x-b^2\sin(\alpha+x)
+bs\{2\sin\alpha+\sin(\alpha+2x)\}
-2s^2\sin(\alpha+x)=0.
\]
Indeed, the first ray equation gives
\[
\cot z=\frac{c-2t\cos x}{2t\sin x}.
\]
Expanding the first closure equation, dividing by the positive quantity \(\sin z\), and substituting this expression gives
\[
0=-ac\sin(\gamma-x)+2at\sin\gamma
+ct\sin(\alpha+2x)-2t^2\sin(\alpha+x).
\]
The Sine Law and cosine-law projections give
\[
a\sin\gamma=c\sin\alpha,
\qquad a\sin(\gamma-x)=c\sin(\alpha+x)-b\sin x,
\]
which proves \(Q_t=0\). The identical calculation with \((b,s,y,\beta)\) in place of \((c,t,z,\gamma)\), using
\[
a\sin\beta=b\sin\alpha,
\qquad a\sin(\beta-x)=b\sin(\alpha+x)-c\sin x,
\]
proves \(Q_s=0\). All divisions are legitimate under the strict angle ranges.

Now place
\[
A=0,\quad B=(c,0),\quad C=(b\cos\alpha,b\sin\alpha),
\]
and set
\[
K=B-t(\cos x,-\sin x),\qquad
L=C-s(\cos(\alpha+x),\sin(\alpha+x)),\qquad d=C-B.
\]
Define
\[
F=2\bigl(|K|^2[L,d]-|L|^2[K,d]\bigr)-(c^2-b^2)[K,L].
\]
With
\[
p=\sin(\alpha+x),\quad q=\sin x,\quad r=\sin\alpha,
\quad u=\sin(\alpha-x),\quad h=2r+\sin(\alpha+2x),
\]
one has the polynomial certificate
\[
2pF=-\bigl(2bcr+2s(bq-cp)\bigr)Q_t
-\bigl(-2bcr+2t(bp-cq)\bigr)Q_s. \tag{*}
\]
For a coefficient audit, expansion of \(F\) in \(t,s\) has coefficients
\[
\begin{array}{c|c}
1&bc(c^2-b^2)r\\
t&b^3p-2b^2cq-2bc^2u-bc^2p\\
s&2b^2cu+b^2cp+2bc^2q-c^3p\\
t^2&2bcr\\
ts&(c^2-b^2)h\\
s^2&-2bcr\\
t^2s&2(bq-cp)\\
ts^2&2(bp-cq).
\end{array}
\]
The coefficients of the right side of (*) and of \(2pF\) agree immediately except possibly in degrees \(t\) and \(s\); those two comparisons are both exactly
\[
hr-q^2=p^2+2pu.
\]
This identity follows from product-to-sum, since both sides after moving \(q^2\) appropriately equal
\[
1-\cos 2\alpha+\frac{\cos 2x-\cos(2\alpha+2x)}2.
\]
Thus (*) holds coefficient by coefficient. In particular, \(Q_t=Q_s=0\) and \(0<\alpha+x<\pi\), hence \(p>0\), imply \(F=0\).
