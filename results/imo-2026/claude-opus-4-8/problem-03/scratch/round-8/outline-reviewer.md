# Outline review — round 8 — imo-2026-03

Two live whole-problem spines (upper polytope σ-face / lower T-parity interleaving), opposite
sides, no shared wall. Both are ADVANCE builds of certified reductions with one honestly-isolated
gap each. I verified the two load-bearing new claims numerically and analytically. Both APPROVED.

---

## upper-vertex-reduction — APPROVE (build)

The new spine replaces the open statement (V) with a **1-homogeneity + σ-face migration** bypass.
I checked the load-bearing pieces:

- **1-homogeneity of f — CORRECT (verified exactly).** For a fixed XY strategy, A is an
  alternating sum of fragment lengths, each fragment = piece × (fraction difference), so
  A(λb, same strategy) = λ·A(b, strategy) exactly. Confirmed numerically to machine precision
  across 4 random strategies at q=4 (match=True every time). The strategy set (cut allocations +
  fractions in [0,1]) is scale-invariant, so f(λb)=min = λ·min = λf(b). Sound. (My first noisy
  numeric that showed a mismatch was pure independent-multistart noise, not a real gap — the
  fixed-strategy check is the correct test and it matches exactly.)

- **σ-face migration — CORRECT, direction is right.** For b in K_q with Σb_i = s < (2^q−1)/D,
  rescale UP by factor (2^q−1)/(Ds) > 1: gaps and floor scale up (stay ≥ 1/D ✓), ordering
  preserved, Σ hits the σ-face, so b' ∈ K_q; and f(b') = factor·f(b) > f(b). Hence max of f over
  K_q lies on the σ-face. This genuinely **replaces (V)** — no vertex-attainment, no PL-marginal
  claim (the false r7 step), no convexity. K_q is downward-closed in scale (Σ ≤ (2^q−1)/D), so
  the σ-face is the far boundary and rescaling-up is the right direction. Verified numerically the
  σ-face point weakly dominates the interior point. Kill-switch passed.

- **Fold of upper-general-cascade — CORRECT.** The task flagged a possible region drop. Checked:
  c(n) = 2^n/D > 1/2 for ALL n (0.667, 0.571, 0.533, … → 1/2⁺), and the flat b_1-threshold at
  q=n+1 is exactly 2^n/D = c(n). So B2-small (a_1 < 1/2) has a_1 < 1/2 < c(n) = 2^{q-1}/D ⟹ NOT in
  tier (a) [b_1-large], hence splits into tier (b) [b_2 > 2^{q-2}/D, certified IH-reducible] ∪ tier
  (c) [flat residual, owned here]. No region is dropped; the fold is sound. Do NOT dispatch a builder
  for upper-general-cascade this round.

**Sole open gap (honest):** step 4, the q≥5 flat-residual cascade restricted to b_1 < 1/2. This is
the same adaptive-cascade core as before, but the framing is now cleaner: everything else is
certified imports (IH-reducible, IH4-flat, GreedyCascade, VertexFace, X, H, Reductions) plus the two
new one-line lemmas (homogeneity, migration).

**Changes for the builder:**
- Propose `lemmas/f-homogeneous.md` and `lemmas/sigma-migration.md` as the two new certifiable
  one-liners. State homogeneity as f(λb)=λf(b) on the positive hard-regime CONE (not on K_q as a set
  — K_q is not scale-invariant; the run_state watch is correct).
- The flat-residual cascade (step 4) is the real work: prove the surviving-singleton alternating sum
  < 1/D under b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D, Σ=(2^q−1)/D, gaps > 1/D. Count cuts explicitly
  (halve b_1 = 1, each pair-cancel = 1, final δ-split = 1; q=5 ⟹ 4 = q−1). GreedyCascade covers the
  b_1 ≥ 1/2 sub-slice in closed form; the genuine work is b_1 < 1/2.
- Do NOT resurrect (V), PL/convexity, or the interior-descent route (r7 dead ends).

## direct-constructive — APPROVE (build)

The **T-parity + generalized interleaving** framing for the augmented a=0 closer.

- **Genuinely different from the refuted DyadicLower route — YES.** No receiver/donor, no flat-move
  monovariant, no cross-group transfer (the three walls of the plateaued route). It is a vertex
  enumeration + parity-counting argument. This is the different-framing the shared-gap-plateau rule
  demanded. Good for field diversity.
- **The identity A = 1 + 2·Σ(G at odd) is honestly NOT overclaimed.** Both explorer and outliner
  flag (lines 135–138 of the outline) that it requires ALL F-pieces at odd ranks — true only in the
  minimizing ordering, NOT arbitrary orderings — so the lower bound over all orderings CANNOT cite
  the identity; it needs genuine per-cell vertex enumeration. The caveat is honest and the hard step
  (step 4) is correctly isolated.
- **Counting bound checks out.** For T odd, #odd ranks − |F| = (n+s−k_n)/2 ≥ s (using budget
  k_n ≤ n−s). Arithmetic verified. n=3 anchor (T=7, the only valid parity) has the complete 5-cell
  enumeration, each giving A = (function of F > 1) + 2t.
- **Numeric gate passed.** n=3 stray, t=0.3: min A = 1.6006 ≈ 1+2t = 1.6, strictly > 1, over 20k
  configs. Consistent with the framing; the infimum-1-not-attained caveat is correctly stated.

**Sole open gap (honest):** step 4 (Case-A T-odd per-cell enumeration for general n — n=3 finite done)
+ step 5 (T-even pigeonhole finish, secondary/easier). The general-n cell-type taxonomy is the real
work and is genuinely hard, but the route is finite and rigorous per n with a solid n=3 anchor.

**Changes for the builder:**
- Do the per-cell enumeration explicitly; do NOT wave from the n=3 anchor to general n via the
  non-general identity. State A > 1 strictly (infimum 1 not attained for s ≥ 1).
- Avoid all recorded dead ends: pointwise A_stray ≥ A_confined (FALSE, 716/17980), receiver-existence,
  cross-group monovariant, relaxed-(†) arbitrary G.

## upper-general-cascade — FOLD (no build), confirmed

Subsumed by the σ-face reduction (verified above). Stays in the population; its certified lemmas
(GreedyCascade, IH-reducible, IH4-flat) remain imports. No builder this round.

---

## Diversity note

Field is two live whole-problem attempts on opposite sides, no shared wall, each with a genuinely-new
framing this round. Adequate breadth for a near-closed problem. WATCH: if the upper flat-residual
cascade (b_1<1/2) AND the lower general-n cell taxonomy BOTH stall next round, both remaining gaps are
"adaptive/finite-but-general" combinatorial cores — reframe then, not before.

## Ranking (this round)

direct-constructive 1707.9 > upper-vertex-reduction 1677.2 > upper-general-cascade 1667.8 (folded) >
caseB-matching 1484 (dead) > potential-duality 1407 (parked) > induction-recursion 1328 (dead).
upper-vertex-reduction rose (σ-migration bypasses the false (V) blocker, subsumes upper-general-cascade);
direct-constructive rose (fresh non-graveyard framing); the two live spines drawn near-parity; folded
upper-general-cascade drops below both. Stale flags cleared.

build set: upper-vertex-reduction, direct-constructive
