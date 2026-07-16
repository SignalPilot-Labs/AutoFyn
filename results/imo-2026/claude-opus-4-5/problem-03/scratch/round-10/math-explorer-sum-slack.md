# n=5 Case B Sum-Slack Exploration — Lens: Algebraic Coverage Proof

## The 11 Failure Conditions

Each strategy works when |condition| <= 1. It fails when |condition| > 1:

| Strategy | Fails when |
|----------|-----------|
| A1  | |gamma - alpha| > 1 |
| A2  | |delta - beta| > 1 |
| A3  | |delta - (1+alpha+beta)| > 1 |
| A4  | |epsilon - gamma| > 1 |
| A5  | |epsilon - (2+alpha+beta+gamma)| > 1 |
| A-x | |epsilon - beta| > 1 |
| A-y | |alpha - epsilon| > 1 |
| A-z | |alpha - delta| > 1 |
| B3  | |2+2*alpha+beta - delta| > 1 |
| B4  | |2+2*alpha+beta - epsilon| > 1 |
| DB4 | |4+2*alpha+2*beta+gamma - epsilon| > 1 |

## LP Analysis: Minimal Sum in the All-Fail Polytope

Enumerating all 2^11 = 2048 sign combinations for the 11 failure conditions, using
LP to find the minimum of 5*alpha+4*beta+3*gamma+2*delta+epsilon subject to each
strategy weakly failing (|condition| >= 1) and all variables >= 0:

- 108 sign combinations are feasible (others contradictory).
- 97 of those have min_sum >= 16 (consistent with sum constraint).
- **11 sign combinations have min_sum < 16**, with global minimum = 11.0.

The LP minimum 11 is achieved at (alpha, beta, gamma, delta, epsilon) = (1, 1, 0, 0, 2).
At this point, five conditions are EXACTLY = 1: A1, A2, A-x, A-y, A-z.

This means the minimum-sum point lies on the BOUNDARY of the failure polytope
(where some strategies barely work, |condition| = 1 exactly). The STRICT interior
of the failure polytope (all |condition| > 1) might have higher minimum sum.

## CRITICAL FINDING: The Sum-Slack Approach Fails

A numerical search for points with ALL 11 conditions STRICTLY failing (|condition| > 1.01)
AND sum < 16 found:

**Explicit counterexample:**
- alpha = 1.3272, beta = 0.9722, gamma = 0.1400, delta = -0.5627, epsilon = 3.2229
- Sum = 5(1.327)+4(0.972)+3(0.140)+2(-0.563)+3.223 = 13.04 < 16
- All 11 conditions: |A1|=1.19, |A2|=1.54, |A3|=3.86, |A4|=3.08, |A5|=1.22, |A-x|=2.25, |A-y|=1.90, |A-z|=1.89, |B3|=6.19, |B4|=2.40, |DB4|=5.52

**The 11 Singleton-Pair strategies do NOT cover all n=5 Case B configurations.**
The sum-slack approach with just these 11 strategies cannot close the proof.

## Why These 11 Strategies Fail

The counterexample has **delta = -0.563 < 0**, meaning d3 = (1+delta)*L0 < L0.
In the counterexample, d3 < L0 while d4 = 4.22*L0 (very large). The 11 strategies all
compare differences that are "close to each other" or to LB pieces. When d3 is small
AND d4 is large AND P1 is substantially larger than L0, all pairwise comparisons
exceed L0:
- A1, A-z: compare P1 with d2 or d3 — P1 is too large.
- A2: compare d1 with d3 — d1 is large, d3 is small, gap = 1.54*L0.
- A4, A-y: compare epsilon with gamma or alpha — epsilon >> gamma, alpha.
- B3, B4, DB4: compare 2+2*alpha+beta with delta or epsilon — delta too small, epsilon too large.

The structural gap is that the 11 strategies are designed for the regime where
**all d_j >= L0** (beta, gamma, delta, epsilon >= 0), or specifically for when
the differences between consecutive pieces are all at least L0. When delta < 0
(d3 < L0) coexists with large epsilon (d4 >> L0), no Singleton-Pair strategy works.

## But XY CAN Still Limit LB (Different Strategy)

The counterexample config IS valid Case B (P6 = 34.96*L0 = 0.555 > c5 = 0.508).
The **Halve+IH strategy** works:
1. XY halves P6 (1 mark): contributes P6/2 to LB via Pairing Cancellation.
2. XY applies n=4 UB on {P1,...,P5} (4 marks).

For the n=4 sub-game: L_sub = 28.04*L0, Q5 = P5 = 10.10*L0 < c(4)*L_sub = 14.47*L0.
The sub-game is in the n=4 "all small" sub-case (Q5 < c(4)*L_sub).
**Winning sub-game strategy**: "Halve P1, P2, P5; split P4 at 0.01 fraction"

This gives sub-game LB = 0.2260 < c(4)*L_sub = 0.2297. Combined:
LB_total = P6/2 + LB_sub = 0.2774 + 0.2260 = 0.5035 < c5 = 0.5079. ✓

The sub-game strategy "halve P1,P2,P5; split P4 near-zero" creates structure:
- 3 pairs from halvings: {P1/2,P1/2}, {P2/2,P2/2}, {P5/2,P5/2}
- 3 singletons: P3, 0.01*P4 (tiny), 0.99*P4 (≈ P3)
This is **NOT the Singleton-Pair (4 pairs + 2 singletons)** framework.

LB gets: P1/2 + P2/2 + P5/2 (from pairs) + 0.99*P4 + 0.01*P4 (= P4 from singletons).
XY gets P3 (the middle singleton). LB total = (P1+P2+P5)/2 + P4.

## Cascading Proof Gap: the Halve+IH Requires Complete n=4 UB

The Halve+IH for n=5 needs the n=4 upper bound proof to work on ANY
{P1,...,P5} configuration (not just when P5 >= c(4)*L_sub).

**Confirmed gap in n=4 proof**: The n=4 proof in geometric-direct.md handles
P5 >= c(4) via Halve+IH, and claims P5 < c(4) forces at least one d_j < L0.
But numerically: configs with P5 < c(4) AND all d_j > L0 exist (e.g.,
alpha_sub=1.57, beta_sub=1.18, gamma_sub=0.26, eta_sub=-0.52, Q5<c4*L_sub).

In this sub-case (eta_sub < 0, i.e., d3_sub < L0_sub), the standard strategies
S6/S4/S5/BPP all fail:
- S6: |gamma_sub - alpha_sub| = 1.31 > 1. Fails.
- S4: |eta_sub - beta_sub| = 1.70 > 1. Fails.
- S5: |eta_sub - (alpha_sub+beta_sub+1)| = 4.27 > 1. Fails.
- BPP: |2+2*alpha_sub+beta_sub - eta_sub| = 6.85 > 1. Fails.

But XY CAN limit the n=4 sub-game to c(4)*L_sub using a non-Singleton-Pair strategy:
"Halve P2, P5; split P1 at 0.05, P4 at 0.20" → LB = 0.226 < 0.230 = c(4)*L_sub. ✓

**Confirmed gap in n=3 proof**: Similarly for n=3, when P4<c(3) AND d1>L0 AND d2>L0
(e.g., P1=2.2/15, d1=d2=1.1/15, P4=5.1/15 < 8/15 = c(3)), strategies S1/S2/S3b all fail.
But XY CAN limit LB: "split P4 at 0.35, halve P3, split P1 at 0.10" → LB=0.514 < c3. ✓

## What's Needed for the Proof

**Wrong approach**: Adding more Singleton-Pair (4 pairs + 2 singletons) strategies.
The LP shows the "all 4-pair fail" polytope intersects with sum < 16.

**Right approach**: Fix the proof architecture for the "all small pieces" sub-case.

The proof currently has:
- Case A (P1 <= L0): Halve-All. COMPLETE.
- Case B-large (P_{n+1} >= c(n)): Halve+IH. REQUIRES complete n-1 proof.
- Case B-small (P1 > L0, P_{n+1} < c(n)): INCOMPLETE for n >= 3.

**Key opening for the outliner**: The "all small" sub-case (all pieces in (L0, c(n)))
needs its own argument. The winning strategy structure appears to be:
- "2 halvings + 2 non-symmetric splits": creates 2 pairs + 5 singletons (9 pieces).
- One split creates a "near-zero" piece (LB forced to take it) while XY takes the
  middle singleton. This reduces LB's effective score.

**Algebraic condition for "2-pair + 5-singleton" strategy (observed pattern)**:
When all pieces are in (L0, c(n)), halving P_2 and P_{n+1} (creating 2 pairs)
and then splitting P_1 at fraction f1 and P_n at fraction f2 to minimize:
LB = P_2/2 + P_{n+1}/2 + lb_score({f1*P1, (1-f1)*P1, P_3, f2*P_n, (1-f2)*P_n})
Subject to the lb_score of 5 singletons being minimized.

The analysis in n=3 shows: lb_score({P4-P2, t, P1-t}) = P4-P2+P1 - middle, 
minimized by choosing t = P4-P2 (making {P4-P2, P4-P2, P1-2*(P4-P2)}).
This gives LB = P1+P2+P3/2 (when P3 = 2*P1) in the specific n=3 example.

**More general formula (to be proved)**: LB from "all small" strategy <= c(n) iff
sum constraint from "P_{n+1} < c(n) and all pieces > L0" gives enough slack.

## Recommendations for Outliner

1. **Do not pursue sum-slack with 11 strategies**: The polytope "all 11 fail AND sum<16" is non-empty. The approach is provably insufficient.

2. **Restructure the proof**: Fix n=3 and n=4 "all small" proofs FIRST:
   - n=3 "all small" (P4 < c(3), d1>L0, d2>L0): Need S4 strategy using
     "cut P4 at P2, halve P3, cut P1 at P4-P2" → LB = P1+P2+P3/2 <= c(3)
     iff 5*alpha+3*beta+gamma <= 7 (to be proved from ordering constraints).
   - n=4 "all small": Need new "2-halve + 2-split" strategy.

3. **Verify Halve+IH chain**: Once n=3 and n=4 "all small" are proved, the
   Halve+IH strategy for n=5 becomes complete:
   - P6 >= c(5): Halve+IH (1 mark on P6 + n=4 full UB on sub-game). Done.
   - The n=4 full UB covers ALL {P1,...,P5} including P5 < c(4)*L_sub.

4. **The 11 strategies ARE a correct cover for the sub-case where all d_j > L0 AND
   the "cascade" conditions hold** (gamma >= alpha+1, etc.). They may be reusable as
   part of the proof once the "all small" gap is fixed.

## Partial Algebraic Results

**If A1, A-z BOTH fail from the same side** (gamma > alpha+1 AND alpha > delta+1):
Then gamma > alpha+1 > delta+2+1 = delta+2, so gamma - delta > 2. And
5*alpha + 4*beta + 3*gamma + 2*delta + epsilon < 16. Substituting: This forces
specific bounds on other variables.

**If A4, A-y, A-x all fail** (|epsilon-gamma|>1, |alpha-epsilon|>1, |epsilon-beta|>1):
These together imply epsilon >> gamma, alpha (or epsilon << all of them). If epsilon is large:
epsilon > gamma+1, epsilon > alpha+1, epsilon > beta+1. Sum constraint:
5*alpha+4*beta+3*gamma+2*delta+epsilon < 16. The minimum of epsilon alone must be < 16,
which is trivially true. But combined with the other constraints from B4 failing:
2+2*alpha+beta < epsilon-1 (B4 fails upward). This means epsilon > 3+2*alpha+beta >= 3.
But then 5*alpha+4*beta+epsilon > 5*alpha+4*beta+3+2*alpha+beta = 7*alpha+5*beta+3.
For this < 16: 7*alpha+5*beta < 13, which is achievable. **So partial chains of
failures don't immediately contradict sum < 16.**

The only route to a contradiction requires using ALL 11 conditions simultaneously,
and as shown, this is not achievable with the sum constraint alone.

## Conclusion

The sum-slack argument with the 11 Singleton-Pair strategies is **insufficient** to
prove n=5 Case B coverage. The proof requires:
1. A complete "all small" argument for n=3 (new strategy S4 or S3-extended).
2. A complete "all small" argument for n=4 (new "2-halve+2-split" strategy).
3. The Halve+IH chain then closes n=5 automatically.

The 11 strategies may still be useful as part of a broader n=5 proof for specific
sub-cases (all d_j >= L0), but they cannot be the SOLE coverage argument.
