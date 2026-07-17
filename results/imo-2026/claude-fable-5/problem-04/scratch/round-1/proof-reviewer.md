# Proof review — round 1 — imo-2026-04 (Mulan's triangle game)

Problem (problems.jsonl): for which θ ∈ (0°, 180°) can Mulan guarantee victory in finitely many steps? `task: compute_and_prove`, `answer_type: characterization`. Both candidates answer: **θ = 180°/n, integer n ≥ 2, within ≤ n − 1 cuts** — and both give both directions.

## Independent verification performed (adversarial re-derivation)

The load-bearing steps, checked from scratch:

1. **Cut model** (children (P, t, Q+R−t) and (Q, R−t, P+t)): re-derived analytically AND verified by exact coordinate geometry on 200 random triangles/cut points — match to 1e-6. Model fidelity to the statement checked: P interior to exactly one side ⟺ opposite vertex well-defined; non-vertex condition ⟺ t ∈ (0, R) open; achievability (IVT resp. Crossbar) present in both proofs, so every split (t, R−t) is realizable. The game reduces faithfully to angle triples.
2. **Necessity invariant** (clean parent ⟹ some child clean, when 180 ∉ θℤ): the four-case analysis re-derived — C₁ dirty forces t ≡ 0 or t ≡ Q+R, C₂ dirty forces t ≡ R or t ≡ −P (mod θℤ, a subgroup of ℝ, so no rationality needed); this IS exhaustive because P ∉ θℤ and Q ∉ θℤ are the parent-cleanness hypotheses, covering exactly the "kept angle already in θℤ" worry. Each combination forces P, Q, R or 180 into θℤ — contradiction. Verified by exact-fraction search at θ = 55, 80, 100, **170, 179** (θ near 180° works: the clean isoceles start (ε, ε, 180−2ε) only needs to dodge a finite excluded set), and 270/7. No counterexample. The invariant excludes angle = θ specifically since θ = 1·θ ∈ θℤ, and cleanness is symmetric so the relabeling WLOG over the attacked vertex is sound.
3. **Sufficiency**: split legality at every step re-checked — fork (n ≥ 3): 0 < t₀ < θ ≤ 60 ≤ R with t₀ < R strict; descent (Lemma 2/4.2): 0 < θ < kθ for k ≥ 2; θ = 90° (n = 2): t = 90−P ∈ (0, R) ⟺ P, Q < 90, proven. Simulated Mulan's exact strategy against exhaustive Shan-Yu keeps for n = 2, 3, 4, 5, 6, 9, 12 over ~500 triples each plus adversarial specials (equilateral, near-degenerate, (k·θ, tiny, rest)): every game terminates, worst case exactly n − 1 cuts. (My first simulation "failure" at n = 9 was my own bug — descending on the maximal multiple present, which cycles; the proofs descend on the specific kθ → (k−1)θ, which is correct. I added this caution to the certified lemma L2.)
4. **Answer completeness**: both directions present, answer stated explicitly, verified on θ = 90, 60 (wins) and 80 (survival). Circularity: none — Lemma 2/4.2 inducts downward on k with the base at the stop-check; the invariant inducts on rounds from an explicitly constructed clean start.

## Verdict per approach

### residue-divisibility-characterization — **APPROVE** (Status: solved — builder's Status confirmed)
- Correctness: 10/10. Every step re-derived independently; no error found.
- Completeness/rigor: 9.5/10. One hair: Lemma 2's inductive step says "Mulan attacks..." without first noting the triangle may already contain an angle θ (game already stopped — conclusion holds trivially with 0 ≤ k−1 cuts). Trivial, does not affect validity; the twin proof states it explicitly.
- Progress: full solution.
- Ranker outcome recorded: verified-milestone.

### circle-group-quotient — **APPROVE** (Status: solved — builder's Status confirmed)
- Correctness: 10/10. Same mathematics, re-verified; the quotient-group packaging (σ = [180] ∈ ℝ/θℤ) is sound, works verbatim for irrational θ, and cleanly separates residue algebra (Sections 1–2) from size/legality (Section 4 via Lemmas 4.1–4.4).
- Completeness/rigor: 10/10. Handles the early-stop case in Lemma 4.2 explicitly; assembly casework exhaustive and disjoint.
- Progress: full solution.
- **Certified as the Full proof in `results/imo-2026-04/current.md`** (cleaner write-up); residue-divisibility-characterization stands as an independent verification.
- Ranker outcome recorded: verified-milestone.

## Lemma certifications
All four proposed shared lemmas admitted to `results/imo-2026-04/lemmas/` (sorry-free, statements no stronger than proved):
- `cut-model.md` (L0), `exact-multiple-descent.md` (L2, with a usage caution on which multiple to descend on), `theta-90-one-cut.md` (L1), `cleanness-invariant.md` (L3).

## current.md
Created (reviewer-owned): Status **solved**, Full proof = certified circle-group-quotient proof; Approaches tried and Current best filled in.

Goal Progress: SOLVED — imo-2026-04 is fully proven (answer θ = 180°/n, n ≥ 2 integer, ≤ n − 1 cuts), with two independent verified proofs; the run's goal is met in round 1.
