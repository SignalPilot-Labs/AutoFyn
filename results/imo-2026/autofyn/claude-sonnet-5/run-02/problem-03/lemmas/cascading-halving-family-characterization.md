## Statement

Fix $n\ge1$ and the ladder $p_i=2^{n+1-i}/D$, $D:=2^{n+1}-1$, $i=1,\dots,n+1$.
For $0\le k\le n$, let $R_k$ be the Xiang Yu response that cuts each of
$p_1,\dots,p_k$ into two exactly equal halves ($p_i\to\{p_{i+1},p_{i+1}\}$,
using $p_i/2=p_{i+1}$ for the geometric ladder) and leaves
$p_{k+1},\dots,p_{n+1}$ untouched, and let $S_k$ be the resulting multiset,
$A(S_k)$ its alternating-sum invariant (`integral-alternating-sum-formula`).
Then, writing $L:=n-k$ and $f(n):=1/D$ (the target):
$$D\cdot A(S_k) = T(L) := \frac{2^{L+1}+(-1)^L}{3},$$
and consequently
$$A(S_k)=f(n) \iff L\in\{0,1\} \iff k\in\{n-1,n\},$$
with $A(S_k)>f(n)$ strictly for every $k\le n-2$ (equivalently $T(L)>1$ for
every $L\ge2$, and $T$ is non-decreasing in $L$, strictly increasing for
$L\ge1$).

This is a genuine, fully proved, general-$n$, closed-form characterization
of an infinite sub-family of the tie-vertices identified by
`vertex-minimum-theorem` (each $R_k$ is itself exactly such a vertex: $k$
independent type-(II) "fragment = fragment" tie constraints on a
$k$-dimensional cell). It **corrects** an earlier unverified and false
conjecture (a round-4 proof-outline asserted, without proof, that *every*
$k\in\{0,\dots,n\}$ hits the target — refuted by exact `Fraction`
computation before this lemma was derived).

## Proof

See `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, "Round 4
build: the Cascading-Halving-Family Theorem," Steps 1–4.

Sketch: (1) By direct bookkeeping of the construction, $S_k$ has $p_i$
($2\le i\le k$) at multiplicity $2$, $p_{k+1}$ at multiplicity $3$, and
$p_i$ ($k+2\le i\le n+1$) at multiplicity $1$ (for $k\ge1$; $k=0$ is the
trivial all-multiplicity-$1$ case). (2) By the certified
`odd-run-reduction-lemma`, $A(S_k)$ equals the alternating sum of the
odd-multiplicity survivors, which is exactly the ladder's own tail
$\{p_{k+1},\dots,p_{n+1}\}$ — already sorted, since the ladder is
decreasing — so $A(S_k)=\sum_{j=k+1}^{n+1}(-1)^{j-k-1}p_j$. (3) Reindexing
by $t=j-k-1$ and using $p_{k+1+t}=2^{L-t}/D$ ($L=n-k$), this tail sum times
$D$ equals $T(L):=\sum_{t=0}^L(-1)^t2^{L-t}$, which satisfies the
recurrence $T(L)=2^L-T(L-1)$ (split off the $t=0$ term and reindex the
rest), solved in closed form by induction as
$T(L)=\big(2^{L+1}+(-1)^L\big)/3$. (4) $T(0)=T(1)=1$ directly from the
closed form; for $L\ge2$, $T(L)\ge3$ (even $L$) or $T(L)\ge5$ (odd $L$),
in both cases $>1$, so $T(L)=1$ forces $L\in\{0,1\}$.

## Certification note

Proposed for certification this round (round 4), not yet reviewed. Verified
independently by exact `Fraction` arithmetic (no floating point) for
$n=1,\dots,8$ and every $k=0,\dots,n$ (i.e. every $L=0,\dots,8$): the closed
form $T(L)=(2^{L+1}+(-1)^L)/3$ matches, term by term, both (a) a direct
sort-and-alternate-sum computation on the raw (non-reduced) multiset $S_k$
and (b) the odd-run-reduced tail sum — zero mismatches in all cases. The
induction proof of the closed form is elementary algebra (geometric-series
recurrence), independently checked symbolically.

## Certification note (proof-reviewer, round 4)
**CERTIFIED.** Independently re-derived the closed form $T(L)=(2^{L+1}+
(-1)^L)/3$ by direct exact-`Fraction` computation of the raw sort-and-
alternate-sum for $L=0,\dots,11$ ($n=1,\dots,11$, every $k=0,\dots,n$),
zero mismatches against the formula. Confirmed $T(L)=1\iff L\in\{0,1\}$ and
$T(L)>1$ strictly for $L\ge2$. The proof sketch's use of
`odd-run-reduction-lemma` and the multiplicity bookkeeping was checked
against the raw multiset directly, not just via the lemma, as an
independent cross-check. Promoted to `lemmas/`.
