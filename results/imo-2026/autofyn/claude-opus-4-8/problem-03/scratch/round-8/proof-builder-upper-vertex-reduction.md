# Build report — upper-vertex-reduction — round 8

**Status: partial.** Spine rebuilt as instructed; (V) replaced; flat-residual gap shrunk cleanly but
NOT fully closed for q ≥ 5.

## What I installed (new, proved in full)

1. **Lemma f-homogeneous (§B):** f(λb) = λ f(b) on the positive cone. Proof: a strategy parametrised by
   (cut pattern, fractional positions in (0,1)) is scale-free; running it on λb yields every final part
   = λ·(part on b); A scales by λ; min over the common strategy set scales by λ.
2. **Lemma σ-migration (§C):** max_{K_q} f = max_{σ-face} f. Any K_q point with Σ < S rescales UP by
   S/Σ > 1 onto the σ-face — gaps and floor scale up (stay ≥ 1/D), Σ hits S — with f weakly larger by
   homogeneity (f ≥ 0). **This VALIDLY replaces the round-7 open statement (V)**: no vertex-attainment,
   no PL, no convexity. Verified by the outline-reviewer too.
3. **σ-face tiers (§D):** (a) b_1 > 2^{q-1}/D and (b) b_2 > 2^{q-2}/D both satisfy certified
   IH-reducible → IH(q−1). Complement = flat residual (b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D).
4. **Lemma TwoLevelCascade (§E1–E2), NEW closures inside the flat residual:**
   - **c1** (b_1 ≥ S/2): generalized GreedyCascade (arbitrary total mass S) → A = 2b_1 − S ≤ 1/D.
   - **c2a** (b_1 < S/2, b_2 ≥ (S−b_1)/2): [halve b_1; greedy-cascade b_2] → A = 2b_2 − (S−b_1) ≤ 1/D,
     using b_2 ≤ 2^{q-2}/D. This is genuinely new (GreedyCascade only gave c1).

## The remaining gap (honest)

**c2b = {b_1 < S/2 AND b_2 < (S−b_1)/2}, q ≥ 5.** For q = 4 certified IH4-flat closes it. For q ≥ 5 open.

- I attempted the natural 3-level extension (halve b_1, halve b_2, greedy b_3): it FAILS because the
  value 2b_3 − s_3 is not bounded by 1/D (b_3 lacks a dyadic cap; only b_1, b_2 are capped by the flat
  condition). Numerically this fixed strategy overshoots to A ≈ 4.0 while the true optimum is ≈ 0.16.
- Discovery correcting the outline's framing: **c1 ∪ c2a are only thin slivers** (each of width ~1/(2D)
  in b_1), so c2b is essentially the WHOLE flat residual, not a thin remainder. The min-A optimum over
  c2b is ≈ 0.16–0.47 ≪ 1 (wide margin — target true), but the optimal cut pattern is ADAPTIVE with no
  closed form (confirmed r6/r7). This is the same wall as before, now cleanly isolated.

## Spec concern (for the orchestrator)

The outline (and reviewer) stated "the genuinely-open slice is b_1 < 1/2" and implied it is a thin
residual mopped up by GreedyCascade + a cascade. **This is optimistic:** GreedyCascade (c1) and the new
c2a together cover only two measure-~1/(2D) slivers near the top of the flat residual; the open region
c2b (both top pieces non-dominant) is the bulk of the flat residual, not a corner. The σ-migration spine
is a genuine and correct advance (kills the false (V)), and c2a is a new closed sub-slice, but the core
adaptive-cascade gap is essentially as large as it was — not near-closed. Next round should treat c2b as
a full open crux (adaptive strategy for both-non-dominant flat configs, q ≥ 5), possibly via a different
framing (e.g. a global potential / matching argument), since the greedy-cascade family provably tops out
at two levels.

## Route verdict
CHANGES REQUESTED (partial, real progress: (V) replaced by a certified-quality reduction; two new
promotable lemmas f-homogeneous, σ-migration, plus TwoLevelCascade; c2a newly closed). The sole open
gap c2b (q ≥ 5) is honestly recorded. Promotable: f-homogeneous, σ-migration, TwoLevelCascade.
