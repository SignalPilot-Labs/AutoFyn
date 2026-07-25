## Source
`approaches/self-similar-induction-on-n.md`, round 18. Certified by the
round-18 proof-reviewer after independent re-derivation (own `sympy`
symbolic algebra and exact-`Fraction`/constrained-`scipy` scripts, not
reusing the builder's).

## Lemma 1 (Sharper residual-range for $\mathrm{GT}(m)$ sub-case (i), odd
excess $e=1$)

For every $k\ge2$, write $m=k+1$ (excess $e=1$). Recall the certified
Half-Sum Corollary route gives, for $D=\{a_1\}\cup R$ with
$a_1\in(2^{k-1},2^k]$, $\max(R)\le2^{k-1}$, $\mathrm{sum}(D)=2^m$:
$$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\frac{2^k}6+\frac{2^m}6
-\frac{a_1}2-\frac12,$$
a general-purpose algebraic identity (independently re-derived
symbolically, matches exactly). Specializing to $m=k+1$:
$$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\frac{2^k-a_1-1}2,$$
which is $\ge0$ **iff $a_1\le2^k-1$**. Hence $\mathrm{GT}(m)$ sub-case
(i) at $e=1$ is already closed, via the already-certified Half-Sum
Corollary, for every $a_1\in(2^{k-1},2^k-1]$ — the genuinely open
residual is exactly the width-$1$ window $a_1\in(2^k-1,2^k]$ at the
*top* of the range, not the whole previously-believed-open range
$[2^{k-1}+1,2^k]$.

*Independent verification.* `sympy` symbolic re-derivation of both the
general identity and its specialization at $m=k+1$: exact match (see
review notes, round 18).

## Lemma 2 (Cardinality-Constrained Half-Sum Lemma, $k=2$ instance)

For $R$ a finite multiset with $\max(R)\le2$, $|R|\le3$,
$\mathrm{sum}(R)=S\in[4,5)$:
$$\mathrm{OddSum}(R\cup\{2,1\})\ \ge\ \frac{S+4}2,$$
with equality attained (e.g. the symmetric tie configuration
$R=\{b,b,1\}$, $b=(S-2)/2$).

*Proof (exhaustive casework on $n:=|R|\in\{2,3\}$).*
- $n=2$: $R=\{a,b\}$, $a,b\le2$ forces $a+b\le4$; combined with $S\ge4$
  forces $S=4$, $a=b=2$, giving $\mathrm{OddSum}=4=(S+4)/2$ exactly.
- $n=3$, $a=2$ (tie with $\Gamma_1$'s own top): removing both copies of
  the value $2$ (occupying ranks $1,2$) preserves the parity of every
  lower rank, giving $\mathrm{OddSum}(M)=2+\mathrm{OddSum}(\{b,c,1\})$
  with $b+c=S-2\in[2,3)$. A three-way split on $b,c$ vs. $1$ gives
  $\mathrm{OddSum}(\{b,c,1\})\ge(b+c)/2+1$ in every feasible sub-case
  (verified), so $\mathrm{OddSum}(M)\ge(S+4)/2$.
- $n=3$, $a<2$ (no element reaches the cap, so $\Gamma_1$'s own $2$ is
  the unique global max): the Global-Max Peeling identity gives
  $\mathrm{OddSum}(M)=2+\mathrm{EvenSum}(\{a,b,c,1\})$; splitting on $a$
  vs. $1$ ($a\le1$ is vacuous since it forces $S\le3<4$) and applying the
  elementary rank-shift identity $\mathrm{EvenSum}(S)=
  \mathrm{OddSum}(S\setminus\{\max\})$ again gives
  $\mathrm{OddSum}(M)\ge(S+4)/2$, strictly, in every sub-case.

Combined with Lemma 1's reduction: $\mathrm{GT}(m)$ sub-case (i), $e=1$,
$k=2$ ($m=3$) is fully closed for every $a_1\in(2,4]$.

*Independent verification (reviewer, own scripts).* `scipy.optimize`
constrained minimization (`LinearConstraint` sum$=S$ exactly, `Bounds`
$[0,2]$ per coordinate, multi-restart `SLSQP`), $n\in\{2,3\}$, $S$
sampled densely in $[4,5)$: minimum observed margin
$\approx1.2\times10^{-12}$ (machine-precision zero), attained at
interior points — matching the proof's claimed equality locus, zero
violations across all sampled configurations.

## Known cosmetic (non-load-bearing) error in the source file, corrected
here

The source proof's "$n=3,a=2$" branch, sub-case "$b\ge1>c$," asserts the
boundary case $S=4$ "is not attained... $c<1$ forces $b>2$." This is
false: e.g. $b=1.5,c=0.5$ satisfies $b\ge1>c$, $b+c=2=S-2$ at $S=4$,
$b\le2$ — a genuine feasible equality point in this sub-case (distinct
from the "symmetric point" the source names as the sole equality
locus). This does **not** affect the lemma's validity: the required weak
inequality $\mathrm{OddSum}(\{b,c,1\})\ge(b+c+2)/2$ still holds (with
equality, not strictness) in this sub-case; only the incidental
"strictness" side-remark in the source is wrong. Certified with this
correction noted; the sub-case's required inequality itself is
independently re-verified correct.

## Explicitly NOT certified

The **general** Cardinality-Constrained Half-Sum Lemma (arbitrary $k$),
stated in the source file as a conjecture verified only numerically to
$k=2,\ldots,6$: **not proved**, not certified. Do not cite as a theorem.
