## Statement

For any finite multiset $T$ of positive reals and any $a>0$,
$$A(\{a,a\}\cup T) = A(T),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order functional
of the certified `integral-alternating-sum-formula` lemma.

## Proof

See `results/imo-2026-03/approaches/exchange-argument-extremal-response.md`,
Lemma E2. For every $x\ge0$, $N_{\{a,a\}\cup T}(x) = 2\cdot\mathbb1[a>x] +
N_T(x)$, and $2\cdot\mathbb1[a>x]\in\{0,2\}$ is always even, so
$N_{\{a,a\}\cup T}(x)$ and $N_T(x)$ have the same parity for every $x$. By the
certified `integral-alternating-sum-formula` lemma, $A(S)=\int_0^\infty
\mathbb1[N_S(x)\text{ odd}]\,dx$ depends only on the parity function of $N_S$,
so $A(\{a,a\}\cup T)=A(T)$.

## Certification note (proof-reviewer, round 3)

Independently re-verified by an exact-`Fraction` script (20000 random trials,
multisets of size 1–8 plus a random injected equal pair, comparing direct
sort-and-alternate-sum before/after removing the pair): zero mismatches. The
proof is a one-line consequence of the integral/parity characterization of
$A$ already certified in `integral-alternating-sum-formula` — no gap, and it
requires no adjacency or ordering assumption on the pair within $T$ (unlike a
naive "adjacent transposition" argument, the parity argument works
regardless of where $a$'s two copies land in the sorted order). Strictly
generalizes `leftover-formula` (whose exactly-equal pairs are each an
instance of this lemma, applied repeatedly) and is the elementary building
block underlying the more general `odd-run-reduction-lemma`. Certified
correct, fully general — no game-specific structure required.
