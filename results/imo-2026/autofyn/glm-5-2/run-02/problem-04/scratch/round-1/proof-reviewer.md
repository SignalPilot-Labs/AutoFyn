# proof-reviewer — IMO 2026 P4 (Mulan's triangle game), round 1

Target characterization: **Mulan wins ⇔ θ = 180°/N for some integer N ≥ 2.**

I independently re-derived the angle-triple transform, the create-move validity, the k-descent monovariant, and the four-case obstruction from scratch, and verified each numerically (python3):
- Angle-triple transform: confirmed (children sum to 180°, P-angles supplementary).
- IF create-move + k-descent: for N ∈ {2,3,4,5,7,8,11,13,17,19,23,99}, 200 random triangles each, all moves legal and both children carry a θ-multiple; worst-case move count = N−1 exactly (Shan-Yu always picks larger-index child).
- ONLY four-case obstruction: 0 escapes across 13 θ values — rational {72,100,50,7,13,40,135,36.5,60.0001,17.5,170}° and irrational {180/π, 50√2}° — 5000 γ-steps each.

---

## mod-theta-descent — verdict: APPROVE, Status: solved

**Correctness.** Every load-bearing step verified:

1. **Angle-triple transform (§0).** Direct angle chase; child 2's P-angle = 180° − (X−γ) − Z = Y + γ using X+Y+Z=180°. Correct. The supplementary-pair corollary (the two P-angles sum to 180°) is the structural fact the four-case obstruction leans on.

2. **IF create-move (§I.1–I.2).** γ = θ − (Y mod θ) ∈ (0°,θ). Both children's P-angles are θ-multiples by construction (child 2: Y+γ ≡ 0; child 1: 180°−Y−γ ≡ 180° ≡ Nθ ≡ 0). Validity casework is exhaustive and disjoint: N≥3 (θ≤60°) vs N=2 (θ=90°). The "θ strictly between 60° and 90°" concern is vacuous — N is an integer ≥2, so θ ∈ {90°} ∪ {≤60°}. Case A (N≥3): X ≥ 60° and X ≠ θ when θ=60° (excluded as a θ-multiple), so θ < X strictly, giving γ < X; Y < 120° ≤ 180°−θ gives m = ⌊Y/θ⌋ ≤ N−2, so both P-angles (m+1)θ and (N−m−1)θ lie in [θ,(N−1)θ] ⊂ (0°,180°); X−γ > X−θ > 0. All six child angles in (0°,180°). Case B (N=2): both Y,Z < 90° (at most one angle > 90°, none = 90°), γ = 90°−Y, γ < X ⇔ Z < 90° ✓. Both children get 90°. Confirmed for non-integer-degree θ (e.g. 180/7): the mod-θ arithmetic only uses Nθ=180° and residues in ℝ/θℤ.

3. **k-descent (§I.3).** Splitting kθ with γ=θ: child 1 carries θ (index 1, win), child 2 carries (k−1)θ (strict decrease). Validity: γ=θ ∈ (0,kθ) since k≥2; Y < 180°−θ because Y < Y+Z = 180°−kθ ≤ 180°−2θ < 180°−θ (Z>0 makes strict). At k=2 both children carry θ. Total ≤ N−1 moves. Strict monovariant, terminating.

4. **ONLY — initial triangle (§II.2).** Forbidden values {θ,2θ,…,qθ}, q=⌊180°/θ⌋, **finite** (qθ < 180° because r=180°−qθ ∈ (0°,θ)). Bad locus in the open 2-simplex is a finite union of lines (3 families × q lines), empty interior; Δ is open nonempty, so Δ\ℒ ≠ ∅. This is NOT a Kronecker-density issue (we forbid actual angle values kθ, not cosets mod 180°) — the proof correctly avoids that trap. Uniform over all non-unit-fraction θ, rational or irrational.

5. **ONLY — four-case obstruction (§II.3).** The crux. Invariant (I): X,Y,Z ≢ 0 mod θ. The claim "both children contain a θ-multiple" decomposes via the distributive law into a disjunction of 2×2=4 conjunctions (child 1's θ-multiple is in slot γ or slot 180°−Y−γ since Y≢0; child 2's is in slot X−γ or Y+γ since Z≢0). Exhaustive; disjointness is not required (ruling out each conjunction rules out the disjunction). Each case:
   - (γ≡0, X−γ≡0) ⇒ X≡0, contradicts (I). ✓
   - (γ≡0, Y+γ≡0) ⇒ Y≡0, contradicts (I). ✓
   - (180°−Y−γ≡0, X−γ≡0) ⇒ Y+γ≡r and γ≡X ⇒ X+Y≡r ⇒ Z≡r−(X+Y)≡0, contradicts (I). ✓
   - (180°−Y−γ≡0, Y+γ≡0) ⇒ Y+γ≡r and ≡0 ⇒ r≡0, contradicts r∈(0°,θ). ✓
   Cases 3 and 4 use 180°≡r≢0 (mod θ), i.e. the ONLY-regime hypothesis. No escape: an angle could be a θ-multiple in BOTH slots of a child, but the case analysis picks one slot per child — the distributive covering handles overlaps. The failed "group ⊆ ℤ/p" invariant is correctly replaced by (I) "no angle ≡ 0 mod θ"; the distinction is that (I) is a per-angle residue condition, robust to arbitrary γ, while the group-membership condition was not.

**No gaps found.** No hand-waving, no skipped cases, no circularity, no crux-move references to other problems. The answer θ = 180°/N (N ≥ 2 integer) is verified correct: IF direction constructs the winning strategy with explicit bound N−1; ONLY direction constructs Shan-Yu's defense. Both the set and its complement are proved. The build set's headline approach delivers.

**Promotable lemmas certified:** (1) mod-θ four-case obstruction — already in `lemmas/mod-theta-obstruction.md`, marked Certified (statement correct, no stronger than proved, verified independently). (2) Angle-triple transform, create-multiple, k-descent, initial-triangle existence — all proved in-file and correct; the obstruction lemma is the load-bearing one and is now certified for import.

**Outcome recorded:** verified-milestone.

---

## geometric-anchor — verdict: CHANGES REQUESTED, Status: partial

**Correctness.** The dyadic IF subcase (θ = 180°/2^a, a ≥ 1) is proved self-containedly and rigorously:
- Lemma 1 (altitude-foot interior): largest angle A ≥ B,C; if B ≥ 90° then A+B ≥ 180° ⇒ C ≤ 0, contradiction; so B,C < 90°; foot of altitude from A lies interior to BC iff both base angles acute. ✓ Standard.
- Perpendicular-anchor corollary (θ=90° in 1 move): cut from altitude foot F to A; both children ABF, ACF have 90° at F. ✓
- Lemma 2 (bisector step): angle 2θ at V, internal bisector to opposite side gives θ at V in both children. ✓
- Lemma 3 (IH-reuse): a winning decision tree for target τ is a depth-m tree with τ-bearing leaves, executable in any target's game (mechanics are target-independent; only the stop condition changes). ✓ Trivially sound.
- Induction on a: base a=1 (θ=90°, perpendicular anchor, 1 move); step: force 2θ = 180/2^{a−1} via IH (≤ a−1 moves, checking for early θ at each node), then bisect (1 move); total ≤ a moves. ✓

No gaps in what it claims. The scope is honestly stated: GAP-D1 (non-dyadic IF, N with odd factor) and GAP-D2 (entire ONLY direction) are deferred to mod-theta-descent, flagged as shared walls, not overclaimed. This is exactly a clean scoped partial.

**Why CHANGES REQUESTED, not APPROVE.** Status is partial by design — it does not solve the whole problem. The deferrals are honest gaps (not the builder's fault — the synthetic toolkit genuinely cannot reach odd-factor N or Shan-Yu's defense). With mod-theta-descent now SOLVED, the deferrals are resolvable by import: geometric-anchor can be promoted to a full solution by invoking the certified obstruction lemma and the create-move/k-descent for non-dyadic N. The builder should either (a) explicitly import those now-certified pieces and upgrade to solved, or (b) remain a documented insurance partial. Either is acceptable; the current file as-is is a correct partial.

**Promotable lemmas certified:** altitude-foot-interior, bisector-step, dyadic-if — all correct and self-contained. I certify the dyadic-if theorem into `lemmas/dyadic-if.md` as an independent (mod-θ-free) certification of the IF direction for N = 2^a, usable as insurance.

**Outcome recorded:** partial (clean dyadic-IF partial; deferrals GAP-D1/GAP-D2 are honest shared-wall gaps, resolvable now that mod-theta-descent is certified).

---

## Goal progress

**Status: SOLVED.** The target characterization is fully proved both directions by `mod-theta-descent` (reviewer-certified, APPROVE): Mulan wins ⇔ θ = 180°/N for some integer N ≥ 2. The `geometric-anchor` approach is a clean independent certification of the dyadic-IF subcase (partial, CHANGES REQUESTED — may import the certified obstruction + create-move to upgrade). The crux lemma (mod-θ four-case obstruction) is certified into `results/imo-2026-04/lemmas/mod-theta-obstruction.md`. `current.md` is updated with `## Status: solved` and the full proof. Nothing remains for the core problem; the run goal is met.
