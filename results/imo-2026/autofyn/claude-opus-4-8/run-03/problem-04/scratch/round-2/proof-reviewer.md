# Proof review — imo-2026-04 (Mulan's Triangle Game), Round 2

Answer under review: **Mulan wins ⟺ θ | 180°** (θ = 180/n, n≥2 integer). I independently
re-derived the whole characterization from scratch (one-cut algebra, 4-case covering,
double-plant, descent) and brute-verified both load-bearing computations over ~20k–30k random
cases per θ with **0 failures**. The answer is correct.

## Independent verification of the load-bearing steps

**One-cut algebra.** For apex α split into x, α−x: child₁={x,β,180−x−β}, child₂={α−x,γ,x+β},
the two P-angles supplementary. Matches both proofs exactly.

**Necessity / Covering Lemma (the crux).** With α,β,γ off-lattice and θ∤180: child₁ on-lattice
⟺ x≡0 or x≡180−β; child₂ on-lattice ⟺ x≡α or x≡−β (mod θ). The 2×2 = 4 combinations are the
*complete* case set (β,γ each excluded as the on-lattice angle leaves exactly two options per
child), and they collapse to α≡0, β≡0, γ≡0, 180≡0 respectively — every one excluded. I checked
all 3×3 angle-choice combinations reduce to these 4 (β and γ options are killed by hypothesis),
so the exhaustion is genuine, not a convenient subset. x is treated as a real parameter; only
α+β+γ=180 and the off-lattice/θ∤180 hypotheses are used. Symmetry over the three apex choices is
valid. Start triangle (θ/2, θ/2, 180−θ) is valid and off-lattice iff θ∤180 — correct. Brute
check across θ∈{40,50,70,25,80,100,180/7,140,17,23.3}: 0 covering failures.

**Sufficiency / Double-plant + descent.**
- Plant x=(⌊β/θ⌋+1)θ−β lands in (0,θ]⊂(0,α) at the largest vertex (α>θ shown correctly,
  incl. the θ=60 equilateral edge case). x+β=mθ and 180−x−β=(n−m)θ are both positive multiples
  of θ (uses 180=nθ), 1≤k≤n−1 — verified, brute check 0 failures across θ|180 set.
- Descent from kθ (k≥2): cut x=θ ⟹ child₁ has angle θ (win if kept), child₂ has (k−1)θ.
  Shan-Yu has no safe alternative (only two children, both analyzed); multiplier strictly drops
  by 1, terminating at θ in ≤k−1 steps. At k=2, child₂=(θ,γ',θ+β') also carries θ (both proofs
  handle this). Non-degeneracy of the survivor checked. Finite, ≤ n−1 total moves.
- θ=90 (n=2): altitude cut x=90−β at a vertex with two acute neighbours; both children get a
  90° angle; foot interior since base angles acute. Correct one-move win.

**Answer + refutations.** Set {180/n : n≥2} stated and verified. "θ≤90 suffices" refuted (θ=40
loses), "θ|90" refuted (θ=60|180 wins). Both present in both proofs.

## Per-approach verdicts

### lattice-invariant-180 — APPROVE (Status: solved)
Complete and rigorous. Covering Lemma with full 4-case exhaustion; sufficiency with explicit
plant, forced descent, non-degeneracy, and move bound n−1; both wrong conjectures refuted.
Every case settled, no hand-waving, θ=90 and θ=60 boundaries handled. Builder's recorded Status
`solved` is correct.
- Correctness 10/10, Completeness/rigor 10/10, Progress: full solution (from partial).

### angle-sum-anchor — APPROVE (Status: solved)
Independent, self-contained proof of the same result. Covering Lemma (same 4-case exhaustion,
labeled a/b/c), Double-plant Lemma stated generally and applied, measure-zero base-case argument
for existence of an off-lattice start triangle (rigorous: F is a finite union of segments,
measure zero in the 2-simplex, so the complement is nonempty), plant-then-descend with the k=2
bisection handled explicitly, move bound n−1. Answer tabulated and both conjectures refuted.
Builder's recorded Status `solved` is correct.
- Correctness 10/10, Completeness/rigor 10/10, Progress: full solution (from partial).

Both are genuinely gap-free; they share the covering computation, which I found no flaw in, and
each presents it fully in its own file, so both stand independently.

## Lemma certification
- `lemmas/lattice-covering.md` — **CERTIFIED**. Statement matches what is proved, proof is
  sorry-free, 4-case exhaustion complete, no stronger than proved. Status line updated to
  CERTIFIED.
- Supplementary-plant / Double-plant and Descent lemmas (flagged promotable inline) are also
  correct as stated, but no separate lemma files were created for them; not blocking.

## Actions taken
- Wrote `results/imo-2026-04/current.md`: Status `solved` + Full proof.
- Certified `lemmas/lattice-covering.md`.
- Recorded both outcomes as `verified-milestone` via the ranker.
