## Statement

Fix $n\ge2$ and the $n$-ladder $p_1>\dots>p_{n+1}$. Suppose the theorem's
lower-bound direction holds for $n-1$:
$$(\star_{n-1})\qquad \text{every legal Xiang-Yu response (}\le n-1\text{
cuts) to the }(n-1)\text{-ladder gives }\Phi\ge c(n-1)=2^{n-1}/(2^n-1).$$
Then: if Xiang Yu spends exactly one cut on $p_1$, splitting it
**symmetrically** into $f_1=f_2=p_1/2$, and spends his remaining $n-1$ cuts
on the tail $\{p_2,\dots,p_{n+1}\}$ in *any* legal way whatsoever, the
resulting $\Phi\ge p_1=2^n/(2^{n+1}-1)$.

**Unconditional status.** Since $c(2)=4/7$'s lower-bound half is already
fully, rigorously, non-numerically established (all $10$ cut-distribution
cases for $n=2$ closed exactly, `smoothing-compactness-certificate`
rounds 1–2), $(\star_2)$ holds, so this statement is **unconditionally
proved for $n=3$**. For $n\ge4$ it is a valid conditional/recursive
reduction of the same shape a full induction would need, not yet an
unconditional new result, since $(\star_{n-1})$ for $n-1\ge3$ is exactly
the general lower bound this whole line of approaches is trying to close.

## Proof

Write $F=\{p_1/2,p_1/2\}=\{p_2,p_2\}$ (using $p_1=2p_2$, the exact-doubling
identity of `tail-self-similarity`) and let $G'$ be Xiang Yu's refinement of
the tail using $\le n-1$ cuts. Since $F$'s two elements are equal,
$N_F(x)\in\{0,2\}$ for every $x$ (always even), so the odd-parity indicator
$u\equiv0$ identically, and $A(F)=f_1-f_2=0$. By the general cross-term
identity `cross-term-identity-threshold` (with $F,G'$ at threshold
$r=\mathrm{Total}(G')$), the cross term vanishes and
$$A(F\cup G')=A(F)+A(G')-2\int_0^r uv = A(G').$$
By `tail-self-similarity`, $G'/r$ is a legal Xiang-Yu response (same
$\le n-1$ cuts, rescaled) to the $(n-1)$-ladder. By $(\star_{n-1})$,
$\Phi(G'/r)\ge c(n-1)$, and since $\Phi(S)=(\mathrm{Total}(S)+A(S))/2$ with
$\mathrm{Total}=1$ for the $(n-1)$-ladder, $2c(k)-1=f(k)$ for every $k$
(direct check: $2\cdot2^kf(k)-1=(2^{k+1}-(2^{k+1}-1))f(k)=f(k)$), so
$A(G'/r)\ge f(n-1)$. By the scaling lemma $A(\lambda S)=\lambda A(S)$,
$A(G')=r\cdot A(G'/r)\ge r\cdot f(n-1)=f(n)=a_n$ (the cross-level constant
of `tail-self-similarity`). Hence $A(F\cup G')=A(G')\ge a_n$, so
$\Phi(F\cup G')=(1+A(F\cup G'))/2\ge(1+a_n)/2=p_1$.

## What this does *not* cover

Asymmetric $c=1$ splits ($f_1\ne f_2$) and all $c\ge2$ (more cuts spent
fragmenting $p_1$) are **not** covered by this argument — the
"cross-term vanishes" mechanism is special to exactly two equal fragments.
Numerically, asymmetric splits are never better for Xiang Yu than the
symmetric one (checked $n=3$, several $f_1$ values,
`/tmp/round-4/check2.py`), but no proof of that dominance was found; see
`greedy-halving-adversary.md`'s Proposition 13 discussion for the concrete
trade-off witness and why the natural derivative argument fails to be
sign-definite.

## Certification note

Proof verified by hand-tracing the algebra above and cross-checked
numerically for $n=3$ (exact `Fraction` arithmetic, matches $\Phi=8/15$
exactly at the symmetric split against random tail refinements,
`/tmp/round-4/check1.py`). Depends on `tail-self-similarity`,
`cross-term-identity-threshold`, `dominant-element-removal-identity`'s
sibling scaling lemma ($A(\lambda S)=\lambda A(S)$), and (conditionally,
for $n\ge4$) the general theorem's own lower-bound half one level down.

## Origin

`results/imo-2026-03/approaches/greedy-halving-adversary.md`, Proposition
13 (round 4).

## Certification note (proof-reviewer, round 4)
**CERTIFIED (as stated — conditional for $n\ge4$, unconditional for $n=3$).**
Re-derived the proof chain step by step: $u\equiv0$ on an equal pair is
correct (parity argument), the cross-term identity instantiation is a
direct application of the certified `cross-term-identity-threshold`, the
rescaling step correctly invokes `tail-self-similarity`, and the algebra
$2c(k)-1=f(k)$ was independently re-checked symbolically. Independently
re-verified the $n=3$ conclusion by a 200000-trial exact-`Fraction` random
search over all legal tail refinements with the symmetric $c=1$ split fixed:
minimum $\Phi$ found was exactly $8/15=p_1$, never below — matching the
theorem exactly, with $(\star_2)$ imported correctly from the
already-certified $n=2$ lower-bound closure. The lemma's scope is honestly
stated (unconditional only at $n=3$; a conditional reduction for $n\ge4$
that does not yet close the general case). Promoted to `lemmas/`.
