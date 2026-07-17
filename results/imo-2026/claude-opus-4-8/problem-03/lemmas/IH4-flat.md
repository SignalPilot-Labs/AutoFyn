# Lemma IH4-flat — the q=4 flat-residual leaf (certified round 6)

**Statement.** Let q = 4, b_1 ≥ b_2 ≥ b_3 ≥ b_4 > 1/D with all consecutive gaps > 1/D,
S = Σ b_i < 15/D, and **S − max(b_1, 2b_2) ≥ 7/D** (the complement of IH-reducible's hypothesis at
q=4). Then b_2 < 4/D, and XY forces A < 1/D with 3 cuts.

**Proof.** Since 2b_2 ≤ max(b_1,2b_2), S − 2b_2 ≥ 7/D, so 2b_2 ≤ S − 7/D < 8/D, i.e. **b_2 < 4/D.**
Gaps give b_3 < b_2 − 1/D < 3/D, b_4 < b_3 − 1/D < 2/D, b_3 > b_4 + 1/D > 2/D, and b_3 + b_4 > 3/D.

XY plays 3 cuts: (1) halve b_1 → pair {b_1/2, b_1/2} (XOR ∅, Lemma X); (2) cut b_2 into (b_3, b_2−b_3)
→ the new length-b_3 piece cancels the intact b_3 (XOR ∅), leaving singleton b_2 − b_3 (> 1/D);
(3) cut b_4 into (b_4 − δ, δ), δ small. By Lemma X, A = alternating sum of the three singletons
S₃ = {b_2 − b_3, b_4 − δ, δ}. Two exhaustive sub-cases on sign(b_3 + b_4 − b_2):

- **b_2 < b_3 + b_4:** then b_2 − b_3 < b_4; for 0 < δ < min(b_4/2, b_3+b_4−b_2) the sort is
  b_4 − δ > b_2 − b_3 > δ, so A = (b_4 − δ) − (b_2 − b_3) + δ = b_3 + b_4 − b_2. As b_2 > b_3 + 1/D
  and b_4 < 2/D, 0 < A < b_4 − 1/D < 1/D.
- **b_2 ≥ b_3 + b_4:** then b_2 − b_3 ≥ b_4 > b_4 − δ; the sort is b_2 − b_3 > b_4 − δ > δ, so
  A = (b_2 − b_3) − (b_4 − δ) + δ = (b_2 − b_3 − b_4) + 2δ. Since b_2 < 4/D and b_3 + b_4 > 3/D,
  0 ≤ b_2 − b_3 − b_4 < 1/D; choosing 0 < δ < min(b_4/2, (1/D − (b_2 − b_3 − b_4))/2) gives A < 1/D.

Both sub-cases give A < 1/D with 3 cuts. ∎

**Consequence (IH(4)).** Together with IH-reducible (reducible region ↦ IH(3), proved) these two
complementary conditions exhaust all q=4 hard-regime instances, so **IH(4) holds unconditionally**
(for hard-regime instances), closing the Case-B B1-large upper bound for n ≤ 4.

**Certification.** Reviewer-verified round 6: b_2 < 4/D derivation, both sign sub-cases, and the
δ-choice checked; full IH(4) closure (reducible ∪ flat) verified 0 failures / worst A·D ≤ 1 over
8·10^4 exact hard-regime configs at D = 15, 31, 63, 127. Derived from certified Lemmas X and H.
No empirical percentage in the statement. Admitted to the shared cache.
