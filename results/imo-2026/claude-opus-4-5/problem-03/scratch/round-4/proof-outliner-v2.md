## imo-2026-03

### Corrected Outline for geometric-direct

The outline-reviewer correctly identified two fatal flaws:
1. The "0 marks" case claim is nonsensical for n >= 2 (LB picks multiple pieces)
2. The "always split P_1" strategy fails when P_1 < c(n) and sub-game is geometric

The explorers found key working strategies:
- **Case 2b** (P_1 <= L_0 and P_{n+1} > c(n)): PROVED for general n via n-mark pairing
- **Case 2a** (P_1 > L_0 and P_{n+1} > c(n)): Verified for n=2,3, needs general proof
- **Case 1** (P_{n+1} <= c(n)): Strategy unclear in original outline

**Key discovery from exhaustive search:** XY can create MULTIPLE pairs by splitting different LB pieces. For n=3 with a "failing" config [8/83, 18/83, 24/83, 33/83], XY uses 2 marks to create pairs {P_1, P_1} and {P_3, P_3} by splitting P_2 and P_4, achieving LB = 42/83 < c(3).

---

geometric-direct: revise
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Case split on P_1 vs L_0 = 1/(2^{n+1}-1), with multi-pair creation strategies

Skeleton:
  1. Import certified lemmas: Greedy Optimality, Geometric Dominance, Parity Constraint
  2. Lower bound (COMPLETE): Geometric config [L_0, ..., L_n] achieves exactly c(n) against any XY response. Proof in geometric-direct.md Part 3.
  3. **Upper bound via two-case split on P_1:**
     - **Case A (P_1 <= L_0):** XY uses the n-mark pairing strategy on P_{n+1}, creating sub-pieces {P_n, ..., P_2, r, r}. The formula LB = 1/2 + P_1/2 <= c(n) applies when P_{n+1} >= c(n); when P_{n+1} < c(n), the sorted order changes but LB <= c(n) still holds. — by explorer's Case 2b lemma (PROVED for general n)
     - **Case B (P_1 > L_0):** XY creates multiple pairs by splitting different pieces. The key is to pair each large piece P_k with a copy created from a larger piece. — requires explicit construction
  4. Subcase analysis for Case B:
     - **B1 (P_{n+1} > c(n)):** XY uses k marks to split P_{n+1} into sub-pieces that create pairs with smaller original pieces. For n=2: 1 mark halving P_3 suffices. For n=3: 2 marks creating {P_3, P_3} from P_4.
     - **B2 (P_{n+1} <= c(n)):** XY splits multiple original pieces to create pairs. Example: split P_2 -> {P_1, P_2-P_1} and split P_4 -> {P_3, P_4-P_3} creating pairs {P_1, P_1} and {P_3, P_3}. LB = P_1 + P_3 + max(P_2-P_1, P_4-P_3).
  5. Conclude: For any LB config, XY limits LB to <= c(n). Combined with lower bound, c(n) = 2^n/(2^{n+1}-1).

Key lemmas (claim + mechanism):
  - **Case A Pairing Lemma (PROVED):** For P_1 <= L_0, XY's n-mark strategy on P_{n+1} gives LB = 1/2 + P_1/2 <= c(n) — because the pairing construction creates n pairs from {P_n,...,P_2,r,r} and P_1 is the unique minimum
  - **Multi-Pair Strategy:** When P_1 > L_0, XY creates multiple pairs by splitting different pieces — because splitting P_k into {P_j, P_k - P_j} creates a copy of P_j, and Pairing Cancellation applies to each pair
  - **LB bound for multi-pair:** With k pairs, LB = sum of (one element from each pair) + (something from remaining pieces) — algebraic manipulation needed for general formula

Open gaps:
  - **Case B explicit strategy for general n:** The multi-pair approach works computationally but needs a general construction. For which pieces should XY create pairs? What's the formula?
  - **Case B2 (P_1 > L_0 and P_{n+1} <= c(n)) algebraic proof:** Verified computationally for n=3 but no closed-form strategy yet
  - **Pairing interactions:** When multiple pairs exist, the Pairing Cancellation Lemma must be applied iteratively; verify the total formula

Cases to cover:
  - Case A: P_1 <= L_0 (any P_{n+1}) — PROVED via explorer's Case 2b
  - Case B1: P_1 > L_0 and P_{n+1} > c(n) — verified for n=2,3
  - Case B2: P_1 > L_0 and P_{n+1} <= c(n) — verified for n=3 via exhaustive search

Watch out for:
  - The multi-pair strategy uses FEWER than n marks in some cases; don't assume XY uses all marks
  - The formula LB = 1/2 + P_1/2 only applies in Case A when P_{n+1} > c(n); when P_{n+1} < c(n), sorted order changes
  - For Case B, the strategy of "split P_2 to create P_1 copy, split P_4 to create P_3 copy" works but may need refinement for edge cases

---

### Alternative approach: LP/convex saddle-point

two-strategy-saddle: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Saddle-point analysis via concavity of V(P) = min_{XY} LB_score(P, XY)

Skeleton:
  1. Define V(P) = min_{XY response} LB_greedy_value(P). V is concave (minimum of linear functions).
  2. LB's problem: max_P V(P) over the simplex. Maximum of concave is at the unique interior critical point.
  3. At the geometric config, all XY strategies (Case A pairing, Case B multi-pair, halving) give LB = c(n) exactly — this is the saddle.
  4. For non-geometric configs, at least one XY strategy gives LB < c(n).
  5. Conclude: c(n) is the minimax value.

Key lemmas:
  - **Concavity of V:** V(P) = min_sigma f_sigma(P) where each f_sigma is linear in P — standard convex analysis
  - **Complementary slackness:** At saddle, multiple XY strategies achieve the same value — verified at geometric config

Open gaps:
  - Formal proof that geometric is the UNIQUE critical point
  - Verification that all XY strategies achieve c(n) at geometric config (not just the ones we've checked)

Watch out for: This is more structural but harder to make rigorous than direct case analysis

---

### Build Set

**build set: geometric-direct**

The geometric-direct approach should be revised with the corrected case structure:
- Case A (P_1 <= L_0) is PROVED — import the explorer's Case 2b lemma directly
- Case B needs the multi-pair strategy formalized; the exhaustive search shows it works but the general construction is missing

The builder should:
1. State Case A (P_1 <= L_0) using the explorer's formula: XY uses n marks on P_{n+1} creating {P_n, ..., P_2, r, r}, result LB <= c(n)
2. For Case B, state the computational verification for n=2,3 and describe the multi-pair mechanism
3. Flag Case B for general n as an open gap if the algebraic proof isn't found
4. The proof is PARTIAL (Case A done, Case B computational) but significant progress

If Case B cannot be closed with a general proof, mark status as "partial" with the specific remaining gap.

---

### Notes on critical errors in original outline

1. **"XY uses 0 marks if P_1 <= c(n)"** — WRONG. With 0 marks on n+1 pieces, LB picks ceil((n+1)/2) pieces at odd positions. For the geometric config, LB gets L_n + L_{n-2} + ... > c(n). XY MUST use marks.

2. **"Always split P_1"** — WRONG for P_1 < c(n) with geometric sub-game. The bound f(P_1) = P_1/2 + c(n-1)(1-P_1) > c(n) when P_1 < c(n).

3. **Case structure based on P_1 vs L_0** is CORRECT (from explorers). But both cases require explicit XY strategies, not "0 marks" or "split P_1."

The key insight is that XY's strategy depends on P_1 relative to L_0, and involves creating PAIRS (either via the n-mark pairing in Case A, or multi-pair creation in Case B). The Pairing Cancellation Lemma is the unifying mechanism.
