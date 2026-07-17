## Status
solved

## Approaches tried
- Normalize angles by $\theta$, preserve a nonintegral-coordinate invariant when $180^\circ/\theta\notin\mathbb Z$, and for integral total first force an integral angle and then halve its integer label — worked as a complete proof skeleton; the detailed angle chase and interval lemma remained to be written.
- Completed the normalized-state approach by proving the cut formula, exhaustive safe-child lemma, strict integer-crossing lemma (including $n=2$), and strong-induction descent to label $1$ — worked, yielding the full characterization.

## Current best
The complete characterization is
$$\boxed{\theta=180^\circ/n\text{ for an integer }n\ge2.}$$
The proof normalizes all angles by $\theta$. For nonintegral total, an exhaustive four-pair calculation gives Shan-Yu a branch-stable nonintegrality invariant. For integral total, an open interval crossing creates a positive integral angle in either child, after which balanced splitting and strong induction force the exact normalized angle $1$.

## Full proof
Set
$$s=\frac{180^\circ}{\theta}.$$
Using the **change-of-variables/reformulation technique** in the knowledge base, represent a triangle whose angles are $a\theta,b\theta,c\theta$ by $(a,b,c)$. The angle-sum theorem gives
$$a+b+c=s. \tag{1}$$

We first derive the transition caused by a cut. Relabel the current triangle as $ABC$ so that Mulan cuts from $A$ to an interior point $P$ of $BC$. Write
$$\angle A=a\theta,\quad \angle B=b\theta,\quad \angle C=c\theta,
\qquad \angle BAP=x\theta.$$
Because $AP$ is strictly inside $\angle A$, $0<x<a$ and $\angle PAC=(a-x)\theta$. By **angle chasing** (the knowledge base's synthetic toolkit),
$$
\angle APB=180^\circ-(x+b)\theta=(s-b-x)\theta=(a+c-x)\theta,
$$
while
$$
\angle APC=180^\circ-(a-x+c)\theta=(s-a+x-c)\theta=(b+x)\theta.
$$
Thus the children have normalized triples
$$
(x,b,a+c-x),\qquad (a-x,c,b+x). \tag{2}
$$
Conversely, every $x$ with $0<x<a$ defines a legal cut: the ray from $A$ making angle $x\theta$ with $AB$ lies strictly inside $\angle A$; since a triangle is convex, that ray exits the triangle through the open opposite side $BC$. Moves from other vertices are covered by relabeling.

### Necessity

Suppose $s\notin\mathbb Z$. Shan-Yu initially chooses an equiangular triangle, represented by $(s/3,s/3,s/3)$. Its coordinates are nonintegral, because $s/3\in\mathbb Z$ would imply $s\in\mathbb Z$.

We prove a safe-child lemma using the **invariant** and **casework/exhaustion** techniques in the knowledge base.

**Safe-child lemma.** If $a,b,c,s$ are nonintegral and satisfy (1), then after every cut at least one child in (2) has all three coordinates nonintegral.

Indeed, the first child's unchanged coordinate $b$ is nonintegral, so an integral coordinate there must be $x$ or $a+c-x$. The second child's unchanged coordinate $c$ is nonintegral, so an integral coordinate there must be $a-x$ or $b+x$. If both children had an integral coordinate, one of exactly four pairings would occur:

1. $x,a-x\in\mathbb Z$, forcing their sum $a\in\mathbb Z$;
2. $x,b+x\in\mathbb Z$, forcing their difference $b\in\mathbb Z$;
3. $a+c-x,a-x\in\mathbb Z$, forcing their difference $c\in\mathbb Z$;
4. $a+c-x,b+x\in\mathbb Z$, forcing their sum $a+b+c=s\in\mathbb Z$.

Every case contradicts the hypotheses. This proves the lemma.

After each move Shan-Yu retains the safe child. Induction on the number of moves shows that every normalized angle in every retained triangle is nonintegral. In particular no angle equals $\theta$; in fact, this invariant excludes every positive integral multiple of $\theta$. Thus Mulan cannot guarantee victory if $s$ is nonintegral. Necessarily,
$$\frac{180^\circ}{\theta}\in\mathbb Z. \tag{3}$$

### Sufficiency

Now let $s=n\in\mathbb Z$. Since $0^\circ<\theta<180^\circ$, we have $n>1$, hence $n\ge2$.

We first establish the required **pigeonhole/extremal integer-crossing lemma**.

**Integer-crossing lemma.** If positive nonintegral $a,b,c$ satisfy $a+b+c=n\in\mathbb Z$, then the coordinates can be ordered so that for some integer $r$,
$$b<r<a+b. \tag{4}$$

If some coordinate exceeds $1$, call it $a$ and call either other coordinate $b$. Since $b$ is nonintegral, $r=\lfloor b\rfloor+1$ satisfies
$$b<r<b+1<a+b.$$
Otherwise all three coordinates are less than $1$. Their positive integral sum is less than $3$ and at least $2$, so it equals $n=2$. Choose any two as $a,b$ and leave the third as $c$. Then $b<1$ and $a+b=2-c>1$, so $r=1$ satisfies (4). These cases are exhaustive, proving the lemma.

If a current triangle has no integral normalized angle, apply this lemma and set $x=r-b$. By (4), $0<x<a$, so the corresponding cut is legal. Formula (2) shows that the second child has normalized angle
$$b+x=r,$$
and the first has normalized angle
$$a+c-x=a+b+c-r=n-r.$$
Both are positive: $r>b>0$, and $r<a+b=n-c<n$, so $n-r>0$. Hence either child Shan-Yu retains has a positive integral normalized angle.

We now use **strong induction**, equivalently a well-founded integer **monovariant**, as named in the knowledge base.

**Integral-label descent lemma.** From any triangle having an angle $k\theta$, where $k$ is a positive integer, Mulan can force a win in finitely many further moves.

For $k=1$, the game has already stopped with Mulan's victory. Let $k>1$ and assume the assertion for all smaller positive integers. At the vertex carrying $k\theta$, put $j=\lfloor k/2\rfloor$. Then
$$1\le j<k,$$
so the interior ray making angle $j\theta$ with one incident side gives a legal cut and splits the marked angle into
$$j\theta\quad\text{and}\quad(k-j)\theta=\left\lceil\frac{k}{2}\right\rceil\theta.$$
By (2), one child contains the first angle and the other contains the second. Moreover,
$$1\le j\le k-1,\qquad 1\le k-j\le k-1.$$
Whichever child Shan-Yu keeps therefore has a smaller positive integral label, to which the strong induction hypothesis applies. This proves the lemma and also proves finite termination independently of Shan-Yu's choices.

Mulan's complete strategy is now exhaustive. If the current triangle has normalized angle $1$, she has won. If it has an integral normalized angle $k>1$, she applies the descent lemma. If it has no integral normalized angle, she first uses the integer-crossing cut, after which either retained child has a positive integral label, and then applies the descent lemma. Thus every integral $s=n\ge2$ is sufficient.

Combining this with (3), Mulan can guarantee victory precisely for
$$
\boxed{\theta=\frac{180^\circ}{n}\quad(n=2,3,4,\ldots).}
$$
For verification, each displayed value obeys $0^\circ<180^\circ/n<180^\circ$ since $n\ge2$, and substitution gives $180^\circ/\theta=n$, exactly the integral-total case proved sufficient above. Conversely, every other allowed $\theta$ gives nonintegral $s$ and is defeated by Shan-Yu's invariant strategy. $\square$

## Promotable lemmas
- **Safe-child lemma.** If $a,b,c,s$ are nonintegral, $a+b+c=s$, and a split produces $(x,b,a+c-x)$ and $(a-x,c,b+x)$, at least one child has no integral coordinate. Proved under Necessity.
- **Integer-crossing lemma.** Positive nonintegral $a,b,c$ of integral sum $n\ge2$ can be ordered so an integer $r$ satisfies $b<r<a+b$. Proved under Sufficiency, including the $n=2$ case.
- **Integral-label descent lemma.** A triangle with angle $k\theta$, $k\in\mathbb Z_{>0}$, is finitely winning by a balanced split and strong induction. Proved under Sufficiency.
