# GPT-5.6 audit of `zcode/glm-5-2/run-02`

## Scope and grading standard

I audited `problem-01.md` through `problem-06.md` against the corresponding
statements in `problems.jsonl`. I read the Problem 2 artifact README before
inspecting and executing its exact verifier.

I use the requested harsh completion-based IMO standard: 7 for a complete
proof or one needing only a genuinely tiny local repair; 0 when a
load-bearing argument is missing. No partial credit is manufactured without a
problem-specific marking scheme. Correct reproducible code is accepted, but
numerical experiments and claims that a computation succeeded are not proof.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete exact computer-assisted proof | 7/7 |
| 3 | Both minimax directions remain unproved | 0/7 |
| 4 | Complete | 7/7 |
| 5 | Complete after a small local repair | 7/7 |
| 6 | Central lemma is false as argued; global periodicity does not follow | 0/7 |
| **Total** |  | **28/42** |

## Problem 1 — 7/7

For each prime `p`, the selected valuations change by

\[
(a,b)\mapsto(\min(a,b),|a-b|),
\]

which preserves their gcd. Hence `G_p=gcd_i v_p(a_i)` is invariant.

The lexicographic measure `(k,P)`, where `k` is the number of nonunits and `P`
the product of all entries, proves termination. If a move creates a 1 then `k`
drops; otherwise the gcd is at least 2, `k` is unchanged, and `P` drops by that
gcd factor. At termination `k<=1`, while the valuation invariant excludes
`k=0`. The sole nonunit has valuation `G_p` at every prime and is therefore
choice-independent.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The computer-assisted algebra is retained and reproducible. After following
the README, I ran `code/groebner_proof.py`. It reconstructs `A,B,C,M,N,K,L`,
forms the two oriented-angle polynomial conditions, verifies their displayed
factorizations, constructs the exact numerator `P` of the circumcentre's
`x`-coordinate, and reduces it modulo

\[
\langle R_m,R_n,c^2+s^2-1\rangle
\]

over the exact coefficient ring `ZZ[a,h]`. The decisive output is:

```text
DOMAIN ZZ[a,h]
remainder of O_x-numerator P modulo the ideal:
0
```

The removed factors are nonzero on an admissible configuration, and the
circumcentre denominator is nonzero because `A,K,L` are noncollinear. The
angle equations are used only in the necessary direction, so extra algebraic
branches would not invalidate the implication.

**Verdict: complete exact certificate, 7/7.**

## Problem 3 — 0/7

The submission itself repeatedly recognizes that the two essential claims are
not proved.

For the lower bound it establishes the parity estimate only when Xiang Yu's
cut locations are integral in the chosen scale. Piecewise linearity does not
extend that estimate to arbitrary real cuts. Even if a minimum is attained at
a rational vertex, the parity argument applies to integer piece lengths and
does not imply the same lower bound at an arbitrary rational vertex.

For the upper bound it gives a response only to Liu Bang's proposed geometric
partition. To prove a minimax upper bound, Xiang Yu needs a strategy against
every initial placement of Liu Bang's marks. Sharpness on the configuration
used for the lower bound reverses the quantifiers and is insufficient. The
final note explicitly concedes that the universal upper bound is absent.

**Verdict: incomplete in both directions, 0/7.**

## Problem 4 — 7/7

The characterization

\[
\theta=\frac{180^\circ}{n},\qquad n\ge2,
\]

is proved correctly.

When `180°/theta=n` is integral, Phase A chooses the largest scaled angle `c`
and an integer `m` in `(a,a+c)`. The resulting split puts integer angles `m`
and `n-m` in the two possible children. Phase B decreases an integer multiple
`k` to `k-1` unless the retained child already contains angle 1, so the process
terminates.

When the ratio is nonintegral, the all-nonmultiple state is nonempty. The four
possible ways both children could acquire multiples force one of the parent
angles, or the total angle, to be a multiple. Hence Shan-Yu can retain a safe
child forever.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The answer is correctly

\[
f(x)=x+c,\qquad c\ge0.
\]

Putting `x=f(y)` in the sandwich gives

\[
f(f(y))=2f(y)-y.
\]

For `c(x)=f(x)-x`, this yields `c(f(x))=c(x)` and
`f^n(x)=x+n c(x)`, so positivity forces `c(x)>=0`. The rewritten upper
inequality

\[
p^2+2p(x+y)\le (x-y)^2+2q^2+4yq
\tag{U'}
\]

is correct. The arithmetic-progression orbit argument rules out two distinct
positive drift values.

The zero-drift case is garbled in the draft but is locally repairable using
its existing construction. Once the only possible values are 0 and `p>0`, set
`Z={c=0}`, `P={c=p}`, and `alpha=inf P`. The interval-avoidance lemma implies
`alpha>0`; choose `y_k in Z` increasing to `alpha` and `x_k in P` decreasing
to `alpha`. Applying (U') with `q=0` gives

\[
p^2+2p(x_k+y_k)\le(x_k-y_k)^2.
\]

The limit says `p^2+4p alpha<=0`, impossible. The draft instead momentarily
chooses an unjustified point `alpha+epsilon in P` and inserts incorrect right
side terms, but immediately states the intended positive-versus-vanishing
limit. Replacing that sentence by the two sequences above is a small local
repair, not a new strategy.

Finally every translation is verified by QM-AM-GM.

**Verdict: complete after a small local repair, 7/7.**

## Problem 6 — 0/7

The central Lemma 2 contains a false divisibility inference. In Case B, from

\[
\gcd(m^*,a_{i_0})=1,\quad \gcd(m,a_{i_0})>1,\quad m=m^*+r,
\]

the proof asserts `gcd(m,a_i0)=gcd(r,a_i0)`. If a prime `q` divides both `m`
and `a_i0`, then `q` does not divide `m*`, and
`r=m-m*` is congruent to `-m*`, not 0, modulo `q`. Thus the stated premises
normally imply the opposite of the asserted conclusion. Case A replaces the
missing descent by phrases such as “on the next descent step” and “tracing
this link backwards,” without a valid divisibility chain.

There is a second independent fatal gap. A relation

\[
a_{n+T}=a_n+L\qquad(n\ge i)
\]

cannot be made true for every `n>=1` merely by replacing `T,L` by multiples.
Backward stepping eventually enters the uncontrolled initial prefix.

**Verdict: incomplete, 0/7.**

## Final assessment

Problems 1, 2, 4, and 5 are complete, with a short local correction required
in Problem 5. Problems 3 and 6 lack load-bearing universal arguments.

**Final score: 28/42.**
