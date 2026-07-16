# Outline Review: Round 4

## geometric-direct: advance

**Verdict: RETHINK**

### Summary of the Proposed Approach

The outline proposes to close the upper bound gap using:
1. **Pairing Cancellation Lemma**: For any multiset S and v > 0, LB_score({v, v} ∪ S) = v + LB_score(S).
2. **Induction on n**: XY's strategy is to split the largest piece P_1 in half (use 1 mark), then apply the (n-1)-case strategy to the sub-game {P_2, ..., P_{n+1}}.
3. **Case split**: If P_1 <= c(n), XY uses 0 marks; if P_1 > c(n), XY splits P_1.

### Verification Results

**Pairing Cancellation Lemma: VERIFIED**
- Tested with 100 random cases and several specific examples.
- The parity argument is sound: two copies of v insert at consecutive positions, one goes to each player, all other parities shift by 2 (unchanged).

**Algebraic Identity c(n-1) = c(n)/(2(1-c(n))): VERIFIED**
- Confirmed for n = 2, 3, 4, 5, 6 via direct computation.

**Sub-game reduction: VERIFIED**
- After splitting P_1, the sub-game {P_2, ..., P_{n+1}} has n pieces and XY has n-1 marks remaining.
- This is exactly the (n-1)-case: (n-1)+1 = n pieces with n-1 marks.

### Critical Flaw #1: The "0 marks" case claim is nonsensical for n >= 2

The outline claims (line 12): "If P_1 <= c(n), XY uses 0 marks, LB gets at most P_1 <= c(n)."

**This claim is nonsensical for n >= 2.** With n+1 >= 3 pieces, LB picks ceil((n+1)/2) >= 2 pieces at odd positions in sorted order. LB's total is the sum of pieces at odd positions, NOT just a single piece.

Verified counterexample for n=2: Config [4/7, 2/7, 1/7] (the geometric config, P_1 = largest = 4/7).
- P_1 = 4/7 <= c(2) = 4/7. By the outline, XY uses 0 marks.
- LB picks positions 1, 3 from [4/7, 2/7, 1/7]: LB = 4/7 + 1/7 = 5/7 > c(2) = 4/7.

XY MUST use marks even against the geometric config! The "0 marks" case cannot work as stated.

### Critical Flaw #2: The "always split P_1" strategy fails for P_1 < c(n)

Ignoring the broken "0 marks" case, suppose XY always splits P_1 and applies the induction. The algebraic bound is:

f(P_1) = P_1/2 + c(n-1)*(1-P_1)

The outline claims this is <= c(n). But the algebra shows f(P_1) <= c(n) **if and only if P_1 >= c(n)**.

Verification: The threshold is exactly c(n) because f is linear with slope (1/2 - c(n-1)) < 0 (since c(n-1) > 1/2), and f(c(n)) = c(n) exactly.

For P_1 < c(n), the worst-case bound gives f(P_1) > c(n).

**Counterexample: Config [2/5, 2/5, 1/5] for n=2 (P_1 = 2/5 < c(2) = 4/7)**
- Sub-game [2/5, 1/5] scales to [2/3, 1/3] = the geometric config for n=1.
- XY splits P_1, applies n=1 strategy to sub-game.
- Sub-game achieves LB = c(1) * (1-P_1) = 2/3 * 3/5 = 2/5 (tight at geometric).
- Total: P_1/2 + 2/5 = 1/5 + 2/5 = 3/5 = 0.6 > c(2) = 4/7 = 0.571. **FAILS!**

However, XY CAN limit this config to <= c(2) using a different strategy:
- Split P_3 = 1/5 instead of P_1.
- Pieces: [2/5, 2/5, 1/10, 1/10]. LB picks 2/5 + 1/10 = 1/2 < c(2). OK!

The outline's single-strategy induction is fatally flawed.

### Summary of Fatal Flaws

1. **"0 marks" case is nonsensical**: The claim "LB gets at most P_1" when XY uses 0 marks is simply false for n >= 2. LB picks multiple pieces.

2. **"Always split P_1" fails for P_1 < c(n)**: The inductive bound f(P_1) > c(n) when P_1 < c(n), and there exist configs (like [2/5, 2/5, 1/5]) where the sub-game achieves the worst case.

3. **No fallback strategy specified**: The outline provides no mechanism to handle P_1 < c(n) configs. A different XY strategy is required for each such config.

### Why the outline cannot be fixed with minor changes

The core issue is that the Pairing Cancellation + induction approach does NOT yield a uniform XY strategy. Different LB configs require different XY responses:
- For P_1 >= c(n): split P_1, apply IH. Works.
- For P_1 < c(n) and sub-game NOT geometric: splitting P_1 still works (actual < bound).
- For P_1 < c(n) and sub-game IS geometric: splitting P_1 fails. XY must use a different strategy (e.g., split a smaller piece, or use multiple marks elsewhere).

The outline has no mechanism to handle the third case. A complete proof requires:
1. Characterizing which configs have P_1 < c(n) with geometric sub-game.
2. Providing an explicit XY strategy for each such config.

This is a fundamental restructuring, not a gap to close while building.

### Issues with other proposed approaches

**pairing-cancellation-induction: new** - Same fatal flaw as geometric-direct (it's essentially the same approach repackaged).

**two-strategy-cover: new** - The case split on P_1 vs L_0 is more nuanced but:
- Case 2a (P_{n+1} > c(n) and P_1 > L_0) is only computationally verified for n=3, not proved.
- The algebraic argument for general n is explicitly flagged as a "gap".
- Better than geometric-direct but still incomplete.

**minimax-saddle-point: advance** - The concavity/saddle-point argument gives intuition but:
- "Uniqueness of critical point" is hand-waved.
- No explicit XY strategy construction.
- More conceptual gaps than direct approaches.

### Existing approaches in the ranking

- **geometric-direct** (Elo 1598, partial): Has complete lower bound but flawed upper bound proposal.
- **induction-on-n** (Elo 1468, dead-end): Upper bound fatally flawed.
- **minimax-saddle-point** (Elo 1528, never built): Structural but vague.
- **minimax-value** (Elo 1476, never built): Similar to saddle-point.
- **piece-count-parity** (Elo 1430, never built): Unknown status.

---

## Approach Registration

The three new approaches from the outliner (pairing-cancellation-induction, two-strategy-cover, minimax-saddle-point) should NOT be registered because:
- pairing-cancellation-induction has the same fatal flaw as geometric-direct.
- two-strategy-cover has explicit gaps in Case 2a.
- minimax-saddle-point is already in the ranking (duplicate name).

No new registrations this round.

---

## Ranking Update

Based on this analysis:

1. **geometric-direct** remains the strongest (has complete lower bound, verified answer, most progress toward upper bound) despite the failed outline proposal.
2. **minimax-saddle-point** is still viable as a conceptual framework but has no progress.
3. **two-strategy-cover** (if it were registered) would be promising due to its explicit case analysis, but has unfilled gaps.
4. **induction-on-n** is dead-ended.

Comparisons:
- geometric-direct > minimax-saddle-point (geometric-direct has proved lower bound + verified formula)
- geometric-direct > minimax-value (same reason)
- minimax-saddle-point vs piece-count-parity: insufficient evidence for ordering

---

## Recommendation

The outline's proposed approach (Pairing Cancellation + induction with "split largest") is **fatally flawed** for configs where P_1 < c(n) and the sub-game is geometric.

**Direction for next round**:
1. The **two-strategy-cover** approach (Case 2b pairing for P_1 <= L_0, different strategy for P_1 > L_0) is more promising because it explicitly handles the problematic region.
2. The Case 2b part ("pairing creates n pairs") is proved algebraically for general n.
3. The gap is Case 2a (P_1 > L_0 and P_{n+1} > c(n)): needs an explicit XY strategy and algebraic proof.

Alternatively: abandon the "single recursive strategy" paradigm and prove the upper bound by:
- Direct LP/minimax analysis showing geometric is the unique saddle point.
- Exhaustive case analysis with multiple XY strategies depending on config type.

---

## Note on geometric-direct.md Status Discrepancy

The approach file `geometric-direct.md` claims "Status: solved" but `current.md` says "Status: partial". The approach file's upper bound proof says "extends naturally to general n" which is hand-waving. The reviewer-owned `current.md` is authoritative: the problem is NOT solved.

---

## Build Set

**build set: none**

No approach should be built this round. The geometric-direct outline proposal is fatally flawed, and sending it to the builder would waste effort on a doomed line.

**Recommended actions for next round**:

1. **The outliner must produce a corrected approach** that handles the P_1 < c(n) case properly. The two-strategy-cover framework (from the induction explorer) is more promising:
   - Case 2b (P_{n+1} > c(n) and P_1 <= L_0): Proved algebraically using the pairing construction.
   - Case 2a (P_{n+1} > c(n) and P_1 > L_0): Needs explicit proof.
   - Case 1 (P_{n+1} <= c(n)): Trivial.

2. **The Pairing Cancellation Lemma is VALID** and should be preserved. But it must be applied to the RIGHT piece (not always P_1).

3. **Key insight from the counterexample**: When P_1 < c(n), XY may need to split a SMALLER piece (not P_1) to achieve LB <= c(n). The optimal XY strategy depends on the full config, not just P_1.

4. **Alternative direction**: Use direct LP/minimax to show the geometric config is the unique saddle point, avoiding the recursive structure entirely.

---

## Ranking Comparisons (for orchestrator to apply via MCP)

```json
[
  {"winner": "geometric-direct", "loser": "minimax-saddle-point"},
  {"winner": "geometric-direct", "loser": "minimax-value"},
  {"winner": "geometric-direct", "loser": "induction-on-n"},
  {"winner": "geometric-direct", "loser": "piece-count-parity"},
  {"winner": "minimax-saddle-point", "loser": "induction-on-n"},
  {"winner": "minimax-value", "loser": "induction-on-n"}
]
```

build set: none
