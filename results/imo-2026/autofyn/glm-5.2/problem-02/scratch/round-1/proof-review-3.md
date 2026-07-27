# Proof review: imo-2026-02 (OM = ON) — round 3 (final)

**Candidate status (as written):** solved
**My judgement: solved** — the §3 sign argument has been correctly rewritten; the two compensating errors from round 2 are fixed exactly as recommended (Option A). The proof is now complete and rigorous.
**Verdict: APPROVE**

---

## Summary

| Section | Status | Notes |
|---|---|---|
| §1 Reduction (homothety + Thales) | ✓ complete, rigorous | unchanged from rounds 1–2; sound. |
| §2 Direction Lemma ∡(BC,BA')=90°−A−α | ✓ complete, rigorous | genuine polynomial certificate, exact pseudodivision remainder 0, non-vacuous, **signed +θ**. |
| §3 B↔C symmetry | ✓ now correct & rigorous | the orientation-reversal sign flip is applied at the right step; the spurious CB→BC flip is removed; conclusion holds. |

The conclusion OM = ON is fully established: §1 reduces OM=ON to |A'B|=|A'C|; §2 + §3 give ∡(BC,BA')=+θ and ∡(BC,CA')=−θ (equal-and-opposite), forcing A' onto perp-bis(BC).

---

## 1. Independent verification performed (re-derived from scratch)

### 1a. The certificate g = C·T is genuine (re-confirmed)

Re-ran `certverify.py` and re-derived the entire pipeline (parametrisation → conK/conL → A' → G → g → C → certificate):

- **`g·Td − C·Tn == 0` as a rational identity in the free ring** ℤ[s_α, c_α, s_A, c_A, t_β, t_γ]: **True**. Cleared numerator: **0 ops** (identically zero). ✓
- **Pseudodivision route** (`dirdiv3.py`): dividing the cleared numerator of g by the cleared numerator of C as polynomials in t_γ over the fraction field ℚ(s_α, c_α, s_A, c_A)(t_β): **remainder is zero** (deg_tγ C=4, deg_tγ g=7). This is an exact polynomial division in a polynomial ring over a fraction field — fully rigorous, no numerical approximation. ✓
- **Non-vacuous** (the round-1 trap was `F = L1·conK + L2·conL`, vacuous when conK, conL are independent): at a random free-indeterminate eval (sa=0.37, ca=0.91, sA=0.52, cA=−0.83, tb=0.6, tg=1.4): **g = −9.36e−2 ≠ 0** and **C = 5.44e−1 ≠ 0**. So C=0 is a proper subvariety and g vanishing on it is a genuine constraint. This is a real polynomial divisibility, not a trivial ideal-membership. ✓
- **Free in s_α, c_α, s_A, c_A** (no Pythagorean relation imposed on α, A): the half-angle substitution bakes in sin²β+cos²β=1 and sin²γ+cos²γ=1 (legitimate — β, γ are real angles), while s_α, c_α, s_A, c_A remain free. An identity in the free ring holds a fortiori under specialization to the actual trig values. ✓

### 1b. The certificate proves SIGNED +θ (not unsigned parallelism)

On a concrete valid config (A=55°, α=25°): G(+θ) = (A'−B) × R_{+θ}(C−B) ≈ **0**, while G(−θ) ≈ **−0.185 ≠ 0**. Same pattern on all 4 tested configs (G(−θ) ∈ {−0.175, −0.185, −0.384, −0.177}). The certificate is specific to +θ = +(90°−A−α), the signed directed angle. This is essential because §3 needs the signed value. ✓

---

## 2. §3 — the rewritten sign argument is now CORRECT and RIGOROUS ✓

This was the gap in round 2 (two compensating errors). The rewritten §3 (lines 93–108) applies the fix exactly as round 2's Option A recommended.

### 2a. The corrected chain

1. **Relabeling σ** (B↔C, M↔N, K↔L, β↔γ, fixes A, α, A'). Verified: σ produces a valid config with α'=α, β'=γ, γ'=β — all six angle hypotheses hold (the three conditions are merely permuted). A' is fixed because σ exchanges the two perpendiculars A'K⊥AK and A'L⊥AL whose intersection defines A'. ✓

2. **The relabeled triangle (A,C,B) is CW** (reverse orientation): original ABC is CCW (C above x-axis); relabeled ACB is CW. ✓

3. **Orientation-reversal sign flip applied at the right step.** §2 was proved in a CCW frame and yields the SIGNED value ∡(BC,BA')=+θ. The relabeled config is CW; to apply the CCW-framed lemma we reflect CW→CCW, and a reflection is orientation-reversing, negating directed angles. Transferring back to the original frame: **∡(CB, CA') = −θ = −(90°−A−α).** ✓ This is the step that was WRONG in round 2 (round 2 wrote +θ here, missing the flip); it is now correct.

4. **Line CB = line BC (mod π), no further flip.** The proof correctly notes "directed angles are taken modulo π between (undirected) lines, the line CB is the same line as BC, so no further sign is introduced: ∡(BC, CA') = ∡(CB, CA') = −(90°−A−α)." ✓ This is the step where round 2 introduced a SPURIOUS flip; the spurious flip is now removed. Reversing a line adds π to its direction, which is 0 mod π, so no sign change. Verified numerically: ∡(CB,CA') = ∡(BC,CA') = −θ on all configs.

### 2b. Numerical confirmation of the corrected §3 (8 configs)

Re-ran `signcheck_final.py` across 8 valid configs (varying A∈{35,45,50,55,65,70,75,80}, α∈{5,8,10,15,18,20,25,30}):

| A | α | θ | ∡(BC,BA') | ∡(CB,CA') | ∡(BC,CA') | \|A'B\|−\|A'C\| |
|---|---|---|---|---|---|---|
| 70 | 15 | +5° | +5.0000° | −5.0000° | −5.0000° | −6.7e−16 |
| 55 | 25 | +10° | +10.0000° | −10.0000° | −10.0000° | −4.4e−16 |
| 45 | 18 | +27° | +27.0000° | −27.0000° | −27.0000° | +2.7e−12 |
| 65 | 8 | +17° | +17.0000° | −17.0000° | −17.0000° | −7.1e−15 |
| 50 | 30 | +10° | +10.0000° | −10.0000° | −10.0000° | +9.8e−15 |
| 35 | 20 | +35° | +35.0000° | −35.0000° | −35.0000° | −1.6e−12 |
| 75 | 5 | +10° | +10.0000° | −10.0000° | −10.0000° | −1.6e−15 |
| 80 | 10 | 0° | −0.0000° | +0.0000° | +0.0000° | −4.4e−16 |

Every config: ∡(BC,BA')=+θ, ∡(CB,CA')=−θ, ∡(BC,CA')=−θ (no flip), and |A'B|−|A'C|≈0. The corrected §3 reasoning matches the numerics exactly. ✓

### 2c. The base-angles-equal ⟹ isosceles conclusion holds (no circularity)

From (∗) and (∗σ): ∡(BC,BA')=+θ and ∡(BC,CA')=−θ. The two lines BA', CA' make equal-and-opposite directed angles with BC. I independently verified by coordinates (place B=(0,0), C=(d,0)): line BA' through B with direction θ, line CA' through C with direction −θ intersect at **A'=(d/2, (d/2)tan θ)** — the x-coordinate is d/2, exactly the perpendicular bisector of BC. This is a direct, non-circular derivation of A'∈perp-bis(BC). ✓ (θ≠π/2 is guaranteed since θ=π/2 would force A+α=0, impossible for positive A,α.)

The proof's route via "∠A'BC=|∡(BC,BA')|=|θ|=|∡(CB,CA')|=∠A'CB ⟹ isosceles" is also valid: in this symmetric configuration both interior angles equal |θ| (verified by coordinates — A' lies at (d/2,(d/2)tanθ), on the side consistent with the directed angle, so each interior angle = |θ|, not π−|θ|). The conclusion |A'B|=|A'C| follows. No circularity: §2 and §3 give the two signed angles independently (§2 by certificate, §3 by applying §2 to the relabeled config with the orientation flip); the isosceles deduction uses only these two angle values. ✓

---

## 3. Remaining-gap scan — none found

- **§1 homothety**: h(A,1/2) sends B↦M, C↦N; maps perp-bis(BC)→perp-bis(MN) bijectively (similarity preserves equidistance up to the common 1/2 scale); h⁻¹(O)=2O−A=A'. So OM=ON ⟺ A'∈perp-bis(BC) ⟺ |A'B|=|A'C|. Sound. ✓
- **A' well-defined (K×L≠0)**: A,K,L non-collinear is given (else O, the circumcentre of △AKL, would be undefined). ✓
- **k₁=sin(α+γ)≠0**: interior-angle range 0<α+γ<C≤π forces sin(α+γ)>0; similarly sin(α+β)>0. All divisions by these are legitimate. ✓
- **Td≠0 concern (round 2 minor)**: the "g=C·T" phrasing requires Td=(t_γ²+1)·Φ≠0 on the locus. Rescued by the pseudodivision route (ghn=Chn·Q, remainder 0), which works with cleared numerators whose denominators are products of (1+t_β²),(1+t_γ²) powers — always positive. The proof mentions both formulations; the pseudodivision is the rigorous one. Not a gap. ✓
- **Problem match**: task=proof_only, answer_type=none. The proof proves OM=ON — exactly what is asked. No numerical answer to verify. ✓

---

## Scores

- **Correctness: 5/5** — §1 sound; §2 certificate genuine (exact pseudodivision remainder 0, non-vacuous, signed +θ); §3 sign argument now correct (orientation-reversal flip at the right step, no spurious CB→BC flip), verified numerically on 8 configs and by independent coordinate derivation.
- **Completeness / rigor: 5/5** — every step justified; all cases covered (θ>0, θ<0, θ=0 all give A' on perp-bis); tools named (Thales, homothety, polynomial pseudodivision); no hand-waving.
- **Progress: 5/5** — the round-2 gap (§3 sign handling) is fully closed; the proof is now complete.

---

## Verdict: APPROVE

**Status: solved.** The proof is complete and rigorous. The two compensating sign errors identified in round 2 have been corrected exactly as recommended (Option A): the orientation-reversal sign flip is now applied at the σ-application step (yielding ∡(CB,CA')=−θ), and the spurious CB→BC sign flip has been removed (correctly: line CB = line BC mod π introduces no flip). The corrected chain ∡(BC,BA')=+θ, ∡(BC,CA')=−θ ⟹ equal-and-opposite ⟹ A'∈perp-bis(BC) ⟹ |A'B|=|A'C| ⟹ OM=ON is sound, independently verified both numerically (8 configs) and by coordinate derivation. The recorded Status `solved` is **correct**.

The proof is complete and rigorous.
