# geometric-anchor — perpendicular + bisector chain (synthetic-geometry IF for dyadic θ)

## Status
partial

## Approaches tried
- Geometric construction via altitudes and angle-bisectors (this file) — a different ROUTE for the IF direction (synthetic/constructive geometry rather than algebraic mod-θ). Independently certifies the dyadic subcase θ = 180°/2^a (a ≥ 1) by a perpendicular one-cut base case and a bisector-doubling induction, with NO use of the mod-θ create-move or the four-case obstruction. Outcome: dyadic IF certified self-containedly; non-dyadic IF and the ENTIRE ONLY direction honestly deferred (see Gaps). (keep prior entries)
- Round 1 build: wrote the altitude-foot-interior lemma as a named lemma with the acute/right/obtuse classification; wrote the bisector lemma; wrote the dyadic induction on a rigorously with the IH-reuse equivalence stated as an explicit one-line lemma; marked the ONLY + non-dyadic-IF deferrals as named gaps. Status: partial — a clean, self-contained, reviewer-certifiable dyadic-IF sub-proof plus an honest scope statement.

## Current best
A complete, rigorous, self-contained synthetic-geometry proof of the **dyadic IF direction**: for every θ of the form 180°/2^a with integer a ≥ 1, Mulan guarantees victory in ≤ a moves from any initial triangle. The proof uses only (i) the altitude-foot-interior lemma (perpendicular anchor, base case θ = 90°) and (ii) the angle-bisector lemma (doubling step, 2θ → θ), plus ordinary induction on a. It is a genuine alternative to the mod-θ create-move + k-descent: it invokes no modular arithmetic, no mod-θ lattice, and no four-case obstruction. It independently certifies the create-move for N = 2, 4, 8, … (the dyadic unit fractions), which is exactly the insurance the outline-reviewer asked for.

**Open gaps (named, in-file):**
- **GAP-D1 (non-dyadic IF).** This approach does NOT prove Mulan wins for θ = 180°/N when N has an odd factor (e.g. N = 3, 5, 6, 7, …). The perpendicular/bisector toolkit only closes dyadic chains θ → 2θ → 4θ → … → 90°. The odd-factor step is deferred to the `mod-theta-descent` create-move + k-descent (a shared wall — see Gaps §GAP-D1).
- **GAP-D2 (ONLY direction).** This approach proves NO part of the converse (that for θ not a unit fraction of 180°, Shan-Yu has a defense). The entire ONLY direction is deferred to the `mod-theta-descent` four-case mod-θ obstruction (a shared wall).

So this file is a **scoped partial**: it independently certifies one piece of the IF direction (the dyadic subcase) and imports nothing; it does not, by itself, solve the whole problem.

## Target (whole problem)
The conjectured full characterization (field consensus, to be proved by the population as a whole): θ = 180°/N for some integer N ≥ 2. This file contributes a self-contained proof of the IF direction for the subfamily N = 2^a.

## Technique
Synthetic Euclidean geometry (altitude = perpendicular from a vertex; internal angle bisector) + induction on the dyadic exponent a. KB entries used: **Induction** (General Proof Methods), **Casework / exhaustion** (General Proof Methods), **Synthetic toolkit — angle chasing** (Geometry section). No number theory, no modular arithmetic.

---

## Full proof of the dyadic IF direction

We prove the following scoped theorem. Throughout, a "move" is one round of (Mulan chooses P on the perimeter, P not a vertex; cuts from P to the opposite vertex; Shan-Yu discards one child; the other child becomes the new T). Mulan "wins in m moves" if, no matter how Shan-Yu discards, the triangle T after at most m moves has θ among its three angles.

**Theorem (Dyadic IF).** Let a be an integer with a ≥ 1, and set θ = 180°/2^a. Then from any non-degenerate initial triangle T, Mulan has a strategy guaranteeing that θ appears as an angle of T within at most a moves, regardless of Shan-Yu's discards.

We prove three lemmas and then induct on a.

### Lemma 1 (Altitude-foot interior)

In every non-degenerate triangle, the foot of the altitude from the largest-angle vertex lies strictly in the interior of the opposite side.

*Proof.* Let the triangle be ABC, and let A be a vertex at which the largest angle is attained: ∠A ≥ ∠B and ∠A ≥ ∠C. We claim ∠B < 90° and ∠C < 90°. Suppose for contradiction that ∠B ≥ 90°. Since A is largest, ∠A ≥ ∠B ≥ 90°, so ∠A + ∠B ≥ 180°, forcing ∠C = 180° − ∠A − ∠B ≤ 0°, contradicting that the triangle is non-degenerate (∠C > 0°). Hence ∠B < 90°; by symmetry ∠C < 90°.

The foot F of the perpendicular from A to the line BC lies on the segment BC (rather than on its extension) if and only if both base angles ∠B and ∠C are acute. Indeed, F lies on the ray from B through C iff the angle ∠ABF = ∠B is acute (otherwise the perpendicular from A meets the line BC on the side of B away from C), and dually F lies on the ray from C through B iff ∠C is acute. Since both are acute, F lies in the interior of segment BC. ∎

**Corollary (Perpendicular anchor).** From any triangle T, Mulan can force θ = 90° to appear in one move.

*Proof.* Let A be a largest-angle vertex of T and let the opposite side be BC. By Lemma 1 the foot F of the altitude from A lies strictly inside BC, so F is on the perimeter of T and is not a vertex. Mulan chooses P = F and cuts from P to the opposite vertex A (the segment PA is the altitude, hence perpendicular to BC). The cut splits T into two triangles ABP and ACP. In triangle ABP, the angle at P is 90° (PA ⊥ BC and PB lies along BC). In triangle ACP, the angle at P is 90° (PA ⊥ BC and PC lies along BC). Thus both children have a 90° angle. Whichever child Shan-Yu discards, the remaining triangle has θ = 90° as an angle. ∎

This settles the base case a = 1 (θ = 90° = 180°/2): Mulan wins in 1 = a move.

### Lemma 2 (Bisector step: 2θ → θ)

Suppose the current triangle T has an angle equal to 2θ at some vertex V, where 0° < θ < 90° (so 0° < 2θ < 180°). Then Mulan has a one-move strategy that places θ in both children, hence wins regardless of Shan-Yu's discard.

*Proof.* Let V be the vertex with ∠V = 2θ, and let the opposite side be XY. Mulan chooses P to be the point where the **internal angle bisector** of ∠V meets the side XY, and cuts from P to V. The internal bisector of an angle of a triangle meets the opposite side in the interior of that side (the bisector ray lies strictly inside the angle ∠V, hence inside the triangle, hence meets the segment XY at an interior point); so P is on the perimeter and is not a vertex — a legal move.

The cut splits ∠V = 2θ into two angles of measure θ each: the angle at V in child 1 is θ, and the angle at V in child 2 is θ. Hence both children have θ as an angle. Whichever child Shan-Yu discards, the remaining triangle has θ. ∎

### Lemma 3 (IH-reuse: "target τ appears" is a configuration event, independent of the official stop target)

Let τ be any angle in (0°, 180°). The statement "Mulan has a strategy that, run in the game with official stop-target τ, forces τ to appear as an angle of T within ≤ m moves" is equivalent to: "Mulan has a decision tree of depth ≤ m (a function from the current triangle to a cut, robust to Shan-Yu's discards) such that every leaf triangle has τ among its three angles." In particular, the same decision tree can be executed inside the game with any other official stop-target τ′: at each node, if the current triangle already has τ′, Mulan has already won (the game stops); otherwise Mulan follows the tree's prescribed cut. After ≤ m steps along the tree, either τ′ has appeared (Mulan wins) or a leaf with τ as an angle is reached.

*Proof.* The game mechanics (legal cut, two children, Shan-Yu's discard) do not depend on the stop-target; the target only determines the stopping condition. A strategy for target τ is precisely a decision tree whose leaves are τ-bearing triangles. Such a tree is well-defined and executable in any version of the game; the only thing that changes is when the official game stops. Running the τ-tree inside the τ′-game therefore reaches, within its depth, either a τ′-bearing triangle (early stop, win for target τ′) or a τ-bearing leaf. ∎

### Induction on a

We prove the Theorem (Dyadic IF) by induction on a.

**Base case a = 1.** Here θ = 180°/2 = 90°. By the Perpendicular-anchor corollary, Mulan forces 90° in one move from any triangle. So she wins in 1 = a move. ✓

**Inductive step.** Let a ≥ 2 and assume (induction hypothesis, IH) that for θ̃ = 180°/2^{a−1} = 2θ, Mulan can force θ̃ to appear as an angle of T within ≤ a − 1 moves from any triangle. We prove the claim for θ = 180°/2^a = θ̃/2.

Mulan's strategy in the game with official target θ:

1. **Phase 1 (force 2θ to appear).** Execute the IH-strategy for target 2θ. By Lemma 3, this decision tree can be run inside the game with target θ. Follow it for up to a − 1 moves. At each move, check whether the current triangle has θ as an angle.
   - If yes, Mulan has already won (in ≤ a − 1 ≤ a moves).
   - If no, continue following the tree.
   By the IH, after at most a − 1 moves the tree reaches a leaf whose triangle has 2θ as an angle. (If θ appeared earlier we already won, so assume it did not.)

2. **Phase 2 (bisect 2θ).** The current triangle T has an angle 2θ at some vertex V, with 0° < θ < 90° (since a ≥ 2 ⇒ θ = 180°/2^a ≤ 45° < 90°, and θ > 0°). Apply Lemma 2: Mulan bisects the 2θ angle. Both children have angle θ. Whichever child Shan-Yu discards, the remaining triangle has θ. Mulan wins in this one additional move.

Total move count: at most (a − 1) + 1 = a. ✓

This closes the induction. The proof uses only the altitude-foot-interior lemma, the angle-bisector lemma, and ordinary induction — no modular arithmetic, no mod-θ lattice, no create-move, no four-case obstruction. ∎

---

## Gaps (explicit, honest scope)

This file proves ONLY the dyadic IF subcase. The following are NOT proved here.

### GAP-D1 (non-dyadic IF direction)
The Theorem above covers only θ = 180°/2^a (N = 2, 4, 8, 16, …). It does **not** prove that Mulan wins for θ = 180°/N when N has an odd factor (N = 3, 5, 6, 7, 9, 10, 11, …). The reason is intrinsic to the geometric toolkit: the bisector step (Lemma 2) only ever halves an angle (2θ → θ), so the perpendicular anchor (θ = 90°) together with bisectors can only ever produce angles of the form 180°/2^a. There is no synthetic-geometry move in this file that produces, say, 60° = 180°/3 from an arbitrary triangle in a target-agnostic way. Closing the odd-factor IF direction requires a different idea; the `mod-theta-descent` approach supplies one (the create-move γ = θ − (Y mod θ), followed by the k-descent γ = θ reducing kθ → (k−1)θ). That mechanism is a **shared wall**: this file imports it as a black box and does not re-prove it. Until `mod-theta-descent`'s create-move + k-descent is reviewer-certified, the non-dyadic IF direction is unproven by the population.

### GAP-D2 (the ENTIRE ONLY direction)
This file proves no part of the converse: that for θ NOT of the form 180°/N (e.g. θ = 72°, 100°, 50°, 7°, irrational θ, etc.), Shan-Yu has a defense preventing Mulan from ever forcing θ. The synthetic-geometry toolkit here (altitudes, bisectors) is constructive on Mulan's side and offers no obvious invariant for Shan-Yu's defense. The ONLY direction is deferred entirely to the `mod-theta-descent` four-case mod-θ obstruction (the supplementary-at-P + four-case residue chase). That obstruction is a **shared wall**: this file does not re-prove it. Until `mod-theta-descent`'s four-case obstruction is reviewer-certified, the ONLY direction is unproven by the population.

### Summary of scope
- **Independently certified here:** Mulan wins for θ = 180°/2^a (a ≥ 1). Fully rigorous, self-contained, no imports.
- **Imported (not proved here):** non-dyadic IF (GAP-D1, from `mod-theta-descent`); the entire ONLY direction (GAP-D2, from `mod-theta-descent`).
- **Population role:** diversity insurance on the IF direction's dyadic core (an independent certification of the create-move for N = 2, 4, 8, …), keeping the field from collapsing to a single framing. It is a valid partial member; it is not, and does not claim to be, a whole-problem solution.

## Key lemmas (claim + mechanism)
- **Altitude-foot interior (Lemma 1):** the altitude from the largest-angle vertex has its foot interior to the opposite side — by classification (largest angle ⇒ the other two are acute ⇒ the foot is interior). Yields the perpendicular anchor.
- **Perpendicular-anchor corollary:** θ = 90° forced in one move from any triangle — by cutting from the altitude foot to the opposite vertex; both children get a 90° angle at the foot.
- **Bisector step (Lemma 2):** an angle 2θ at vertex V ⇒ bisecting it (cut along the internal bisector to the opposite side) gives θ in both children — by definition of angle bisection; the internal bisector meets the opposite side in its interior, so the move is legal.
- **IH-reuse (Lemma 3):** a winning decision tree for target τ is a depth-m tree with τ-bearing leaves, executable in any target's game — because the game mechanics are target-independent; only the stop condition depends on the target.
- **Dyadic induction (Theorem):** θ = 180°/2^a wins in ≤ a moves — by IH (force 2θ = 180°/2^{a−1} appears, then bisect).

## Promotable lemmas
- **Lemma 1 (Altitude-foot interior).** In every non-degenerate triangle, the foot of the altitude from a largest-angle vertex lies strictly interior to the opposite side. Proof above (acute-right-obtuse reduction via "largest ⇒ other two acute"). Proved in this file. Candidate for certification into `results/imo-2026-04/lemmas/altitude-foot-interior.md` — reusable by any approach needing the perpendicular anchor.
- **Lemma 2 (Bisector step).** If T has an angle 2θ at vertex V with 0° < θ < 90°, then the internal bisector cut (P = bisector foot on the opposite side) gives both children angle θ at V. Proof above. Candidate for `results/imo-2026-04/lemmas/bisector-step.md`.
- **Theorem (Dyadic IF).** For every integer a ≥ 1, θ = 180°/2^a is a Mulan win in ≤ a moves. Proof above (perpendicular base + bisector induction + IH-reuse). Candidate for `results/imo-2026-04/lemmas/dyadic-if.md` — an independent certification of the IF direction for N = 2^a, usable as insurance if the create-move inequalities in `mod-theta-descent` are ever questioned for dyadic N.
