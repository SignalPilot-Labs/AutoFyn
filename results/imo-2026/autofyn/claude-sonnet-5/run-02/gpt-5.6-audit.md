# GPT-5.6 audit of `autofyn/claude-sonnet-5/run-02`

## Scope and grading standard

I audited the selected `current.md` in each of
`results/imo-2026/autofyn/claude-sonnet-5/run-02/problem-01` through
`problem-06` against the exact statements `imo-2026-01` through
`imo-2026-06` in `problems.jsonl`. I inspected promoted lemma and approach
files where a selected proof depended on them. For Problem 2 I also inspected
and executed the supplied exact symbolic checker
`problem-02/scratch/round-2/build.py` with bytecode writing disabled.

The harness's labels “solved,” “approved,” “certified,” and its numerical
experiments were not treated as proof. Code-assisted mathematics is accepted
when the code constructs and exactly checks the claimed certificate. A
floating-point experiment or an unavailable computation is not accepted.

I use the strict completion-based standard requested for these audits: a
complete proof receives 7; a proof with a genuine but uniquely local,
mechanical repair receives 6. A submission missing a load-bearing direction
or theorem receives 0. In particular, extensive research notes or proofs of
special cases do not become a solution to a statement quantified over every
positive integer.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Exact certificate, but one exceptional denominator branch needs a local repair | 6/7 |
| 3 | No general proof; both general minimax directions remain open | 0/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete | 7/7 |
| 6 | No general proof; decisive FAH and termination hypotheses remain open | 0/7 |
| **Total** |  | **27/42** |

## Problem 1 — 7/7

### What the proof does

For every prime `p`, the solution replaces each board entry by its `p`-adic
valuation. A move on two valuation coordinates is

\[
(\alpha,\beta)\longmapsto
(\min(\alpha,\beta),|\alpha-\beta|).
\]

The Euclidean identity

\[
\gcd(\min(\alpha,\beta),|\alpha-\beta|)
=\gcd(\alpha,\beta)
\]

therefore preserves the gcd `g_p` of the complete list of `p`-adic
valuations.

For termination, the proof uses the lexicographic monovariant

\[
\left(\sum_i\Omega(a_i),\ \#\{i:a_i>1\}\right).
\]

If the chosen entries have nontrivial gcd, the first component decreases.
If they are coprime, they become `1` and their product, so the first component
is unchanged and the second decreases by one. Thus every play terminates.

At termination there is at most one nonunit. The invariant excludes an
all-ones terminal board, and if `M` is the sole nonunit then

\[
v_p(M)=\gcd_i v_p(x_i)
\]

for every prime `p`. This determines `M` uniquely from the initial board.

### Skeptical checks

- The valuation formula for `lcm(m,n)/gcd(m,n)` is correctly
  `|v_p(m)-v_p(n)|`.
- The multiset-gcd convention handles zero valuations correctly; no step
  assumes all exponents are positive.
- In the non-coprime case the total `Omega` decreases even if one output is
  still nontrivial. In the coprime case the nonunit count falls exactly by
  one. These cases are exhaustive.
- Lexicographic order on nonnegative integer pairs is well-founded, so the
  monovariant proves finite termination rather than merely excluding a
  repeated state.
- To rule out the all-ones board, the proof chooses a prime dividing one
  initial entry. Its valuation list is nonzero and hence has positive gcd;
  the all-ones board would give gcd zero.
- Only primes occurring initially can occur in the final product, so the
  closed form for `M` is a finite integer product.

No mathematical defect was found. The computational simulations at the end
are unnecessary; the preceding argument is self-contained.

**Verdict: complete, 7/7.**

## Problem 2 — 6/7

### Geometric reduction

The proof normalizes

\[
B=(0,0),\qquad C=(1,0),\qquad A=(p,q),\quad q>0.
\]

Since `M,N` are consecutive side midpoints, they are both on the nine-point
circle of `ABC`. Comparing their squared distances from the circumcenter `O`
of `AKL` and from the nine-point center reduces the target to

\[
O_x=\frac p2+\frac14.
\]

The three given angle equalities are translated into cross/dot polynomial
equations `eq1=eq2=eq3=0`. Eliminating `l2` first yields a cubic locus
`X(k1,k2,p,q)=0` and a second equation `eq2_num=0`. An exact polynomial
identity then forces the numerator of
`O_x-(p/2+1/4)` to vanish.

### Angle-orientation checks

The cross/dot dictionary would be invalid if the two equal unsigned angles
had opposite rotational orientations. The proof does not ignore this issue.
It derives six strict cross-product signs from the four containment
hypotheses:

- interiority of `K` in triangle `BMC`;
- interiority of `L` in triangle `BNC`;
- `K` lying inside angle `LBA`; and
- `L` lying inside angle `ACK`.

Positive barycentric/cone decompositions show that both vector pairs in each
of the three angle equations rotate counterclockwise. Hence each given
unsigned equality really implies its displayed polynomial equation, not a
supplementary-angle branch. The sign argument uses only containment, so it is
not circular.

The cone calculation correctly establishes
`D2=-cross(K-B,A-C)<0` from the positive-combination expression for
`K-B` at vertex `B` of triangle `BMC`. The submitted proof's separate
argument for `D != 0`, however, contains a real exceptional-case gap. It
says strict interiority of `L` in triangle `BNC` implies `l1 != 1`.
That is false when `p>1`, because `N_x=(p+1)/2>1` and the interior of
`BNC` can cross the line `x=1`.

The failure occurs on admissible configurations, not merely on an extraneous
algebraic component. For example, with

\[
p=\frac65,\quad q=\frac35,\quad
K=\left(\frac{17}{16}-\frac{\sqrt{201}}{48}\right)
  \left(\frac{21}{25},\frac3{25}\right),
\]

\[
L=\left(1,\frac{17-\sqrt{209}}{40}\right),
\]

all three angle equations and all four strict containment conditions hold,
while `D=0` and `l1=1`. Thus the elimination
`l2=S(l1-1)/D` and the later denominator `4DD3` are undefined there.

There is a short mechanical repair. The reflection exchanging
`B,M,K` with `C,N,L` sends `p` to `1-p` and preserves the full
hypothesis system, so one may assume `p<=1`. Then strict interiority in
`BNC` does give `l1<1`, and the submitted nonsingular-system argument
proves `D!=0`.

The remaining denominator is proportional to twice the signed area of
`AKL`. Since the problem calls `AKL` a triangle and supplies its
circumcenter, it is noncollinear, so that denominator is nonzero.

### Exact algebraic certificate

The load-bearing identity is

\[
\operatorname{Fn\_num\_raw}D_2
-(k_2-q)\operatorname{eq2\_num}
=D X(E_1l_1+E_0).
\]

The supplied `scratch/round-2/build.py` is self-contained. Starting from the
raw coordinates, cross products, and dot products, it:

1. constructs `eq1`, `eq2`, and `eq3`;
2. solves `eq1=0` for `l2` and checks the substitution exactly;
3. derives the explicit cubic `X` from `eq3`;
4. derives `eq2_num`;
5. constructs the circumcenter and the target numerator and denominator; and
6. expands both sides of the closing identity.

I executed it in exact symbolic arithmetic. The relevant outputs were:

```text
direct l2 substitution check (should be 0): 0
Identity check (LHS-RHS, should be 0): 0
resultant(X,D,k2) == 0 ? False
resultant(X,D2,k2) == 0 ? False
```

The exact factorization of the circumcenter denominator and the relation to
the signed-area denominator also matched the proof. This is a valid
reproducible certificate, not a numerical sample.

An older approach file had a sign slip in a displayed `l2` formula. The
selected `current.md` uses the corrected formula, and the checker verifies
the direct substitution is zero. The historical typo therefore does not
affect the submitted proof.

After the reflection normalization above, `X=eq2_num=0`, the identity, and
`D2!=0` force the target numerator to zero; the nonzero denominator then
gives the required equality.

**Verdict: complete after a local exceptional-branch repair, 6/7.**

## Problem 3 — 0/7

### What is claimed and what is actually established

The file conjectures the correct-looking value

\[
c(n)=\frac{2^n}{2^{n+1}-1},
\]

with the usual geometric ladder partition. It contains a large amount of
serious partial work, including:

- the reduction of the claiming stage to the sum of the odd-ranked piece
  lengths;
- complete solutions for `n=1` and `n=2`;
- vertex-reduction and alternating-sum identities for fixed cutting
  compositions;
- several lower-bound subcases for the ladder construction;
- several exact finite chamber closures; and
- substantial progress on the `n=3` and `n=4` subproblems.

Those results are not a proof for arbitrary `n`. The selected file says this
explicitly:

```text
## Full proof
(absent — Status is `partial`. The problem asks for general n; only n=1
and n=2 are fully closed.)
```

### Missing lower-bound direction

For the ladder opening, the proof must show that every legal Xiang Yu
refinement leaves Liu Bang at least the proposed value. The file closes
various cut distributions—initially the case where the top ladder piece is
untouched, later several one-cut and vertex families—but still leaves
general simultaneous refinement patterns open. Its own latest summaries
identify unresolved `h(m)`/`MaxCeil`/`MinFloor` families for general `m`.

Thus there is no induction or exhaustive classification covering every way
Xiang Yu may distribute `n` cuts. Proving individual endpoints, symmetric
cuts, or finitely many small-`m` vertices does not imply the required
general lower bound.

### Missing upper-bound direction

For an arbitrary Liu Bang marking, the solution must exhibit or prove the
existence of an Xiang Yu response keeping the odd-rank sum below the claimed
constant. The file never supplies this for arbitrary `n`.

Even at `n=4`, the chamber-based approach retains an explicit residual region
and records that a purported “100% coverage” claim had to be retracted after
an exact counterexample to the chosen chamber family. Later partition/pinning
families close additional witnesses and strips, but the file still does not
prove that the resulting family covers all legal openings or all required
response types. Empirical coverage and millions of random trials are not an
exhaustive mathematical argument.

### Why the accumulated lemmas do not amount to a solution

The vertex-minimum theorem can replace a continuum by finitely many vertices
for a *fixed* combinatorial composition. It does not give a uniform
classification or bound over all compositions as `n` varies. Likewise,
conditional propagation theorems only move the obstruction from one named
family to another unless their hypotheses are proved for every parameter.

The submission is admirably candid about this. Its `partial` status is
accurate, and no hidden full proof appears later in the file.

Under a research-progress rubric, the exact `n=1,2` solutions and structural
lemmas are meaningful. Under the requested completion-heavy IMO grading,
however, neither direction of the general minimax equality is complete.

**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

### Claimed characterization

\[
\boxed{\theta=\frac{180^\circ}{n}\quad\text{for an integer }n\ge2.}
\]

### Single-move model

Writing the current triangle as `(A,B,C)`, a cut from the `A` vertex with
parameter `0<x<A` gives the two angle triples

\[
(x,B,180^\circ-x-B),
\qquad
(A-x,C,B+x).
\]

Every `x` in the open interval is geometrically realizable by a unique ray
from the vertex to the opposite open side, so the algebraic model represents
exactly the legal moves.

### Resonant case

If `theta=180 degrees/n`, the chain lemma is correct: from a triangle with an
angle `K theta`, cutting that vertex with `x=theta` makes one child contain
`theta` immediately and the other contain `(K-1)theta`. Induction therefore
forces a win.

If the starting triangle contains no integral multiple of `theta`, the proof
chooses the largest angle `A` and orders the other two as `beta>=gamma`. In
units of `theta`, let `g=gamma/theta` and set `k=ceil(g)`. The chosen

\[
x=180^\circ-\beta-k\theta
\]

makes one child contain `k theta` and the other contain `(n-k)theta`.

The domain checks are valid:

- `k>g` gives `x<A`;
- for `n>=3`, the largest normalized angle is at least 1 and, under the
  no-multiple hypothesis, strictly greater than 1, giving `x>0`;
- the separately handled `n=2` case also has `0<x<A`; and
- `1<=k<=n-1`, so both forced multiples are genuine triangle angles.

Whichever child Shan-Yu retains, the chain lemma finishes the game in
finitely many moves.

### Nonresonant case

Call a triangle safe when none of its angles belongs to `theta Z`. For any
cut of a safe triangle, if the first child is unsafe then either

\[
x\in\theta\mathbb Z
\quad\text{or}\quad
180^\circ-x-B\in\theta\mathbb Z.
\]

In the first case, subtracting `x` from `A` and adding it to `B` cannot place
either result on the lattice because `A,B` were off it. In the second case,
the other child's two changing angles are `k theta-C` and
`180 degrees-k theta`; the first is off the lattice because `C` is, and the
second is off it precisely because `180 degrees/theta` is nonintegral.
Thus at least one child remains safe after every move.

The equilateral triangle is a valid safe starting position: if
`60 degrees=k theta`, then `180 degrees/theta=3k` would be an integer. Shan-Yu
can therefore keep a safe child forever in every nonresonant case.

The two cases are exact complements, and both game quantifiers—every initial
triangle in the winning direction and a single perpetual Shan-Yu strategy in
the losing direction—are handled.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

### Necessity

Squaring the two positive inequalities gives

\[
2x^2+2f(y)^2\ge(f(x)+y)^2\ge4xf(y).
\]

Putting `x=f(y)` forces equality throughout and hence

\[
f(f(y))=2f(y)-y.
\]

Iterating from any `y>0` gives

\[
f^n(y)=y+n(f(y)-y).
\]

All iterates must remain positive, so `f(y)>=y`.

Writing `S(x)=f(x)-x`, applying the lower squared inequality with first
argument `f(x)`, and using the functional identity yields

\[
(x-y)^2+4f(x)(S(x)-S(y))\ge0.
\]

Swapping `x,y` gives the other direction, so

\[
-\frac{(x-y)^2}{4f(x)}
\le S(x)-S(y)
\le\frac{(x-y)^2}{4f(y)}.
\]

Subdivide any interval `[a,b]` into `N` equal parts. Since
`f(t)>=t>=a>0`, summing the consecutive estimates gives

\[
|S(a)-S(b)|\le\frac{(b-a)^2}{4aN}.
\]

Letting `N` tend to infinity proves that `S` is constant. Thus
`f(x)=x+c` with `c>=0`.

### Sufficiency and checks

For `f(x)=x+c`, `c>=0`, both squared differences equal

\[
(x-y-c)^2\ge0,
\]

so every such function works.

- Every substitution stays in the positive domain.
- Squaring is legitimate because all sides are positive.
- The orbit argument uses no continuity, monotonicity, or surjectivity.
- The subdivision estimate is two-sided and uniform on `[a,b]`, so it
  genuinely forces constancy without an unstated regularity assumption.
- The injectivity paragraph is correct but unnecessary.

No gap was found.

**Verdict: complete, 7/7.**

## Problem 6 — 0/7

### What the submission proves

The file contains a very large body of partial number-theoretic work and a
collection of certified subfamily theorems. Among other things, it proves
literal periodicity for:

- even initial values;
- prime-power initial values;
- several families such as `a_1=3q^j`; and
- `a_1=pq` for several fixed small primes `p`, outside explicitly handled
  exceptional sets.

It also develops bounded-gap, persistent-type, finite-core, absorption, and
conditional residue-cycle machinery. These are genuine results, but the
problem asks for every possible `a_1>1`.

### The decisive missing hypotheses

The selected file has no full proof:

```text
## Full proof
Not present — Status is `partial`.
```

For a general initial value, its Master Conditional Theorem still assumes
two unproved statements:

1. **H1 / FAH:** at the terminal finite core, the relevant persistent prime
   types have the required pairwise intersection property. The file also
   calls equivalent versions Symmetric FAH, Cofinite FAH, or EEA.
2. **H2:** the iterated absorption chain of finite prime sets terminates.

If both held, the conditional theorem would make the successor rule depend
on finitely many residue classes and would produce exact periodicity. But the
submission repeatedly states that neither hypothesis is established in the
general case. Rephrasing FAH in residue or automaton language does not prove
it, and proving a self-absorbing-core theorem conditional on FAH and
termination does not discharge either condition.

### Why the special families do not cover the problem

The listed families are infinite but not exhaustive. Fixed-prime
instantiations such as `p=5,7,11,13,17,19` do not imply the corresponding
theorem for arbitrary `p`, much less arbitrary integers with several prime
factors. The file explicitly leaves the general `a_1=pq` theorem partial and
identifies residual `p`-independent gaps.

Likewise, a proof for each of a growing list of seeds or subfamilies cannot
replace a uniform argument over all initial values. The reported simulations
also cannot do so. Indeed, the file itself records that one claimed
round-30 numerical singleton pattern failed independent reproduction; this
does not damage the proven subfamily theorems, but it reinforces why the
experiments cannot be promoted to the missing general result.

### Grading verdict

There is no derivation of `T,L` for an arbitrary sequence because the bridge
from the finite structural lemmas to universal exact periodicity is
conditional on H1 and H2. These are the central difficulty of the problem,
not local omissions. The many correct special cases and conditional lemmas
are substantial research progress but do not constitute an IMO solution to
the quantified statement.

**Verdict: incomplete, 0/7.**

## Final coordinator-style assessment

Problems 1, 4, and 5 are clean self-contained solutions. Problem 2 is also
complete: its geometry correctly fixes all angle branches and exceptional
denominators, while the supplied exact checker verifies the large elimination
identity from raw coordinates.

Problems 3 and 6 are not failed proofs disguised as completed ones; their
selected files honestly say that they are partial and omit a full-proof
section. They contain extensive useful mathematics, but the missing portions
are precisely the general statements demanded by the problems. Under a
completion-based IMO standard they therefore receive no points.

**Final score: 27/42.**
