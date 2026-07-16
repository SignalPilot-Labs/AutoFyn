## Status
solved

## Approaches tried
- One arithmetic orbit generates a uniform lattice envelope on the whole tail, and every other positive-displacement orbit amplifies the asymptotic envelope into exact equality — worked; the remaining possible mixture of zero and positive displacement is excluded by a direct clopen argument.

## Current best
The complete characterization is
\[
\boxed{f(t)=t+c\quad(t>0),\qquad c\ge 0.}
\]
The proof below derives an exact displacement inequality, constructs arithmetic forward orbits, obtains the explicit tail estimate \(\lvert f(t)-t-c\rvert\le c^2/(8t)\) from one positive orbit, exactifies this estimate along every other positive orbit, and eliminates a mixed zero/positive displacement by connectedness.

## Full proof
We prove that the solutions are exactly
\[
f(t)=t+c\qquad(c\ge 0).
\]
The main tools are the **Functional equations—special values and iteration** technique and the **Sum of squares (SOS) / completing the square** technique from the knowledge base. At the end we use the **Check the answer** principle to verify every member of the resulting family.

Define the displacement
\[
g(t)=f(t)-t\qquad(t>0).
\]
All quantities in the given inequalities are positive. Consequently, squaring both inequalities is reversible, and the hypothesis is equivalent to
\[
(f(x)+y)^2-4xf(y)\ge 0                                      \tag{1}
\]
and
\[
2x^2+2f(y)^2-(f(x)+y)^2\ge 0.                               \tag{2}
\]
Fix positive \(x,y\), and write
\[
d=g(x)-g(y),\qquad r=x-y-g(y).
\]
Since \(g(x)=g(y)+d\), direct expansion of the left side of (1) gives
\[
\begin{aligned}
(f(x)+y)^2-4xf(y)
&=(x+y+g(y)+d)^2-4x(y+g(y))\\
&=(x+y+g(y))^2-4x(y+g(y))
   +2d(x+y+g(y))+d^2\\
&=(x-y-g(y))^2
   +d\bigl(2x+2y+2g(y)+d\bigr)\\
&=r^2+d\bigl(2x+2y+g(x)+g(y)\bigr).
\end{aligned}                                                   \tag{3}
\]
Likewise, expanding the left side of (2) yields
\[
\begin{aligned}
2x^2+2f(y)^2-(f(x)+y)^2
&=2x^2+2(y+g(y))^2-(x+y+g(y)+d)^2\\
&=2x^2+2(y+g(y))^2-(x+y+g(y))^2\\
&\hspace{2cm}-2d(x+y+g(y))-d^2\\
&=(x-y-g(y))^2
   -d\bigl(2x+2y+2g(y)+d\bigr)\\
&=r^2-d\bigl(2x+2y+g(x)+g(y)\bigr).
\end{aligned}                                                   \tag{4}
\]
We retain these two paired slack formulas for use below.

We next determine every forward orbit of \(f\). In the original inequality put \(x=f(y)\). Its upper endpoint becomes
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y),
\]
while its lower endpoint becomes
\[
\sqrt{f(y)f(y)}=f(y).
\]
Thus the middle term is squeezed between two equal numbers, so
\[
\frac{f(f(y))+y}{2}=f(y).
\]
Therefore
\[
f(f(y))=2f(y)-y,                                                \tag{5}
\]
and hence
\[
g(f(y))=f(f(y))-f(y)=f(y)-y=g(y).                              \tag{6}
\]
We claim that, for every integer \(n\ge 0\),
\[
f^n(y)=y+n g(y)\quad\text{and}\quad g(f^n(y))=g(y).            \tag{7}
\]
For \(n=0\) both statements follow from the definition of the zeroth iterate. If they hold for an integer \(n\), then (6), applied to \(f^n(y)\), gives
\[
g(f^{n+1}(y))=g(f^n(y))=g(y),
\]
and
\[
f^{n+1}(y)=f^n(y)+g(f^n(y))=y+n g(y)+g(y)=y+(n+1)g(y).
\]
Thus (7) follows by induction.

Every iterate \(f^n(y)\) is positive because \(f\) maps positive reals to positive reals. If \(g(y)<0\), choose an integer \(n>y/(-g(y))\). Formula (7) would then give
\[
f^n(y)=y+n g(y)<0,
\]
a contradiction. We have proved
\[
g(y)\ge 0\qquad\text{for every }y>0.                           \tag{8}
\]
In particular,
\[
H(x,y):=2x+2y+g(x)+g(y)>0.
\]
Since both expressions (3) and (4) are nonnegative, they imply respectively
\[
dH(x,y)\ge-r^2\qquad\text{and}\qquad dH(x,y)\le r^2.
\]
We therefore obtain the exact displacement bound
\[
\boxed{
 |g(x)-g(y)|\bigl(2x+2y+g(x)+g(y)\bigr)
 \le (x-y-g(y))^2
 }                                                               \tag{9}
\]
for all positive \(x,y\).

We now split into exhaustive cases.

**Case 1: no point has positive displacement.** By (8), this means \(g(t)=0\) for every \(t>0\). Hence \(f(t)=t\), which is the claimed family with \(c=0\).

**Case 2: some point has positive displacement.** Fix \(v>0\) and put
\[
c=g(v)>0.
\]
Formula (7) shows that for every integer \(n\ge0\),
\[
f^n(v)=v+nc,
\qquad
 g(v+nc)=c.                                                       \tag{10}
\]
We derive a uniform estimate for \(g\) on a whole tail, rather than merely on this orbit.

Let \(t\ge v+c/2\), and set
\[
k=\left\lfloor\frac{t-v}{c}+\frac12\right\rfloor.
\]
Then \((t-v)/c\ge1/2\), so \(k\ge1\). From
\[
k\le \frac{t-v}{c}+\frac12<k+1
\]
we get
\[
-\frac12<\frac{t-v}{c}-k\le\frac12,
\]
and consequently
\[
|t-(v+kc)|\le\frac c2.                                          \tag{11}
\]
Put \(y=v+(k-1)c\). This number is positive, and (10) gives \(g(y)=c\). Applying (9) with \(x=t\), we find
\[
|g(t)-c|\bigl(2t+2y+g(t)+c\bigr)
   \le (t-y-c)^2
   =(t-(v+kc))^2
   \le\frac{c^2}{4}.                                             \tag{12}
\]
By (8), all the terms omitted from the coefficient besides \(2t\) are nonnegative. Thus that coefficient is at least \(2t\), and (12) gives the explicit uniform tail estimate
\[
\boxed{
 |g(t)-c|\le \frac{c^2}{8t}
 \qquad(t\ge v+c/2).
 }                                                                \tag{13}
\]
No continuity or other regularity of \(g\) has been used; (13) is a numerical consequence of (9) and the nearest point on the fixed arithmetic lattice (10).

We next amplify (13) to an exact statement. Let \(u>0\) satisfy
\[
a:=g(u)>0.
\]
By (7), for every integer \(n\ge0\),
\[
t_n:=f^n(u)=u+na,
\qquad
 g(t_n)=a.                                                        \tag{14}
\]
Because \(a>0\), we have \(t_n\to\infty\). Hence for every sufficiently large \(n\), estimate (13) applies to \(t_n\), and (14) gives
\[
|a-c|=|g(t_n)-c|\le\frac{c^2}{8t_n}
       =\frac{c^2}{8(u+na)}.                                     \tag{15}
\]
The right side tends to zero. More explicitly, if \(|a-c|>0\), then choosing a sufficiently large \(n\) would make \(c^2/(8(u+na))<|a-c|\), contradicting (15). Therefore \(a=c\). We have proved that every positive value of \(g\) equals \(c\). Together with (8), this says
\[
g(t)\in\{0,c\}
\qquad\text{for every }t>0.                                     \tag{16}
\]

It remains to rule out a mixture of these two values. Define the zero locus
\[
Z=\{t>0:g(t)=0\}.
\]
We prove directly from (9), without assuming continuity of \(g\), that \(Z\) is both closed and open relative to \((0,\infty)\).

First, let \((z_n)\) be a sequence in \(Z\) converging to some \(z>0\). Applying (9) with \((x,y)=(z,z_n)\) gives
\[
|g(z)|\bigl(2z+2z_n+g(z)\bigr)\le(z-z_n)^2.                    \tag{17}
\]
If \(g(z)=c\), then taking limits in this purely numerical inequality gives
\[
c(4z+c)\le0,
\]
which is impossible because \(c,z>0\). By (16), the only remaining possibility is \(g(z)=0\), so \(z\in Z\). Thus \(Z\) is sequentially closed. In a metric space, the **sequential characterization of closed sets** states that a set is closed if and only if it contains the limit of every convergent sequence of its points; hence \(Z\) is relatively closed in \((0,\infty)\).

Second, fix \(p\in Z\), and choose
\[
\delta=\min\left\{\frac p2,\frac12\sqrt{c(2p+c)}\right\}>0.
\]
Suppose \(x>0\) and \(|x-p|<\delta\). If \(g(x)=c\), then (9), applied to \((x,p)\), would imply
\[
c(2x+2p+c)\le(x-p)^2.                                          \tag{18}
\]
But the left side of (18) is strictly greater than \(c(2p+c)\), whereas
\[
(x-p)^2<\delta^2\le\frac14c(2p+c).
\]
This is a contradiction. Thus \(g(x)\ne c\), and (16) forces \(g(x)=0\). Therefore every \(p\in Z\) has a relative neighborhood contained in \(Z\), so \(Z\) is relatively open.

By the **Connectedness Theorem for real intervals**, the interval \((0,\infty)\) has no subset other than the empty set and the whole interval that is both relatively open and relatively closed. Hence \(Z=\varnothing\) or \(Z=(0,\infty)\). In the present case, however, \(g(v)=c>0\), so \(v\notin Z\); and if \(Z=(0,\infty)\), that would be contradicted. Thus \(Z=\varnothing\). From (16),
\[
g(t)=c\qquad\text{for every }t>0,
\]
so
\[
f(t)=t+c
\]
with \(c>0\). Together with Case 1, necessity gives \(f(t)=t+c\) for some \(c\ge0\).

We finally verify sufficiency for every such constant, including the endpoint \(c=0\). Let \(c\ge0\) and define \(f(t)=t+c\). This indeed maps \(\mathbb R_{>0}\) into \(\mathbb R_{>0}\). Direct SOS computations give
\[
\begin{aligned}
(f(x)+y)^2-4xf(y)
&=(x+y+c)^2-4x(y+c)\\
&=x^2+y^2+c^2-2xy-2xc+2yc\\
&=(x-y-c)^2\ge0,
\end{aligned}                                                    \tag{19}
\]
and
\[
\begin{aligned}
2x^2+2f(y)^2-(f(x)+y)^2
&=2x^2+2(y+c)^2-(x+y+c)^2\\
&=x^2+y^2+c^2-2xy-2xc+2yc\\
&=(x-y-c)^2\ge0.
\end{aligned}                                                    \tag{20}
\]
Thus the two squared inequalities (1) and (2) hold. Since all expressions in the original statement are positive, taking nonnegative square roots reverses none of the equivalences used in obtaining (1) and (2). Therefore both original inequalities hold for every positive \(x,y\).

Hence the complete answer is
\[
\boxed{f(t)=t+c\text{ for all }t>0,\text{ where }c\ge0}.\qquad\qedhere
\]

## Promotable lemmas
- **Arithmetic-orbit lemma.** If a positive-real-valued function satisfies the problem's two-sided inequality and \(g=f-\mathrm{id}\), then \(f^n(y)=y+ng(y)\), \(g(f^n(y))=g(y)\), and \(g(y)\ge0\) for every \(y>0\) and integer \(n\ge0\). Proved in the Full proof from (5) through (8).
- **One-orbit tail-envelope lemma.** If \(g(v)=c>0\), then \(|g(t)-c|\le c^2/(8t)\) for every \(t\ge v+c/2\). Proved in the Full proof from (10) through (13).
- **Envelope exactification lemma.** Under the same assumptions, every positive value of \(g\) equals \(c\). Proved in the Full proof from (14) through (16).
- **Zero-locus dichotomy lemma.** Once the range of \(g\) is contained in \(\{0,c\}\) with \(c>0\), the exact displacement bound (9) makes \(\{g=0\}\) relatively open and closed, and therefore it is empty or the whole positive interval. Proved in the Full proof after (16).
