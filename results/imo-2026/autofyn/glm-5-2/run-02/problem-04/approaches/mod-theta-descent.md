# mod-theta-descent — direct mod-θ lattice + k-descent (the workhorse)

## Status
solved

## Approaches tried
- mod-θ lattice / descent monovariant (this file) — both directions now written in full rigorous prose: validity-inequality lemma unified as one casework (N≥3 vs N=2), k-descent with strict monovariant and move bound, four-case mod-θ obstruction with exhaustive disjoint case check, initial-triangle existence as a finite-union-of-lines argument (no Kronecker density invoked). Numerically re-verified: create-move+descent for N∈{2,3,4,5,7,8,11,13,17,19,23,99} (all hit the bound ≤ N−1); obstruction 0 escapes in 3000 random trials each for θ∈{72,100,50,7,13,40,135,36.5,60.0001,17.5,170}. (keep prior entries)

## Current best
Complete characterization: **Mulan guarantees victory in finitely many steps iff θ = 180°/N for some integer N ≥ 2.** Both directions proved below; no gaps.

## Full proof

### Problem statement (recap)

Let θ be a fixed angle with 0° < θ < 180°, known to both players. Shan-Yu picks the initial paper triangle T. Thereafter, at each step: if T has an angle equal to θ, the game stops and Mulan wins; otherwise Mulan picks a point P on the perimeter of T, not a vertex, and makes a straight cut from P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one and the other becomes the new T. Determine for which real θ Mulan can guarantee victory in finitely many steps, regardless of Shan-Yu's play.

**Answer.** Mulan guarantees victory in finitely many steps **if and only if** θ = 180°/N for some integer N ≥ 2 (i.e. θ is a unit fraction of the straight angle: 180°/θ ∈ ℤ, 180°/θ ≥ 2).

We prove the two directions separately. The argument uses the **invariant / monovariant** technique and **modular arithmetic over ℝ/θℤ** (both in the Combinatorics / Number-Theory sections of `knowledge_base.md`), with **casework** and **induction on k** (General Proof Methods).

---

### 0. The exact angle-triple transform (preliminary lemma)

Let T have angles (X, Y, Z), so X + Y + Z = 180°, each in (0, 180°). Mulan elects to split the angle X (she chooses this by placing P on the side opposite the X-vertex). The cut from P to the X-vertex splits X into γ (the part adjacent to Y) and X − γ (adjacent to Z), with γ ∈ (0, X) — the openness is exactly the rule that P is not a vertex. The two children are:

- **child 1 (keeps Y):** (γ, Y, 180° − Y − γ);
- **child 2 (keeps Z):** (X − γ, Z, Y + γ).

*Derivation.* Triangle 1 has the X-vertex, the Y-vertex, and P; its angle at the X-vertex is γ (the part of X on the Y-side of the cut), its angle at the Y-vertex is Y (unchanged), so its third angle (at P) is 180° − γ − Y. Triangle 2 has the X-vertex, the Z-vertex, and P; its angle at the X-vertex is X − γ, its angle at the Z-vertex is Z, so its third angle is 180° − (X − γ) − Z = 180° − X + γ − Z = (Y + Z) + γ − Z = Y + γ, using X + Y + Z = 180°. ∎

**Structural corollary (supplementary pair).** The two angles created at P, namely (180° − Y − γ) in child 1 and (Y + γ) in child 2, sum to 180°. Everything below flows from this. Mulan controls the choice of the split vertex (equivalently which angle X to destroy) and the parameter γ ∈ (0, X); Shan-Yu then chooses which child survives.

---

### I. IF direction — θ = 180°/N, N ≥ 2 ⇒ Mulan wins

Fix N ≥ 2 and put θ := 180°/N, so that N·θ = 180°. Call an angle a **θ-multiple** if it equals kθ for some integer k with 1 ≤ k ≤ N − 1 (these are exactly the positive multiples of θ that are strictly less than 180°). In particular θ itself is a θ-multiple (k = 1). Note that a number a with 0 < a < 180° is a θ-multiple iff a ≡ 0 (mod θ), because Nθ = 180° forces every positive multiple of θ below 180° to be one of θ, 2θ, …, (N−1)θ.

Mulan plays in two phases.

#### I.1 Phase 1 — create a θ-multiple

At the start of her turn, if some angle of T already equals θ, the game stops and Mulan wins. If some angle is a θ-multiple kθ with k ≥ 2, skip to Phase 2. So assume **no angle of T is a θ-multiple**; we exhibit a move producing a θ-multiple in both children.

Let X be a **largest** angle of T, so X ≥ 60° (the largest of three positive numbers summing to 180° is at least 60°). Let Y, Z be the other two angles (X + Y + Z = 180°, Y, Z > 0). Both Y and Z are non-θ-multiples (we are in the "no θ-multiple" case), so their residues modulo θ are nonzero: r_Y := Y mod θ ∈ (0, θ), and likewise for Z. Set

$$\gamma \;=\; \theta - r_Y \;\in\; (0, \theta).$$

(Equivalently, γ ≡ −Y (mod θ) and 0 < γ < θ.) Mulan splits the angle X with this γ (γ adjacent to Y).

**Claim (both children carry a θ-multiple at P).**
- Child 2's angle at P is Y + γ. By construction Y + γ ≡ Y + (−Y) ≡ 0 (mod θ).
- Child 1's angle at P is 180° − Y − γ ≡ 180° − (Y + γ) ≡ 180° ≡ Nθ ≡ 0 (mod θ), using Nθ = 180°.

So both children's P-angles are θ-multiples. Whichever child Shan-Yu keeps has a θ-multiple.

#### I.2 Validity of the create-move

We must show the move is legal (γ ∈ (0, X)) and that both children are non-degenerate (all six child angles lie in (0, 180°)). We treat the size of θ in two exhaustive, disjoint cases.

**(A) N ≥ 3, i.e. θ ≤ 60°.**
Since no angle is a θ-multiple and θ itself is a θ-multiple, no angle equals θ. Combined with X ≥ 60° ≥ θ:
- If θ < 60°, then X ≥ 60° > θ, so θ < X.
- If θ = 60°, then X ≠ 60° (60° is a θ-multiple, excluded) and X ≥ 60°, so X > 60° = θ.

In both sub-cases θ < X strictly. As γ < θ, we obtain γ < X, i.e. **γ ∈ (0, X)**: the split is legal.

For non-degeneracy, it remains to check the two P-angles are in (0, 180°). Write Y = mθ + r_Y with m = ⌊Y/θ⌋ ≥ 0 (an integer), r_Y = Y mod θ ∈ (0, θ). Then

$$Y + \gamma \;=\; m\theta + r_Y + (\theta - r_Y) \;=\; (m+1)\theta,$$

a θ-multiple. For this to be < 180° = Nθ we need m + 1 ≤ N − 1, i.e. m ≤ N − 2, i.e. Y < (N−1)θ = 180° − θ. Now Y is an angle adjacent to the largest angle X, so Y < 180° − X (strictly, since Z = 180° − X − Y > 0). As X ≥ 60°, Y < 180° − 60° = 120°. And in Case A, θ ≤ 60° gives 180° − θ ≥ 120°. Hence Y < 120° ≤ 180° − θ, so **Y < 180° − θ**, giving Y + γ = (m+1)θ ≤ (N−1)θ < Nθ = 180°. The other P-angle, 180° − Y − γ = 180° − (m+1)θ = (N − m − 1)θ, is also a positive θ-multiple (since m ≤ N − 2 gives N − m − 1 ≥ 1). Both children are non-degenerate. The remaining child angles γ, Y, X − γ, Z are all in (0, 180°) (γ ∈ (0, θ) ⊂ (0, 180°); Y, Z are angles; X − γ = X − (θ − r_Y) > X − θ > 0 since X > θ). ✓

**(B) N = 2, i.e. θ = 90°.** The θ-multiples are just {90°} (only k = 1 is allowed). "No θ-multiple" means no angle equals 90°. We claim **both** angles adjacent to the largest angle are strictly less than 90°. Indeed, at most one angle of a triangle exceeds 90° (two would sum to > 180°), and no angle equals 90° here, so the angles > 90° form a set of size at most 1. The largest angle X is that angle if it exists; otherwise all three are < 90°. Either way, both Y and Z satisfy Y, Z < 90°.

Pick Y (either adjacent angle; both work). Since Y is not a θ-multiple, Y mod 90° = Y (as 0 < Y < 90°), so r_Y = Y and γ = 90° − Y ∈ (0, 90°). Now:
- **γ < X:** γ = 90° − Y, so γ < X ⇔ X + Y > 90° ⇔ Z < 90°, which holds by the claim above.
- **Y + γ = 90°** (a θ-multiple, the index-1 case) **< 180°**, and 180° − Y − γ = 90°, also a θ-multiple. Both children are non-degenerate (γ > 0, X − γ = X + Y − 90° > 0 since Z < 90°, etc.).

Both cases (A), (B) being settled, the create-move is always valid, and both children carry a θ-multiple. Note Case B produces θ itself (index 1) in both children: Mulan wins on the very next turn's check, in **1 move** total.

#### I.3 Phase 2 — k-descent

After Phase 1 the surviving child has a θ-multiple kθ at its P-vertex for some k with 1 ≤ k ≤ N − 1 (the index satisfies k = m + 1 where m = ⌊Y/θ⌋ ≤ N − 2 in Case A; in Case B k = 1). If k = 1, that is θ and Mulan wins at the next check. Otherwise k ≥ 2; iterate the following **descent step**.

**Setup.** T has an angle equal to kθ at some vertex, with k ≥ 2 (and k ≤ N − 1, since kθ < 180° = Nθ). Call that angle X := kθ; let Y, Z be its adjacent angles (X + Y + Z = 180°, so Y + Z = 180° − kθ).

**Move.** Mulan splits X with γ = θ (the part adjacent to either neighbor; choose Y). The children are:
- child 1 = (θ, Y, 180° − Y − θ);
- child 2 = ((k−1)θ, Z, Y + θ).

**Validity of γ = θ.** Since k ≥ 2, 0 < θ < kθ = X, so γ = θ ∈ (0, X): the split is legal. For non-degeneracy:
- child 1 needs 180° − Y − θ > 0, i.e. Y < 180° − θ. Now Y ≤ Y + Z = 180° − kθ ≤ 180° − 2θ < 180° − θ (the first inequality is Z ≥ 0, strict as Z > 0). ✓
- child 2 needs (k−1)θ > 0 (true, k ≥ 2) and Y + θ < 180°, i.e. Y < 180° − θ — just established. ✓
All remaining child angles (θ, Y, (k−1)θ, Z) are visibly in (0, 180°).

**Effect (strict monovariant).** Child 1 carries θ at the split vertex — if Shan-Yu keeps child 1, the next check stops the game and Mulan wins. Child 2 carries (k−1)θ at the split vertex. To delay, Shan-Yu keeps child 2; the θ-multiple index of the surviving child strictly decreases **k ↦ k − 1**.

**Termination.** Starting from k ≤ N − 1, after at most N − 2 descent steps the index reaches k = 2. At k = 2, the move with γ = θ produces child 1 = (θ, Y, 180° − Y − θ) and child 2 = (θ, Z, Y + θ) — **both children carry θ** (child 2's split-vertex angle is (k−1)θ = θ). Whichever child Shan-Yu keeps, the next check fires and Mulan wins.

#### I.4 Total move bound

Phase 1 contributes 1 move (which already wins in Case B). In Case A, Phase 2 contributes at most (k−1) moves where k ≤ N − 1, i.e. at most N − 2 descent moves. Thus in all cases Mulan wins in **at most N − 1 moves**, a finite, deterministic bound independent of Shan-Yu's choices. (Numerical check: for N = 2, 3, 4, 5, 7, 8, 11, 13, 17, 19, 23, 99 the worst-case count equals N − 1 exactly when Shan-Yu always keeps the larger-index child; verified.)

**Remark (real θ, not just integer-degree).** The mod-θ arithmetic above uses only the relation Nθ = 180° and the residue Y mod θ; nowhere is θ required to be an integer number of degrees. For example θ = 180°/7 (≈ 25.714°) works verbatim — the residues live in ℝ/(180°/7)ℤ, and the descent index k is an integer in {1, …, 6}. (Verified numerically above.) Hence the IF direction holds for **every** integer N ≥ 2, including non-integer-degree θ.

This completes the IF direction. ∎ (of the IF direction)

---

### II. ONLY direction — θ ≠ 180°/N ⇒ Shan-Yu wins

Assume 180°/θ ∉ ℤ. Write

$$180° \;=\; q\,\theta \;+\; r, \qquad q = \lfloor 180°/\theta \rfloor \geq 1, \quad r \in (0, \theta).$$

(That r ≠ 0 is exactly the assumption 180°/θ ∉ ℤ; q ≥ 1 because θ < 180°. When θ > 90° we have q = 1, r = 180° − θ ∈ (0, θ) since θ ∈ (90°, 180°). When θ ∈ (0°, 90°) with 180°/θ ∉ ℤ we have q ≥ 2 and r ∈ (0, θ).) Work modulo θ; an angle a is a θ-multiple iff a ≡ 0 (mod θ). Note **180° ≡ r ≢ 0 (mod θ)**.

#### II.1 Shan-Yu's invariant

Define the invariant

> **(I)**: *no angle of T is a θ-multiple* — equivalently, all three angle-residues (mod θ) are nonzero.

Since θ itself is a θ-multiple, (I) ⇒ "no angle equals θ": maintaining (I) prevents the stopping condition forever.

#### II.2 Shan-Yu's initial triangle (existence lemma)

Shan-Yu must open with a triangle satisfying (I). The forbidden angle-values (θ-multiples in (0°, 180°)) are exactly {θ, 2θ, …, qθ}, a **finite** set of q points: indeed q = ⌊180°/θ⌋ and r = 180° − qθ > 0 gives qθ < 180° < (q + 1)θ, so the positive multiples of θ below 180° are precisely θ, 2θ, …, qθ. (This is finite regardless of whether θ/180° is rational or irrational — we forbid the actual angle *values* kθ < 180°, not the coset set {kθ mod 180°}, so no Kronecker-density phenomenon enters.)

Let Δ = {(A, B) ∈ ℝ² : A > 0, B > 0, A + B < 180°} be the open 2-simplex (a nonempty open convex set). The "bad" locus — points where some angle is a θ-multiple — is

$$\mathcal{L} \;=\; \bigcup_{k=1}^{q}\Bigl(\{A = k\theta\} \;\cup\; \{B = k\theta\} \;\cup\; \{A + B = 180° - k\theta\}\Bigr),$$

a finite union of lines (the three families correspond to A, B, C = 180° − A − B being a θ-multiple). Each line has empty interior in ℝ²; a finite union of lines has empty interior. A nonempty open set in ℝ² cannot have empty interior, so **Δ ⊄ ℒ**, i.e. Δ \ ℒ ≠ ∅ (indeed it is open and dense, of full Lebesgue measure). Pick (A₀, B₀) ∈ Δ \ ℒ and set C₀ = 180° − A₀ − B₀. Then A₀, B₀, C₀ are all in (0°, 180°), sum to 180°, and none is a θ-multiple. Shan-Yu opens with T₀ = (A₀, B₀, C₀), which satisfies (I). ✓

This argument is uniform over every non-unit-fraction θ (rational like 72°, 100°, 50°, 7°, 13°, 40°, 135°, 36.5°, 60.0001°, or irrational) — the only feature used is that the forbidden set is finite, which holds for all fixed θ.

#### II.3 Maintenance of (I) — the four-case obstruction

Assume T = (X, Y, Z) satisfies (I): X ≢ 0, Y ≢ 0, Z ≢ 0 (mod θ). Mulan makes any legal move (any choice of split vertex, any γ ∈ (0, X)). By relabeling, suppose she splits X, with γ adjacent to Y; the children are child 1 = (γ, Y, 180° − Y − γ) and child 2 = (X − γ, Z, Y + γ).

**Claim.** It is impossible for **both** children to contain a θ-multiple. Consequently at least one child satisfies (I), and Shan-Yu keeps that child.

*Proof by contradiction.* Suppose both children contain a θ-multiple. In child 1 the three angle-residues are (γ mod θ, Y mod θ, (180° − Y − γ) mod θ); by (I), Y ≢ 0, so the θ-multiple in child 1 is in one of the **two remaining slots**: either γ ≡ 0 or 180° − Y − γ ≡ 0 (mod θ). In child 2 the residues are ((X − γ) mod θ, Z mod θ, (Y + γ) mod θ); by (I), Z ≢ 0, so the θ-multiple in child 2 is either X − γ ≡ 0 or Y + γ ≡ 0 (mod θ).

Thus there are exactly **2 × 2 = 4** disjoint, exhaustive combinations. We rule each out (all congruences are mod θ):

1. **γ ≡ 0 and X − γ ≡ 0.** Then X ≡ γ + (X − γ) ≡ 0 + 0 = 0. But X ≢ 0 by (I). ✗
2. **γ ≡ 0 and Y + γ ≡ 0.** Then Y ≡ (Y + γ) − γ ≡ 0 − 0 = 0. But Y ≢ 0 by (I). ✗
3. **180° − Y − γ ≡ 0 and X − γ ≡ 0.** The first gives Y + γ ≡ 180° ≡ r (mod θ). The second gives γ ≡ X. Substituting: Y + X ≡ r. But X + Y + Z = 180° ≡ r, so Z ≡ r − (X + Y) ≡ r − r = 0. But Z ≢ 0 by (I). ✗
4. **180° − Y − γ ≡ 0 and Y + γ ≡ 0.** The first gives Y + γ ≡ 180° ≡ r. The second gives Y + γ ≡ 0. Hence r ≡ 0 (mod θ). But r ∈ (0, θ), so r ≢ 0 (mod θ). ✗

All four combinations contradict (I) (or, in case 4, the defining property r ∈ (0, θ) of the ONLY regime). Hence no γ makes both children contain a θ-multiple.

Therefore at least one child has **no** θ-multiple, i.e. satisfies (I). Shan-Yu keeps that child. The invariant (I) is maintained for every Mulan move. ∎

#### II.4 Shan-Yu wins

Shan-Yu opens with a triangle satisfying (I) (II.2) and, after every Mulan move, keeps a child still satisfying (I) (II.3). Since (I) excludes any angle equal to θ (a θ-multiple), the stopping condition is never met, for any Mulan strategy. Hence Mulan cannot guarantee victory — **Shan-Yu has a strategy (the (I)-preserving strategy) that prevents θ forever**. ✓

(Exhaustiveness of the four-case check, stated once: each child has exactly three angles; in child 1 the slot Y is nonzero mod θ by (I), leaving 2 candidate slots; in child 2 the slot Z is nonzero by (I), leaving 2 candidate slots; 2 × 2 = 4 disjoint combinations, all ruled out. No angle of either child escapes the analysis.)

---

### III. Combining both directions

- IF (§I): if θ = 180°/N, N ≥ 2, Mulan wins in ≤ N − 1 moves.
- ONLY (§II): if 180°/θ ∉ ℤ, Shan-Yu has a (I)-preserving strategy preventing θ forever, so Mulan does not guarantee victory.

The boundary is exactly "180°/θ ∈ ℤ and ≥ 2" ⇔ "θ = 180°/N for some integer N ≥ 2" (the constraint N ≥ 2 is the assumption θ < 180°, and θ > 0 excludes N = ∞). The two directions are complementary and exhaustive over θ ∈ (0°, 180°).

Therefore: **Mulan guarantees victory in finitely many steps, regardless of how Shan-Yu plays, if and only if θ = 180°/N for some integer N ≥ 2.** ∎

---

## Promotable lemmas

1. **Angle-triple transform (§0).** Statement: splitting angle X of (X,Y,Z) (X+Y+Z=180°) with γ ∈ (0,X) adjacent to Y yields child 1 = (γ, Y, 180°−Y−γ) and child 2 = (X−γ, Z, Y+γ); the two P-angles are supplementary (sum 180°). Proved in §0 above (direct angle chase). Located: this file, §0.

2. **Create-multiple lemma (§I.1–I.2).** Statement: for θ = 180°/N (N ≥ 2), from any triangle with no θ-multiple, choosing X = max angle (≥ 60°) and γ = θ − (Y mod θ) makes both children's P-angles θ-multiples; the move is valid (γ ∈ (0,X), all child angles in (0,180°)) via the N ≥ 3 (θ ≤ 60°) vs N = 2 (θ = 90°) casework. Proved in §I.1–I.2. Located: this file, §I.1–I.2.

3. **k-descent lemma (§I.3).** Statement: for θ = 180°/N, splitting an angle kθ (2 ≤ k ≤ N−1) with γ = θ yields child 1 = (θ, Y, …) carrying θ and child 2 = ((k−1)θ, Z, Y+θ); the surviving θ-multiple index strictly decreases k ↦ k−1, terminating at k = 2 (both children carry θ) in ≤ N−2 descent steps. Proved in §I.3. Located: this file, §I.3.

4. **Mod-θ four-case obstruction (§II.3).** Statement: for r = 180° mod θ ∈ (0,θ) (θ not a unit fraction), the invariant (I) "no angle ≡ 0 (mod θ)" is preserved under arbitrary Mulan moves — the four combinations of θ-multiple slots across the two children reduce respectively to X ≡ 0, Y ≡ 0, Z ≡ 0, or r ≡ 0, all contradictions. Proved in §II.3. Located: this file, §II.3.

5. **Initial-triangle existence (§II.2).** Statement: for any non-unit-fraction θ, a triangle satisfying (I) exists — the forbidden angle-values form a finite set {θ, 2θ, …, qθ} (q = ⌊180°/θ⌋), so the bad locus in the open 2-simplex is a finite union of lines with nonempty (open, dense) complement. Proved in §II.2. Located: this file, §II.2.
