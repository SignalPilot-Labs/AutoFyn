## Lemmas: Element Bound, and the general $j=1$ Lower-Bound theorem for the geometric construction

### Lemma E (Element Bound)

**Statement.** For any finite multiset $S$ of positive reals and any
$x\in S$, $\mathrm{OddSum}(S)\ge x$.

**Proof (as given, verified correct).** Let $g=\max(S)$. By the Global-max
Peeling Lemma (`dominant-piece-lower-bound.md`),
$\mathrm{OddSum}(S)=g+\mathrm{EvenSum}(S\setminus\{g\})\ge g\ge x$ (using
$\mathrm{EvenSum}\ge0$ and $g=\max(S)\ge x$ since $x\in S$). This is a
strictly shorter proof than the builder's original case-split (which used
First-mover-half plus a uniqueness argument); both are valid, and the
statement is immediate once the Peeling Lemma is on hand.

**Independent verification.** Re-derived independently by the
proof-reviewer via the shorter route above; agrees with the builder's
(longer, also correct) proof.

### Theorem ($j=1$, arbitrary split, arbitrary tail refinement)

**Statement.** Fix $m\ge1$ and suppose $T(m-1)$ holds: for every $k'\le
m-1$ and every refinement of the unnormalized geometric partition
$\Gamma_{m-1}=(2^{m-1},\dots,2,1)$ using $\le k'$ cuts,
$\mathrm{OddSum}\ge2^{m-1}$. Then for every way XY splits the top piece
$T=2^m$ of $\Gamma_m$ into two positive fragments $t_1\ge t_2>0$ (an
arbitrary split) and refines the tail $\Gamma_{m-1}$ (scaled to total
$R=2^m-1$) with any $\le m-1$ further cuts, the resulting multiset $M$
satisfies $\mathrm{OddSum}(M)\ge 2^m$.

**Proof.** As given in `approaches/self-similar-induction-on-n.md`
(Step 1, Steps 1a–1d): the tail's own maximum after refinement is
$\le T/2$ (splitting never increases a piece's max fragment), so $t_1\ge
T/2\ge$ every element of the refined tail, making $t_1$ a global max;
peeling $t_1$ (Peeling Lemma) reduces the claim to
$\mathrm{OddSum}(\{t_2\}\cup S)\le R$, which is proved by a two-way case
split on $t_2$ vs. $s_1:=\max(S)$: if $t_2\le s_1$, peel $s_1$ and use
Lemma E on $t_2$; if $t_2>s_1$, peel $t_2$ and use the inductive
hypothesis $T(m-1,k-1)$ directly. Full algebra checked line by line by the
reviewer; matches.

**Independent verification.** Numerically re-derived by the proof-reviewer
via randomized brute-force search over splits $(t_1,t_2)$ and randomized
tail refinements, for $m=2$ (worst found $\mathrm{OddSum}=4.0$, matching
the bound exactly) and $m=3$ (worst found $\approx8.001$, matching
$2^3=8$ up to search resolution). No violation found.

**Caveat.** This theorem is conditional on the inductive hypothesis
$T(m-1)$ (for the *whole* tail refined with $\le m-1$ cuts, not a
sub-multiset with an element removed); it does **not** extend to $j\ge2$
cuts on the top piece by the same method — see the documented obstruction
("Lemma X′", not proved) in `approaches/self-similar-induction-on-n.md`.

**Source.** Proved in `approaches/self-similar-induction-on-n.md`
(round 2, Step 1 and the "Element Bound" lemma). Certified by the
proof-reviewer, round 2.

**Reuse.** Directly reusable as a certified building block: closes the
$j=1$ face of Lower-bound Case 2 (`current.md`'s open gap 1) in full
generality, conditional only on the one-level-down instance of the same
statement. Also directly closes $T(1)$ in full (combined with the $j=0$
case, `dominant-piece-lower-bound.md`), giving an alternative,
generalizable proof of $c(1)\ge2/3$'s lower-bound half.
