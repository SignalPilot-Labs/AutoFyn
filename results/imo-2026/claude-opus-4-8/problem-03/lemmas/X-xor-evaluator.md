# Lemma X — XOR/parity evaluator + cut toggle (certified round 4)

**Setup.** In the odd-sum marking game (Lemma G1), once cuts are fixed and pieces are sorted,
LB's take is the odd-sum O = (1+A)/2 with A the sorted alternating sum, and by Lemma R (certified)
A = μ{t : N(t) odd}, N(t) = #{pieces of length > t}. Total length = 1.

**Statement (evaluator).** For a finite multiset of positive lengths {ℓ_1,…,ℓ_m}, place each as an
interval [0, ℓ_i]. Then
    A = μ( [0,ℓ_1] ⊕ [0,ℓ_2] ⊕ … ⊕ [0,ℓ_m] ),   ⊕ = symmetric difference.

*Proof.* A point t lies in ⊕_i [0,ℓ_i] iff it lies in an odd number of the [0,ℓ_i], i.e. iff
#{i : ℓ_i ≥ t} is odd. This differs from N(t) = #{i : ℓ_i > t} only on the finite (measure-zero)
set {ℓ_i}. Hence μ(⊕_i [0,ℓ_i]) = μ{t : N(t) odd} = A (Lemma R). ∎

**Statement (cut toggle).** Cutting a piece of length ℓ into (m, ℓ−m) with 0 < m ≤ ℓ/2 replaces
[0,ℓ] by [0,m], [0,ℓ−m]; in the XOR this multiplies the running set by the toggle set
    T = [0,ℓ] ⊕ [0,m] ⊕ [0,ℓ−m] = [0,m] ∪ (ℓ−m, ℓ]   (Lebesgue measure 2m).

*Proof.* [0,ℓ] ⊕ [0,m] = (m, ℓ] (as [0,m] ⊂ [0,ℓ]). Then, using m ≤ ℓ−m, (m,ℓ] ⊕ [0,ℓ−m] has
union [0,ℓ] and intersection (m, ℓ−m], so the symmetric difference is [0,ℓ] ∖ (m, ℓ−m] =
[0,m] ∪ (ℓ−m, ℓ]. ∎

**Machine check (reviewer, round 4).** For every random ℓ, m ≤ ℓ/2, A_of{m, ℓ−m} = ℓ − 2m,
matching [0,ℓ] ⊕ T = (m, ℓ−m] (measure ℓ−2m). Verified in exact rational arithmetic.

**Certification.** Reviewer-verified round 4. Both statements correct, proofs sorry-free, derived
from certified Lemma R. Admitted to shared cache. Reusable exact scoring tool for any cutting
strategy (evaluate A of any final multiset by XOR of prefix intervals).
