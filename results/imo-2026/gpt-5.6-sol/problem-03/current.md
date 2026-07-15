## Status
solved

## Approaches tried
- Threshold-parity toggles, completed by a provenance multigraph for the dyadic lower bound and a closest-subset-sums/transport construction for the universal upper bound — worked. The layer-cake identity makes each cut an exact parity toggle; the multigraph argument handles arbitrary real and repeated cuts, while the transport construction realizes every abstract cancellation by positive fragments of actual Liu intervals.

## Current best
The exact value is
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
A complete proof is given below. The two load-bearing facts are proved as the Dyadic refinement lemma and the Universal refinement lemma.

## Full proof
Put
\[
Q=1+2+\cdots+2^n=2^{n+1}-1.
\]
We shall prove that Liu Bang can guarantee \(2^n/Q\), and that no larger number can be guaranteed.

### 1. Reduction of the claiming game to an alternating discrepancy

Let the final piece lengths, in nonincreasing order, be
\[
b_1\ge b_2\ge\cdots\ge b_m>0.
\]
We first prove rigorously that the player whose turn it is receives, under optimal play, total value
\[
P(b)=b_1+b_3+b_5+\cdots.
\]
This is a backward-induction argument (the **Induction** method in the knowledge base).

The assertion is immediate for one piece. Suppose it is known for every multiset of fewer than \(m\) pieces. Let \(T=\sum_i b_i\), and suppose the current player first chooses \(b_j\). By the induction hypothesis, the opponent, moving first on the remaining multiset, obtains its odd-ranked sum. Hence the current player's eventual total is \(T\) minus that odd-ranked sum.

If \(j\) is odd, this eventual total is
\[
G_j=b_2+b_4+\cdots+b_{j-1}+b_j+b_{j+2}+b_{j+4}+\cdots,
\]
and therefore
\[
P(b)-G_j=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{j-2}-b_{j-1})\ge0.
\]
If \(j\) is even, it is
\[
G_j=b_2+b_4+\cdots+b_j+b_{j+1}+b_{j+3}+\cdots,
\]
and hence
\[
P(b)-G_j=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{j-1}-b_j)\ge0.
\]
All displayed differences are nonnegative because the \(b_i\) are nonincreasing. Choosing \(b_1\) gives equality, so it is optimal and the value is \(P(b)\). This also deals with ties: the inequalities remain valid when some adjacent lengths are equal, and although several moves may then be optimal, the value is unchanged.

Append one algebraic zero to the list when \(m\) is odd, and define
\[
D(b)=b_1-b_2+b_3-b_4+\cdots.
\]
(The appended zero is not asserted to be a physical piece.) Since the total length is \(1\), adding the equations for the total sum and the alternating sum gives
\[
P(b)=\frac{1+D(b)}2. \tag{1}
\]
Equivalently, grouping adjacent ranks gives
\[
D(b)=(b_1-b_2)+(b_3-b_4)+\cdots, \tag{2}
\]
where an unpaired last positive piece is paired with the algebraic zero. In particular \(D(b)\ge0\).

For completeness, here is the threshold form motivating the approach. Define
\[
N_b(t)=\#\{i:b_i\ge t\},\qquad E(b)=\{t>0:N_b(t)\text{ is odd}\}.
\]
Using the layer-cake identity \(b_i=\int_0^\infty {\bf1}_{t\le b_i}\,dt\), and interchanging a finite sum and an integral (a finite instance of **Double counting**), we get
\[
\begin{aligned}
D(b)
&=\int_0^\infty\sum_i(-1)^{i+1}{\bf1}_{t\le b_i}\,dt\\
&=\int_0^\infty {\bf1}_{N_b(t)\text{ odd}}\,dt
=|E(b)|. \tag{3}
\end{aligned}
\]
Indeed, at a fixed threshold the indicators are \(1\) for precisely the first \(N_b(t)\) ranks, and \(1-1+\cdots+(-1)^{N_b(t)+1}\) is \(1\) or \(0\) according as \(N_b(t)\) is odd or even.

If one current piece of length \(x\) is split into positive lengths \(u\le v\), where \(u+v=x\), its contribution to the parity of \(N_b(t)\) changes as follows. On \((0,u]\), one old surviving piece is replaced by two, so parity toggles. On \((u,v]\), both before and after the cut exactly one of these pieces survives, so it does not toggle. On \((v,x]\), the old piece survives and neither daughter does, so it toggles. Above \(x\), neither configuration contributes. Thus, up to endpoints of measure zero,
\[
E(\text{after})=E(\text{before})\mathbin{\triangle}\bigl((0,u]\cup(v,x]\bigr). \tag{4}
\]
This calculation applies to the length of the current daughter that is actually cut. Consequently it remains valid when a Liu interval, or one of its descendants, is cut repeatedly; it never treats a former parent as though it still existed.

### 2. Liu's dyadic marking and its robustness

Liu marks the cumulative points
\[
\frac1Q,\quad \frac{1+2}{Q},\quad\ldots,\quad
\frac{1+2+\cdots+2^{n-1}}Q.
\]
These are \(n\) distinct points strictly between \(0\) and \(1\), and the resulting \(n+1\) interval lengths are
\[
\frac1Q,\frac2Q,\ldots,\frac{2^n}Q. \tag{5}
\]
We prove the required robustness before rescaling.

**Dyadic refinement lemma.** If the \(n+1\) pieces of lengths \(1,2,4,\ldots,2^n\) are subjected to at most \(n\) cuts, at arbitrary real interior points and with repeated cuts permitted, then the final sorted alternating discrepancy is at least \(1\).

**Proof.** Suppose first that exactly \(n\) cuts have been made. There are then \(2n+1\) final fragments. Pair the sorted fragments in ranks \((1,2),(3,4),\ldots,(2n-1,2n)\), leaving rank \(2n+1\) as the singleton.

Make a multigraph \(G\) whose \(n+1\) vertices are the original dyadic parent pieces. For every ranked pair, draw an edge between the original parents from which its two fragments came. If both fragments came from the same parent, this is a loop. This provenance is unambiguous even after repeated cuts: every current daughter lies in one unique original Liu interval. There are \(n+1\) vertices and exactly \(n\) edges.

Some connected component of \(G\) is a tree. Indeed, every connected multigraph with \(v\) vertices has at least \(v-1\) edges, with equality exactly for a tree (so a loop or a pair of parallel edges creates a cycle and forces at least \(v\) edges in that component). If no component were a tree, every component would have at least as many edges as vertices, contradicting the global counts \(n<n+1\).

Let \(C\) be a tree component, and bipartition its vertices as \(A\sqcup B\). Assign sign \(+1\) to the vertices in \(A\) and \(-1\) to those in \(B\). Since every edge in a bipartite tree has one endpoint in each part, the signed sum of all fragment lengths belonging to vertices of \(C\) can be regrouped edge by edge. Each paired edge contributes, up to sign, the difference between the two lengths in that ranked pair. If the global singleton belongs to a vertex of \(C\), it contributes its own length; otherwise there is no singleton term in this component. Therefore the triangle inequality gives
\[
\left|\sum_{i\in A}2^i-\sum_{i\in B}2^i\right|
\le \sum_{\substack{\text{ranked pairs}\\\text{whose edge lies in }C}}
|\text{first length}-\text{second length}|
+\begin{cases}
\text{singleton length},&\text{if it lies in }C,\\
0,&\text{otherwise}.
\end{cases} \tag{6}
\]
Here the parent mass identity was used: all descendants of parent \(i\) have total length \(2^i\), regardless of how often that parent was cut.

The integer on the left of (6) is nonzero. To see this, take the largest exponent \(j\) occurring among the vertices of \(C\). Its term \(2^j\) has one sign, whereas the sum of the absolute values of all possible smaller terms is at most
\[
1+2+\cdots+2^{j-1}=2^j-1<2^j.
\]
Thus it cannot be cancelled. The left side of (6), being a nonzero integer, is at least \(1\). The right side is at most the sum over all ranked pair gaps plus the global singleton, which is exactly \(D(b)\) by (2). Hence \(D(b)\ge1\).

If only \(k<n\) cuts were made, formally add \(n-k\) zero fragments, one at a time, by replacing any current fragment \(x\) algebraically by \(x,0\). Give the zero the same original provenance as that fragment. This does not change the sorted positive multiset or its discrepancy, but it brings the formal number of cuts to \(n\) and the number of fragments to \(2n+1\), so the preceding graph proof applies. These zero fragments are only a proof device, not marks or physical pieces. Thus the lemma also covers fewer than \(n\) cuts. ∎

After division by \(Q\), the lemma and (1) show that Liu's payoff under the marking (5) is always at least
\[
\frac{1+1/Q}{2}=\frac{Q+1}{2Q}
=\frac{2^{n+1}}{2(2^{n+1}-1)}
=\frac{2^n}{2^{n+1}-1}. \tag{7}
\]
This proves the lower bound.

### 3. Xiang's universal response

We now prove the matching upper bound. This part uses the **Pigeonhole principle** on subset sums and an explicit constructive refinement, in accordance with the knowledge-base principle **Constructive vs. existence**.

We shall repeatedly use two elementary observations.

First, deleting two equal entries from a multiset does not change \(D\). This follows either from (3), because two equal pieces add \(2\) to every threshold count below their common length and hence do not change its parity, or directly by sorting: all copies of a given length form one consecutive block, and removing two terms from that block leaves the parity of every later rank unchanged.

Second, if a parent interval is prescribed positive fragment lengths \(z_1,\ldots,z_d\) summing to its length, those fragments are realized by exactly \(d-1\) legal marks at its successive partial sums. They are strictly interior and distinct because every \(z_i>0\). Marks lying in different parent intervals are automatically distinct. Thus it is enough to count the number of fragments minus the number of parent intervals.

**Universal refinement lemma.** Let \(V\le n+1\) positive parent lengths \(a_1,\ldots,a_V\) have total \(S\). Xiang can use at most \(n\) cuts so that the final discrepancy is at most \(S/(2^{n+1}-1)\). In fact, if \(V\le n\), he can make the discrepancy \(0\).

**Proof.** First suppose \(V=n+1\). Consider the \(2^V\) subset sums
\[
\sum_{i\in I}a_i\qquad(I\subseteq\{1,\ldots,V\}),
\]
all lying in \([0,S]\). If two are equal, choose two distinct subsets with equal sums. Otherwise, place all \(2^V\) distinct sums in increasing order. Their \(2^V-1\) consecutive gaps have total \(S\), so by the Pigeonhole principle some gap is at most
\[
\delta:=\frac{S}{2^V-1}. \tag{8}
\]
In either case there are distinct subsets \(I,J\) whose sums differ by some \(d\) with \(0\le d\le\delta\). Cancel their intersection and put
\[
A=I\setminus J,\qquad B=J\setminus I,\qquad C=\{1,\ldots,V\}\setminus(A\cup B).
\]
Then \(A,B\) are disjoint, not both empty, and, after interchanging them if necessary,
\[
\sum_{i\in A}a_i-
\sum_{j\in B}a_j=d. \tag{9}
\]

Assume first that \(B\ne\varnothing\). Match mass from the \(A\)-parents against mass from the \(B\)-parents by the following finite greedy transport. Select one parent on each side with positive remaining mass, remove the smaller of the two remaining masses from both, and record two fragments of that common positive length, one from each selected parent. At least one selected remaining mass becomes zero at every step, so the process terminates, and it consumes all mass on the \(B\)-side. Let \(e\) be the number of matched fragment-pairs and let \(r\) be the number of \(A\)-parents with positive residual mass at termination. The total residual mass is \(d\).

If \(d>0\), then \(r\ge1\). Of the \(|A|+|B|\) initially positive remainders, the process ends with exactly \(r\) positive ones. Since every recorded pair makes at least one remainder zero, we have
\[
e\le |A|+|B|-r. \tag{10}
\]
There are \(2e+r\) positive fragments in the parents of \(A\cup B\), so producing them costs
\[
2e+r-(|A|+|B|)
\le |A|+|B|-r \tag{11}
\]
cuts. For each parent in \(C\), Xiang cuts it into two equal positive halves, costing one further cut. Thus the total number of cuts is at most
\[
|A|+|B|-r+|C|=V-r\le V-1=n. \tag{12}
\]
Every matched transport pair and every pair of equal halves from \(C\) may be deleted without changing \(D\). What remains consists of the \(r\) residual fragments and has total mass \(d\); consequently its alternating discrepancy is at most its total mass \(d\). Hence the complete final multiset has
\[
D\le d\le\delta=\frac{S}{2^{n+1}-1}. \tag{13}
\]

If \(d=0\), the greedy transport ends with no residual fragment. On its last step both last positive remainders vanish simultaneously, so \(e\le |A|+|B|-1\). The transport cuts then number at most \(|A|+|B|-2\), and after halving every \(C\)-parent the total is at most \(V-2<n\). All final fragments occur in designated equal pairs, so \(D=0\).

It remains in the \(V=n+1\) case to treat \(B=\varnothing\). Then the total mass of the nonempty collection \(A\) is \(d\le\delta\). Halve every parent in \(C\) and also every parent in \(A\) except one. This uses \(|C|+|A|-1=V-1=n\) cuts. Deleting the resulting equal pairs leaves one uncut \(A\)-parent, whose length is at most the total \(A\)-mass \(d\). Thus again \(D\le d\le\delta\). (With positive parent lengths, this case necessarily has \(d>0\).)

Now suppose \(V\le n\). Apply exactly the same subset-sum and refinement construction with this value of \(V\). If \(d=0\), it already gives \(D=0\) with at most \(V-2\) cuts. If \(d>0\) and \(B\ne\varnothing\), the construction before (12) leaves \(r\) residual fragments and uses at most \(V-r\) cuts. Cut each residual fragment into two equal positive halves, using \(r\) more cuts. The total is at most \(V\le n\), and now every fragment belongs to an equal pair, so \(D=0\). If \(B=\varnothing\), halve every parent: this uses exactly \(V\le n\) cuts and also gives \(D=0\). All cuts used here split current positive fragments into positive fragments; in particular no endpoint or zero-size cut, and no perturbation or limiting argument, is needed. This proves the lemma. ∎

Consider now an arbitrary Liu marking. If it creates \(V\le n\) initial intervals, the lemma lets Xiang force \(D=0\), hence by (1) Liu receives exactly \(1/2\), which is already no more than the claimed bound. If Liu uses all \(n\) marks, then \(V=n+1\), \(S=1\), and the lemma gives a legal response satisfying
\[
D\le\frac1{2^{n+1}-1}=\frac1Q.
\]
Equation (1) then gives
\[
P\le\frac{1+1/Q}{2}=\frac{2^n}{2^{n+1}-1}. \tag{14}
\]
Thus no Liu strategy can guarantee more than this number.

Combining (7) and (14), the largest guaranteed share is
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
For \(n=1\), this reads \(c_1=2/3\): Liu's explicit dyadic gaps are \(1/3,2/3\), while for arbitrary two gaps the subset-sum construction uses the one permitted cut and gives \(D\le1/3\); if Liu made no mark, Xiang bisects the stick and gives \(D=0\). Hence the base case, the fewer-marks case, and the stated formula are all directly verified. ∎
