# Proof review: imo-2026-02 (OM = ON) — round 1

**Candidate status (as written):** partial
**My judgement: partial** (matches the candidate's own marking — the candidate is honest about the gap)
**Verdict: CHANGES REQUESTED**

---

## Summary

The proof has two genuinely rigorous parts and one un-closed gap:

1. **§1 The antipode/homothety reduction** — fully rigorous, complete. Verified independently (see below).
2. **§2–§3 The analytic reduction to a single trigonometric divisibility (∗)** `H ≡ 0 (mod C)` — the *reduction* logic is rigorous and verified, but the divisibility itself is **only checked numerically (~1e-12), not proven**. This is the gap.
3. **§4 The gap** — admitted. The symbolic polynomial division did not terminate within budget.

So: real, substantial progress (a clean reformulation of the theorem plus a complete reduction to one algebraic identity), but the load-bearing identity is unproven. Numerical evidence, however strong, is not a proof for an olympiad `proof_only` problem. **Not solved.**

---

## 1. The reduction OM=ON ⟺ |A'B|=|A'C| (§1) — SOUND

I re-derived this independently:

- `O` circumcenter of `AKL` ⇒ `A' := 2O−A` is the antipode of `A` on `(AKL)` ⇒ `AA'` is a diameter ⇒ `∠AKA' = ∠ALA' = 90°` (Thales) ⇒ `A'K ⊥ AK`, `A'L ⊥ AL`. (R1) ✓
- Homothety `h` center `A` ratio `1/2`: `h(B)=M`, `h(C)=N`. Since `MN ∥ BC` and `h` maps the midpoint of `BC` to the midpoint of `MN` while preserving directions (hence perpendicularity to `BC` ⇒ perpendicularity to `MN`), `h` sends `perp-bis(BC)` bijectively onto `perp-bis(MN)`. ✓
- `O ∈ perp-bis(MN) ⟺ OM=ON` (definition). `h` is invertible (ratio `1/2 ≠ 0`), `h⁻¹(O)=2O−A=A'`. So `OM=ON ⟺ A' ∈ perp-bis(BC) ⟺ |A'B|=|A'C|`. (R2) ✓

**Hidden-assumption check:**
- *`A'` well-defined / `K×L ≠ 0`*: the problem statement itself ("Let `O` be the circumcentre of triangle `AKL`") presupposes `A,K,L` non-collinear, so `K×L ≠ 0` is given. Acceptable — no separate proof needed, but the candidate should state this once for completeness.
- *Orientation / frame*: the candidate correctly restricts to the standard oriented frame (`A=(0,0)`, `B` on `+x`, `C` upper half-plane, `0<A<π`) and states the interior-angle range `0<α`, `0<α+γ<C`, `0<α+β<B` keeps sines positive. This is a legitimate WLOG (any non-degenerate triangle can be placed thus). The sign choices for the six ray directions (`BK=π−α`, etc.) are forced in this frame. No generality is lost.

**§1 is rigorous and complete.**

## 2. Parametrisation, conK/conL, and the formula for A' (§2) — SOUND

I numerically verified the whole pipeline independently (`/tmp/verify.py`, 40 random configurations solving the full nonlinear system `conK=conL=0`):

- `OM=ON` holds to ~1e-10 across all configs.
- `A' = 2O` satisfies `A'K ⊥ AK`, `A'L ⊥ AL` (dot products ~1e-15).
- `|A'B| = |A'C|` holds to ~1e-10.
- The linear-system formula `A' = (|L|²·JK − |K|²·JL)/(K×L)` equals `2O` to ~1e-15.

I also checked the structural claims by direct expansion (`/tmp/symcheck.py`, `/tmp/structural.py`):

- **`A'` is linear in `(b,c)`** with angle-only coefficients: `A' = b·a_b − c·a_c`. ✓ (matches candidate eq. for `a_b, a_c`).
- **`F := |A'B|² − |A'C|²` is homogeneous degree 2 in `(b,c)`**: I confirmed `F(2c,2b) = 4·F(c,b)` exactly. ✓ So `F = b²F₁ + bc·F₂ + c²F₃` with angle-only `Fᵢ`. ✓
- **`conK`, `conL` are linear in `(b,c)`** (since `K=c·k̂`, `C=b·ĉ_A`, both degree-1; cross with an angle-only direction preserves `(b,c)`-linearity). ✓ Hence the consistency determinant `C(β,γ) = P(γ)S(β) − Q(γ)R(β) = 0` is the single locus equation, and `b/c = ρ = −Q/P = −S/R` on the locus. ✓
- **Elimination of `b/c`**: substituting `b = ρc` (with `ρ = −Q/P`, `P≠0` on the interior) into `F=0` yields `H := Q²F₁ − PQ·F₂ + P²F₃ = 0`, valid since `P≠0`. The implication `F=0 on locus ⟺ H=0 on locus C=0` is clean (no logical gap), modulo `P≠0` (i.e. `sin(α+γ)≠0`, true in the interior).

So the reduction **of the theorem to the single identity `H ≡ 0 (mod C)` is rigorous**. The parametrisation reproduces the correct configuration; there is no flaw in the reduction that would invalidate even the numerical claim.

**One correction to the outline-review (not a flaw in this candidate):** the outline-review claimed `conK` is *linear* in `(sin γ, cos γ)`, enabling a trivial linear elimination. I checked this directly: `P(γ) = 2 sin²(α+γ)` and `Q(γ)` are both **degree 2** in `(sin γ, cos γ)` (e.g. `coeff of sin²γ in P is 2cos²α`). The candidate is right to push back on the "linear" suggestion — but the candidate's counter-framing ("degree 4 after half-angle") is a *red herring*: the half-angle substitution inflates the degree; in the raw `sin/cos` ring it is degree 2. The candidate applied half-angle substitution *before* attempting elimination, which is the wrong order (see route below).

## 3. The gap: `H ≡ 0 (mod C)` is unverified symbolically (§4) — GENUINE GAP

This is the load-bearing step and it is **not proven**. The candidate is explicit:

- Numerical evidence (~1e-12 on 40 configs; smooth bounded ratio `H/C` off the locus) is strong and consistent with `H = C·T`, but **numerical verification is not a rigorous proof**. For a `proof_only` olympiad problem this is disqualifying on its own.
- The symbolic Groebner/polynomial-division over four tan-half-angle variables did not terminate.

So the candidate correctly self-downgrades to `partial`. **The Status in the file is honest and correct.**

Note also that, because the divisibility is unproven, even the *claim* that `H` is divisible by `C` (vs. `H` merely vanishing on the real locus `C=0 ∩ interior` for some other reason, e.g. an additional implicit relation) is not fully established. The numerical evidence makes `H = C·T` overwhelmingly likely, but likelihood is not proof.

## 4. The synthetic angle-chase fallback — not viable as attempted

The round-2 builder tried to prove `∠A'BC = ∠BCA'` by a linear angle-sum chase and found `θ = ∠A'BC` is **not** a linear combination of `(A,B,C,α,β,γ)` (large least-squares residual). This is consistent with the identity being genuinely *nonlinear* in the angle parameters (as the analytic route also reveals — `H` and `C` are trig polynomials, not linear).

**Specific missing lemma for a synthetic route:** one would need a *trigonometric* (not angle-sum) identity of the form
```
tan(∠A'BC) = tan(∠BCA')
```
expressed via `tan α, tan β, tan γ` and the consistency relation `C(β,γ)=0`, then verified modulo that relation. This is essentially the same divisibility `H ≡ 0 (mod C)` re-dressed in tangent language — no easier than the analytic route. **I do not recommend the synthetic angle chase as the primary closing route**; it collides with the same nonlinear identity.

## Recommended concrete route to close the gap

The divisibility `H ≡ 0 (mod C)` is a **univariate polynomial divisibility** once one variable is isolated. The cleanest terminating route:

**Pseudodivision in `t_γ := tan(γ/2)`.** Treat the half-angle-polynomialised `H` and `C` as polynomials in the single variable `t_γ`, with coefficients in the rational-function field `ℚ(t_α, t_β, t_A)` (where `t_α=tan(α/2)`, etc.). Perform **pseudodivision** of `H` by `C` with respect to `t_γ`. This is a finite, cheap computation:

- `deg_{t_γ} C` is small (≤ 4 after half-angle; the structure `C = P(γ)S(β) − Q(γ)R(β)` makes it bidegree `(4 in t_γ, 4 in t_β)`).
- `deg_{t_γ} H` is bounded (≈ 8–12).
- Pseudodivision produces a remainder `R` with `deg_{t_γ} R < deg_{t_γ} C`, and an identity `D·H = Q·C + R` (`D` = leading-coefficient power of `C`).
- **Verify `R ≡ 0` as a polynomial in `t_γ` over `ℚ(t_α, t_β, t_A)`** — i.e. every coefficient (a rational function of `t_α, t_β, t_A`) vanishes identically.

If `R ≡ 0`, then `C | H` over `ℚ(t_α, t_β, t_A)[t_γ]`, hence over the tan-half-angle ring, hence (a fortiori) `H ≡ 0 (mod C)` as a trigonometric identity. This is a **certificate**: it terminates in seconds with `sympy`'s `poly_div`/`prem`, and the zero-remainder check is a finite coefficient-by-coefficient simplification. The candidate's earlier Groebner attempt failed because it ran an *unconstrained multivariate* Groebner basis over all four variables simultaneously; pseudodivision in one variable avoids that blow-up entirely.

**Fallback if pseudodivision's remainder does not vanish identically** (i.e. the divisibility only holds *after* imposing `s²+c²=1` unit-circle relations, not in the free tan-half-angle ring): then augment the certificate with the two Pythagorean identities — i.e. exhibit
```
D·H = Q·C + R + U·(t_α²-adjusted) + V·(t_β²-adjusted) + W·(t_γ²-adjusted)
```
or reduce `R` modulo the unit-circle relations `s²+c²−1`. Still a terminating computation, just one more layer.

**Either way, the path is: half-angle → view as univariate in `t_γ` → pseudodivide → check zero remainder.** The builder should run this and include the (verified) remainder-zero as the certificate, or print the explicit quotient `T = H/C` and verify `H = C·T` by product-to-sum expansion.

## Scores

- **Correctness:** 4/5 — everything written is correct; the one unproven step is honestly flagged, not falsely asserted.
- **Completeness / rigor:** 2/5 — the load-bearing divisibility is unproven (numerical only). Reduction is rigorous; the certificate is missing.
- **Progress:** 4/5 — substantial: a clean equivalent reformulation plus a complete reduction to one algebraic identity. Far closer than the starting point.

## Verdict: CHANGES REQUESTED

Status: **partial** (not `solved`; not `unsolved` — the approach is sound and the reduction is rigorous, a real, attackable gap remains). The builder should close the gap by the **univariate pseudodivision of `H` by `C` in `t_γ = tan(γ/2)`** described above, exhibiting either a zero remainder (certificate) or an explicit quotient `T` with `H = C·T` verified by expansion. The synthetic angle chase is not recommended as the primary route — it reduces to the same nonlinear identity.

The recorded Status `partial` is correct; do not upgrade to `solved`.
