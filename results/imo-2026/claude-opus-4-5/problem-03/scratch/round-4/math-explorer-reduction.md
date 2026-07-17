## imo-2026-03 — Reduction Despite Interleaving (Sandwich Case)

### Problem Setup Recap

P(m): For m+1 sorted pieces p_1 ≤ … ≤ p_{m+1} summing to S, XY with m marks achieves alternating sum A ≤ S·t_m (where t_m = 1/(2^{m+1}-1)).

Sandwich case (Case B, k* = m+1): p_k > 2^{k-1}·S·t_m for all k=1,…,m AND p_{m+1} ≤ 2^m·S·t_m = S·c(m).

---

### KEY INSIGHT #1: p_{m+1} < 2·p_m in the True Sandwich Case

From sandwich conditions:
- p_m > 2^{m-1}·S·t_m  (k=m does NOT satisfy threshold)
- p_{m+1} ≤ 2^m·S·t_m = 2·(2^{m-1}·S·t_m) < 2·p_m

So **p_{m+1} < 2·p_m** follows automatically. This is the essential prerequisite for XY's strategy.

---

### KEY INSIGHT #2: XY Splits p_{m+1} at p_m, Creating a Cancelling Pair

**XY's strategy (true sandwich case):**
1. Use 1 mark to split p_{m+1} into (p_m, p_{m+1} - p_m).  
   — Since p_{m+1} < 2·p_m, we have p_{m+1} - p_m < p_m. The two pieces of size p_m form a "pair."
2. Use remaining m-1 marks on sub-problem {p_1,…,p_{m-1}, p_{m+1}-p_m} per P(m-1).

**Sub-problem:**  m pieces, m-1 marks, sum S'' = S - 2·p_m.  P(m-1) applies directly. ✓

---

### KEY INSIGHT #3: Parity Preservation (Pair Contributes 0 to A)

After XY acts, the combined sorted pieces are:
- **Top**: p_m, p_m (the pair — from original p_m and the sub-piece of p_{m+1})
- **Below**: sub-problem pieces Q_1 ≥ Q_2 ≥ … ≥ Q_{2m-1}, all ≤ p_m

Inserting the pair at positions 1-2 shifts all sub-problem pieces by 2. Since shift-by-2 preserves parity (odd→odd, even→even):
- Pair contributes: p_m - p_m = 0 to A.
- A_combined = 0 + A_sub (sub-problem alternating sum with same parities). ✓

This holds regardless of whether Q_1 equals p_m (ties: Q_1 = p_m lands at position 3 which is still odd, consistent with its odd role in the sub-problem). 

Verified computationally: all sub-problem pieces ≤ p_m (since XY only splits, never merges), so the pair always sits at positions 1-2.

---

### KEY INSIGHT #4: The Algebraic Bound Closes

**Claim:** (S - 2·p_m)·t_{m-1} < S·t_m.

**Proof:**  
(S - 2·p_m)/S ≤ t_m/t_{m-1} iff p_m ≥ S·2^{m-1}·t_m.

Computing the threshold:
t_{m-1} - t_m = (2^m/(( 2^m-1)(2^{m+1}-1))), and (t_{m-1}-t_m)/(2·t_{m-1}) = 2^{m-1}·t_m.

So the needed condition is p_m ≥ 2^{m-1}·S·t_m — but the **sandwich condition gives p_m > 2^{m-1}·S·t_m strictly**. ✓

Therefore A = A_sub ≤ (S-2·p_m)·t_{m-1} < S·t_m. ✓

**Numerical verification (m=2):** Config p1=0.15, p2=0.29, p3=0.56, S=1, t_2=1/7.
- XY splits p3 into (p2=0.29, 0.27). Pair: (0.29, 0.29).
- Sub-problem: {0.15, 0.27}, S''=0.42.
- P(1) Case 2: p2>2p1? No. Split 0.27 at 0.15 → A_sub=0.27-0.15=0.12.
- A = 0.12 < 1/7 ≈ 0.1429. ✓

---

### Exploration of Specific Reduction Questions

**Q1: Apply P(m-1) to {p_1,…,p_m} using m-1 marks + 1 mark to halve p_{m+1}?**

This is NOT the strategy that works. Halving p_{m+1} creates pair (p_{m+1}/2, p_{m+1}/2). In sandwich case, p_{m+1}/2 ≤ 2^{m-1}·S·t_m < p_m. So the pair INTERLEAVES with the sub-problem (it's below p_m, not above). The parity preservation argument requires the pair to sit at the TOP (positions 1-2), but p_{m+1}/2 < p_m means the pair sits somewhere in the middle. The pair still contributes 0, but A_sub ≤ (S-p_{m+1})·t_{m-1} which needs p_{m+1} ≥ S·c(m) — the opposite of what sandwich gives. **Dead end.**

**Q2: How does halved p_{m+1}/2 interact with the sorted order?**

p_{m+1}/2 ≤ 2^{m-1}·S·t_m (from p_{m+1} ≤ 2^m·S·t_m) and p_m > 2^{m-1}·S·t_m. So p_{m+1}/2 < p_m, meaning halved pieces sit BELOW p_m. They interleave with the sub-problem pieces. The interleaving disrupts clean analysis. This is why halving is the WRONG strategy — **split at p_m, not at half.**

**Q3: Can we bound the contribution from interleaving?**

Not needed with the correct strategy (split at p_m). The pair (p_m, p_m) sits at the TOP and contributes exactly 0. No interleaving with the sub-problem occurs because all sub-problem pieces are ≤ p_m.

**Q4: Use all m marks on {p_1,…,p_m}, leaving p_{m+1} intact?**

Then p_{m+1} is the largest piece and LB takes it first. This gives A ≥ p_{m+1} - (XY's take from rest) which could be large. XY needs to be extremely effective on the remaining pieces to compensate. Numerically suboptimal and hard to analyze. **Not the right approach.**

---

### The Mixed Case B Issue (Important Caveat)

The true sandwich case is when ALL k=1,…,m fail the threshold (p_k > 2^{k-1}·S·t_m). There is a **mixed Case B** where k_star = m+1 (max satisfying index) but some k' < m+1 also satisfies the threshold.

In the mixed case: p_{k'} ≤ 2^{k'-1}·S·t_m for some k' < m+1. The true sandwich condition p_m > threshold_m fails (if k'=m). The pair strategy then runs into: p_{m+1} ≥ 2·p_m (since p_{m+1} ≤ 2^m·S·t_m and p_m ≤ 2^{m-1}·S·t_m, so the strict < fails).

**Numerical observation**: XY still achieves A ≤ S·t_m in the mixed case, but by a different strategy:

For m=2 mixed case (p_2 ≤ 2S/7 and p_3 ≤ 4S/7): XY achieves A = p_3 - p_1 - p_2 = 2p_3 - S by splitting p_3 into m+1=3 sub-pieces that "collect" all p_1 and p_2 at even positions (p1=0.15, p2=0.285, p3=0.565: A_XY-optimal = 0.130 ≤ 1/7 via this mechanism, confirmed numerically).

A = 2p_{m+1} - S ≤ S·t_m iff p_{m+1} ≤ S·c(m). ✓ (exactly the Case B condition!)

**Strategy for mixed case**: Use all m marks on p_{m+1} to split it into m+1 sub-pieces L_1 > p_m > L_2 > p_{m-1} > … > p_1 > L_{m+1}. This requires p_{m+1} to have enough "room" (specifically p_{m+1} > p_m for L_1 > p_m, which holds in sorted order when p_{m+1} > p_m strictly). But if p_{m+1} = p_m, the geometric configuration occurs and the copy strategy handles it.

**The mixed case requires separate proof effort** — the current induction-on-n approach doesn't cleanly handle it via the algebraic miracle of Case A.

---

### Summary for Proof Builder

**For the true sandwich case (closing the main gap):**

In Case B where k_star = m+1 and ALL p_k > 2^{k-1}·S·t_m for k=1,…,m:

1. **Note:** p_m > 2^{m-1}·S·t_m and p_{m+1} ≤ 2^m·S·t_m, so p_{m+1} < 2·p_m.
2. **XY's strategy:** Split p_{m+1} at position p_m (using 1 mark), creating pieces (p_m, p_{m+1}-p_m) with p_{m+1}-p_m < p_m.
3. **Parity preservation:** The pair (p_m, p_m) sits at positions 1-2 of combined sorted order (all sub-problem pieces ≤ p_m). Inserting the pair at positions 1-2 shifts subsequent items by 2, preserving parity. So A = 0 + A_sub.
4. **Apply P(m-1):** Sub-problem {p_1,…,p_{m-1}, p_{m+1}-p_m} has m pieces, sum S''=S-2p_m, uses m-1 remaining marks. By inductive hypothesis, A_sub ≤ S''·t_{m-1}.
5. **Bound:** (S-2p_m)·t_{m-1} < S·t_m iff p_m > 2^{m-1}·S·t_m. ✓ (sandwich condition).
6. **Conclusion:** A < S·t_m. ✓

**Remaining gap (mixed Case B):** When k_star=m+1 but p_m ≤ threshold_m, neither this strategy nor Case A's algebraic miracle applies cleanly. The proof builder should either:
(a) Argue this falls under a re-defined Case A (using k' = max satisfying k < m+1 when p_{k'} satisfies AND p_{k'+1} doesn't, giving ratio > 2 for no-interleaving; then use the sub-problem directly);
(b) Handle the mixed case via a separate argument showing XY can achieve A = 2p_{m+1}-S ≤ S·t_m using all m marks on p_{m+1}.

**Key computed bound:** Max A over all m=2 true-sandwich configs with this strategy: 0.140 < 1/7 ≈ 0.143. Verified. Max A over all m=3 configs with full recursive strategy: 0.0884 > 0.0667 (but this is due to incorrect handling of mixed Case B, not the true sandwich case — the true sandwich case itself gives A < S·t_m by the proof above).
