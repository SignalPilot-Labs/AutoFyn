## imo-2026-03

### Summary

The explorers discovered key structural results that close most of the upper bound gap:

1. **Pigeonhole Lemma** (new): For any pieces p_1 <= ... <= p_{n+1} summing to 1, there exists k in {1,...,n+1} such that p_k <= 2^{k-1} * t_n (where t_n = 1/(2^{n+1}-1)).
2. **Pair-Cancellation / A = p_1 Lemma** (new): If XY halves p_2,...,p_{n+1}, the alternating sum A = p_1 exactly.
3. **n=1 complete proof** (new, clean): case-split on ratio a_2/a_1 (threshold 2).
4. **n=2 complete proof** (new): trichotomy on which of the 3 pigeonhole conditions holds.

The remaining gap is: for n >= 3 and k >= 3 (when p_k <= 2^{k-1}*t_n but p_1 > t_n and p_2 > 2t_n), what is XY's strategy?

---

geometric-dominance: revise
Target: c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
Technique: Direct case analysis via pigeonhole + pair-cancellation, building from n=1,2 complete proofs to general n.
Skeleton:
  1. Preliminaries: greedy optimality, alternating sum A formula (already proven).
  2. Lower bound: geometric marking guarantees LB >= c(n) (already proven).
  3. **Upper bound via pigeonhole**: For any LB marking p_1 <= ... <= p_{n+1}, at least one of these holds:
     - (A) p_1 <= t_n
     - (B) p_2 <= 2t_n (so p_2 - p_1 < t_n)
     - ...
     - (K) p_k <= 2^{k-1} * t_n for some k <= n
     - (N+1) p_{n+1} <= 2^n * t_n = c(n)
  4. Case k=1: XY halves p_2,...,p_{n+1}. By pair-cancellation, A = p_1 <= t_n. LB gets (1+A)/2 <= c(n). **COMPLETE.**
  5. Case k=2: p_2 - p_1 < t_n (since p_1 > t_n and p_2 <= 2t_n). XY halves p_3,...,p_{n+1} (n-1 marks). The two singletons p_1, p_2 contribute p_2 - p_1 < t_n to A. **COMPLETE.**
  6. Case k=n+1: p_{n+1} <= c(n). XY uses sandwich strategy to force LB to take p_{n+1} as their entire share. **COMPLETE (modulo verifying sandwich achievable).**
  7. **GAP: Cases k=3,...,n.** When p_k <= 2^{k-1} * t_n but p_1 > t_n and p_2 > 2t_n. Need XY strategy achieving A <= t_n.
Key lemmas (claim + mechanism):
  - Pigeonhole Lemma: some p_k <= 2^{k-1} * t_n -- because sum of strict bounds exceeds 1.
  - Pair-cancellation: A = p_1 when XY halves all but p_1 -- because equal pairs contribute 0 to alternating sum and p_1 lands at an odd position.
  - n=2 trichotomy gives complete proof for n=2 -- because k in {1,2,3} exhausts all cases and each has a strategy.
Open gaps: Cases k=3,...,n for general n (XY strategy needed).
Cases to cover: k=1, k=2, k=3,...,n, k=n+1 (the intermediate cases k=3,...,n are the gap).
Watch out for: The case k=2 relies on p_2 - p_1 < t_n; verify this follows from the pigeonhole failure of k=1.

---

ratio-based-induction: new
Target: c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
Technique: Strong induction with a strengthened hypothesis; XY's strategy based on ratio a_{n+1}/a_n (threshold 2), mirroring the clean n=1 proof.
Skeleton:
  1. **Base case n=1**: Two strategies based on ratio a_2/a_1:
     - If a_2/a_1 > 2: XY halves a_2. A = a_1 < 1/3.
     - If a_2/a_1 <= 2: XY clones a_1 inside a_2. A = 1 - 2a_1 <= 1/3.
     Both give A <= t_1. **COMPLETE.**
  2. **Inductive hypothesis**: For any m <= n pieces summing to S with smallest piece <= S * t_{m-1}, XY (with m-1 marks) achieves A <= S * t_{m-1}. (Scale-invariant.)
  3. **Inductive step for n+1 pieces**: Look at ratio a_{n+1}/a_n.
     - If a_{n+1}/a_n > 2: XY halves a_{n+1}, creating pair (a_{n+1}/2, a_{n+1}/2). Pair contributes 0 to A. Remaining problem: n pieces p_1,...,p_n (where p_i = a_i for i < n, p_n includes the pair contributions) with n-1 XY marks. Apply induction.
     - If a_{n+1}/a_n <= 2: XY clones a_n inside a_{n+1} (mark at distance a_n from one end). Creates pair (a_n, a_{n+1}-a_n). Pair cancels in A. Remaining problem structured for induction.
  4. Conclude A <= t_n for the full configuration.
Key lemmas (claim + mechanism):
  - Ratio threshold 2 is exactly geometric -- because geometric marking has a_{k+1}/a_k = 2 for all k.
  - Each XY move (halve or clone) creates a canceling pair -- because pairs at adjacent positions contribute 0 to A.
  - Scale-invariant induction -- because A/S is dimensionless and the bound t_n depends only on n.
Open gaps: The inductive step needs careful bookkeeping of how the pair affects the residual sorted order. Need to verify A_residual * scaling <= t_{n-1} * scaling implies A_total <= t_n.
Cases to cover: Ratio > 2 vs ratio <= 2 at each step (binary tree of depth n).
Watch out for: The residual problem after one XY mark may not have exactly n pieces; the pair might interleave with existing pieces in a way that changes the sorted positions. Must handle this.

---

exchange-argument: new
Target: c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
Technique: Variational/exchange argument showing geometric marking is uniquely LB-optimal (different framing from constructive XY strategies).
Skeleton:
  1. Define V(L) = min_X G(L,X) as LB's guaranteed value under marking L.
  2. Lower bound: V(geometric) = c(n) (already proven).
  3. **Claim: If L is not geometric, then V(L) < c(n).**
  4. Proof: Consider any marking L = (p_1,...,p_{n+1}) with some ratio p_{k+1}/p_k != 2.
     - If p_{k+1}/p_k > 2: XY halves p_{k+1}. The piece p_{k+1}/2 < p_k creates a new interleaving that benefits XY.
     - If p_{k+1}/p_k < 2: The pieces are "too close"; XY can exploit by cloning or by the pigeonhole slack.
  5. This establishes V(L) < c(n) for all L != geometric.
  6. Therefore max_L V(L) = V(geometric) = c(n), so LB cannot guarantee more than c(n).
Key lemmas (claim + mechanism):
  - Geometric is a critical point -- because any perturbation strictly decreases V(L) (a local maximum argument).
  - Ratios away from 2 give XY a strict advantage -- because the pair-cancellation is incomplete or the sorted order shifts.
Open gaps: The variational argument needs to be made rigorous. Must show V is continuous and that non-geometric L have V(L) < c(n).
Cases to cover: Ratio > 2 vs ratio < 2 at each position k.
Watch out for: This approach avoids constructing explicit XY strategies but must still establish V(L) <= c(n) for ALL L, not just argue geometric is a local max.

---

induction-on-n: advance
Target: c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
Technique: Strong induction with saddle-point verification.
Skeleton:
  (existing file with lower bound proven)
  - The upper bound section needs the pigeonhole case analysis incorporated.
  - Specifically: incorporate the new n=1 clean proof (ratio-based case split) and the n=2 trichotomy as base cases, then extend.
Key lemmas: Same as geometric-dominance.
Open gaps: Same k=3,...,n gap.
Cases to cover: Same.
Watch out for: The file's current "saddle point" claim is incomplete; the builder must NOT claim the saddle point proves the upper bound without a constructive XY strategy for ALL LB markings.

Note: induction-on-n and geometric-dominance share the same gap and the same structural approach. Recommend advancing geometric-dominance (cleaner structure after revision) and marking induction-on-n as redundant/lower priority.

---

### Field summary

| Slug | Action | Reason |
|------|--------|--------|
| geometric-dominance | revise | Incorporate explorer's pigeonhole + pair-cancellation results. Gap: k=3,...,n cases. |
| ratio-based-induction | new | Different attack: n=1 clean proof as template, ratio-based recursion. May close the gap. |
| exchange-argument | new | Alternative framing: show geometric uniquely optimal via variational argument. |
| induction-on-n | advance (low priority) | Same approach as geometric-dominance; either one closing the gap suffices. |
| pairing-interleave | stale | Superseded by the cleaner pigeonhole/pair-cancellation structure. |

### Build set recommendation

1. **geometric-dominance** (revise): Primary; has the most complete structure.
2. **ratio-based-induction** (new): Promising alternative that may close k=3,...,n gap differently.

The exchange-argument is theoretically clean but may be harder to make rigorous; hold for later if the other two stall.
