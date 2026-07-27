# GPT-5.6 audit of `zcode/glm-5-2/run-01`

## Scope and grading standard

I audited the six submitted Markdown solutions against the corresponding
statements in `problems.jsonl`. For Problem 2 I also inspected and executed
the retained exact algebra verifier in `code/om_on_proof_verify.py`.

I used the requested harsh, completion-based IMO standard. A complete proof
receives 7; a proof with a genuine but uniquely local, mechanical repair
receives 6. A missing load-bearing argument or a wrong answer receives 0;
substantial progress does not by itself earn partial credit. Code is accepted
when it constitutes a reproducible rigorous certificate rather than a
numerical experiment.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete exact computer-assisted proof | 7/7 |
| 3 | Both general bounds contain load-bearing gaps | 0/7 |
| 4 | Correct characterization, but the interval/cut lemma needs a local repair | 6/7 |
| 5 | Wrong characterization; valid translations are omitted | 0/7 |
| 6 | Central lemma and passage from eventual to global periodicity are unproved | 0/7 |
| **Total** |  | **20/42** |

## Problem 1 — 7/7

For every prime `p`, a move sends the two selected valuations

\[
(a,b)\longmapsto(\min(a,b),|a-b|).
\]

This preserves the gcd of the complete list of `p`-adic valuations. The proof
also gives a valid well-founded termination argument: a move either increases
the number of entries equal to 1, or, when both outputs remain nonunits,
strictly decreases the total prime-factor multiplicity. Thus every play
terminates with at most one nonunit.

The valuation-gcd invariant excludes the all-ones board and determines the
remaining number prime by prime. Therefore the terminal value is independent
of all choices.

The sentence saying that a relevant `D_p` is positive because it “divides a
positive integer” is imprecise. The actual reason is that it is the gcd of a
nonempty collection of positive valuations, zeros being harmless under
`gcd(0,e)=e`. This is a tiny wording repair and does not affect the proof.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The prose uses a rational half-angle coordinate parametrization. It constructs
`K` and `L`, translates the two remaining angle hypotheses into polynomial
equations `fA=fB=0`, clears the circumcentre equation for `OM=ON` to a target
polynomial `TGT`, and claims

\[
TGT\in\langle fA,fB\rangle.
\]

The enormous polynomials are omitted from the Markdown, so the prose alone
would not be independently checkable. Here, however, the missing exact work is
retained in `code/om_on_proof_verify.py`. I ran that verifier. It rebuilds the
ray directions, intersections, angle polynomials, and target from the original
coordinate definitions, computes a Gröbner basis over
`Q[p,q,a,u,v]`, and reduces the target exactly. Its decisive output was:

```text
remainder of TGT mod <fA,fB> = 0
```

The accompanying 25/25 numerical check is only corroboration; the score rests
on the exact zero remainder.

The nonzero factors discarded in forming `fA` and `fB` are nonzero on a real
admissible configuration, and the argument uses the angle equations only in
the necessary direction. Therefore possible extraneous algebraic solutions do
not threaten the implication. The intersection denominators and the
circumcentre determinant are likewise nonzero for the configuration in the
problem.

Under the explicit rule that correct code is allowed, this is a reproducible
exact certificate and earns full credit.

**Verdict: complete computer-assisted proof, 7/7.**

## Problem 3 — 0/7

The claimed value is

\[
c(n)=\frac{2^n}{2^{n+1}-1},
\]

but neither required general inequality is proved.

### Lower bound

The induction isolates the largest initial piece `L` and then considers only
the cases in which it contributes one or two final pieces. That restriction is
false: Xiang Yu may place several of his marks inside the same initial piece,
so `L` can produce as many as `n+1` final pieces. The matching/parity cases in
the submission do not handle this possibility. Consequently the proposed Liu
Bang strategy is not established.

### Upper bound

The final Case C merely says to recurse after halving a piece and asserts that
the decreasing thresholds must force arrival in Case A or B within the cut
budget. It does not prove that the updated state satisfies the hypotheses of
the next invocation, that the budget and thresholds evolve as claimed, or
that a closing case must be reached. The file itself earlier recognizes this
region as the unresolved part. Although a pair of identical banked fragments
can cancel in an alternating sum, that observation does not supply the missing
recursive invariant or termination argument.

These are the two central directions of the problem, not tiny omissions.

**Verdict: incomplete, 0/7.**

## Problem 4 — 6/7

The characterization

\[
\theta=\frac{180^\circ}{n},\qquad n\ge2,
\]

is correctly proved.

When `180°/theta` is nonintegral, Shan-Yu can start from a triangle whose three
scaled angles are nonintegral. The cut identities show that if one child gains
an integral scaled angle, the other child remains entirely nonintegral. This
gives a valid invariant avoiding `theta` forever.

When `180°/theta=n` is integral, the peeling step correctly reduces an
integer angle `k` until angle 1 is reached. The preceding seed argument,
however, lists `(a,b+c)` as one of the cut-realizable intervals and uses it
in the proof. That interval is generally not realizable by a cevian split.
The list also duplicates `(b,a+b)` and omits valid intervals, so this is
more than cosmetic notation.

The seed lemma has a short repair. Let `a=min(a,b,c)` and
`m=ceil(a)`. Then `m` lies in at least one of the two realizable intervals

\[
(a,a+b),\qquad(a,a+c).
\]

Indeed, if both upper endpoints were at most `m`, then
`n+a=(a+b)+(a+c)<=2m`. For `n>=3`, using `a<=n/3` and
`m<a+1` gives simultaneously `n-a<2` and `n-a>=2n/3>=2`, a
contradiction; `n=2` is immediate because then `m=1`. Choosing the
corresponding apex and setting `sigma=m-a` gives integral angles `m` and
`n-m` in the two children.

The submitted cut parameter also has a local formula error: in the general
interval `m in (v,u+v)`, it must be `sigma=m-v`, not
`sigma=n-w-m`. With these two local corrections, both children are good and
the peeling argument completes the proof.

**Verdict: complete after a local interval/cut repair, 6/7.**

## Problem 5 — 0/7

The submitted answer, `f(x)=x` only, is false. In fact every

\[
f(x)=x+c\qquad(c\ge0)
\]

satisfies the problem: the middle expression is

\[
\frac{f(x)+y}{2}=\frac{x+(y+c)}2=\frac{x+f(y)}2,
\]

so the two inequalities are precisely QM-AM and AM-GM applied to `x` and
`f(y)=y+c`. Thus, for example, `f(x)=x+1` is an immediate counterexample to
the claimed uniqueness.

The exact fatal step is the purported quadratic analysis leading to
`f(x)<=x` or `f(x)>=sqrt(2)x`. After squaring the left inequality, the true
condition is

\[
2x^2+2f(y)^2-(f(x)+y)^2\ge0.
\]

The submission rewrites this as

\[
y^2-2f(x)y+2x^2-f(x)^2\ge0,
\]

which has silently replaced the indispensable term `2f(y)^2` by `2y^2`.
There is no basis for that replacement. Everything eliminating positive
translations depends on this invalid quadratic dichotomy.

The earlier valid identity

\[
f(f(y))=2f(y)-y
\]

does not repair the proof; translations satisfy it as well.

**Verdict: wrong answer and load-bearing algebra error, 0/7.**

## Problem 6 — 0/7

The central Key Lemma is asserted rather than proved, and one of its stated
justifications is internally inconsistent.

In Case 1, the proof replaces a minimal admissible `m*` by `m'=m*-p0` and
claims that the required gcd conditions remain true. It says
`m* congruent m' (mod s_i)` for primes `s_i` dividing `m*`. But
`m*-m'=p0`, so this congruence would require `s_i|p0`; since both are primes,
that means `s_i=p0`, exactly the case the paragraph purports to exclude.
Admissibility of `m*` therefore gives no reason for `m'` to keep a common
factor with each earlier term.

Case 2 similarly says that “tracing the divisibility” produces a small common
prime. The displayed facts `q|a_n+d`, `s|a_n`, and `0<d<q` do not imply the
required conclusion. This is the heart of the bounded-prime argument, so all
later finite-state reasoning is conditional on an unproved theorem.

There is also an independent last-step error. The finite-state discussion
would yield a relation only after some index `N`. The claim that one may
“shift indices” and thereby obtain the required identity for every positive
`n` is invalid: eventual affine periodicity does not automatically cover the
initial prefix.

Finite computations for selected starting values cannot prove either missing
universal statement.

**Verdict: incomplete, 0/7.**

## Final assessment

Problems 1 and 2 are complete. Problem 4 has the correct characterization and
strategy but needs a short interval/cut repair. Problems 3 and 6 lack their
load-bearing general arguments. Problem 5 is not merely incomplete: it gives
the wrong family and relies on an explicit invalid algebraic rewrite.

**Final score: 20/42.**
