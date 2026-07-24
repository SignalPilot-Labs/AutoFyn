## Statement

For a finite multiset $S=\{L_1\ge\dots\ge L_m\}$ of positive reals, define
$A(S) := \sum_{i=1}^m (-1)^{i+1}L_i$ and $N(x):=\#\{i: L_i>x\}$. Then
$$A(S)=\int_0^\infty \mathbb 1[N(x)\text{ is odd}]\,dx,$$
and consequently $\Phi(S) = \dfrac{\mathrm{Total}(S)+A(S)}{2}$ with
$0\le A(S)\le\mathrm{Total}(S)$.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 2.
Direct: write each $L_i=\int_0^\infty\mathbb1[x<L_i]dx$, swap sum and
integral (finite sum), and observe the inner alternating sum over the
prefix $\{1,\dots,N(x)\}$ telescopes to $\mathbb1[N(x)\text{ odd}]$.

## Certification note (proof-reviewer, round 1)

Algebraically elementary and self-contained; the derivation is a direct
telescoping computation with no hidden gap. Certified correct.
