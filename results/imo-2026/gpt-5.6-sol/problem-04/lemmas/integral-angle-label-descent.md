# Integral angle-label descent

## Statement
Fix $0^\circ<\theta<180^\circ$ in the triangle-cutting game. If the current triangle has an angle $k\theta$ for a positive integer $k$, then Mulan can force victory after finitely many further moves.

## Proof
Use strong induction on $k$. If $k=1$, the winning condition already holds. For $k>1$, let $j=\lfloor k/2\rfloor$. From the vertex whose angle is $k\theta$, draw the interior ray making angle $j\theta$ with one incident side. Since $1\le j<k$, this ray lies strictly inside the angle and meets the open opposite side, so it is a legal cut. One child retains an angle $j\theta$ at that vertex and the other retains the complementary angle $(k-j)\theta$. Both labels lie in $\{1,\ldots,k-1\}$. Whichever child Shan-Yu keeps therefore has a smaller positive integral angle label, and the strong induction hypothesis applies. Since the label strictly decreases at each such move, victory occurs after finitely many moves. $\square$
