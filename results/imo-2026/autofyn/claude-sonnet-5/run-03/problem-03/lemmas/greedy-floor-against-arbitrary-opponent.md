## Lemma: Greedy-floor guarantee against an arbitrary (non-optimal) opponent

**Statement.** Let $N$ be a finite multiset of positive reals. If Player 1
plays "always claim a currently-largest unclaimed element of $N$" on every
one of its own turns, then, **regardless of Player 2's strategy** (not
assumed optimal, not even assumed rational), Player 1's total is
$\ge \mathrm{OddSum}(N)$. Symmetrically, if Player 2 plays greedily on
every one of its turns while Player 1 plays arbitrarily, Player 2's total
is $\ge \mathrm{EvenSum}(N)$.

This strictly generalizes the Greedy-Optimality Lemma
(`greedy-optimality-oddsum.md`), which only asserts equality when *both*
players play optimally; here only one side is required to be greedy, and
the bound still holds against an arbitrary (adversarial or not) opponent.

**Proof.** Uses only the inequality $(\ast)$ from the proof of
Greedy-Optimality (`greedy-optimality-oddsum.md`): for any finite multiset
$S$ sorted descending $x_1\ge\cdots\ge x_m$ and any index $i$,
$\mathrm{EvenSum}(S)\le\mathrm{OddSum}(S\setminus\{x_i\})$ — a purely
combinatorial fact about sorted lists, with no assumption on optimal play,
so it is legitimate to reuse against an adversarial (not-necessarily-optimal)
opponent.

Induct on $m=|N|$. Base cases $m=0$ (both totals $0$) and, implicitly,
$m=1$ (Player 1 takes the unique element, total $=x_1=\mathrm{OddSum}(N)$)
are immediate.

Inductive step, $m\ge2$ (reducing by $2$ per full round): Player 1's first
move takes $g=\max(N)$ (any copy if tied). Player 2 then claims an
*arbitrary* element $x_i$ of $N\setminus\{g\}$. It is Player 1's turn again
on $N\setminus\{g,x_i\}$ (size $m-2$), with Player 1 still committed to
greedy and Player 2 still arbitrary. By the inductive hypothesis, Player
1's total from this point on is $\ge\mathrm{OddSum}(N\setminus\{g,x_i\})$.
Hence Player 1's total overall is
$$\ge g+\mathrm{OddSum}\bigl(N\setminus\{g,x_i\}\bigr)=g+\mathrm{OddSum}\bigl((N\setminus\{g\})\setminus\{x_i\}\bigr)\overset{(\ast)}{\ge} g+\mathrm{EvenSum}(N\setminus\{g\})=\mathrm{OddSum}(N),$$
the last equality being the Global-max Peeling Lemma
(`dominant-piece-lower-bound.md`). This holds for the arbitrary $x_i$
Player 2 chose, proving the first statement. The second (roles swapped)
follows by the identical induction with mover roles exchanged.
$\blacksquare$

**Independent verification.** Re-derived from scratch by the proof-reviewer
(round 2), confirming both the induction structure and the reuse of
inequality $(\ast)$ is valid (it does not depend on which player is
"optimal").

**Caveat (important, documented by the builder and confirmed by the
reviewer).** This lemma alone is *not* sufficient to prove a composite
"priority" strategy (e.g. LB statically clearing one region of the
multiset before another) achieves the *global* value $\mathrm{OddSum}$ of
the *whole* multiset when the region boundary is artificial: an exact
game-tree counterexample (verified by the reviewer, $n=3$,
$Q=\{2/15,2/15,2/15,2/15\}$, $Y=\{1/15,2/15,4/15\}$) shows a
"clear $Q$ before $Y$" static-priority strategy achieves only $7/15$,
strictly below the true value $9/15$ and below the target $c(3)=8/15$.
So this lemma gives a valid floor for greedy-on-the-whole-multiset, but
does **not** license splitting the multiset into pieces and applying it
piecewise with a fixed priority order between the pieces.

**Source.** Proved in `approaches/greedy-reduction-geometric.md`
(Section 4b, Lemma 4), round 2. Certified by the proof-reviewer, round 2.

**Reuse.** Directly reusable wherever a floor guarantee is needed against
an opponent not known/assumed to play optimally (e.g. as a building block
in a genuine interleaving argument), but must not be used as a shortcut to
avoid the true interleaved-sort analysis of a split multiset.
