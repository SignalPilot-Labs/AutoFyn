## Status
solved

## Approaches tried
- Oblique coordinates based at \(A\), with the circle represented by its two linear coefficients — all branch, ray-intersection, and circle-system issues were settled, reducing the theorem to one explicit determinant identity; the requested final human-checkable cancellation remained unproved in round 1.
- Quadratic ray-length elimination followed by an explicit low-degree certificate — worked: the two closure conditions give independent quadratics in \(BK\) and \(CL\), and a coefficient-by-coefficient audit proves that their displayed linear combination is the required determinant identity.

## Current best
The oblique-coordinate approach is complete. After the certified oriented-ray reconstruction, the two closure conditions yield quadratics \(Q_t=Q_s=0\). The determinant expression equivalent to \(OM=ON\) is an explicit linear combination of these quadratics; the full coefficient audit is included below.

## Full proof
Let
\[
\alpha=\angle BAC,\quad \beta=\angle ABC,\quad \gamma=\angle BCA,
\qquad a=BC,\quad b=CA,\quad c=AB.
\]
Set
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
Reflecting the configuration if necessary, which preserves angles and distances, put
\[
A=(0,0),\quad B=(c,0),\quad C=(b\cos\alpha,b\sin\alpha)
\]
with the oriented determinant \([B,C]>0\).

We first invoke the certified **oriented positive-ray reconstruction lemma**. The strict ray orders forced by the interiority hypotheses give
\[
0<x<\min(\beta,\gamma),\qquad 0<y<\beta-x,
\qquad 0<z<\gamma-x. \tag{1}
\]
Writing \(e(\theta)=(\cos\theta,\sin\theta)\), intersection of the positive rays from \(B\) and the midpoint \(M=B/2\), and similarly from \(C\) and \(N=C/2\), gives
\[
K=B-t e(-x),\qquad t=BK=\frac{c\sin z}{2\sin(x+z)}, \tag{2}
\]
\[
L=C-s e(\alpha+x),\qquad s=CL=\frac{b\sin y}{2\sin(x+y)}. \tag{3}
\]
For completeness, (2) follows from
\(B-t e(-x)=B/2+u e(z)\) by taking determinants with the two direction vectors; the calculation at \(C\) is identical with the indicated directions. By (1), all the sines in (2) and (3) are positive, so \(s,t>0\), and no reflected or negative-ray branch has been introduced.

The same lemma, using the **Sine Law** (Knowledge Base, Synthetic toolkit) in triangles \(BKC\) and \(BLC\), gives the remaining closure conditions
\[
t=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)}, \tag{4}
\]
\[
s=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}. \tag{5}
\]
The denominators are positive because they are sines of angles of the respective nondegenerate triangles.

We eliminate \(z\) from (2) and (4). Equation (2), expanded, gives
\[
\cot z=\frac{c-2t\cos x}{2t\sin x}. \tag{6}
\]
This division is legitimate because \(t,\sin x,\sin z>0\). Cross-multiplying (4), expanding the sines containing \(z\), and dividing by \(\sin z\), we get
\[
t\{\sin(\alpha+2x)\cot z+\cos(\alpha+2x)\}
=a\{\sin(\gamma-x)\cot z-\cos(\gamma-x)\}. \tag{7}
\]
Substitute (6), multiply by \(2t\sin x\), and move the right side left:
\[
\begin{aligned}
0={}&\{t\sin(\alpha+2x)-a\sin(\gamma-x)\}(c-2t\cos x)\\
&+2t\sin x\{t\cos(\alpha+2x)+a\cos(\gamma-x)\}.
\end{aligned}
\]
Using \(\sin U\cos x-\cos U\sin x=\sin(U-x)\), this becomes
\[
0=-ac\sin(\gamma-x)+2at\sin\gamma
+ct\sin(\alpha+2x)-2t^2\sin(\alpha+x). \tag{8}
\]
The Sine Law in \(ABC\) gives \(a\sin\gamma=c\sin\alpha\). Also
\[
a\sin(\gamma-x)=c\sin(\alpha+x)-b\sin x. \tag{9}
\]
Indeed, expand the left side and use \(a\sin\gamma=c\sin\alpha\) and the cosine-law projection \(a\cos\gamma=b-c\cos\alpha\). Substitution in (8) proves
\[
Q_t:=bc\sin x-c^2\sin(\alpha+x)
+ct\{2\sin\alpha+\sin(\alpha+2x)\}
-2t^2\sin(\alpha+x)=0. \tag{10}
\]

The elimination of \(y\) is analogous but is written out. Equations (3) and (5) give
\[
\cot y=\frac{b-2s\cos x}{2s\sin x}
\]
and
\[
s\{\sin(\alpha+2x)\cot y+\cos(\alpha+2x)\}
=a\{\sin(\beta-x)\cot y-\cos(\beta-x)\}.
\]
Division is valid because \(s,\sin x,\sin y>0\). Substitution and multiplication by \(2s\sin x\) gives
\[
0=-ab\sin(\beta-x)+2as\sin\beta
+bs\sin(\alpha+2x)-2s^2\sin(\alpha+x). \tag{11}
\]
The Sine Law gives \(a\sin\beta=b\sin\alpha\), and the projection identity \(a\cos\beta=c-b\cos\alpha\) gives
\(a\sin(\beta-x)=b\sin(\alpha+x)-c\sin x\). Thus
\[
Q_s:=bc\sin x-b^2\sin(\alpha+x)
+bs\{2\sin\alpha+\sin(\alpha+2x)\}
-2s^2\sin(\alpha+x)=0. \tag{12}
\]

We now invoke the certified **oblique circle-coefficient criterion**, which uses coordinates, Cramer's rule, and the **Power of a Point identity** (Knowledge Base, Synthetic toolkit). For \(d=C-B\), it states that the circle through \(A,K,L\) satisfies \(OM=ON\) if and only if
\[
F:=2\bigl(|K|^2[L,d]-|L|^2[K,d]\bigr)
-(c^2-b^2)[K,L]=0. \tag{13}
\]
There is no singular case: the stated circumcentre of triangle \(AKL\) presupposes that \(A,K,L\) are noncollinear, so \([K,L]\ne0\), exactly the criterion's nonsingularity condition. Briefly, the criterion writes the circle as \(|X|^2-U\cdot X=0\); equality of its powers at \(B/2,C/2\) is equivalent to a linear relation between the two oblique coefficients, and Cramer's rule converts that relation into (13).

It remains to prove (13). Abbreviate
\[
p=\sin(\alpha+x),\quad q=\sin x,\quad r=\sin\alpha,
\quad u=\sin(\alpha-x),\quad h=2r+\sin(\alpha+2x).
\]
From (2) and (3), scalar-product and determinant calculations give
\[
|K|^2=c^2-2ct\cos x+t^2,
\quad |L|^2=b^2-2bs\cos x+s^2, \tag{14}
\]
\[
[K,L]=bcr-csp-btp+ts\sin(\alpha+2x), \tag{15}
\]
\[
[L,d]=bcr+s(bq-cp),
\quad [K,d]=bcr+t(-bp+cq). \tag{16}
\]
Multiplying (14)--(16) in (13) and collecting gives the complete coefficient table
\[
\begin{array}{c|l}
\text{monomial}&\text{coefficient in }F\\ \hline
1&bc(c^2-b^2)r\\
t&b^3p-2b^2cq-2bc^2u-bc^2p\\
s&2b^2cu+b^2cp+2bc^2q-c^3p\\
t^2&2bcr\\
ts&(c^2-b^2)h\\
s^2&-2bcr\\
t^2s&2(bq-cp)\\
ts^2&2(bp-cq).
\end{array} \tag{17}
\]
No other monomial can occur by (14)--(16). The entries in (17) use only the sine addition formulas; in particular the \(ts\)-coefficient simplifies to \((c^2-b^2)h\).

We claim the explicit certificate
\[
\boxed{\begin{aligned}
2pF={}&-\bigl(2bcr+2s(bq-cp)\bigr)Q_t\\
&-\bigl(-2bcr+2t(bp-cq)\bigr)Q_s.
\end{aligned}} \tag{18}
\]
Let \(R\) denote its right side. Multiplying its two linear factors by (10) and (12), and comparing with twice \(p\) times (17), gives this full audit:
\[
\begin{array}{c|l|l}
&[2pF]&[R]\\ \hline
1&2bcpr(c^2-b^2)&2bcpr(c^2-b^2)\\
t&2b(b^2p^2-2bcpq-c^2p^2-2c^2pu)
&2b(b^2p^2-2bcpq-c^2hr+c^2q^2)\\
s&2c(b^2p^2+2b^2pu+2bcpq-c^2p^2)
&2c(b^2hr-b^2q^2+2bcpq-c^2p^2)\\
t^2&4bcpr&4bcpr\\
ts&2p(c^2-b^2)h&2p(c^2-b^2)h\\
s^2&-4bcpr&-4bcpr\\
t^2s&4p(bq-cp)&4p(bq-cp)\\
ts^2&4p(bp-cq)&4p(bp-cq).
\end{array} \tag{19}
\]
The \(t\)- and \(s\)-rows agree by
\[
hr-q^2=p^2+2pu. \tag{20}
\]
To derive (20) by product-to-sum,
\[
hr=1-\cos2\alpha+\frac{\cos2x-\cos(2\alpha+2x)}2,
\]
while
\[
q^2+p^2+2pu
=1-\cos2\alpha+\frac{\cos2x-\cos(2\alpha+2x)}2.
\]
Thus every row of (19) agrees, proving (18) by equality of polynomial coefficients.

Finally, (10) and (12) give \(Q_t=Q_s=0\), so (18) yields \(2pF=0\). Since \(x<\beta\) and \(\alpha+\beta<\pi\), we have \(0<\alpha+x<\pi\), hence \(p>0\). Therefore \(F=0\). By the oblique circle-coefficient criterion, \(OM=ON\), as required. ∎

## Promotable lemmas
- **Quadratic ray-length certificate.** With the notation above, the closure conditions imply the independent equations \(Q_t=Q_s=0\), and the determinant target \(F\) satisfies (18). The eliminations are proved in (6)--(12), and the complete coefficient audit is (14)--(20).
