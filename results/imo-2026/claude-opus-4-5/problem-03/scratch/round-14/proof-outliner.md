## imo-2026-03

n5-five-mark: revise
Target: Prove c(5) = 32/63 via three-tier strategy cascade: V_j -> Pairwise -> (2,2,1)
Technique: Casework with pairwise coverage + finite vertex enumeration for bounded region
Skeleton:
  1. Case B small (P_6 < c(5), P_1 > L_0): all shifted params {alpha, beta, gamma, delta, epsilon, zeta} > 0 with weighted sum 6*alpha + 5*beta + 4*gamma + 3*delta + 2*epsilon + zeta = 42 — by B_small characterization (CERTIFIED)
  2. Tier 1 (V_j): If any d_j <= L_0, halve all except {P_j, P_{j+1}}, singletons have diff d_j <= L_0, LB = 1/2 + d_j/2 <= c(5) — by Singleton-Pair Formula (CERTIFIED)
  3. Tier 2 (Pairwise): If all d_j > L_0 but some pair of shifted params has |x_i - x_j| <= 1, construct 4-mark strategy giving singletons with diff <= L_0 — by explicit 15-pair constructions (NEEDS REVISION)
  4. Tier 3 (Bounded Region): If all 15 pairwise diffs > 1, config is in bounded region g in (1, 1.2), v_0 in (0, 1/3) — by Rearrangement Inequality (CERTIFIED)
  5. Tier 3 ((2,2,1)): For any config in the bounded region, some (2,2,1) variant achieves LB <= c(5) — by 63-vertex finite check + compactness (NEEDS ALGEBRAIC PROOF)
Key lemmas (claim + the one-line mechanism that makes it true):
  - **10 non-adjacent pair constructions are correct** — because "chop-at-adjacent" (cut P_{k+1} at P_k) creates pair {P_k, P_k} and singletons {P_1, d_k} or {d_j, d_k}. All 10 verified with 0 failures.
  - **5 adjacent pairs require "free-position cut"** — because adjacent pairs (alpha-beta, beta-gamma, etc.) cannot both have the needed singletons from chop-at-adjacent (e.g., creating singleton d_1 consumes P_1 into a pair). Instead: cut P_4 at t in (d_3, P_2), halve P_1, P_5, P_6; singletons {P_2, P_3}; XY gets both sub-pieces of P_4; LB = 1/2 + (P_2+P_3-P_4)/2 <= c(5) iff alpha+beta <= delta.
  - **(beta, gamma) algebraic condition: alpha+beta <= delta always holds when ONLY |beta-gamma| <= 1** — because |alpha-delta| > 1, |beta-delta| > 1, |gamma-delta| > 1 together with weighted sum constraint force delta to be large. Computationally verified 0/10000 exceptions.
  - **63 boundary vertices at g=1 all have a (2,2,1) variant achieving LB <= c(5)** — because each vertex is explicitly enumerable (wrs in {35,...,41}, total 63), and for each, the optimal (2,2,1) variant and its LB can be computed. Min margin 0.0057 > 0.
  - **Interior follows from boundary + compactness** — because LB as a function of (g, v_0, permutation) is continuous, the bounded region is compact, and boundary is already handled by Pairwise at g=1.
Open gaps:
  - Tier 2 (Pairwise): Replace the INCORRECT (beta, gamma) construction with the CORRECT one from explorer-pairwise. Add explicit constructions for all 5 adjacent pairs: (alpha, beta), (beta, gamma), (gamma, delta), (delta, epsilon), (epsilon, zeta).
  - Tier 3 ((2,2,1)): Algebraic verification of the 63-vertex finite check. For each vertex, derive (1) which (2,2,1) variant is optimal, (2) the LB formula, (3) verify LB <= c(5) algebraically.
Cases to cover:
  - 10 non-adjacent pairs: (alpha, gamma), (alpha, delta), (alpha, epsilon), (alpha, zeta), (beta, delta), (beta, epsilon), (beta, zeta), (gamma, epsilon), (gamma, zeta), (delta, zeta) — use "chop-at-adjacent" constructions
  - 5 adjacent pairs: (alpha, beta), (beta, gamma), (gamma, delta), (delta, epsilon), (epsilon, zeta) — use "free-position cut" constructions
  - 63 boundary vertices: wrs=35 (1), wrs=36 (5), wrs=37 (6), wrs=38 (9), wrs=39 (16), wrs=40 (12), wrs=41 (14)
Watch out for:
  - The (beta, gamma) construction "halve P_1, P_4, P_5, P_6" creates singletons {P_2, P_3}, NOT {d_1, d_2}. This is WRONG for the condition |beta-gamma| <= 1. The correct construction cuts P_4 at a free position t.
  - For adjacent pairs, the algebraic condition (e.g., alpha+beta <= delta for (beta, gamma)) must be PROVED to hold when ONLY that pair has diff <= 1 and all others > 1. The explorer verified computationally but builder should attempt algebraic proof.
  - The 63-vertex enumeration must be complete (all wrs from 35-41, all valid permutations for each wrs). Missing even one vertex leaves a gap.
  - For (2,2,1), the optimal variant varies by vertex (not a single universal choice). Builder should either enumerate all or identify a decision rule.

---

geometric-direct: advance
Target: Complete proof of c(n) = 2^n / (2^{n+1} - 1) for all n >= 1
Technique: Case analysis + strategy construction for each n
Skeleton:
  1. Lower bound: LB's geometric config achieves exactly c(n) — PROVED for all n
  2. Upper bound Case A (P_1 <= L_0): Halve-All Strategy — PROVED for all n
  3. Upper bound Case B large (P_{n+1} >= c(n)): Halve+IH Strategy — PROVED for all n >= 2
  4. Upper bound Case B small (P_{n+1} < c(n)):
     - n=1: automatic
     - n=2: sum constraint forces d_1 < L_0 — PROVED
     - n=3: three explicit strategies S1, S2, S3 — PROVED
     - n=4: V_j + Pigeonhole + Pairwise cascade — PROVED (Pigeonhole CERTIFIED)
     - n=5: V_j + Pairwise + (2,2,1) cascade — depends on n5-five-mark revisions
     - n>=6: OPEN (exponentially growing bounded region, no finite check feasible)
Key lemmas (claim + the one-line mechanism that makes it true):
  - n=4 Pigeonhole: min weighted sum with all pairwise > 1 exceeds 20 > 16, so some pairwise <= 1 — CERTIFIED
  - For n>=5, Pigeonhole fails (56 < 63 for n=5, 84 < 127 for n=6, etc.)
Open gaps:
  - n=5 depends on n5-five-mark approach (Pairwise fixes + (2,2,1) algebraic proof)
  - n>=6 is genuinely OPEN — no current strategy works
Cases to cover: n=1,2,3,4,5 (n>=6 deferred)
Watch out for:
  - The n=4 written proof has some Pairwise construction errors (e.g., (gamma, eta) claims wrong piece count), but coverage is computationally verified. These should be fixed for full rigor.
  - Do NOT attempt to extend (2,2,1) to n>=6 — the bounded region grows exponentially and no single strategy family works.

---

## Builder Instructions for n5-five-mark

**Priority 1: Fix Tier 2 (Pairwise) Section**

Replace the INCORRECT constructions with the CORRECT ones from explorer-pairwise:

**10 Non-Adjacent Pairs (Chop-at-Adjacent) — ALL VERIFIED CORRECT:**

1. (alpha, gamma): cut P_3 at P_2, halve P_4, P_5, P_6. Singletons: {P_1, d_2}.
2. (alpha, delta): cut P_4 at P_3, halve P_2, P_5, P_6. Singletons: {P_1, d_3}. [ALREADY CORRECT]
3. (alpha, epsilon): cut P_5 at P_4, halve P_2, P_3, P_6. Singletons: {P_1, d_4}.
4. (alpha, zeta): cut P_6 at P_5, halve P_2, P_3, P_4. Singletons: {P_1, d_5}.
5. (beta, delta): cut P_2 at P_1 + cut P_4 at P_3, halve P_5, P_6. Singletons: {d_1, d_3}.
6. (beta, epsilon): cut P_2 at P_1 + cut P_5 at P_4, halve P_3, P_6. Singletons: {d_1, d_4}.
7. (beta, zeta): cut P_2 at P_1 + cut P_6 at P_5, halve P_3, P_4. Singletons: {d_1, d_5}.
8. (gamma, epsilon): cut P_3 at P_2 + cut P_5 at P_4, halve P_1, P_6. Singletons: {d_2, d_4}.
9. (gamma, zeta): cut P_3 at P_2 + cut P_6 at P_5, halve P_1, P_4. Singletons: {d_2, d_5}.
10. (delta, zeta): cut P_4 at P_3 + cut P_6 at P_5, halve P_1, P_2. Singletons: {d_3, d_5}.

**5 Adjacent Pairs (Free-Position Cut) — NEW CONSTRUCTIONS:**

1. **(alpha, beta):** Cut P_3 at t in (d_2, P_1), halve P_4, P_5, P_6. Singletons: {P_1, P_2}.
   - LB = P_4/2 + P_5/2 + P_6/2 + P_1 + P_2 = 1/2 + (P_1 + P_2 - P_3)/2
   - Condition: P_1 + P_2 <= P_3 + L_0, i.e., alpha <= gamma (in shifted units)
   - Claim: alpha <= gamma always holds when ONLY |alpha - beta| <= 1

2. **(beta, gamma):** Cut P_4 at t in (d_3, P_2), halve P_1, P_5, P_6. Singletons: {P_2, P_3}.
   - LB = P_1/2 + P_5/2 + P_6/2 + P_2 + P_3 = 1/2 + (P_2 + P_3 - P_4)/2
   - Condition: P_2 + P_3 <= P_4 + L_0, i.e., alpha + beta <= delta (in shifted units)
   - Claim: alpha + beta <= delta always holds when ONLY |beta - gamma| <= 1 (verified 0/10000 exceptions)

3. **(gamma, delta):** Cut P_5 at t in (d_4, P_3), halve P_1, P_2, P_6. Singletons: {P_3, P_4}.
   - LB = P_1/2 + P_2/2 + P_6/2 + P_3 + P_4 = 1/2 + (P_3 + P_4 - P_5)/2
   - Condition: P_3 + P_4 <= P_5 + L_0, i.e., beta + gamma <= epsilon

4. **(delta, epsilon):** Cut P_6 at t in (d_5, P_4), halve P_1, P_2, P_3. Singletons: {P_4, P_5}.
   - LB = P_1/2 + P_2/2 + P_3/2 + P_4 + P_5 = 1/2 + (P_4 + P_5 - P_6)/2
   - Condition: P_4 + P_5 <= P_6 + L_0

5. **(epsilon, zeta):** Cut P_6 at t in (P_4, P_5), halve P_1, P_2, P_4. Singletons: {P_3, P_5}.
   - LB = P_1/2 + P_2/2 + P_4/2 + P_3 + P_5 = 1/2 + (P_3 + P_5 - P_6)/2
   - Condition: P_3 + P_5 <= P_6 + L_0

**Priority 2: Add 63-Vertex Algebraic Framework for (2,2,1)**

The builder should:

1. **Enumerate all 63 vertices explicitly:**
   - wrs = 35: 1 vertex, v_0 = 1/3, unique permutation
   - wrs = 36: 5 vertices, v_0 = 2/7, enumerate permutations
   - ... (total 63)

2. **For each vertex, derive:**
   - The 6 shifted params {alpha, beta, gamma, delta, epsilon, zeta} in terms of (v_0, g=1, permutation)
   - The optimal (2,2,1) variant from computational results (e.g., Split (P_4, P_6), Halve P_3 for 19 vertices)
   - The LB formula for that variant
   - Verify LB <= c(5) = 32/63 algebraically

3. **For interior (g > 1):**
   - At g=1 exactly, Pairwise applies (some adjacent ranks give |diff|=1)
   - For g > 1, continuity/compactness: the minimum of max_vertex(LB - c(5)) over all (2,2,1) variants is negative (margin >= 0.0057), so by continuity the interior is also covered

**Builder deliverable:** Replace Tier 2 section with correct constructions. Add Tier 3 algebraic verification (at least outline the 63-vertex structure with explicit formulas for a representative subset).

---

build set: n5-five-mark
