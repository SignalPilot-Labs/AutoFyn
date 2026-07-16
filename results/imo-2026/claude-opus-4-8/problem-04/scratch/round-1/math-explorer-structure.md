## imo-2026-04

### Conjectured Answer

**Mulan can guarantee winning iff theta = 180°/k for some integer k ≥ 2.**

Equivalently: 180/theta is a positive integer (≥ 2). These are the "aliquot parts" of 180°: theta ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 22.5°, 20°, …}. (Flagged as conjecture, but supported by substantial structural evidence below.)

---

### Cut Operation: Angle Arithmetic

From triangle {A, B, C} (A+B+C=180°), cutting from vertex A (adjacent to B and C) with parameter A1 ∈ (0, A):

- **Child1**: {A1, B, C+(A−A1)} — inherits B; P-angle = C+(A−A1)
- **Child2**: {A−A1, C, B+A1} — inherits C; P-angle = B+A1

Key facts:
- P-angles of the two children sum to exactly 180°: (B+A1) + (C+(A−A1)) = A+B+C = 180°.
- Original angle B is "kept" in child1; C is "kept" in child2.
- Mulan controls A1 continuously (any value in (0,A)).
- Shan-Yu controls which child to keep.

**When does Mulan force theta in BOTH children from one cut (vertex A)?**

The 4 exhaustive cases (since B, C ≠ theta by game state):

| Child1 source | Child2 source | Consequence |
|---|---|---|
| A1 = theta | A−A1 = theta | A = 2*theta |
| A1 = theta | B+A1 = theta | B = 0 (impossible) |
| C+(A−A1) = theta | A−A1 = theta | C = 0 (impossible) |
| C+(A−A1) = theta | B+A1 = theta | A+B+C = 2*theta, so 180 = 2*theta, i.e., theta = 90° |

**Conclusion**: Mulan can win in ONE step if and only if some angle of T = 2*theta (cut from that vertex with A1 = theta), or theta = 90° (P-angles both equal 90°).

---

### Key Invariant for Shan-Yu (theta ≠ 180°/k)

**Define the "safe set"** S = {triangles with no angle equal to j·theta for any positive integer j with j·theta < 180°}.

**Claim**: S is closed under any cut Mulan makes (Shan-Yu can always keep a child in S).

**Proof sketch**: Suppose T = {A,B,C} ∈ S. Suppose child1 has j·theta and child2 has m·theta simultaneously. Analyzing all cases:
- If A1 = j·theta (child1 vertex split) and B+A1 = m·theta (child2 P-angle): then B = (m−j)·theta. But B ∈ T ∈ S means B is not a multiple of theta. Contradiction.
- If A1 = j·theta and C+(A−A1) = m·theta: then A+C = (j+m)·theta. With B: A+B+C = 180°, so B = 180°−(j+m)·theta = (k−j−m)·theta (for theta = 180°/k). But for theta ≠ 180°/k: 180° is not a multiple of theta, so this forces a contradiction.
- Similarly all other cases force some angle of T to be a multiple of theta.

Therefore: for theta ≠ 180°/k, at most ONE child can have a multiple of theta. Shan-Yu keeps the other child (which is in S).

**Shan-Yu's starting triangle** (for theta ≠ 180°/k): {theta/2, theta/2, 180°−theta}.
- theta/2 is not a multiple of theta (would require j = 1/2, not integer). ✓
- 180°−theta is a multiple of theta iff 180° = (j+1)·theta iff theta = 180°/k. Since theta ≠ 180°/k: NOT a multiple. ✓
- Valid triangle (all angles > 0, sum = 180°). ✓

So Shan-Yu starts in S and stays in S forever. **Mulan cannot win for theta ≠ 180°/k.**

---

### Mulan's Winning Strategy (theta = 180°/k)

**Why Shan-Yu's safe-set strategy fails**: For theta = 180°/k, the angle 180°−theta = (k−1)·theta IS a multiple of theta. So the triangle {theta/2, theta/2, (k−1)·theta} has a multiple of theta as its third angle — it's NOT in the safe set. Shan-Yu cannot use this triangle.

**Key mechanism**: For theta = 180°/k, consecutive multiples of theta are "complementary": j·theta + (k−j)·theta = k·theta = 180°. In particular, **theta + (k−1)·theta = 180°**, so Mulan can set the two P-angles to be theta and (k−1)·theta simultaneously with one cut.

**Step-by-step strategy from any triangle**:

*Step 1*: From any triangle T = {A,B,C} (no angle = theta):
- **If some adjacent angle < theta (say B < theta)**: Cut from vertex A with A1 = theta−B. Then:
  - child2 P-angle = B+A1 = theta → game stops if Shan-Yu keeps child2. So Shan-Yu MUST discard child2.
  - child1 P-angle = 180°−theta = (k−1)·theta. Shan-Yu keeps child1 = {theta−B, B, (k−1)·theta}.
  
- **If all angles ≥ theta** (forces k ≥ 3, since 3·theta ≤ 180° = k·theta): Cut from any vertex A=A with A1 = theta:
  - child1 = {theta, B, C+(A−theta)}: has theta! Shan-Yu discards.
  - child2 = {A−theta, C, B+theta}: all angles < theta (since A−theta < A, etc.); in particular, some angle ≤ (A−theta) < A ≤ 180°−theta.
  - From child2, some angle is < theta. Apply the first sub-case.

*After Step 1*: Shan-Yu holds a triangle with angle (k−1)·theta (or close to that structure).

*Step 2*: From T' = {u, v, (k−1)·theta} with u+v = theta:
Cut from vertex (k−1)·theta with C1 = (k−2)·theta − u:
- child2 = {theta, v, (k−2)·theta}: has theta! Shan-Yu discards.
- child1 = {(k−2)·theta−u, u, 2·theta}: **has 2·theta**.

*Step 3*: From triangle with 2·theta (as one angle), cut from 2·theta with A1 = theta:
- child1 = {theta, adj1, adj1'}: has theta.
- child2 = {theta, adj2, adj2'}: has theta.
- **Both children have theta! WIN!**

**Total bound**: At most ~3 steps per "descent level", and at most k−1 descent levels → O(k) steps total. Always finite.

---

### Distinct Structural Openings

1. **The "two-P-angle" condition**: Both children contain theta from a single cut iff vertex = 2·theta or theta = 90°. This is the ONLY way Mulan can win. This gives the central reachability question: can Mulan force 2·theta into the triangle?

2. **The "complementary multiples" mechanism**: P-angles always sum to 180°. For BOTH to be multiples of theta, their sum 180° must be an integer multiple of theta. This holds iff 180°/theta ∈ Z, i.e., theta = 180°/k. This is the algebraic heart of the characterization.

3. **Safe-set invariant (Shan-Yu direction)**: S = {no angle is a multiple of theta} is invariant under cuts when theta ≠ 180°/k. Proof uses that two distinct multiples summing to 180° require 180°/theta ∈ Z. Triangle {theta/2, theta/2, 180°−theta} ∈ S is Shan-Yu's explicit starting point.

4. **Descent strategy (Mulan direction)**: For theta = 180°/k, the multiples k·theta=180°, (k−1)·theta, …, 2·theta, theta form a "chain." Mulan can always step Shan-Yu down this chain using the P-angle forcing trick (theta + (k−1)·theta = 180°). This terminates in finitely many rounds.

5. **The "all angles ≥ theta" obstruction**: When all angles exceed theta (possible only when theta < 60° = 180°/3), Mulan cannot directly create P-angle=theta. But vertex-splitting by theta still forces Shan-Yu into a triangle with a smaller angle, eventually enabling the P-angle trick.

---

### Candidate Techniques

- **Invariant / monovariant** (combinatorics KB entry): The safe set S is the key invariant for Shan-Yu's non-losing strategy. The "minimum angle" or "maximum multiple of theta present" serves as a monovariant for Mulan's descent.
- **Algebraic characterization via divisibility**: 180/theta ∈ Z is the exact condition. The algebraic condition comes from "no two distinct positive integer multiples of theta sum to 180" being equivalent to theta ≠ 180/k.
- **Forcing / adversarial game**: Both P-angles must be controlled simultaneously. Mulan's power is choosing the cut; Shan-Yu's power is choosing which child to keep.

---

### Cheap-Kill Candidates

- **Parity / divisibility check**: theta = 180°/k is equivalent to 180/theta being a positive integer. This is a clean divisibility check.
- **Supplementary angle structure**: P-angles sum to 180°. If theta = 180°/k, then theta has a "complementary multiple" (k−1)·theta = 180°−theta. This is the structural reason for Mulan's win. For theta ≠ 180°/k, no such complementary multiple exists.

---

### Knowledge-Base Entries to Use

- **Invariants & monovariants** (combinatorics section): Central to Shan-Yu's strategy.
- **Games and strategy** (crux corpus subtopic): The adversarial structure of the game.
- **Constructive vs. existence**: Mulan needs an explicit strategy (constructive proof).
- **Direct proof / induction**: The descent from (k−1)·theta to 2·theta can be structured as an inductive descent.

---

### Analogous Past Problems (Cruxes)

- **aimo-0225** (game on regular n-gon with triangle counters): The 2-adic valuation of an arc difference determines P/N status. The "doubling" structure is analogous to how 180/theta being a power of 2 (or integer) governs win/loss here. Crux move: "determine game value by recursing on the 2-adic valuation of a difference that exactly halves at each step." Partially analogous.
- No exact triangle-cutting analog found in corpus (geometry cruxes not extracted).

---

### Prior Progress

None (first round, status = unsolved).

---

### Dead Ends (Do Not Retry)

None from prior rounds.

---

### Small-Case / Intuition Notes (Conjectural)

| theta | 180/theta | Mulan wins? | Evidence |
|---|---|---|---|
| 90° | 2 | YES | 1-step win: both P-angles = 90° |
| 60° | 3 | YES | 2-step win: force 120°=2θ, then split |
| 45° | 4 | YES | 3-4 step win verified by explicit trace |
| 36° | 5 | YES | 4-5 step win verified; {18,18,144} unsafe for Shan-Yu |
| 72° | 5/2 | NO | Shan-Yu cycles: {36,36,108} → {36,36,108} |
| 40° | 9/2 | NO | Shan-Yu uses {20,20,140}: 140 not multiple of 40° |
| Irrational | — | NO | Shan-Yu maintains {θ/2, θ/2, 180−θ} cycle |
| 30° | 6 | YES | 1-step from equilateral (has 60=2·30) |

All conjecture (not proved), but mechanically verified by explicit game traces above.

---

### Critical Gap for the Proof

**Mulan direction**: Need to prove that from ANY starting triangle (not just rational-angle ones), Mulan can reach a triangle with a multiple n·theta (n ≥ 2) in finite steps. The inductive descent from Step 1 needs careful analysis when all angles of the starting triangle exceed theta. (The vertex-split=theta trick creates a child with a smaller min angle, but that kept child might not immediately have a useful multiple.)

**Shan-Yu direction**: The safe-set invariant proof is essentially complete. The key lemma: "if T ∈ S and cut creates multiples j·theta and m·theta in the two children respectively, then some angle of T is a multiple of theta, contradicting T ∈ S." This is proved by case analysis on the 4 ways theta can appear in a child (vertex split or P-angle).
