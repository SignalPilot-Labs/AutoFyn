# Math Explorer Report: Inductive Pattern from n to n+1
## Problem: imo-2026-03

---

## CRITICAL FINDING: The True Open Gap Is n=3 B_small "all d_j > L0"

The run_state says the open gap is "Case B for n>=5 needs algebraic proof." This is WRONG. The gap starts at n=3.

### Where the n=3 Proof Breaks

The n=3 Case B proof in `geometric-direct.md` (lines 377-545) has a structural gap. It handles:
- **P4 >= c3 = 8*L0**: Halve+IH (proved round 9). ✓
- **P4 < c3 with some d_j <= L0**: S1 (d1<=L0), S2 (d2<=L0). ✓
- **P4 < c3 with all d1,d2 > L0 and P4 < c3**: Claims S3 applies. WRONG.

S3's key claim is "when d1>L0 and d2>L0, the sum constraint P1+P2+P3 < 7*L0 forces d2 < 2*L0, hence d2-P1 < L0." But this sum constraint comes from **P4 > c3 = 8*L0 (B_large)**! In B_small (P4 < c3), the constraint REVERSES to P1+P2+P3 > 7*L0, and d2 can be arbitrarily large.

**Numerical verification**: 90108/496738 B_small "all d1,d2>L0" configs fail S3 (using correct sum-to-1 sampling).

### B_small Missing Case Is Genuine But Fixable

**XY CAN always win** for n=3 B_small (optimization with 3 XY marks found 0 failures in 367 valid configs). The proof gap is algebraic, not a conceptual failure.

**Missing strategies for n=3 B_small "all d_j > L0"**:

Strategy `S_d3` (when d3=P4-P3 <= L0): halve P1, halve P2. Singletons: {P3, P4}. LB = 1/2+d3/2 <= c3. Uses 2 marks. ✓ (Not in current proof!)

Strategy `S_P3P4v`: halve P1, cut P4 at any v in (d3, P2). Sorted order: P3 > P4-v > P2 > v > P1/2. LB = P3+P2+P1/2 = (5/2)*P1+2*d1+d2. Works when this is <= c3.

Combined coverage of n=3 B_small needs:
- S1: d1 <= L0
- S2: d2 <= L0
- **S_d3 (NEW)**: d3 <= L0
- When all d1,d2,d3 > L0: a sum-slack argument or additional strategies.

**Key sum-slack constraint for n=3 all-large-d sub-case**: From 4*P1+3*d1+2*d2+d3=1 with all > L0: the "slack" = 4a+3b+2c+e = 1/3 where a=P1-L0, b=d1-L0, c=d2-L0, e=d3-L0 >= 0. This is VERY TIGHT (versus B_large where 4a+3b+2c+e < 1/3 - which was wrong: B_large reverses this).

---

## Sum Constraint Reversal (Critical)

For the upper bound, the two regions have OPPOSITE sum constraints:

| Region | Constraint on sorted pieces |
|--------|---------------------------|
| B_large (P_{n+1} >= c(n)) | n*alpha + (n-1)*b1 + ... + b_{n-1} < RHS(n) |
| **B_small (P_{n+1} < c(n))** | **n*alpha + (n-1)*b1 + ... + b_{n-1} > RHS(n)** |

where RHS(n) = 2^n - 1 - n(n+1)/2 and alpha = P1/L0-1, b_j = d_j/L0-1.

For n=3: RHS=1. B_large: 3*alpha+2*beta+gamma < 1. B_small: 3*alpha+2*beta+gamma > 1.

**Consequence**: All strategies and sum-slack arguments from B_large (including the 11 n=5 strategies claiming 0/500k failures) were tested on B_large configs. The B_small region has the constraint reversed and requires completely different analysis.

---

## Strategy Count Pattern

| n | B_large strategies | B_small strategies (known) |
|---|-------------------|---------------------------|
| 3 | S1, S2, S3 (via Halve+IH + d_j<=L0) | S1, S2, S_d3 + ???  |
| 4 | S6, S4, S5, BPP (from round 7) | Same S1'/S2'/S3' + S6/S4/S5/BPP??? |
| 5 | 11 strategies A1-A5, B3, B4, DB4 | Unknown |

Critical question: Do the SAME explicit strategies (S_j-type) that work in B_large also work in B_small? Likely not, because they use the B_large sum constraint.

**N=3 B_small "all d_j > L0" exhaustive search**: Strategy `S_P3P4v` (halve P1, cut P4 at v in (d3, min(P2, P4-P3+epsilon))) gives LB = P3+P2+P1/2. Condition: (5/2)*P1+2*d1+d2 <= c3.

When this fails (large P1+d1): need further strategy. Optimization confirms XY can always win but no clean algebraic formula was found.

---

## Case A Constraint Pattern for General n (Confirmed)

From prior exploration (correct):
- The "all-d_j-large" gap-width formula: gap between S_{n-1}-coverage and BPP-coverage = alpha - 1.
- This is negative iff alpha < 1.
- In B_large deepest Case A: alpha < 1 is forced by sum constraint for all n.
- For n=3,4: alpha < 1/3. For n=5: alpha < 9/10. Pattern: margin toward 0 as n grows.

**This argument applies only in B_large (sum constraint < RHS)**. In B_small (sum > RHS), alpha can be large and the gap-width argument breaks.

---

## Induction Structure Assessment

**Strong induction from n-1 to n for B_small**: NO clear structure found. The Halve+IH strategy (which IS inductive) works only for B_large (P_{n+1} >= c(n)). For B_small, induction would need to reduce to an (n-1)-game with pieces summing differently.

**One possible inductive angle for B_small**: If LB's largest piece P_{n+1} < c(n), then the SUM of all pieces except P_{n+1} is > 1-c(n) = (2^n-1)*L0. LB's pieces are "spread out" (large differences). XY might use all n marks to "pair up" adjacent pieces, creating n/2 pairs and 1-2 singletons. The singleton-difference condition then depends on the pairwise gaps.

The formula for n=3: when d3<=L0, halve P1 and P2 → singletons {P3, P4}, LB = 1/2+d3/2 <= c3. Analog for general n: when d_n = P_{n+1}-P_n <= L0, halve P1,...,P_{n-1} using n-1 marks → singletons {P_n, P_{n+1}}, LB = 1/2+d_n/2 <= c(n). This uses n-1 marks and handles the "last difference small" case.

The analog for each d_j <= L0: if d_j <= L0, XY can always win B_small by creating singletons near P_j and P_{j+1}. This covers the "at least one small difference" sub-case.

The hard sub-case: **B_small with ALL d_j > L0**. This is the TRUE remaining gap.

---

## Small-Case Evidence for B_small "All d_j > L0"

**N=3**: Sum constraint 3*alpha+2*beta+gamma > 1 (B_small). RHS(3) = 1.
- All d_j > L0: alpha,beta,gamma > 0.
- P4 < c3 forces alpha+beta+gamma < 4 (since P4 = 4*L0+something < 8*L0).
- Strategy "halve P1, cut P4 at v in (d3,P2)" gives LB=(5/2)*P1+2*d1+d2 = (5/2+2+1)*L0 + (5/2*a+2*b+c) = (9.5*L0 + extra). For LB <= c3=8*L0: 5/2*a+2*b+c <= -1.5*L0 < 0. IMPOSSIBLE unless the ordering condition changes.

Wait - the formula LB = P3+P2+P1/2 uses specific ordering. If the ordering is different, the formula changes. The optimization finds v that achieves LB around 0.50 in practice.

**N=3 actual computed examples**: For P1=0.0767, P2=0.1533, P3=0.32, P4=0.45 (exact fractions): optimization gives LB = 0.5117 < c3 = 0.5333. XY wins by halving P1 and cutting P4 at v ≈ 0.3085 (creating sub-pieces {0.3085, 0.1415} from P4). LB picks P3=0.32, P2=0.1533, P1/2=0.0383 in sorted order.

**Key formula**: LB = P3+P2+P1/2 when P3 > P4-v > P2 > v > P1/2, i.e., d3 < v < P2. This range is non-empty when d3 < P2. For this to achieve LB <= c3: P3+P2+P1/2 = (5/2)*P1+2*d1+d2 <= 8/15. With 4*P1+3*d1+2*d2+d3=1: the condition becomes expressible in terms of P1, d1, d2, d3. A sum-slack argument might close this.

---

## Distinct Openings for the Outliner

1. **Fix n=3 B_small directly**: Add S_d3 (halve P1, halve P2 when d3<=L0) to the proof. Then handle "all d_j > L0" sub-case for n=3 B_small via a separate sum-slack argument using 3*alpha+2*beta+gamma > 1 and alpha+beta+gamma < 4. Candidate: show 5/2*P1+2*d1+d2 <= c3 follows from the B_small sum constraint when the ordering condition is satisfied, and when it's not, a different strategy works.

2. **Bypass B_small entirely via different case split**: Instead of splitting by P_{n+1} vs c(n), split by "is the SECOND-LARGEST piece >= c(n-1) or not?" This might allow a cleaner inductive structure that avoids the B_small/B_large asymmetry.

3. **Use LP duality / linear programming** to certify that for n=3,4 B_small "all d_j > L0", the system of strategy-failure conditions (each |s2-s1| > L0) is infeasible given sum constraints. This is a finite-dimensional LP.

4. **Strategy family approach**: For B_small with all d_j > L0, note that the n+1 differences {d0=P1, d1=P2-P1, ..., d_{n-1}=P_{n+1}-P_n} form a CHAIN. The B_small condition + sum constraint constrains this chain. A pairwise-comparison argument: among all pairs (d_i, d_j), some pair has |d_i-d_j| <= L0 (pigeon-hole). The corresponding singleton-difference strategy achieves LB <= c(n). CONJECTURE - needs algebraic verification.

5. **Separate the case d_n = P_{n+1}-P_n**: In B_small, P_{n+1} is not much above P_n (since both are < c(n)). If d_n <= L0, S_d_n works. If d_n > L0, the sum constraint is very tight. Explore if d_n > L0 in B_small leads to contradiction (sum would exceed 1).

---

## Candidate Techniques

- **Singleton-Pair Formula** (certified lemma): LB = 1/2 + (s2-s1)/2. Core tool for all strategies.
- **Pairing Cancellation Lemma** (certified): Used in all pair-based strategies.
- **Sum-slack argument**: Show all strategy conditions cannot fail simultaneously given sum constraint. Works for B_large; needs adaptation for B_small with REVERSED constraint.
- **LP infeasibility**: For finite n, show the failure polytope is empty via LP.

## Cheap-Kill Candidates

- **S_d3 strategy** (NEW, trivial to add to proof): when d_{n-1} = P_{n+1}-P_n <= L0, halve P1,...,P_{n-1}. Singletons {P_n, P_{n+1}}. LB = 1/2+d_{n-1}/2 <= c(n). This covers one more sub-case in B_small and is completely algebraic. Cost: 0 (just add to proof).

- **Check n=3 "all d_j > L0" via LP**: 3 parameters (alpha, beta, gamma) with 3*alpha+2*beta+gamma > 1, alpha,beta,gamma > 0, alpha+beta+gamma < 4. All 5 strategy-failure conditions form a polytope. Verify LP infeasibility (= XY always wins). Quick computation.

## Knowledge-Base Entries

- Pairing Cancellation Lemma (in proof, certified)
- Singleton-Pair Formula (in proof, certified)
- Greedy Optimality (certified)
- Sum-slack / pigeonhole on pairwise diffs (round 6 notes in knowledge_base)

## Analogous Past Problems

- None identified that directly match the B_small "reversed sum constraint" structure.

## Prior Progress

- n=1,2,3,4: claimed proved, but n=3 B_small "all d_j > L0" has a gap in S3's application.
- n>=5 B_large: proved by Halve+IH.
- n=5 B_small: 11 strategies identified but tested on WRONG region (B_large).
- n=3 B_small "all d_j > L0": algebraic gap confirmed; XY CAN win (optimization shows 0 failures); specific strategies known for sub-sub-cases; full algebraic coverage still open.

## Dead Ends (Do Not Retry)

- "S1/S2/S3 cover all n=3 Case B" - FALSE for B_small "all d_j > L0". S3 uses B_large sum constraint.
- "11 n=5 strategies cover all Case B" - Tested on B_large region only (sum < RHS). B_small region (sum > RHS) was never tested.
- "Sum constraint forces d2 < 2*L0 in B case" - Only true in B_LARGE. In B_small constraint reverses.
- "XY cannot win n=3 B_small with 2 marks" - WRONG. XY can (e.g., halve P1 + cut P4 at v).

## Small-Case / Intuition Notes

**Conjecture**: For n=3 B_small "all d_j > L0", strategy "halve P1, cut P4 at any v in (d3, P2)" achieves LB = P3+P2+P1/2, and the B_small sum constraint (3*alpha+2*beta+gamma > 1) PLUS the "all d_j > L0" condition can be shown to force P3+P2+P1/2 <= c3. Numeric: 0 failures in 367 valid configs tested by optimization. Label as conjecture; full proof needed.

**Conjecture**: For general n, B_small with all d_j > L0 can be handled by strategies of the form "halve P1,...,P_{n-2}, cut P_{n+1} at v" (using n-1 marks, leaving P_{n-1} and P_n as "large singletons" and the P_{n+1} cut creates the pair). LB = P_n + P_{n-1} + sum of pairs. The condition is controlled by the reversed sum constraint.
