# Lemma P (parity of the piece count)

**Status:** certified (proof-reviewer, round 3). Elementary; verified numerically (20000 samples,
odd piece count, all pieces ≥ 1: 0 violations).

## Statement
Let a finite multiset of pieces have an **odd** number k of elements, each of length **≥ 1**. Then the
alternating sum A = Σ_i (−1)^{i+1} p_i (pieces sorted p_1 ≥ … ≥ p_k) satisfies A ≥ 1.

## Proof
Write k = 2r + 1 and group
  A = (p_1 − p_2) + (p_3 − p_4) + ⋯ + (p_{2r−1} − p_{2r}) + p_{2r+1}.
Each parenthesised pair is ≥ 0 by sortedness, and the trailing term is p_k = min piece. Hence
A ≥ p_k ≥ 1. ∎

## Application scope
In the geometric lower bound (unnormalized G_n, target A ≥ 1): if Xiang Yu makes t cuts producing
k = (n + 1) + t pieces, then k is odd iff t ≡ n (mod 2), and the extra "all pieces ≥ 1" hypothesis holds
precisely when Xiang Yu never cuts a piece below length 1. This is a genuine but **restricted** family of
Xiang Yu responses. It does NOT cover the residual lower-bound gap (t ≥ 2 with some piece < 1 or wrong
parity), which remains open.
