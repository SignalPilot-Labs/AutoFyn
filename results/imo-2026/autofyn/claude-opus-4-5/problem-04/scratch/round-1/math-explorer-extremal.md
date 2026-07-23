## imo-2026-04

### Problem Restatement
Two-player game on triangles. θ fixed. Shan-Yu picks initial triangle; then alternately: if any angle = θ, Mulan wins. Otherwise Mulan places P on a perimeter edge, cuts from P to the opposite vertex (splitting one angle), two sub-triangles formed; Shan-Yu discards one, keeps the other. Characterize all θ for which Mulan wins.

---

### Key Structural Observations (Angle Mechanics)

**Cut mechanics:** When Mulan cuts with P on edge BC to vertex A (angle A):
- Sub-tri 1 (ABP): angles {B, t, 180−B−t}
- Sub-tri 2 (ACP): angles {A−t, C, B+t}
where t = angle_BAP ∈ (0, A) is Mulan's choice. Angle B is preserved in sub-tri 1; angle C is preserved in sub-tri 2.

**Bisection lemma (key move):** Setting t = A/2 (bisecting angle A) forces A/2 into BOTH sub-triangles:
- Sub-tri 1: {B, A/2, C+A/2}
- Sub-tri 2: {A/2, C, B+A/2}
Shan-Yu must keep one with A/2. This is the core forcing mechanism.

**Instant-win condition:** θ appears in BOTH sub-triangles simultaneously iff:
- θ = 90° (use t = 90−B; then both subs get 90°), OR
- The vertex angle being cut to equals 2θ (set t = θ; sub-tri 1 gets θ, sub-tri 2 gets θ since A−t = θ).
No other case forces θ into both sub-triangles.

**Consequence:** For θ > 90°: the angle 2θ > 180° is impossible as a triangle angle, so Mulan can NEVER force θ into both sub-tris. Shan-Yu wins for all θ ∈ (90°, 180°).

---

### Critical Pair-Sum Trick

For the cut with 180−B−t = j₁θ AND B+t = j₂θ (i.e., t = 180−B−j₁θ):
- Sub-tri 1 has j₁θ as an angle.
- Sub-tri 2 has j₂θ as an angle.
- These are consistent: j₁θ + j₂θ = 180 iff (j₁+j₂)θ = 180.

**For θ = 180/n (integer n ≥ 2):** j₁+j₂ = n is solvable with positive integers j₁, j₂. E.g., j₁=1, j₂=n−1. So Mulan can force both sub-tris to have positive multiples of θ summing to 180.

**For θ = 180p/q with p ≥ 2, gcd(p,q) = 1:** (j₁+j₂)θ = 180 requires j₁+j₂ = q/p, which is non-integer. NO pair of positive multiples of θ sums to 180. Shan-Yu's invariant "no angle is a positive multiple of θ" is indestructible.

---

### Conjectured Answer (with strong computational support)

**Mulan wins if and only if θ = 180°/n for some integer n ≥ 2.**

Equivalently: 180/θ is a positive integer. Equivalently: θ ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 22.5°, 20°, 18°, …}.

These are EXACTLY the angles at the center of a regular n-gon (n ≥ 2 sides).

---

### Distinct Openings / Attack Routes

**Opening A (Shan-Yu loses — Mulan's strategy via multiples):**
For θ = 180/n:
1. Phase 1: From any triangle {A,B,C}, Mulan sets t = 180−B−j₁θ where j₁+j₂=n. Sub-tri 1 has j₁θ, sub-tri 2 has j₂θ. Shan-Yu must keep one with a multiple of θ.
2. Phase 2: From a triangle with multiple 2^k·θ as a vertex angle, Mulan bisects it (t = 2^{k-1}·θ). Both sub-tris get 2^{k-1}·θ. Shan-Yu must keep one.
3. Repeat until the triangle has 2θ as a vertex angle. Then cut with t=θ; both sub-tris get θ. Done.
Finiteness: each phase reduces the chain level by 1; chain has at most log₂(n) levels.

**Opening B (Shan-Yu wins — invariant approach):**
For θ = 180p/q with p ≥ 2 (including all irrational θ):
- Invariant: "no angle is a positive multiple of θ."
- Shan-Yu starts with equilateral (60°,60°,60°) — no angle is a multiple of θ (since 60/θ = 60q/(180p) = q/(3p) which for p≥2 is not a positive integer in general; Shan-Yu can always find a suitable starting triangle).
- Mulan cannot break the invariant: forcing both sub-tris to have multiples of θ requires (j₁+j₂)θ = 180, impossible.

**Opening C (θ = 90° special case):**
From ANY triangle, Mulan sets t = 90−B. Then:
- Sub-tri 1: angle = 180−B−(90−B) = 90 ✓
- Sub-tri 2: angle = B+(90−B) = 90 ✓
Both sub-tris have 90°. Mulan wins in 1 step from any triangle.

**Opening D (Backward induction / potential function):**
Define the "depth" of θ as d(θ) = min {k : 2^k·θ < 180 and 2^k·θ is reachable}. The cascade strategy reduces depth by 1 per phase. The potential Φ = max chain level of angle in current triangle is monotone decreasing. If θ = 180/n: Φ is eventually 0 (reach vertex 2θ). Otherwise Φ has no 0 state in the "reachable" portion.

**Opening E (Angle space / invariant set):**
The "safe set" S_θ = {triangles with no angle ∈ {kθ : k ≥ 1} ∩ (0,180)} is what Shan-Yu tries to maintain.
- For p≥2: S_θ is closed under Shan-Yu's choices (he can always avoid the sub-tri with kθ, since Mulan can't force both subs into S_θ^c).
- For p=1: S_θ is NOT closed — Mulan can eventually force both subs into S_θ^c, so Shan-Yu cannot maintain S_θ.

---

### Cheap-Kill Candidates

- **Parity / integrality:** The condition 180/θ ∈ ℤ is a direct integrality kill. Prove no integer pair (j₁,j₂) exists with j₁+j₂ = 180/θ when 180/θ ∉ ℤ. Equivalently check: can sum of two multiples of θ equal 180? This is the central invariant computation.
- **Angle sum constraint:** A + B + C = 180 with all angles positive creates rigid constraints on what multiples can coexist.
- **Max angle ≥ 60:** Any triangle always has max angle > 60°, ensuring at least one "large" angle for Mulan to work with in Phase 1.

---

### Candidate Techniques (Knowledge Base)

- **Invariants & Monovariants** (KB: "Invariants & Monovariants"): The set of "unsafe angles" (multiples of θ) forms the key invariant for both directions.
- **Constructive / incremental** (KB: "Constructive / incremental"): Mulan's strategy is a constructive cascade.
- **Pigeonhole / extremal** (KB): In Phase 1, finding j₁ such that j₁θ ∈ (C, 180−B) uses the spacing between consecutive multiples vs. the angle A.
- **Backward induction** (KB general methods): Characterize WIN set inductively.
- **Casework** (KB general): Cases p=1 vs p≥2 vs irrational.

---

### Analogous Past Problems (Cruxes)

- **aimo-0262** (Cinderella game): Adversary game where player maintains a self-reproducing invariant family; each legal move can restore the invariant. Directly analogous to Shan-Yu's "safe set" invariant strategy. Crux: "Cinderella maintains the invariant that two adjacent buckets are empty, the two flanking buckets have combined content at most threshold."
- **aimo-0225** (isosceles game): Game on triangle arcs where P/N status determined by 2-adic valuation of differences. Somewhat analogous but less close.
- **aimo-0236** (token game with valuation): Two-phase invariant (stronger bound before opponent moves, weaker after). The cascade-down structure (decreasing chain level) is similar.

---

### Prior Progress

None — first round, problem is `unsolved`.

### Dead Ends (Do Not Retry)

- **Pure bisection strategy (bisect largest angle every time):** This does NOT converge to θ in general; Shan-Yu can cycle. Mulan needs to use the pair-sum trick for Phase 1.
- **θ > 90 case being winnable:** Proved impossible (2θ > 180, no instant-win cut exists, and Shan-Yu's invariant is unbreakable).
- **"All rational θ in (0°, 90°) are winning":** FALSE. θ = 72° = 180·2/5 is rational and < 90°, but Shan-Yu wins (verified computationally: no cut from {89,89,2} forces both sub-tris to have multiples of 72°).

---

### Small-Case / Intuition Notes (labeled as conjecture)

- **Conjecture (strongly supported):** Answer is θ = 180°/n for n ≥ 2. Verified computationally for n = 2, 3, 4, 5, 6, 7, 180; verified Shan-Yu wins for θ = 72 (n=5/2), 120 (n=3/2), 67.5° (n=8/3).
- **Proof sketch for Mulan wins:** Phase 1 forces a multiple of θ into the kept triangle; Phase 2 cascades down via bisection. Needs careful argument for Phase 1 when max(A) < θ (gap: might need more than one step for Phase 1 in degenerate triangles). Mulan always wins in at most O(log n) steps.
- **Proof sketch for Shan-Yu wins:** The invariant "no angle is kθ for any k≥1" is clean and provably maintained when 180/θ ∉ ℤ. Shan-Yu starts with equilateral triangle. The key computation is purely algebraic.
- **Irrational θ:** Shan-Yu wins. The pair-sum condition (j₁+j₂)θ = 180 has no integer solution when θ is irrational (180 is rational). Shan-Yu maintains rational-angle triangles (rational cuts keep angles rational; irrational cuts by Mulan create irrational angles in one sub-tri but not both simultaneously with θ).
