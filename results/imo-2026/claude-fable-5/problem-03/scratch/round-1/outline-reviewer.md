# Outline review — round 1 — imo-2026-03

Target claim checked: c(n) = 2^n/(2^{n+1} − 1), D = 2^{n+1} − 1. All three slugs target the whole problem (both bounds, answer stated) — no fragment/single-line-split problem. The rivalry note holds: the three lower-bound mechanisms (G4 mass-balance recursion, L1 self-similar induction, E3 discrete parity) and the two upper-bound architectures are genuinely distinct; the shared C/D/F lemmas are routine cache candidates, not a load-bearing shared gap. No recorded dead ends exist yet (fresh workspace).

Independent checks I ran this round:
- Lemma C (claiming value = Odd(P)) is the standard greedy/exchange result — sound.
- Doubling-chain lemma (approach 1, Step 4): verified the induction q_j > 2^{n+1−j}/D closes and Σq > 1 — sound and exact.
- k = 1 lower-bound accounting (approach 2, Step 2): checked the symmetric-difference identity {N_P odd} = A Δ B (parity of N_S + N_R), B ⊆ (0, M] since max piece of R is M, and |A Δ B| ≥ (s_1 − M) + |B| − (M − s_2) = |B|. Correct as written.
- Lower bound at n = 2: fine-grid search over all ≤ 2-mark replies to G_2 = {1,2,4}/7 gives min Odd = 4/7 exactly (tight, zero slack). Consistent with all three lower-bound plans.
- IH′ calibration (approach 2): Σ_{j=2}^{k+1} 2^{n+1−j} = 2^n − 2^{n−k} — exact equality, induction correctly calibrated.

---

## pairing-defect-strategy-family — APPROVE

Route is sound: Odd-reduction → defect identity → n-mark WLOG → strategy family + chain lemma (upper) / mass-domination recursion (lower). The chain lemma is verified; the file already records that cascades are load-bearing (counterexample q = (0.49, 0.345, 0.165)) and that the per-position bounds are false — both correct and important warnings. Gaps G3/G4 are honestly flagged with plausible mechanisms.

Builder notes (not blockers):
1. G3 (deficient-case cascade): the cascade-selection rule must also verify the MARK count ≤ n in every branch — each matched pair costs one cut, but the terminal remainder chain must not overrun the budget; keep an explicit ledger.
2. G4: the "cross pair's S-side ≤ partner + gap" inequality in Step 5 needs the pair-gap summed once globally, not once per cross pair — write the mass balance so the total defect appears only once.
3. Prove and file Lemmas C, D, F under `lemmas/` first (shared with the siblings).

## self-similar-induction — APPROVE (with one concrete hole to fix — CHANGES REQUESTED items folded into the build)

The induction architecture is the most advanced: base n = 1 complete, lower-bound k = 0 and k = 1 cases proven (k = 1 accounting checked, correct), upper-bound IH′ exactly calibrated. L1 (k ≥ 2) is the honest hard gap with sensible repair candidates.

**Hole found in Step 3's exhaustion argument (must be fixed, it is stated as if closed):** "if no usable k exists then q_j < 2^{n+1−j}/D for ALL j, contradiction" is FALSE as written. The k-selection requires the threshold for a *prefix* 2 ≤ j ≤ k+1, so it can fail at j = 2 while holding at j = 3. Concrete counterexample, n = 3, D = 15: q = (0.35, 0.245, 0.235, 0.17). Here q_1 < 8/15, q_2 < 4/15 (no k = 0, no k ≥ 1), yet q_3 = 0.235 ≥ 2/15 — no contradiction, and no strip move per the stated rule. The config IS beatable: cascade q_1 → (0.245, 0.105), q_3 → (0.105, 0.13), q_4 → (0.13, 0.04) gives Odd = 0.52 < 8/15 with exactly 3 marks. Also checked: the file's U1 fallback "cut the larger of a near-pair down to the smaller" does NOT close this config (reduced-instance IH′ gives defect ≤ 0.53/7 ≈ 0.0757 > 1/15). So U1 is really medium-hard and the selection rule needs cascade-like moves (or an extended IH′ "m marks vs ≤ m+1 pieces" plus a smarter matching) — the builder must treat the whole upper-bound case analysis, not just the feasibility branch, as open. Record this counterexample in the approach file.

Second note: state and prove the trivial extension of IH′ to configurations with FEWER than m + 1 pieces (extra marks: halve everything extra, defect monotone) — it is used implicitly when strips reduce piece count.

## exact-value-function — CHANGES REQUESTED

The LP-vertex route (E1) is legitimate in principle and its payoff (discrete parity at the geometric config) is attractive. But two stated mechanisms are defective:

1. **The integrality claim in E3 is false as stated.** "Vertex replies produce sizes in ½ℤ" ignores equipartition vertices: within one piece, the equalities s_a = s_b = s_c are legitimate polytope facets, so a vertex can cut a piece into k ≥ 3 EQUAL parts, producing sizes q_i/k — thirds, fifths, etc., not half-integers. The parity argument "leftover ≥ 1 unit" then degrades to "leftover ≥ 1/k unit", which is not enough. The conclusion is still numerically true (my n = 2 grid check found min Odd = 4/7 exactly, including equipartition-type replies), so the route is not dead — but E3 must either (a) prove equipartitions into ≥ 3 parts are always dominated by match/halve replies, or (b) run the parity argument per denominator class. Fix the mechanism statement in the file before building on it.
2. **E1 vertex classification is broader than "match/halve/cascade".** Vertices of an n-dimensional cut-position polytope are intersections of n tight constraints drawn from cross-piece ties, same-piece ties (→ equipartitions), and boundary cuts (→ marks coalescing / fewer effective marks). The classification must enumerate all three families, not just the two named. The "fewer effective marks" boundary also interacts with Lemma F's parity weapon — handle explicitly.

These are fixable, and this slug's lower-bound mechanism is the only one of the three that avoids the analytic defect estimate, so it earns a place in the population. But its foundation is the riskiest; it builds third priority.

---

## Ranking and registration

Registered all three (new, cold-start 1500). Comparisons applied:
- self-similar-induction vs pairing-defect-strategy-family: **draw** (slug 2 has the most proven content — k = 1 case, calibrated IH′ — but I found a concrete hole in its upper-bound case analysis; slug 1's chain lemma is verified sound and its cascade requirement was validated computationally).
- self-similar-induction beats exact-value-function (proven subcases vs a defective mechanism statement).
- pairing-defect-strategy-family beats exact-value-function (verified core lemma vs risky foundation).

Post-update Elo: pairing-defect-strategy-family 1517, self-similar-induction 1515, exact-value-function 1469.

## Build set

All three build this round — the two leaders on their hard gaps (G3/G4; L1 + the exhaustion-hole repair), and exact-value-function on repairing E1/E3's mechanism (test the equipartition-domination claim numerically at n = 2, 3 before proving). Every builder proves/imports Lemmas C, D, F first and files them under `results/imo-2026-03/lemmas/` for certification.

build set: pairing-defect-strategy-family, self-similar-induction, exact-value-function
