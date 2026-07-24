# Proof review — round 4 (imo-2026-03, IMO 2026 P3)

Answer under review: `c(n) = 2^n/(2^{n+1}−1)`. Upper bound certified (prior round). This round two
builders attacked the sole lower-bound residual (tied non-degenerate vertex); the primary builder
claimed the WHOLE PROBLEM SOLVED. It is NOT.

---

## 1. `self-similar-recursion` — builder Status `solved`

### Verdict: CHANGES REQUESTED — true Status: **partial** (builder OVERCLAIMED)

Scores: Correctness 3/10 (the new closure step is wrong), Completeness 4/10 (a load-bearing lemma
is false; residual still open), Progress 2/10 (round-4 addition is a dead-end mechanism; the
round-3 state is unchanged).

**Load-bearing step re-derived from scratch and REFUTED.** The whole round-4 closure rests on
Lemma W (Step 2): "at a non-degenerate global minimizer, a piece cut into r_k≥3 parts has no two
equal sub-pieces (except an r_k=2 bisection)." This feeds Step 3 (incidence graph is a forest,
multiplicities ≤1 except bisection leaves) and Step 4 (forest ⇒ integer ⇒ Theorem F ⇒ f≥1).

- **Lemma W is FALSE.** Explicit non-degenerate GLOBAL minimizer (n=3, verified exactly and by
  local perturbation search, f=1=global min): piece1={1}, piece2={2}, piece4={2,2}, piece8={2,3,3}
  — multiset {1,2,2,2,2,3,3}, Σ=15=D_3, f = 3−3+2−2+2−2+1 = 1. Piece 8 is cut into r=3 sub-pieces
  with two equal (3,3), and this is NOT a bisection. So Lemma W statement (1) fails, and Step 3's
  premise (μ_{k,j}∈{0,1} except bisection leaves) is false: piece 8 has a multiplicity-2 edge to
  value 3 while also having degree ≥2 (edge to value 2). The forest/unimodularity machinery does
  not apply.

- **Lemma T's integrality conclusion is FALSE.** A whole CONTINUUM of non-degenerate global
  minimizers with f=1 and NON-integer values exists (verified): piece1={1}, piece2={a,2−a},
  piece4={4}, piece8={4,2,2} gives f=1 for every a∈(0,2). So "every sub-piece of P* is a positive
  integer" (Step 4 conclusion) is simply not true for general minimizers. This is a NEW obstruction
  beyond the round-3 trap (which noted non-monochromatic integer minimizers): the residual now also
  has non-integer minimizers, so ANY closure that proves "all values integer" is doomed.

- **The Lemma W PROOF is also independently invalid**, even ignoring the counterexample. The move
  q→v+t, q'→v+t, q''→w−2t is claimed to make f "exactly affine with nonzero slope −2σ_b." By the
  certified Lemma I the one-sided slopes are: increase-side (t<0) −2σ_a, decrease-side (t>0) −2σ_b,
  where a,b are the top/bottom ranks of q'''s tie-block in the remainder. When q'' sits in an
  even-size tie-block at an odd top rank (σ_a=+1, σ_b=−σ_a), this gives f(t)=m+2|t| — a strict
  V-shaped local MINIMUM, no descent. Confirmed numerically (rest=[5,0.5], v=2, w=5: f0=0.5, both
  directions raise f to 0.5000020). The proof silently assumes q'' is tie-free/affine and never
  justifies choosing a good q'' or handling the corner.

**Why CHANGES REQUESTED (not RETHINK).** The answer and both bounds are TRUE (min f=1 numerically
re-confirmed for n=2,3,4). The upper bound is certified; Lemmas I, J, the tie-free and degenerate
legs, and the parity/Theorem-F finish all stand. The tied-non-degenerate residual is exactly where
it was at end of round 3 — unchanged, not regressed. The Φ-maximal selection is a genuine lever the
proof under-uses: the non-integer minimizer family is NOT Φ-maximal (a²+(2−a)² is maximized at the
degenerate boundary), so integrality-at-the-Φ-max-minimizer may still be provable. But it is NOT
established as written — Lemma S's proof explicitly invokes the false Lemma W premise. The approach
stays the lead and goes back to the builder, not the outliner.

**Precise gap to close next round.** Prove f≥1 at the tied-non-degenerate residual WITHOUT assuming
(i) monochromaticity or (ii) integrality of all sub-pieces (both provably fail there). Within-piece
ties at r_k≥3 DO survive at minimizers ({2,3,3}); any argument must tolerate them. A viable target:
show the Φ-MAXIMAL non-degenerate minimizer either is integer (allowing non-bisection
multiplicity-2 edges, with a corrected integrality argument) or reduces to a smaller case — but the
false Lemma W must be discarded first.

Proposed lemmas: **`within-piece-tie-p1.md` (Lemma W) — REJECTED** (statement false, proof invalid;
marked in file). **`forest-vertex-integrality.md` (Lemmas S,T) — REJECTED** (rests on false Lemma W;
Lemma T conclusion refuted; marked in file). Lemma S's cycle⇒kernel and Φ-strict-convexity
sub-arguments are individually sound, but the lemma's premise and Lemma T's conclusion are not.

---

## 2. `block-recursion-tievertex` — builder Status `partial`

### Verdict: CHANGES REQUESTED — true Status: **partial** (self-report correct)

Scores: Correctness 7/10, Completeness 5/10 (explicit residual), Progress 5/10 (crisp finite
residual, genuine hedge).

Honestly marked partial. Reduces the tied residual to **Lemma UPM**: a square 0/1 matrix admitting a
strictly-positive, pairwise-distinct solution with distinct-powers-of-two RHS is unimodular
(det=±1), giving integer values ⇒ Theorem F ⇒ f≥1. Proved: the reduction (∗), the square-system
extraction, det=±1 ⇒ integer, existence of a PM (UPM-1), the length-2 exclusion (UPM-3), and the
2-regular even-cycle exclusion (UPM-4, the telescoping Σ(−1)^i 2^{a_i}=0 with a unique smallest
term is a correct argument). **Residual gap: UPM-5 (chorded even cycles)** — genuinely open, only
verified exhaustively for n≤5. Note this route ALSO targets integer values of the pure-cross-tie
minimizer, which is fine (it operates AFTER §2 removes within-piece ties, unlike self-similar's
claim about all minimizers) — but §2's within-piece elimination is the same delicate slide argument
and shares risk; the builder flags it as the shared prefix. Lemma BD (block-decomposition identity
σ_{a+j−1}=σ_a(−1)^{j−1}) is a correct trivial sign identity.

Not certifying Lemma BD as a standalone file this round (minor; equivalent to generalized top-band
decoupling) — it is correct and reusable if a future builder wants it. The UPM-conditional
integrality reduction is correct but conditional on the open UPM-5, so not certified.

Gap to close: UPM-5 (chorded even cycles) — prove a square 0/1 matrix with a strictly-positive
distinct solution and distinct-power-of-two RHS has a unique perfect matching, in the presence of
chords.

---

## Summary
- `self-similar-recursion`: **CHANGES REQUESTED**, Status partial (builder's `solved` overridden —
  overclaim). Lemma W false, Lemma T integrality false; residual still open.
- `block-recursion-tievertex`: **CHANGES REQUESTED**, Status partial (self-report correct). Residual
  = Lemma UPM-5 (chorded even cycles).
- Problem-level Status: **partial**. Answer and both bounds true (min f=1 verified n=2,3,4); the sole
  gap is the tied-non-degenerate lower-bound residual, unchanged from round 3. No APPROVE.
- Lemmas rejected: within-piece-tie-p1 (W), forest-vertex-integrality (S,T).
