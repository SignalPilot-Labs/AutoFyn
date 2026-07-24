## Statement

Fix $n\ge1$ and the $n$-ladder $p_i=p_i(n)=2^{n+1-i}/(2^{n+1}-1)$,
$i=1,\dots,n+1$. Let Xiang Yu spend all $n$ of his cuts fragmenting $p_1$
into $q_i:=p_1\cdot p_i(n)$ for $i=1,\dots,n+1$ (a rescaled copy of the whole
$n$-ladder, using exactly $n$ cuts for $n+1$ pieces), leaving the tail
$p_2,\dots,p_{n+1}$ completely untouched (the "$c=n$" slice of Xiang Yu's
strategy space). Then the sorted order of the resulting $2n+1$ pieces is the
strict alternation
$$q_1 > p_2 > q_2 > p_3 > q_3 > \dots > p_{n+1} > q_{n+1},$$
and consequently $\Phi = \sum_{i=1}^{n+1}q_i = p_1(n) = 2^n/(2^{n+1}-1)$
exactly — this specific Xiang-Yu strategy at $c=n$ achieves (does not merely
bound) the target value.

**Scope note (do not overclaim):** this shows only that the minimum of $\Phi$
over $c=n$ strategies is $\le p_1(n)$ (achievability). It does **not** show
$p_1(n)$ is the minimum over *all* $c=n$ strategies (that direction — the
actual lower bound — is open for $n\ge3$; see
`results/imo-2026-03/approaches/self-similar-bracketing.md`, Proposition B2,
for why this is not a free corollary).

## Proof

See `results/imo-2026-03/approaches/self-similar-bracketing.md`, Lemma B1.
Over the common denominator $D=(2^{n+1}-1)^2$: $q_i = 2^{2n+1-i}/D$ and
$p_{i+1} = 2^{n-i}(2^{n+1}-1)/D = (2^{2n+1-i}-2^{n-i})/D$ for $i=1,\dots,n$.
*Claim 1:* $q_i>p_{i+1}$ since $q_i-p_{i+1}=2^{n-i}/D>0$. *Claim 2:*
$p_{i+1}>q_{i+1}$ iff (dividing numerators by the common factor $2^{n-i}$)
$2^{n+1}-1>2^n$, i.e. $2^n>1$, true for all $n\ge1$. Chaining Claims 1–2
gives the full strict alternating chain of $2n+1$ terms (matching the total
piece count), with every $q_i$ at an odd sorted rank and every $p_{i+1}$ at
an even sorted rank ($q_i$ at position $2i-1$, $p_{i+1}$ at position $2i$).
By `claiming-subgame-reduction`, $\Phi=\sum_{\text{odd rank}}=\sum_i q_i=p_1$.

## Certification note (proof-reviewer, round 3)

Independently re-verified by direct computation for $n=1,2,3,4$ (e.g.
$n=2$: $q=(16/49,8/49,4/49)$, tail $(14/49,7/49)$, sorted
$16>14>8>7>4$ — matches the claimed alternation exactly, $\Phi=28/49=4/7$).
The proof's two elementary numerator inequalities are checked algebraically
above with no hidden step (no condition on $n$ needed beyond $n\ge1$, which
is given). Certified correct, gap-free. Certified as an **achievability**
fact only — pair with `results/imo-2026-03/approaches/
self-similar-bracketing.md`'s Proposition B2 (not itself certified as a
lemma, since it is a negative/diagnostic argument rather than a standalone
reusable identity) for why the matching minimality direction is genuinely
open, not a trivial corollary.
