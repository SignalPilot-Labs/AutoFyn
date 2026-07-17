# Lemma IH-reducible — pure conditional one-step reduction (certified round 6)

**Context (Case-B hard-regime upper bound).** For q pieces b_1 ≥ … ≥ b_q > 1/D, D = 2^{n+1}−1,
define IH(q): "if all b_i > 1/D and S = Σ b_i < (2^q − 1)/D, then XY forces A ≤ 1/D with ≤ q−1 cuts."
By Lemma X a pair of equal pieces cancels in the XOR, so A depends only on the unpaired pieces.

**Statement.** Let q ≥ 2, b_1 ≥ … ≥ b_q > 1/D with all consecutive gaps > 1/D and S < (2^q − 1)/D.
If
    **S − max(b_1, 2b_2) < (2^{q−1} − 1)/D,**
then one pair-cancelling cut reduces the position to a valid IH(q−1) instance. Hence if IH(q−1)
holds, IH(q) holds for this position (A ≤ 1/D with ≤ q−1 cuts).

**Proof.** S − max(b_1, 2b_2) = min(S − b_1, S − 2b_2), so the hypothesis makes at least one branch
admissible.
- If S − b_1 < (2^{q−1} − 1)/D: **halve b_1**. The pair {b_1/2, b_1/2} XOR-cancels (Lemma X); the
  active multiset {b_2,…,b_q} has q−1 pieces, all > 1/D, sum S − b_1 < (2^{q−1} − 1)/D. This is a
  valid IH(q−1) instance.
- Else S − b_1 ≥ (2^{q−1} − 1)/D, forcing S − 2b_2 < (2^{q−1} − 1)/D: **cut b_1 at b_2**. The new
  length-b_2 piece cancels the intact b_2 (Lemma X); the active multiset {b_1 − b_2, b_3,…,b_q} has
  q−1 pieces, all > 1/D (b_1 − b_2 > 1/D by the hard-regime gap), sum S − 2b_2 < (2^{q−1} − 1)/D.
  This is a valid IH(q−1) instance.

By Lemma X, A of the whole config equals A of the active IH(q−1) instance; so IH(q−1) ⟹ A ≤ 1/D
with (q−2)+1 = q−1 cuts. ∎

**Note.** IH(q−1) as stated carries **no gap condition** — its proof (e.g. IH(3)'s exhaustive
gap-case split) covers all instances — so no gap-preservation is required on the reduced multiset.
The statement carries **no empirical percentage** (fixes the round-5 rejection reason): the condition
is the exact boundary between the reducible region and the flat residual.

**Certification.** Reviewer-verified round 6: identity S − max = min(S−b_1, S−2b_2) checked; both
reduced instances confirmed to have sum below the exact IH(q−1) boundary (2^{q−1}−1)/D and all pieces
> 1/D over 8·10^4 exact configs. Derived from certified Lemmas X. Admitted to the shared cache.
