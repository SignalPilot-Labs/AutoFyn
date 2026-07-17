# Lemma f-homogeneous — 1-homogeneity of the min-strategy value (certified round 8)

**Setup.** Odd-sum marking game (Lemma G1); A = μ(⊕_i [0,ℓ_i]) is the XOR-of-prefix-intervals
evaluator (Lemma X). For a length vector b = (b_1 ≥ … ≥ b_q > 0) in the positive cone,
f(b) := min over XY cut-strategies using ≤ q−1 cuts of A.

**Statement.** For every b in the positive cone {b_1 ≥ … ≥ b_q > 0} and every λ > 0,
    **f(λb) = λ f(b).**

**Proof.** Parametrise an XY strategy by (P, φ): P a combinatorial cut pattern (which current part each
of the ≤ q−1 cuts acts on, in order), φ a vector of fractions ρ ∈ (0,1) placing each cut at absolute
position ρL on a current part of length L (splitting it into ρL and (1−ρ)L). This parametrisation is
scale-free: the admissible set of (P, φ) does not depend on b.

Fix (P, φ) and run it on b and on λb in lockstep. By induction on cuts executed, every current part in
the λb-run equals λ times the corresponding part in the b-run: initial parts b_i vs λb_i; a fraction-ρ
cut sends x → (ρx, (1−ρ)x) and λx → (ρλx, (1−ρ)λx) = λ(ρx,(1−ρ)x). Hence the final length multiset on
λb is λ times that on b. Since A depends only on the length multiset (Lemma X) and
⊕_part [0, λ·part] = λ·(⊕_part [0,part]), scaling every length by λ scales A by λ:
A(λb,(P,φ)) = λ A(b,(P,φ)). Taking the min over the common strategy set (λ > 0 commutes with min),
f(λb) = λ f(b). ∎

**Note.** Homogeneity is on the positive *cone*, not on K_q as a set (K_q's constraints Σ ≤ S,
b_q ≥ 1/D are not scale-invariant). Used only to migrate the max onto the σ-face (Lemma σ-migration).
