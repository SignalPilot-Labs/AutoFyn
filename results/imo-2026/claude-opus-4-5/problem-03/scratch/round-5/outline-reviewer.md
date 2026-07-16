# Outline Review: Round 5

## Approach: geometric-direct (REVISE)

### Verdict: CHANGES REQUESTED

The outline is sound but has under-specified sub-case analysis in Strategy S3 for n=3, and the general-n gap mechanism is not yet proven. The technique is correct and should proceed to building.

### What I verified

1. **Case A halve-all strategy**: SOUND. Verified algebraically and computationally for n=1 to n=5. The formula LB = 1/2 + P_1/2 <= c(n) when P_1 <= L_0 is correct. The Pairing Cancellation application is valid.

2. **n=3 Case B Strategy S3 (critical check)**: SOUND WITH CLARIFICATION NEEDED.
   - The claim d_2 - P_1 < L_0 when d_1 > L_0 and d_2 > L_0 is CORRECT for Case A (d_2 > P_1).
   - However, the approach file's analysis of Case B (d_2 <= P_1) is incomplete. I verified algebraically:
     - When d_2 <= P_1 AND d_1 > L_0 AND d_2 > L_0 AND P_1 > L_0: the bound P_1 - d_2 <= L_0 holds.
     - Proof: If P_1 > d_2 + L_0, then 3*P_1 + 2*d_1 + d_2 > 3*(d_2 + L_0) + 2*L_0 + d_2 = 4*d_2 + 5*L_0. For this to be < 7*L_0, need d_2 < L_0/2, contradicting d_2 > L_0.
   - The builder must add this sub-case analysis explicitly.

3. **n=2 Case B four sub-cases**: SOUND. Verified computationally.

4. **General-n Case B (the gap)**: The outline correctly identifies this as open. I verified computationally:
   - For n=4: With the complete strategy family (split one piece to match another, halve subsets), ALL Case B configs achieve LB <= c(4). Max gap = 0 in 100k trials.
   - For n=5: Same result with complete strategy family. The "gap" found in quick tests was due to incomplete strategy enumeration.
   
   **Key insight**: The general-n proof should enumerate the strategy family systematically:
   - For each j in {1,...,n}: Strategy S_j creates singletons (P_j, P_{j+1}) with n-1 pairs by splitting/halving. When d_j <= L_0, this gives LB <= c(n).
   - The "all d_j > L_0" case needs the sum-slack argument.

### Issues to fix while building

1. **Complete the S3 sub-case analysis for n=3**: Add the explicit proof that P_1 - d_2 <= L_0 when d_2 <= P_1 (the contradiction argument via 4*d_2 + 5*L_0 < 7*L_0).

2. **State the general-n strategy family explicitly**: The builder should formulate:
   - Strategy S_j (j = 1,...,n-1): When d_j <= L_0, XY creates singletons (P_j, P_{j+1}).
   - Strategy S_n (combination): When all d_j > L_0, use the sum-slack bound to show some combination achieves LB <= c(n).

3. **The sum-slack bound for general n**: The claim "max_j(d_j) < ((2^n-1) - n(n+1)/2)/(n-1) * L_0" needs proof. The key is:
   - n*P_1 + sum_{j=1}^{n-1} (n-j)*d_j < (2^n - 1)*L_0
   - With each term > L_0, this gives algebraic slack.

4. **The singleton-pair formula**: This is stated but not proved formally. The builder should prove: when XY creates 2n pieces as (n-1) pairs + 2 singletons s_1 < s_2, then LB = (1 - s_1 + s_2)/2.

### Load-bearing lemmas

| Lemma | Mechanism | Status |
|-------|-----------|--------|
| Halve-All Strategy | Pairing Cancellation applied n times | SOUND |
| Singleton-Pair Formula | Pairing Cancellation + greedy sorting | Stated, needs proof |
| Sum-Slack Bound (n=3) | Contradiction via 3*P_1 + 2*d_1 + d_2 < 7*L_0 | SOUND |
| Sum-Slack Bound (general n) | Averaging on constraint | OPEN GAP |

### Case coverage

- Case A (P_1 <= L_0): COMPLETE
- Case B trivial (P_{n+1} <= c(n)): COMPLETE
- Case B n=1: COMPLETE
- Case B n=2: COMPLETE (4 sub-cases)
- Case B n=3: COMPLETE (3 strategies, but sub-case analysis for S3 needs explicit proof)
- Case B n >= 4: OPEN (computationally verified, algebraic proof missing)

### Prior dead ends avoided

The outline correctly avoids:
- induction-on-n (dead-ended in Round 1)
- "always split P_1" strategies (fails for small P_1)
- Equal sub-pieces of P_{n+1} (fails when r < 0)

---

## Ranking update

The approaches in the population:
1. **geometric-direct** (Elo 1620, last: partial) - Lower bound proved, upper bound Case A proved, Case B n=2,3 proved, general-n gap narrowing
2. **minimax-saddle-point** (Elo 1528) - Not built, alternative LP route
3. **minimax-value** (Elo 1476) - Not built, similar to minimax-saddle-point
4. **induction-on-n** (Elo 1468, dead-end) - Fatal flaw in Round 1
5. **piece-count-parity** (Elo 1430) - Not built, parity analysis

**Comparisons**:
- geometric-direct vs minimax-saddle-point: geometric-direct has progressed (Case A filled, n=3 verified), minimax-saddle-point has not been built. Winner: geometric-direct.
- geometric-direct vs induction-on-n: induction-on-n is dead-ended. Winner: geometric-direct.
- minimax-saddle-point vs piece-count-parity: Both unbuilt; saddle-point has cleaner theoretical framework. Draw (insufficient evidence).

---

## Build set

The outliner recommends building only geometric-direct this round, which is correct. The approach is close to completion - with the n=3 sub-case clarification and an attempt at the general-n sum-slack lemma, this could reach solved status.

build set: geometric-direct
