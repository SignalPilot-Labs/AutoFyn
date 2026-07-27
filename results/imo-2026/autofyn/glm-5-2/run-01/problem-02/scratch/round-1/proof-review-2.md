# Proof review: imo-2026-02 (OM = ON) — round 2

**Candidate status (as written):** solved
**My judgement: partial** (the proof's §3 has a genuine sign-handling error; the conclusion is correct but the reasoning is not rigorous)
**Verdict: CHANGES REQUESTED**

---

## Summary

The proof has three parts:

1. **§1 The antipode/homothety reduction** — fully rigorous and complete. ✓
2. **§2 The Direction Lemma ∡(BC, BA') = 90° − A − α** — proved by a genuine, non-vacuous polynomial certificate. The certificate is verified and proves a SIGNED directed angle (not just unsigned parallelism). Essentially complete (one minor concern about Td ≠ 0 on the locus, addressable via the pseudodivision route). ✓
3. **§3 The B↔C symmetry** — the **conclusion** ∡(BC, CA') = −(90° − A − α) is **correct** (numerically verified to ~1e-12 on 6 configs), but the **proof's reasoning has a sign-handling error**: two compensating mistakes that produce the right answer by coincidence. This is a **gap**.

---

## 1. §1 Reduction — SOUND (no change from round 1)

OM = ON ⟺ A' ∈ perp-bis(BC) ⟺ |A'B| = |A'C|, via homothety h(A, 1/2) and Thales. Re-verified: A'K ⊥ AK, A'L ⊥ AL (antipode on (AKL)), h maps perp-bis(BC) → perp-bis(MN), h⁻¹(O) = A'. No issues. ✓

---

## 2. §2 Direction Lemma — CERTIFICATE IS GENUINE AND NON-VACUOUS ✓

I independently re-derived the entire pipeline (parametrisation, conK/conL, A', G, g, C) and verified the certificate.

### 2a. Setup is correct

- Frame: A = origin, B = (1,0), C = (b cos A, b sin A) with 0 < A < π (CCW triangle). ✓
- Ray directions (BK: π−α, MK: γ, CL: A+π+α, NL: A−β, CK: A+π+α+γ, BL: π−α−β) are forced in this frame. ✓
- K = BK ∩ MK, L = CL ∩ NL solved correctly (verified numerically). ✓
- conK = (K−C) × dir(CK), conL = (L−B) × dir(BL): both linear in b (deg_b = 1, confirmed). ✓
- Consistency C = k₀l₁ − l₀k₁ = 0 with b = −k₀/k₁ (k₁ = sin(α+γ) ≠ 0 in interior). ✓
- A' = (L_y|K|² − K_y|L|²)/(K×L), etc. (perpendicular-through-K and -through-L, since A is origin). ✓
- G = (A'−B) × R_θ(C−B) with θ = 90° − A − α, cos θ = sin(A+α), sin θ = cos(A+α). ✓
- g = k₁²·G(−k₀/k₁) = G₂k₀² − G₁k₀k₁ + G₀k₁² (clearing denominator). ✓

### 2b. Certificate g = C·T is genuine (not vacuous)

- **Symbolic verification** (`certverify.py`, `dirdiv3.py`, my `independent_cert.py`):
  - `g*Td − C*Tn == 0` as a rational function: **True**.
  - Cleared-numerator polynomial identity: **True** (0 ops).
  - Pseudodivision of cleared ghn by cleared Chn as polynomials in t_γ over ℚ(s_α, c_α, s_A, c_A)(t_β): **remainder 0** (deg_tγ Chn = 4, deg_tγ ghn = 7). ✓

- **Not vacuous** (the trap from round 1 was `F = L1·conK + L2·conL`, which is vacuous when conK, conL are independent / det ≠ 0):
  - g at random free-indeterminate eval (sa=0.37, ca=0.91, sA=0.52, cA=−0.83, tb=0.6, tg=1.4): **g = −9.36e−02 ≠ 0**. So g is not identically zero.
  - C at same eval: **C = 5.44e−01 ≠ 0**. So the locus C = 0 is a proper subvariety, and g vanishing on it is a real constraint.
  - This is a genuine **polynomial divisibility** (g divisible by C), NOT a trivial ideal-membership in a maximal ideal. ✓

### 2c. The certificate proves a SIGNED directed angle (+θ, not ±θ)

Numerical verification: G(+θ) = (A'−B) × R_{+θ}(C−B) evaluates to **~0** on the locus, while G(−θ) = (A'−B) × R_{−θ}(C−B) evaluates to **~−0.18 to −0.38 ≠ 0**. So the certificate is specific to +θ = +(90° − A − α), not unsigned parallelism. This matters for §3, which needs the signed result.

### 2d. Minor concern: "g = C·T = 0" on the locus requires Td ≠ 0

The certificate is g·Td = C·Tn (rational identity). On the locus C = 0: g·Td = 0. To conclude g = 0, need Td = (t_γ²+1)·Φ ≠ 0. Since t_γ²+1 > 0 always, the question is whether Φ ≠ 0.

- **Numerically**: Φ ≠ 0 on all 8 tested valid configurations (values −0.12 to −0.24). ✓
- **Via pseudodivision route**: the cleaner certificate is ghn = Chn·Q (polynomial identity, remainder 0), where ghn, Chn are cleared numerators. On the locus Chn = 0 (since C = Chn/Chd and Chd ≠ 0 — Chd is a product of (1+t_β²) and (1+t_γ²) powers, always positive). So ghn = 0, hence g = ghn/ghd = 0 (ghd is also a product of (1+t_β²) and (1+t_γ²) powers, always positive). This route **does not require Φ ≠ 0**.

The proof mentions both formulations ("g = C·T" and "pseudodividing... yields remainder 0"). The pseudodivision route is rigorous; the "g = C·T = 0" phrasing is slightly sloppy (doesn't address Td ≠ 0) but is rescued by the pseudodivision. **This is a minor presentation gap, not a mathematical gap.**

**§2 is essentially complete and correct.** ✓

---

## 3. §3 The B↔C symmetry — CONCLUSION CORRECT, PROOF HAS A SIGN ERROR ✗

This is where I found the gap. The **conclusion** is correct (verified numerically), but the **proof's reasoning** contains two compensating sign errors.

### 3a. What the proof claims

The proof states:
> "The involution σ reverses the orientation of directed angles. Applying σ to (∗) gives
> ∡(CB, CA') = 90° − A − α, i.e. ∡(BC, CA') = −(90° − A − α). (∗σ)"

So the proof's chain is:
1. σ reverses orientation of directed angles. [Correct claim.]
2. Applying σ to (∗): ∡(CB, CA') = +(90° − A − α). [**WRONG** — see below.]
3. Converting CB → BC: ∡(BC, CA') = −(90° − A − α). [**WRONG conversion** — see below.]
4. Final: ∡(BC, CA') = −(90° − A − α). [Right answer, wrong reasoning.]

### 3b. What the actual values are (verified numerically on 6 configs)

| Config | target | ∡(CB, CA') actual | proof claims | ∡(BC, CA') actual | proof claims |
|--------|--------|--------------------|--------------|--------------------|--------------|
| A=70,α=15 | +5° | **−5°** | +5° | −5° | −5° |
| A=55,α=25 | +10° | **−10°** | +10° | −10° | −10° |
| A=45,α=18 | +27° | **−27°** | +27° | −27° | −27° |
| A=65,α=8 | +17° | **−17°** | +17° | −17° | −17° |

(Directed angles between lines, mod π, in (−π/2, π/2].)

**The proof's intermediate step (∡(CB, CA') = +target) is WRONG.** The actual value is **−target**.

### 3c. Why the proof's intermediate step is wrong

The B↔C relabeling σ produces a valid configuration (I verified all six angle hypotheses hold for the relabeled config with β↔γ). However, the relabeled triangle B'C'A (where B'=C, C'=B) has **opposite orientation**: the original triangle BCA is counterclockwise (CCW, since C is above the x-axis), but B'C'A is **clockwise** (CW, since C'=B is on the x-axis and B'=C is above it, so going B'→C'→A is clockwise).

§2's Direction Lemma is proved for a **CCW** triangle (the proof explicitly places C at (b cos A, b sin A) with 0 < A < π, i.e., sin A > 0, C above x). When §2 is applied to the CW relabeled config, the signed result picks up a **negative sign** (the orientation reversal negates directed angles):

- §2 on CCW relabeled (after reflecting CW→CCW): ∡(B'C', B'A') = 90° − A − α.
- Reflection to restore CCW negates directed angles: ∡(B'C', B'A') = **−(90° − A − α)** in the original frame.
- B'C' = line CB, B'A' = line CA'. So ∡(CB, CA') = **−(90° − A − α)**.

The proof writes ∡(CB, CA') = **+(90° − A − α)**, missing the sign flip from the orientation reversal. **This is error #1.**

### 3d. Why the proof's CB→BC conversion is wrong

The proof then converts "∡(CB, CA') = +target" to "∡(BC, CA') = −target" via a sign flip.

But in the proof's stated convention — "∡(ℓ₁, ℓ₂) denotes the directed angle from **line** ℓ₁ to line ℓ₂ **modulo π**" — the line CB and the line BC are the **same geometric line**. Directed angles between lines (mod π) are invariant under reversing a line: ∡(CB, CA') = ∡(BC, CA'). There is **no sign flip**.

This is true in all standard conventions (mod π between lines, or mod π between directed segments — reversing one segment adds π to the direction, which is 0 mod π). I verified numerically: ∡(CB, CA') = ∡(BC, CA') = −target on all configs.

**The proof's CB→BC sign flip is spurious. This is error #2.**

### 3e. The two errors cancel

- Error #1: proof writes ∡(CB, CA') = +target (should be −target). Missing sign flip from orientation reversal.
- Error #2: proof writes ∡(BC, CA') = −∡(CB, CA') (should be +∡(CB, CA')). Spurious sign flip from CB→BC.

Net: (+target) × (−1) = −target. The correct answer, reached by two wrong steps.

### 3f. The proof's intermediate step leads to a contradiction

If the proof's intermediate step (∡(CB, CA') = +target) were taken at face value — without the compensating spurious CB→BC flip — then ∡(BC, CA') = ∡(CB, CA') = +target (same line). Combined with §2's ∡(BC, BA') = +target, this gives ∡(BC, BA') = ∡(BC, CA') = +target, meaning BA' ∥ CA' (both make the same directed angle with BC). Since both lines pass through A', they must be the same line, forcing B, C, A' collinear. But numerically A' is NOT on line BC (cross product (A'−B) × (C−B) ≈ −0.22 ≠ 0). **Contradiction.**

This confirms the proof's intermediate step is not just imprecise but **mathematically wrong**.

### 3g. The correct derivation

The correct §3 argument is:

1. The B↔C relabeling σ produces a valid configuration with opposite (CW) orientation.
2. §2, proved for CCW triangles, when applied to the CW relabeled config (after reflecting to restore CCW), gives ∡(CB, CA') = **−(90° − A − α)** in the original frame (the reflection negates the signed angle).
3. Since line CB = line BC (mod π): ∡(BC, CA') = **−(90° − A − α)**. No second sign flip.
4. From §2 and step 3: BA' makes angle +target with BC, CA' makes angle −target. Their intersection A' lies on the perpendicular bisector of BC (a coordinate check: placing B=(0,0), C=(d,0), the two lines intersect at x = d/2). ✓

The proof's claim "σ reverses the orientation of directed angles" is **correct in spirit** (the relabeling does reverse the triangle's orientation), but the proof **does not correctly apply** this reversal — it puts the sign flip at the wrong step.

---

## Scores

- **Correctness:** 3/5 — §1 and §2 are correct. §3's conclusion is correct but the proof's reasoning has two compensating sign errors; the intermediate step ∡(CB, CA') = +target is mathematically wrong (contradicts numerics and leads to a contradiction if taken at face value).
- **Completeness / rigor:** 3/5 — §1 complete, §2 essentially complete (minor Td≠0 concern rescued by pseudodivision route). §3 has a genuine gap in the sign-handling argument; the correct derivation (orientation reversal negating the signed angle) is not presented.
- **Progress:** 5/5 — enormous progress from round 1. The certificate is now genuine and non-vacuous (closing the round-1 gap). The Direction Lemma is proved. Only the §3 sign argument needs correction.

---

## Verdict: CHANGES REQUESTED

Status: **partial** (not `solved` — the §3 symmetry argument has a sign-handling gap; not `unsolved` — the approach is correct, §1 and §2 are complete, and the fix is straightforward).

### Exact gap to close

The proof's §3 step "Applying σ to (∗) gives ∡(CB, CA') = 90° − A − α" is **wrong** (the actual value is −(90° − A − α), verified numerically on 6 configs). The proof then introduces a **spurious** sign flip in the conversion "∡(BC, CA') = −(90° − A − α)" from CB→BC (lines CB and BC are identical mod π; no sign flip). These two errors cancel.

### What the builder must do

Fix the §3 sign argument. Either:

**(A) Correct the orientation-reversal argument (preferred, minimal fix):**
Replace the current §3 with a correct derivation:
- The B↔C relabeling produces a valid config with **opposite (CW) orientation**.
- §2 is proved for CCW triangles; applying it to the CW relabeled config (after reflecting to restore CCW, which negates directed angles) gives ∡(CB, CA') = −(90° − A − α) directly.
- Since line CB = line BC (mod π), ∡(BC, CA') = −(90° − A − α). No second sign flip.
- Conclude A' ∈ perp-bis(BC) from the two signed angle identities.

**(B) Provide a separate direct certificate for the CA' direction:**
Set up G' = (A'−C) × R_{−θ}(B−C) (or equivalently R_θ(C−B), since B−C = −(C−B)) and prove G' = 0 via a polynomial certificate analogous to §2. This would be completely independent of the symmetry argument. (Note: since R_θ(B−C) = −R_θ(C−B), G' = 0 is equivalent to (A'−C) ∥ R_θ(C−B), i.e., ∡(BC, CA') = θ... but numerically ∡(BC, CA') = −θ, so the correct target is R_{−θ}, not R_{+θ}. This confirms the sign issue.)

**Option (A) is the minimal fix** and requires only reorganizing the sign flip (move it from the CB→BC step to the σ-application step). The key claim "σ reverses orientation" is correct; it just needs to be applied correctly.

The recorded Status `solved` is **incorrect**; it should be `partial` until the §3 sign argument is fixed.
