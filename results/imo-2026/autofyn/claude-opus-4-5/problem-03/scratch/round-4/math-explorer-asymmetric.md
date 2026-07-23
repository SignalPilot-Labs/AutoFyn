## imo-2026-03 — Sandwich Case Asymmetric Splits

- **Distinct openings found:**
  - **CLEAN PROOF OF SANDWICH CASE** (the gap is now CLOSED — see below)
  - The strategy is: cut p_{m+1} to create a DUPLICATE of p_m; the two copies cancel at the top; apply P(m-1) recursively to the residue.
  - Alternative lens: the "proportional clone" strategy (XY splits p_{m+1} proportionally to p_1,...,p_m) gives intuition but is messier to prove; the "create duplicate" strategy is cleaner.

- **The PROOF of the Sandwich Case:**

**Strategy:** In the sandwich case P(m) with m+1 pieces p_1 ≤ ... ≤ p_{m+1} summing to S (where p_k > 2^{k-1}·S·t_m for k=1,...,m and p_{m+1} ≤ 2^m·S·t_m = S·c(m)):

XY uses m marks as follows:
1. **Mark 1:** Cut p_{m+1} into (p_m, p_{m+1} - p_m). This creates **two copies of p_m** in the piece set.
2. **Marks 2 through m:** Apply P(m-1) to the sub-problem {p_1, ..., p_{m-1}, p_{m+1} - p_m} (which has m pieces, using m-1 marks by the inductive hypothesis).

**Why the two copies of p_m cancel:**
- In the sandwich case, p_{m+1} ≤ 2^m·S·t_m and p_m > 2^{m-1}·S·t_m (strict). Therefore 2p_m > 2·2^{m-1}·S·t_m = 2^m·S·t_m ≥ p_{m+1}, i.e., **p_{m+1} < 2p_m**, hence p_{m+1} - p_m < p_m. ✓
- All sub-problem pieces {p_1,...,p_{m-1}, p_{m+1}-p_m} are < p_m (since p_k < p_m for k < m by sorted order, and p_{m+1}-p_m < p_m as just shown).
- Any further cuts by P(m-1) only make pieces smaller. So the two copies of p_m remain the LARGEST pieces throughout, sitting at positions 1 and 2 in the global sorted order.
- LB takes position 1 (one copy of p_m), XY takes position 2 (the other copy). **Contribution to A: 0** (pair cancellation). ✓

**Bound on sub-problem A:**
- Sub-problem sum: S_sub = p_1 + ... + p_{m-1} + (p_{m+1} - p_m) = S - 2p_m.
- By IH (P(m-1) proved for m-1 < m): A_sub ≤ S_sub · t_{m-1} = (S - 2p_m) · t_{m-1}.
- Need: (S - 2p_m) · t_{m-1} ≤ S · t_m.
- Equivalent to: p_m ≥ S · 2^{m-1}/(2^{m+1}-1) = 2^{m-1} · S · t_m.
- **This is EXACTLY the sandwich condition for k = m (strict >, so bound is strict <).** ✓

**Conclusion:** A_total = 0 + A_sub ≤ (S - 2p_m) · t_{m-1} < S · t_m. ✓

**Concrete verification for m=2:**
- Pieces p1=0.145, p2=0.287, p3=0.568 (near-worst case). Sandwich? ✓
- Step 1: Cut p3=0.568 → (p2=0.287, p3-p2=0.281). Two copies of 0.287 at top, cancel.
- Step 2: Apply P(1) to {0.145, 0.281}, sum=0.426.
- Bound: (1 - 2×0.287)/7 = 0.426/7 = 0.1420 < 1/7 = 0.1429. ✓

**Concrete verification for m=3 (the previously failing case):**
- Pieces p=0.070, 0.140, 0.290, 0.500.
- Step 1: Cut p4=0.500 → (p3=0.290, 0.210). Two copies of 0.290 at top, cancel.
- Step 2: Apply P(2) to {0.070, 0.140, 0.210}, sum=0.420.
- Bound: (1 - 2×0.290)/7 = 0.420/7 = 0.0600 < 1/15 = 0.0667. ✓

- **Candidate technique:** Recursive pairing / "create duplicate" strategy. One mark creates a pair at the top that cancels; induction handles the residue.

- **Cheap-kill candidates:** The key algebraic identity: (S-2p_m)·t_{m-1} < S·t_m iff p_m > 2^{m-1}·S·t_m, which is the sandwich condition for k=m. This is a near-tautology given the case setup.

- **Knowledge-base entries to use:** The inductive hypothesis P(m-1) (scale-invariant claim), Greedy Optimality Lemma (already proved in the approach file), Pigeonhole Existence Lemma and Sub-Problem Size Bound (already in the approach file).

- **Analogous past problems (cruxes):** None specifically analogous — the "create a duplicate to cancel" trick is specific to this game structure.

- **Prior progress:** Upper bound Case A (k* < m+1) fully proved. **Case B (sandwich, k* = m+1) NOW PROVED** by the above strategy. The answer c(n) = 2^n/(2^{n+1}-1) is now fully established.

- **Dead ends (do not retry):**
  - Simple "halve p3" strategy fails in sub-case p3 < 3S/7 for m=2.
  - "Apply P(m-1) to top m pieces and halve p_{m+1}" fails since it requires p_{m+1} ≥ S·c(m).
  - "Proportional clone" (split p_{m+1} proportionally to all others) requires careful interleaving analysis and doesn't cleanly give a recursive proof.
  - Lemma 5 "p_1 ≤ t_n OR p_{n+1} ≤ c(n)" is FALSE (counterexample found in R2).

- **Small-case / intuition notes:**
  - The "create duplicate" strategy uses ONLY 1 mark for the pairing, leaving m-1 marks for the sub-problem. This is exactly the budget required.
  - The tight case occurs near the sandwich boundaries: p_k ≈ 2^{k-1}·S·t_m, in which case (S-2p_m)·t_{m-1} approaches S·t_m from below.
  - At the EXACT geometric piece set (p_k = 2^{k-1}·S·t_m), the strategy gives A_total = S·t_m exactly (tight), confirming optimality.
  - The strategy naturally terminates: when the sub-problem pieces all equal each other, P(m-1) uses 0 marks and A = 0.

**SUMMARY FOR PROOF-BUILDER:**
The sandwich case proof is now complete. The builder should add to the `induction-on-n` approach file, under Case B:

> XY uses 1 mark to cut p_{m+1} → (p_m, p_{m+1}-p_m), creating two copies of p_m. Since p_{m+1} < 2p_m (which follows from p_m > 2^{m-1}·S·t_m and p_{m+1} ≤ 2^m·S·t_m), the piece p_{m+1}-p_m < p_m. Thus all sub-problem pieces are < p_m, the two p_m copies occupy positions 1 and 2 in the global sorted order, and they cancel (contribute 0 to A). XY then applies P(m-1) to {p_1,...,p_{m-1},p_{m+1}-p_m} with the remaining m-1 marks. The sub-problem sum is S-2p_m, so A_sub ≤ (S-2p_m)·t_{m-1}. The sandwich condition p_m > 2^{m-1}·S·t_m gives (S-2p_m)·t_{m-1} < S·t_m. Therefore A_total < S·t_m. □
