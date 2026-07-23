# Build report — residue-divisibility-characterization (round 1)

## What was completed
Full, rigorous proof written to `results/imo-2026-04/approaches/residue-divisibility-characterization.md`, Status: **solved**.

- **Cut model (Lemma 1)** derived from the problem statement in both directions: (a) every legal move is (attacked vertex R, t ∈ (0,R)) yielding children (P, t, Q+R−t) and (Q, R−t, P+t) — with the nondegeneracy and positivity of all six child angles checked; (b) achievability of every t ∈ (0,R) via a continuity/IVT argument on the cut point sliding along the opposite side. Reduction to angle triples stated explicitly (moves and stop condition depend only on the triple).
- **Timing convention** fixed once: stop-check at the start of every round (including round 0), so a child containing θ is a win at the next check.
- **Lemma 2 (GAP A closed):** angle = kθ ⟹ Mulan wins in ≤ k−1 further cuts; full induction, including uniqueness of k and legality of the split t = θ (0 < θ < kθ for k ≥ 2).
- **Lemma 3 (θ = 90 one-cut win):** attack the largest angle R with t = 90−P; legality t ∈ (0,R) reduces to P, Q < 90, proven via "at most one angle ≥ 90" and the R = 90 case being an immediate stop. Both children contain 90.
- **Sufficiency (GAP B closed per reviewer's advice):** n = 2 routed *entirely* through Lemma 3 (no fork patching); the fork claim starts at n ≥ 3, where t₀ ∈ (0, θ) strictly (P ∉ θℤ ⟹ t₀ ≠ 0) and t₀ < θ ≤ 60 ≤ R gives t₀ < R strictly even at θ = R = 60. Both fork children carry a positive multiple of θ (< 180, so k ≤ n−1), and Lemma 2 finishes. Uniform explicit bound: ≤ n−1 cuts for θ = 180/n, all n ≥ 2.
- **Necessity (GAP C closed):** "≡ mod θ" defined as difference ∈ θℤ ⊂ ℝ (subgroup of (ℝ,+)), so irrational θ needs nothing extra. Clean start exists (isoceles family (x, x, 180−2x), finitely many excluded x). Invariant step written once with the relabeling symmetry stated explicitly; the four-case intersection each yields R ≡ 0, P ≡ 0, Q ≡ 0, or 180 ∈ θℤ — all contradictions. Induction on rounds concludes the game never stops.
- **Final answer stated and verified** (Section 4): Mulan wins iff θ = 180°/n, n ≥ 2 integer; dichotomy over all θ ∈ (0,180) checked; smallest instances sanity-verified.

## Remaining gaps
None. `## Spec concerns` section in the approach file records only the two conventions (stop-check timing; meaning of ≡ mod θ) — both fixed in-proof, not gaps.

## Promotable lemmas (for reviewer certification into lemmas/)
- L0: cut model (Lemma 1, both directions).
- L1: θ = 90° one-cut win (Lemma 3).
- L2: angle kθ ⟹ win in ≤ k−1 cuts (Lemma 2).
- L3: cleanness invariant under every move when 180 ∉ θℤ (Step 3b).
