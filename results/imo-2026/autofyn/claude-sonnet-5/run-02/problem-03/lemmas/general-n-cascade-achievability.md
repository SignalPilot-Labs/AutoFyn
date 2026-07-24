## Statement

For every `n≥1`, fix the ladder configuration `p_i = 2^{n+1-i}/(2^{n+1}-1)`
for `i=1,…,n+1` (so `p_1>⋯>p_{n+1}>0`, `∑p_i=1`, `p_i=2p_{i+1}` for every
`i≤n`). For `0≤k≤n`, define the **prefix cascading-halving response**:
cut each of `p_1,…,p_k` exactly once, splitting `p_i→(p_{i+1},p_{i+1})`,
leaving `p_{k+1},…,p_{n+1}` untouched (uses `k≤n` cuts, within Xiang Yu's
budget).

**Theorem.** For every `n≥1`, both boundary cases `k=n` and `k=n-1` give
`Φ = a_n := 2^n/(2^{n+1}-1)` exactly, where `Φ(S)` denotes the sum of the
odd-sorted-rank pieces of the resulting multiset `S` (Liu Bang's
guaranteed total under the claiming-subgame reduction).

Consequence: `\min_X \Phi(\text{ladder}) \le a_n` for every `n` — the
"achievability"/tightness half of confirming the ladder attains the
conjectured value `c(n)=a_n` exactly (not just `\ge a_n`). This does
**not** establish the converse `\ge a_n` for `n\ge3` (open), nor the
general upper bound over all Liu Bang configurations (open).

## Proof

See `results/imo-2026-03/approaches/smoothing-compactness-certificate.md`,
section "General-`n` cascade achievability theorem": a direct
rank-position count. For `k=n`, the resulting multiset is
`{p_2,p_2,…,p_n,p_n,p_{n+1},p_{n+1},p_{n+1}}` (each of `p_2,…,p_n` with
multiplicity 2, `p_{n+1}` with multiplicity 3); each multiplicity-2 run
contributes its value once to `Φ` (one odd, one even rank), the
multiplicity-3 run contributes its value twice (two of its three
consecutive ranks are odd), giving
`Φ = (p_2+⋯+p_n) + 2p_{n+1} = 1-p_1+p_{n+1} = a_n` after substituting the
ladder's closed form. For `k=n-1`, the multiset is
`{p_2,p_2,…,p_{n-1},p_{n-1},p_n,p_n,p_n,p_{n+1}}`; the same run-counting
gives `Φ = (p_2+⋯+p_{n-1}) + 2p_n + 0\cdot p_{n+1} = 1-p_1+p_n-p_{n+1}
= a_n` (the `p_{n+1}` run has multiplicity 1 at an even rank, contributing
0). Both cases reduce to the identical algebraic identity
`(2^{n+1}-1)-2^n+1 = 2^{n+1}-2^n`, confirmed exactly.

No induction, case-split, or numerics needed — the argument is a single
direct computation for general `n`. Edge case `n=1` checked by hand:
`k=n=1` and `k=n-1=0` both give `Φ=2/3=a_1`.

## Certification note (round 4, proof-builder self-check)

Cross-checked by an independent exact-`Fraction` script
(`/tmp/round-4/verify_cascade.py`) for every `n=1,…,8` and both
`k\in\{n-1,n\}`: all 16 cases match `a_n` exactly (exact rational equality,
zero discrepancy) — confirming the closed-form derivation above rather
than restating the round-4 explorer's own `n≤6` numerical finding (which
had also claimed, incorrectly, that *every* `k` works — corrected by the
round-4 outline-reviewer to `k\in\{n-1,n\}` only, and it is precisely that
corrected, narrower claim that is proved here in general).

## Certification note (proof-reviewer, round 4)
**CERTIFIED.** Independently re-verified both closed-form rank-count
computations ($k=n$ and $k=n-1$) by direct exact-`Fraction`
sort-and-alternate-sum for $n=1,\dots,8$, exact match with $a_n$ in all 16
cases; also re-derived the $k=n-1$ mismatch check (`p_{n+1}` at an even
rank, contributing 0) by hand — correct. Promoted to `lemmas/`.
