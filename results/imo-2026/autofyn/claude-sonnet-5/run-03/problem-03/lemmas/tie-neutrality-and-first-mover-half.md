## Lemmas: Tie-neutrality and first-mover-gets-half, for the alternating-claim game

Both facts below use the Greedy-Optimality Lemma
(`greedy-optimality-oddsum.md`): the first claimer's total on a finite
multiset $S$ sorted descending is $\mathrm{OddSum}(S)$.

### Lemma A (Tie-neutrality)

**Statement.** If two pieces in the multiset have exactly equal length $v$,
then (regardless of the rest of the multiset) exactly one of the two copies
of $v$ is claimed by the first-mover and the other by the second-mover.

**Proof.** Sort the multiset descending, keeping the two copies of $v$
adjacent (always possible: no other element can be strictly interposed
between two equal elements in a descending sort). The two copies occupy two
*consecutive* ranks $i,i+1$. Exactly one of any two consecutive integers is
odd; since the first-mover receives exactly the odd-ranked elements
(Greedy-Optimality Lemma), the two copies of $v$ split one to each player,
independent of $i$. $\blacksquare$

More generally, the same argument shows: a block of $k$ mutually-tied
elements occupying consecutive ranks $i,i+1,\dots,i+k-1$ contributes a total
to the first-mover that depends only on $i$ (the parity/count of
higher-ranked elements) and $k$ — not on which physical copies are assigned
to which internal rank — because $\mathrm{OddSum}$ sums by rank, and all
$k$ tied elements have the same value $v$, so the sum over any subset of
$\lceil k/2\rceil$ or $\lfloor k/2\rfloor$ of them (whichever the odd ranks
in the block pick out) is simply that count times $v$.

### Lemma B (First-mover gets at least half, zero extra splits)

**Statement.** For any finite multiset of positive reals with total sum
$W$, the first-mover's value $\mathrm{OddSum}\ge W/2$.

**Proof.** Sort descending $y_1\ge y_2\ge\cdots\ge y_m$. Pair
$(y_1,y_2),(y_3,y_4),\dots$ (an unpaired $y_m$ if $m$ is odd). Each pair
satisfies $y_{2i-1}\ge y_{2i}$ since sorted descending. First-mover's value
is $y_1+y_3+\cdots$, second-mover's is $y_2+y_4+\cdots$; summing the
pairwise inequalities (and noting any unpaired final term only adds to the
first-mover's side) gives first-mover's value $\ge$ second-mover's value.
Since the two sum to $W$, first-mover's value $\ge W/2$. $\blacksquare$

**Source.** Both proved in `approaches/universal-halving-adversary.md`
(Lemma 1, Lemma 2). Certified by the proof-reviewer, round 1.

**Reuse.** Tie-neutrality (including its generalized block form) is the
tool needed to correctly account for multi-way ties that arise in
self-similar / recursive constructions (e.g. when a bisected top piece ties
in value with an untouched sub-piece of the tail) — this is exactly the
kind of tie that appears, not fully rigorously handled, in the "$j=1$"
telescoping computation of `approaches/self-similar-induction-on-n.md`; the
generalized block form above closes that gap and should be invoked
explicitly there. Lemma B gives a cheap floor ($\ge W/2$) usable as a
sanity bound but is, by itself, insufficient to reach $c(n)$ for $n\ge2$.
