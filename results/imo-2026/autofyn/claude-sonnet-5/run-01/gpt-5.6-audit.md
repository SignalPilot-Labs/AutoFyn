# GPT-5.6 audit of `autofyn/claude-sonnet-5`

## Scope and grading standard

I audited the six selected proofs against the corresponding statements in
`problems.jsonl`. The selected submissions are:

- Problem 1: `problem-01/imo-2026-01-solution.md`
- Problem 2: `problem-02/current.md`, including the certificate in
  `problem-02/code/verify_bezout.py`
- Problem 3: `problem-03/current.md` and the lemma/approach files on which its
  imported lower bound depends
- Problem 4: the full proof in `problem-04/imo-2026-04.md`
- Problem 5: the full proof in `problem-05/imo-2026-05.md`
- Problem 6: `problem-06/current.md`

The internal Autofyn labels “solved,” “approved,” and “certified” were not
treated as mathematical evidence. I checked the cited arguments themselves.
Code is allowed where it supplies a correct, exact, reproducible certificate;
numerical experiments alone are only corroboration.

I use the completion-heavy grading standard requested for these audits: a
complete proof with at most a tiny local repair receives 7, while a missing
load-bearing direction or lemma receives 0 rather than speculative partial
credit. For context, I separately mention where an ordinary problem-specific
marking scheme might plausibly recognize substantial progress.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete; exact algebraic certificate is valid | 7/7 |
| 3 | Upper bound proved, but physical lower bound has major gaps | 0/7 |
| 4 | Complete; two harmless local errors | 7/7 |
| 5 | Complete | 7/7 |
| 6 | Complete | 7/7 |
| **Total** |  | **35/42** |

The only rejected proof is Problem 3. Its claimed answer appears to be right,
and its upper-bound half is good mathematics, but its lower-bound half is
promoted from an abstract D/M game to the actual cutting game through a chain
of lemmas that does not establish that promotion.

## Problem 1 — 7/7

### Outline of the argument

For each prime `p`, the proof replaces every board entry by its `p`-adic
valuation. A move on two entries becomes

\[
(a,b)\longmapsto (\min(a,b),|a-b|).
\]

The gcd of the complete valuation list is preserved by this Euclidean step.
Consequently

\[
\Gamma=\prod_p p^{\gcd_i v_p(x_i)}
\]

is invariant. Termination is proved independently using

\[
\Psi=\left(\prod_i x_i\right)
      2^{\#\{i:x_i>1\}}.
\]

Every legal move decreases `Psi` by at least a factor of two. At a terminal
position there is at most one entry greater than 1, and the invariant then
identifies that entry uniquely.

### Skeptical checks

- When the selected entries are coprime, their product does not fall, but the
  number of nonunits drops by one; hence `Psi` still halves. When their gcd is
  nontrivial, the product falls sufficiently to cover the possible change in
  the nonunit count. All equality cases, including equal selected numbers,
  are handled.
- Zero valuations cause no issue: the transform is precisely an ordinary
  Euclidean gcd step on nonnegative integers.
- “Terminal” initially yields only *at most* one nonunit. The proof correctly
  excludes the all-ones board. Some initial entry has a prime divisor, so the
  corresponding valuation list is not identically zero and has positive gcd;
  the all-ones board would give gcd zero for every prime.
- On a terminal board `(M,1,...,1)`, the exponent of each prime in `Gamma` is
  exactly `v_p(M)`, so the displayed formula determines `M` and proves choice
  independence.

I found no load-bearing omission. The solution is far longer than necessary,
but that is not a correctness defect.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

### Outline of the argument

The proof normalizes

\[
B=(-1,0),\qquad C=(1,0),\qquad A=(p,q),\quad q>0.
\]

It shows that the desired equality is equivalent to the circumcenter `O` of
`AKL` satisfying `O_x=p/2`. The points `K,L` are parametrized on their rays
using the common angle `theta`. The remaining angle equalities produce two
quadratic equations `Q_1=Q_2=0` in the normalized ray distances. Finally an
exact Bezout certificate gives

\[
\Delta T=P_1Q_2+P_2Q_1
\]

on `cos^2(theta)+sin^2(theta)=1`, where `T=0` is exactly the target
`O_x=p/2` condition and

\[
\Delta=\frac{2q\sin(\theta+\alpha)}{\sin\alpha}>0.
\]

### Geometric and branch checks

- The coordinate normalization loses no generality, and the reduction
  `OM=ON iff O_x=p/2` is correct.
- The ray parametrizations use the correct rotations at `B` and `C`.
- The containment hypotheses are actually used to choose the signed-angle
  branches. They imply the negative signs required in the first quadratic
  and the positive signs required in the second. Thus the proof is not
  silently replacing an unsigned angle equality by an invalid signed or
  supplementary branch.
- The cross/dot-product formulations at `M` and `N` preserve those same
  signs. Therefore the problem's hypotheses genuinely imply `Q_1=Q_2=0`.
- The circumcenter is part of the problem's given configuration, so the
  nondegeneracy of triangle `AKL` needed for the determinant is legitimate.
- Since `0<theta+alpha<pi`, the displayed `Delta` is strictly positive.
  Hence the certificate really forces `T=0`.

### Audit of the code certificate

I treated `code/verify_bezout.py` as part of the submitted certificate and
inspected what it proves. It reconstructs the raw cross/dot angle polynomials
from the coordinate vectors, checks their equality with the closed forms
modulo

\[
\cos^2\theta+\sin^2\theta-1,
\]

and verifies that the remainder of

\[
\Delta T-(P_1Q_2+P_2Q_1)
\]

modulo that same relation is identically zero. It also includes an exact
rational Pythagorean spot check. This is a reproducible exact symbolic
certificate, not a floating-point experiment or an unsupported “CAS says
zero” assertion. The identity is needed only for a genuine angle, so proving
it on the trigonometric variety is sufficient.

`verify_numeric.py` is only corroborative and does not itself certify all
containment branches. The proof does not need it.

### Presentation issue

`current.md` imports a substantial existence/uniqueness “Theorem A,” while
the associated lemma file mainly summarizes it. That theorem is unnecessary:
the problem already gives `K,L`. Fixing the supplied configuration directly
provides positive ray lengths, the two equations, and the needed sign
conditions. Deleting the existence/uniqueness claim repairs the exposition
without adding any new mathematical idea. I therefore make no deduction.

**Verdict: complete, 7/7.**

## Problem 3 — 0/7

### Claimed answer

\[
c(n)=\frac{2^n}{2^{n+1}-1}.
\]

The value appears correct. The submission proves one inequality well, but it
does not rigorously prove the other.

### What is successfully proved

The upper-bound half in `current.md`, Sections 1–3 of the full proof, is
convincing.

1. The greedy analysis of the claiming phase correctly expresses Liu Bang's
   payoff using the alternating sum `e` of the sorted final pieces.
2. The Pigeonhole Margin Lemma correctly places `2^k` subset sums into
   `2^k-1` intervals and obtains a nonempty signed subset with discrepancy at
   most `S/(2^k-1)`.
3. The Signed-Sum Realizability Lemma is a valid induction. Pairing a global
   maximum with an oppositely signed term preserves the optimal signing after
   the merge `M(x,y)=x-y`; the all-one-sign case correctly reduces through a
   zero term.
4. Deleting the terms outside the chosen symmetric difference and then doing
   the merges uses exactly `m` legal operations.

This establishes that Xiang Yu can force

\[
e\le \frac{S(A)}{2^{m+1}-1}
\]

for every Liu Bang opening. The token argument in
`lemmas/superincreasing-no-early-zero.md` also correctly proves a lower bound
*inside the restricted D/M formalism*.

The failure is the next step: showing that the D/M restriction captures the
minimum over every physical sequence of cuts.

### Fatal gap 1: the Vertex Lemma's joint-minimum corollary is false as stated

`lemmas/vertex-lemma.md` correctly proves that, with one cut coordinate varied
and all others fixed, the objective is continuous and piecewise linear. It
then claims that every coordinate of every joint minimizer must be at a
breakpoint—tie, bisection, or degeneration.

That conclusion does not follow. A piecewise-linear function can be constant
on a nontrivial interval, so an interior non-breakpoint can be a minimizer.
The one-variable argument proves only that the coordinate can be moved to
*some* endpoint or breakpoint without worsening the current objective. It
does not show that the original minimizer already has the asserted form.
Moreover, successively moving coordinates can destroy breakpoint relations
previously arranged for other coordinates.

A genuine global-polyhedral argument selecting a compatible vertex minimizer
might repair this, but no such argument is supplied.

### Fatal gap 2: the peeling step does not reconcile two different graphs

`lemmas/dm-completeness-partial.md` requires a cut that is simultaneously:

- a leaf-parent in the physical cut forest, so it can be undone; and
- an in-degree-zero node in the tie-dependency graph, so no remaining cut
  depends on its output.

The finite-graph argument only supplies an in-degree-zero tie node. It does
not prove that this node is a leaf-parent in the physical ancestry forest.
Conversely, an arbitrarily selected leaf-parent may still be the target of
another unresolved tie. Forest ancestry and tie dependency are genuinely
different relations.

This is not merely an auditor's speculative objection. The “Honest scope
note” in `lemmas/all-cycles-resolution.md` explicitly says that the
forest-depth/indegree compatibility is handled only at “proof sketch” level.
That compatibility is precisely what the induction needs.

### Fatal gap 3: physical configurations and active-multiset bookkeeping are conflated

When a bisecting leaf is undone, duplicate-pair cancellation yields an
identity of the form

\[
e(\mathrm{FINAL})
=e(\mathrm{FINAL}'\setminus\{\ell\}),
\]

not `e(FINAL)=e(FINAL')`. The multiset on the right after cancellation is an
active-token bookkeeping object; it need not be the physical outcome of the
shorter cut forest. The strong induction, however, is stated for physical
configurations. The same mismatch occurs in the tie-to-original case,
especially when the alleged matching piece `ell` was itself created by an
earlier cut.

The proof therefore has not justified invoking physical-cut induction on the
reduced active multiset and then appending a D/M operation.

### Fatal gap 4: the Cycle Common-State Lemma assumes the missing compatibility

The all-cycles repair claims that the acyclic remainder may be executed before
any cut in a chosen cyclic component, so all cyclic input pieces occur
simultaneously in one D/M-reachable state. Minimality in the condensation of
the *tie-dependency graph* does not prove this. An acyclic cut can be a physical
descendant of a cyclic cut or can consume a piece produced by it without
creating the relevant kind of tie edge.

Thus the proof has not shown that the participants of the cycle coexist as
active tokens. The disjoint-support premise needed by the subsequent even-
and odd-`#X` signed-sum arguments is consequently unavailable. Those parity
calculations may be correct conditional on a common state, but their
load-bearing premise is not proved.

### Fatal gap 5: the `#X=0` cycle case is not closed

The earlier shared-value cycle-breaking result is stated for distinct
once-cut original pieces. `lemmas/all-cycles-resolution.md` says it applies
“verbatim” to arbitrary derived participants, but does not establish that
extension.

Even in the original scope, piecewise linearity does not imply that every
minimizing breakpoint must be a crossing with the specially chosen untouched
original or a degenerate endpoint. Other crossings and flat minimizing
intervals can occur. The asserted exhaustive list of ways the minimum can be
attained is therefore unproved.

### Grading verdict

The claimed lower bound for the actual cutting game rests on D/M completeness,
and D/M completeness remains unproved. This is a central missing direction,
not a one-line repair. Under a conventional problem-specific partial-credit
scheme, the complete upper bound could plausibly be worth about 3/7. Under the
requested completion-heavy standard, however, it cannot receive credit as a
claimed full solution.

**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

### Outline of the argument

Represent a triangle by its angle triple `(alpha,beta,gamma)`. Cutting the
vertex of angle `alpha` with parameter `0<t<alpha` gives children

\[
L(t)=(t,\beta,\alpha+\gamma-t),\qquad
R(t)=(\alpha-t,\gamma,\beta+t).
\]

For `theta=180 degrees/n`, attacking an angle larger than `theta` with
`t=theta` makes one child contain `theta`, forcing Shan-Yu to retain the
other child and thereby subtracting `theta` from the attacked angle. When a
small helper angle `h<theta` is present, the helper-reset move forces the
universal triangle

\[
(\theta-h,h,180^\circ-\theta).
\]

Its last angle is `(n-1)theta`, so repeated forced subtraction reaches
`theta`.

For the converse, when `180 degrees/theta` is not an integer, Shan-Yu starts
from

\[
(\theta/2,\theta/2,180^\circ-\theta)
\]

and maintains the invariant that no angle is an integral multiple of
`theta`. The four congruence cases show that, after any cut at any vertex,
both children cannot simultaneously violate the invariant. Shan-Yu can
therefore preserve it forever.

### Skeptical checks

- Both child-triple formulas are correct and preserve total angle 180
  degrees.
- The transfer move is genuinely forced because the discarded choice would
  contain `theta` immediately.
- Substituting `t=theta-h` in the helper-reset move gives exactly
  `(theta-h,h,180 degrees-theta)` on the retained side and puts `theta` in
  the rejected side.
- The room-condition sum argument ensures an eligible partner exists. Its
  use of `theta<=90 degrees` is valid for every integer `n>=2`.
- The proof uses a fixed finite pipeline, not a naive redispatch loop; the
  manufactured `(n-1)theta` coordinate then decreases deterministically.
- The survival triangle is positive and satisfies the invariant whenever
  `180 degrees/theta` is nonintegral.
- The congruence argument is symmetric in the attacked vertex and covers an
  arbitrary real split, not merely the special winning moves.

### Two local errors found

1. The proof writes `ceil(A_0/theta)<=n-1`, which can be false when
   `A_0/theta` lies strictly between `n-1` and `n`. The number of required
   subtractions is instead the least `j` for which
   `A_0-j theta<=theta`; it is still at most `n-1` because `A_0<n theta`.
   The termination bound survives unchanged.
2. Lemma 4 contains the reversed display `a+b+c>3theta=180`. The intended
   relation is `180=a+b+c>3theta`, yielding `theta<60 degrees`. The
   surrounding argument uses the correct conclusion, so this is plainly a
   typographical reversal.

Both are isolated one-line repairs and neither changes the strategy or the
characterization.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

### Outline of the argument

Substituting `x=f(y)` collapses both outer terms of the given inequality and
forces

\[
f(f(y))=2f(y)-y.
\]

Iteration then gives `f^n(y)=y+n(f(y)-y)`. Positivity of every iterate
implies `f(y)>=y`. Writing `d(x)=f(x)-x`, the squared lower inequality,
applied with `x` replaced by `f(x)`, gives the exact identity and inequality

\[
(2f(x)-x+y)^2-4f(x)f(y)
=(x-y)^2+4f(x)(d(x)-d(y))\ge0.
\]

Partitioning any interval `[a,b]` into `N` equal pieces and applying this in
both directions yields

\[
|d(b)-d(a)|\le \frac{(b-a)^2}{4aN}.
\]

Letting `N` grow proves that `d` is constant, hence `f(x)=x+c` with `c>=0`.
The converse follows from ordinary QM-AM-GM applied to `x` and `y+c`.

### Skeptical checks

- The substitution `x=f(y)` is legal because the codomain is positive.
- The iterate argument uses no unstated continuity, measurability, or
  surjectivity assumption.
- Squaring is reversible in the required direction because all expressions
  are positive.
- The algebraic defect identity has the correct coefficient `4f(x)`.
- The partition estimate is applied in both orientations, so it controls the
  absolute difference rather than only proving one-sided monotonicity.
- The denominator is uniformly bounded using `f(x_i)>=x_i>=a>0`; hence the
  limit argument is rigorous.
- For `f(x)=x+c`, the middle expression is `(x+(y+c))/2`, so both required
  inequalities are exactly QM-AM and AM-GM.

No gap or illegitimate regularity assumption was found.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

### Outline of the argument

Let `k=a_1`. The proof first establishes the exact recursive
characterization: an integer `n>k` is a nonterm if and only if it is coprime
to some earlier term. It then proves:

1. every multiple of a term is a term;
2. if `rs` is a nonterm, then `r^2s` is a nonterm; and
3. if `p>k` is prime and `n` is a nonterm, then `np` is a nonterm.

The third statement is proved by a valid minimal-counterexample descent. From
these claims, the proof shows that two integers at least `k` having the same
set of prime divisors at most `k` have the same term/nonterm status.

Set

\[
P=\prod_{p\le k,\ p\text{ prime}}p.
\]

Congruent integers modulo `P` have the same small-prime set, so each residue
class is uniformly a term class or a nonterm class once restricted to
integers at least `k`. If there are `T` good residue classes, their increasing
enumeration immediately gives

\[
a_{n+T}=a_n+P
\]

for every `n>=1`.

### Skeptical checks

- The recursive IN/OUT lemma follows exactly from the minimality in the
  sequence definition; it does not assume the desired periodicity.
- The “multiple of a term” claim correctly uses the fact that every two
  distinct terms have gcd greater than one.
- In the big-prime companion lemma, the auxiliary number `y^alpha` is in the
  required domain and is strictly smaller than the alleged minimal
  counterexample. The descent through `p^i y^alpha` therefore closes.
- In the main minimal-counterexample theorem, `e_0=d_0/p` satisfies
  `e_0>=c_0>=k`. This domain check is crucial and is present.
- Removing a factor `p<=k` preserves the small-prime signature because
  similarity already forces `p` to divide the smaller member; when `p>k`,
  removal plainly affects no small prime.
- Sorting the finitely many good residue representatives in `[k,k+P)` gives
  consecutive nonoverlapping blocks. Thus the final relation holds from the
  first term, with no unproved “eventually periodic” to “periodic” jump.

There is one microscopic wording issue in Claim 1: its cited pairwise-term
corollary is stated for distinct terms, while the witness `m` could in
principle equal the term `n`. In that case `gcd(n,n)=n>1` directly, so the
same contradiction is immediate. This is not a mathematical gap.

The numerical checks in Section 8 are unnecessary; the proof before them is
self-contained.

**Verdict: complete, 7/7.**

## Final coordinator-style assessment

Problems 1, 2, 4, 5, and 6 are full solutions. Problem 2's computational
component is acceptable because it is an exact symbolic certificate whose
mathematical role and domain are explicit. Problem 4's two mistakes are
localized notation/arithmetic slips with immediate repairs and no effect on
the strategy.

Problem 3 is qualitatively different. The missing physical-cut/D/M
equivalence is the bridge needed for the entire lower bound, and several
later cycle arguments assume that bridge rather than establish it. It should
not be promoted as a solved proof in its current form.

**Final score: 35/42.**
