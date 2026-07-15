## imo-2026-03

Answer (all three explorers, verified n = 1..4 numerically): **c(n) = 2^n/(2^{n+1} − 1)**; write D = 2^{n+1} − 1. LB's optimal marking: points at (2^k − 1)/D, k = 1..n, creating geometric pieces {1/D, 2/D, ..., 2^n/D} (crux transfer from aimo-0117 / aimo-0019: dyadic domination — largest piece exceeds the sum of all others by exactly 1/D).

Shared reductions all approaches use (propose for the lemma cache, prove once, certify, import):
- **Lemma C (claiming value):** with optimal play on a fixed multiset P, first claimer gets exactly Odd(P) = sum of odd-ranked pieces — exchange induction, both one-sided guarantees, Odd + Even = total. This settles the claiming-phase-optimality subtlety cleanly and one-sidedly.
- **Lemma D (defect identity):** Odd − Even = measure{x : #{pieces > x} odd} (layer-cake). Corollaries: stripping an exact equal pair preserves the defect; equal-pairs + leftover ρ ⇒ LB = 1/2 + ρ/2 (tie-proof); LB ≥ 1/2 always.
- **Lemma F (fewer marks):** if LB uses m < n marks, XY halves all m+1 pieces (m+1 ≤ n marks) ⇒ LB gets exactly 1/2 < c(n). So WLOG LB uses all n marks; conversely the lower bound must beat EVERY k ≤ n marks by XY (k < n is XY's parity weapon — halving only the top piece already ties at 4/7 for n = 2 with ONE mark).

I tested the load-bearing upper-bound mechanism computationally this round: the halve + match-and-halve family ALONE fails (explicit n = 2 counterexample q = (0.49, 0.345, 0.165), family gives 0.5725 > 4/7 while true V ≈ 0.51); adding cascade cuts closes all 2000 random n = 2 configs. So every approach's upper bound must include cascades — this is recorded in the approach files.

---

pairing-defect-strategy-family: new
Target: c(n) = 2^n/(2^{n+1} − 1) — full claim, both bounds.
Technique: reduce to Odd(P); express LB's surplus as pairing defect; explicit one-shot XY strategy family + doubling-chain extremal lemma (upper); mass-domination defect count on the geometric configuration (lower).
Skeleton:
  1. Claiming value = Odd(P) — Lemma C (exchange induction).
  2. Defect identity + strip-pairs invariance — Lemma D (layer-cake).
  3. WLOG n marks by LB — Lemma F (halve-everything reply).
  4. Upper bound: XY family — (A) halve-all-but-smallest ⇒ LB ≤ (1 + q_{n+1})/2; (F(j,r)) cut q_j into exact copies of q_{j+1..r} + remainder, halve the rest — always exactly n marks ⇒ LB ≤ (1 + ρ_{j,r})/2; (K) cascades for the deficient case. Doubling-chain lemma: q_{n+1} > 1/D and all d_j = q_j − Σ_{i>j} q_i > 1/D force Σq > 1, contradiction — so some option ≤ 1/D.
  5. Lower bound: geometric marking; any near-pairing with defect < 1/D violates mass balance at the top piece (g_n exceeds everything else by 1/D), pushing the defect into g_n-internal pairs which are charged to XY's mark budget; recurse down the scales stripping exact pairs.
  6. Combine; verify n = 1, 2 answers; note attainment.
Key lemmas (claim + mechanism):
  - Claiming value = Odd(P) — because taking the max reduces you to second player on the rest, and the two one-sided guarantees sum to the total.
  - Defect = measure{N(x) odd} — because the alternating sum integrates the parity of the level-count.
  - Chain lemma: not all of q_{n+1}, d_1, ..., d_n exceed 1/D — because d_j > 1/D forces q_j > 2^{n+1−j}/D by downward induction, and the sum then exceeds 1.
  - Match-and-halve uses exactly n marks for every (j, r) — because each matched pair costs one cut and each halved piece one cut: (r−j) + (j−1) + (n+1−r) = n.
Open gaps: G3 (hard, upper): deficient case d_j < 0 — cascade achieving leftover ≤ 1/D. G4 (hard, lower): the mass-balance recursion with exact mark accounting. G1/G2 routine.
Cases to cover: LB < n marks; XY any k ≤ n; endpoint marks; ties.
Watch out for: per-position bounds p_{2i} ≤ 2^{n−i}/D are FALSE (disproved by explicit n = 2 example — recorded in the file); zero slack at the geometric configuration, so estimates must be exact.

self-similar-induction: new
Target: c(n) = 2^n/(2^{n+1} − 1) — full claim, both bounds.
Technique: induction on n via self-similarity — the n smallest geometric pieces ARE G_{n−1} at the same unit; strip-exact-pairs (defect-invariant) drives both inductions. Crux transfer: aimo-0262 self-reproducing invariant.
Skeleton:
  1. Base n = 1 complete (median-is-1/3 argument, both directions).
  2. Lower bound IH: any ≤ m-mark refinement of {u, 2u, ..., 2^m u} has defect ≥ u. Case k = 0 marks in top piece: top piece is strict max, LB grabs it, done. Case k = 1: PROVEN in the file — threshold accounting at M = 2^{n−1}u shows the defect ≥ defect(rest) ≥ u, using s_1 + s_2 = 2M exactly. Case k ≥ 2: the open gap.
  3. Upper bound IH′: vs any (m+1)-piece config of total S, XY with m marks forces defect ≤ S/(2^{m+1} − 1). Step: cut q_1 into exact copies of q_2..q_{k+1}, strip the k pairs, recurse with n − k marks; the IH threshold Σ_{j=2}^{k+1} q_j ≥ (2^n − 2^{n−k})/D holds termwise from the case selection q_j ≥ 2^{n+1−j}/D, and if NO k works then Σq < 1, contradiction.
  4. Combine; state and verify the answer.
Key lemmas (claim + mechanism):
  - Self-similarity: small pieces of G_n = G_{n−1} at the same unit — because 2^{j}/D for j < n is the G_{n−1} sequence times u = 1/D.
  - Strip-pairs invariance — because removing two equal pieces changes N(x) by 2, preserving parity.
  - k = 1 merge accounting (proven): defect ≥ |B| + (s_1 − M) − (M − s_2) = |B| — because A = (s_2, s_1) and B ⊆ (0, M].
  - Exhaustion: if q_j < 2^{n+1−j}/D for all j then total < 1 — geometric series.
Open gaps: L1 (hard): lower-bound step for k ≥ 2 marks in the top piece (candidate repairs listed in the file: locate-B strengthening, k-induction inside g_n, mark-charging). U1 (medium): feasibility branch of strip-k when q_1 < q_2 + ... + q_{k+1}. U2 routine.
Cases to cover: every k = 0..n (lower); every branch of the k-selection incl. infeasibility (upper); LB < n marks; ties.
Watch out for: IH threshold met with EQUALITY at geometric — no lossy estimates allowed; only strip EXACT pairs.

exact-value-function: new
Target: c(n) = 2^n/(2^{n+1} − 1) — full claim, both bounds at once via max_q V(q).
Technique: minimax/LP-vertex classification — XY's best response is piecewise-linear in the cut positions, so it is attained at a vertex where sub-pieces tie with existing pieces (match/halve/cascade); then the lower bound at the geometric configuration becomes a DISCRETE parity argument: pieces are integers 1, 2, ..., 2^n in units 1/D with odd total, and vertex replies preserve (half-)integrality, so no reply pairs everything with leftover < 1.
Skeleton:
  1. Lemmas C, D, F (shared).
  2. Vertex lemma: inf over XY replies attained on closed pattern-polytopes at vertices = matching/halving equalities — linearity of Odd per pattern + compactness.
  3. V(q) = 1/2 + ρ*(q)/2, ρ* = minimal leftover over the finite reply family.
  4. Upper: max_q ρ*(q) ≤ 1/D — chain lemma + deficient-case cascades.
  5. Lower: ρ*(geometric) ≥ 1/D — integrality/parity of vertex replies to the integer configuration (only the unit piece is odd; halving it breaks integrality, which is exactly the obstruction).
  6. Combine, verify.
Key lemmas (claim + mechanism):
  - Vertex lemma — because Odd is linear on each fixed interleaving pattern, so the min sits on pattern facets = size ties.
  - Integrality: vertex replies to integer pieces produce sizes in ½ℤ generated by matching/halving — so the leftover is ≥ 1 unit (parity of odd total 2^{n+1} − 1).
Open gaps: E1 (medium, load-bearing): rigorous vertex/attainment argument with tie/semicontinuity handling — if E1 leaks the whole discrete lower bound collapses. E2 (hard): deficient-case cascades (shared difficulty with approach 1's G3). E3 (hard): the integrality argument itself.
Cases to cover: all mark assignments and patterns; XY < n marks; LB < n marks; ties.
Watch out for: Odd discontinuous across pattern boundaries; halves of the unit piece.

---

**Rivalry note:** the three slugs share the routine reductions (C, D, F — cache candidates) but differ in overall route: one-shot strategy family + global mass balance (slug 1), recursion on the self-similar structure (slug 2), full best-response classification + discrete parity (slug 3). No shared unproved lemma is load-bearing across all three: G4, L1, E3 are three genuinely different lower-bound mechanisms, and G3/E2 vs U1 are different upper-bound architectures — no single-line trap.

**Recommended build set:** pairing-defect-strategy-family, self-similar-induction, exact-value-function — with priority on the first two; if the reviewer trims to two, drop exact-value-function (its E1 is the riskiest foundation). Builders should prove Lemmas C, D, F first and file them under `results/imo-2026-03/lemmas/` for certification, then attack their slug's hard gap; numeric harness pattern for testing candidate lemmas at n = 2, 3 is in `/tmp/check.py` (grid best-response + strategy-family evaluators).
