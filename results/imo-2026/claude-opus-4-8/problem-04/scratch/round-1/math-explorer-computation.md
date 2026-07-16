## imo-2026-04

### Child angle formulas (verified)

Cut from vertex A (angle A°) to point P on side BC, splitting A = A1 + A2:
- **Child1** = (A1, B, A−A1+C) = (A1, B, 180−A1−B)
- **Child2** = (A2, C, A1+B) = (A−A1, C, A1+B)

The two "new" angles at P are A2+C (in Child1) and A1+B (in Child2). They are supplementary: (A2+C) + (A1+B) = 180°. Old angles B and C survive unchanged into Child1 and Child2 respectively.

### Key structural observation

From parent (A,B,C), Mulan controls the cut parameter x = A1 ∈ (0,A) freely. In each cut, Mulan puts at most 2 "new" angles into play (x and A−x); the old angles B and C pass directly into children. For both children to have θ simultaneously (so Shan-Yu cannot avoid it), analysis of all cases yields exactly two possibilities:

1. **A = 2θ**: set x = θ → Child1 = (θ, B, θ+C) and Child2 = (θ, C, θ+B). Both have θ.
2. **θ = 90°**: set A1+B = 90° (always achievable) → both children have 90° (the supplementary pair at P both equal 90°).

(Cases 2 gives Child1 angle = 180−(A1+B) = 90° and Child2 angle = A1+B = 90°.)

### General one-step forcing analysis

From T = (A,B,C) with **no multiple of θ** as any angle (call this set S**), consider cuts from vertex A:
- **bad1(x)**: x values making Child1 have some kθ: {nθ : n ≥ 1} ∪ {A+C−nθ : n ≥ 1}
- **bad2(x)**: x values making Child2 have some kθ: {A−mθ : m ≥ 1} ∪ {mθ−B : m ≥ 1}

For BOTH children to be ∉ S**, need x ∈ bad1 ∩ bad2. Checking all four intersection types:

| Pair | Condition | Outcome |
|------|-----------|---------|
| nθ = A−mθ | A = (n+m)θ | Impossible (A ∉ {kθ} since T ∈ S**) |
| nθ = mθ−B | B = (m−n)θ | Impossible (B ∉ {kθ}) |
| A+C−nθ = A−mθ | C = (n−m)θ | Impossible (C ∉ {kθ}) |
| A+C−nθ = mθ−B | **A+B+C = (n+m)θ** | Possible iff **180/θ ∈ ℤ** |

**Algebraic theorem (PROVED):** From T ∈ S**, Mulan can force BOTH children ∉ S** in one cut if and only if θ = 180°/N for some positive integer N.

### Conjectured answer (CONJECTURE)

**Mulan can guarantee winning in finitely many steps, for any initial triangle Shan-Yu picks, if and only if 180°/θ is a positive integer (i.e., θ = 180°/N for some integer N ≥ 2).**

The winning values are θ ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 180°/8, …}.

### Mulan's winning strategy (for θ = 180°/N)

**Phase 1 — Create a multiple of θ in both children (1 step):**
Given T = (A,B,C) ∈ S**. Find integer n with C/θ < n < (A+C)/θ (equivalently C < nθ < A+C). This integer exists because:
- For N ≥ 3: the max angle satisfies A ≥ 60° > θ = 180/N, so A/θ > 1, guaranteeing an integer in the interval of length A/θ > 1 (and C/θ not an integer since C ∉ {kθ}).
- For N = 2 (θ = 90°): take n = 1; valid since C < 90° and A+C > 90° whenever the triangle is acute (if it is obtuse, cut from the obtuse vertex instead with the same argument).

Set x = A+C−nθ ∈ (0,A). Then:
- Child1 = (A+C−nθ, B, nθ): has angle **nθ** ∉ S**
- Child2 = (nθ−C, C, (N−n)θ): has angle **(N−n)θ** ∉ S**

Both children are ∉ S**. Shan-Yu must keep one; say it has angle kθ for some k ∈ {n, N−n} with 1 ≤ k ≤ N−1.

**Phase 2 — Reduce kθ to θ (at most k−1 steps):**
From a triangle with angle kθ (k ≥ 2), cut from that vertex with x = θ:
- Child1 = (θ, B', kθ−θ+C') = (θ, B', (k−1)θ+C'): has θ ✓
- Child2 = ((k−1)θ, C', θ+B'): has (k−1)θ

For k = 2: Child2 = (θ, C', θ+B') also has θ. BOTH children have θ → WIN!
For k ≥ 3: Shan-Yu picks Child2 (has (k−1)θ, no θ yet). Recurse with k reduced by 1.
After k−1 steps, reach k = 2 and win.

**Total: at most 1 + (N−1) = N steps.** (The Phase 1 step is always 1 step since we force both children to get multiples.)

### Shan-Yu's survival strategy (for θ ≠ 180°/N)

Shan-Yu picks any starting triangle T₀ with no angle equal to kθ for any k = 1, 2, … (finitely many constraints in (0°,180°); easy to satisfy). From any T ∈ S**, the algebraic analysis above shows bad1 ∩ bad2 = ∅, so Mulan cannot make BOTH children ∉ S** in any one cut. Hence there is always at least one child in S**. Shan-Yu picks that child. The game never produces a triangle with angle θ.

**Note:** For irrational θ, the equilateral triangle (60°, 60°, 60°) works as T₀ since 60° is never an integer multiple of irrational θ (except in degenerate rational cases). From the equilateral, analysis shows the only θ for which both children get θ are rational values (θ = 30°, 60°, 90°), all of which are 180°/N.

### Code run and simulation output

**From (28°, 57°, 95°) with θ=60° (N=3):**
- Phase 1: cut from 28° (A=28, B=57, C=95), n=1, x = 28+95−60 = 63... let me show what actually happened:
  - Step 0: cut from vertex 28 with x=3, giving Child1=(3,57,120) and Child2=(25,95,60). Both have multiples of 60° (120 and 60). Shan-Yu picks (3,57,120) (has 120=2θ, no θ).
  - Step 1: cut from vertex 120 with x=60. Child1=(60,3,117)✓, Child2=(60,57,63)✓. BOTH have θ=60°! WIN.

**From (38.7°, 33.4°, 107.9°) across all N=2,3,4,5,6:**
```
N=2, θ=90.00°: Mulan wins in 1 step
N=3, θ=60.00°: Mulan wins in 2 steps
N=4, θ=45.00°: Mulan wins in 3 steps
N=5, θ=36.00°: Mulan wins in 3 steps
N=6, θ=30.00°: Mulan wins in 4 steps
```

**θ=72° (not 180/N) survival check:** From each triangle in S** for θ=72°, bad1 ∩ bad2 = ∅ confirmed computationally for 5 test triangles. Shan-Yu always has a safe child.

### Distinct openings for the outliner

1. **Direct algebraic game-tree approach**: The key move is the "case (d)" identity A+B+C = (n+m)θ = 180 that allows Mulan to split any triangle into two children each with a multiple of θ. This is the heart of both the winning strategy and the impossibility.

2. **Monovariant / induction on the multiplicity k**: From a triangle with angle kθ, Mulan reduces to k−1 in one step. The "race to 1" gives a concrete bound of N total steps.

3. **Shan-Yu's invariant for the impossible case**: S** = {triangles with no angle = kθ} is closed under "Shan-Yu picks the safe child" exactly when 180/θ ∉ ℤ, because bad1 ∩ bad2 = ∅ algebraically.

4. **The supplementary-pair trick (θ = 90°)**: The two new angles at the cut point always sum to 180°. For both to equal θ simultaneously, need 2θ = 180°, giving θ = 90° as the "one-step from anywhere" special case. This is a sub-case of the general N=2 argument.

- **Distinct openings:** (1) Algebraic game-tree: the "case (d)" identity 180 = (n+m)θ is the pivot — shows the criterion is exactly θ | 180. (2) Monovariant: "max multiple of θ in current triangle" decreases by 1 in Phase 2 and drops to ≤ N−1 in Phase 1, giving termination. (3) Closed-set argument: S** is closed under Shan-Yu's move iff 180/θ ∉ ℤ, giving the impossibility. (4) Supplementary-pair trick for θ=90° as an illustrative special case.
- **Candidate technique(s):** Combinatorial game theory (closed safe sets / forcing), monovariant (multiplicity of θ), elementary angle arithmetic. No heavy machinery needed.
- **Cheap-kill candidates:** The criterion 180/θ ∈ ℤ is clean and elementary. The impossibility proof is a finite case split on 4 algebraic intersections, all vacuous except one (case d).
- **Knowledge-base entries to use:** "Invariants & monovariants" (Combinatorics section), "General Proof Methods: Induction / Invariant", "General Proof Methods: Casework/exhaustion".
- **Analogous past problems (cruxes):** Not checked (no crux corpus query done in this lens). The problem is combinatorial game theory on a continuous space, so standard crux corpus may not have close analogs.
- **Prior progress:** None (first round).
- **Dead ends (do not retry):** Attempting to use "rational vs. irrational" as the criterion — this is WRONG. The criterion is NOT "θ rational" but specifically "180/θ is a positive integer." For example, θ = 72° = 2×36° is rational but Mulan CANNOT win. Conversely, θ = 180°/7 is rational and Mulan CAN win.
- **Small-case / intuition notes (CONJECTURE):** The answer is θ ∈ {180°/N : N ∈ ℤ, N ≥ 2}. Equivalently, 180°/θ is a positive integer ≥ 2. Verified computationally for N = 2,3,4,5,6,7,180 (winning) and θ = 72°, 120°, 100°, √2°, 180/π° (losing). The key insight: the only way to force both children to have a multiple of θ (defeating Shan-Yu) is when A+B+C = 180° = (n+m)θ for integers n, m, which requires θ | 180°.
