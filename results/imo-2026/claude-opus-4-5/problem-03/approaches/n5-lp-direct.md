# Approach: n5-lp-direct

## Status
partial

## Target
Prove c(5) = 32/63 via LP-based verification that (2,1,1) template coverage sets cover the entire Tier 3 bounded region.

## Approaches tried
- n5-lp-direct (Round 17) — LP coverage verification for n=5 Tier 3 region. Key findings:
  1. All 31 Z-type vertices have positive margin with exact rational arithmetic (min margin = 1/2520 at wrs=40).
  2. For each fixed template T, LB(x,T) is CONVEX in x (sum of 5 largest of 10 linear functions = max over 252 subsets).
  3. The "copy" templates (where cuts create copies of existing piece sizes) achieve LB <= c(5) at all 31 Z-type vertices.
  4. However, "copy" templates do NOT cover all interior points (small negative margins observed in grid sampling, ~-0.0001 to -0.0006).
  5. GENERAL (2,1,1) strategies with optimized cut positions DO cover the interior points that "copy" templates miss (verified on individual uncovered points, margin improvement from -0.00008 to +0.00786).
  **GAP:** Full algebraic proof of interior coverage requires showing that for EVERY config x in Tier 3, SOME (2,1,1) template achieves LB(x,T) <= c(5). The convexity of LB(x,T) for fixed T is established, but the union-of-convex-sets coverage is not yet rigorously closed.

## Current best

**Three-Tier Strategy Cascade (FRAMEWORK ESTABLISHED)**

For n=5 with 6 pieces P_1 <= ... <= P_6, define shifted params alpha = P_1/L_0 - 1, beta = d_1/L_0 - 1, etc., where L_0 = 1/63.

**Tier 1 (V_j strategies) and Tier 2 (Pairwise strategies):** CERTIFIED in prior rounds.

**Tier 3 (Bounded region):** When all pairwise diffs > 1 and all params > 0, the config lies in a bounded region with g in (1, 6/5) and v_0 in (0, 1/3).

---

### Key Structural Lemma: LB(x,T) is Convex

**Lemma (LB Convexity):** For each fixed (2,1,1) template T, the function LB(x,T) is convex in the configuration x.

*Proof:* A (2,1,1) template creates 10 output pieces, each of which is a linear function of the input piece sizes (P_1, ..., P_6). Specifically:
- Halved piece: P_H/2, P_H/2
- 2-cut piece: c_1, c_2 - c_1, P_D - c_2 (where c_1, c_2 are cut positions)
- 1-cut piece: c_3, P_C - c_3
- 3 unchanged pieces

When cut positions are fixed linear combinations of piece sizes (as in "copy" templates), all 10 output pieces are linear in (P_1, ..., P_6).

LB = sum of 5 largest of these 10 linear functions. This equals:

LB(x,T) = max_{S subset of {1,...,10}, |S|=5} sum_{i in S} piece_i(x)

The maximum over C(10,5) = 252 linear functions is convex (pointwise supremum of linear functions). QED.

**Corollary:** For each template T, the coverage set C_T = {x : LB(x,T) <= c(5)} is a convex set (sublevel set of a convex function).

---

### 31 Z-Type Vertices: Exact Rational Verification

**Theorem:** All 31 Z-type vertices (v_0 = 0, r_alpha = 0, wrs in {35,...,41}) satisfy LB(v, T_v) <= c(5) for some (2,1,1) "copy" template T_v.

*Proof:* Exact rational arithmetic verification for each vertex.

**Summary by wrs:**

| wrs | Count | Min Margin | Example Template |
|-----|-------|------------|------------------|
| 35 | 1 | 1/126 | (2,3,0,1,5,4) |
| 36 | 4 | 1/756 | (1,5,0,4,3,2) |
| 37 | 3 | 16/2331 | (2,3,0,1,5,4) |
| 38 | 6 | 5/798 | (1,3,0,2,5,4) |
| 39 | 7 | 2/273 | (3,5,0,4,2,1) |
| 40 | 6 | 1/2520 | (2,3,0,1,5,4) |
| 41 | 4 | 13/1722 | (3,2,0,1,5,4) |

**All margins are strictly positive.** Minimum margin: 1/2520 at wrs=40, vertex ranks (0,3,2,1,5,4).

---

### Detailed Verification for wrs=35 (Exact)

**Vertex data:**
- wrs = 35, v_0 = 0, g = 6/5
- Permutation ranks: (r_alpha, r_beta, r_gamma, r_delta, r_epsilon, r_zeta) = (0, 1, 2, 3, 4, 5)
- Shifted params: alpha = 0, beta = 6/5, gamma = 12/5, delta = 18/5, epsilon = 24/5, zeta = 6

**Piece sizes (exact rational):**
- P_1 = 1/63
- P_2 = 16/315
- P_3 = 11/105
- P_4 = 8/45
- P_5 = 17/63
- P_6 = 8/21

**Template: H=2, D=3, S1=0, S2=1, C=5, S3=4**

This means:
- Halve P_3 (index 2): creates {11/210, 11/210}
- 2 cuts on P_4 (index 3) at positions P_1 and P_1+P_2: creates {1/63, 16/315, 1/9}
- 1 cut on P_6 (index 5) at position P_5: creates {17/63, 1/9}
- Singletons: P_1, P_2, P_5 (indices 0, 1, 4)

**Output 10 pieces:**
{1/63, 1/63, 16/315, 16/315, 11/210, 11/210, 1/9, 1/9, 17/63, 17/63}

**Structure: 5 perfect pairs!**

By Pairing Cancellation Lemma: LB = 1/63 + 16/315 + 11/210 + 1/9 + 17/63 = 1/2 exactly.

**Margin:** c(5) - LB = 32/63 - 1/2 = 1/126 > 0. QED.

---

### Detailed Verification for wrs=40 (Minimum Margin)

**Vertex data:**
- wrs = 40, v_0 = 0, g = 21/20
- Ranks: (0, 3, 2, 1, 5, 4)
- Shifted params: alpha = 0, beta = 63/20, gamma = 21/10, delta = 21/20, epsilon = 21/4, zeta = 21/5

**Best template:** (2, 5, 0, 4, 3, 1)
**LB:** 1279/2520
**Margin:** 1/2520

This is the tightest Z-type vertex. The margin is still positive but small (approximately 0.000397).

---

### Interior Coverage: Gap Analysis

**The Gap:** While all 31 Z-type vertices have positive margin with "copy" templates, systematic sampling reveals that some interior points have small NEGATIVE margins (~-0.0001 to -0.0006) with "copy" templates.

**Resolution Attempt:** General (2,1,1) templates with optimized (non-copy) cut positions DO achieve LB <= c(5) at these interior points. For example:

**Uncovered point (by copy templates):**
- Params: (1.0293, 0.0101, 4.0870, 2.0485, 5.1062, 3.0678)
- Best copy template LB: 0.50801660 (margin: -0.00008)

**With general (2,1,1) optimization:**
- Optimal config: H=5, D=4, C=3, cuts at (0.032211, 0.153257, 0.048259)
- Best LB: 0.50007246 (margin: +0.00786)

The general (2,1,1) strategy covers this point with positive margin.

---

### What Remains for Complete Proof

**Option A (LP Feasibility):** Formulate the LP:
"Find x in Tier 3 region such that LB(x, T) > c(5) for ALL feasible (2,1,1) templates T."

This requires showing that for every x, there exists cut positions c_1, c_2, c_3 (and choice of H, D, C) such that LB <= c(5). The LP would verify infeasibility of the "uncovered" system.

**Challenge:** The space of (H, D, C) choices is finite (60), but the cut positions form a continuous 3-dimensional space per choice, making direct LP intractable.

**Option B (Convexity + Compactness):** Since LB(x, T) is convex in x for each T, and the Tier 3 region is compact, we could try to show:
1. At each Z-type vertex v, some T_v achieves LB(v, T_v) < c(5) with positive margin m_v.
2. The coverage set C_{T_v} is convex and contains v with margin m_v.
3. By compactness and positive margins, the union of C_{T_v} covers a neighborhood of the Z-type boundary.
4. Combined with Tier 2 at the g=1 boundary, this would cover the full Tier 3 region.

**Challenge:** Step 4 requires showing that the convex neighborhoods sufficiently overlap to cover the interior. The minimum margin (1/2520) is small, and the Lipschitz constant / polytope diameter ratio is needed.

**Option C (Discretize to Finite Templates):** Identify a FINITE set of templates such that their union covers Tier 3. The "copy" templates plus a small number of additional templates with specific non-copy cut positions.

---

## Full proof
(Status is `partial` - the Z-type vertex verification is complete, but interior coverage via LP is not yet rigorous.)

**What is proved:**
1. **LB Convexity Lemma:** For each fixed (2,1,1) template T, LB(x,T) is convex in x.
2. **31 Z-Type Vertex Coverage:** All 31 Z-type vertices satisfy LB(v, T_v) <= c(5) with positive margin (min 1/2520).
3. **Computational Evidence:** 100% coverage with general (2,1,1) strategies in sampling tests; "copy" templates cover ~94% of random interior points.

**What remains:**
- Rigorous proof that the union of coverage sets covers the ENTIRE Tier 3 interior, not just the sampled points.
- Either an LP-based certificate or an algebraic argument closing the coverage gap.

---

## Promotable lemmas

**Lemma: LB(x,T) Convexity (n=5)**
*Statement:* For n=5 and any fixed (2,1,1) template T creating 10 output pieces as linear functions of (P_1,...,P_6), the function LB(x,T) = sum of 5 largest pieces is convex in x.
*Mechanism:* LB = max over C(10,5) = 252 linear functions; max of linear = convex.
*Where proved:* This file, Key Structural Lemma.

**Lemma: 31 Z-Type Vertex Coverage (n=5)**
*Statement:* All 31 Z-type vertices (v_0=0, r_alpha=0, wrs in {35,...,41}) of the Tier 3 bounded region satisfy LB(v, T_v) <= c(5) for some "copy" (2,1,1) template T_v. Minimum margin: 1/2520.
*Where proved:* This file, Exact Rational Verification section. 31 vertices checked with exact rational arithmetic.
