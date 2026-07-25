## Lemma: "Duplicate-the-rest" is an exact XY response to LB's geometric construction

**Statement.** Fix $n\ge1$. Let LB's partition be the geometric
construction $p_i=2^{n+1-i}/(2^{n+1}-1)$ for $i=1,\dots,n+1$ (pieces
proportional to $2^n,2^{n-1},\dots,2,1$). Let $p_1=2^n/(2^{n+1}-1)$ be the
largest piece and $R=\{p_2,\dots,p_{n+1}\}$ the other $n$ pieces
(summing to $S=(2^n-1)/(2^{n+1}-1)$). XY spends exactly $n$ of its $n$
available marks to replace $p_1$ with the $n+1$ pieces
$R\cup\{p_1-S\}$ (valid: this partitions $p_1$ into $n+1$ positive parts
using $n$ cuts, since $p_1-S=1/(2^{n+1}-1)>0$). Then the resulting
multiset has $\mathrm{OddSum}$ (LB's total, LB claiming first) exactly
$c(n)=2^n/(2^{n+1}-1)$.

**Proof.** Work unnormalized: total stick length $V=2^{n+1}-1$, pieces
$2^n,2^{n-1},\dots,2,1$ (integers); the claim $c(n)=2^n/V$ is
scale-invariant so this suffices. So $p_1=2^n$, $R=\{2^{n-1},\dots,2,1\}$
($n$ values), $S=\mathrm{sum}(R)=2^n-1$ (geometric series
$2^{n-1}+\cdots+1=2^n-1$), leftover $\ell=p_1-S=1$.

XY's new multiset is $M=R\cup R\cup\{1\}$: for each $j=1,\dots,n-1$ the
value $2^j$ appears exactly twice (once from the original untouched $R$,
once from the duplicate produced by splitting $p_1$), and the value $1=2^0$
appears three times (once from each copy of $R$, plus the leftover
$\ell=1$). Total pieces: $2n+1$.

For each $j=1,\dots,n-1$: the pair $\{2^j,2^j\}$ occupies two *consecutive*
ranks in the descending sort of $M$ (no other distinct value can lie
strictly between two copies of $2^j$, since the only repeated values in
$M$ are the $2^j$, $j=1,\dots,n-1$, and the three copies of $1$, which are
strictly smaller than every $2^j$, $j\ge1$). By Tie-neutrality
(`tie-neutrality-and-first-mover-half.md`, Lemma A), each such pair
contributes exactly one copy of $2^j$ to LB (the first claimer). Summing
over $j=1,\dots,n-1$: LB gets $\sum_{j=1}^{n-1}2^j = 2^n-2$ from these
pairs.

The three copies of $1$ occupy the bottom three ranks of the sorted list,
say ranks $2n-1,2n,2n+1$ (since $1$ is the unique minimum of $M$, all other
$2n-2$ entries strictly exceed $1$). Among positions $2n-1,2n,2n+1$: the two
outer ones $2n-1,2n+1$ are odd (LB's), the middle one $2n$ is even (XY's).
So LB gets exactly two of the three copies of $1$, contributing $2$.

Summing: LB's total $=(2^n-2)+2=2^n$, matching the unnormalized target
exactly. Dividing by $V=2^{n+1}-1$ gives $c(n)=2^n/(2^{n+1}-1)$.
$\blacksquare$

**Independent verification.** Checked by direct computation (exact integer
arithmetic, brute-force $\mathrm{OddSum}$ of the constructed multiset)
for $n=1,\dots,9$: exact match with $2^n$ in every case.

**Source.** Proved in `approaches/universal-halving-adversary.md`
("Theorem: Self-similar duplication is exactly optimal against LB's own
geometric construction"). Certified by the proof-reviewer, round 1.

**Reuse.** Shows XY has an explicit response achieving equality with $c(n)$
against LB's *specific* candidate-optimal partition, for every $n$ — this
is the "equality witness" needed to complete the still-open general upper
bound (showing no LB partition beats $c(n)$) at least in the special case
where LB actually plays the geometric construction. It does **not** by
itself establish the upper bound for arbitrary LB partitions.
