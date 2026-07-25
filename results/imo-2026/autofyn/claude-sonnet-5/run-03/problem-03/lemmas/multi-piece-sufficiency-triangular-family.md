# Certified (round 10): Multi-Piece Sufficiency Theorem for the triangular
# family

Certified from `approaches/lp-duality-split-polytope.md` (round 10, "the
Multi-Piece Sufficiency Theorem" section).

## Setting

The triangular family: $p_i=(n+2-i)/D_n$, $D_n=N(N+1)/2$, $N=n+1$, landmarks
$\{1,\dots,N\}$ in $d$-units, $d=1/D_n$. $\mathrm{OddSum}(X)=\tfrac12+\tfrac
d2\mathrm{AltSum}(X')$ for any legal XY response $X$ (dimensionless image
$X'=X/d$) — a direct, self-contained scaling identity (not dependent on any
single-piece-split framing), re-derived and verified below.

## Theorem (Multi-Piece Sufficiency)

For every $n\ge3$ ($N=n+1\ge4$), the triangular-family partition admits an XY
response using exactly $n$ cuts — splitting landmarks $N$ into $(N-1,1)$,
landmark $N-1$ into $(N-1-\varepsilon_N,\varepsilon_N)$, each landmark
$j=2,\dots,N-2$ into $(j/2,j/2)$, and leaving landmark $1$ unsplit, with
$\varepsilon_N:=\mathrm{Thr}(N)/4$, $\mathrm{Thr}(N):=D_n/(2^N-1)$ — achieving
$$\mathrm{OddSum}=\frac12+\frac{\varepsilon_N}2=\frac12+\frac12\Bigl(c(n)-
\frac12\Bigr)<c(n),$$
with exact margin $c(n)-\mathrm{OddSum}=\tfrac12(c(n)-\tfrac12)$, for every
$n\ge3$ simultaneously.

**Proof.** (1) $\mathrm{Thr}(N)<1$ for $N\ge4$ (induction: $N(N+1)/2\le2^N-2$,
base $N=4$: $10\le14$; step uses $N+1<2^N$ for $N\ge4$), so $0<\varepsilon_N<
1/4$. (2) Cut count is exactly $N-1=n$ (two 1-cut splits at landmarks $N,N-1$,
one 1-cut split each at $N-3$ landmarks $2,\dots,N-2$), legal, all fragments
positive. (3) The descending sort order is: $N-1$; $N-1-\varepsilon_N$; pairs
$j/2,j/2$ for $j=N-2,\dots,3$ (empty range if $N=4$); four copies of $1$ (from
landmark $N$'s "1" fragment, landmark $2$'s $(1,1)$ split, and unsplit landmark
$1$); $\varepsilon_N$ alone at the bottom — verified by comparing every
adjacent pair of values under $0<\varepsilon_N<1/4\le N/2$. (4) By the
Even-Block-Neutrality Lemma (an isolated block of $2t$ tied copies, distinct
from every other value, contributes $0$ to AltSum and does not shift any other
element's rank parity — proved by the standard "even shift preserves parity"
argument), every middle pair and the block of four $1$'s contributes $0$;
the top pair contributes $(N-1)-(N-1-\varepsilon_N)=\varepsilon_N$; the final
element, at rank $2N-1$ (always odd), contributes $+\varepsilon_N$. Total:
$\mathrm{AltSum}(X')=2\varepsilon_N$. (5) Substituting into the scaling
identity and using $dD_n=1$, $d\cdot\mathrm{Thr}(N)=1/(2^N-1)$, and the
certified identity $c(n)-\tfrac12=\tfrac1{2(2^{n+1}-1)}$
(`lemmas/target-excess-identity.md`), $\mathrm{OddSum}(X)=\tfrac12+\tfrac1
{4(2^N-1)}=\tfrac12+\tfrac12(c(n)-\tfrac12)<c(n)$ (strict since $c(n)>1/2$ for
every finite $n$). $\blacksquare$

## Independent verification (reviewer)

Re-implemented the construction from scratch (exact `Fraction` arithmetic,
independent of the builder's script): for every $N=4,\dots,39$ (36 instances),
verified (a) the fragment multiset sums exactly to $D_n$; (b) the exact
alternating sum $\mathrm{AltSum}(X')$ (computed directly via literal sort, with
a correctly-signed alternating sum — not merely "sum of odd ranks") equals
$2\varepsilon_N$ exactly; (c) the final $\mathrm{OddSum}$ equals $\tfrac12+
\tfrac12(c(n)-\tfrac12)$ exactly and is strictly less than $c(n)$ in every
case. Zero deviations across all 36 instances.

## Consequence

Combined with the already-certified Multi-Piece Necessity Theorem
(`lemmas/idx1-closure-and-full-multi-piece-necessity.md`, every $idx$, every
$n\ge3$), this gives a complete Necessity+Sufficiency picture for the
triangular family: no single-piece response suffices, but a genuinely
multi-piece response (using the full cut budget) always does, with comfortable
margin, for every $n\ge3$.

## Scope (honest)

This resolves the sufficiency question for the triangular family specifically.
It does **not** resolve the general balanced-region upper-bound direction:
other balanced partitions (in particular ones close to LB's own extremal
geometric partition) are not covered, and the construction relies on the
landmarks being a full consecutive-integer run (an AP-specific structural
feature). A numerical (non-exact) check in the source approach file found the
analogous construction does not work on LB's geometric partition — consistent
with the geometric partition being the true extremal case, not further
evidence either way for the general theorem.
