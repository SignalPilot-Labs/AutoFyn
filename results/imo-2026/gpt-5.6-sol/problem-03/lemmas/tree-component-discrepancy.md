# Tree-component discrepancy lemma

## Statement
Let \(a_1,\ldots,a_m>0\). Suppose that for any different subsets \(I,J\subseteq\{1,\ldots,m\}\),
\[
\left|\sum_{i\in I}a_i-\sum_{j\in J}a_j\right|\ge d
\]
for some \(d>0\). Refine these \(m\) parent pieces using at most \(m-1\) binary splits. If the resulting lengths in nonincreasing order are \(x_1,\ldots,x_q\), then
\[
x_1-x_2+x_3-x_4+\cdots+(-1)^{q+1}x_q\ge d.
\]

## Proof
Pair adjacent final ranks \((x_1,x_2),(x_3,x_4),\ldots\), leaving \(x_q\) unmatched when \(q\) is odd. Form a multigraph on the \(m\) parents by joining the parents containing the two pieces in each pair; loops and parallel edges are allowed. If \(s\le m-1\) splits were made, then \(q=m+s\), so the number of edges is \(\lfloor q/2\rfloor\le m-1\).

Consequently some connected component \(C\) is a tree: otherwise every component would contain a cycle and hence have at least as many edges as vertices, giving at least \(m\) edges in total. Bipartition \(C\) into vertex classes \(A,B\); for an isolated vertex use that vertex as \(A\) and put \(B=\varnothing\). Since \(A\ne B\), the hypothesis gives
\[
\left|\sum_{i\in A}a_i-\sum_{i\in B}a_i\right|\ge d.
\]
Every descendant piece of a vertex in \(C\) is an endpoint of an edge of \(C\), except possibly the unique globally unmatched piece. Each edge of \(C\) joins opposite bipartition classes, so its endpoint lengths \(u,v\) contribute either \(u-v\) or \(v-u\) to the displayed parent-sum difference. The unmatched piece, if its parent lies in \(C\), contributes with either sign. The triangle inequality therefore bounds the displayed difference by a sub-sum of the nonnegative terms
\[
(x_1-x_2)+(x_3-x_4)+\cdots.
\]
This sum is the asserted alternating discrepancy, so it is at least \(d\). ∎
