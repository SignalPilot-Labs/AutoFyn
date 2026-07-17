# IMO 2026 Problem 4 — Mulan's Triangle Game

## Problem Statement

Shan-Yu and Mulan are playing a game. Let θ be an angle with 0° < θ < 180° known to both players. Initially, Shan-Yu makes a paper triangle T with measurements of his choice. Then, they repeatedly perform the following steps: If T has at least one angle measuring exactly θ, then the game stops and Mulan wins. Otherwise, Mulan chooses a point P on the perimeter of T, different from its three vertices. She then makes a straight cut from P to the opposite vertex of T, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new T.

For which real values of θ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

**Task:** compute_and_prove (characterization)  
**Domain:** combinatorics  

## Status
solved

## Approaches tried
- Unified characterization via pair-sum constraint and cascade strategy — worked

## Current best
Complete proof of the characterization: Mulan wins iff θ = 180°/n for some integer n ≥ 2.

## Full proof

**Theorem.** Mulan can guarantee victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2.

---

### Preliminaries: Cut Mechanics

**Setup.** Let triangle T have vertices A, B, C with angles α, β, γ at those vertices (α + β + γ = 180°). When Mulan places point P strictly between B and C on edge BC and cuts to vertex A, this produces:
- T₁ = triangle ABP
- T₂ = triangle ACP

Let t = ∠BAP (the portion of α going to T₁). The angles are:
- T₁: angle at A = t, angle at B = β, angle at P = 180 - t - β
- T₂: angle at A = α - t, angle at C = γ, angle at P = β + t

**Supplementary Angles Lemma.** The angles at P in T₁ and T₂ sum to 180°.

*Proof.* (180 - t - β) + (β + t) = 180°. Equivalently, ∠APB and ∠APC are supplementary since B, P, C are collinear.

---

### Part A: Necessity

**Definition.** The safe set S_θ = {triangles with no angle equal to kθ for any positive integer k}.

**Lemma A1 (Pair-Sum Constraint).** If T ∈ S_θ and both sub-triangles T₁, T₂ have angles that are positive multiples of θ, then those multiples must both be at the cut point P, giving (j₁ + j₂)θ = 180°.

*Proof.* Since T ∈ S_θ, angles β, γ, α are not multiples of θ. The angles in T₁ are β (not a multiple), t, and 180 - t - β. The angles in T₂ are γ (not a multiple), α - t, and β + t.

- If T₁'s multiple is t = jθ and T₂'s is β + t = j₂θ, then β = (j₂ - j)θ, contradicting β not being a multiple.
- If T₂'s multiple is α - t = kθ and T₁'s is 180 - t - β, then γ = (j₁ - k)θ, contradicting γ not being a multiple.

Therefore both multiples must be at P: j₁θ = 180 - t - β and j₂θ = β + t, giving (j₁ + j₂)θ = 180°.

**Lemma A2.** The equation (j₁ + j₂)θ = 180° has solutions j₁, j₂ ≥ 1 iff 180/θ is an integer ≥ 2.

**Lemma A3.** For θ with 180/θ ∉ ℤ_{≥2}, the set S_θ is non-empty (finitely many bad angles, measure-zero constraint).

**Theorem A.** If 180/θ ∉ ℤ_{≥2}, Shan-Yu wins by choosing T₀ ∈ S_θ and always keeping a sub-triangle in S_θ (which exists by Lemma A1).

---

### Part B: Sufficiency

Fix θ = 180°/n for n ≥ 2.

**Case n = 2 (θ = 90°):** For any triangle, relabel so the largest angle is at C. If C < 90° (acute), cut to any vertex A with t = 90 - β; then both angles at P equal 90°. If C ≥ 90° (obtuse/right), cut to C with t = 90 - α; valid since α < 90 and C ≥ 90.

**Case n ≥ 3:** Two phases.

**Phase 1:** If no angle equals θ (game hasn't ended), some angle exceeds θ (since 3θ ≤ 180 only for n ≤ 3, with equality only for equilateral which has angle = θ). Relabel so α > θ. Cut from P on BC to A with t = jθ - β for j in the interval (nβ/180, n(180-γ)/180). This interval has length nα/180 > 1, so integer j ∈ {1,...,n-1} exists. Then:
- Angle at P in T₁ = (n-j)θ
- Angle at P in T₂ = jθ

Both sub-triangles have multiples of θ at vertex P.

**Phase 2 (Cascade):** Starting from mθ at a vertex with m ∈ {2,...,n-1}:
- If m is even, bisect (t = (m/2)θ) to get (m/2)θ in both sub-triangles.
- If m ≥ 3 is odd, cut with t = θ. T₁ has θ at the vertex (Mulan wins), T₂ has (m-1)θ.

Since m decreases at each step, Mulan wins in O(n) moves.

---

### Conclusion

The winning values of θ are exactly θ = 180°/n for integers n ≥ 2: {90°, 60°, 45°, 36°, 30°, ...}.
