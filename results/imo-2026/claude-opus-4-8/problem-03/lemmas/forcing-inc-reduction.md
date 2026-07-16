# Lemma (Inclusion forcing + INC reduction)

**Status:** CERTIFIED (proof-reviewer, round 5). Proposed by `ll-inclusion-gap` (Steps 2–3).
Both parts re-derived by the reviewer; each is immediate and correct.

Notation: `S_P := {x ≥ 0 : N_P(x) odd}`, `A(P) = measure(S_P)` (Lemma M0), merge identity
`A(Q∪R) = A(Q) + A(R) − 2·measure(S_Q ∩ S_R)` (Lemma M), both certified in
`lemmas/alt-sum-integral.md`.

## Part 1 — Forcing Lemma
Let `Q` partition `2^n` and let `R` satisfy `max(R) ≤ 2^{n−1}`. If `S_Q ⊆ S_R` then
`max(Q) ≤ 2^{n−1}`.

*Proof.* Suppose `q_1 := max(Q) > 2^{n−1}`. Since `Σ Q = 2^n`, `q_1` is the unique part `> 2^{n−1}`,
so the second-largest part `q_2 ≤ 2^{n−1}`. For `x ∈ [2^{n−1}, q_1)` (nonempty), only `q_1` exceeds
`x`, so `N_Q(x) = 1` and `x ∈ S_Q`. But `S_R ⊆ [0, max(R)) ⊆ [0, 2^{n−1})`, so `x ∉ S_R`. Hence
`S_Q ⊄ S_R`, contradiction. ∎

## Part 2 — INC reduction
If `S_Q ⊆ S_R` then `A(Q ∪ R) = A(R) − A(Q)`.

*Proof.* `S_Q ⊆ S_R ⟹ measure(S_Q ∩ S_R) = measure(S_Q) = A(Q)`. By the merge identity,
`A(Q∪R) = A(Q) + A(R) − 2A(Q) = A(R) − A(Q)`. ∎

**Consequence.** In the inclusion branch, Lemma LL (`A(Q∪R) ≥ 1`) is equivalent to
`A(R) ≥ A(Q) + 1`.

## Scope / caution
These two parts are rigorous. They do NOT by themselves close the inclusion branch: the inequality
`A(R) ≥ A(Q) + 1` is exactly the remaining crux (open for general n). NOTE: the accompanying
"Structural Lemma" (dyadic-band parity) of `ll-inclusion-gap` is NOT certified — its claim (a)
("no part of Q lies in a forbidden-band interior") is FALSE (counterexample Q = {3/2, 3/2, 2, 3}
at n = 3 is an inclusion config with two parts in the forbidden band (1,2)); its headline conclusion
`A(Q) ≤ A(G_{n−1})` is nonetheless numerically true but needs an even-multiplicity-aware reproof.
