## Status
solved

## Approaches tried
- Normalize all angles by $\theta$; use a branch-stable nonintegrality invariant for necessity, and for integral total use an integer-crossing cut followed by descent of a positive integral angle label — worked.

## Current best
The complete characterization is
\[
\boxed{\theta=180^\circ/n\quad\text{for an integer }n\ge2.}
\]
The proof derives the exact two-child transition, gives Shan-Yu a safe-child counterstrategy when $180^\circ/\theta$ is nonintegral, and gives Mulan a finite forcing strategy when it is integral.

## Full proof
Set
\[
s=\frac{180^\circ}{\theta}.
\]
Using the **change-of-variables/reformulation technique** in the knowledge base, represent a triangle whose angles are $a\theta,b\theta,c\theta$ by $(a,b,c)$. The angle-sum theorem gives
\[
a+b+c=s. \tag{1}
\]

We first derive the transition caused by a cut. Relabel the current triangle as $ABC$ so that Mulan's chosen perimeter point $P$ lies in the open side $BC$, and the cut joins $P$ to the opposite vertex $A$. Write
\[
\angle A=a\theta,\quad \angle B=b\theta,\quad \angle C=c\theta,
\qquad \angle BAP=x\theta.
\]
Because $AP$ is strictly inside $\angle A$, $0<x<a$ and $\angle PAC=(a-x)\theta$. By **angle chasing** from the knowledge base,
\[
\angle APB=180^\circ-(x+b)\theta=(a+c-x)\theta,
\]
and
\[
\angle APC=180^\circ-(a-x+c)\theta=(b+x)\theta.
\]
Thus the two children have normalized triples
\[
(x,b,a+c-x),\qquad (a-x,c,b+x). \tag{2}
\]
Conversely, every $x$ with $0<x<a$ defines a legal move: the ray from $A$ making angle $x\theta$ with $AB$ lies strictly inside $\angle A$ and, by convexity of the triangle, meets the open opposite side $BC$.

### Necessity
Suppose $s\notin\mathbb Z$. Shan-Yu initially chooses an equiangular triangle, represented by $(s/3,s/3,s/3)$. All three coordinates are nonintegral, since $s/3\in\mathbb Z$ would imply $s\in\mathbb Z$.

We use the **invariant** and **casework/exhaustion** techniques from the knowledge base. Assume a retained triangle $(a,b,c)$ has all three coordinates nonintegral. Since their sum is the fixed nonintegral number $s$, all of $a,b,c,s$ are nonintegral. In (2), the first child already has the nonintegral coordinate $b$, so if that child has an integral coordinate, then either $x$ or $a+c-x$ is integral. The second child already has the nonintegral coordinate $c$, so if it has an integral coordinate, then either $a-x$ or $b+x$ is integral. If both children had an integral coordinate, one of the following four pairs would consist of integers:

1. $x,a-x$, whose sum is $a$;
2. $x,b+x$, whose difference is $b$;
3. $a+c-x,a-x$, whose difference is $c$;
4. $a+c-x,b+x$, whose sum is $a+b+c=s$.

Each case contradicts the corresponding nonintegrality. Hence at least one child has all three normalized angles nonintegral. Shan-Yu retains such a child after every cut. Induction on the number of moves preserves this invariant, so no retained triangle ever has normalized angle $1$. Therefore Mulan cannot guarantee victory when $s$ is nonintegral. Necessarily,
\[
\frac{180^\circ}{\theta}\in\mathbb Z. \tag{3}
\]

### Sufficiency
Now let $s=n\in\mathbb Z$. Since $0^\circ<\theta<180^\circ$, $n>1$, and hence $n\ge2$.

First we prove an integer-crossing lemma using the knowledge base's **pigeonhole/extremal principle**. If positive nonintegral $a,b,c$ satisfy $a+b+c=n$, then they can be ordered so that some integer $r$ satisfies
\[
b<r<a+b. \tag{4}
\]
Indeed, if one coordinate exceeds $1$, call it $a$ and call either other coordinate $b$. Since $b$ is nonintegral, $r=\lfloor b\rfloor+1$ gives
\[
b<r<b+1<a+b.
\]
Otherwise all three coordinates are less than $1$. Their positive integral sum is less than $3$ and at least $2$, so it equals $2$. Choose any two as $a,b$ and leave the third as $c$. Then $b<1<2-c=a+b$, so $r=1$ proves (4).

If the current triangle has no integral normalized angle, order its coordinates according to this lemma and set $x=r-b$. By (4), $0<x<a$, so this is a legal cut. Formula (2) shows that the second child has normalized angle $b+x=r$, while the first has normalized angle
\[
a+c-x=a+b+c-r=n-r.
\]
Both labels are positive: $r>b>0$, and $r<a+b=n-c<n$. Thus whichever child Shan-Yu keeps has a positive integral normalized angle.

It remains to prove that any positive integral normalized angle forces a finite win. We use **strong induction**, equivalently the knowledge base's well-founded integer **monovariant**. Suppose the current triangle has an angle $k\theta$ with $k\in\mathbb Z_{>0}$. If $k=1$, Mulan has already won. If $k>1$, put $j=\lfloor k/2\rfloor$. From the vertex carrying $k\theta$, draw the interior ray making angle $j\theta$ with one incident side. This is legal because $1\le j<k$. The two child triangles retain at that vertex the respective angles
\[
j\theta\quad\text{and}\quad(k-j)\theta.
\]
Both new labels lie in $\{1,\ldots,k-1\}$. Whichever child Shan-Yu keeps therefore has a smaller positive integral label. Strong induction applies, and the strict decrease also proves termination after finitely many moves.

Mulan's strategy is now exhaustive. If the current triangle has normalized angle $1$, she has won. If it has a positive integral normalized angle greater than $1$, she applies the descent. If it has no integral normalized angle, she makes the crossing cut, after which either retained child has a positive integral label, and then applies the descent. Thus every integer $n\ge2$ is sufficient.

Combining necessity and sufficiency,
\[
\boxed{\theta=\frac{180^\circ}{n}\quad(n=2,3,4,\ldots).}
\]
For every displayed value, $0^\circ<180^\circ/n<180^\circ$ and substitution gives $180^\circ/\theta=n$, the integral-total case proved sufficient. Every other allowed $\theta$ gives nonintegral $s$ and is defeated by Shan-Yu's invariant strategy. $\square$
