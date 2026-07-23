# Proof-builder report — upper-vertex-reduction (round 7)

**Status: partial.** File: `results/imo-2026-03/approaches/upper-vertex-reduction.md`.

## What I proved (rigorous, no numerics on the load-bearing parts)

The Case-B hard-regime upper bound IH(q) (for ALL q, incl. the IH(q≥5) flat residual) is recast as a
max–min over the compact polytope
  K_q = {b_i−b_{i+1} ≥ 1/D, b_q ≥ 1/D, Σb_i ≤ (2^q−1)/D} ⊂ ℝ^q,
with f(b) = min over ≤ q−1 XY cuts of A (= μ(⊕[0,b_i]), Lemma X). IH(q) ⟺ f ≤ 1/D on K_q. I closed:

1. **§A f continuous + min ATTAINED** (Berge Maximum Theorem over finitely many cut patterns +
   Weierstrass). This settles the achievability concern: f ≤ 1/D genuinely exhibits an XY strategy, not
   a bare existence claim. Also gives existence of max_{K_q} f.
2. **§B Lemma VertexFace** (promotable): every vertex of K_q has some gap = 1/D or b_q = 1/D — pure
   polytope combinatorics (q+1 constraints, ≥ q active at a vertex ⟹ ≤ 1 inactive ⟹ a gap or bottom
   face is active). On a gap-face certified Reduction 2 gives A = gap ≤ 1/D; on the bottom-face
   certified Lemma H gives A = b_q = 1/D. So **f(v) ≤ 1/D at every vertex v.** No PL assumption.
3. **§C tightness**: f(geometric) = 1/D exactly (Reduction 2 up via its gap = 1/D, certified lower
   bound down). The target constant is tight, realised at the σ∩gap vertex.

Net: **IH(q) for all q ⟸ (V): f attains its max over K_q at a vertex.** Every vertex is already ≤ 1/D.

## The blocking gap (the reviewer's acceptance criterion)

**(V) is NOT established, and I did not paper over it.** The outline's justification — "marginal of a
jointly-PL function is PL" — is FALSE in general: partial minimisation preserves PL only under JOINT
CONVEXITY, and A is a non-convex sorted alternating sum. Crucially this is the exact **asymmetry with
the LOWER bound**: DyadicLower's vertex spine worked because its A had NO inner min (A was a direct
function of the fragment multiset); the upper side's f = min-over-strategies adds an inner min that
destroys PL. So the mirror is not clean and the lower-bound machinery does NOT transfer to (V). The
reviewer's suggested route-(b) (push interior→boundary without decreasing f) is also unproven and not
obviously true (halving b_1 is free, so f need not increase with b_1).

Numerically (V) holds (kill-switch reproduced: f(geometric)·D = 1.0000, 8 interior configs f·D ≤ 0.27,
no interior peak), and I showed f is non-affine on an interior segment (peak 0.27 between endpoints
0.10/0.12) — consistent with, but not proving, PL-ness. So the CONCLUSION appears true; only the PROOF
of (V) is missing. **(V) is the sole gap; Status partial. No overclaim.**

## Spec concerns / notes for the orchestrator

- The framing is a CORRECT and clean reduction (IH(q) ⟸ (V)) and disposes of every vertex by explicit
  certified strategies — real, reusable structural progress — but it does NOT close IH(q≥5). It shares
  the same wall as the q-induction, now isolated as a single convex-analytic statement (V) rather than
  an induction step. If the reviewer wants a live upper approach that can actually finish, (V) must be
  attacked head-on (is f PL for THIS A? or a direct interior bound), OR the upper wall needs the
  explicit-leaf route (upper-general-cascade's IH5-flat 2-delta / B2-flat), which does not depend on (V).
- Promotable this round: **Lemma VertexFace** (vertices of K_q lie on gap/bottom faces ⟹ f ≤ 1/D) and
  **f-continuous-attained** (Berge). Both fully proven, no numerics on the load-bearing steps.
- Diversity: this is the genuinely-different global-max reframe that answered the round-6 flag, but its
  novelty (V) is unproven. If (V) can't be moved next round, the upper wall is again one framing (the
  explicit-leaf cascade) — escalate for a new upper framing then.
