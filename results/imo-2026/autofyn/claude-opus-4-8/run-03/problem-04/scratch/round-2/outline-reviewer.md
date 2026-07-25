# Outline review — round 2 — imo-2026-04 ("Mulan's Triangle Game")

## Headline verdict
The characterization **Mulan wins ⟺ θ | 180°** (θ = 180/n, n ≥ 2) is CORRECT. I
independently verified both load-bearing computations; the round-1 "θ ≤ 90" conjecture is
genuinely refuted. Both proof directions have sound, essentially complete skeletons. The
three approaches are all valid whole-problem attempts, but they are **not independent
cross-checks** — they share one identical load-bearing computation (the mod-θ covering
lemma). That shared gap is, however, already CLOSED (verified below), so the usual
single-gap-trap risk does not bite this round.

## Verification I ran (the gate's own checks)
- **Necessity covering (the crux), θ∤180.** For 20k+ random triangles with all angles
  ∉ θℤ, over all 3 cut-vertex choices and 30 sampled x each, at least one child always had
  ALL angles ∉ θℤ — i.e. Shan-Yu always has a safe child, for every x Mulan picks. Zero
  failures for θ = 40, 50, 70, 25, 80, 100, 7. This confirms the invariant holds for ALL x
  (the exact worry flagged in the dispatch: x is Mulan's continuous parameter, and the
  covering must cover every x — it does).
- **The 4-case exhaustion is genuinely exhaustive.** "Both children bad" = (x≡0 ∨ x≡180−b)
  ∧ (x≡a ∨ x≡−b) mod θ; the four products force a≡0, b≡0, c≡0 (via a+b≡180 ⟹ c≡0), or
  180≡0. First three contradict I; the fourth needs θ|180. No fifth case exists — it is an
  AND of two two-way ORs, so exactly four products. Airtight.
- **Sufficiency double-plant, θ|180.** For 3k+ random off-lattice triangles per θ, cutting
  the largest vertex with x ≡ −b (mod θ) put a positive θ-multiple in BOTH children. Zero
  failures for θ = 90, 60, 45, 36, 30, 20, 180/7.
- **θ=90 altitude edge.** For 200k random triangles with no 90° angle, an interior-altitude
  option (a vertex whose two other angles are both acute) always exists. Zero failures.

## Per-approach verdicts

### lattice-invariant-180 — APPROVE (primary)
Most complete: both directions written out end-to-end targeting the full claim.
- Necessity is correct and essentially done (the covering + base + induction).
- Sufficiency (plant → forced descent → θ) is correct. Note the descent reaches an angle of
  exactly θ directly via one more forced plant at 2θ (keeps {θ, γ, θ+β}), so Lemma 0 /
  the explicit "bisect 2θ" finish is auxiliary, not load-bearing for correctness — builder
  need not sink effort into the full 6-sub-case Lemma 0 (G5) unless it wants the cleaner
  narrative.
- Fixable gaps to close while building (CHANGES-level, not blockers):
  - G1: give one explicit legal starting triangle with all angles ∉ θℤ, and state clearly
    that necessity = "there EXISTS a Shan-Yu start + discard rule avoiding θ forever."
  - G2 boundary a=θ (θ=60): resolve by noting the game only continues when no angle equals
    θ, so the largest angle a is strictly > 60 = θ (equilateral is the sole a=60 case and it
    already has angle 60 = θ, an immediate win). Hence (0,a) has length > θ and contains an
    open-interval representative of x ≡ −b (mod θ). State this explicitly.
  - Non-degeneracy of both children (all angles in (0,180)) at the plant and each descent
    step — quick to write, must be shown, not asserted.

### angle-sum-anchor — APPROVE (build; owns the compute_and_prove answer requirement)
Reaches the same answer; its genuine added value is J3: the explicit answer-set tabulation
{180/n : n ≥ 2} = {90, 60, 45, 36, 30, …} with verification, plus the explicit refutation of
BOTH wrong conjectures (θ≤90 via θ=40 loss; θ|90 via θ=60 win). This is a rigor requirement
(answer_type = characterization / compute_and_prove) and is best owned here.
- Required change (per its own J1): the write-up MUST rest on the covering computation, NOT
  on the "only guaranteed residue is 180's" heuristic. The "anchor" language is intuition,
  not proof — as the file itself admits. Builder must import/prove the covering lemma and
  present it as the load-bearing step; do not hand the reviewer the anchor narrative as if it
  were the argument.

### reduce-to-2theta — APPROVE but NOT in this round's build set (registered, live alternate)
Correct and cleanly framed (reduce to forcing 2θ; boolean potential Φ + monovariant m giving
the explicit finite move bound ≤ 180/θ — a nice rigor touch). But it is the **most redundant**
of the three: its Flip lemma IS the covering lemma, its Descent lemma IS the sibling's descent,
and its Lemma 0 (the 6-sub-case reduction, H1) is its heaviest unproven piece yet is only
needed for its own framing. It re-narrates the same proof rather than providing an independent
verification path. Keep it live in the population; do not spend a parallel builder on it this
round.

## Diversity note for the orchestrator
All three approaches share ONE load-bearing computation (lemmas/lattice-covering.md, the 4-case
mod-θ covering). They differ only in narration (invariant defense vs 2θ-reduction+potential vs
angle-sum-anchor), not in the actual hard step. This is the "too close, one wall" pattern
CLAUDE.md warns about — but here the wall is already down (I verified the covering by hand and
computation), so it is not a risk this round; it just means building all three buys little
extra assurance. The right move is one clean complete write-up (lattice-invariant-180) plus one
that owns the explicit answer verification (angle-sum-anchor). No genuinely different framing is
needed because the problem is essentially solved; the remaining work is rigor/edge-case detail.

## Shared lemma
lemmas/lattice-covering.md does not yet exist. The primary builder should create and prove it:
"If a,b,c ∉ θℤ and θ∤180, then for every cut vertex and every x∈(0,a) at least one child has
all angles ∉ θℤ." Proof = the verified 4-case argument above. Once the reviewer certifies it,
angle-sum-anchor imports it (satisfies its J1).

## Ranking (this round)
lattice-invariant-180 (1531) > reduce-to-2theta (1486) ≈ angle-sum-anchor (1483).
lattice-invariant-180 leads on completeness; angle-sum-anchor and reduce-to-2theta drawn
(anchor owns answer verification but leans on heuristic; reduce has cleaner logic but a heavier
own Lemma 0 and is the most redundant).

build set: lattice-invariant-180, angle-sum-anchor
