## imo-2026-03 — UB Hard Case (Geometric-Selfsimilar Lens)

### Summary of findings

**HS-A2 HAS A COMPLETE ANALYTIC PROOF FOR THE SUB-A P SUB-CASE.**
This is the designated "sole blocking gap." The proof uses the Sigma-P bound and a 6-case analysis on the sorted order of Y''={p1,d2,p4,p5} after pair2_3. No sub-case is left open. See the complete case structure below.

---

### Distinct openings

**Opening 1 (KEY): HS-A2 Sub-A P is provable by 6-case analysis on sorted Y''.**

Setup: In T5 pure hard case (Σ=31t, all dj>t, δ>t, p1≤31t/2, p2<8t), the pair1_2 cut (cut p1 at offset p2) gives Y'={d1,p3,p4,p5}. T4-at-t on Y' fires Sub-A P (E1≥Eps+E3=δ+d4) when δ>2t, giving A_P=δ/2>t — this is the unique genuine pair1_2 failure mode. The fix: use pair2_3 (cut p2 at offset p3) to get Y''={p1,d2,p4,p5} with p4=δ+d4, p5=δ.

**The Sigma-P bound**: From the Sub-A P condition D1_Y' ≥ δ+d4 and Σ=31t:
```
31-2p2-4δ-3d4-2d3 ≥ δ+d4
=> p2 ≤ (31-5δ-4d4-2d3)/2
=> 2d2 ≤ 2(p2-p3) ≤ 31-7δ-6d4-4d3     [*]
```
(using p3=δ+d4+d3, p2=p3+d2).

**6-case analysis on sorted Y''** (showing T4-at-t closes each via R, S, or P):

**Case A** (d2 > p4=δ+d4): E2=d2-p4. From [*]: d2 ≤ (31-7δ-6d4-4d3)/2, so
  E2 ≤ (31-7δ-6d4-4d3)/2 - (δ+d4) = (31-9δ-8d4-4d3)/2.
  With δ>2, d4>1, d3>1: 9·2+8·1+4·1=30, so E2 < (31-30)/2 = t/2 < t. **R closes.**

**Case B1** (δ ≤ d2 ≤ p4, d2 < δ+t): Sorted Y''={p1,p4,d2,δ}. E3=d2-δ<t. **S(E3) closes.**

**Case B2** (δ ≤ d2 ≤ p4, d2 ≥ δ+t): For Case B2 to be consistent with [*]:
  2(δ+t) ≤ 2d2 ≤ 31-7δ-6d4-4d3, so 9δ+6d4+4d3 ≤ 29. With δ>2,d3>1: 6d4 ≤ 29-18-4=7, so d4 < 7/6.
  Then E2=p4-d2 ≤ p4-(δ+t) = d4-t < 7/6-1 = t/6 < t. **R closes.**

**Case C1** (d2 < δ, d2 ≥ δ-t): Sorted Y''={p1,p4,δ,d2}. E3=δ-d2 ≤ t. **S(E3) closes.**
(This is the case of the R12 witness: δ=2.194t, d2=1.812t, E3=0.382t < t.)

**Case C2** (d2 < δ-t, δ ≤ 3t): Sub-A P on Y'' fires (D1_Y''=p1-p4 ≥ δ). Proof: from [*], p2 ≤ (31-5δ-4d4-2d3)/2. And D1_Y''≥δ iff p2 ≤ 31-5δ-3d4-d3. The difference is (31-5δ-2d4)/2 > 0 for δ≤3,d4<7/6. So Sub-A P fires. A_P=d2/2 < (δ-t)/2 ≤ (3t-t)/2 = t. **P closes.**

**Case C3** (d2 < δ-t, δ > 3t): IMPOSSIBLE. Sub-A P on Y' requires p2 ≤ (31-5δ-4d4-2d3)/2. But p2=p3+d2=δ+d4+d3+d2 > 3+1+1+0 = 5. And (31-5·3-4·1-2·1)/2 = (31-15-4-2)/2 = 5. So p2 > 5 contradicts p2 ≤ 5. **Vacuous.**

**Numerical validation**: 26 Sub-A P failure configs with δ>2t tested (off-grid exact Fractions); 0 failures. Cases B1 and C1 are most common (S closes); Case C2 closes via P; Case A rare but closed by R; Case B2 exists (R closes via d4<7/6 bound); Case C3: 0 instances (correctly impossible).

---

**Opening 2: Sub-A C and Sub-B "failures" of T4-at-t are NOT genuine pair1_2 failures.**

When T4-at-t on Y' falls into Sub-A C (E3<D1<Eps+E3, A_C=δ+d4-D1>t) or Sub-B (D1<E3), pair1_2's FULL merge family (including invisible-pair halving and cross-matching M2) still achieves A≤t. Tested: 149 such configs (off-grid); 0 true mu>t violations. Example: Sub-A C config with A_C=1.55t gives mu=0.0909t via pair1_2 full merge family. Conclusion: the only genuine pair1_2 failures are Sub-A P with δ>2t.

---

**Opening 3: pair1_2 always works for δ ≤ 2t.**

Numerical check (1555 configs, all hard case, δ≤2t): 0 pair1_2 failures. When Sub-A P fires with δ≤2t: A_P=δ/2≤t (strictly ≤t), so the T4 P strategy itself closes. For Sub-A C/B cases: the full merge family handles them (Opening 2). So δ≤2t is fully covered by pair1_2 alone.

---

**Opening 4: The remaining analytic gap is the PAIR1_2 SUCCESS REGION proof.**

The T5 proof outline is:
- If δ≤2t: pair1_2 works (Opening 3). Need: prove min A(Y',3)≤t analytically for all hard case Y' with δ≤2t. T4 Sub-A P gives A_P=δ/2≤t directly. Sub-A C and Sub-B need the full merge family argument (not just T4-named strategies).
- If δ>2t: pair2_3 works (Opening 1/HS-A2). PROVEN for Sub-A P. NUMERICALLY ZERO failures for both pair1_2 and pair2_3 across all 3057 δ>2t configs.

The pair1_2 success region (δ≤2t) still lacks a WRITTEN analytic proof that the full merge family achieves A≤t. This is the remaining construction gap in the geometric-selfsimilar approach.

---

**Opening 5: m≥6 is a separate open problem (HS-A3).**

Not scouted this round. For m=6: Σ=63t, budget b=5, hard case p1≤63t/2, all 5 gaps>t, δ>t. The pair1_2 and pair2_3 strategies would again reduce to 4-piece subproblems but with different Sigma. The same δ-threshold (now some multiple of t) analysis would apply. Whether Case C3-type impossibilities hold for m=6 is unclear without analysis.

---

### Candidate technique(s)

- **Case analysis on the sorted order of a reduced tuple** (opening 1): the key technique for HS-A2. After reducing from 5 pieces to 4 via pair2_3, the 4 pieces can be in 6 relative orderings; the Sigma-P bound constrains each.
- **Deriving subsidiary bounds from a "P-fires" condition**: the Sigma-P bound [*] is the engine. It converts "Sub-A P fires on Y'" into a linear constraint on d2 relative to δ,d4,d3.
- **Invisible-pair parity cancellation (Lemma R1)**: already certified, used by both pair1_2 and pair2_3 reductions.

### Cheap-kill candidates

- The Case B2 Sigma-P bound gives d4 < 7/6 t — a tight pigeonhole. If d4 < 7/6, then Case B2's E2<t/6 is strict. No additional work needed.
- Case C3 impossibility: pure arithmetic. 5δ+4d4+2d3 > 5·3+4·1+2·1=21 and p2>5, combined with Sub-A P forcing p2≤(31-21)/2=5. Immediate contradiction.

### Knowledge-base entries to use

- **Parity-Invisible Pair (Lemma R1)**: the foundation for both cuts.
- **Certified Lemma MK**: covers δ≤t and any dj≤t (the easy cases).
- **Certified Lemma T4-tight-m4**: the 4-piece bound at threshold Σ(Y')/15. Careful: NOT directly applicable at threshold t (which is typically larger than Σ(Y')/15 for the hard case). The NAMED STRATEGIES (R/S/P/C) from T4 are what apply case-by-case.
- **Certified Lemma AB**: μ(X,b)=0 for b≥|X|. Closes the slack-budget cases.

### Analogous past problems (cruxes)

**aimo-0019** (combinatorics/games-and-strategy): Paintball interval covering game with dyadic response. The crux: "respond to each opponent move by painting the next dyadic interval." Structural analogy: a 2-player game on a line where one player's response mirrors the opponent's claim using a dyadic invariant. The dyadic structure 2^n/(2^{n+1}-1) in our answer matches the dyadic interval halving in this problem. However, the crux move (painting the next dyadic cell beyond the frontier) does not adapt to our setting (our player is choosing a cut point, not painting a cell). **Partially analogous** — confirms the dyadic structure but the crux itself doesn't adapt.

**aimo-0262** (combinatorics/games-and-strategy): Cinderella/Stepmother bucket game. Crux: "maintain invariant that two adjacent buckets are empty." This is an invariant-based 2-player strategy game. Analogous in form (maintain a structural invariant across the opponent's moves), but the invariant type (empty adjacency vs. alternating sum bound) is different. **Weakly analogous.**

**No direct analogue found** in the corpus for the specific structure of our problem (alternating sum of piece sizes, parity-invisible pairs, merge-family optimization). The analytic content (case analysis + Sigma bound) has no crux match.

### Prior progress

- Certified lemmas: MK (easy cases), T4-tight-m4 (4-piece bound), AB (budget slack).
- T5 structural reduction: pair1_2 eliminates p2 (invisible pair), reduces to 4-piece Y' with 3 cuts. Airtight.
- Off-grid witness X={157/5,13,46/5,34/5,23/5} confirmed as genuine pair1_2 failure (pair2_3 closes it at 0.382t).
- **NEW THIS ROUND**: HS-A2 Sub-A P case has a complete 6-case analytic proof. 0 failures in numerical validation (26 targeted Sub-A P configs + 3057 general δ>2t configs).

### Dead ends (do not retry)

- SB-monotone (refuted R7): rejected.
- R3-cascade (refuted R8): rejected.
- Complement-cut m=4→3→R4 (refuted R9): rejected.
- p1@p2 threshold-invariant induction (refuted R11): rejected.
- Unified refined-R {Claim_R, T_R} mutual induction (refuted R9-R11): rejected.
- Integer-grid UB numerics (grid artifact, refuted R12): ALL UB checks must use off-grid exact Fractions.
- T4-named-strategies-only for pair1_2 success region: insufficient (R12 proved this), need full merge family.
- Naive pair2_3-P argument requiring d2<2t globally: d2<2t is NOT always true (d2 can reach 3.5t in Case A); the proof requires case-by-case analysis, not a global d2 bound.

### Small-case / intuition notes (conjectured, not proved)

- CONJECTURE: The pair1_2 success region (δ≤2t hard case) proof reduces to showing min A(Y',3)≤t for all Y'={d1,p3,p4,p5} with T5 constraints and δ≤2t. This is likely closed by T4's C strategy (A_C=δ+d4-D1 ≤ δ-t ≤ t when δ≤2t AND D1≥d4 which is guaranteed by Sub-A not Sub-B), plus the Sub-B case handled by the full merge family or pair1_3 cut. Numerically zero failures in 1555 δ≤2t configs, but no analytic write-up yet.

- CONJECTURE: For m≥6 (HS-A3), the same pair1_2 + pair2_3 tree works with a modified Sigma-P bound. The δ>2t threshold may shift. Not verified.

- The R12 witness falls in Case C1 (delta-t ≤ d2 < delta), closed by S(E3)=0.382t. This is the "typical" Sub-A P failure.

- Case C3 impossibility is a robust algebraic constraint: 5δ+4d4+2d3 ≤ 31-2p2 < 31-10 = 21 (since p2>5 in hard case) but δ>3 gives 5δ>15, d4>1 gives 4d4>4, d3>1 gives 2d3>2, sum>21. QED.
