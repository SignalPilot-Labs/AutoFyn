# Proof review — round 1 — imo-2026-03

Problem: c(n) = largest total Liu Bang can guarantee. `compute_and_prove`, answer_type `expression`.
Claimed answer in all three approaches: **c(n) = 2^n/(2^{n+1} − 1)**.

I re-derived every load-bearing step independently (see notes per approach) and ran independent computational verification (exact rationals + brute-force game trees + multistart numerical minimization), not reusing the builders' scripts.

---

## Approach 1: pairing-defect-strategy-family — VERDICT: APPROVE

**True Status: solved** (builder's claim confirmed).

**Scores.** Correctness 10/10, Completeness/rigor 10/10, Progress 10/10 (from skeleton to full proof in one round).

**Load-bearing steps, independently re-derived:**
1. **Lemma C (claiming value = Odd(P)).** Re-derived the exchange induction by hand; the j > 1 case index bookkeeping (q_i ≥ p_{i+2}, Even(Q) ≥ Even(P) − p_2) checks out exactly. Independently verified by brute-force game-tree search on 300 random multisets including ties and zeros — value equals Odd(P) every time. This kills the classic "greedy claiming is optimal" hand-wave: the proof gives both one-sided guarantees rigorously, covering all opponent deviations, ties, and zero-length pieces.
2. **Lemma D / Lemma P (defect = |{x : N(x) odd}| = min pairing cost).** Layer-cake computation re-derived; both directions of the pairing duality are proved (subadditivity blockwise; consecutive pairing attains).
3. **Theorem UB (pigeonhole + merge).** Re-derived: 2^{n+1} subset sums vs D = 2^{n+1}−1 intervals forces a nonzero signed combination |ΣA − ΣB| ≤ 1/D; the merge process turns it into equal pairs + leftovers of total δ. I audited the mark ledger adversarially in all three branches (A_fin ≠ ∅: ≤ n; A_fin = ∅: last step must be an a = b step, ≤ n−1; B = ∅: ≤ n) and legality (every mark strictly interior to a current piece whose interior is mark-free). Independent exact-rational re-implementation: 400 random configs each for n = 1..4, marks ≤ n and defect ≤ 1/D always.
4. **Theorem LB (tree-component signing).** Re-derived: ≤ 2n+1 pieces ⇒ ≤ n pairs ⇒ some component of the block multigraph has e = v−1 ⇒ tree (loops/parallel edges are cycles) ⇒ bipartite ±1 signing telescopes block masses 2^j u to a nonzero ±{0,1} signed sum of distinct powers of 2, ≥ 1 by binary uniqueness ⇒ every pairing costs ≥ u ⇒ defect ≥ u by Lemma P. Uniform in XY's mark count k ≤ n (fewer marks only remove edges), covers wasted/endpoint marks. Numerically confirmed: min defect over ≤ n-cut refinements of the geometric config is exactly 1/D at n = 1, 2, 3.
5. **Edge cases.** LB with < n+1 positive pieces: Lemma F (XY halves everything, value exactly 1/2 < 2^n/D). Zero-length pieces / endpoint marks: Section 0 + multiset formulation. Both bounds constructive; inf attained; sup attained at the geometric marking — "largest c" is well-defined and equals 2^n/D.
6. **Answer check.** (1 + 1/D)/2 = (D+1)/(2D) = 2^n/D ✓; n = 1 exact-fraction grid minimax returns 2/3 ✓.

**No gaps found.** Full proof written into `results/imo-2026-03/current.md`. Outcome recorded: `verified-milestone`.

---

## Approach 2: self-similar-induction — VERDICT: APPROVE

**True Status: solved** (builder's claim confirmed).

**Scores.** Correctness 10/10, Completeness/rigor 10/10, Progress 10/10.

Note: the slug's original induction line was abandoned mid-round; the file now contains an independent complete write-up sharing the pigeonhole/tree core with Approach 1 but with a genuinely different upper-bound realization (Lemma R: superposition/tape matching instead of the iterative merge) and its own Lemma C proof (largest-remaining strategy with the (∗) case analysis, which I re-derived — the i even / i odd telescoping brackets are correct).

**Independently checked:**
- **Lemma R mark ledger.** ≤ s cuts at β-positions inside A-pieces + ≤ r−1 cuts at α-positions inside B-pieces + |Z| midpoints = ≤ k−1; boundary-coinciding tape positions correctly cost nothing; the A-fragments over (0, Σ_B] and the B-fragments realize the same partition of (0, Σ_B) by T, so the equal-pair matching is exact and leftovers total exactly |x·q|. Verified by an independent exact-rational implementation: 400 random configs each for n = 1..4 — defect == |x·q| ≤ 1/D and marks ≤ n every time; the worked n = 3 counterexample q = (0.35, 0.245, 0.235, 0.17) reproduces defect 1/100 with 3 marks.
- **Lemma T / Lemma G.** Same tree mechanism as Approach 1; the loopless-tree deduction ("a loop or parallel edge leaves the underlying simple graph too few edges to connect") is valid; Lemma G's 2-adic argument for δ(g) = u is correct.
- **Case m < n** (halve all m+1 pieces, m+1 ≤ n marks) and endpoint-mark conventions (§0) are handled.

**No gaps found.** Both APPROVEd files constitute two mutually confirming complete write-ups. Outcome recorded: `verified-milestone`.

---

## Approach 3: exact-value-function — VERDICT: CHANGES REQUESTED (moot — siblings solved)

**True Status: partial** (builder's claim accurate — no overclaim; gaps declared honestly).

**Scores.** Correctness 9/10 (everything asserted as proven is in fact proven), Completeness 6/10 (two real gaps), Progress 8/10.

**Checked and sound:** Lemma C (same value lemma, correct min_i Odd(S_i) computation); Lemmas D, D1–D4, F; Lemma V (attainment via closed pattern polytopes Q_σ where defect is linear, plus the rank-s perturbation argument — the equal-value-same-perturbation trick correctly preserves the order facets); Lemma P (integer-vertex parity: alternating sum ≡ total ≡ D ≡ 1 mod 2); Chain Lemma (downward induction q_j > 2^{n+1−j}/D, sum contradiction — arithmetic verified).

**Remaining gaps (as declared):** E2 (upper bound, deficient case (c) — needs cascade replies) and E3′ (lower bound for fractional vertices). Both are now subsumed: the solved siblings prove the same two bounds by other means, so there is no need to close E2/E3′. Recommend freezing this approach rather than spending further rounds; its Lemma V and Chain Lemma remain correct standalone results (not admitted to the lemma cache — superseded, no remaining consumer; correctness not in question).

Outcome recorded: `partial`.

---

## Lemma certifications

Admitted to `results/imo-2026-03/lemmas/` (all `sorry`-free, statements no stronger than proved, independently verified):
- `claiming-value.md` (Lemma C)
- `defect-identity.md` (Lemma D, D0–D2, D4, pairing duality)
- `fewer-marks.md` (Lemma F)
- `upper-bound-pigeonhole-realization.md` (Lemma P pigeonhole + Lemma R realization + Theorem UB)
- `lower-bound-tree-signing.md` (Lemma T + Lemma G + Theorem LB)

Rejected (not for incorrectness): exact-value-function's Lemma V, integer-vertex parity, Chain Lemma — correct but superseded by the solved route; no consumer remains.

---

## Goal Progress

- **pairing-defect-strategy-family: solved — APPROVE.**
- **self-similar-induction: solved — APPROVE.**
- **exact-value-function: partial — CHANGES REQUESTED** (gaps E2, E3′ remain; moot given the solves).
- **Overall: imo-2026-03 is SOLVED in round 1.** `current.md` Status = solved with the full proof recorded. Answer: **c(n) = 2^n/(2^{n+1} − 1)**, verified at n = 1 (2/3), n = 2 (4/7), n = 3 (8/15) by independent computation. The run's goal is met; no further building rounds are needed on this problem.
