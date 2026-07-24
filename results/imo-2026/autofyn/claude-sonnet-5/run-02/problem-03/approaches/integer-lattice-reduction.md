## Status
unsolved

## Approaches tried
- **Round 6 (this build).** Carried out the outline's Step 1 (integer
  rescaling setup) and Step 2 (the "rationality sub-lemma") in full, with a
  genuine, checkable result: a **correct general Rationality Lemma** (every
  vertex of the polyhedral cell decomposition has rational fragment values)
  is proved, but the **sharper conjectured form the outline asked for
  ("denominator dividing $D$") is FALSE**, refuted by an explicit,
  fully-worked, exact-fraction counterexample embedded in the legal $n=2$
  ladder composition space (not a numerics-only claim — a closed-form
  fragment value $4/21$ at a fully legal vertex, with $21\nmid 7=D$ and
  $7\nmid21$ either way other than the trivial $D\mid 21$ direction, which is
  the wrong direction for the claim). This pins down *exactly* why the
  outline's "easy win" sub-lemma is not automatic: vertices with **three or
  more simultaneously tied fragments inside one piece** (available whenever
  a piece receives $\ge2$ of Xiang Yu's cuts) introduce denominator factors
  equal to the tie's multiplicity, which need not divide $D=2^{n+1}-1$ (a
  Mersenne number, coprime to every integer $2\le k\le n+1$ whenever $k$
  shares no factor with $D$ — e.g. $D=7$ is coprime to $3$). This is a
  genuine, reviewer-checkable negative finding, not a guess.
  Consequently attempted a **repaired, weaker rationality statement**
  (denominator divides $D\cdot L$, $L=\mathrm{lcm}$ of the vertex's
  tie-multiplicities) — proved. Then attempted Step 3 (the digit/carry
  evaluation of $(\star\star)$'s window integral) on the *restricted* locus
  of "binary-tree" refinements (every tie-multiplicity a power of $2$),
  reasoning informally that an exact bisection of a tail piece should leave
  the parity of $N_{G'}(x)$ unchanged at every point (since it replaces one
  value by an *even* number, $2$, of equal half-value copies). **This
  informal claim is false, and direct exact-`Fraction` computation refutes
  it**: bisecting a single tail piece of an otherwise-unrefined $n=4$ ladder
  tail changes the window integral $\int_{W\cap[0,r)}v\,dt$ from $5/31$ to
  either $3/31$, $7/31$, $5/31$, or $6/31$ depending on *which* tail piece is
  bisected — sometimes decreasing, sometimes strictly *increasing* (§4
  below has the full computation). So even the restricted binary-tree case
  of Step 3 does not reduce to the unrefined-tail case as hoped; the digit
  model does not transplant even under the outline's own best-case
  simplifying assumption. Reporting this as the wall reached this round:
  real progress on Steps 1–2 (one genuinely reusable lemma, one genuine
  refutation redirecting future work), Step 3 attempted and its natural
  first approach (parity-invariance under bisection) is now refuted by
  explicit computation rather than left as an untested hope, Step 4 not
  reached.

## Current best
Two proved, reusable facts (§§1–2 below): the **General Rationality Lemma**
for vertices of the polyhedral cell decomposition (Cramer's-rule argument,
fully general, no restriction to the ladder or to minimizers), and a
concrete **refutation** of the stronger "denominator divides $D$" form
conjectured in the round-6 outline, together with the **repaired weaker
form** (denominator divides $D\cdot L$). Also a concrete, computation-backed
**refutation of Step 3's natural first attempt** (§4): exact bisection of a
tail piece does *not* leave the window integral $\int_{W\cap[0,r)}v\,dt$
invariant, so the hoped-for reduction of the binary-tree-refinement case to
the already-solved unrefined-tail case fails, and no positive digit/carry
formula for $(\star\star)$ was found this round.

## Full proof
(absent — Status is `unsolved`; $(\star\star)$ from
`rank-tie-vertex-reduction.md` §5.1 remains open, and this approach's own
Step 3/4 gap is a genuinely new sub-obstruction, not merely a restatement)

---

## 1. Setup: the integer rescaling (outline Step 1)

Fix $n\ge1$ and let $D:=2^{n+1}-1$. The ladder is $p_i:=2^{n+1-i}/D$ for
$i=1,\dots,n+1$; indeed
$$\sum_{i=1}^{n+1}p_i=\frac1D\sum_{i=1}^{n+1}2^{n+1-i}=\frac1D\sum_{k=0}^{n}2^k
=\frac{2^{n+1}-1}{D}=1,$$
confirming the ladder is a legal length-$1$ marking, and after multiplying
every quantity in the game by $D$, the ladder pieces become the exact
integers
$$q_i:=D\,p_i=2^{n+1-i},\qquad i=1,\dots,n+1,\qquad\{q_1,\dots,q_{n+1}\}
=\{2^n,2^{n-1},\dots,2,1\}.$$
Since $A(\cdot)$ and $\Phi(\cdot)=(1+A)/2$ are homogeneous of degree $1$
in the multiset's values (immediate from the definition: sorting is
scale-invariant, and $A$ is a fixed $\pm1$-signed sum of the sorted
values), $A(D\cdot S)=D\cdot A(S)$ for every multiset $S$, so proving
any inequality of the form $A(S)\ge f(n)$ is equivalent to proving
$A(D\cdot S)\ge D\cdot f(n)$ in the rescaled model — the rescaling changes
nothing about which inequality must be proved, only the units in which it
is stated, and it makes the ladder pieces literal integers. This is the
outline's Step 1; the substantive question, per the outline, is whether an
**arbitrary legal refinement** of these pieces (i.e. every fragment
appearing at every possible vertex of $\bar\Omega$, not just the unrefined
ladder itself) also lands on integers, or at least on a controlled set of
rationals — this is Step 2, addressed next.

## 2. The Rationality Lemma (outline Step 2, general form — proved)

**Lemma R1 (General Rationality).** Fix any Liu Bang configuration
$p_1,\dots,p_{n+1}\in\mathbb Q$ and any legal cut-budget composition
$(c_1,\dots,c_{n+1})$. Every vertex of the polyhedral cell decomposition of
$\bar\Omega=\prod_i\bar\Delta^{c_i}(p_i)$ described in
`vertex-minimum-theorem` (cut out by $d$ independent constraints, each of
type (I) "fragment $=0$" or type (II) "fragment $=$ fragment") has **all
fragment coordinates in $\mathbb Q$**.

*Proof.* Fix a vertex $V$ and let $d=\sum_i c_i$ be the total number of free
parameters (each piece's simplex $\bar\Delta^{c_i}(p_i)$ has dimension
$c_i$, since it is the set of $(c_i+1)$-tuples of nonnegative reals summing
to the fixed rational $p_i$ — so choosing $c_i$ of the $c_i+1$ fragment
values freely determines the last by subtraction from $p_i$; we use exactly
this affine coordinatization, one free coordinate per piece-with-a-cut,
dropping one fragment per piece as the dependent one). In these $d$
free coordinates $y=(y_1,\dots,y_d)\in\mathbb R^d$, every *other* fragment
(the ones not chosen as free coordinates) is an affine function of $y$ with
**rational** coefficients: it is either literally one of the $y_j$, or it is
$p_i-\sum(\text{the other free coordinates of piece }i)$, a rational affine
combination since $p_i\in\mathbb Q$. Consequently every type-(I) constraint
"fragment $=0$" and every type-(II) constraint "fragment $=$ fragment" is,
after substituting these affine expressions, a **linear equation in $y$ with
rational coefficients and rational constant term**. By definition of a
$0$-dimensional vertex of the arrangement, $V$ is cut out by exactly $d$
such equations that are linearly independent (as a system in $y$); write
this system as $My=b$ with $M\in\mathbb Q^{d\times d}$ invertible,
$b\in\mathbb Q^d$. Then $y=M^{-1}b\in\mathbb Q^d$ (a rational matrix's
inverse, when it exists, is rational — Cramer's rule: each entry of
$M^{-1}$ is a ratio of a cofactor to $\det M$, both polynomial, hence
rational, functions of $M$'s rational entries), so every free coordinate is
rational, and hence (by the affine formulas above, all with rational
coefficients) so is every fragment. $\blacksquare$

This is fully general: no ladder-specific structure, no restriction to
minimizing vertices — it applies to *every* vertex of *every* legal
composition, for *every* rational Liu Bang configuration. In particular it
applies to the auxiliary problem actually needed for $(\star\star)$: since
$(\star\star)$ must hold for the *worst case over all legal tail
refinements* $G'$ (not merely a $\Phi$-minimizing one — re-reading
`rank-tie-vertex-reduction.md` §5.1, the Cross-Term Reduction Theorem's
hypothesis is "$G'$ an *arbitrary* legal refinement"), the relevant
polytope is $\bar\Omega_{\text{tail}}$ (legal refinements of the tail
$T=\{p_2,\dots,p_{n+1}\}$ under any composition using $\le n-1$ cuts), and
the function being extremized is $t\mapsto\int_{W\cap[0,r)}v_{G'}(t)\,dt$
where $v_{G'}$ is the odd-parity indicator of $G'$. This function is
piecewise-linear in the fragment coordinates of $G'$ by the same
argument as $\Phi$'s piecewise-linearity in `vertex-minimum-theorem` (fixing
the sorted order and the position of $W$'s endpoints relative to the sorted
values makes the integral a fixed linear combination of fragment lengths),
so its extrema over $\bar\Omega_{\text{tail}}$ are likewise attained at
vertices of the same kind of cell decomposition, to which Lemma R1 applies
verbatim. **So: every fragment value that can ever be adversarially chosen
to maximize the window integral is rational.** This much of the outline's
premise is solid.

## 3. Refutation of the sharper "denominator divides $D$" sub-lemma

The outline's Step 2 conjectured the sharper statement that every such
fragment value lies in $\tfrac1D\mathbb Z$ (equivalently: after the
rescaling of §1, every fragment value is an *integer*). This is what would
make Step 3's clean binary-digit/carry model apply without further work.
**This sharper form is false**, and the following is a fully worked,
non-numerical counterexample (verified once by hand below, and
independently cross-checked by an exact-`Fraction` script with zero
discrepancy).

**Counterexample.** Take $n=2$ ($D=2^3-1=7$, ladder $p_1=4/7,\,p_2=2/7,\,
p_3=1/7$). Xiang Yu's budget is $2$ cuts total. Consider the legal
composition $c_1=2,\,c_2=c_3=0$ (both cuts spent on $p_1$, tail untouched),
and within $p_1$'s simplex $\bar\Delta^2(p_1)$ (dimension $2$: three
fragments $y_1,y_2,y_3\ge0$, $y_1+y_2+y_3=p_1$) take the vertex cut out by
the two independent type-(II) constraints $y_1=y_2$ and $y_2=y_3$ — a
genuine vertex of the arrangement in the sense of `vertex-minimum-theorem`
($d=c_1=2$ free parameters for this piece, $2$ independent tie constraints,
matching). Solving:
$$y_1=y_2=y_3=\frac{p_1}{3}=\frac{4/7}{3}=\frac{4}{21}.$$
The denominator of $4/21$ (in lowest terms, $\gcd(4,21)=1$) is $21$, and
$21\nmid7=D$ (indeed $D\mid21$ is the only divisibility relation between
them, and it is the wrong direction — the claim requires the fragment's
denominator to divide $D$, not the reverse). Equivalently, after the $\times
D=\times7$ rescaling of §1, this fragment's value is $7\cdot4/21=4/3$,
**not an integer** — directly refuting "every refinement lands on the
integer lattice $\{2^n,\dots,1\}$-generated model."

This composition is fully legal (uses exactly the $n=2$ budget of $2$
cuts, both on $p_1$, tail untouched) and the resulting vertex is a genuine
vertex of $\bar\Omega$ per `vertex-minimum-theorem`'s own definition (cut
out by $2$ independent type-(II) constraints matching the free-parameter
count of the piece being cut) — so this is not an edge case excluded by the
theorem's hypotheses. (For completeness, and to confirm no accidental
contradiction with already-certified work: the resulting multiset is
$\{4/21,4/21,4/21,2/7,1/7\}=\{6/21,4/21,4/21,4/21,3/21\}$ sorted
descending $6/21,4/21,4/21,4/21,3/21$, giving $\Phi=6/21+4/21+3/21=13/21
>12/21=4/7=c(2)$ — strictly above the target, so this vertex is *not* a
$\Phi$-minimizer and there is no tension with the fully-certified $c(2)=4/7$
result; it is offered here purely as a counterexample to the *rationality*
sub-lemma, which the outline stated for "every tie vertex," not only
minimizing ones.)

**Root cause, stated precisely.** In the proof of Lemma R1, the matrix $M$
for a vertex with a $k$-way tie inside one piece (i.e. $k$ fragments of a
single piece all forced equal by $k-1$ independent type-(II) constraints)
has, in the relevant $(k-1)\times(k-1)$ block, the sub-matrix of a
"consecutive difference" system whose solution divides that piece's total
by $k$ exactly (as in the worked example: $3$-way tie $\Rightarrow$ divide
by $3$). This $k$ can be **any integer $2\le k\le c_i+1\le n+1$** achievable
by some legal composition — nothing in `vertex-minimum-theorem` restricts
$k$ to powers of $2$. Since $D=2^{n+1}-1$ is a Mersenne number, it can be
(and for $n=2$, is: $D=7$) coprime to some such $k$ (here $k=3$), so the
extra denominator factor $k$ is **not absorbed by $D$**. This is the
precise, checkable reason the outline's Step 2 "should follow automatically
from tie-equalities being rational" does not in fact hold in the sharp
form conjectured — rationality (Lemma R1) is automatic; the *specific*
denominator $D$ is not.

## 3.1 The repaired (correct) rationality statement

**Lemma R2 (repaired).** At a vertex $V$ cut out by type-(I)/(II)
constraints as above, write the vertex's *tie profile* as the partition of
each cut piece's fragment-count into tied blocks (e.g. the counterexample's
profile for $p_1$ is "one block of size $3$"; a piece with fragments
$y_1=y_2$, $y_3$ free, $y_4=0$ has profile "one block of size $2$, one
singleton, one zero"). Let $L:=\mathrm{lcm}$ of all block sizes $\ge2$
occurring anywhere in $V$'s tie profile (across all pieces), with $L:=1$ if
there are no such blocks (every constraint is type (I) or involves only
singleton fragments). Then every fragment value of $V$ lies in
$\tfrac1{D\cdot L}\mathbb Z$.

*Proof.* Within a single piece, a block of $k$ mutually-tied fragments
summing (together with the piece's other, non-tied fragments) to the
piece's rational total $p_i$ has each tied fragment equal to
$\frac1k\big(p_i-\text{(sum of the piece's other, already-rational,
fragments)}\big)$ — rational with denominator dividing $k$ times the
existing denominator. Every non-tied fragment is rational by Lemma R1 with
denominator dividing $D$ (it is a direct affine rational combination of the
$p_i=q_i/D$, $q_i\in\mathbb Z$, with no extra division introduced, since it
is pinned by type-(I) "$=0$" constraints or by being the single free
representative of its own block, hence solved directly from a piece-sum
equation with denominator $D$ only). Chaining through all of $V$'s
(finitely many) blocks, each dividing at most once more by its own block
size, the final denominator of any fragment divides $D$ times the product
of the block sizes it was involved in dividing by — which divides $D\cdot
L$ since each individual division is by some block size $k\mid L$ (a
single fragment is only ever divided once, by its own block's size,
regardless of how many *other* blocks exist elsewhere in the vertex, since
distinct pieces' tie constraints do not interact — the piece-sum
constraints are decoupled across pieces). $\blacksquare$

This is the correct, provable version of the outline's Step 2: rationality
with a denominator controlled by the vertex's own combinatorial tie
structure, **not** uniformly by $D$ alone. It reduces to the outline's
conjectured statement exactly on the sub-locus where $L=1$ or $L$ is a
power of $2$ dividing into $D\cdot2^m$ terms that the digit model can still
absorb — see §4.

## 4. Step 3, attempted on the binary-tree locus — refuted by direct computation

Call a legal tail refinement $G'$ of $T=\{p_2,\dots,p_{n+1}\}$
**binary-tree** if every tie block occurring in its vertex representation
(in the sense of Lemma R2) has size a power of $2$ — equivalently, $G'$ is
obtained from $T$ by a sequence of exact bisections (each cut splits an
existing fragment into two *equal* halves). This is the most favorable
restricted case for the outline's hoped-for digit/carry model, since by
Lemma R2 it keeps every fragment's denominator in $D\cdot2^{\mathbb
Z_{\ge0}}$, matching the "binary ladder" flavor the crux-corpus leads
(`aimo-0141`, `aimo-0917`) actually concern.

**The natural first attempt (and why it fails).** The tempting claim,
motivated by `aimo-0917`'s companion popcount fact (a value repeatedly
halved under a binary tree produces, at each depth, a *power-of-two* count
of equal leaves), is: *bisecting a tail piece never changes the parity of
$N_{G'}(x)$ at any point $x$, since it replaces one value by an even number
($2$) of half-value copies, and an even count contributes $0$ to parity.*
If true, this would give $v_{G'}=u_T$ pointwise for every binary-tree $G'$,
reducing $(\star\star)$ on this whole locus to the already-solved
unrefined-tail case.

**This claim is false, refuted by direct exact computation, not merely
unconfirmed.** Take $x=0$ and a single tail piece of value $q>0$
unsplit: $N(x)=1$ (odd) for $x$ just below $q$. Bisect it into two copies
of $q/2$: for the same $x$ (just below $q$, above $q/2$), *both* copies
exceed $x$, so $N(x)=2$ (even) — the piece's *own* contribution flips
parity, because for $x$ in the band $[q/2,q)$ only the *undivided* piece
counted before, and bisection does not add "two copies exceeding $x$" and
"zero copies exceeding $x$" as the naive count-parity argument assumed;
it can add two copies *both* exceeding $x$, an even number that still
changes $N(x)$'s value (from $1$ to $2$) and hence its *parity* is
unaffected only by luck, not in general, once other pieces are added to
the count and $x$ ranges over an interval where the split piece's
*own former single contribution* mattered. Concretely, with the full
$n=4$ ladder tail $T=\{p_2,p_3,p_4,p_5\}=\{8,4,2,1\}/31$ (rescaled;
$D=31$), asymmetric cut $x=20/31$ on $p_1=16/31$ giving window
$W\cap[0,r)=[0,15/31)$ (with $r=15/31$, $\Delta=24/31$):
$$\int_{W}u_T\,dt=\frac5{31},\qquad
\text{after bisecting }p_2=\tfrac8{31}\text{ into two }\tfrac4{31}\text{'s:}
\quad\int_W v_{G'}\,dt=\frac3{31},$$
$$\text{after bisecting }p_3=\tfrac4{31}\text{ into two }\tfrac2{31}\text{'s:}
\quad\int_W v_{G'}\,dt=\frac7{31}\ (\textbf{strictly larger}),$$
$$\text{after bisecting }p_4=\tfrac2{31}\text{: }\int_Wv_{G'}\,dt=\frac5{31}
\ (\text{unchanged, coincidentally}),\qquad
\text{after bisecting }p_5=\tfrac1{31}\text{: }\int_Wv_{G'}\,dt=\frac6{31}.$$
(Recomputed independently by exact `Fraction` interval-breakpoint
integration — see the worked script; every value above is exact, no
floating point.) So bisection of a single tail piece can **decrease,
leave unchanged, or strictly increase** the window integral depending on
*which* piece is bisected — it is not parity-invariant, and in particular
the case that strictly increases it ($5/31\to7/31$) is exactly the
dangerous direction for $(\star\star)$ (a larger left side makes the
inequality harder to satisfy), so this is not a merely cosmetic
counterexample: it shows bisection can genuinely work *against*
$(\star\star)$, not just fail to obviously help it.

**Consequence.** The hoped-for reduction "binary-tree refinement $\Rightarrow$
same window integral as the unrefined tail" is false. Step 3 as outlined —
"re-derive $I_1+I_2$ as a digit/carry sum ... aiming for a closed form" —
was attempted on its most favorable sub-case and does not produce the
clean invariance the outline's motivating analogy (`aimo-0917`'s
popcount-additivity) suggested. No positive digit/carry formula for
$(\star\star)$'s window integral was found this round, on the restricted
locus or in general.

## 5. Honest summary of the wall reached

- **Proved, general, reusable:** Lemma R1 (rationality at every vertex of
  every legal composition) and Lemma R2 (the correct denominator bound,
  $D\cdot L$ with $L=\mathrm{lcm}$ of tie-block sizes) — available for
  `rank-tie-vertex-reduction` and `rank-pigeonhole-budget` to use in place
  of the false "denominator divides $D$" premise.
- **Refuted, with a fully worked counterexample:** the outline's sharper
  Step-2 conjecture. This is the honest, checkable reason the "digit model
  transplants automatically" hope does not pan out as stated.
- **Refuted, on its own most-favorable sub-case, backed by exact
  computation:** Step 3's natural first attempt — that exact bisection of
  a tail piece leaves the window integral parity-invariant, reducing the
  binary-tree locus to the already-solved unrefined-tail case. §4 exhibits
  a concrete $n=4$ instance where bisecting different single tail pieces
  moves the window integral from $5/31$ to each of $3/31,\,7/31,\,5/31,\,
  6/31$ — sometimes strictly *increasing* it, the direction dangerous for
  $(\star\star)$. This closes off the most obvious route into Step 3, with
  a concrete disproof rather than an unexplored hope.
- **Not reached:** a working digit/carry formula for $(\star\star)$'s
  window integral, even restricted to binary-tree refinements; outline
  Step 4 (achievability/tightness), since it presupposes a complete Step 3.

**Recommendation for the next round.** The digit/carry transplant's core
promise — that rescaling to integers makes the window-integral computation
mechanical — is now shown false at two separate points: (i) general legal
refinements need not even land on the integer/dyadic lattice generated by
$D$ (§3's refutation), and (ii) even restricted to refinements that do stay
on a dyadic lattice, the window integral is not invariant under further
refinement, and can move in the direction that hurts $(\star\star)$ (§4's
refutation). Recommend **not** re-attempting the binary-digit/popcount
transplant from `aimo-0917`/`aimo-0141`/`aimo-0764` in this form — the
static-set/monovariant machinery those crux entries supply does not carry
over to this problem's adversarial-minimax window integral, confirming the
risk the round-6 outline itself flagged as unconfirmed. Treat this
approach's two lemmas (Lemma R1, general rationality; Lemma R2, the
repaired $D\cdot L$ denominator bound) as its reusable contribution, and
redirect further effort at $(\star\star)$ toward the other live framings
(`lp-duality-certificate`, `greedy-halving-adversary`, `rank-pigeonhole-
budget`), since closing $(\star\star)$ by exact combinatorial computation
appears to require genuinely new ideas beyond bisection/popcount, not
already in the crux corpus for this shape of problem.
