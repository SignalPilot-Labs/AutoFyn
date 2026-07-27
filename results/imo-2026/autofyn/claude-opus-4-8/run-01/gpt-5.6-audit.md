# GPT-5.6 audit of `autofyn/claude-opus-4-8/run-01`

## Scope and grading standard

I audited the selected `current.md` for Problems 1–6 against the corresponding
statements in `problems.jsonl`, following the load-bearing cited lemmas. For
Problem 2 I read `code/README.md` first, inspected the recovered builder and
post-run verifier, and independently executed the exact certificate.

I use the requested harsh completion-based IMO standard: a complete proof, or
one needing only a genuinely tiny local correction, receives 7. A missing
load-bearing theorem receives 0; substantial partial progress is not assigned
invented partial credit without a problem-specific marking scheme. Exact,
reproducible code is allowed. Status labels, reviewer approval, and numerical
tests are not treated as proof by themselves.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete exact computer-assisted proof | 7/7 |
| 3 | Explicitly incomplete in both general minimax directions | 0/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Complete small-prime descent and finite-state proof | 7/7 |
| **Total** |  | **35/42** |

## Problem 1 — 7/7

For each prime `p`, the move sends the two selected valuations to

\[
(a,b)\mapsto(\min(a,b),|a-b|),
\]

so the gcd of the complete valuation list is invariant.

The lexicographic pair `(N,P)`, with `N` the number of nonunits and `P` the
product of all board entries, strictly decreases. A coprime move lowers `N`;
a noncoprime move either lowers `N` or keeps it fixed while lowering `P` by the
selected gcd. Thus every play terminates.

At a terminal board at most one nonunit remains. The per-prime valuation-gcd
invariant excludes the all-ones board and determines the survivor by

\[
v_p(M)=\gcd_i v_p(x_i^{(0)}).
\]

Lemma 5' contains a false sentence: a prime dividing one initial entry need not
give a positive gcd of all 2026 valuations, because another entry may have
valuation zero. The required conclusion is nevertheless repaired in one line.
A move cannot replace two selected nonunits by `(1,1)`, because the product of
the two outputs is `lcm(m,n)>1`. Hence the number of nonunits decreases by at
most one; starting positive and stopping at `N<=1`, it must stop at `N=1`.
This is a genuinely tiny local repair and does not affect the termination or
uniqueness argument.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The proof gives a trigonometric parametrization with

\[
0<\theta<B,\quad 0<\theta<C,\quad
0<\gamma<C-\theta,\quad0<\beta<B-\theta.
\]

The two remaining angle conditions become the closing relations

\[
\sin\gamma\sin C\sin(A+2\theta+\gamma)
=2\sin A\sin(\theta+\gamma)\sin(C-\theta-\gamma),
\]

and its `B,beta` analogue. The derivation by the sine rule is correct, with all
cleared factors positive on the physical range.

The target `OM=ON` is reduced by the circumcentre formula to

\[
2(|u|^2v_2-|v|^2u_2)=D(1-2A_x),
\]

where `D` is the nonzero signed double area of `AKL`. Half-angle substitutions
`t=tan(gamma/2)` and `s=tan(beta/2)` convert the closing relations to quartics
`P(t)=0`, `Q(s)=0` and the target to a polynomial `TN=0`.

The pseudo-division certificate is

\[
\operatorname{lc}(P)\operatorname{lc}(Q)TN=fP+gQ
\]

modulo the three Pythagorean relations. Its leading coefficients are

\[
-2\sin A\sin\theta\sin(C-\theta),\qquad
-2\sin A\sin\theta\sin(B-\theta),
\]

both nonzero on the physical domain. Thus this is not merely generic ideal
membership: division by the leading coefficients is valid for every allowed
configuration.

The retained artifact is unusually well documented. `gb2_build.py` was
recovered verbatim from the run log; `verify_certificate.py` independently
rebuilds all three polynomials, verifies both pseudo-division identities and
the reduction modulo the Pythagorean ideal, and emits explicit cofactors. I
executed it. It reported

```text
deg_t P = 4, deg_s Q = 4
f terms: 1058, g terms: 840
certificate lc(P)*lc(Q)*TN = f*P + g*Q (mod rho): True
```

The audit sandbox then prevented the script's final attempt to overwrite the
already-retained `certificate_cofactors.txt`; that happened after the exact
verification returned `True` and is irrelevant to the certificate.

All denominator and branch conditions used by the half-angle substitution are
covered by the strict angle inequalities above. Hence `P=Q=0` implies `TN=0`,
which is equivalent to `OM=ON`.

**Verdict: complete exact computer-assisted proof, 7/7.**

## Problem 3 — 0/7

The file is candidly marked partial and does not contain a full proof. The
proposed answer is

\[
c(n)=\frac{2^n}{2^{n+1}-1},
\]

but central cases remain open in both directions.

For Liu Bang's lower bound, the confined dyadic case and numerous parity and
majorization lemmas are established. The remaining unconfined `L2` case is
reduced to a within-group flat move on the tight face `E_F=O_G`; the submission
explicitly states that no monovariant or closing move is proved there.

For Xiang Yu's upper bound, several regions are closed, including the reducible
case, all cases through `q=4`, and two dominant-piece cascades. For general
`q>=5`, the bulk flat residual

\[
b_1<S/2,\qquad b_2<(S-b_1)/2
\]

remains open. The proposed vertex-maximization route is rejected because the
value function is nonconvex, and the three-level greedy cascade is recorded as
insufficient. Computations and exact verification of the surrounding lemmas do
not prove either missing general case.

These are not editorial omissions; they are the two remaining minimax cores.

**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

The proof correctly characterizes the winning values as

\[
\theta=\frac{180^\circ}{m},\qquad m\ge2.
\]

For such a value, the seed move creates a positive multiple of `theta` in both
children, and the peeling move decreases that multiple until `theta` itself is
reached.

For `180°/theta` nonintegral, let `F` be the finite set of positive multiples
of `theta` below `180°`. The four-case split lemma is exhaustive: if both
children of an `F`-free triangle contained an `F`-angle, one would force a
parent angle to lie in `F`, or force `(a+b)theta=180°`. Both contradict the
invariant. An `F`-free starting triangle exists by avoiding finitely many
values in an isosceles one-parameter family. Shan-Yu can therefore keep an
`F`-free child forever.

The AND-OR rank argument correctly translates this invariant into failure of
any finite Mulan strategy. All cut legality and positivity conditions are
handled.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The complete answer is

\[
f(x)=x+c,qquad c\ge0.
\]

Putting `x=f(y)` in the original sandwich gives

\[
f(f(y))=2f(y)-y.
\]

For `g=f-id`, every forward orbit is arithmetic, `g` is orbit-invariant, and
positivity forces `g>=0`. The squared right inequality gives the correct
off-diagonal estimate. By choosing increasingly large points on one orbit and
nearest points on another, the proof forces any two positive values of `g` to
be equal.

It remains to exclude coexistence of zero and that unique positive value `c`.
For `z` with `g(z)=0` and `b` with `g(b)=c`, the proof derives

\[
(b-z)^2\ge4cz.
\]

This makes both level sets open. Since `(0,infinity)` is connected, only one
can be nonempty, so `g` is constant. Finally, direct square identities verify
all translations with `c>=0`.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

The proof closes the difficult finite-prime step through a valid
minimum-height descent.

Call the prime support of a term a clause. The key lemma states that any two
clauses share a prime at most `a_1`. Assuming a violating pair `S_j,S_k` of
minimum height `k`, the earlier clause `S_j` contains a large prime. Let `R` be
the product of its small primes and choose the least power multiplier so that

\[
x=p_0^nR\ge a_1.
\]

The size lemma correctly proves

\[
a_1\le x<a_j,
\]

while `supp(x)` is exactly the small shadow of `S_j` and is disjoint from
`S_k`.

If `x` is a term, pairwise noncoprimality with `a_k` gives an immediate
contradiction. If it is not a term, the first earlier clause missed by `x`
forms a violating pair of smaller height with `S_j`. Both cases contradict
minimality, proving the small-common-prime lemma.

For an inclusion-minimal clause, its small shadow then hits every clause and is
itself realized as a clause. Minimality forces the clause to contain only
primes at most `a_1`. Hence only finitely many minimal clauses exist. Membership
in the global admissible set consequently depends on residues modulo the
product `M` of their finitely many primes. Once all minimal clauses have
appeared, every finite admissibility set equals the global one, so the greedy
sequence enumerates a periodic residue set and satisfies

\[
a_{n+T}=a_n+M
\]

for all positive `n`. The supporting finish package correctly explains why the
identity holds from the beginning, not just eventually.

No circularity or false large-prime inference was found.

**Verdict: complete, 7/7.**

## Final assessment

Problems 1, 2, 4, 5, and 6 are complete. Problem 3 contains extensive and
carefully labeled progress, but its two remaining general cases are precisely
the load-bearing minimax arguments.

**Final score: 35/42.**
