## Statement

For the $n$-ladder ($n\ge2$), the explicit partition
$F^*=\{p_2,p_3,\dots,p_n,\,p_{n+1},p_{n+1}\}$ of $p_1$ (using $n-1$ cuts,
well within Xiang Yu's budget of $n$) satisfies
$$A(F^*\cup\{p_2,\dots,p_{n+1}\}) = p_{n+1} = a_n := \frac1{2^{n+1}-1}$$
exactly. (For $n=1$: $F=\{p_1\}$, $A=p_1-p_2=a_1$ directly.)

This proves the achievability half of "claim (A)" ($\min_F A(F\cup T)\le
a_n$, tail $T$ untouched) completely, for every $n\ge1$.

## Proof

$F^*$ sums to $p_1$: using $p_i=2p_{i+1}$ repeatedly,
$\sum_{i=2}^np_i+2p_{n+1}=r+p_{n+1}=p_1$ (since $r=p_{n+1}(2^n-1)$ and
$p_1=2^np_{n+1}$). The multiset $F^*\cup T$ is
$\{p_2,p_2,p_3,p_3,\dots,p_n,p_n,p_{n+1},p_{n+1},p_{n+1}\}$: each pair
$\{p_i,p_i\}$ ($2\le i\le n$) occupies two consecutive sorted ranks and
contributes $0$ to $A$ regardless of starting parity; the final triple
$\{p_{n+1},p_{n+1},p_{n+1}\}$ starts at an odd rank ($2(n-1)$ ranks used by
complete pairs, an even number) and contributes $+p_{n+1}-p_{n+1}+p_{n+1}
=p_{n+1}$. Summing gives $A=p_{n+1}=a_n$.

## Verification (proof-reviewer, round 5)

Independently re-verified by exact-`Fraction` computation for $n=2,\dots,8$:
constructed $F^*$, checked it sums to $p_1$ exactly, and computed
$A(F^*\cup T)$ by direct sort-and-alternate-sum — matches $a_n$ exactly in
every case, zero mismatches. The sign-bookkeeping proof was independently
re-derived and found gap-free.

## Origin / usage

Derived in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §2
(round 5). Gives, for the first time, an explicit closed-form tight
Xiang-Yu response for the "tail untouched" sub-case, usable by any future
approach needing a concrete witness.

## Certification note (proof-reviewer, round 5)
**CERTIFIED.** Fully general (every $n\ge1$), gap-free, independently
re-verified. Promoted to `lemmas/`.
