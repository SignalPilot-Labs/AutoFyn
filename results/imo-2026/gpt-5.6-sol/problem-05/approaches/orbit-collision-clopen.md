## Status
solved

## Approaches tried
- Forced equality at an image point, arithmetic-orbit collision, and a clopen zero-fiber argument — worked: the image substitution gives exact translation orbits, a floor-based comparison makes all positive orbit increments equal, and connectedness excludes mixing zero and positive increments.

## Current best
The complete characterization is
\[
\boxed{f(t)=t+c\quad(t>0),\qquad c\ge 0.}
\]
Necessity follows from an exact pair of squared-slack identities, invariance of the displacement on forward orbits, an Archimedean collision of any two positive-increment orbits, and connectedness of \((0,\infty)\). Sufficiency is verified by showing that both squared slacks equal \((x-y-c)^2\).

## Full proof
We prove that the solutions are exactly
\[
f(t)=t+c\qquad(c\ge 0).
\]

Let \(f:\mathbb R_{>0}\to\mathbb R_{>0}\) satisfy the given inequalities. We use the **Functional equations—special values and iteration** technique from the knowledge base, together with **Sum of squares (SOS) / completing the square**, **induction**, and **contradiction**.

Define the displacement
\[
g(t)=f(t)-t\qquad(t>0).
\]
All quantities occurring in the original inequalities are positive. Consequently, squaring either inequality is reversible, and the hypothesis is equivalent to
\[
(f(x)+y)^2-4xf(y)\ge 0, \tag{1}
\]
and
\[
2x^2+2f(y)^2-(f(x)+y)^2\ge 0. \tag{2}
\]
Fix positive \(x,y\), and put
\[
d=g(x)-g(y),\qquad q=(x-y-g(y))^2,
\]
\[
C=2x+2y+g(x)+g(y).
\]
Since \(f(t)=t+g(t)\), we also have
\[
C=x+y+f(x)+f(y)>0. \tag{3}
\]
We now retain the exact two slack formulas before drawing any conclusion from them. As \(g(x)=g(y)+d\),
\[
\begin{aligned}
(f(x)+y)^2-4xf(y)
&=(x+y+g(y)+d)^2-4x(y+g(y))\\
&=(x+y+g(y))^2-4x(y+g(y))
   +2d(x+y+g(y))+d^2\\
&=(x-y-g(y))^2
   +d\bigl(2x+2y+2g(y)+d\bigr)\\
&=q+dC. \tag{4}
\end{aligned}
\]
Here the last equality uses
\(2g(y)+d=g(x)+g(y)\). Similarly,
\[
\begin{aligned}
2x^2+2f(y)^2-(f(x)+y)^2
&=2x^2+2(y+g(y))^2-(x+y+g(y)+d)^2\\
&=2x^2+2(y+g(y))^2-(x+y+g(y))^2\\
&\qquad{}-2d(x+y+g(y))-d^2\\
&=(x-y-g(y))^2
   -d\bigl(2x+2y+2g(y)+d\bigr)\\
&=q-dC. \tag{5}
\end{aligned}
\]
Thus (1) and (2) say simultaneously that \(q+dC\ge0\) and \(q-dC\ge0\). We will use the resulting exact displacement bound
\[
|g(x)-g(y)|\,[2x+2y+g(x)+g(y)]
 \le (x-y-g(y))^2. \tag{D}
\]
Indeed, (D) follows immediately from (4), (5), and the positivity of \(C\) in (3): the two inequalities give \(-q\le dC\le q\), hence \(|d|C\le q\).

We next use the decisive special value \(x=f(y)\), which is legal because \(f(y)>0\). At this value, the left endpoint of the original sandwich is
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y),
\]
while its right endpoint is
\[
\sqrt{f(y)f(y)}=f(y).
\]
Therefore the middle expression must equal the same number:
\[
\frac{f(f(y))+y}{2}=f(y).
\]
Equivalently,
\[
f(f(y))=2f(y)-y. \tag{6}
\]
Subtracting \(f(y)\) from both sides of (6) gives
\[
g(f(y))=f(f(y))-f(y)=f(y)-y=g(y). \tag{7}
\]

We claim that for every integer \(n\ge0\),
\[
f^n(y)=y+n g(y), \tag{8}
\]
where \(f^0(y)=y\). This is proved by induction, as in the knowledge-base **Induction** method. The cases \(n=0\) and \(n=1\) follow respectively from the definition and from \(f(y)=y+g(y)\). If (8) holds at some \(n\), repeated application of (7) gives
\(g(f^n(y))=g(y)\), and therefore
\[
f^{n+1}(y)=f^n(y)+g(f^n(y))
=y+n g(y)+g(y)=y+(n+1)g(y).
\]
This completes the induction.

Formula (8), together with the positive codomain of \(f\), forces
\[
g(y)\ge0\qquad\text{for every }y>0. \tag{9}
\]
For if \(g(y)<0\), the Archimedean property supplies an integer
\(n>y/(-g(y))\), and then (8) gives
\(f^n(y)=y+n g(y)<0\), contradicting \(f^n(y)>0\).

For completeness, (6) also proves that \(f\) is injective, although injectivity is not needed later. If \(f(r)=f(s)\), then
\[
2f(r)-r=f(f(r))=f(f(s))=2f(s)-s,
\]
and hence \(r=s\).

We now prove that any two positive values of \(g\) are equal. Suppose
\[
g(u)=a>0,\qquad g(v)=b>0. \tag{10}
\]
By (8) and (7), the orbit points
\[
X_n=f^n(u)=u+na
\]
satisfy \(g(X_n)=a\), while
\[
Y_m=f^m(v)=v+mb
\]
satisfy \(g(Y_m)=b\).

For each sufficiently large integer \(n\), define
\[
k_n=\left\lfloor\frac{X_n-v}{b}\right\rfloor,
\qquad m_n=k_n-1.
\]
Because \((X_n-v)/b\to\infty\), we have \(k_n\to\infty\), so for all sufficiently large \(n\), \(k_n\ge1\), \(m_n\ge0\), and \(m_n\to\infty\). The defining property of the floor function gives
\[
0\le X_n-v-k_nb<b.
\]
As \(k_n=m_n+1\), this is
\[
0\le X_n-\bigl(v+(m_n+1)b\bigr)<b. \tag{11}
\]
Apply (D) with \(x=X_n\) and \(y=Y_{m_n}\). Since
\(g(X_n)=a\), \(g(Y_{m_n})=b\), and
\(Y_{m_n}+g(Y_{m_n})=v+(m_n+1)b\), we obtain
\[
|a-b|\,[2X_n+2Y_{m_n}+a+b]
\le \bigl(X_n-v-(m_n+1)b\bigr)^2<b^2. \tag{12}
\]
Both \(X_n=u+na\to\infty\) and \(Y_{m_n}=v+m_nb\to\infty\). Hence the bracket in (12) tends to infinity. If \(a\ne b\), the left side of (12) would therefore tend to infinity while remaining strictly less than the fixed number \(b^2\), a contradiction. Thus
\[
a=b. \tag{13}
\]
We have proved that all positive values of \(g\), if any exist, coincide.

We finish necessity by an exhaustive case split, as prescribed by the knowledge-base **Casework / exhaustion** method.

If \(g\) has no positive value, then (9) gives \(g\equiv0\), so \(f(t)=t\).

Otherwise, choose a point where \(g\) is positive and denote its value by \(c>0\). By (13),
\[
g(t)\in\{0,c\}\qquad(t>0). \tag{14}
\]
Let
\[
Z=\{t>0:g(t)=0\}.
\]
We show directly from (D), without assuming continuity of \(f\) or \(g\), that \(Z\) is both closed and open in \((0,\infty)\).

First, \(Z\) is closed. Let \(z_n\in Z\) and suppose \(z_n\to z\in(0,\infty)\). If \(g(z)=c\), applying (D) with \((x,y)=(z,z_n)\) yields
\[
c(2z+2z_n+c)\le(z-z_n)^2. \tag{15}
\]
The left side is at least \(2zc>0\), whereas the right side tends to \(0\). More explicitly, for all sufficiently large \(n\),
\(|z-z_n|<\sqrt{zc}\), so the right side is less than \(zc\), contradicting the lower bound \(2zc\) for the left side. Therefore \(g(z)=0\), so \(z\in Z\). By the sequential characterization of closed subsets of a metric space, \(Z\) is closed in \((0,\infty)\).

Second, \(Z\) is open. Fix \(p\in Z\), and set
\[
\delta=\min\left\{\frac p2,\sqrt{cp}\right\}>0.
\]
Take any \(x>0\) with \(|x-p|<\delta\). Then \(x>p/2\). If \(g(x)=c\), applying (D) with \((x,y)=(x,p)\) gives
\[
c(2x+2p+c)\le(x-p)^2. \tag{16}
\]
But \(x>p/2\) implies
\[
c(2x+2p+c)>3cp,
\]
whereas \(|x-p|<\delta\le\sqrt{cp}\) implies
\[
(x-p)^2<cp.
\]
These two estimates contradict (16). Hence \(g(x)=0\), and the relative neighborhood
\((p-\delta,p+\delta)\cap(0,\infty)\) lies in \(Z\). Thus \(Z\) is open.

The interval \((0,\infty)\) is connected, and the **connectedness theorem for intervals** states that a subset of a connected space which is both open and closed is either empty or the whole space. Therefore \(Z=\varnothing\) or \(Z=(0,\infty)\). In the present case some point has displacement \(c>0\), so \(Z\ne(0,\infty)\). Hence \(Z=\varnothing\), and (14) gives \(g\equiv c\). Combining this with the no-positive-value case, every solution must have
\[
f(t)=t+c
\]
for some constant \(c\ge0\).

It remains to verify every candidate, in accordance with the knowledge-base **Check the answer** rule. Fix \(c\ge0\) and define \(f(t)=t+c\). This maps \(\mathbb R_{>0}\) into itself. For arbitrary positive \(x,y\), the squared slack in the lower inequality is
\[
\begin{aligned}
(f(x)+y)^2-4xf(y)
&=(x+y+c)^2-4x(y+c)\\
&=x^2+y^2+c^2-2xy-2xc+2yc\\
&=(x-y-c)^2\ge0, \tag{17}
\end{aligned}
\]
and the squared slack in the upper inequality is
\[
\begin{aligned}
2x^2+2f(y)^2-(f(x)+y)^2
&=2x^2+2(y+c)^2-(x+y+c)^2\\
&=x^2+y^2+c^2-2xy-2xc+2yc\\
&=(x-y-c)^2\ge0. \tag{18}
\end{aligned}
\]
Thus
\[
4xf(y)\le(f(x)+y)^2\le2x^2+2f(y)^2.
\]
All quantities whose squares occur here are positive, so taking square roots and dividing by \(2\) recovers exactly
\[
\sqrt{\frac{x^2+f(y)^2}{2}}
\ge\frac{f(x)+y}{2}
\ge\sqrt{xf(y)}.
\]
Therefore every \(c\ge0\) works, and the stated family is complete. ∎

## Promotable lemmas
- **Orbit-displacement rigidity lemma.** If a positive-real function satisfies the paired slack identities (4)–(5), then the forced relation \(f(f(y))=2f(y)-y\) gives \(f^n(y)=y+n(f(y)-y)\) and nonnegative displacement; any two positive displacement values coincide by the floor-based orbit collision in (10)–(13). Proved in the middle of the Full proof.
- **Zero-fiber clopen lemma.** If a nonnegative displacement function satisfying (D) has range contained in \(\{0,c\}\) for some \(c>0\), then its zero fiber is open and closed in \((0,\infty)\), hence is empty or the entire interval. Proved after (14) in the Full proof.
