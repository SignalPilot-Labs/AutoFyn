# Proof-reviewer — round 4 — imo-2026-03 (IMO 2026 P3)

Two approaches built; independent verdict each. Neither is a solve — the problem stays `partial`.

---

## Approach: direct-constructive

**Verdict: CHANGES REQUESTED. True Status: partial (builder's recorded Status is correct — honest).**

Scores: Correctness 9/10 · Completeness/rigor 6/10 (real gaps, honestly flagged) · Progress 7/10.

### What I verified independently
- **Spare-R_n generalisation (§4.1).** R_n = 2^n/D; every other final piece is an uncut R_j
  (≤ 2^{n−1}/D) or a strict sub-piece (< 2^j/D), all < 2^n/D, so R_n is the unique max ⟹ r_1 = 2^n/D
  ⟹ O ≥ r_1. Correct and fully general. **Certified** (see lemmas).
- **Δ-reduction to (★) (§4.2.6, §4.4).** A = μ{N odd} is continuous and piecewise-affine on the
  compact simplex Δ (n+1 fragments summing to 2^n, the ≤ n+1 count built into the dimension). Minimum
  of a continuous piecewise-affine function over a polytope is attained at a vertex of the
  hyperplane-arrangement-refined cell complex (point with n independent tight constraints) — standard
  and correct. So "lower bound ⟺ (★): A(vertex) ≥ 1" is a valid REDUCTION. The interleaving cell
  (A ≡ 1) and all a=1 vertices (top-fragment cascade §4.2.4) are genuinely closed. The load-bearing
  claim that ≤ n+1 fragments is essential is honest (with n+3 fragments min A drops to ≈0). The
  merge of L1 and L2 into the single (★) is a genuine simplification and is correctly argued.
- **IH(1),IH(2),IH(3) of B1-large (§6.2).** Verified the algebra. IH(3) doubly-hard leaf
  |b_1−b_2−b_3| < 1/D from the sum bound S < 7/D and gaps > 1/D: both sub-cases (b_1 ≥ b_2+b_3 gives
  b_1−b_2−b_3 < 4/D−3/D = 1/D; b_1 < b_2+b_3 gives S−2b_1 < 7/D−6/D = 1/D) are correct, cases
  exhaustive and disjoint. Machine-checked 0 fails over 10^5 hard configs. Correct.
- The load-bearing merge slogan the builder itself flagged ("A = 1 + 2Σ(I_k−f_j)" global-vs-local
  hazard): the ACTUAL argument used is the Δ-vertex reduction + cascade, NOT that slogan, and it is
  sound. No hidden circularity (the dropped integral ‡ is correctly identified as identical to
  2^n − O and is not load-bearing).

### Gaps that remain (block `solved`, honestly flagged — NOT overclaimed)
1. **(★)** — A ≥ 1 at a=0 *clustered* vertices of Δ. This is the whole lower bound now; only a
   local-min (Lemma S) is proven, the global min is open. Numerically min_Δ A = 1 (n≤5) but no
   config-independent certificate. **This is a reduction, not a proof.**
2. **U1 = Case-B hard regime** — general IH(q≥4) pair-creation step (B1-large, only q≤3 proved) and
   **B2 entirely open** (no explicit strategy with ≤ n budget). Case A (Lemma H) and easy Case-B
   sub-cases (Reductions 1–2) are closed.

Route: re-dispatch the builder to close (★) at a=0 clustered vertices (now a finite vertex
inventory via the fragment-count bound — a per-cell LP lower bound may crack it) and the general
IH(q)/B2. The approach is right; the walls persist.

---

## Approach: caseB-matching

**Verdict: RETHINK. True Status: unsolved as framed (core mechanism refuted). Builder's recorded
Status `partial` overstates the approach — its distinctive mechanism is dead; I record dead-end.**

Scores: Correctness 8/10 (salvaged lemmas correct; core lemma correctly refuted) ·
Completeness 3/10 (no path to Case B from this framing) · Progress 5/10 (3 certifiable reductions).

### Core lemma refuted — I reproduced the counterexample independently
Lemma M ("finite matching menu forces A ≤ 1/D") is **FALSE**. Exact rational check of
n=3, a = (5144, 2787, 1386, 683)/10000:
- sum = 1, all pieces > 1/15, all consecutive gaps (0.2357, 0.1401, 0.0703) > 1/15 — a hard-regime
  Case-B config. ✓
- My own exhaustive menu search (all matchings × halve/keep, budget ≤ 3, `fractions.Fraction`):
  **best menu A = 683/10000 ≈ 0.0683 > 1/15 ≈ 0.0667.** ✓ (attained by keep a_4, halve a_1,a_2,a_3)
- Fragment cascade (cut a_1 at a_2, residual at a_3; 2 cuts): pieces {a_1−a_2−a_3, a_4} plus
  cancelling copies ⟹ **A = 288/10000 ≈ 0.0288 ≤ 1/15.** ✓

So the theorem (Case-B bound with general cuts) is true, but the menu framing cannot reach it. The
approach's induction-free selling point does not exist; it collapses onto direct-constructive's
fragment-cascade wall (U1). Correct diagnosis by the builder.

### Salvaged lemmas — verified and CERTIFIED (general n)
All three verified in exact rational arithmetic:
- **Lemma X (XOR/parity evaluator + cut toggle).** A = μ(⊕_i [0,ℓ_i]); cutting ℓ into (m,ℓ−m),
  m ≤ ℓ/2, toggles the A-set by [0,m] ∪ (ℓ−m,ℓ] (measure 2m). Derived from certified Lemma R.
  A_of{m,ℓ−m} = ℓ−2m confirmed. → `lemmas/X-xor-evaluator.md`.
- **Reduction 1 (halve-all).** p ≤ n pieces ⟹ halve all ⟹ A = 0. Correct. → `lemmas/CaseB-reductions.md`.
- **Reduction 2 (close-pair).** p = n+1, d* = min consecutive gap ≤ 1/D ⟹ pair closest (1 cut) +
  halve rest (p−2 cuts) = n cuts ⟹ A = d* ≤ 1/D. Verified A = d* exactly over 2000 random configs
  at n=3,4. → `lemmas/CaseB-reductions.md`.
- The **Spare-R_n lemma** (from direct-constructive) is certified in the same file.

Together with Case A (Lemma H), these reduce the Case-B upper bound to the single **hard regime**
(p = n+1, all pieces AND all consecutive gaps > 1/D) for all n. That is real, reusable progress —
but the approach's own mechanism cannot cross it, hence RETHINK. Route: retire the matching-menu
framing; either re-plan a fragment-based finite optimisation (a strictly-richer "cascade menu") or
concentrate Case-B effort on direct-constructive's Lemma I / IH(q) on the hard regime. The field
has again collapsed to one framing at the U1 wall — the outliner should introduce a genuinely
different Case-B framing (away from the graveyard AND away from cascade menus if they re-hit U1).

---

## Recorded outcomes (record_outcome, round 4)
- direct-constructive → **advanced** (L1+L2 merged into single vertex inequality (★); spare-R_n
  generalized; IH(1,2,3) proven; (★) a=0 vertices + IH(q≥4)/B2 still open).
- caseB-matching → **dead-end** (Lemma M refuted by exact n=3 counterexample; menu framing
  insufficient; salvaged+certified Lemma X, Reduction 1, Reduction 2).

## Certified into lemmas/
`X-xor-evaluator.md` (Lemma X), `CaseB-reductions.md` (Reduction 1, Reduction 2, Spare-R_n).
Not written as standalone files (stay in approach, tied to open gaps): the Δ-reduction to (★) and
the IH pair-creation leaves q≤3 — correct but not self-contained importable theorems.

## current.md
Updated (I own it). Status stays **partial**. Recorded the caseB refutation + certifications and
the round-4 lower-bound reduction to (★). Answer c(n) = 2^n/(2^{n+1}−1) stands (n=1,2 fully proven,
n=3 consistent). Both walls — (★) at a=0 clustered vertices (lower) and the Case-B hard regime
(upper) — remain the blockers to `solved`.
