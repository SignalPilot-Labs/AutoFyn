# Proof-reviewer report — round 2 — imo-2026-02 (IMO 2026 P2, prove OM=ON)

Three approaches reviewed independently. One SOLVED (verified from scratch), two honest
partials. Headline: **trig-lawofsines is APPROVED — the problem is solved.**

---

## 1. trig-lawofsines — VERDICT: APPROVE — Status: solved

Builder claimed SOLVED. I adversarially re-derived the entire load-bearing chain from
scratch (sympy, `/tmp/verify_numeric.py`, `/tmp/verify_T_equiv.py`, `/tmp/verify_cert.py`)
and it holds. The recorded Status is CORRECT.

**What I independently verified:**
- **Geometry & parametrisation (§1–2).** Rebuilt A,K,L from B=(0,0),C=(1,0) via the ray
  angles; re-derived every triangle-angle claim (∠KBC=B−θ, ∠KCB=C−θ−γ, ∠BKC=A+2θ+γ, and
  the L-side mirror). All correct. The strict inequalities (⋆) follow from the containment
  hypotheses; all four hypotheses E1,E2,E3 are genuinely injected (E1 fixes θ on both
  sides, E3 via ∠BMK=γ into the cevian for BK and ∠LCK=γ into ∠KCB, E2 mirror).
- **Closing relations E3′,E2′ (§3).** Re-derived by equating the certified cevian length
  BK=(AB/2)sinγ/sin(θ+γ) with the △BKC value; reproduces E3′ exactly. E2′ is the correct
  mirror. Solving E3′/E2′ for γ,β in the physical intervals reconstructs the config with
  OM=ON to machine precision across 6 random scalene triangles.
- **Reduction to (T) (§4).** Verified the sharper fact that `OM²−ON² = (T-difference)/(4D)`
  as an exact identity for ARBITRARY A,K,L (ratio = 1/(4D) in every trial). Since D≠0,
  `OM=ON ⟺ (T)`. Step 4 is airtight (any sign convention in the stated circumcentre
  formula is immaterial — the final (T) is verified directly).
- **The certificate (§5–6) — THE load-bearing step.** I rebuilt P(t), Q(s), TN(t,s) from
  the angle definitions independently and ran the pseudo-division myself:
  `lc(P)·TN = q1·P + R1` (deg_t R1 = 3), `lc(Q)·R1 = q2·Q + R2` (deg_s R2 = 3), and the
  Groebner reduction of R2 modulo ⟨ρ1,ρ2,ρ3⟩ returned **exactly 0**. So
  `lc(P)·lc(Q)·TN = f·P + g·Q` is a genuine polynomial identity. This is an exact symbolic
  reduction to 0, not a numeric check — same rigor standard as the certified
  reduction-power-to-core lemma.
- **Leading coefficients.** `lc(P,t) = −2 sinA sinθ sin(C−θ)` and
  `lc(Q,s) = −2 sinA sinθ sin(B−θ)` both reproduced exactly (mod ρ), and both nonzero on
  (⋆) (all three sines positive: A,θ∈(0,π); C−θ,B−θ∈(0,π) since θ<min(B,C)).
- **Denominator.** Tden factors as `sinA³·[sin(A+2θ+γ)(1+t²)]²·[sin(A+2θ+β)(1+s²)]²`,
  strictly positive on (⋆), so TN=0 ⟹ (T) with no lost factor.

**On the round-1 "spurious branch" fear.** It fully dissolves: the finish is now an
EXPLICIT polynomial certificate (6.4), a literal identity in the trig indeterminates and
t,s. It holds at every point, so at the physical config where P=0,Q=0 it forces TN=0. No
branch selection is invoked in the actual proof; §5's involution discussion is only
motivational. The round-1 Gröbner false-negative came from the lossy (cos2γ,sin2γ) doubling;
the single-angle t=tan(γ/2) removes it, exactly as claimed.

No hidden gap, no circularity, no skipped case (single 1-parameter family; degenerate
A,K,L collinear excluded by D≠0). The computational certificate is reproducible and I
reproduced it. **Complete and correct.**

Score — Correctness 10/10, Completeness/rigor 10/10, Progress: closes the whole problem
(gap that stood across all three approaches).

current.md set to Status=solved with the Full proof written.

## 2. power-of-point-BC — VERDICT: CHANGES REQUESTED — Status: partial

Recorded Status `partial` is CORRECT; no overclaim (builder explicitly flags G3 open and
the Lemma O / G2 sub-steps as not fully closed). Real progress this round: **E2′,E3′
proven gap-free** (§E), matching my independent derivation — now certified to
`lemmas/closing-relations.md`. The directed-angle mod-π equality (§B1) is also sound.
Remaining gaps (precise): **(G3)** the final scalar identity
`c·BA′ − b·CA″ = (c²−b²)/2` after substituting the SAS chain + E2′,E3′ is NOT closed
synthetically (same scalar wall); **Lemma O** (A′∈(A,B), A″∈(A,C) strict; cyclic order
A,A′,K,L,A″) argued only in part / numerically; **§G** the "Q on the A-side of MN"
betweenness sub-step not fully closed. Score — Correctness 9/10 (what is written is valid),
Completeness 5/10, Progress: advanced (E2′,E3′ closed). NOTE: now that trig-lawofsines is
solved, this slug is no longer needed for the run; kept live for population value only.

## 3. inversion-at-A — VERDICT: CHANGES REQUESTED — Status: partial

Recorded Status `partial` is CORRECT and notably honest: the builder proves the circle→line
reformulation exactly (ℓ*=ι(ω) is the polar of A; intercepts p,q; Prop R) and then
truthfully shows it is TAUTOLOGICAL — pinning ℓ* ≡ pinning O, so the inversion step does
not inject E1–E3. Lemmas I1,I2, Prop R are genuinely provable and reusable. Gap
**(G-scalar)**: the E2/E3 coupling identity in (θ,β,γ,α,b,c) is open — the same wall.
No overclaim (no Full proof written, explicitly). Score — Correctness 9/10, Completeness
4/10, Progress: partial (clean reformulation + honest localisation of the unused hypotheses).

---

## Lemmas certified this round
- `lemmas/closing-relations.md` — E2′,E3′ (from power-of-point-BC §E / trig §3). Gap-free
  given the certified cevian lengths; re-derived and reproduced. CERTIFIED.
- `lemmas/T-reduction-and-certificate.md` — the (T)-reduction (OM²−ON²=(T-diff)/(4D)) and
  the Weierstrass ideal-membership certificate (from trig-lawofsines §4–6). Independently
  reproduced exactly. CERTIFIED.

## Bottom line
Problem imo-2026-02 is **SOLVED**. trig-lawofsines → APPROVE (headline). power-of-point-BC
and inversion-at-A → CHANGES REQUESTED (both honest partials, no overclaim).
