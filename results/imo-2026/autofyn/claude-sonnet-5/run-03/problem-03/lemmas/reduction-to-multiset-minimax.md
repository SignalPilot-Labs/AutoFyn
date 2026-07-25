## Lemma: Reduction of the two-phase stick game to a multiset minimax

**Statement.** In the original game (Liu Bang (LB) marks $\le n$ points on
$[0,1]$; Xiang Yu (XY), seeing LB's marks, marks $\le n$ further points; the
stick is cut at all marks; the pieces are then claimed alternately, LB
first, each maximizing own total), the value equals
$$c(n)=\max_{\substack{p_1,\dots,p_k>0\\ \sum p_i=1,\ k\le n+1}}\ \min_{\substack{\text{refinement of }\{p_i\}\text{ using}\\ \le n\text{ further cuts}}} \mathrm{OddSum}(\text{resulting multiset}),$$
where a "refinement using $\le n$ further cuts" means: choose non-negative
integers $m_1,\dots,m_k$ with $\sum m_i\le n$ and, for each $i$, split
$p_i$ into $m_i+1$ arbitrary positive pieces summing to $p_i$.

Moreover: (a) the value of the whole two-phase game depends only on the
multiset of final piece lengths, not on their order along the stick
(position-irrelevance); (b) the game played on a stick of length $L$ has
value exactly $L$ times the value of the same game on $[0,1]$
(scale-invariance).

**Proof.** By the Greedy-Optimality Lemma (see
`greedy-optimality-oddsum.md`), once the marking phase is finished, the
claiming phase's outcome under optimal play by both sides is exactly
$\mathrm{OddSum}$ of the final multiset of piece lengths — a fact that
depends only on that multiset, not on the pieces' positions on the stick;
this gives position-irrelevance directly, since marking a point only ever
splits one existing piece into two sub-pieces summing to the original
piece's length, an operation depending only on that piece's length.

It remains to identify which multisets are reachable at each stage. A
choice of $\le n$ marked points by LB partitions $[0,1]$ into some number
$k\le n+1$ of positive-length pieces (the gaps between $0$, the marks, and
$1$); conversely every composition of $1$ into $k\le n+1$ positive parts,
in any order, is realized by placing marks at the corresponding partial
sums — so LB's reachable set of "marking-phase outcomes" is exactly the set
of multisets $\{p_1,\dots,p_k\}$, $k\le n+1$, $\sum p_i=1$. Given such a
partition at specific positions, each of XY's $\le n$ further marks lands
inside exactly one current piece (marks are distinct, so a mark cannot
coincide with an existing one); a set of marks landing inside piece $i$
splits it into (number of marks in it)$+1$ sub-pieces of arbitrary positive
lengths summing to $p_i$, and marks in different pieces act independently.
Hence XY's reachable refinements, as multisets, are exactly those
parametrized by $m_1,\dots,m_k\ge0$, $\sum m_i\le n$, with arbitrary
positive lengths in each piece. Both players optimize the resulting
$\mathrm{OddSum}$ (LB maximizing at the outer level by choice of partition,
XY minimizing at the inner level by choice of refinement), giving exactly
the displayed minimax.

Scale-invariance: rescaling $[0,L]\to[0,1]$ by $x\mapsto x/L$ carries marks
to marks and pieces to pieces of proportionally scaled length; it is a
bijection between the two players' strategy spaces on the two sticks that
scales every resulting piece length, and hence every claimed total, by
$1/L$; consequently the value scales by $L$. $\blacksquare$

**Source.** Proved independently in `approaches/greedy-reduction-geometric.md`
(Lemma 2) and `approaches/self-similar-induction-on-n.md` (Lemma 2), and
used as a black box (with attribution) in
`approaches/universal-halving-adversary.md`. Certified by the
proof-reviewer, round 1.

**Reuse.** This is the standard reduction all three approaches build on; any
future approach to imo-2026-03 may cite it directly instead of re-deriving
it.
