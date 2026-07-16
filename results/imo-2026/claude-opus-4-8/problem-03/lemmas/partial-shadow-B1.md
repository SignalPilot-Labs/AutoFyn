# Lemma (Partial-shadow prefix, upper bound Regime B / sub-case B1)

**Status:** CERTIFIED (proof-reviewer, round 5). Reviewer independently re-derived the chain
Σ R' = 1 − 2A_1 + 2s, Σ_even(R') ≥ p_2 ≥ s, A(R') ≤ 1 − 2A_1, val ≤ 1 − A_1 and confirmed each step;
re-verified val ≤ 1 − A_1 over 17961 random flat configs (exact Fractions, m ≤ 9): 0 violations.
Verified numerically by builder: key facts `val ≤ 1 − A_1`, `A(R') ≤ 1 − 2A_1`,
`Σ_even(R') ≥ s` each hold with **0 violations over 80000 random flat configs** (m ≤ 9); B1 within its
regime 0/5482 fail `val ≤ c(n)`; n = 2 exhaustive DENOM = 84 all ≤ 4/7.

Imports: Lemma G (val = (T+A)/2, T = 1), Lemma M0 (A = measure{N odd}, doubling parity-invisibility),
and the identity Σ_odd − Σ_even = A, Σ_odd + Σ_even = T.

## Statement

Let Liu Bang's pieces be A_1 ≥ A_2 ≥ … ≥ A_m (m ≤ n + 1, Σ A_i = 1) with **A_1 < 1/2**. Then Xiang Yu,
using at most n cuts, can force

  **val(final) ≤ 1 − A_1.**

Consequently, if in addition **A_1 ≥ 1 − c(n)** (sub-regime B1), then val(final) ≤ c(n), where
c(n) = 2^n/(2^{n+1} − 1).

## Proof

Since A_1 < 1/2, A_2 + ⋯ + A_m = 1 − A_1 > A_1. Let **k** be the largest index with 2 ≤ k ≤ m and
A_2 + ⋯ + A_k ≤ A_1. Then k ≥ 2 (A_2 ≤ A_1), and k < m (the full tail A_2 + ⋯ + A_m = 1 − A_1 > A_1),
so **A_{k+1} exists**. Put **s := A_1 − (A_2 + ⋯ + A_k) ≥ 0**; by maximality of k, A_2 + ⋯ + A_{k+1} > A_1,
so **s < A_{k+1}**.

Xiang Yu cuts A_1 at the interior partial sums A_2, A_2 + A_3, …, A_2 + ⋯ + A_k, carving A_1 into
{A_2, …, A_k, s} (drop s if s = 0). This uses ≤ k − 1 ≤ m − 1 ≤ n cuts, all interior to A_1 (distinct
from LB's marks and from each other), a legal move.

The final multiset is F = {A_2, …, A_k doubled} ∪ R', where **R' := {s} ∪ {A_{k+1}, …, A_m}**. Each
value A_i (2 ≤ i ≤ k) occurs twice, contributing an even amount to N_F(x) for all x, so
N_F(x) ≡ N_{R'}(x) (mod 2) and by Lemma M0 **A(F) = A(R')**; by Lemma G, val(F) = (1 + A(R'))/2.

Now Σ R' = s + (A_{k+1} + ⋯ + A_m) = s + (1 − A_1 − (A_2 + ⋯ + A_k)) = s + 1 − A_1 − (A_1 − s) =
**1 − 2A_1 + 2s**. Sort R' as p_1 ≥ p_2 ≥ …. Both A_{k+1} (≥ s) and s are elements of R', so at least two
elements are ≥ s, whence **p_2 ≥ s** and Σ_even(R') = p_2 + p_4 + ⋯ ≥ p_2 ≥ s. Therefore

  A(R') = Σ R' − 2·Σ_even(R') ≤ (1 − 2A_1 + 2s) − 2s = **1 − 2A_1**,

and val(F) = (1 + A(R'))/2 ≤ (1 + 1 − 2A_1)/2 = **1 − A_1**.

If A_1 ≥ 1 − c(n) then 1 − A_1 ≤ c(n), giving val ≤ c(n). ∎

## Scope note

Gives val ≤ 1 − A_1 for **every** flat config (any n, m), but this bounds val by c(n) only when
A_1 ≥ 1 − c(n) (sub-regime B1). For A_1 < 1 − c(n) (sub-regime B2) one has 1 − A_1 > c(n) and XY must
spend leftover cuts on R' — open for general n (closed at n = 2 by a separate two-cut move). The naive
"one cut of A_1 at A_2" is the k = 2 special case (forced when m = 3) and does **not** suffice for m > 3.
