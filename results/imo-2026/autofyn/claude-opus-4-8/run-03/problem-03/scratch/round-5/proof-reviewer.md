# Proof-reviewer report — imo-2026-03, round 5

Problem is `compute_and_prove`, find-all style: `solved` requires BOTH bounds rigorous with the
closed form c(n) = 2^n/(2^{n+1}−1) stated and verified. All three approaches state the answer, but
only n = 1 is fully proven (both bounds); n ≥ 2 has open gaps in both directions. Overall Status
stays **partial**. No overclaiming found — all three builders honestly mark their gaps.

---

## 1. induction-peel — Verdict: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 5/5 · Completeness 3/5 (real gaps remain) · Progress: advanced.

**What I re-derived independently and confirmed:**
- **R3** (meas{N_X ≥ k} = x_(k)): trivial and correct — certified as **L13**.
- **R4** level-set identity ∫[D odd] − ∫D = 2(Σ_m B_{2m−1} − Σ_m A_{2m}). I re-derived the
  underlying *pointwise* identity f(d) = 2(Σ 1[d≤−(2m−1)] − Σ 1[d≥2m]) and checked it termwise
  (d = 0,±1,±2,±3,±4) — matches f(d)=1[d odd]−d. Numerically 0 mismatches / 3000 random Q_low,C.
  Certified as **L12**.
- **Case B (k_C = 0) closed forms** for A_{2m}, B_{2m−1}: re-implemented from the stated formulas
  and checked against direct step-function computation — 0 mismatches over 20000 legal Case-B
  configs (n = 2,3,4). The *reduction* of Case B to (CB) is rigorous.

**The load-bearing gap (still open, correctly flagged):** the reduction to (CB) Σ_m A_{2m} ≤
Σ_m B_{2m−1} does NOT prove (CB). (CB) is only *numerically* confirmed (0 violations / 60k). The
k_C ≥ 1 aggregate charging (1''') and the UB branch inequalities (gap 2, untouched this round)
remain open. Case B is a genuine reduction-of-scope advance, not a closure. Recorded `advanced`.

**Overclaim check:** the build report is accurate — it labels (CB) a sub-gap, not proven. Good.

---

## 2. alternating-sum-potential — Verdict: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 5/5 · Completeness 3/5 · Progress: advanced (a real slice closed).

**What I re-derived and confirmed:** the **Case 2b (c_n = 1) two-part-top-cut** proof. Key chain:
with a+b=2^n, a≥H, e = a−H = H−b (exact), truncation L6 gives S(B)=e+S(B_low); the L3 XOR split on
B_low = {H,b}⊔R gives S(B_low)=(H−b)+S(R)−2W with W ≤ meas[b,H) = H−b; hence
S(B)=2(H−b)+S(R)−2W ≥ S(R). Every step checks out, and the a=b=H boundary reduces to L9. Verified
numerically: S(B) ≥ S(R), 0 violations / 20000 random legal configs (n=2,3,4). This genuinely
closes the entire c_n = 1 slice. Certified as **L14**.

**Remaining gap (correctly flagged):** the residual Gβ is now exactly **c_n ≥ 2 and e < 1**,
reduced to the coupled overlap (Wβ) 2W ≤ e+S(Q_low)+(S(R)−1). The pointwise W ≤ S(Q_low) that
powers Case 2b is TIGHT at the cascade, so (Wβ) genuinely needs the lower-block surplus (global) —
still open. UB (G2) untouched. The obstruction map O1–O4 is prior-round material, re-affirmed.
Recorded `advanced`.

**Note on (Tβ)/β-reforge:** per my standing memory, β(B) ≤ 2^n−1 is EXACTLY equivalent to S(B) ≥ 1
— a reframing, not a closure. The builder states this explicitly (Spec concerns). No overclaim.

---

## 3. interlacing-bijection — Verdict: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 5/5 (what is written) · Completeness 2/5 (the crux is only sketched) ·
Progress: partial (new framing + one identity, no closure).

**What I confirmed:** **Lemma IB-1** is the SAME identity as induction-peel's R4 (A_j, B_j
level-set measures; Σ_{i≥0}B_{2i+1} = Σ_{m≥1}B_{2m−1}). It is correct and independently derived;
certified jointly as **L12**. The R2/L9 re-readings in this language are correct.

**The gap (honestly flagged, load-bearing):** the excess→deficit **injection Φ is the entire
content and is NOT constructed.** The builder is admirably explicit that the height-≤2
"clean-descent" slice is *indicated, not certified* ("the disjointness/nesting bookkeeping is
stated but not written out to full rigor... even the height-≤2 case is NOT true from ∫D ≤ 1
alone"). Heights ≥ 3 and the budget-driven totality are open. So this approach's net new rigorous
content is the reframing + IB-1 (= L12), not any new closed sub-case. The "budget essential"
numeric (free-Q violates PM 67/20000) is a supporting check, not a proof step. Recorded `partial`
(a genuinely new framing worth keeping, but no gap closed beyond the shared identity). No overclaim.

---

## Certified this round (into lemmas/)
- **L12** level-set/crossing form of (PM) — ∫[D odd]−∫D = 2(Σ B_{2m−1} − Σ A_{2m}); (PM) ⟺
  odd-down time ≥ even-up time. (= induction-peel R4 = interlacing IB-1.) EQUIVALENT recasting,
  NOT a closure.
- **L13** meas{N_X ≥ k} = x_(k) + single-block sum bound Σ s_k ≤ 2^n.
- **L14** two-part top-cut closure: S({a,b}⊔R) ≥ S(R); closes the c_n = 1 slice of the LB.

**NOT certified:** the Case-B closed forms (correct but narrow, and entangled with the still-open
(CB)); the height-≤2 injection slice (self-flagged as not rigorous).

## Standing crux (unchanged in shape, narrowed in scope)
- **LB residual:** c_n ≥ 2 ∧ e < 1 — (PM) Σ B_{2m−1} ≥ Σ A_{2m} / coupled (Wβ) / (CB) for k_C=0.
  Still OPEN; needs a global argument consuming the single-block part budget + origin-group sums.
- **UB:** the MATCH/BISECT branch inequalities U_{k−1}(c(A)) ≤ sum/D_k for arbitrary A — the
  SOLE fully-open second crux, untouched all three approaches this round. Field still needs a
  genuinely different UB framing (per round-4 directive).
