## Status
partial

## Approaches tried
- Round 1: dyadic reserve induction with initial gaps proportional to \(1,2,4,\ldots,2^n\) — the drafting reduction, discrepancy reformulation, exact effect of an arbitrary refinement, legality/compactification setup, and the complete case \(n=1\) are proved below. The proposed all-\(n\) dyadic reserve inequality and matching universal refinement inequality remain open; no invariant presently written here proves either one, so this attempt does not claim the conjectured formula for \(n>1\).

## Current best
For every fixed final multiset of piece lengths, finite backward induction proves that optimal drafting gives Liu Bang exactly the odd-ranked sum. Consequently his payoff is
\[
 P(B)=\frac{1+D(B)}2,
 \qquad D(B)=b_1-b_2+b_3-b_4+\cdots,
\]
where \(b_1\ge b_2\ge\cdots\), and a terminal zero is appended algebraically when necessary. The layer-cake formula
\[
 D(B)=\int_0^\infty \bigl(N_B(t)\bmod 2\bigr)\,dt
\]
is proved, as is the exact statement that a legal split \(x=u+v\), \(0<u\le v\), toggles threshold parity precisely on \((0,u]\cup(v,x]\), up to endpoints. These statements include ties, arbitrary real cuts, and repeated cuts of a daughter piece.

The complete answer for the base case is \(c_1=2/3\), with both players' strategies proved for one or two Liu-parent intervals.

For general \(n\), put \(Q=2^{n+1}-1\). Liu can legally create parent intervals of lengths \(1/Q,2/Q,\ldots,2^n/Q\). To complete this route one must still prove both of the following quantified refinement statements:

1. every provenance-respecting refinement of \(\{1,2,\ldots,2^n\}\) by at most \(n\) binary splits has sorted alternating discrepancy at least \(1\);
2. for every collection of at most \(n+1\) positive parent lengths of total \(1\) and every \(\varepsilon>0\), there is a legal provenance-respecting refinement by at most \(n\) cuts with discrepancy at most \(1/Q+2\varepsilon\).

The reserve phrases in the outline do not yet constitute proofs of these assertions: an arbitrary real split may move both daughters across many sorted ranks, and a later split must act on a current daughter rather than on its original parent. Establishing these two statements is the explicit remaining gap.

## Promotable lemmas
- **Greedy drafting lemma.** For a finite multiset \(b_1\ge\cdots\ge b_m\ge0\), in the alternating take-one game with the first player moving first and both players maximizing their own total, the first player's minimax value is \(b_1+b_3+b_5+\cdots\). Ties do not affect the value. Proved below, Lemma 1.
- **Alternating discrepancy layer-cake lemma.** For any finite multiset \(B\) of nonnegative reals, its sorted alternating discrepancy is the measure of the thresholds at which an odd number of elements of \(B\) reach the threshold. Proved in Lemma 2.
- **Single-refinement toggle lemma.** Replacing one current piece \(x\) by positive daughters \(u\le v\), \(u+v=x\), toggles threshold-count parity exactly on \((0,u]\cup(v,x]\), up to a null set, whether or not the piece is an original parent. Proved in Lemma 3.
- **Exact solution for one mark.** In the stated game with \(n=1\), the largest guaranteed share is \(2/3\). Proved in Lemma 4.

### Rigorous progress

We record all reductions carefully because they remain valid infrastructure for either missing refinement inequality.

**Lemma 1 (greedy drafting, by finite backward induction).** Let \(b_1\ge b_2\ge\cdots\ge b_m\ge0\) be the lengths of the pieces when marking is over. In the ensuing zero-sum drafting game, the first player's value is
\[
O(B):=b_1+b_3+b_5+\cdots.
\]
In particular, taking a currently longest piece is optimal at every position.

**Proof.** We induct on \(m\). The assertion is immediate for \(m=0,1\). Suppose it is known for every multiset of \(m-1\) pieces. Let
\[
E(B):=b_2+b_4+b_6+\cdots;
\]
thus the total length is \(O(B)+E(B)\).

If the first player takes \(b_1\), the opponent becomes the first player in the game on \(b_2,\ldots,b_m\). By the induction hypothesis, the opponent receives \(b_2+b_4+\cdots=E(B)\). Hence the original first player receives \(O(B)\).

It remains to prove that no other first move gives more. Suppose the first player removes \(b_j\). By the induction hypothesis, the opponent receives the odd-ranked sum of the remaining sorted list. If \(j=2q+1\) is odd, that sum is
\[
 b_1+b_3+\cdots+b_{2q-1}+b_{2q+2}+b_{2q+4}+\cdots.
\]
For each \(i=1,\ldots,q\), we have \(b_{2i-1}\ge b_{2i}\). Therefore the displayed sum is at least
\[
 b_2+b_4+\cdots+b_{2q}+b_{2q+2}+b_{2q+4}+\cdots=E(B).
\]
If \(j=2q\) is even, the opponent's odd-ranked sum is again
\[
 b_1+b_3+\cdots+b_{2q-1}+b_{2q+2}+b_{2q+4}+\cdots,
\]
and the same termwise inequalities \(b_{2i-1}\ge b_{2i}\), now for \(i=1,\ldots,q\), show that it is at least \(E(B)\). Thus after any first move the opponent can obtain at least \(E(B)\), so the original first player can obtain at most \(O(B)\). Taking \(b_1\) attains this bound.

All comparisons used are non-strict. Hence repeated equal lengths may create several optimal moves, but do not change the value. Applying the same argument after every history proves that choosing any currently longest piece is an optimal strategy. \(\square\)

Define the **sorted alternating discrepancy** by
\[
D(B):=b_1-b_2+b_3-b_4+\cdots.
\]
If \(m\) is odd, we may append one zero solely in this algebraic definition; no zero-length physical piece is introduced. Since the actual pieces have total length \(1\), Lemma 1 gives
\[
 2P(B)=(b_1+b_2+\cdots+b_m)+(b_1-b_2+b_3-b_4+\cdots)=1+D(B),
\]
and hence
\[
\boxed{P(B)=\frac{1+D(B)}2}. \tag{1}
\]
Grouping consecutive terms also shows \(D(B)\ge0\), because \(D=(b_1-b_2)+(b_3-b_4)+\cdots\), with a final nonnegative unpaired term if necessary. In particular Liu always gets at least \(1/2\).

**Lemma 2 (layer-cake formula).** For \(t>0\), let
\[
N_B(t):=\#\{i:b_i\ge t\}.
\]
Then
\[
D(B)=\int_0^\infty \mathbf 1_{\{N_B(t)\text{ is odd}\}}\,dt. \tag{2}
\]

**Proof.** The elementary layer-cake identity \(b_i=\int_0^\infty \mathbf 1_{\{t\le b_i\}}dt\) and finite linearity of the integral give
\[
D(B)=\int_0^\infty \sum_{i=1}^m(-1)^{i+1}\mathbf 1_{\{t\le b_i\}}\,dt.
\]
Because the \(b_i\) are nonincreasing, for a fixed \(t\) the indicators in this sum consist of exactly \(N_B(t)\) initial ones followed by zeros. Their alternating sum is \(1\) when \(N_B(t)\) is odd and \(0\) when it is even. This proves (2). The convention at the finitely many thresholds \(t=b_i\) does not affect the integral. \(\square\)

**Lemma 3 (exact effect of one arbitrary split).** Suppose a current piece of length \(x\) is split into two positive pieces \(u,v\), where without loss of generality \(0<u\le v\) and \(u+v=x\). Let \(B'=(B\setminus\{x\})\cup\{u,v\}\). Then, away from the three endpoints \(u,v,x\), the parity of \(N_{B'}(t)\) differs from that of \(N_B(t)\) exactly for
\[
 t\in(0,u)\cup(v,x). \tag{3}
\]
Equivalently, if \(E(B)=\{t>0:N_B(t)\text{ is odd}\}\), then up to a set of measure zero,
\[
E(B')=E(B)\mathbin{\triangle}\bigl((0,u]\cup(v,x]\bigr), \tag{4}
\]
where \(\triangle\) denotes symmetric difference.

**Proof.** Contributions of all pieces other than the split piece are unchanged. For \(0<t<u\), the old piece contributes one to \(N_B(t)\), whereas both daughters contribute, so the count changes by one modulo \(2\). For \(u<t\le v\), both the old piece and only the daughter \(v\) contribute, so parity does not change. For \(v<t<x\), the old piece contributes and neither daughter does, so parity changes. For \(t>x\), none of the three contributes. This proves (3) and (4); endpoint choices are irrelevant to measure. \(\square\)

This lemma is provenance-safe. If Xiang later cuts a daughter produced by an earlier cut, that daughter is simply the “current piece” \(x\) in the lemma. Thus repeated cuts in one Liu interval are covered, but only through the actual current daughter selected at each step; (4) does not license an abstract toggle unrelated to an existing piece.

For reference, the dyadic proposal is legally realizable. Set
\[
Q:=1+2+\cdots+2^n=2^{n+1}-1.
\]
Liu marks the \(n\) points
\[
 \frac1Q,\quad \frac{1+2}{Q},\quad\ldots,\quad \frac{1+2+\cdots+2^{n-1}}Q.
\]
They are strictly increasing and lie strictly between \(0\) and \(1\), and the resulting parent lengths are \(1/Q,2/Q,\ldots,2^n/Q\). The unresolved lower-bound assertion is exactly that every sequence of at most \(n\) applications of Lemma 3 to this multiset leaves \(D\ge1/Q\). Neither (2) nor (4) alone implies this, because a symmetric-difference toggle can increase or decrease the measure according to its overlap with the current odd-threshold set.

**Lemma 4 (the complete base case \(n=1\)).** The answer for one permitted mark per player is
\[
\boxed{c_1=\frac23}.
\]

**Proof: Liu's guarantee.** Liu marks the point \(1/3\), producing parent pieces of lengths \(1/3\) and \(2/3\). If Xiang makes no mark, Liu takes the longer piece and gets \(2/3\).

If Xiang cuts the parent of length \(1/3\), the final lengths are \(2/3,u,1/3-u\), where \(0<u<1/3\). The \(2/3\)-piece is largest; by Lemma 1 Liu gets it and also the smaller of the two other pieces, so his payoff is at least \(2/3\).

If Xiang cuts the parent of length \(2/3\), write its positive daughters as \(u,v\), where \(u+v=2/3\). The final pieces are \(1/3,u,v\). For three numbers of total \(1\), the odd-ranked sum equals \(1\) minus the median. The median is at most \(1/3\): if both \(u,v\le1/3\), this is immediate; otherwise exactly one of \(u,v\) exceeds \(1/3\) (they cannot both exceed it because their sum is \(2/3\)), and then the median is \(1/3\). Hence Liu again receives at least \(2/3\). These cases exhaust Xiang's legal choices.

**Proof: Xiang's upper response.** First suppose Liu marks once, producing positive lengths \(a\ge b\) with \(a+b=1\).

If \(b<1/3\), then \(a>2/3\). Xiang cuts the \(a\)-parent into pieces of lengths \(1/3\) and \(a-1/3\), both positive. The three final lengths are \(b,1/3,a-1/3\), and both \(1/3\) and \(a-1/3\) are at least \(1/3\). Thus the median is \(1/3\), so Liu's payoff is \(1-1/3=2/3\).

If \(b\ge1/3\) and \(a>b\), choose any \(0<\delta<\min\{a-b,1/3\}\) and cut the \(a\)-parent into \(a-\delta\) and \(\delta\). Then \(a-\delta>b>\delta\), so the median is \(b\ge1/3\), and Liu's payoff \(1-b\) is at most \(2/3\).

The only remaining tied case is \(a=b=1/2\). Xiang cuts either parent into \(1/3\) and \(1/6\). The final lengths are \(1/2,1/3,1/6\), so Liu gets \(1/2+1/6=2/3\).

Finally, if Liu uses no mark, Xiang marks at \(1/3\), creating pieces \(1/3\) and \(2/3\), and Liu receives exactly \(2/3\). All marks used above are strictly interior. When Liu has marked once, Xiang cuts in the interior of one of Liu's intervals, so Xiang's point is automatically distinct from Liu's point. Thus the responses are legal. The lower and upper bounds coincide, proving \(c_1=2/3\). \(\square\)

### Quantifiers needed for any future completion

Suppose the missing universal refinement statement is eventually established only on the closure of the cut-configuration space, where a daughter is permitted to have length zero. It is not legitimate to call that closed minimizer a legal Xiang strategy. What is sufficient is the following explicit approximation conclusion:

> For every fixed legal Liu marking and every \(\varepsilon>0\), Xiang has a legal set of at most \(n\) distinct interior marks for which Liu's drafting payoff is at most \(2^n/(2^{n+1}-1)+\varepsilon\).

Indeed, if \(c>2^n/(2^{n+1}-1)\), choose \(0<\varepsilon<c-2^n/(2^{n+1}-1)\). The displayed response gives Liu strictly less than \(c\), so Liu cannot guarantee \(c\). This is the correct infimum quantifier; attainment of the closed minimum is unnecessary.

A perturbation argument, when available, must preserve provenance: each zero daughter is replaced by a sufficiently small positive daughter inside the same current parent, and all resulting cut positions must be chosen distinct from the finitely many existing marks. The payoff is continuous in the labeled daughter lengths: every order statistic is continuous (indeed, \(k\)-th largest equals the maximum, over all \(k\)-subsets, of the minimum on that subset), and the payoff is a finite sum of order statistics. Therefore a sufficiently small legal perturbation changes the payoff by less than any prescribed \(\varepsilon\). This observation handles legality once a valid closed-polytope construction has been supplied, but it does not supply the missing construction itself.
