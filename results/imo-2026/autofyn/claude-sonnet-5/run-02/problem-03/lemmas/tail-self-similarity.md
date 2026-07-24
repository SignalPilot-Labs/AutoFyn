## Statement

For the $n$-ladder ($n\ge1$), $p_i=2^{n+1-i}f(n)$, $f(n):=1/(2^{n+1}-1)$,
let $r:=1-p_1=\sum_{i=2}^{n+1}p_i$ (the total of the tail). Then:

1. **(Tail self-similarity.)** The rescaled tail $\{p_2,\dots,p_{n+1}\}/r$ is
   *exactly* the $(n-1)$-ladder: if $q_1>\dots>q_n$ denotes the
   $(n-1)$-ladder ($q_i=2^{n-i}f(n-1)$, $f(n-1)=1/(2^n-1)$), then
   $p_{i+1}/r=q_i$ for every $i=1,\dots,n$.
2. **(Exact doubling.)** $p_1=2p_2$ for every $n\ge1$.
3. **(Cross-level constant.)** $r\cdot f(n-1)=f(n)$.

## Proof

$p_{i+1}=2^{n-i}f(n)$ directly from the ladder formula. By the geometric-sum
formula, $r=1-p_1=1-2^nf(n)=(2^{n+1}-1-2^n)f(n)=(2^n-1)f(n)$ (using
$f(n)=1/(2^{n+1}-1)$). Hence
$$\frac{p_{i+1}}r=\frac{2^{n-i}f(n)}{(2^n-1)f(n)}=\frac{2^{n-i}}{2^n-1}=2^{n-i}f(n-1)=q_i,$$
since $f(n-1)=1/(2^n-1)$ by definition. This proves (1). For (2):
$p_1=2^nf(n)=2\cdot2^{n-1}f(n)=2p_2$. For (3):
$r\cdot f(n-1)=(2^n-1)f(n)\cdot\frac1{2^n-1}=f(n)$.

## Certification note

Proved by direct closed-form algebra (no case analysis, no numerics
required for correctness) and cross-checked by exact `Fraction` arithmetic
for $n=1,\dots,7$ (`/tmp/round-4/verify_general.py`). Fully general — this
is the precise, general-purpose form of the "self-similarity" that several
sibling approaches (`self-similar-potential-certificate`,
`self-similar-bracketing`, `rank-tie-vertex-reduction`) have informally
leaned on without stating this cleanly. Any future induction-on-$n$
argument for this problem should cite this lemma directly rather than
re-deriving the rescaling from scratch.

## Origin

`results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemmas 11–12
(round 4). Used by Proposition 13 (symmetric-split $c=1$ lower bound) in
the same file.

## Certification note (proof-reviewer, round 4)
**CERTIFIED.** Re-derived all three closed-form identities from scratch
(geometric-tail sum for $r$, the ratio $p_{i+1}/r$, the doubling
$p_1=2p_2$, and $r\cdot f(n-1)=f(n)$) and independently cross-checked by
exact-`Fraction` arithmetic for $n=1,\dots,8$ — zero discrepancies.
Elementary, fully general, no gap. Promoted to `lemmas/`.
