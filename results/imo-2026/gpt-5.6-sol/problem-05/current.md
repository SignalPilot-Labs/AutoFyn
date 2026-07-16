## Status
solved

## Approaches tried
- Lattice-envelope amplification — worked: one positive arithmetic orbit gives a uniform tail bound, which becomes exact on every positive-displacement orbit; a clopen argument excludes mixed zero and positive displacement.
- Orbit-collision and clopen zero fiber — worked independently: floor-based comparison of two arithmetic orbits forces their positive increments to coincide, and connectedness excludes a mixed zero fiber.

## Current best
The complete characterization is
\[
\boxed{f(t)=t+c\quad(t>0),\qquad c\ge0.}
\]
Both built approaches prove it. The proof below uses the shorter lattice-envelope amplification route.

## Full proof
Let
\[
g(t)=f(t)-t.
\]
Because every quantity in the original inequalities is positive, squaring is reversible. Thus the hypothesis is equivalent to
\[
(f(x)+y)^2-4xf(y)\ge0                                      \tag{1}
\]
and
\[
2x^2+2f(y)^2-(f(x)+y)^2\ge0.                               \tag{2}
\]
Put \(d=g(x)-g(y)\) and \(r=x-y-g(y)\). Direct expansion, an application of the knowledge-base **Sum of squares / completing the square** technique, gives the paired identities
\[
(f(x)+y)^2-4xf(y)
=r^2+d\bigl(2x+2y+g(x)+g(y)\bigr),                         \tag{3}
\]
\[
2x^2+2f(y)^2-(f(x)+y)^2
=r^2-d\bigl(2x+2y+g(x)+g(y)\bigr).                         \tag{4}
\]

We next use the knowledge-base **Functional equations—special values and iteration** technique. Set \(x=f(y)\) in the original sandwich. Both outside terms become \(f(y)\), so
\[
f(f(y))=2f(y)-y,
\]
and hence
\[
g(f(y))=g(y).                                               \tag{5}
\]
Induction now gives, for every integer \(n\ge0\),
\[
f^n(y)=y+ng(y),\qquad g(f^n(y))=g(y).                       \tag{6}
\]
If \(g(y)<0\), choose an integer \(n>y/(-g(y))\). Then (6) gives \(f^n(y)<0\), contradicting the positive codomain. Therefore
\[
g(y)\ge0\quad(y>0).                                        \tag{7}
\]
Consequently \(2x+2y+g(x)+g(y)>0\). Since both (3) and (4) are nonnegative, they yield
\[
|g(x)-g(y)|\bigl(2x+2y+g(x)+g(y)\bigr)
\le (x-y-g(y))^2.                                           \tag{8}
\]

We use the knowledge-base **Casework / exhaustion** method. If \(g\) has no positive value, then (7) gives \(g\equiv0\), so \(f(t)=t\).

Otherwise choose \(v>0\) with \(c=g(v)>0\). Formula (6) gives
\[
g(v+nc)=c\qquad(n\ge0).                                    \tag{9}
\]
For any \(t\ge v+c/2\), set
\[
k=\left\lfloor\frac{t-v}{c}+\frac12\right\rfloor.
\]
Then \(k\ge1\) and \(|t-(v+kc)|\le c/2\). Taking \(y=v+(k-1)c\) in (8), and using (9), gives
\[
|g(t)-c|\bigl(2t+2y+g(t)+c\bigr)
\le (t-(v+kc))^2\le c^2/4.
\]
By (7), the coefficient on the left is at least \(2t\), and therefore
\[
|g(t)-c|\le \frac{c^2}{8t}
\qquad(t\ge v+c/2).                                        \tag{10}
\]

Now suppose \(g(u)=a>0\). By (6),
\[
g(u+na)=a\qquad(n\ge0).
\]
Since \(u+na\to\infty\), substituting \(t=u+na\) into (10) for all sufficiently large \(n\) gives
\[
|a-c|\le\frac{c^2}{8(u+na)}.
\]
Letting \(n\to\infty\), we obtain \(a=c\). Thus
\[
g(t)\in\{0,c\}
\qquad(t>0).                                                 \tag{11}
\]

Let \(Z=\{t>0:g(t)=0\}\). We prove directly from (8), without assuming continuity, that \(Z\) is relatively closed and open. If \(z_n\in Z\) and \(z_n\to z>0\), then (8) gives
\[
|g(z)|(2z+2z_n+g(z))\le(z-z_n)^2.
\]
The possibility \(g(z)=c\) would make the left side tend to \(c(4z+c)>0\) while the right side tends to zero. Hence \(g(z)=0\), so \(Z\) is closed by the sequential characterization of closed sets in metric spaces.

For openness, fix \(p\in Z\) and put
\[
\delta=\min\{p/2,\sqrt{cp}\}>0.
\]
If \(|x-p|<\delta\), then \(x>p/2\). Were \(g(x)=c\), (8) would imply
\[
c(2x+2p+c)\le(x-p)^2.
\]
The left side is greater than \(3cp\), while the right side is less than \(cp\), a contradiction. Thus \(g(x)=0\), and \(Z\) is open. By the knowledge-base **Connectedness Theorem for real intervals**, \(Z\) is empty or all of \((0,\infty)\). Since \(g(v)=c>0\), it is not all of the interval. Hence \(Z=\varnothing\), so \(g\equiv c\). Necessity therefore gives
\[
f(t)=t+c
\]
for some \(c\ge0\).

It remains to apply the knowledge-base **Check the answer** principle. For any \(c\ge0\), define \(f(t)=t+c\). This maps positive reals to positive reals, and direct calculation gives
\[
(f(x)+y)^2-4xf(y)=(x-y-c)^2\ge0,
\]
\[
2x^2+2f(y)^2-(f(x)+y)^2=(x-y-c)^2\ge0.
\]
Because all original expressions are positive, taking square roots recovers both original inequalities. Thus every \(c\ge0\) works, and the complete answer is
\[
\boxed{f(t)=t+c\text{ for all }t>0,\text{ where }c\ge0}. \qed
\]
