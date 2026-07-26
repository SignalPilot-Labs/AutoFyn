# imo-2026-04 — Mulan's triangle game

## Status
solved

## Approaches tried
- mod-theta-descent — **SOLVED** (workhorse, reviewer-certified round 1). Both directions proved in full rigorous prose. IF: create-move (γ = θ − (Y mod θ)) makes both children's P-angles θ-multiples; validity via N≥3 (θ≤60°) vs N=2 (θ=90°) casework, exhaustive and disjoint; k-descent (γ=θ) strictly decreases the index k↦k−1, terminating at k=2 (both children carry θ) in ≤N−2 steps; total ≤N−1 moves. Works for all real θ=180°/N including non-integer-degree (e.g. 180/7). ONLY: invariant (I) "no angle ≡0 mod θ"; initial triangle exists (forbidden set {θ,2θ,…,qθ} finite, bad locus = finite union of lines in open 2-simplex, complement nonempty); four-case obstruction (2 slots × 2 slots, exhaustive via distributive law) rules out both-children-θ-multiple using 180°≡r∈(0,θ). Uniform over all non-unit-fraction θ (rational or irrational). Numerically verified: create-move+descent for N∈{2,3,4,5,7,8,11,13,17,19,23,99}; obstruction 0 escapes in 13 θ values (incl. irrational).
- geometric-anchor — partial (diversity on dyadic IF). Independent synthetic-geometry route (altitude-foot-interior + bisector + dyadic induction) certifies θ=180/2^a for the IF direction self-containedly, ≤a moves. Defers non-dyadic IF and the ENTIRE ONLY direction to mod-theta-descent (honest gaps GAP-D1, GAP-D2). Reviewer-certified as a clean scoped partial; its dyadic-IF is a genuine independent certification (no mod-θ arithmetic) and serves as insurance on the dyadic core.
- fixpoint-attractor, torsion-subgroup — registered insurance re-skins of the mod-θ wall; not built.

## Current best
Complete characterization, proved both directions: **Mulan guarantees victory in finitely many steps, regardless of Shan-Yu's play, if and only if θ = 180°/N for some integer N ≥ 2.** IF direction: ≤ N−1 moves via create-move + k-descent. ONLY direction: Shan-Yu maintains invariant (I) "no angle ≡ 0 mod θ" (180°≡r∈(0,θ)), opening with a generic triangle (finite forbidden set) and, after each Mulan move, keeping a child still satisfying (I) — the four-case obstruction (exhaustive 2×2 mod-θ residue chase) shows at least one child always satisfies (I), so no angle ever equals θ.

## Full proof

### Answer
Mulan guarantees victory in finitely many steps **if and only if** θ = 180°/N for some integer N ≥ 2 (i.e. 180°/θ ∈ ℤ and ≥ 2).

### Preliminary lemma (angle-triple transform)
Let T have angles (X, Y, Z), X+Y+Z = 180°, each in (0°, 180°). Mulan splits angle X with parameter γ ∈ (0, X), the part γ adjacent to Y (she places P on the side opposite the X-vertex; P not a vertex ⇔ γ ∈ (0, X) open). The two children are:
- **child 1 (keeps Y):** (γ, Y, 180° − Y − γ);
- **child 2 (keeps Z):** (X − γ, Z, Y + γ).

*Proof.* Direct angle chase. Child 1: angles at X-vertex = γ, at Y-vertex = Y, at P = 180° − γ − Y. Child 2: angles at X-vertex = X − γ, at Z-vertex = Z, at P = 180° − (X−γ) − Z = Y + γ (using X+Y+Z=180°). ∎ The two P-angles (180°−Y−γ) and (Y+γ) are supplementary (sum 180°). Mulan controls the split vertex (which X to destroy) and γ ∈ (0, X); Shan-Yu chooses which child survives.

---

### I. IF direction — θ = 180°/N, N ≥ 2 ⇒ Mulan wins

Fix N ≥ 2, θ := 180°/N (so Nθ = 180°). Call a ∈ (0°,180°) a **θ-multiple** iff a ≡ 0 (mod θ) (equivalently a ∈ {θ, 2θ, …, (N−1)θ}). In particular θ is a θ-multiple. Mulan plays in two phases.

#### I.1 Phase 1 — create a θ-multiple
If some angle of T already equals θ, Mulan wins. If some angle is a θ-multiple kθ (k≥2), skip to Phase 2. Assume no angle is a θ-multiple. Let X be a **largest** angle (X ≥ 60°); Y, Z the others (both non-θ-multiples, so r_Y := Y mod θ ∈ (0°, θ)). Set
$$\gamma = \theta - r_Y \in (0°, \theta).$$
Mulan splits X with this γ (adjacent to Y). Both children's P-angles are θ-multiples:
- child 2 P-angle: Y + γ ≡ Y + (−Y) ≡ 0 (mod θ);
- child 1 P-angle: 180° − Y − γ ≡ 180° − 0 ≡ Nθ ≡ 0 (mod θ).

Whichever child Shan-Yu keeps carries a θ-multiple.

#### I.2 Validity of the create-move (exhaustive disjoint casework)
**(A) N ≥ 3 (θ ≤ 60°).** No angle equals θ (= a θ-multiple). Combined with X ≥ 60°: if θ < 60° then X ≥ 60° > θ; if θ = 60° (N=3) then X ≠ 60° (excluded) and X ≥ 60°, so X > 60° = θ. Either way θ < X strictly, so γ < θ < X, i.e. **γ ∈ (0, X)**. For the P-angles: write Y = mθ + r_Y, m = ⌊Y/θ⌋ ≥ 0. Then Y + γ = (m+1)θ. Need (m+1)θ < 180° = Nθ, i.e. m ≤ N−2. Now Y < 180° − X (since Z > 0) and X ≥ 60° give Y < 120°; and θ ≤ 60° gives 180° − θ ≥ 120°; hence Y < 120° ≤ 180° − θ, so Y/θ < N − 1, giving m ≤ N − 2. ✓ So child 2 P-angle (m+1)θ ∈ [θ, (N−1)θ] ⊂ (0°,180°); child 1 P-angle (N−m−1)θ ∈ [θ, (N−1)θ] ⊂ (0°,180°). Remaining angles: γ ∈ (0°,θ); Y, Z are angles; X − γ > X − θ > 0. All six child angles in (0°,180°). ✓

**(B) N = 2 (θ = 90°).** θ-multiples = {90°}; "no θ-multiple" = no angle = 90°. At most one angle exceeds 90° (two would sum > 180°), and none equals 90°, so the angles > 90° form a set of size ≤ 1; the largest angle X is that one if it exists, otherwise all three are < 90°. Either way both Y, Z < 90°. Pick Y: r_Y = Y, γ = 90° − Y ∈ (0°, 90°). Validity: γ < X ⇔ X + Y > 90° ⇔ Z < 90° ✓; Y + γ = 90° ∈ (0°,180°); 180° − Y − γ = 90° ∈ (0°,180°); X − γ = X + Y − 90° = 90° − Z > 0 (Z < 90°) ✓. Both children have 90°; Mulan wins on the next check, 1 move total.

Cases (A), (B) are exhaustive (N integer ≥ 2 ⇒ θ ∈ {90°} ∪ {≤ 60°}) and disjoint. The create-move is always valid; both children carry a θ-multiple.

#### I.3 Phase 2 — k-descent
The surviving child has a θ-multiple kθ at its P-vertex, 1 ≤ k ≤ N−1 (in Case A, k = m+1 ≤ N−1; in Case B, k = 1). If k = 1, that is θ and Mulan wins at the next check. If k ≥ 2, set X := kθ and split with γ = θ (adjacent to Y):
- child 1 = (θ, Y, 180° − Y − θ) — carries **θ** at the split vertex;
- child 2 = ((k−1)θ, Z, Y + θ) — carries **(k−1)θ** at the split vertex.

*Validity.* γ = θ ∈ (0, X) since k ≥ 2. Child 1: 180° − Y − θ > 0 ⇔ Y < 180° − θ; Y ≤ Y + Z = 180° − kθ ≤ 180° − 2θ < 180° − θ ✓ (Z > 0 makes Y < Y+Z strict). Child 2: (k−1)θ > 0 (k ≥ 2); Y + θ < 180° ⇔ Y < 180° − θ ✓. All other angles visible. ✓

*Monovariant.* Child 1 carries θ (index 1) → Mulan wins next check. Child 2 carries (k−1)θ (index k−1 < k). To delay, Shan-Yu keeps child 2; the θ-multiple index strictly decreases k ↦ k − 1.

*Termination.* From k ≤ N−1, after at most N−2 descent steps the index reaches k = 2. At k = 2: child 1 = (θ, Y, …) and child 2 = ((2−1)θ, Z, Y+θ) = (θ, Z, Y+θ) — **both children carry θ**. Whichever Shan-Yu keeps, the next check fires.

#### I.4 Total move bound
Phase 1: 1 move (wins immediately in Case B). Phase 2: at most N−2 descent moves. Total **≤ N − 1 moves**, finite and independent of Shan-Yu's choices. (The mod-θ arithmetic uses only Nθ = 180° and residues mod θ; θ need not be an integer number of degrees — e.g. θ = 180°/7 works verbatim, residues in ℝ/(180°/7)ℤ, k integer in {1,…,6}.) ∎

---

### II. ONLY direction — 180°/θ ∉ ℤ ⇒ Shan-Yu wins

Write 180° = qθ + r, q = ⌊180°/θ⌋ ≥ 1, r ∈ (0°, θ) (r ≠ 0 is exactly the hypothesis 180°/θ ∉ ℤ). An angle a ∈ (0°,180°) is a θ-multiple iff a ≡ 0 (mod θ) (i.e. a ∈ {θ, 2θ, …, qθ}, a finite set). Note **180° ≡ r ≢ 0 (mod θ)**.

#### II.1 Shan-Yu's invariant
**(I):** *no angle of T is a θ-multiple* — equivalently all three angle-residues (mod θ) are nonzero. Since θ is a θ-multiple, (I) ⇒ no angle equals θ: maintaining (I) prevents the stopping condition forever.

#### II.2 Shan-Yu's initial triangle (existence)
Forbidden angle-values (θ-multiples in (0°,180°)) = {θ, 2θ, …, qθ}, **finite** (q = ⌊180°/θ⌋, qθ < 180° because r > 0). In the open 2-simplex Δ = {(A,B) : A > 0, B > 0, A+B < 180°}, the bad locus where some angle is a θ-multiple is
$$\mathcal{L} = \bigcup_{k=1}^{q}(\{A=k\theta\} \cup \{B=k\theta\} \cup \{A+B=180°-k\theta\}),$$
a finite union of lines, hence empty interior. Δ is open and nonempty with nonempty interior, so Δ ⊄ ℒ, i.e. Δ \ ℒ ≠ ∅ (open, dense, full measure). Pick (A₀, B₀) ∈ Δ \ ℒ, set C₀ = 180° − A₀ − B₀; none of A₀, B₀, C₀ is a θ-multiple. Shan-Yu opens with T₀ = (A₀, B₀, C₀), satisfying (I). ✓ (Uniform over all non-unit-fraction θ — rational or irrational — since only finiteness of {kθ < 180°} is used.)

#### II.3 Maintenance of (I) — the four-case obstruction
Assume T = (X, Y, Z) satisfies (I): X, Y, Z ≢ 0 (mod θ). Mulan makes any legal move (any split vertex, any γ ∈ (0, X)). Relabel so she splits X with γ adjacent to Y; children (by the transform): child 1 = (γ, Y, 180° − Y − γ), child 2 = (X − γ, Z, Y + γ).

**Claim.** It is impossible for **both** children to contain a θ-multiple. Hence at least one child satisfies (I), and Shan-Yu keeps that child.

*Proof by contradiction.* Suppose both children contain a θ-multiple. In child 1 the slot Y is nonzero mod θ by (I), so a θ-multiple occurs in slot γ or slot (180° − Y − γ). In child 2 the slot Z is nonzero by (I), so a θ-multiple occurs in slot (X − γ) or slot (Y + γ). The condition "both children contain a θ-multiple" is the disjunction (over 2×2 = 4 conjunctions); ruling out each conjunction rules out the disjunction (exhaustive by the distributive law; cases need not be disjoint). All congruences mod θ:

1. **γ ≡ 0 ∧ (X − γ) ≡ 0.** Then X ≡ γ + (X − γ) ≡ 0, contradicting X ≢ 0. ✗
2. **γ ≡ 0 ∧ (Y + γ) ≡ 0.** Then Y ≡ (Y + γ) − γ ≡ 0, contradicting Y ≢ 0. ✗
3. **(180° − Y − γ) ≡ 0 ∧ (X − γ) ≡ 0.** The first gives Y + γ ≡ 180° ≡ r; the second gives γ ≡ X. Hence X + Y ≡ r. But X + Y + Z ≡ 180° ≡ r, so Z ≡ r − (X + Y) ≡ 0, contradicting Z ≢ 0. ✗
4. **(180° − Y − γ) ≡ 0 ∧ (Y + γ) ≡ 0.** The first gives Y + γ ≡ 180° ≡ r; the second gives Y + γ ≡ 0. Hence r ≡ 0 (mod θ), contradicting r ∈ (0°, θ). ✗

All four fail; therefore no γ makes both children carry a θ-multiple. At least one child satisfies (I); Shan-Yu keeps it. (I) is maintained for every Mulan move. ∎

#### II.4 Shan-Yu wins
Shan-Yu opens with a triangle satisfying (I) (II.2) and, after every Mulan move, keeps a child still satisfying (I) (II.3). Since (I) excludes any angle equal to θ, the stopping condition is never met, for any Mulan strategy. Mulan cannot guarantee victory. ✓

---

### III. Combining both directions
- IF (§I): θ = 180°/N (N ≥ 2) ⇒ Mulan wins in ≤ N−1 moves.
- ONLY (§II): 180°/θ ∉ ℤ ⇒ Shan-Yu has an (I)-preserving strategy preventing θ forever.

The two conditions are complementary and exhaustive over θ ∈ (0°, 180°): "180°/θ ∈ ℤ and ≥ 2" ⇔ "θ = 180°/N for some integer N ≥ 2" (θ < 180° ⇒ N ≥ 2; θ > 0° excludes N = ∞).

**Therefore: Mulan guarantees victory in finitely many steps, regardless of how Shan-Yu plays, if and only if θ = 180°/N for some integer N ≥ 2.** ∎

## Problem statement
Shan-Yu and Mulan are playing a game. Let θ be an angle with 0°<θ<180° known to both players. Initially, Shan-Yu makes a paper triangle T with measurements of his choice. Then, they repeatedly perform the following steps: If T has at least one angle measuring exactly θ, then the game stops and Mulan wins. Otherwise, Mulan chooses a point P on the perimeter of T, different from its three vertices. She then makes a straight cut from P to the opposite vertex of T, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new T. For which real values of θ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?
