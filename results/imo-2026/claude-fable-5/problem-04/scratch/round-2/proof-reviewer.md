# Proof review — imo-2026-04 — round 2

Problem (problems.jsonl): the Shan-Yu/Mulan triangle-cutting game; `task: compute_and_prove`, `answer_type: characterization`. Both directions required for `solved`.

## Independent verification performed (adversarial)

I did not trust either builder's checks; I re-derived the load-bearing steps from scratch:

1. **Piece-angle formula** (the single load-bearing identity both proofs rest on: cut to vertex A, angle a, companion B, angle b, parameter t ∈ (0, a) gives pieces (b, t, a+c−t) and (c, a−t, b+t)) — re-derived numerically from **raw coordinates** (place triangle by law of sines, pick random P on BC, measure all six angles): 3000 random triangles/cuts, max deviation 2.05·10⁻¹¹. The formula, the supplementary P-angles, and the (0°,180°) ranges are correct.
2. **Four-case closure (Safety Preservation)** — brute-forced with exact rationals: θ ∈ {40, 72, 120, 7/3, 170, 1234/11} (all with 180/θ ∉ ℤ, incl. θ > 90°), random safe triangles, and **adversarial** cut parameters (every multiple kθ < a, and t = θ − r_B, i.e. the exact parameter that breaks the lemma when 180/θ ∈ ℤ): 436 422 cuts, at least one piece safe in every single one. 0 failures.
3. **Direction A strategies simulated against an exhaustive Shan-Yu** (both pieces explored at every cut, worst case taken; exact rationals; random starts plus adversarial starts whose angles are multiples of θ):
   - remainder-forcing strategy (forcing cut t = θ − r_b, then tracked descent): n = 2,…,9 — Mulan always wins, worst case exactly n − 1 cuts, every cut-validity assertion (t strictly interior) passed. Matches the claimed bound.
   - descending-chain strategy (trichotomy I/II/III, grind s = x−θ, ignition s = θ−x, tracked descent): n = 2,…,12 — always wins, worst cases (1,2,4,5,6,8,9,10,12,13,14) all within the claimed bounds n−1 (n ≤ 3) / 2n−4 (n ≥ 4).
4. **Descent well-definedness stress test.** My first, deliberately *stateless* simulation of descent (pick any multiple angle each turn) hit an infinite loop at θ = 22.5°, T = (67.5°, 45°, 67.5°) — cutting the 3θ angle reproduces the same triangle. This is exactly the trap the refuted round-1 monovariant fell into. **Both proofs avoid it correctly**: their strong induction tracks the exhibited multiple (m−1)θ through the recursion (a history-dependent strategy, which is legitimate), and descending-chain's Remark after Lemma A1 records the counterexample explicitly. Re-simulating faithfully (tracked index) gives the bounds above. Not a gap — but it confirms this step genuinely needed the care both builders gave it.
5. Spot checks: forcing-lemma validity edge cases (n = 2 acute a+b > 90°; n ≥ 3 max angle ≥ 60° ≥ θ; safety excludes a = θ), the θ = 40° verification triangle (55°, 55°, 70°) is safe (the outline's (50°, 80°, 50°) was indeed unsafe — builder's erratum is correct), θ = 90° example arithmetic, θ = 120° example.

---

## Approach 1: remainder-forcing (`results/imo-2026-04/approaches/remainder-forcing.md`)

**Verdict: APPROVE. True Status: solved.** Builder's claimed Status is accurate.

- **Correctness: 10/10.** Every step re-derived and confirmed. Cut Lemma (1) IVT realizability with P strictly interior (f(0)=0 < t < a = f(1) forces s* ∈ (0,1)); the angle-additivity Claim proved honestly via the convex-sector argument; piece formula matches my coordinate derivation. Descent Lemma: strong induction sound, t = θ ∈ (0, mθ) valid precisely because m ≥ 2, top-of-iteration check handled in both base and step, both Shan-Yu options covered. Forcing Lemma: t = θ − r_b ∈ (0, θ), congruence algebra (b+t ≡ 0; a+c−t = 180°−(b+t) ≡ 0 using 180° ≡ 0) correct; validity split n ≥ 3 / n = 2 (obtuse/acute) exhaustive and each case airtight; O1 caps the forced multiples at n−1. Direction B: safe start (finite exclusion set vs. infinite isoceles family), four-case closure correct and exhaustive (inherited angles b, c eliminated by safety of T — the 2×2 disjunction over the remaining two angles per piece covers every way each piece can be unsafe), induction over iterations explicit.
- **Completeness / rigor: 10/10.** No skipped cases found: n = 2 handled separately with safe ⟺ no right angle; θ > 90° correctly folded into Direction B (180/θ ∈ (1,2)); check-before-cut timing explicit everywhere; every invoked cut's parameter shown strictly interior; quantification over *every* Mulan move justified via Cut Lemma (3) converse. Congruence mod θ over ℝ and R1 (positivity needed for "residue 0 ⟹ positive multiple") defined before use. Answer stated explicitly and verified by substitution (both checks recomputed by me).
- **Progress: full solve from a round-1 empty baseline; sharpest bound (n − 1 cuts, matched exactly by my worst-case simulation).**

Outcome recorded: `verified-milestone`.

## Approach 2: descending-chain (`results/imo-2026-04/approaches/descending-chain.md`)

**Verdict: APPROVE. True Status: solved.** Builder's claimed Status is accurate. Independent of remainder-forcing in Direction A (different strategy: ignition/grind vs. one-cut forcing); Direction B is the same four-case closure, proved inline as required.

- **Correctness: 10/10.** Lemma 0 (cut formula, strict monotonicity + IVT bijection) correct. Lemma A1 (descent) correct — the refuted "largest multiple drops" monovariant is gone, replaced by tracked strong induction, with the θ = 15° counterexample recorded so it stays dead. Lemma A2 (ignition): s = θ − x validity via z ≥ 90° − x/2 hence z − s ≥ (90° − θ) + x/2 > 0 (uses θ ≤ 90°, true for all n ≥ 2) — verified; pieces (x, θ−x, (n−1)θ) and (y, z−θ+x, θ) match the formula; n = 2 degenerate case ((n−1)θ = θ) noted. Lemma A3 (grind): pieces (y, x−θ, z+θ) and (z, θ, x+y−θ); kept piece safe (residues y, x, z unchanged) with smallest angle exactly x − θ — all confirmed. Proposition A: trichotomy exhaustive/disjoint ((III) empty for n ≤ 3 since smallest angle ≤ 60°); grind count m ≤ n − 3 from x₀ < (n−2)θ; bounds n−1 / 2n−4 confirmed by simulation. Direction B (B1 safe start, B2 closure, Proposition B induction): correct, identical in substance to the certified lemma.
- **Completeness / rigor: 9.5/10.** One presentational (non-blocking) nit: Lemma A1's inductive step k ≥ 2 does not restate that if the current T *also* has an angle θ the check fires first (remainder-forcing's Step 2 does say this). Not a gap: the protocol restated at the top of the proof fires the check before any cut, and an early stop is a Mulan win within the bound — the strategy is only invoked when the game continues. Everything else fully quantified and case-complete.
- **Progress: full independent solve; slightly weaker bound (2n − 4 for n ≥ 4) — correctness unaffected.**

Outcome recorded: `verified-milestone`.

## Lemma certification: `lemmas/safe-piece-exists.md`

**CERTIFIED.** Self-contained (definitions, piece-formula setup with the strict-interiority and relabeling arguments, statement, four-case proof); statement is exactly what is proved (no overreach — hypothesis 180/θ ∉ ℤ used only in case (iv), and the importer remark correctly notes the lemma is *false* without it, which is the other half of the problem); quantification over every legal cut justified. Independently verified as described above (coordinate re-derivation + 436k adversarial exact-rational cuts). Status line in the file updated to CERTIFIED. Both approaches also carry the four-case proof inline this round, per the outline-reviewer's condition — confirmed present (remainder-forcing Step 6; descending-chain Lemma B2).

## current.md

Created (first write) per the file contract: **Status: solved**; Full proof = remainder-forcing's proof (leaner, sharper bound n − 1), with descending-chain recorded as the independent verified alternative; dead ends preserved under Approaches tried.

## Goal Progress

- **Status: `solved`** — `results/imo-2026-04/current.md` carries the full approved proof. Answer: **Mulan wins iff θ = 180°/n, n ∈ ℤ, n ≥ 2** (iff 180/θ ∈ ℤ); within n − 1 cuts.
- Per-slug verdicts: **remainder-forcing — APPROVE (solved, verified-milestone)**; **descending-chain — APPROVE (solved, verified-milestone)**.
- Lemma `safe-piece-exists` — certified.
- Ranking state after my `record_outcome` calls: remainder-forcing Elo 1516, descending-chain Elo 1484, both `last_outcome: verified-milestone`, `stale: true` (Elo update is the outline-reviewer's job, moot now that the run's goal is met).
- The run's goal is met. No further rounds needed on this problem.
