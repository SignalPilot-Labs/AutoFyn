## Status
solved

## Approaches tried
- **Dyadic multiples and affine thinness** — worked. A grid-mark fork and balanced splitting prove sufficiency for reciprocal targets; nested finite-horizon attractors, exhaustive affine predecessor classification, König's infinity lemma, and countable-line avoidance prove necessity.

## Current best
The complete characterization is
\[
\boxed{\theta=\frac{180^\circ}{n}\quad\text{for every integer }n\ge2}.
\]
The proof gives a strategy using at most \(1+\lceil\log_2(n-1)\rceil\) cuts from any nonterminal triangle and excludes every nonreciprocal target.

## Full proof
Put
\[
t=\frac{\theta}{180^\circ}.
\]
Thus \(0<t<1\). We normalize every angle by dividing it by \(180^\circ\), so an ordered state is a triple
\[
(a,b,c)\in\Omega:=\{(a,b,c):a,b,c>0,\ a+b+c=1\}.
\]
This is the **change of variables/reformulation** technique from the knowledge base. The order is bookkeeping; cyclically permuting coordinates does not alter the triangle.

### 1. The transition formula

Suppose Mulan cuts from the vertex whose angle is \(a\). Let the cut split that angle into \(x\) and \(a-x\), where \(0<x<a\). The internal ray making angle \(x\) with the side adjacent to angle \(b\) meets the opposite side in its interior, so every such \(x\) is realized by a legal cut, and conversely every legal cut gives such an \(x\).

One child keeps angle \(b\), and its other angle at the selected vertex is \(x\). By the angle-sum theorem its third angle is \(1-b-x\). The other child keeps \(c\), has angle \(a-x\) at the selected vertex, and hence has third angle
\[
1-c-(a-x)=1-a-c+x=b+x.
\]
Therefore Shan-Yu's two possible retained states are
\[
C_1=(x,b,1-b-x),\qquad C_2=(a-x,c,b+x). \tag{1}
\]
All coordinates are positive: besides \(x>0\) and \(a-x>0\), we have \(1-b-x=a+c-x>c>0\) and \(b+x>0\). Cuts from the other two vertices are described by cyclic permutations of (1).

### 2. Dyadic descent from a multiple of the target

We first prove a constructive lemma by **strong induction**, as named in the knowledge base.

**Lemma 1 (multiple-angle descent).** Suppose a current triangle has an angle \(kt\), where \(k\) is a positive integer. Then Mulan can force a triangle containing angle \(t\) after at most \(\lceil\log _2 k\rceil\) further cuts.

**Proof.** For \(k=1\), the current triangle already contains \(t\). Let \(k\ge2\), and set
\[
p=\left\lfloor\frac{k}{2}\right\rfloor,\qquad q=\left\lceil\frac{k}{2}\right\rceil.
\]
Then \(p,q\) are positive integers, \(p+q=k\), and both are smaller than \(k\). Mulan cuts from the vertex of angle \(kt\), splitting it into the positive angles \(pt\) and \(qt\). This is legal because both are strictly between \(0\) and \(kt\). Whichever child Shan-Yu retains contains one of these two split angles. By induction, Mulan then needs at most
\[
\max\{\lceil\log _2p\rceil,\lceil\log _2q\rceil\}=\lceil\log _2q\rceil
\]
additional cuts.

Write \(d=\lceil\log _2k\rceil\). Since \(k\le2^d\), we have \(q=\lceil k/2\rceil\le2^{d-1}\), and hence \(\lceil\log _2q\rceil\le d-1\). Including the first cut, at most \(d\) cuts are needed. \(\square\)

### 3. Sufficiency when \(t=1/n\)

Assume \(t=1/n\) for an integer \(n\ge2\), and consider any state \((a,b,c)\).

If one angle equals \(kt\) for a positive integer \(k\), then \(k\le n-1\), because that angle is strictly less than the total angle \(1=nt\). Lemma 1 supplies a finite winning strategy.

Suppose instead that no angle is a positive integral multiple of \(t\). Place the grid marks
\[
0,t,2t,\ldots,(n-1)t,nt=1
\]
on an interval of length \(1\), partitioned consecutively into intervals of lengths \(a,b,c\). No interior partition boundary can be a grid mark. Indeed, if the first boundary is \(jt\), then the first angle is the positive multiple \(jt\); if the second boundary is \(jt\), then the remaining angle is \(1-jt=(n-j)t\). Either contradicts this case. Thus every interior grid mark lies strictly inside an angle interval. There is at least one interior mark because \(n\ge2\).

Cyclically label the angles so that a chosen interior mark \(kt\), where \(1\le k\le n-1\), lies in the interval \((b,b+a)\). This is a cyclic choice of the starting point of the cumulative partition: the interval in question has length \(a\) and is preceded by the interval of length \(b\). Choose
\[
x=kt-b.
\]
The strict inclusion \(b<kt<b+a\) gives \(0<x<a\), so this is a legal cut from the vertex of angle \(a\). Formula (1) gives
\[
1-b-x=1-kt=(n-k)t
\]
in the first child and \(b+x=kt\) in the second. Hence, whichever child Shan-Yu keeps, it contains a positive integral multiple of \(t\), with coefficient at most \(n-1\). Lemma 1 then forces the target angle.

Thus Mulan wins from every initial triangle, and from every nonterminal triangle she needs at most
\[
1+\lceil\log _2(n-1)\rceil \tag{2}
\]
cuts. This is genuine finite termination, not merely decrease of a real-valued quantity. When \(n=2\), the only interior mark is \(t\), and the construction produces coefficients \(k=n-k=1\), so both children already contain the target.

### 4. Nested finite-horizon attractors

For necessity, retain arbitrary \(t\in(0,1)\). Let
\[
W_0=\{(a,b,c)\in\Omega:\text{one of }a,b,c\text{ equals }t\}.
\]
For \(E\subseteq\Omega\), define
\[
\operatorname{Pre}(E)=\{S\in\Omega:\text{Mulan has a legal cut at }S
\text{ whose two children both belong to }E\}.
\]
The strict requirement \(0<x<a\), or its cyclic counterpart, is part of this definition. Define the nested sets
\[
W_{r+1}=W_r\cup\operatorname{Pre}(W_r). \tag{3}
\]

**Lemma 2 (finite horizon and finite victory).** A state lies in \(W_r\) if and only if Mulan has a strategy guaranteeing victory in at most \(r\) cuts from that state. Moreover, Mulan can guarantee victory in finitely many cuts from a fixed state if and only if that state belongs to \(\bigcup_{r\ge0}W_r\).

**Proof.** The first assertion follows by induction on \(r\). It is true for \(r=0\). If a state is in \(W_r\), induction gives a win within \(r\) cuts. If it is in \(\operatorname{Pre}(W_r)\), Mulan makes the witnessing cut; either retained child lies in \(W_r\), so induction gives at most \(r\) more cuts. Conversely, if a nonterminal state admits a strategy winning within \(r+1\) cuts, its first prescribed cut must leave, under either response, a child from which the continuation wins within \(r\) cuts. Both children lie in \(W_r\), so the parent lies in \(W_{r+1}\).

Membership in some \(W_r\) implies finite forced victory. Conversely, fix one initial state and one strategy which wins after finitely many cuts against every response sequence. Form its response tree: nodes are finite histories consistent with the strategy, and each nonterminal node has the two children corresponding to Shan-Yu's choices after the prescribed cut. If depths were unbounded, **König's infinity lemma** would give an infinite branch. In this binary setting, prove the lemma by repeatedly choosing a child below which nodes occur at arbitrarily large depths; one exists, for otherwise depth below the parent would be bounded. The resulting nested nodes form an infinite branch, a play on which the strategy never wins, contradiction. Thus this one tree has finite maximum depth \(R\), and the first assertion puts the initial state in \(W_R\). This supplies a bound only for the fixed state and strategy, not a global uniform bound. \(\square\)

### 5. The affine-thinness lemma

For finite \(K\subset\mathbb Z_{>0}\), let
\[
\mathcal H_K=\bigcup_{k\in K}\bigl(\{a=kt\}\cup\{b=kt\}\cup\{c=kt\}\bigr)\cap\Omega. \tag{4}
\]
Each equality describes a proper affine line in the two-dimensional plane \(a+b+c=1\), unless its intersection with \(\Omega\) is empty.

**Lemma 3 (finite-rank multiple-line lemma).** If
\[
1\ne mt\qquad\text{for every positive integer }m, \tag{5}
\]
then for every \(r\ge0\) there is finite \(K_r\subset\mathbb Z_{>0}\) such that \(W_r\subseteq\mathcal H_{K_r}\). One may take \(K_0=\{1\}\) and
\[
K_{r+1}=K_r\cup\{p+q:p,q\in K_r\}
\cup\{|p-q|:p,q\in K_r,\ p\ne q\}. \tag{6}
\]

**Proof.** The assertion for \(r=0\) is the definition of \(W_0\). Suppose it holds for \(r\), and consider a state in \(\operatorname{Pre}(W_r)\). By cyclic symmetry suppose the cut is from \(a\), with children (1). Each child belongs to \(\mathcal H_{K_r}\), so choose a coordinate equal to \(pt\) in \(C_1\) and one equal to \(qt\) in \(C_2\), where \(p,q\in K_r\).

If the chosen coordinate of \(C_1\) is its inherited angle \(b\), the parent satisfies \(b=pt\). If the chosen coordinate of \(C_2\) is inherited angle \(c\), the parent satisfies \(c=qt\). These cases put the parent in \(\mathcal H_{K_r}\). Otherwise there are exactly four ordered pairings:

1. \(x=pt\) and \(a-x=qt\), giving \(a=(p+q)t\).
2. \(x=pt\) and \(b+x=qt\), giving \(b=(q-p)t\). Since \(b>0\), \(q>p\).
3. \(1-b-x=pt\) and \(a-x=qt\). Since \(1-b=a+c\), subtraction gives \(c=(p-q)t\); since \(c>0\), \(p>q\).
4. \(1-b-x=pt\) and \(b+x=qt\), giving \(1=(p+q)t\), impossible by (5).

Thus every legal projected parent lies on a line indexed by (6). This is the full affine elimination: in Cases 1–3 eliminating \(x\) yields a proper parent line; in Case 4 the two equations can lose all restriction on the parent only through exactly \(1=(p+q)t\). The coefficient is positive and the coefficient of the total angle is one; no relation \(s=mt\) with \(s>1\), no zero or negative coefficient, and no unrelated identity occurs. Strict legality can only shrink the projection, and positivity excludes zero and wrongly signed differences.

There are finitely many old indices, three cut vertices, and finitely many ordered witness pairings, so (6) is finite. Since (3) retains \(W_r\), induction proves the lemma. \(\square\)

This identifies the exceptional dimension jump completely: only the supplementary pair \(1-b-x=pt\), \(b+x=qt\) can avoid forcing a parent multiple-line, and only when \(1=(p+q)t\).

### 6. Necessity and final verification

Assume (5). By Lemma 3, \(\bigcup_{r\ge0}W_r\) lies in a countable union of proper affine lines in \(\Omega\). Each is relatively closed with empty relative interior and hence nowhere dense. The **Baire category theorem**, relative to the nonempty open subset \(\Omega\) of the Euclidean plane \(a+b+c=1\), says this countable union cannot cover \(\Omega\).

Equivalently, an elementary witness exists on
\[
(a,b,c)=(s,s,1-2s),\qquad 0<s<\tfrac12.
\]
All multiple-lines exclude only countably many \(s\), namely values satisfying \(s=kt\) or \(1-2s=kt\) for some positive integer \(k\); a real interval is uncountable. Choose a state \(S\notin\bigcup_rW_r\). If Mulan had a finite-winning strategy from \(S\), Lemma 2, including its König-lemma direction, would put \(S\) in some \(W_r\), contradiction. Shan-Yu can therefore choose this initial triangle, so Mulan cannot guarantee victory.

Hence universal finite victory requires \(1=nt\) for some positive integer \(n\). Since \(0<t<1\), \(n\ge2\). Conversely, Sections 2–3 give an explicit legal finitely terminating strategy for every \(t=1/n\). Translating back gives
\[
\boxed{\theta=\frac{180^\circ}{n}\quad(n=2,3,4,\ldots)}.
\]
The construction and bound (2) verify every listed value, while Lemmas 2–3 exclude every unlisted real value. \(\blacksquare\)
