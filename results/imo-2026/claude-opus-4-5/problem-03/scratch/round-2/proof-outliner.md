## imo-2026-03

### Overview and Critical Correction

**Round 2 explorers discovered that Round 1 was WRONG about "arithmetic beats geometric".**

The error: Round 1 computed XY's response to arithmetic [1/6, 1/3, 1/2] as equal-split (1/2 -> [1/4, 1/4]), giving LB = 7/12. But XY's OPTIMAL response is asymmetric: 1/2 -> [1/3, 1/6], creating pieces [1/3, 1/3, 1/6, 1/6], giving LB only 1/2.

For geometric [1/7, 2/7, 4/7], ANY split of 4/7 gives LB exactly 4/7 (proved by the explorers via case analysis).

**The correct answer is c(n) = 2^n / (2^{n+1} - 1).** This was the "claimed answer" all along; Round 1 incorrectly disputed it.

---

geometric-direct-revised: revise
Target: c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Geometric construction for lower bound + explicit XY strategy for upper bound + induction on n
Skeleton:
  1. **Setup:** Define D = 2^{n+1} - 1, c(n) = 2^n/D. LB's geometric config is L_k = 2^k/D for k = 0, 1, ..., n.
  2. **Greedy Optimality Lemma (import):** Both players play greedy; LB gets odd-indexed pieces in sorted order. — *Certified in lemmas/greedy-optimality.md*
  3. **Geometric Dominance Lemma:** L_n = 2^n/D > sum of L_0 + ... + L_{n-1} = (2^n - 1)/D. — *By geometric series sum*
  4. **Part A (Lower Bound): LB guarantees >= c(n) with geometric config.**
     - Case A.1: XY places 0 marks inside L_n. L_n is largest piece; LB picks it first; LB >= c(n).
     - Case A.2: XY places j >= 1 marks inside L_n.
       - Subcase: XY places ALL n marks inside L_n. Total pieces = 2n+1 (odd). LB picks ceil((2n+1)/2) = n+1 pieces. Extra pick helps LB; verify LB >= c(n).
       - Subcase: XY places j < n marks inside L_n (key: j = n-1 optimal for XY).
       - **Key Invariant Lemma:** For any cut of L_n into sub-pieces {a_1, ..., a_{j+1}} summing to L_n, greedy picking from {L_0, ..., L_{n-1}} union {a_1, ..., a_{j+1}} gives LB >= L_n = c(n).
  5. **Part B (Upper Bound): XY limits any LB to <= c(n).**
     - Base case n=1: explicit XY strategies limit LB to 2/3.
     - Inductive step: For LB's pieces P_1 >= ... >= P_{n+1} summing to 1, XY uses n-1 marks inside P_1 to create "paired" sub-pieces. 
     - **Interleaving Claim:** XY creates sub-pieces Q_k slightly exceeding L_{n-k}, sorted order becomes [Q_1, P_2, Q_2, P_3, ..., Q_n, P_{n+1}]. LB picks all Q_k, totaling P_1.
     - Key constraint: P_1 <= c(n) when LB plays optimally (otherwise XY exploits the imbalance).
  6. **Saddle-point equality:** At geometric config, XY's two principal strategies (split vs. avoid largest) give equal values c(n); any LB deviation allows XY to do strictly better.
  7. **Conclusion:** c(n) = 2^n/(2^{n+1}-1).
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Greedy Optimality:** Both players picking largest is optimal — exchange argument shows deviating loses >= the gain from taking the larger piece first. (Certified)
  - **Geometric Dominance:** L_n > L_0 + ... + L_{n-1} — because 2^n > 2^n - 1 (geometric series).
  - **Key Invariant:** Any partition of L_n into sub-pieces gives LB >= L_n — because the doubling L_k = 2*L_{k-1} ensures sub-pieces "straddle" L_{n-1} in sorted order; LB picks one from each straddled level totaling L_n.
  - **Parity Lemma:** XY uses <= n-1 marks to avoid giving LB an extra pick (n marks create 2n+1 pieces, odd, LB picks n+1).
  - **Interleaving for Upper Bound:** XY can create sub-pieces Q_k = P_{k+1} + epsilon inside P_1 — because sum of sub-pieces = P_1 and there is slack (2P_1 - 1 > 0 when P_1 > 1/2).
Open gaps:
  - The Key Invariant needs rigorous proof for general j (the case j = n-1 was outlined; arbitrary j needs analysis).
  - The upper bound interleaving argument needs the P_1 <= c(n) claim proved (show XY can exploit P_1 > c(n)).
  - Edge case: What if P_1 <= 1/2? Then all pieces <= c(n) and XY's task is simpler.
Cases to cover:
  - Lower bound: j = 0, 1, ..., n marks inside L_n.
  - Upper bound: m = 0, 1, ..., n marks by LB; P_1 > 1/2 vs P_1 <= 1/2.
Watch out for:
  - The Key Invariant is the crux. The doubling property (L_k = 2*L_{k-1}) is essential; without it (e.g., arithmetic), XY can clone pieces and reduce LB below c(n).
  - Parity: n marks by XY gives odd piece count; XY should use n-1.
  - The upper bound interleaving fails if P_2 >= Q_1; need to handle this case.

---

minimax-saddle-point: new
Target: c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Game-theoretic saddle-point characterization; the geometric config is where XY's two key strategies give equal values
Skeleton:
  1. **Setup:** The game is a sequential Stackelberg game: LB commits to a configuration, then XY responds optimally, then both pick greedily.
  2. **Value function:** For LB config (a_1, ..., a_{n+1}) summing to 1 (sorted ascending), define V(a) = min over XY strategies of LB's greedy payoff.
  3. **XY's two principal strategies (for n=2 in detail):**
     - Strategy A: XY splits largest piece a_{n+1} with 1 mark at midpoint.
     - Strategy B: XY splits two largest pieces a_{n+1} and a_n, each with 1 mark.
     - XY picks whichever gives smaller LB payoff.
  4. **Saddle-point condition:** The geometric config (1, 2, ..., 2^n)/D satisfies Strategy A value = Strategy B value = c(n). This is the minimax: LB maximizes V; XY minimizes it; both optimize to c(n) at geometric.
  5. **Uniqueness of saddle:** Any deviation by LB from geometric ratio allows at least one XY strategy to reduce LB below c(n).
  6. **Lower bound from saddle:** LB's geometric config achieves V = c(n).
  7. **Upper bound from saddle:** For any LB config, XY picks the better strategy; the minimum over XY strategies is <= c(n) at any non-geometric config.
  8. **Conclusion:** Game value = c(n) = 2^n/(2^{n+1}-1).
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Greedy Optimality:** (import from certified lemma)
  - **Saddle at geometric:** Strategy A and Strategy B give equal values at (1,2,4)/D for n=2 — because 2b = c at geometric (the doubling), so both strategies give c/2 + b = c.
  - **Non-geometric is suboptimal:** If the doubling fails (c < 2b or c > 2b), one strategy does strictly better than the other, and the worse strategy for XY still beats c(n).
Open gaps:
  - The two-strategy sufficiency: prove that XY's optimal is always one of these two (or a finite enumerable set).
  - The saddle equality condition: derive it for general n (not just n=2).
  - Uniqueness of the saddle-point configuration.
Cases to cover: none (the saddle-point is a single configuration)
Watch out for:
  - The "two strategies" simplification may not hold for all n; XY may have more varied responses.
  - The saddle-point argument is elegant but may be harder to make rigorous than the direct proof.

---

induction-on-n-revised: revise
Target: c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Strong induction on n with explicit XY strategy; FIXES the fatal error from Round 1
Skeleton:
  1. **Base case n=1:** c(1) = 2/3. LB's optimal is [1/3, 2/3]; XY's best responses give LB exactly 2/3. Upper bound: XY limits any LB to <= 2/3.
  2. **Inductive hypothesis:** c(k) = 2^k/(2^{k+1}-1) for all k < n.
  3. **Lower bound (LB >= c(n)):** LB uses geometric config; case analysis on XY's marks in L_n. Import the Key Invariant Lemma.
  4. **Upper bound (XY <= c(n)) — REVISED:** For LB's pieces P_1 >= ... >= P_{n+1}, XY uses n-1 marks inside P_1. The CRITICAL FIX: XY creates sub-pieces Q_k such that after sorting, LB picks exactly the sub-pieces of P_1, totaling P_1.
  5. **Why P_1 <= c(n):** If P_1 > c(n), then P_2 + ... + P_{n+1} < 1 - c(n) = (2^n - 1)/D. XY's interleaving exploits this slack to ensure LB gets exactly P_1 < c(n)... wait, this is backward. Need: P_1 <= c(n) OR XY can do even better.
  6. **Correct upper bound mechanism:** XY's strategy ensures LB's payoff = P_1 (via interleaving). Since LB is maximizing, LB chooses the config maximizing P_1 subject to P_1 <= c(n) (because geometric is the max). For P_1 > c(n), the pieces are "top-heavy" and XY can split P_1 to make it smaller.
  7. **Recurrence verification:** 1/c(n) = 2 - 2^{-n}; c(n) is decreasing in n.
  8. **Conclusion:** c(n) = 2^n/(2^{n+1}-1).
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Greedy Optimality:** (import)
  - **Geometric Dominance:** (import)
  - **Recurrence:** 1/c(n) = 1/c(n-1) + 2^{-n} — by direct computation.
  - **Upper bound interleaving:** XY's n-1 marks in P_1 create sub-pieces that pair with P_2, ..., P_{n+1}, so LB picks exactly the sub-pieces summing to P_1.
Open gaps:
  - The upper bound still has the same gap as Round 1: proving LB's payoff = P_1 for any LB config.
  - The "P_1 <= c(n) or XY exploits" claim needs proof.
Cases to cover:
  - Base n=1: 4 cases (XY marks 0 or 1, LB marks 0 or 1).
  - Inductive step: LB marks m = 0, 1, ..., n.
Watch out for:
  - This is essentially the same approach as Round 1 with the SAME gaps. The upper bound interleaving argument is still the hard part.
  - Round 1's proof was marked "solved" but had fatal errors; this revision must actually fill the gaps.

---

piece-count-parity: advance
Target: c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Parity analysis of total piece count determines pick advantage; XY optimizes by targeting even total
Skeleton: (already outlined; advance to build)
  1. LB creates n+1 pieces; XY creates up to n additional cuts.
  2. Total pieces = n+1+j where j = XY's marks.
  3. If n+1+j even: both pick (n+1+j)/2 pieces.
  4. If n+1+j odd: LB picks ceil, XY picks floor; LB has advantage.
  5. XY's optimal: choose j = n-1 so total = 2n (even); both pick n.
  6. This parity constraint bounds XY's strategy space.
  7. With parity fixed, compute LB's payoff via sorted order analysis.
Key lemmas: parity determines pick counts; XY avoids odd totals.
Open gaps: the main proof (lower and upper bounds) still needed; this is a structural observation, not a full proof.
Cases to cover: none (parity is a global constraint)
Watch out for: parity alone doesn't determine the answer; it constrains but doesn't solve.

---

### Recommended build set

1. **geometric-direct-revised** (revise) — The most promising. Corrects the Round 1 error, targets the correct answer, has the clearest structure. Key gap is the Key Invariant.

2. **minimax-saddle-point** (new) — A fresh perspective. The saddle-point structure was identified by the explorers and may give a cleaner proof. Worth pursuing in parallel.

3. **induction-on-n-revised** (revise) — Same structure as Round 1 but with the correct target. The upper bound gap persists; this may inform the other approaches.

**Do NOT build piece-count-parity alone** — it's a structural observation that feeds into the other approaches, not a standalone proof.

### Summary

| Slug | Action | Target | Main gap |
|------|--------|--------|----------|
| geometric-direct-revised | revise | c(n) = 2^n/(2^{n+1}-1) | Key Invariant for lower bound; interleaving for upper bound |
| minimax-saddle-point | new | c(n) = 2^n/(2^{n+1}-1) | Two-strategy sufficiency; saddle equality for general n |
| induction-on-n-revised | revise | c(n) = 2^n/(2^{n+1}-1) | Upper bound interleaving (same as Round 1) |
| piece-count-parity | advance | c(n) = 2^n/(2^{n+1}-1) | Feeds into other proofs; not standalone |

**Note on induction-on-n:** The Round 1 approach file claims status "solved" but the proof-reviewer found fatal errors. This must be revised, not advanced.
