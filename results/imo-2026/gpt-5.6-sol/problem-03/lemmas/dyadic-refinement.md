# Dyadic refinement lemma

## Statement
If parent masses are \(1,2,4,\ldots,2^n\), every refinement by at most \(n\) binary cuts has sorted alternating discrepancy at least \(1\).

## Certified proof
First suppose exactly \(n\) cuts are made, yielding \(2n+1\) fragments. Sort them and pair ranks \((1,2),(3,4),\ldots,(2n-1,2n)\), leaving the last rank alone. Form a multigraph on the \(n+1\) original parents, putting one edge for each ranked pair between the parents from which its fragments descend. There are \(n\) edges, so some connected component is a tree: otherwise every component would have at least as many edges as vertices, contrary to \(n<n+1\).

Bipartition such a tree component as \(A\sqcup B\). Give its parent vertices signs \(+1\) and \(-1\) on the two parts. Every paired edge then contributes, up to sign, the difference of its two fragment lengths; if the global singleton belongs to the component, it contributes its own length. Since descendants preserve their parent's total mass, the triangle inequality yields
\[
\left|\sum_{i\in A}2^i-\sum_{i\in B}2^i\right|
\le \sum_{\text{pairs in the component}}|x-y|+\text{(its singleton, if any)}.
\]
The integer on the left is nonzero: the largest power \(2^j\) occurring has magnitude greater than the sum \(1+2+\cdots+2^{j-1}=2^j-1\) of all possible smaller powers. Thus the left side is at least \(1\). The right side is at most the global sum of ranked-pair gaps plus the singleton, which is exactly the sorted alternating discrepancy. Hence that discrepancy is at least \(1\).

For fewer than \(n\) cuts, append enough algebraic zero fragments, assigning each a parent's provenance, to reach \(2n+1\) entries. This changes neither the sorted discrepancy nor parent totals, so the same argument applies. ∎
