# Lemma REFL (general reflection identity)

**Status:** CERTIFIED (proof-reviewer, round 6). Proposed by `ll-dyadic-symdiff`. Reviewer
re-derived the set identity from scratch and machine-verified `A(Q∪R) = μ − A(Q'∪R)` over 2282
budget-valid n=3 instances (0 mismatches). Extends the certified `max(Q)=2^{n−1}` identity to the
whole range `μ ≥ 2^{n−1}`.

## Statement
Let `Q` be a finite multiset of positive reals with `μ := max(Q)`, let `Q' := Q ∖ {μ}` (one copy of
the maximum removed), and let `R` be a finite multiset with `max(R) ≤ 2^{n−1}`. Write
`N_P(x) = #{parts of P exceeding x}`, `S_P := {x ≥ 0 : N_P(x) odd}`, and (certified,
`lemmas/alt-sum-integral.md`) `A(X∪Y) = measure(S_X △ S_Y)`. If `μ ≥ 2^{n−1}` then
```
A(Q ∪ R) = μ − A(Q' ∪ R).
```
Equivalently, `A(Q∪R) ≥ 1` iff the upper bound `A(Q'∪R) ≤ μ − 1` holds.

## Proof
Fix `x ∈ [0, μ)`. The removed part `μ` satisfies `μ > x`, and every other part of `Q` exceeds `x`
iff it is a part of `Q'` exceeding `x`; hence `N_Q(x) = 1 + N_{Q'}(x)`. For `x ≥ μ` no part of `Q`
exceeds `x`, so `N_Q(x) = N_{Q'}(x) = 0`. Therefore on `[0,μ)`, `N_Q` odd ⟺ `N_{Q'}` even, and above
`μ` neither set has mass, giving
```
S_Q = [0, μ) ∖ S_{Q'}    (★),
```
where `S_{Q'} ⊆ [0,μ)` because `max(Q') ≤ μ`. Since `μ ≥ 2^{n−1} ≥ max(R)`, also `S_R ⊆ [0,μ)`. Put
`U := [0,μ)`. For any `A, B ⊆ U` the pointwise identity `(U ∖ A) △ B = U ∖ (A △ B)` holds: for
`x ∈ U`, `x ∈ (U∖A)△B ⟺ (x∉A) xor (x∈B) ⟺ ¬((x∈A) xor (x∈B)) ⟺ x ∉ A△B`. Applying it with
`A = S_{Q'}`, `B = S_R` and (★) (and noting `S_Q△S_R` has no mass in `[μ,∞)`),
```
S_Q △ S_R = (U ∖ S_{Q'}) △ S_R = U ∖ (S_{Q'} △ S_R).
```
As `S_{Q'} △ S_R ⊆ U` with `measure(U) = μ`,
`A(Q∪R) = measure(S_Q△S_R) = μ − measure(S_{Q'}△S_R) = μ − A(Q'∪R)`. ∎

## Scope
For `μ = 2^{n−1}` this recovers the earlier `max(Q)=2^{n−1}` reflection; the lemma covers the whole
band `μ ∈ [2^{n−1}, ∞)`. It converts the lower bound `A(Q∪R) ≥ 1` (branches `max(Q) ≥ 2^{n−1}`) into
the single upper-bound target `A(Q'∪R) ≤ μ − 1`. **Non-circular:** `Q'∪R` has total sum
`2^{n+1} − μ − 1 ≠ 2^n − 1`, so it is not a valid `G_{n−1}`-refinement and (RED) is proved as an
upper bound, never by re-invoking the induction hypothesis on `Q'∪R`. The residual `A(Q'∪R) ≤ μ − 1`
(GAP-A) and the complementary branch `max(Q) < 2^{n−1}` (GAP-B) remain OPEN.
