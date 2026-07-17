# Lemma GreedyCascade — dominant-piece cascade (certified round 7)

**Setup.** Odd-sum marking game (Lemma G1); A = μ{N odd} evaluated by Lemma X as the XOR of
prefix intervals; D = 2^{n+1}−1, c(n) = 2^n/D. LB's final pieces b_1 ≥ … ≥ b_p, Σ b_i = 1,
p ≤ n+1 (so p−1 ≤ n cuts available to XY).

**Statement.** If **b_1 ≥ 1/2**, then XY, using p−1 ≤ n cuts, forces
    **A = 2 b_1 − 1.**
Consequently, if additionally b_1 ≤ c(n) then A ≤ 2c(n) − 1 = 1/D, i.e. O ≤ c(n).

**Proof.** XY cascades the top piece b_1, matching each other piece with a fragment of b_1.
Set r_1 = b_1. For j = 1,…,p−1 cut the running leftover r_j at position b_{j+1}, producing a
fragment of length b_{j+1} and a new leftover r_{j+1} = r_j − b_{j+1}. Then
r_j = b_1 − (b_2 + … + b_j), and the final leftover is
    r_p = b_1 − (b_2 + … + b_p) = b_1 − (1 − b_1) = 2b_1 − 1 ≥ 0   (using b_1 ≥ 1/2).

*Legality.* The cut at b_{j+1} requires 0 < b_{j+1} ≤ r_j = b_1 − (b_2+…+b_j), i.e.
b_1 ≥ b_2 + … + b_{j+1}. Since b_1 ≥ 1/2 ≥ 1 − b_1 = b_2 + … + b_p ≥ b_2 + … + b_{j+1}, this
holds. Strictness (positive leftover) fails only at the last step when b_1 = 1/2, where
r_{p−1} = b_p already, so the intact copy of b_p is present and the final cut is unneeded
(p−2 cuts suffice); then A = 2b_1 − 1 = 0. In all cases ≤ p−1 cuts are used.

*Final multiset.* b_2,…,b_p remain intact; b_1 is split into the fragments b_2,…,b_p and the
leftover r_p. So each length b_j (j ≥ 2) appears exactly twice — once intact, once as a fragment.
In A = μ(⊕_i [0, ℓ_i]) (Lemma X), two equal lengths cancel: [0,b_j] ⊕ [0,b_j] = ∅. Only [0, r_p]
survives, so A = μ([0, 2b_1 − 1]) = 2b_1 − 1. ∎

**Consequence.** Closes the Case-B sub-region **B2-large: 1/2 ≤ a_1 ≤ c(n), all n** with an
explicit closed-form (p−1)-cut strategy (uniform in n; no gap conditions; not a q-induction, so
immune to the r6 fixed-point obstruction). Since c(n) = 2^n/(2^{n+1}−1) > 1/2 for all n, the
interval [1/2, c(n)] is nonempty.

**Machine check (reviewer, round 7).** Simulated the cascade and evaluated A by XOR over 3000
exact random configs (n = 2..7, b_1 ≥ 1/2): A = 2b_1 − 1 with 0 failures. Boundary b_1 = 1/2
gives A = 0.

**Certification.** Reviewer-verified round 7. Statement is a pure conditional (no empirical
percentage), proof sorry-free, derived from certified Lemmas G1, R, X. The legality bound and the
final-multiset pairing were re-derived independently. Admitted to shared cache.

**Scope.** Requires a dominant piece b_1 ≥ 1/2. B2-small (a_1 < 1/2) is NOT covered and remains
open (the adaptive fragment-cascade wall, same as the IH(q≥5) flat residual).
