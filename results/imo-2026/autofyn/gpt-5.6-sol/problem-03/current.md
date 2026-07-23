## Status
solved

## Approaches tried
- Subset-sum folding for Xiang Yu together with a dyadic lower invariant for Liu Bang — worked. The folding construction is made exact by choosing consecutive subset sums; consecutiveness forces every positive-sign parent to have length at least the residual, which lets the entire unmatched residual lie in one parent. The lower invariant is proved by pairing adjacent final ranks and forming a multigraph on Liu's original pieces: the cut budget forces a tree component, whose bipartition gives two distinct subset sums of powers of two differing by at most the alternating discrepancy.

## Current best
The complete minimax argument proves that the largest guaranteed share is
\[
 c_n=\frac{2^n}{2^{n+1}-1}.
\]
The main lower-bound lemma is stronger than the originally proposed informal frontier: if positive parent lengths have all distinct subset sums separated by at least \(d\), then every refinement using at most one fewer split than the number of parents has sorted alternating discrepancy at least \(d\).

## Full proof
Put
\[
 T=1+2+\cdots+2^n=2^{n+1}-1.
\]
We prove that the answer is
\[
 \boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
The proof uses the **Reformulate**, **Pigeonhole / extremal principle**, **Double counting**, **Invariants & monovariants**, **Constructive vs. existence**, and **Check the answer** methods listed in the knowledge base.

### 1. The claiming phase

Suppose the final piece lengths, in nonincreasing order, are
\[
 x_1\ge x_2\ge\cdots\ge x_q>0.
\]
We first prove by backward induction on \(q\) that the player whose turn it is receives, under optimal play, total length
\[
 x_1+x_3+x_5+\cdots.
\]
The assertion is immediate for \(q=1\). Assume it for every smaller number of pieces. If the current player takes \(x_i\), the induction hypothesis says that the opponent subsequently receives the odd-ranked terms of the list obtained by deleting \(x_i\). Thus the current player receives the total of all the other terms not assigned to the opponent, together with \(x_i\).

Let \(O=x_1+x_3+x_5+\cdots\). If \(i\) is odd, comparison with \(O\) shows that the loss caused by taking \(x_i\) rather than \(x_1\) is
\[
 (x_1-x_2)+(x_3-x_4)+\cdots+(x_{i-2}-x_{i-1})\ge0.
\]
If \(i\) is even, that loss is
\[
 (x_1-x_2)+(x_3-x_4)+\cdots+(x_{i-1}-x_i)\ge0.
\]
Every summand is nonnegative because the list is nonincreasing. Hence taking a longest remaining piece is optimal, and taking \(x_1\) yields exactly \(O\). This completes the induction. Ties cause no problem, since the corresponding differences are zero.

Define the sorted alternating discrepancy
\[
 D(x_1,\ldots,x_q)=x_1-x_2+x_3-x_4+\cdots+(-1)^{q+1}x_q.
\]
Because \(\sum_i x_i=1\), Liu Bang's optimal share in the claiming phase is
\[
 x_1+x_3+\cdots=\frac{1+D}{2}. \tag{1}
\]

### 2. A general lower-bound lemma for refinements

We now prove the load-bearing invariant in a precise form.

**Lemma (tree-component discrepancy lemma).** Let \(a_1,\ldots,a_m>0\), and suppose that any two distinct subset sums of these numbers differ by at least \(d>0\). Refine the \(m\) numbers by making at most \(m-1\) binary splits, where a split replaces one current piece by two positive pieces having the same total length. If the resulting lengths in nonincreasing order are \(x_1,\ldots,x_q\), then
\[
 D(x_1,\ldots,x_q)\ge d.
\]

**Proof.** Pair adjacent ranked pieces as
\[
 (x_1,x_2),(x_3,x_4),\ldots.
\]
If \(q\) is odd, leave the last and smallest piece \(x_q\) unmatched. Make a multigraph \(G\) whose \(m\) vertices are the original parent pieces. For every displayed pair, join the parents from which its two members descend. If both members descend from the same parent, this gives a loop; two different pairs may give parallel edges. If \(q\) is odd, mark the vertex containing the unmatched piece.

Let \(e=\lfloor q/2\rfloor\) be the number of edges. If \(s\) splits were made, then \(q=m+s\), with \(s\le m-1\). When \(q\) is even,
\[
 e=\frac{m+s}{2}\le m-\frac12,
\]
so the integer \(e\) satisfies \(e\le m-1\). When \(q\) is odd,
\[
 e=\frac{m+s-1}{2}\le m-1.
\]
Thus in all cases \(G\) has at most \(m-1\) edges.

At least one connected component of \(G\) is a tree. Indeed, if no component were a tree, every component would contain a cycle (a loop counts as a cycle, as do two parallel edges), and hence every component with \(v\) vertices would have at least \(v\) edges. Summing over the components would give at least \(m\) edges, contrary to \(e\le m-1\).

Choose a tree component \(C\). Since it is a tree, it is bipartite; write its vertex classes as \(A\) and \(B\). If \(C\) consists of one isolated vertex, take that vertex as \(A\) and take \(B=\varnothing\). Consider
\[
 \Delta_C=\left|\sum_{i\in A}a_i-\sum_{i\in B}a_i\right|.
\]
The two sums are distinct subset sums: the subsets \(A,B\) are disjoint, and \(A\ne B\) because \(C\) is nonempty. By hypothesis,
\[
 \Delta_C\ge d. \tag{2}
\]

Every final piece descending from a vertex of \(C\) is an endpoint of an edge of \(C\), except possibly the unique globally unmatched piece, if its parent lies in \(C\). For an edge joining \(A\) to \(B\), let its two endpoint-piece lengths be \(u\) and \(v\). Its contribution to the signed difference \(\sum_{i\in A}a_i-\sum_{i\in B}a_i\) is either \(u-v\) or \(v-u\), and therefore has absolute value \(|u-v|\). If the unmatched piece of length \(y\) lies in \(C\), it contributes either \(y\) or \(-y\). The triangle inequality consequently gives
\[
 \Delta_C\le \sum_{\substack{\text{rank pairs whose}\\\text{edge lies in }C}} |u-v|+\begin{cases}y,&\text{if the unmatched piece lies in }C,\\0,&\text{otherwise.}\end{cases} \tag{3}
\]
For every rank pair, its first member is at least its second, so the sum of \(|u-v|\) over all rank pairs, plus the unmatched \(x_q\) when \(q\) is odd, is exactly
\[
 (x_1-x_2)+(x_3-x_4)+\cdots=D(x_1,\ldots,x_q).
\]
The right side of (3) uses only some of these nonnegative terms. Therefore (2) and (3) imply \(D\ge d\), proving the lemma. \(\square\)

Liu Bang now marks \(n\) points so that his \(n+1\) consecutive parent lengths are
\[
 \frac1T,\frac2T,\frac4T,\ldots,\frac{2^n}{T}. \tag{4}
\]
These are positive and sum to one, so the marks are distinct interior points.

Two subset sums of \(1,2,4,\ldots,2^n\) are distinct integers and hence differ by at least \(1\). (In fact, uniqueness of binary expansion says all these subset sums are distinct.) After division by \(T\), distinct subset sums of the lengths in (4) differ by at least \(1/T\). Xiang Yu makes at most \(n=(n+1)-1\) splits of the parent pieces. The lemma with \(m=n+1\) and \(d=1/T\) therefore gives \(D\ge1/T\). By (1), Liu Bang can guarantee
\[
 \frac{1+1/T}{2}=\frac{T+1}{2T}=\frac{2^{n+1}}{2T}=\frac{2^n}{T}. \tag{5}
\]
This proves the required lower bound.

### 3. A consecutive-subset-sum signing

We next construct Xiang Yu's response to an arbitrary marking by Liu Bang. Suppose Liu Bang's marks produce \(m\) positive parent lengths
\[
 a_1,\ldots,a_m,\qquad 1\le m\le n+1,
\]
whose sum is \(1\).

List all \(2^m\) subset sums, with repetitions, in nondecreasing order:
\[
 0=b_0\le b_1\le\cdots\le b_{2^m-1}=1.
\]
By the **Pigeonhole Principle** applied to the \(2^m-1\) adjacent gaps, some consecutive pair satisfies
\[
 r:=b_{j+1}-b_j\le\frac1{2^m-1}. \tag{6}
\]
Choose subsets \(L,U\subseteq\{1,\ldots,m\}\) representing \(b_j,b_{j+1}\), respectively. Cancel their common indices and put
\[
 P=U\setminus L,\qquad N=L\setminus U,
 \qquad Z=\{1,\ldots,m\}\setminus(P\cup N).
\]
Then
\[
 \sum_{i\in P}a_i-
 \sum_{i\in N}a_i=r. \tag{7}
\]
If \(r>0\), then \(P\ne\varnothing\). Moreover, every \(p\in P\) satisfies
\[
 a_p\ge r. \tag{8}
\]
For if \(a_p<r\), then \(p\notin L\), and the subset \(L\cup\{p\}\) would have sum strictly between \(b_j\) and \(b_{j+1}\), contradicting their consecutiveness in the ordered list.

If \(r>0\) and \(N=\varnothing\), then \(P\) has exactly one element. Indeed, if \(p\in P\) and \(|P|\ge2\), then \(0<a_p<\sum_{i\in P}a_i=r\), contradicting (8).

### 4. The exact folding construction and its cut count

We show that Xiang Yu can refine the supported parents \(P\cup N\) into equal pairs and, when \(r>0\), one residual piece of length \(r\).

First suppose \(r>0\) and \(N\ne\varnothing\). Write
\[
 A=\sum_{i\in P}a_i,\qquad B=\sum_{i\in N}a_i,

declaring by (7) that \(A=B+r\). Choose any \(p_*\in P\), and concatenate abstract copies of the \(P\)-parents along \([0,A]\), placing the parent \(p_*\) last. By (8), \(a_{p_*}\ge r\), and hence the combined length of the preceding \(P\)-parents is
\[
 A-a_{p_*}\le A-r=B. \tag{9}
\]
Concatenate the \(N\)-parents, in any order, along \([0,B]\).

Superimpose the two concatenations on \([0,B]\), and subdivide both at the union of all their cumulative parent boundaries in \((0,B)\). If \(B\) lies in the interior of the last \(P\)-parent, also cut that parent at the point corresponding to \(B\). Every common-refinement cell in \([0,B]\) now occurs once as a piece on the \(P\)-side and once as a piece of the same length on the \(N\)-side. By (9), the interval \([B,A]\) lies wholly in the last \(P\)-parent and is a single residual piece of length \(A-B=r\). Thus the supported pieces are equal pairs plus that one residual.

All these abstract subdivisions are physically legal: a boundary lying strictly inside an abstract parent prescribes one mark at the corresponding relative position inside the actual parent interval. Abstract boundaries that already separate two parents prescribe no mark. Hence every prescribed mark is interior to one of Liu Bang's parent intervals; marks in different parent intervals are physically distinct, and marks within one parent are distinct.

Let \(s=|P|+|N|\). There are at most \(|P|-1\) internal cumulative boundaries of the \(P\)-concatenation before \(B\), and exactly \(|N|-1\) internal cumulative boundaries of the \(N\)-concatenation. Making each such boundary on the opposite side costs at most one cut. The truncation boundary \(B\) costs at most one further cut on the \(P\)-side. Therefore the supported construction uses at most
\[
 (|P|-1)+(|N|-1)+1=s-1 \tag{10}
\]
marks. Coincident boundaries only reduce this number.

If \(r>0\) and \(N=\varnothing\), the preceding section showed that \(P\) is a singleton. Leave that parent uncut as the sole residual; the supported construction then uses no cuts, which equals \(s-1\).

Finally, suppose \(r=0\). Then both \(P\) and \(N\) are nonempty: equality of sums is impossible if one of the two disjoint supports is empty, since all \(a_i\) are positive. Concatenate both sides along their common interval \([0,A]=[0,B]\) and take their common refinement as above. Every resulting piece is paired. There is no truncation cut, so the number of cuts is at most
\[
 (|P|-1)+(|N|-1)=s-2. \tag{11}
\]

For each \(i\in Z\), halve the parent \(a_i\), using one cut and producing an equal pair. Since \(|Z|=m-s\), (10) shows that when \(r>0\) the entire construction uses at most
\[
 (s-1)+(m-s)=m-1 \tag{12}
\]
marks. When \(r=0\), (11) gives at most \(m-2\) marks. Thus in every case the construction is legal within the relevant budget stated below; no limiting or coincident-mark argument is needed.

### 5. Xiang Yu's upper bound

If \(m=n+1\), Xiang Yu applies the construction above. It uses at most \(m-1=n\) marks. When \(r=0\), every final piece belongs to an equal pair, so Liu Bang receives exactly half the total length. When \(r>0\), let the sum of one representative from each equal pair be \(H\). The total length identity is
\[
 2H+r=1. \tag{13}
\]
In the globally sorted list, each length occurring in the paired part has even multiplicity, except that the residual may add one further copy to the group of its own length. Consequently the odd-ranked sum takes exactly half of every even multiplicity and additionally takes the residual copy. It is therefore
\[
 H+r=\frac{1+r}{2}. \tag{14}
\]
By (6), now with \(m=n+1\),
\[
 \frac{1+r}{2}\le
 \frac12\left(1+\frac1{2^{n+1}-1}\right)
 =\frac{2^n}{2^{n+1}-1}. \tag{15}
\]

If \(m\le n\) and \(r=0\), the paired construction already gives Liu Bang exactly \(1/2\). If \(m\le n\) and \(r>0\), first use the at most \(m-1\) marks in (12), and then halve the sole residual piece with one additional interior mark. The final multiset consists entirely of equal pairs, and the total number of Xiang Yu's marks is at most \(m\le n\). Liu Bang again receives exactly \(1/2\). Since
\[
 \frac12<\frac{2^n}{2^{n+1}-1},
\]
this also satisfies the desired upper bound. These cases exhaust every number \(m\) of parent pieces that Liu Bang can create with at most \(n\) marks.

Thus, against every initial marking, Xiang Yu has a legal response ensuring that Liu Bang receives no more than \(2^n/T\). Together with Liu Bang's guarantee (5), this proves the boxed value.

As a check of sharpness, against the dyadic parents (4), Xiang Yu may halve the parents of unnormalized lengths \(2,4,\ldots,2^n\). The final unnormalized multiset contains two copies of each of \(1,2,\ldots,2^{n-1}\), together with the original extra \(1\). Its alternating discrepancy is \(1\), so Liu Bang's share is exactly \((1+1/T)/2=2^n/T\). For \(n=1\), the construction gives parent lengths \(1/3,2/3\), and the value is \(2/3\), agreeing with the formula. ∎

## Promotable lemmas
- **Tree-component discrepancy lemma.** If \(m\) positive parent lengths have all distinct subset sums separated by at least \(d\), every refinement made with at most \(m-1\) binary splits has sorted alternating discrepancy at least \(d\). Proved in Section 2 by the adjacent-rank pairing multigraph and a forced tree component.
- **Consecutive-subset-sum folding lemma.** For \(m\) positive masses of total \(1\), there is a refinement using at most \(m-1\) cuts whose multiset consists of equal pairs plus one residual of length at most \(1/(2^m-1)\); if the residual is zero, at most \(m-2\) cuts suffice. Proved in Sections 3–4. The key point is that consecutiveness forces each positive-sign mass to be at least the residual, allowing it to be concentrated in one parent.
- **Odd-rank draft lemma.** In a common-value alternating draft of fixed pieces, taking a longest remaining piece is optimal at every turn, and the first player receives the odd sorted ranks. Proved by backward induction in Section 1.
