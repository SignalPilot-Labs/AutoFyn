## Status
solved

## Approaches tried
- Square both inequalities, intersect their equality cases at \(x=f(y)\), and classify the resulting arithmetic forward orbits by comparing their displacements.
- Completed the orbit-displacement route: nearest-integer alignment proves equality of all positive displacements, and local cone estimates make the zero and positive displacement fibers open, so connectedness excludes their coexistence — worked.

## Current best
The complete classification is
\[
\boxed{f(x)=x+c\quad (x>0),\qquad c\ge 0.}
\]
The proof follows from two exact squared-residual identities, arithmetic-orbit alignment, and connectedness of \(\mathbb R_{>0}\); every member of the displayed family is verified directly in the original chain.

## Full proof
Let
\[
g(t)=f(t)-t
\]
for every \(t>0\). Because every quantity occurring in the original chain is positive, we may square each of its two inequalities without changing its direction or equality cases. Define
\[
L(x,y)=(f(x)+y)^2-4xf(y)
\]
and
\[
U(x,y)=2\bigl(x^2+f(y)^2\bigr)-(f(x)+y)^2.
\]
The lower and upper inequalities in the problem say, respectively, that
\[
L(x,y)\ge 0\qquad\text{and}\qquad U(x,y)\ge 0. \tag{1}
\]
This is the sum-of-squares/completing-the-square reformulation from the knowledge base.

We first record two exact identities. Direct cancellation gives
\[
\begin{aligned}
L(x,y)+U(x,y)
&=2x^2+2f(y)^2-4xf(y)\\
&=2(x-f(y))^2. \tag{2}
\end{aligned}
\]
For the difference, division by \(2\) and a difference-of-squares factorization give
\[
\begin{aligned}
\frac{L(x,y)-U(x,y)}2
&=(f(x)+y)^2-2xf(y)-x^2-f(y)^2\\
&=(f(x)+y)^2-(x+f(y))^2\\
&=(f(x)+y-x-f(y))(f(x)+y+x+f(y))\\
&=(g(x)-g(y))(x+y+f(x)+f(y)).
\end{aligned}
\]
Thus
\[
L(x,y)-U(x,y)
=2(g(x)-g(y))(x+y+f(x)+f(y)). \tag{3}
\]

Fix \(y>0\) and put \(x=f(y)\). By (2), \(L(f(y),y)+U(f(y),y)=0\); by (1), both summands are nonnegative, so both are zero. In particular,
\[
0=L(f(y),y)=(f(f(y))+y)^2-4f(y)^2.
\]
Both \(f(f(y))+y\) and \(2f(y)\) are positive. Equality of their squares therefore yields
\[
f(f(y))+y=2f(y). \tag{4}
\]
Subtracting \(f(y)\) from both sides shows that
\[
g(f(y))=f(f(y))-f(y)=f(y)-y=g(y). \tag{5}
\]

We now determine every forward orbit. Write \(f^0(y)=y\) and let \(f^n\) denote the \(n\)-fold iterate for \(n\ge 1\). We claim that
\[
f^n(y)=y+n g(y)\qquad(n\ge 0). \tag{6}
\]
For \(n=0\) this is the definition. If it holds at \(n\), repeated application of (5) gives \(g(f^n(y))=g(y)\), and hence
\[
f^{n+1}(y)=f^n(y)+g(f^n(y))=y+n g(y)+g(y)=y+(n+1)g(y).
\]
The induction principle proves (6). Since every iterate lies in \(\mathbb R_{>0}\), (6) also implies
\[
g(y)\ge 0. \tag{7}
\]
Indeed, if \(g(y)<0\), the Archimedean property supplies an integer \(n>y/(-g(y))\), for which \(y+n g(y)<0\), contradicting the positivity of \(f^n(y)\).

Next, since \(L,U\ge0\), the elementary inequality \(|L-U|\le L+U\), together with (2) and (3), gives the cone estimate
\[
|g(x)-g(y)|\,(x+y+f(x)+f(y))\le (x-f(y))^2 \tag{8}
\]
for all \(x,y>0\).

We prove that any two positive values of \(g\) are equal. Let \(p,q>0\), and put
\[
a=g(p)>0,\qquad b=g(q)>0.
\]
For every integer \(m\ge0\), consider
\[
r_m=\frac{q+(m+1)b-p}{a}.
\]
By the nearest-integer lemma, there is an integer \(n_m\) such that
\[
|n_m-r_m|\le\frac12. \tag{9}
\]
Here the lemma itself follows from the floor property: taking \(n_m=\lfloor r_m+\tfrac12\rfloor\) gives \(n_m\le r_m+\tfrac12<n_m+1\), hence \(-\tfrac12<r_m-n_m\le\tfrac12\).
Because \(r_m\to+\infty\), there is an integer \(M\) such that \(r_m>1/2\) for every \(m\ge M\); then every integer \(n_m\) satisfying (9) is nonnegative. Thus all orbit points used below are in the domain for \(m\ge M\). Set
\[
x_m=f^{n_m}(p)=p+n_m a,
\qquad y_m=f^m(q)=q+mb.
\]
By (5), or by its repeated application along the orbits,
\[
g(x_m)=a,
\qquad g(y_m)=b,
\qquad f(y_m)=q+(m+1)b.
\]
Moreover, (9) gives
\[
|x_m-f(y_m)|
=|p+n_m a-q-(m+1)b|
=a|n_m-r_m|
\le \frac a2. \tag{10}
\]
Applying (8) to \((x_m,y_m)\) and using (10), we obtain
\[
|a-b|\bigl(x_m+y_m+f(x_m)+f(y_m)\bigr)\le \frac{a^2}{4}. \tag{11}
\]
The factor in parentheses is at least \(y_m=q+mb\), which tends to infinity because \(b>0\). If \(|a-b|>0\), choose \(m\ge M\) so large that
\[
|a-b|(q+mb)>\frac{a^2}{4};
\]
this is possible by the Archimedean property and contradicts (11). Hence \(a=b\). We have therefore proved:
\[
\text{all positive values assumed by \(g\) are one and the same constant.} \tag{12}
\]
This argument covers rational and irrational ratios \(a/b\) alike: the nearest-integer lemma was applied separately to each real number \(r_m\), and no density assertion was used.

It remains to exclude coexistence of displacement zero and positive displacement. Suppose, for contradiction, that both occur. By (12), there is a fixed \(c>0\) such that
\[
g(t)\in\{0,c\}\qquad(t>0),
\]
and both fibers
\[
Z=\{t>0:g(t)=0\},
\qquad P=\{t>0:g(t)=c\}
\]
are nonempty.

We show that \(Z\) is open in \(\mathbb R_{>0}\). Fix \(p\in Z\), so \(f(p)=p\). If \(x\in P\), estimate (8), applied to \((x,p)\), says
\[
c\bigl(x+p+f(x)+f(p)\bigr)\le (x-f(p))^2=(x-p)^2. \tag{13}
\]
The factor in parentheses is strictly larger than \(f(p)=p\), so the left side is strictly larger than \(cp\). Consequently no \(x\in P\) can satisfy
\[
|x-p|<\sqrt{cp},
\]
for then the right side of (13) would be smaller than \(cp\). Since every point belongs to either \(Z\) or \(P\), the relative neighborhood
\[
(p-\sqrt{cp},p+\sqrt{cp})\cap\mathbb R_{>0}
\]
is contained in \(Z\). Hence \(Z\) is open.

Similarly, \(P\) is open. Fix \(q\in P\). For any \(y\in Z\), apply (8) to \((q,y)\). As \(f(y)=y\), we get
\[
c\bigl(q+y+f(q)+f(y)\bigr)\le(q-f(y))^2=(q-y)^2. \tag{14}
\]
The factor in parentheses is strictly larger than \(q\). Thus the left side is strictly larger than \(cq\), and (14) rules out every \(y\in Z\) satisfying \(|y-q|<\sqrt{cq}\). Therefore
\[
(q-\sqrt{cq},q+\sqrt{cq})\cap\mathbb R_{>0}\subseteq P,
\]
so \(P\) is open as well.

Now \(Z\) and \(P\) would be two disjoint, nonempty, relatively open subsets whose union is the interval \(\mathbb R_{>0}\), contrary to the connectedness theorem for real intervals. For completeness, the relevant connectedness assertion follows from the least-upper-bound property: if an interval were partitioned into nonempty disjoint open sets, choose one point from each and, after ordering them, take the supremum of the points of the first set lying between them. If the supremum belongs to the first set, openness gives points of that set immediately to its right, contradicting its being an upper bound; if it belongs to the second set, openness gives an interval immediately to its left containing no point of the first set, contradicting the defining approximation property of the supremum. Thus such a partition cannot exist.

Combining (7), (12), and the preceding exclusion, \(g\) is constant on \(\mathbb R_{>0}\). Hence, for some \(c\ge0\),
\[
f(x)=x+c\qquad(x>0). \tag{15}
\]

Finally, we verify every function in (15) in the original inequalities. Let \(c\ge0\). Then \(f(x)=x+c>0\) for every \(x>0\), so it has the required codomain. For arbitrary \(x,y>0\), direct calculation gives
\[
\begin{aligned}
(f(x)+y)^2-4xf(y)
&=(x+c+y)^2-4x(y+c)\\
&=(x-y-c)^2\ge0,
\end{aligned}
\]
and
\[
\begin{aligned}
2(x^2+f(y)^2)-(f(x)+y)^2
&=2\bigl(x^2+(y+c)^2\bigr)-(x+c+y)^2\\
&=(x-y-c)^2\ge0.
\end{aligned}
\]
Because \(f(x)+y\), \(x\), and \(f(y)\) are positive, taking square roots is legitimate and these two inequalities are respectively equivalent to
\[
\frac{f(x)+y}{2}\ge\sqrt{xf(y)}
\]
and
\[
\sqrt{\frac{x^2+f(y)^2}{2}}\ge\frac{f(x)+y}{2}.
\]
Thus the full original chain holds. This includes the boundary case \(c=0\), as well as every \(c>0\). Therefore the functions in (15), and only those functions, are the required solutions. \(\square\)

## Promotable lemmas
- **Orbit-cone rigidity lemma.** If \(f:\mathbb R_{>0}\to\mathbb R_{>0}\), \(g=f-\mathrm{id}\), \(g(f(y))=g(y)\), and
  \[
  |g(x)-g(y)|(x+y+f(x)+f(y))\le (x-f(y))^2
  \]
  for all positive \(x,y\), then \(g\) is a nonnegative constant. Proved in the Full proof from equations (5)–(14): positivity gives nonnegative arithmetic orbit increments, nearest-integer orbit alignment identifies all positive increments, and the zero/positive fibers are open and cannot partition an interval.
