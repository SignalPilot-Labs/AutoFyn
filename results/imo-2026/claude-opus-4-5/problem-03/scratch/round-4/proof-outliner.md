## imo-2026-03

induction-on-n: revise
Target: c(n) = 2^n / (2^{n+1} - 1) is the exact value LB can guarantee (both bounds)
Technique: Scale-invariant strong induction P(m), with k*-largest pigeonhole + "create-duplicate" strategy for sandwich case
Skeleton:
  1. Greedy Optimality Lemma — by backward induction (already proved)
  2. Lower bound: LB's geometric marking guarantees c(n) — by copy strategy saddle-point analysis (already proved)
  3. Upper bound base P(1) — by explicit 2-case strategy (already proved)
  4. Upper bound inductive step P(m), Case A (k* < m+1): halve+recurse — by ratio > 2 separation + IH P(k*-1) (already proved)
  5. **Upper bound inductive step P(m), Case B (k* = m+1, true sandwich):** — XY splits p_{m+1} at p_m, creating duplicate pair
     5a. Show p_{m+1} < 2p_m — from p_m > 2^{m-1}·S·t_m and p_{m+1} ≤ 2^m·S·t_m
     5b. XY uses 1 mark: cut p_{m+1} → (p_m, p_{m+1}-p_m) — direct construction
     5c. Two copies of p_m at positions 1-2 (all sub-pieces < p_m) — since p_{m+1}-p_m < p_m and p_k < p_m for k < m
     5d. Pair cancellation: contribution 0 to alternating sum — LB takes pos 1, XY takes pos 2
     5e. Apply P(m-1) to {p_1,...,p_{m-1}, p_{m+1}-p_m} with m-1 marks — IH
     5f. Bound: (S-2p_m)·t_{m-1} < S·t_m — because p_m > 2^{m-1}·S·t_m (sandwich condition)
  6. Conclude P(m) holds for all m, hence c(n) = 2^n/(2^{n+1}-1) — by strong induction

Key lemmas (claim + one-line mechanism):
  - p_{m+1} < 2p_m in sandwich case — because p_m > 2^{m-1}·S·t_m and p_{m+1} ≤ 2^m·S·t_m = 2·(2^{m-1}·S·t_m) < 2p_m
  - Sub-problem pieces are all < p_m — because p_k < p_m for k < m (sorted order) and p_{m+1}-p_m < p_m (just shown)
  - Pair sits at positions 1-2 — because both copies equal p_m, which exceeds all sub-problem pieces
  - Alternating sum bound: (S-2p_m)·t_{m-1} < S·t_m — rearranges to p_m > 2^{m-1}·S·t_m, exactly the sandwich condition for k=m

Open gaps: NONE — the sandwich case fix completes the proof
Cases to cover: Case A (k* < m+1) + Case B (k* = m+1) — both now have strategies
Watch out for:
  - Verify p_{m+1} > p_m (so we can cut at p_m) — this is automatic from sorted order
  - Ties in sorted order: if sub-problem piece equals p_m, it still sits below the duplicate pair (positions 3+) since the pair occupies 1-2; parity still works

---

geometric-dominance: archive (superseded)
Reason: Same answer, same lower bound, weaker upper bound framework. The induction-on-n approach with the sandwich fix provides a complete unified proof. No independent progress path.

pairing-interleave: archive (superseded)
Reason: Exploratory approach focused on XY's copy strategy structure. The key insights are now absorbed into induction-on-n (pair cancellation, dyadic thresholds). No remaining gap it could close that induction-on-n doesn't.

ratio-based-induction: archive (superseded)
Reason: Ratio > 2 halving is now a sub-case of induction-on-n (Case A). The ratio ≤ 2 cloning idea is subsumed by the sandwich case's "create duplicate" strategy. Redundant.

---

**Build set:** induction-on-n

The induction-on-n approach is ready for the builder to fill in Case B with the sandwich case proof. All key lemmas and their mechanisms are identified. This should close the gap completely and yield a solved proof.
