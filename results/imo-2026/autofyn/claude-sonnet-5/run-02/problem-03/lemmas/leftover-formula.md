## Statement

If a finite multiset $R$ decomposes as $R=\{v\}\cup\{a_1,a_1'\}\cup\dots\cup
\{a_k,a_k'\}$ with each pair exactly equal ($a_i=a_i'$), then
$A(R)=v$ and $\Phi(R)=\dfrac{\mathrm{Total}(R)+v}{2}$. (Degenerate case: no
unpaired element, all paired — $A(R)=0$, $\Phi(R)=\mathrm{Total}(R)/2$.)

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 3.
Direct consequence of the integral formula: each exactly-equal pair
contributes an even amount to $N(x)$ for every $x$, so parity of $N(x)$ is
governed solely by the unpaired element $v$.

## Certification note (proof-reviewer, round 1)

Follows immediately and rigorously from the certified integral-formula
lemma; no gap. Certified correct.
