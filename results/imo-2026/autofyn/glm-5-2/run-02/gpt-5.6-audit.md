# GPT-5.6 audit of `autofyn/glm-5-2/run-02`

## Scope and grading standard

I audited the selected `current.md` for Problems 1–6 against the statements in
`problems.jsonl`, following the cited lemmas and retained artifacts where they
carry part of the proof. I independently executed the exact symbolic verifier
used in Problem 2.

I used the requested harsh, completion-based IMO standard. A complete proof,
or one needing only a genuinely tiny local repair, receives 7. A missing
load-bearing theorem receives 0 even if important special cases or promising
ideas are proved. Exact reproducible code is accepted; labels such as
`solved`, reviewer approval, and numerical sampling are not evidence by
themselves.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete exact computer-assisted proof | 7/7 |
| 3 | General problem is explicitly unsolved | 0/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Complete bounded-prime and periodicity proof | 7/7 |
| **Total** |  | **35/42** |

## Problem 1 — 7/7

For each prime `p`, a move acts on the chosen valuations by

\[
(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|),
\]

which preserves the gcd of the entire valuation list. The convention
`gcd(0,k)=k` is correctly handled.

The lexicographic monovariant consisting of total prime-factor multiplicity
and the number of nonunits strictly decreases: for a coprime chosen pair the
first coordinate stays fixed and the second drops, while for a noncoprime pair
the first drops. This proves termination under arbitrary choices.

A terminal board has at most one nonunit, and the valuation invariant excludes
the all-ones board. The remaining number has exactly the invariant valuation
at every prime, so it is independent of play.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The coordinate proof turns the first two angle equations into two homogeneous
linear equations in `K-B`. Their determinant factors as

\[
D=-\frac b4(u^2+v^2)D_0(L),
\]

so the actual configuration satisfies `D_0(L)=0`. Their common kernel is
parametrized by `K=B+t d(L)`. The third angle condition and the cleared target
`OM=ON` then become quadratics `e3_line` and `Q_line` in `t`. The decisive
saturation identity is

\[
Q_{t^2}e3_{\rm line}-e_{t^2}Q_{\rm line}=D_0G.
\]

On the actual configuration, `D_0=e3_line=0`, while

\[
e_{t^2}=\frac{b^3}{2}(u^2+v^2)(v-l_y)|L-C|^2>0
\]

by strict interiority. Hence `Q_line=0`, which is precisely the cleared target.

The load-bearing symbolic certificate is retained at
`problem-02/scratch/round-2/my_verify.py`. I ran it independently. It rebuilds
`e1`, `e2`, `e3`, and `Q` from the coordinate definitions and verifies exact
homogeneous linearity, the determinant factorization, the formula for
`e_{t^2}`, zero remainder in the stated fraction-field division, and equality
with the displayed quotient `G`. In particular it reported both

```text
remainder identically zero? True
LHS - D0*G_prop == 0 ... True
```

The proof also addresses the necessary nonvanishing facts: strict interiority
excludes `K=B` and `L=C`, and the defined circumcircle gives the relevant
nonzero determinant. The polynomial angle equations are used only as necessary
conditions, so extra algebraic branches cause no logical problem.

This would not be an ordinary handwritten Olympiad solution, but under the
user's explicit code-allowed rule it is a complete exact certificate.

**Verdict: complete computer-assisted proof, 7/7.**

## Problem 3 — 0/7

The submission does not solve the stated problem for arbitrary `n`. It proves
or claims rigorous values only for

\[
c(1)=\frac23,\qquad c(2)=\frac47,\qquad c(3)=\frac8{15},
\]

and reports a fixed-`n` computational lower-bound check for `n=4`. The proposed
general formula

\[
c(n)=\frac{2^n}{2^{n+1}-1}
\]

remains conjectural in both essential directions.

For the lower bound, the cell-complex approach reduces each fixed `n` to a
finite enumeration but supplies no structural theorem uniform in `n`. The
alternative induction/matching approach has unproved matching hypotheses and
a recorded factor-of-two gap. For the upper bound, the detailed seven-cap
construction is specific to `n=3`; no strategy is proved for every `n>=4`.
The file also records that several proposed general mechanisms, including the
strict dyadic-halving potential and a claimed Hall equivalence, are false.

Complete small cases are meaningful progress, but the universal problem is
missing its central theorem.

**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

The proof establishes exactly

\[
\theta=\frac{180^\circ}{N},\qquad N\in\mathbb Z,\ N\ge2.
\]

For sufficiency, the create move puts a multiple of `theta` in either retained
child. The subsequent peeling move replaces a `k theta` angle by a
`(k-1)theta` angle unless a child already contains `theta`, so the process
terminates. The validity of the prescribed interior cuts is handled separately
for `N=2` and `N>=3`.

For necessity, Shan-Yu begins with a triangle having no angle congruent to zero
modulo `theta`. The proof exhausts the four ways both children could acquire a
multiple of `theta`; each would force a parent angle or `180°` itself to be a
multiple, contrary to the safe-state assumptions. The geometric fact that any
split parameter strictly between 0 and the parent angle can be realized by an
interior cevian is standard.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The answer

\[
f(x)=x+c,\qquad c\ge0,
\]

is correctly established.

Putting `x=f(y)` in the original sandwich forces

\[
f(f(y))=2f(y)-y.
\]

For `g=f-id`, this says that `g` is invariant on each forward orbit and
`f^n(y)=y+n g(y)`. Positivity forces `g>=0`. Squaring the right-hand inequality
gives the correct two-point constraint

\[
4xg(y)\le (x-y)^2+2(x+y)g(x)+g(x)^2.
\]

If `g` assumed two distinct positive values, their invariant arithmetic
progressions would have arbitrarily large close encounters. The irrational
ratio case is covered by standard density, and the rational ratio case by the
corresponding Bezout/residue argument. Substitution at those encounters gives
a fixed bound on a point tending to infinity, a contradiction.

The remaining zero-value case is not waved away: a zero of `g` creates a
neighborhood on which `g=0`, and a maximal-connected-component boundary
argument expands that zero component to all of `(0,infinity)`. Thus `g` is a
single constant, possibly zero. Direct QM-AM and AM-GM verification shows that
every `x+c`, `c>=0`, works.

The text contains a cosmetic factor error in one displayed gap formula, but
the inequality and the proof do not depend on that coefficient.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

This run supplies the theorem missing from several other attempts.

The good/bad recursion is correctly oriented, and any two good integers share
a prime. The stripping lemma replaces a number containing a prime at most `k`
by a no-larger number with exactly the same small-prime support and no large
prime factors. Minimal-counterexample descent then proves the strengthened
statement: any two good numbers share a prime at most `k`, where `k=a_1`.

The greedy characterization identifies the original sequence as the increasing
enumeration of the good integers. Therefore every pair of sequence terms has a
common prime at most `a_1`.

Now classify an integer by the subset of primes at most `a_1` which divide it.
Admissibility depends only on this type and hence only on the residue modulo

\[
L_0=\prod_{p\le a_1}p.
\]

The sequence walks through the cyclically ordered admissible residues. After a
full cycle it returns to the same residue, and the gaps in one cycle sum to
`L_0`. Consequently, for a fixed cycle length `T`,

\[
a_{n+T}=a_n+L_0
\]

for every `n`, as required. Nonemptiness of the admissible residue family is
slightly implicit but immediate: sequence terms have nonempty small-prime
type, and the complete small-prime set (residue zero modulo `L_0`) is a
transversal.

**Verdict: complete, 7/7.**

## Final assessment

Five of the six solutions are complete. Problem 3 contains substantial
small-case work, but the general theorem requested by the problem remains
open, so it receives no credit under the requested standard.

**Final score: 35/42.**
