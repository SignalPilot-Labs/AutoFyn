# Lemma (SET IDENTITY + self-similar reduction, INC branch, R = G_{n−1})

**Status:** CERTIFIED (proof-reviewer, round 7). Reviewer independently re-derived (I)–(III) and
machine-verified the SET IDENTITY `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` (exact set equality via
parity, n = 3..8, 0 mismatch) and the generalized ΣQ-free top-band identity that consumes it
(0 mismatch over ~2000 INC configs, arbitrary ΣQ, n = 3..6, both deficit_top, M ≥ 0). Both identities
are elementary (a count differing by exactly 2). Certified.

Notation (imported): `N_P(x) = #{parts of P exceeding x}`, `S_P = {x ≥ 0 : N_P(x) odd}`,
`A(P) = measure(S_P) = Σ_i(−1)^{i+1}p_i` (parts sorted p_1 ≥ p_2 ≥ …), `G_k = {2^0,…,2^k}`,
`ΣG_k = 2^{k+1} − 1`.

## Statement

**(I) A(G_k) recursion / oddness.** For k ≥ 1, `A(G_k) = 2^k − A(G_{k−1})`; in closed form
`A(G_k) = (2^{k+1} + (−1)^k)/3`, an ODD integer with `A(G_k) ≥ 1`. Equivalently, for m ≥ 1,
`A(G_{m−1}) = 2^m − ... ` and in particular `A(G_{n−3}) = 2^{n−2} − A(G_{n−2})` (n ≥ 3).

**(II) SET IDENTITY.** For n ≥ 3,
`S_{G_{n−1}} ∩ [0, 2^{n−2}) = S_{G_{n−3}}`.
Corollary: if `S_Q ⊆ S_{G_{n−1}}` and `Q_lo := {parts of Q that are < 2^{n−2}}`, then
`S_{Q_lo} = S_Q ∩ [0,2^{n−2}) ⊆ S_{G_{n−3}}`.

**(III) Self-similar identity for M.** In the certified top-band decomposition
(`lemmas/top-band-decomposition.md`) with `M := 2^{n−2} − A(G_{n−2}) − A(Q_lo)`, one has
`M = A(G_{n−3}) − A(Q_lo)`.

## Proof

**(I)** The largest part of G_k is 2^k, occupying odd position 1 with sign +. Deleting it, the
remaining sorted list {2^{k−1},…,2^0} shifts every part up by one position, flipping all its signs;
hence `A(G_k) = 2^k − A(G_{k−1})`. With `A(G_0) = 1`, induction gives `A(G_k)` even − odd = odd, so
`A(G_k)` is an odd integer. The closed form solves the recursion: `(2^{k+1}+(−1)^k)/3` satisfies it
and matches `A(G_0)=1`; the numerator `2^{k+1}+(−1)^k ≡ (−1)^{k+1}+(−1)^k = 0 (mod 3)` and is a
positive odd number not divisible by 2, so the quotient is an odd integer ≥ 1. Setting k = n−2 in the
recursion, `A(G_{n−2}) = 2^{n−2} − A(G_{n−3})`, i.e. `A(G_{n−3}) = 2^{n−2} − A(G_{n−2})`.

**(II)** For `x ∈ [0, 2^{n−2})` both parts `2^{n−2}` and `2^{n−1}` of `G_{n−1}` exceed x, and
`G_{n−1} = G_{n−3} ∪ {2^{n−2}, 2^{n−1}}` (a disjoint union of parts, since `G_{n−3} = {2^0,…,2^{n−3}}`).
Hence `N_{G_{n−1}}(x) = N_{G_{n−3}}(x) + 2`, so the two counts have the same parity on `[0,2^{n−2})`:
`{x < 2^{n−2} : N_{G_{n−1}}(x) odd} = {x < 2^{n−2} : N_{G_{n−3}}(x) odd}`. All parts of `G_{n−3}` are
`≤ 2^{n−3} < 2^{n−2}`, so `N_{G_{n−3}}(x) = 0` for `x ≥ 2^{n−2}` and therefore
`S_{G_{n−3}} = {x < 2^{n−2} : N_{G_{n−3}}(x) odd}`. Combining gives the identity. The corollary is
immediate: `S_{Q_lo} = S_Q ∩ [0,2^{n−2})` (the h high parts of Q are ≥ 2^{n−2}, hence contribute an
even count on [0,2^{n−2}) by part (a) of the top-band decomposition, so parity on [0,2^{n−2}) is that
of `N_{Q_lo}`), and `S_Q ⊆ S_{G_{n−1}}` gives `S_Q ∩ [0,2^{n−2}) ⊆ S_{G_{n−1}} ∩ [0,2^{n−2}) =
S_{G_{n−3}}`.

**(III)** `M = 2^{n−2} − A(G_{n−2}) − A(Q_lo)`; substitute `2^{n−2} − A(G_{n−2}) = A(G_{n−3})` from (I).
∎

## Scope
This packages the structural engine of the two-step strong induction `n → n−2` for G-INC-1 in
`ll-inclusion-gap`: the SET IDENTITY sends the INC constraint on `Q_lo` down two dyadic levels
(`S_{Q_lo} ⊆ S_{G_{n−3}}`), and (III) rewrites the residual `M` as a level-(n−3) alternating-sum
deficit `A(G_{n−3}) − A(Q_lo)`, exactly matching the level-(n−2) induction hypothesis.
