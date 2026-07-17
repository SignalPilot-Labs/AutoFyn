## imo-2026-02

Field this round: advance the two lead approaches with the concrete new closures
the explorers found, and open ONE genuinely-different framing (inversion-at-A) as
the diversity anchor per CLAUDE.md's shared-gap guidance. Leave complex-swap-symmetry
DORMANT (not in build set): it shares the trig approach's CAS-elimination wall, and
the Rules forbid a 4th CAS bash; the trig Weierstrass fix below is the better bet to
close that whole computational family, so building complex this round would duplicate
the wall rather than diversify. All three share the certified reduction
`OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2` (import `lemmas/reduction-power-to-core.md`,
`lemmas/cevian-lengths.md`) — do not re-derive it.

---

power-of-point-BC: advance
Target: OM=ON for the whole 1-parameter family (O=circumcentre AKL).
Technique: power of a point + Law-of-Sines SAS-chain closure of the second
  intersections A'=AB∩ω, A''=AC∩ω (synthetic; no CAS fallback — the diversity anchor).
Skeleton:
  1. Import OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2, pow(B)=BA·BA', pow(C)=CA·CA'' — CERTIFIED.
  2. Step A: ∠A'BK=∠ABK=θ exactly — because A' lies on line AB, so ray BA'=ray BA;
     E1 alone gives the angle, no concyclicity needed.
  3. Step B: inscribed angle on chord AK of ω gives ∠BA'K=∠AA'K=∠ALK=:φ_L (same arc).
  4. Step C: Law of Sines in △A'BK (side BK from L4, angles θ at B, φ_L at A') closes
     BA'=BK·sin(θ+φ_L)/sin(φ_L). Mirror: CA''=CL·sin(θ+φ_K)/sin(φ_K), φ_K=∠AKL.
  5. Step D: SAS chain pins φ_K,φ_L with NO new unknowns:
       △ABK: SAS (AB, ∠ABK=θ [E1], BK [L4]) → ∠BAK, AK.
       △ACL: SAS (AC, ∠ACL=θ [E1], CL [L4]) → ∠CAL, AL.
       ∠BAC=∠BAK+∠KAL+∠LAC (order B,K,L,C at A) → ∠KAL.
       △AKL: SAS (AK, AL, ∠KAL) → φ_K=∠AKL, φ_L=∠ALK.
  6. Substitute Steps A–D into pow(B)−pow(C)=BA·BA'−CA·CA''; show it equals
     (AB²−AC²)/2 as one trig identity in θ (β,γ via certified E2′,E3′). Conclude OM=ON.
Key lemmas (claim + mechanism):
  - Step A angle: ∠A'BK=θ — because A' on line AB forces ray BA'=ray BA, so E1 applies directly.
  - Step B angle: ∠BA'K=∠ALK — inscribed-angle theorem, chord AK subtends equal
    directed angles from A',L on ω (this "automatic from concyclicity" fact is exactly
    the missing non-included angle that closes △A'BK — not a dead end here).
  - Step D closure: AK,AL,∠KAL determined by two SAS triangles + the angle
    decomposition at A, so △AKL is fully solved without touching K,L coordinates.
  - Numeric airtightness: whole chain reproduces pow(B)−pow(C)=(AB²−AC²)/2 to 6
    decimals on all 6 family members (explorer /tmp/probe2.py) — decomposition is exact.
Open gaps (the builder fills these — 3, well scoped):
  - G1 (directed-angle rigor, Step B): show ∠BA'K=∠ALK (NOT the supplement) is FORCED
    by the containment hypotheses (K inside ∠LBA, L inside ∠ACK) — a genuine directed-
    angle (mod π) + sign-resolution argument, not the numeric observation. Same for mirror.
  - G2 (ordering, Step D): prove ∠BAC=∠BAK+∠KAL+∠LAC synthetically — a betweenness fact
    (rays AK,AL inside ∠BAC in order B,K,L,C) forced by "K inside △BMC ∩ ∠LBA",
    "L inside △BNC ∩ ∠ACK". Most tractable gap (pure configuration, no metric content).
  - G3 (final trig identity): once A–D give BA',CA'' as explicit functions of θ and the
    fixed angles, pow(B)−pow(C)=(AB²−AC²)/2 is one identity in θ. Try sympy trig.simplify
    / product-to-sum telescoping BY HAND before any CAS; this is content-equivalent to
    trig's (T) but routed through clean sub-triangles so cross terms may cancel earlier.
Cases to cover: none (continuous family).
Watch out for: G1's supplement ambiguity is the real content — do not assert the
  correct branch, derive it from containment. Do NOT re-assume φ_L=γ or φ_K=β (FALSE,
  checked), BK tangent, BKLC concyclic, or A' on BK/BL/CK/CL (all dead ends).

---

trig-lawofsines: advance
Target: OM=ON for the whole family.
Technique: Law of Sines parametrization → single scalar identity (T), closed by a
  Weierstrass t=tan(γ/2) single-valued substitution (removes the γ↦γ+π ghost).
Skeleton:
  1. Import (T): OM=ON ⟺ 2(|u|²v₂−|v|²u₂)=D(1−2A_x), and closing relations E2′,E3′,
     and cevian formulas — all CERTIFIED/numerically confirmed.
  2. Weierstrass substitution: set t=tan(γ/2), s=tan(β/2). Substitute into the
     ORIGINAL (un-doubled) E3′ [sinγ·sinC·sin(A+2θ+γ)=2sinA·sin(θ+γ)·sin(C−θ−γ)] and
     E2′. Each sin/cos of γ becomes a rational function of t; E3′ becomes ONE polynomial
     equation p(t;θ,A,B,C)=0 of bounded degree (only sinγ,cosγ occur — no sin2γ — so ≤2).
  3. Physical-branch selection: 0<γ<C−θ ⟹ t=tan(γ/2) lies in an explicit interval,
     picking out the UNIQUE physical root t(θ). Mirror s(θ) from E2′.
  4. Substitute t(θ),s(θ) into (T); simplify to 0 — a determinate single-branch RATIONAL
     computation (resultant / direct substitution), NOT ideal membership. Conclude OM=ON.
Key lemmas (claim + mechanism):
  - Branch kill: tan((γ+π)/2)=−cot(γ/2)≠tan(γ/2), so t=tan(γ/2) SEPARATES γ from γ+π —
    this is exactly why the doubled-angle (cos2γ,sin2γ) Gröbner route created the spurious
    branch and Weierstrass does not (the Rule's γ↦γ+π trap is dissolved, not routed around).
  - Bounded degree: E3′ contains only single-angle γ, so its Weierstrass image is degree ≤2
    in t — a resultant against (T) is tractable, no high-degree elimination.
Open gaps:
  - G1: derive p(t;·)=0 explicitly and prove the physical root lies in the stated t-interval
    (single-valued branch selection — now determinate, no CAS branch ambiguity).
  - G2: the final substitution-and-simplify of (T) to 0 on t(θ),s(θ) (rational, mechanical).
Cases to cover: none.
Watch out for: do NOT re-double to (cos2γ,sin2γ) at any point (that reintroduces the ghost —
  Rule in run_state). Keep θ a free continuum. Substitute the physical branch, never plain
  Gröbner ideal-membership on the doubled system (recorded FALSE-NEGATIVE wall).

---

inversion-at-A: new
Target: OM=ON for the whole family (genuinely different framing — diversity anchor).
Technique: inversion centred at A turns ω into a line ℓ*=K*L*; the two secant
  intersections A',A'' become inverse images of ℓ*∩AB, ℓ*∩AC (one line, not two secants).
Skeleton:
  1. Import OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2, pow(B)=BA·BA', pow(C)=CA·CA'' — CERTIFIED.
  2. ι = inversion at A, radius 1. Since A∈ω, ι(ω)=line ℓ*=K*L* (K*=ι(K),L*=ι(L)).
  3. A'=ι(AB∩ℓ*), A''=ι(AC∩ℓ*) — because ι fixes lines through A and is an involution;
     so AA'=1/AP*, AA''=1/AQ*, with P*=AB∩ℓ*, Q*=AC∩ℓ*.
  4. Translate E1–E3 into relations pinning ℓ* via reversed-similarity
     △AXY∼△AY*X* (ratio 1/(AX·AY)) — MAIN gap.
  5. Compute AP*,AQ* from pinned ℓ*; core identity becomes an explicit relation in the two
     foot-distances and AB,AC. Conclude OM=ON.
Key lemmas (claim + mechanism):
  - A'=ι(P*) — ι involution fixing line AB (through centre A) maps ω∩AB to ℓ*∩AB.
  - Reversed similarity — ∠(AX,XY)=∠(AY*,Y*X*), X*Y*=XY/(AX·AY): the lever that injects
    E1–E3 into constraints on the SINGLE line ℓ*, trading two circle-secants for one line.
  - Core-in-feet — pow(B)=BA·(BA−1/AP*), so the identity is a relation in AP*,AQ*,AB,AC.
Open gaps:
  - G-main (step 4): pin direction+position of ℓ* from E1–E3 via reversed similarity.
    Honest risk: may still bottom out in a scalar identity, but in a structurally different
    object (line-through-two-fixed-lines), unlikely to hit the literal γ↦γ+π wall.
  - G-final (step 5): foot-distance algebra (determinate once ℓ* pinned).
  - G-incidence (step 3): low-risk standard inversion fact.
Cases to cover: none.
Watch out for: opposite handedness of the K-side vs L-side conditions; reversed similarity
  flips orientation, so track signs (same orientation-sign trap that bit complex-swap in R1).
  Do NOT re-assume the round-1/2 dead ends (spiral similarity at A sending B↦C,K↦L is FALSE;
  A' not on BK/BL/CK/CL; BKLC and midpoint quadruples not concyclic).

---

complex-swap-symmetry: DORMANT this round (not nominated for build).
Rationale: shares the trig approach's CAS-elimination wall (Tnum=0 needs saturation to the
  geometric component); Rules forbid a 4th CAS bash. The trig Weierstrass fix targets the same
  computational family more cleanly. Keep it live in the population (still ranked by the
  reviewer) but do not spend a builder on it until the Weierstrass route resolves whether the
  single-valued substitution closes this class — if it does, complex closes for free by the
  same mechanism; if it stalls, revisit complex with the same t-substitution next round.
