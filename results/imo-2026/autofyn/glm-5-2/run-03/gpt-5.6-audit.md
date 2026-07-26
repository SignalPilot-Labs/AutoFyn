# GPT-5.6 audit of `autofyn/glm-5-2/run-03`

## Scope and grading standard

I audited the selected `current.md` for Problems 1–6 against the statements in
`problems.jsonl`, following the cited arguments and retained run artifacts. I
also independently reconstructed the exact Gröbner-basis computation used in
Problem 2 from the formulas printed in the proof.

I used the requested harsh, completion-based IMO standard. A complete proof,
or one needing only a genuinely tiny local correction, receives 7. A missing
load-bearing theorem receives 0 even when substantial special cases and
conditional results are present. Exact reproducible code is allowed, while
status labels, reviewer approval, and numerical experimentation are not proof.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete; exact algebra independently reproduced | 7/7 |
| 3 | General theorem explicitly remains open | 0/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Load-bearing governing-prime finiteness theorem remains open | 0/7 |
| **Total** |  | **28/42** |

## Problem 1 — 7/7

For each prime `p`, a move sends the two selected valuations to

\[
(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|),
\]

so the gcd of the entire valuation list is invariant. The proof correctly
handles zero valuations via `gcd(0,k)=k`.

The lexicographic monovariant `(Omega,K)`, consisting of total prime-factor
multiplicity and the number of nonunits, is checked in all cases. For a
coprime pair, `Omega` stays fixed and `K` drops; for a noncoprime unequal pair,
`Omega` drops; equal entries also cause a drop. Thus every play terminates.

A terminal position has at most one nonunit. Since the initial board contains
a nonunit, some prime has a positive invariant valuation-gcd, excluding the
all-ones board. The sole terminal number is then fixed prime by prime.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The proof normalizes

\[
B=(0,0),\quad C=(P_B+P_C,0),\quad A=(P_B,1)
\]

and writes `p=cot(alpha)`, `q=cot(beta)`, and `r=cot(gamma)`. The displayed
formulas for `K` and `L` follow from the sine rule in the two relevant
triangles. Their denominators are nonzero in the stipulated interior
configuration.

The remaining angle hypotheses are encoded as cleared polynomial numerators

\[
F_1=\operatorname{num}(L\cdot K-q\det(L,K)),
\]

\[
F_2=\operatorname{num}((L-C)\cdot(K-C)-r\det(L-C,K-C)).
\]

The inside conditions give the determinant signs needed to select the intended
unsigned angles. The target is the cleared equation

\[
\Pi=\operatorname{num}\left(O_x-\frac{3P_B+P_C}{4}\right)=0,
\]

which puts the circumcentre on the perpendicular bisector of `MN`.

I independently reconstructed this calculation with exact SymPy arithmetic
over the rationals from the formulas in `current.md`. The two generators each
had 16 terms and total degree 4; `Pi` had 68 terms and degree 6. The resulting
six-element Gröbner basis reduced `Pi` to an exact zero normal form. Thus

\[
\Pi\in\langle F_1,F_2\rangle
\]

is genuinely verified. This calculation also covers `P_B=P_C`; the proof does
not divide by their difference.

The run does not package this as a clean standalone verifier and README; the
scripts and outputs are embedded in `logs.jsonl`. That is poor archival
presentation but not a mathematical gap here, because all defining formulas
are printed in `current.md`, the deterministic exact calculation is modest,
and it was independently reproduced.

**Verdict: complete exact computer-assisted proof, 7/7.**

## Problem 3 — 0/7

The proposed value

\[
c(n)=\frac{2^n}{2^{n+1}-1}
\]

is established only for `n=1,2,3,4`. Both directions of the general problem
remain open for `n>=5`.

For the lower bound, no proof is given that the dyadic strategy defeats every
Xiang strategy. The unresolved configurations include the general many-split
case, near ties, and repeated splitting of a large descendant. The attempted
parity-XOR induction contains a concrete false invariant: after a large
fragment is split again, its support can enter the band claimed to be
untouched. The submission itself records the example `8 -> 5+3`, followed by
`5 -> 2.5+2.5`.

For the upper bound, exact finite constructions are completed only for small
`n`; the asserted uniform induction remains conjectural. This is not a matter
of filling in routine details—it is the theorem for all remaining values of
`n`.

**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

The proof correctly obtains

\[
\theta=\frac{180^\circ}{n},\qquad n\ge2.
\]

For necessity, the safe-state argument is exhaustive. If `180°` is not a
positive integer multiple of `theta`, the four possible ways both children of
a cut could acquire a `theta`-multiple respectively force a parent angle or
`180°` to be a multiple, contradicting safety. The proposed initial triangle
is safe under the same hypothesis.

For sufficiency, when no angle is already a multiple, the largest-angle
interval contains a suitable `k theta`; the proof separately handles the
borderline `n=2` case. The cut gives the two children angles `k theta` and
`(n-k)theta`. From a `j theta` angle, a subsequent cut with parameter `theta`
either wins immediately or leaves `(j-1)theta`, so finite descent reaches the
target.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The complete answer is

\[
f(x)=x+c,qquad c\ge0.
\]

Putting `x=f(y)` in the original sandwich yields

\[
f(f(y))=2f(y)-y.
\]

With `g=f-id`, this makes `g` invariant along the forward orbit and gives
`f^n(y)=y+n g(y)`. Positivity forces `g>=0`.

Writing the two squared inequalities as nonnegative defects and taking their
sum and difference gives the valid master estimate

\[
|g(x)-g(y)|(2x+2y+g(x)+g(y))
\le (x-y-g(y))^2.
\]

The two-orbit Diophantine argument uses this amplifying linear factor to rule
out distinct positive values of `g`: rational displacement ratios yield exact
near-collisions through an integer construction, while irrational ratios yield
arbitrarily close large orbit points by density. The zero-displacement case is
handled separately through the quadratic estimate near a zero and a maximal
zero-component boundary argument; it does not assume continuity without
proof.

Consequently `g` is constant. Direct QM-AM-GM verifies every `x+c`, and the
positive codomain forces `c>=0`.

**Verdict: complete, 7/7.**

## Problem 6 — 0/7

The submission explicitly remains conditional. The missing theorem is the
finiteness of the set of governing primes. If that set were finite, the
residue/type argument would indeed give eventual affine periodicity, and the
run proves numerous useful structural lemmas and a LOCK subcase. It never
establishes the finiteness statement for arbitrary `a_1`.

Moreover, the run's formerly proposed quantitative route is false. It records
verified counterexamples to the bound

\[
q\le\operatorname{rad}(a_1):
\]

- for `a_1=375`, a governing prime is `19>15`;
- for `a_1=9375`, a governing prime is `67>15`.

These examples do not disprove the Olympiad statement; their individual
sequences are still eventually periodic. They do disprove the claimed route
to the universal governing-prime bound. Computational evidence for individual
starting values cannot establish finiteness for every `a_1`.

The final file itself identifies this as “Gap A.” Since it is the
load-bearing bridge from local structure to a finite-state process, this is not
a tiny omission and receives no partial credit under the requested policy.

**Verdict: incomplete, 0/7.**

## Final assessment

Problems 1, 2, 4, and 5 are complete. Problem 3 remains a collection of
small-`n` results rather than a solution for all `n`; Problem 6 has a strong
conditional endgame but lacks the theorem that makes the state space finite.

**Final score: 28/42.**
