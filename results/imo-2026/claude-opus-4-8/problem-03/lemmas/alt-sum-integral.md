# Lemma — Integral / measure representation of the alternating sum, merge lemma, A-bounds

**Status:** certified (proof-reviewer, round 2). All statements re-derived and verified numerically
(20000 random trials: 0 violations of the integral representation, the merge inequality, and the
bounds 0 ≤ A ≤ p_1).

## Notation
For a finite multiset of positive reals sorted p_1 ≥ p_2 ≥ … ≥ p_k, set
- A(P) := Σ_i (−1)^{i+1} p_i = (p_1 − p_2) + (p_3 − p_4) + ⋯ (the alternating sum),
- val(P) := Σ_{i odd} p_i, Σ_even(P) := Σ_{i even} p_i, T(P) := Σ p_i,
- N_P(x) := #{i : p_i > x}.
Then val = (T + A)/2 and Σ_even = (T − A)/2.

## Statement 1 (measure form)
A(P) = measure{ x ≥ 0 : N_P(x) is odd } = ∫_0^∞ 𝟙[N_P(x) odd] dx.

**Proof.** With p_{k+1} := 0, for x ∈ [p_{i+1}, p_i) exactly i pieces exceed x, so N_P(x) = i on an
interval of length p_i − p_{i+1}. Hence measure{N_P odd} = Σ_{i odd}(p_i − p_{i+1}) = (p_1−p_2) +
(p_3−p_4) + ⋯ = A(P). (Ties x = p_i form a measure-zero set.) ∎

## Statement 2 (A-bounds)
0 ≤ A(P) ≤ p_1. **Proof.** Each grouped pair (p_{2j-1} − p_{2j}) ≥ 0 gives A ≥ 0; grouping as
A = p_1 − (p_2 − p_3) − (p_4 − p_5) − ⋯ with every removed pair ≥ 0 gives A ≤ p_1. ∎

## Statement 3 (merge lemma)
For any finite multisets X, Y: val(X ∪ Y) ≥ val(X) + Σ_even(Y) (and symmetrically with X,Y swapped).

**Proof.** Counting pieces > x is additive: N_{X∪Y}(x) = N_X(x) + N_Y(x). Where N_X(x) is odd and
N_Y(x) even, the sum is odd, so {N_{X∪Y} odd} ⊇ {N_X odd} ∖ {N_Y odd}; taking Lebesgue measure and
Statement 1, A(X∪Y) ≥ A(X) − A(Y). Then val(X∪Y) = (T_X+T_Y+A(X∪Y))/2 ≥ (T_X+T_Y+A(X)−A(Y))/2 =
val(X) + (T_Y−A(Y))/2 = val(X) + Σ_even(Y). ∎

## Effect of a single cut
Cutting a length-ℓ piece into (a, ℓ−a) with smaller part s = min(a, ℓ−a) flips the parity of N on
[0, s) ∪ [ℓ−s, ℓ) (total measure 2s) and nowhere else; hence |ΔA| ≤ 2s.
