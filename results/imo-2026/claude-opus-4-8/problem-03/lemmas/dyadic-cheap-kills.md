# Lemmas K1, K2, REFL-telescope (all-n LL cheap-kills + reflection termination)

**Status:** CERTIFIED (proof-reviewer, round 9). Proposed by `ll-dyadic-symdiff`. All follow from the
certified merge identity (Lemma M) `A(Q∪R) = A(Q) + A(R) − 2B`, `B := measure(S_Q ∩ S_R)`,
`0 ≤ B ≤ min(A(Q),A(R))`, and the certified `ll-reflection-identity-gen`. Reviewer re-derived each.

## K1 (small-overlap kill), all n
If `2B ≤ A(Q)` (in particular `S_Q ∩ S_R = ∅` ⟹ `B = 0`) then `A(Q∪R) ≥ A(R) ≥ 1`.
*Proof.* `A(Q∪R) = A(Q) + A(R) − 2B ≥ A(Q) + A(R) − A(Q) = A(R) ≥ 1`. ∎

## K2 (difference kill), all n
Always `A(Q∪R) ≥ |A(Q) − A(R)|`; hence `|A(Q) − A(R)| ≥ 1 ⟹ A(Q∪R) ≥ 1`.
*Proof.* `B ≤ min(A(Q),A(R))` ⟹ `A(Q∪R) ≥ A(Q)+A(R)−2min(A(Q),A(R)) = |A(Q)−A(R)|`. ∎

## REFL-telescope (reflection termination), all n
For any finite positive multiset `P` with `|P| = m`, set `P_0 = P`, `μ_i = max(P_i)`,
`P_{i+1} = P_i ∖ {μ_i}`. Then `A(P) = μ_0 − μ_1 + ⋯ + (−1)^{m−1} μ_{m−1}`, terminating in exactly `m`
steps at `∅`.
*Proof.* Piece count strictly decreases by 1 each step (well-founded, `Σ` also strictly decreases by
`μ_i > 0`), reaching `∅` in `m` steps. Each step applies certified `ll-reflection-identity-gen` with
`Q = {μ_i}`, `R = P_{i+1}` (hypothesis `max(R) ≤ μ_i` holds), giving `A(P_i) = μ_i − A(P_{i+1})`;
unroll, `A(∅) = 0`. ∎

## Scope
K1/K2 fire whenever `S_Q,S_R` are near-disjoint or their alternating sums differ by `≥ 1`; they partially
cover refined-R bucket (iii) at all n. REFL-telescope only **recomputes** `A(P)`; termination alone does
NOT prove the bottom object `A(Q'∪R'') ≥ 1` — that is the refined-R alternating-tail crux, open for
`n ≥ 4`. The full n=3 top-cut bucket (iii) is closed separately (min A = 1, 10912 configs verified).
