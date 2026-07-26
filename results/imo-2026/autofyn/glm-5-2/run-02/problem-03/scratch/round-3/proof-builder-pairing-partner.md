# proof-builder — pairing-partner (round 3)

Slug: `pairing-partner`. Approach file: `results/imo-2026-03/approaches/pairing-partner.md`. Status: **partial**.

## What was assigned (Engine C)
Close G1 (Lemma L general-n k≥2 — the interleaving obstruction) via a GLOBAL weight-function / charging inequality that BYPASSES the per-k interleaving/WLOG-k=1 decomposition. Reviewer required fixes: (1) find the hybrid w (size + local-rank) with A ≥ Σw ≥ α(n), tight at pair-pile; (2) OWN the even-piece-count sub-case.

## What was actually achieved (rigorous)
The weight-function `w` itself was NOT found (the reviewer's "honest bet" — if no hybrid w exists, this route dies — landed on the not-found side for general reals). But three new rigorous results were produced that *localize* the obstruction precisely:

1. **(R1) The reduction `L(n+1) ⟺ e_M ≤ o_R`** — a clean reformulation of Lemma L(n+1) purely in terms of the global alternating-pair merge of the M-sub-pieces and the R'-pieces. `e_M` = sum of M-sub-pieces at global EVEN ranks; `o_R` = sum of R'-pieces at global ODD ranks. Lemma L(n+1) is EXACTLY `e_M ≤ o_R`, independent of k. This localizes the interleaving obstruction to a single inequality between two sub-sums (no per-k classification, no WLOG-k=1 exchange). Verified: exact enumeration n=1,2,3 grid + 500k random reals n=2, 0 violations.

2. **(R2) Integer-grid parity theorem** — for every grid-aligned (marks at multiples of 1/D(n)) refinement of the level-n dyadic, A ≥ 1/D(n). Proof: scale by D(n) (ODD); pair-excesses e_i ≡ q_{2i−1}+q_{2i} (mod 2), so Σ e_i ≡ D(n) ≡ 1 (mod 2), a non-negative odd integer ≥ 1. Rigorous but restricted — does NOT lift to reals (finer odd grid gives weaker bound 1/(K·D(n))). This is a genuine new result for the restricted class and reveals the parity mechanism.

3. **(R3) n=1 real case fully closed** — for Liu config (1,2)/3, every real Xiang response gives A ≥ 1/3 = α(1), equality iff the mark lands in the largest piece 2/3. Mechanism: splitting 2/3 into (2/3−a, a) sends the small fragment a to rank 3 (odd, +a) and the large fragment to rank 1 (−a from original 2/3); the ±a cancel, so A = 1/3 exactly, independent of a. Complements the grid theorem and the round-1 n=1 grid proof — n=1 is now real-valued end-to-end.

Also produced the **self-compensation pairing lemma**: in the merged sort paired (p_1,p_2),(p_3,p_4),…, every pair of type (odd R', even M-sub) self-compensates (r_odd ≥ m_even by sorted order), so e_M ≤ o_R reduces to the residual Σ_{MM pairs} m_even ≤ Σ_{RR pairs} r_odd — a Hall-type matching. This residual (Match) is verified (0 violations n=2,3 grid + n=2 reals 500k) but is the open analytic step.

## Honest assessment
- The hybrid weight-function w was NOT found. Pure-size w cannot detect the pair-pile's multiplicity parity (the explorer's obstruction); a hybrid size+local-rank w would essentially re-derive the alternating sum A itself (circular). The reduction (R1) + self-compensation is the viable alternative to an explicit w, but its residual (Match) is unproven for general reals.
- Conjecture (S) "smallest piece ≥ α(n) at the minimizer" is FALSE for reals (verified: Xiang can split a piece to make a sub-α fragment; the fragment cancels at an odd rank, so A ≥ α(n) survives but CK cannot detect it). So the odd-count cheap-kill does NOT lift off the grid.
- The even-count sub-case (pair-pile-type extremals, e_M = o_R = 0) IS Engine C's distinctive ownership and is where the self-compensation reduction lives — but its residual (Match) is the open handle.
- Status stays partial: G1 (k≥2 reals) and G2 (regime-N upper bound, delegated to two-regime-disjunctive) both remain open.

## Promotable lemmas (proposed for certification)
- (R1) Reduction `L(n+1) ⟺ e_M ≤ o_R`.
- (R2) Integer-grid parity theorem.
- Self-compensation pairing lemma.
- CK (odd-count cheap-kill, real-valued, one-line).

## Lesson for next round
The residual (Match) — `Σ_{MM pairs} m_even ≤ Σ_{RR pairs} r_odd` — is the live handle. It is a Hall-type matching condition (match each MM-pair's smaller half to a distinct RR-pair's larger half ≥ it). The superincreasing structure of R (each R-piece exceeds the sum of all smaller R-pieces by 1/D(n+1), the level-boundary excess) is the structural lever expected to close it. If the matching can be proved via the superincreasing dominance, G1 closes cleanly for all reals. If not, the field needs a framing far from both weight-function and extremal-swap (a structural/topological or probabilistic argument on the sorted multiset).
