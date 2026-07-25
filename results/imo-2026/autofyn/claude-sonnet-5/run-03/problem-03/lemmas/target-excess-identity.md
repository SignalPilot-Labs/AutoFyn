## Lemma: $c(n)-\tfrac12$ closed form (target-excess identity)

**Statement.** For $c(n)=2^n/(2^{n+1}-1)$,
$$c(n)-\frac12=\frac1{2(2^{n+1}-1)}.$$

**Proof.** $2c(n)-1=\dfrac{2^{n+1}-(2^{n+1}-1)}{2^{n+1}-1}=\dfrac1{2^{n+1}-1}$,
so $c(n)-\tfrac12=\dfrac1{2(2^{n+1}-1)}$. $\blacksquare$

**Independent verification (proof-reviewer, round 6).** Checked numerically
for $n=5$: $c(5)=32/63$, $c(5)-1/2=(64-63)/126=1/126=1/(2\cdot63)$, matches
$2^{n+1}-1=63$. Trivial but confirmed exact.

**Consequence.** For a candidate single-piece-floor lower bound $F(n)$ on
some LB partition family, proving $F(n)>c(n)$ for all $n$ reduces to
proving $F(n)-\tfrac12>\tfrac1{2(2^{n+1}-1)}$ — an exponentially small
threshold in $n$. If the true excess of $F(n)$ over $1/2$ is only
polynomially small (as observed at every checked instance of the
triangular family, `lp-duality-split-polytope`'s round-6 data), a crude
non-tight polynomial lower bound on that excess suffices for all $n$ at
once.

**Source.** Proved in `approaches/lp-duality-split-polytope.md` (round 6,
Section 6 / Promotable lemmas).

**Reuse.** Reusable by any future attempt at a general-$n$ Multi-Piece
Necessity theorem for the triangular (or a similarly AP-structured)
family: only a polynomial-order lower bound on the single-piece floor's
excess over $1/2$ is needed, not the exact minimizer.
