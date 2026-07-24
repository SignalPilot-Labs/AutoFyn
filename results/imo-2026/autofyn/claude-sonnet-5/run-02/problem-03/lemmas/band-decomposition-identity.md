## Statement

For any finite multiset $F$ of positive reals and any finite reference
multiset $T$ of positive reals, writing $N_F,N_T$ for the exceedance-count
functions, $\psi(x):=N_T(x)\bmod2$, $w(x):=1-2\psi(x)\in\{+1,-1\}$, and
$e(x):=N_F(x)\bmod2\in\{0,1\}$:
$$A(F\cup T) = A(T) + \int_0^\infty e(x)\,w(x)\,dx.$$

Fully general — no ladder-specific structure used; isolates $A(F\cup T)-
A(T)$ as a signed integral of $F$'s own parity pattern against a fixed
weight function determined entirely by $T$.

## Proof

By `integral-alternating-sum-formula`, $A(S)=\int_0^\infty
\mathbb1[N_S(x)\text{ odd}]\,dx$. Here $N_{F\cup T}=N_F+N_T$, so its parity
is $e(x)\oplus\psi(x)$. Using $u\oplus v=u(1-v)+v(1-u)$ for $\{0,1\}$-valued
$u,v$ and expanding: $\int(e\oplus\psi)=\int\psi\,dx+\int e(1-2\psi)\,dx
=A(T)+\int e\,w$.

## Verification (proof-reviewer, round 5)

Independently re-derived the algebraic expansion (elementary XOR identity
plus linearity of the integral) — no gap. Cross-checked numerically as a
special case of the round-5 counterexample computation (Proposition 3 of
`dyadic-band-occupancy.md`), which implicitly uses this decomposition and
whose numeric values were independently reproduced exactly.

## Origin / usage

Derived in `results/imo-2026-03/approaches/dyadic-band-occupancy.md` §1
(round 5, new slug). Used to derive the cardinality-relaxed-minimum-is-zero
result (`claim-a-cardinality-is-essential.md`) and to diagnose why a coarse
per-band occupancy invariant is insufficient (Proposition 3, refuted, see
approach file).

## Certification note (proof-reviewer, round 5)
**CERTIFIED.** Fully general, gap-free, independently re-derived and
cross-checked. Promoted to `lemmas/`.
