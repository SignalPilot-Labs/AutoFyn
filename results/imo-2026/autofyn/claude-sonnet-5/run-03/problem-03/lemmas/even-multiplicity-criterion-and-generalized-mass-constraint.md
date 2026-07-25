# Even-Multiplicity Equality Criterion, and the Generalized Mass-Constraint Theorem

Certified round 17, from `approaches/lp-duality-split-polytope.md`, round-17
section. Independently re-verified by the proof-reviewer (own fresh
exact-`Fraction` scripts, not the builder's).

## Even-Multiplicity Equality Criterion

**Statement.** Let $M$ be a finite multiset of positive reals with
$\mathrm{sum}(M)=1$. Then $\mathrm{OddSum}(M)=\tfrac12$ if and only if $|M|$
is even and every distinct value occurring in $M$ has even multiplicity.

**Proof.** If $|M|$ is odd, $\mathrm{AltSum}(M)=\sum_{i=1}^t(v_{2i-1}-v_{2i})
+v_{2t+1}>0$ strictly (each bracket $\ge0$ by descending sort, last term
$>0$), so $\mathrm{OddSum}(M)>\tfrac12$ strictly — the floor is never attained
when $|M|$ is odd. If $|M|=2t$: $\mathrm{AltSum}(M)=\sum_{i=1}^t(v_{2i-1}-
v_{2i})=0$ iff $v_{2i-1}=v_{2i}$ for every $i$ (Property (P), since every
bracket is $\ge0$), and $\mathrm{OddSum}(M)=\tfrac12$ iff $\mathrm{AltSum}(M)
=0$ (from $\mathrm{OddSum}=\tfrac12(\mathrm{sum}+\mathrm{AltSum})$). Grouping
the sorted sequence into maximal equal-value blocks with multiplicities
$m_1,\ldots,m_r$: if every $m_j$ is even, every block boundary $R_j$ is even,
so every odd rank $p$ within a block is paired with the next (even) rank in
the same block, giving Property (P). Conversely if some $m_{j_0}$ is odd, the
first index $j_0$ where the running sum $R_{j_0}$ turns odd marks a block
ending at an odd rank, whose next rank starts a new (distinct-valued) block —
an unequal Property-(P) pair, so (P) fails. $\blacksquare$

**Reviewer independent re-verification.** Own fresh script
(`verify_evenmult.py`): $30{,}000$ trials (half forcing even multiplicities,
half unconstrained random multisets, all normalized to sum $1$): zero
mismatches between the criterion's prediction and direct computation of
$\mathrm{OddSum}$.

## Generalized Mass-Constraint Theorem

**Statement.** Let $p_1,\ldots,p_N$ be any legal adversary partition,
$S\subseteq\{1,\ldots,N\}$ the active (split) pieces, $U$ the untouched
pieces, with $\{p_i:i\in U\}$ pairwise distinct. If a response's fragment
multiset $M$ (untouched pieces $\cup$ all fragments) attains
$\mathrm{OddSum}(M)=\tfrac12$ exactly, then $\sum_{i\in U}p_i\le\tfrac12\le
\sum_{j\in S}p_j$ — with **no assumption on the splitting mechanism** (any
number of fragments per active piece, any tie structure).

**Proof.** By the Even-Multiplicity Criterion, every distinct value of $M$
has even multiplicity $\ge2$; for $i\in U$, $p_i$ (occurring once as the
untouched piece) must therefore occur at least once more, as a fragment of
some active piece $h(i)\in S$ (a "match," well-defined since the $p_i$,
$i\in U$, are pairwise distinct, so a single fragment matches at most one
$i$). Grouping $U$ by host, $K_j:=\{i\in U:h(i)=j\}$: the match-fragments for
$K_j$ are pairwise-distinct nonnegative reals among piece $j$'s fragments,
which sum to exactly $p_j$, so $\sum_{i\in K_j}p_i\le p_j$. Summing over
$j\in S$ gives $\sum_{i\in U}p_i\le\sum_{j\in S}p_j$; combined with
$\sum_{i\in U}p_i+\sum_{j\in S}p_j=1$, this gives $\sum_{i\in U}p_i\le\tfrac12
\le\sum_{j\in S}p_j$. $\blacksquare$

**Why this strictly generalizes the certified `rank-pinning-lemma-and-mass-
constraint-theorem.md` Mass-Constraint Theorem**: that theorem is proved only
for the specific Multi-Piece Subset-Tie construction family; this one applies
to *any* legal response attaining the floor exactly, via a construction-free
mass-counting argument.

**Application at $e_0$ (independently re-verified exact closed form and
table).** At $e_0$ ($p_i=a+(N-i)\delta$, $\delta=1/(2^N-1)$, $N=n+1$,
certified `lemmas/finite-cell-vertex-reduction-and-region-classification.md`),
the bottom-$m$ mass ($m=N-s$) is $\tfrac mN-\delta\cdot\tfrac{m(N-m)}2$, and
the floor is attainable with $s$ active pieces only if this is $\le\tfrac12$.
Reviewer independently re-derived and re-verified this closed form (own
script, `verify_table.py`) against direct construction of $e_0$'s
coordinates, for $n=3,\ldots,20$ (54 instances: exact match), and reproduced
the file's full requested table at $n=8,9,10$, $s=n-2,n-3,n-4$ digit-for-digit
(9 exact fractions, e.g. $n=8,s=4$: bottom-$5$ mass $2465/4599>1/2$ — the one
genuine rule-out; all others $<1/2$, no obstruction).

**Honest scope (unchanged from the file, correctly not overclaimed).** This
proves $s\gtrsim N/2$ necessary for floor-attainment at $e_0$ — a genuinely
new, general bound — but is asymptotically far weaker than the conjectured
$s\ge n-1$ necessity (for any fixed $m$, the bottom-$m$ mass $\to0$ as
$N\to\infty$, so this technique alone cannot close that gap). Does not
establish the general $s\ge n-1$ conjecture.
