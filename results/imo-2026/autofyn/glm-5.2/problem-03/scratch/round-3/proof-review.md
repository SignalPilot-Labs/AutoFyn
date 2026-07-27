# Proof review — imo-2026-03 (round 3, L(2) closure claim)

## Verdict: CHANGES REQUESTED
## Status: partial (unchanged — already `partial` in results file; do NOT raise to `solved`)

## Scores
- Correctness: 4/5 (the L(2) inequality D ≥ 1 is correct; one stated claim is false — see defect)
- Completeness/rigor: 4/5 (case decomposition complete; interiors covered by direct per-region linear-form bounding; equality overclaim)
- Progress: high — L(2) lower bound is now genuinely rigorous; c(2) ≥ 4/7 stands

## What is correctly established (verified)

1. **L(2) inequality D ≥ 1 is rigorously proved.** I independently re-derived every sub-case and ran a 2,000,000-sample random sweep plus per-case grids (B0/B1/B2/B3/Case A): **0 violations**, min D = 1.0. The case decomposition by k = (# cuts on piece 4) ∈ {0,1,2} is exhaustive:
   - k=0 → Case A (tail gets 0–2 cuts; b₁=4, b₂≤2 ⇒ D≥2≥1). ✓
   - k=1 → B0 (tail intact), B1 (cut on 2), B2 (cut on 1). ✓
   - k=2 → B3 (tail intact). ✓
   Degenerate cuts correctly folded into the case with one fewer cut. The largest fragment M = 4−m ≥ 2 ≥ every tail piece, so b₁ = M (or b₁=2 in B3's f₁<2 sub-branch) — this ordering claim is correct and the proof uses it properly.

2. **Interiors are covered, not just breakpoints.** The L(2) proof does NOT rely on the breakpoint/vertex-min principle; instead, within each region of fixed sorted order it writes D as an explicit linear form in (m, p, q, …) and bounds it using the parameter constraints (0 < m ≤ 2, 0 < p ≤ 1, etc.). The regions partition the full parameter box and each is bounded on its closed domain, so interiors are settled. This is a legitimate (stronger) alternative to the outline-reviewer's vertex-min route. The outline-reviewer's three conditions (complete breakpoints / vertex-min / degenerate vertices) are therefore not strictly required for L(2) because the direct per-region bounding subsumes them.

3. **Parity fix for n=1 is correct.** r₀(t) = #{1,2 ≥ t}: r₀=2 (even) on (0,1], r₀=1 (odd) on (1,2], so D₀ = |(1,2]| = 1 = 2−1. The proof's text matches this ("r_0 equals 2 (even) on (0,1] … 1 (odd) on (1,2]") and explicitly flags the outline's backwards statement. ✓

4. **Toggle-pair (Lemma T) is sound.** Δr = +1 on (0,m], 0 on (m,M], −1 on (M,s] re-derived from differencing the before/after indicator contributions. Halving (m=M=1, s=2): +1 on (0,1], −1 on (1,2] sends r 2→3 on (0,1] and 1→0 on (1,2], D=1. ✓ The false "r_final = r₀ + R" mnemonic is correctly repudiated.

5. **General Case B / L(3) merge / U(2) / general U(n) are honestly flagged OPEN.** "Hard toggle lemma (general Case B — OPEN, not claimed)" (§B-bis), L(3) "merge sub-cases … not closed here" (§B-4), U(2) "framework (not closed)" (§C-2), general U(n) "open" (§C). No overclaim of solvedness there.

## DEFECT — the equality characterization is FALSE (must fix)

The proof states (§B-3 conclusion and Current-best item 4):

> "with equality iff XY halves (4 → 2+2 and, if the second cut hits 2, 2 → 1+1), i.e. the full-halving equality case."

and the Approaches-tried entry:

> "every region giving D ≥ 1, equality only at full halving."

This is **wrong**. D = 1 is attained at many configurations that are NOT full halving. Verified counterexamples (all give D = 1 exactly):

- **B0, 1 cut only, m ∈ [1,2):** 4 → (m, 4−m), tail {2,1} intact. For m=1.5: pieces {2.5, 2, 1.5, 1}, D = 2.5−2+1.5−1 = 1. The proof's own B0 sub-line "1 ≤ m < 2: … D = M−2+m−1 = 1" computes D = 1 for the *entire* interval m ∈ [1,2), contradicting "equality only at full halving" two paragraphs later.
- **B1, region (i), m = 2, any p ∈ (0,1]:** 4 → 2+2 and 2 → (p, 2−p) with p ≠ 1 (not full halving). E.g. p=0.3: pieces {2,2,1.7,1,0.3}, D = 2−2+1.7−1+0.3 = 1. The proof explicitly notes "Equality at m = 2" without restricting p.
- **B3, f₁ ≥ 2, f₂ ≥ 1 (whole region):** two cuts on 4 giving fragments (f₁,f₂,f₃) with f₁≥2, f₂≥1, f₃≤1, tail intact. E.g. 4 → (2, 1.5, 0.5): pieces {2, 2, 1.5, 1, 0.5}, D = 2−2+1.5−1+0.5 = 1. The proof's sub-line "D = (f₁+f₂+f₃) − 3 = 1" is identically 1 on this entire region, which is NOT full halving (full halving for G₂ uses the two cuts on DIFFERENT pieces 4 and 2, not both on 4).

So "equality iff full halving" is an overclaim. The rigor rules explicitly forbid presenting an unproven/false claim as established; overclaiming is worse than admitting a gap.

**Why this does not sink the main bound.** c(2) ≥ 4/7 needs only D ≥ 1 (which is proved) plus existence of an attaining configuration. Full halving {2,2,1,1,1} does attain D = 1, so the lower bound c(2) ≥ 4/7 is fully justified. The defect is purely the "iff / only" wording.

## Required fix

Replace the equality claim in §B-3 (and the Approaches-tried / Current-best text) with something accurate, e.g.:

> "with equality attained in particular at full halving (4 → 2+2 and 2 → 1+1, giving {2,2,1,1,1} with D = 1); equality also occurs in other configurations (e.g. B0 with m ∈ [1,2], and B3 with f₁ ≥ 2, f₂ ≥ 1). The bound D ≥ 1 is tight, so rescaled c(2) ≥ 4/7."

This is a textual correction; no casework computation needs to change. After this fix, the L(2) lower bound (D ≥ 1, hence c(2) ≥ 4/7) is rigorous and the partial Status is honest.

## Other minor notes (non-blocking)

- §B-3 Case A also covers "1 or 2 cuts on the tail"; the b₂ ≤ 2 argument is valid but the proof could note that fragments of 2 are ≤ 2 and fragments of 1 are ≤ 1, so the second-largest piece is ≤ 2 — already implicit, fine.
- The "verified by continuous optimal-XY search" lines for L(3), L(4), L(5) are correctly labelled as numerical confirmation, not proof. Good.
- The equality case at the very end of §C-2 (U(2)) is fine as stated ("attained numerically, and at the LB geometric partition").

## Summary

The load-bearing claim — **L(2): every ≤ 2-cut refinement of G₂ = (1,2,4) has alternating sum D ≥ 1, hence c(2) ≥ 4/7** — is rigorously and correctly proved by exhaustive casework; I independently verified every sub-case algebraically and numerically (0 violations over 2M+ samples and dense grids). The case decomposition is complete, interiors are covered by direct per-region linear-form bounding (subsuming the outline's vertex-min requirement), the n=1 parity fix is correct, and the toggle-pair (T) is sound. General Case B, L(3) merge, U(2), and general U(n) are honestly flagged open. The single defect is the **false equality characterization** ("equality iff full halving"); it must be corrected to "attained at full halving (and elsewhere)". Status remains `partial`; verdict CHANGES REQUESTED pending that textual fix.
