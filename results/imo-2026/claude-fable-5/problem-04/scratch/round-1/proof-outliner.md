## imo-2026-04

**MAJOR CORRECTION TO THE EXPLORERS' CONJECTURE.** The conjectured answer "Mulan wins iff θ ≤ 90°" is wrong. Extending the retrieval explorer's mod-θ observation from forced moves to ALL moves gives an unconditional Shan-Yu invariant: with children C1 = (P, t, Q+R−t), C2 = (Q, R−t, P+t), the residue sum mod θ is invariant (≡ 180), and "both children contain an angle in θℤ" forces some current residue ≡ 0 or 180 ≡ 0 (mod θ). So if 180/θ ∉ ℤ, Shan-Yu starts generic and keeps a θℤ-free child forever. Conversely if 180 = nθ, the cut t ≡ −P (mod θ) is a one-move fork into two children each containing a positive multiple of θ, and "contains kθ" is winning by downward induction (split kθ = θ + (k−1)θ). **Correct answer: Mulan wins iff 180/θ ∈ ℤ, i.e. θ = 180°/n, n ≥ 2.**

Verified by exact-fraction adversarial game search (depth 8, structured candidate cuts, script /tmp/exact_check.py): wins at θ = 30, 36, 45, 60 (incl. extreme starts (1,2,177)); no win at θ = 40, 55. The explorers' grid simulations suggesting wins at θ = 55/33/70 are nearest-grid-point rounding artifacts (the grid fabricates exact hits); the 1°-grid "odd θ stuck" pattern was actually the true signal, not the artifact.

---

residue-divisibility-characterization: new
Target: Mulan wins iff 180/θ ∈ ℤ (θ = 180°/n, n ≥ 2) — full characterization, both directions.
Technique: invariant/monovariant on residues mod θ (necessity) + explicit bounded fork construction with downward induction on multiples of θ (sufficiency). KB: Invariants & monovariants; fork/double-threat pattern (crux aimo-0445).
Skeleton:
  1. Cut model: attacking R with parameter t gives C1 = (P, t, Q+R−t), C2 = (Q, R−t, P+t) — from the statement.
  2. Lemma A: an angle exactly kθ (k ≥ 1) is winning — split kθ = θ + (k−1)θ, both children winning, induct on k.
  3. Sufficiency (180 = nθ): from any θℤ-free triple, cut the largest angle with t ≡ −P (mod θ), t ∈ (0, θ): C2 gets P+t ∈ θℤ, C1 gets Q+R−t ≡ 180 ≡ 0 — both winning by Lemma A. Bounded move count (≤ n-ish).
  4. Necessity (180/θ ∉ ℤ): Shan-Yu starts θℤ-free (finitely many excluded values) and can always keep a θℤ-free child — the four-case intersection argument. No angle ever equals θ.
  5. Assemble; note the condition subsumes θ > 90 (180/θ < 2 ⟹ not an integer).
Key lemmas (claim + mechanism):
  - Lemma A (kθ winning) — because splitting kθ into θ + (k−1)θ makes BOTH children winning, so Shan-Yu's discard is irrelevant.
  - Fork lemma (σ ≡ 0 case) — because t ≡ −P zeroes P+t in C2 while the angle-sum identity zeroes Q+R−t ≡ P+Q+R ≡ 180 in C1.
  - Invariant lemma (σ ≢ 0 case) — because "both children hit θℤ" needs [t] ∈ {0, [Q+R]} ∩ {[R], [−P]}, and every intersection case forces a zero residue or 180 ≡ 0.
Open gaps: GAP A (Lemma A write-up), GAP B (size constraint t₀ < R incl. n = 2 boundary — plug with the θ = 90 one-move win), GAP C (exhaustive case write-up of the invariant for all three attack choices, valid for irrational θ).
Cases to cover: n = 2 (θ = 90) boundary in sufficiency; initial triangle already containing a multiple of θ; all three attack choices in necessity.
Watch out for: never assume θ rational (work in ℝ/θℤ); game-stop check is at round start; sufficiency must work from EVERY start, necessity from ONE chosen start.

circle-group-quotient: new
Target: same characterization (Mulan wins iff 180/θ ∈ ℤ) end to end.
Technique: rival framing — project the game to the circle group G = ℝ/θℤ, decide the quotient game by whether σ = [180] is 0 in G, then a separate lifting lemma handles all size constraints in one place. Different failure profile from the direct write-up: if the direct approach stumbles on boundary/size bookkeeping, this one isolates it.
Skeleton:
  1. Projection π to multisets in G; element-sum σ = [180] invariant under every cut, for both children.
  2. Quotient dichotomy: σ ≠ 0 ⟹ "no element [0]" is Shan-Yu-closed; σ = 0 ⟹ the class [t] = [−P] forks both children into containing [0].
  3. Lifting: necessity lifts for free (projection forgets only); sufficiency needs Lift 1 (a representative t₀ ∈ (0, θ) ⊂ (0, R) when attacking the max angle; n = 2 via direct 90° win) and Lift 2 (finish from an exact multiple kθ, downward induction, ≤ n moves).
  4. σ = 0 ⟺ 180/θ ∈ ℤ; state the answer set.
Key lemmas: same three mechanisms as the rival but layered: algebra in G with NO size talk, then two lifting lemmas with NO residue talk.
Open gaps: Lift 1 boundary bookkeeping; Lift 2 induction write-up; Step 2 symmetry/enumeration.
Cases to cover: n = 2; equilateral start; state already containing [0].
Watch out for: keep the layers strictly separate — that separation is the point of this rival.

escalation-below-90: new (falsification rival / devil's advocate)
Target: the explorers' original answer "Mulan wins iff θ ≤ 90°" — kept alive ONLY as a stress test of the residue invariant, since the two answers are mutually exclusive.
Technique: 2θ-double-threat escalation (create angle 2θ, bisect) + θ-peel forced transfers.
Skeleton:
  0. GATE: exhibit a concrete hole in the residue invariant (wrong child formula, wrong terminal condition, or an unmodeled legal move) — e.g. a verified exact-arithmetic Mulan win at θ = 55°. If the gate fails, record this answer as refuted and kill the slug.
  1. θ > 90: Shan-Yu "all angles < θ" invariant (unbreakable iff 2θ > 180) — shared lemma.
  2. θ = 90: one-move universal fork (r2 = 90 − Q; both children contain 90) — shared lemma.
  3. θ < 90: 2θ-fork + leftover-peeling escalation — currently believed impossible for 180/θ ∉ ℤ.
Open gaps: the gate itself; the entire Step 3 construction.
Cases to cover: n/a until the gate passes.
Watch out for: do NOT cite grid simulations as evidence (rounding artifacts, demonstrated).

---

**Lemma candidates for the shared cache** (any builder may certify): (L1) θ = 90 one-move universal win; (L2) "angle = kθ exactly ⟹ Mulan wins in ≤ k−1 moves"; (L3) θ > 90 Shan-Yu invariant (now redundant to the main characterization but cheap and independent).

**Recommended build priority:** residue-divisibility-characterization first (closest to complete — GAPs A–C are write-up-level, not idea-level), circle-group-quotient second, escalation-below-90 last (its builder's only real job is the gate: an honest adversarial audit of the invariant algebra; expected outcome is a recorded refutation of the θ ≤ 90 answer, which is itself valuable).

build set: residue-divisibility-characterization, circle-group-quotient, escalation-below-90
