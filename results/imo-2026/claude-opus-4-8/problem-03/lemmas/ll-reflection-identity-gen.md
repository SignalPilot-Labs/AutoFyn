# Lemma REFL-gen (reflection identity, relaxed hypothesis)

**Status:** CERTIFIED (proof-reviewer, round 7). Proposed by `ll-dyadic-symdiff`. Reviewer re-derived
the set proof and machine-verified `A(Q∪R) = μ − A(Q'∪R)` under the hypothesis `max(R) ≤ μ` (0 mismatch
over 2572 random rational instances); confirmed it FAILS without the hypothesis (2430/2461 mismatches
when `max(R) > μ`), so the hypothesis is exactly the one used. Strictly generalizes the certified
`lemmas/ll-reflection-identity.md` (drop `μ ≥ 2^{n−1}`).

## Statement
Let `Q` be a finite multiset of positive reals with `μ := max(Q)`, `Q' := Q ∖ {μ}` (one copy of the
maximum removed), and let `R` be a finite multiset with `max(R) ≤ μ`. With `N_P(x) = #{parts of P > x}`,
`S_P = {x : N_P(x) odd}`, `A(X∪Y) = measure(S_X △ S_Y)` (certified `lemmas/alt-sum-integral.md`), then
```
A(Q ∪ R) = μ − A(Q' ∪ R).
```

## Proof
Fix `x ∈ [0, μ)`. The removed part `μ > x`, and every other part of `Q` exceeds `x` iff it is a part of
`Q'` exceeding `x`, so `N_Q(x) = 1 + N_{Q'}(x)`; for `x ≥ μ`, `N_Q(x) = N_{Q'}(x) = 0`. Hence on `[0,μ)`,
`N_Q` odd ⟺ `N_{Q'}` even, giving `S_Q = [0,μ) ∖ S_{Q'}` with `S_{Q'} ⊆ [0,μ)` (as `max(Q') ≤ μ`). The
hypothesis `max(R) ≤ μ` gives `S_R ⊆ [0, max(R)) ⊆ [0, μ) =: U` — this is the ONLY place the certified
Lemma REFL used `μ ≥ 2^{n−1} ≥ max(R)`; the weaker `max(R) ≤ μ` suffices for the same conclusion. The
pointwise identity `(U∖A)△B = U∖(A△B)` for `A,B ⊆ U` then gives `S_Q △ S_R = U ∖ (S_{Q'} △ S_R)`, and
since `S_{Q'}△S_R ⊆ U`, `measure(U) = μ`, `A(Q∪R) = μ − A(Q'∪R)`. ∎

## Scope
Needed for the *second* reflection in the double-REFL telescoping (`ll-dyadic-symdiff`), where the removed
maximum `μ = q_1 = max(Q)` may be `< 2^{n−1}` (outside certified Lemma REFL's range) while the accompanying
`R = G_{n−2}` has `max = 2^{n−2} < q_1`, satisfying `max(R) ≤ μ`. Combined with the first reflection it
yields the double-REFL formula `A(Q∪G_{n−1}) = 2^{n−1} − q_1 + A(Q'∪G_{n−2})` (branch `q_1 > 2^{n−2}`).
