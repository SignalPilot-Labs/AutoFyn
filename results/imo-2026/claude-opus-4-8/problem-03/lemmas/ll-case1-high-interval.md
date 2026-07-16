# Lemma (LL Case-1: high-interval disjointness)

**Status:** CERTIFIED (proof-reviewer, round 5). Proposed jointly by `ll-dyadic-symdiff`
(Case 1) and `ll-inclusion-gap` (GAP-branch Case-1) — same lemma, one canonical file.
Reviewer re-derived the interval argument from scratch and confirmed it.

## Statement
Let `Q` be a partition of `2^n` (n ≥ 1) into positive parts, and let `R` be any finite multiset
with `max(R) ≤ 2^{n−1}`. Write `A(·)` for the alternating sum and `S_P := {x ≥ 0 : N_P(x) odd}`,
`N_P(x) = #{parts of P exceeding x}`. Then
```
A(Q ∪ R) = measure(S_Q △ S_R) ≥ max(Q) − 2^{n−1}   (when max(Q) > 2^{n−1}).
```
In particular, if `max(Q) ≥ 2^{n−1} + 1` then `A(Q ∪ R) ≥ 1`.

## Proof
Let `μ := max(Q)`. Since `Σ Q = 2^n`, at most one part of `Q` can exceed `2^{n−1}` (two parts each
`> 2^{n−1}` would sum to `> 2^n`); so `μ` is the unique such part. For any `x ∈ [2^{n−1}, μ)`:
- Every part other than `μ` is `≤ 2^{n−1} ≤ x`, so only `μ` exceeds `x`: `N_Q(x) = 1` (odd).
- `max(R) ≤ 2^{n−1} ≤ x`, so `N_R(x) = 0`.

Hence `N_{Q∪R}(x) = 1` is odd for every `x ∈ [2^{n−1}, μ)`, so `[2^{n−1}, μ) ⊆ S_Q △ S_R`, giving
`measure(S_Q △ S_R) ≥ μ − 2^{n−1}` (using the certified identity `A(X∪Y) = measure(S_X △ S_Y)`,
`lemmas/alt-sum-integral.md`). If `μ ≥ 2^{n−1} + 1` this is `≥ 1`. ∎

## Scope
This closes the "high largest-part" slice of Lemma LL (t ≥ 2) unconditionally on the internal
structure of `R` (only `max(R) ≤ 2^{n−1}` is used). The residual `max(Q) < 2^{n−1} + 1` is NOT
covered and remains the open crux of Lemma LL, t ≥ 2. Reviewer-verified: n = 3, 8310 configs with
`max(Q) ≥ 5`, 0 violations.
