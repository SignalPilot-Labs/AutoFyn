# Outline review — imo-2026-02 (round 2)

Field: power-of-point-BC (advance), trig-lawofsines (advance), inversion-at-A (new,
diversity anchor), complex-swap-symmetry (dormant, not built). Shared certified
reduction `OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2` imported by all — not re-derived. Good.

Two load-bearing claims checked numerically/symbolically this round:
- **A' lies strictly between A and B** (f=AA'/AB ∈ 0.77–0.91 on the sampled family, /tmp/probe2.py).
  This DECIDES the sign structure of power-of-point-BC's Step B (below).
- **E3′ under Weierstrass t=tan(γ/2) is degree 4 in t, not ≤2** (sympy, confirmed).
  Corrects the outliner's degree claim for trig-lawofsines (below). Not fatal.

---

## power-of-point-BC — CHANGES REQUESTED (advance; build)

The Law-of-Sines closure chain A–D is the right technique and is not circular against the
reduction: the reduction (core identity) is the target, and Steps A–D build BA', CA'' as an
independent trig expression to substitute in. No step assumes OM=ON. Approve to build, with
these mandatory corrections/warnings:

- **Step A is sound.** A' on line AB ⟹ ray BA' = ray BA (A' between A and B, verified), so
  ∠A'BK = ∠ABK = θ by E1 directly. Clean.
- **Step B / G1 — the explorer's "same arc" justification is WRONG; the RESULT is right.**
  Because A' is strictly between A and B, rays A'A and A'B are OPPOSITE, so ∠BA'K = π − ∠AA'K
  (NOT equal). The inscribed-angle theorem gives ∠AA'K = π − ∠ALK (A' and L are on OPPOSITE
  arcs of chord AK, not the same arc as the explorer wrote). The two supplement flips cancel:
  ∠BA'K = ∠ALK = φ_L. The builder must present it as this two-step directed-angle (mod π)
  argument with the arc/side resolution derived from the containment hypotheses — NOT as the
  explorer's single "same arc" line, which is geometrically false as stated. G1 as the
  outliner phrased it ("directed-angle mod π + sign-resolution, not the numeric observation")
  is correct; hold the builder to it. Same for the mirror ∠CA''L=∠AKL.
- **G2 (ordering at A) is the most tractable gap** — pure betweenness from "K inside ∠LBA ∩
  △BMC", "L inside ∠ACK ∩ △BNC". No metric content. Fine.
- **G3 is content-equivalent to trig's identity (T) — DIVERSITY CAVEAT.** Once A–D express
  BA', CA'' in θ (with β,γ as functions of θ via the E2′,E3′ closing relations), the final
  identity pow(B)−pow(C)=(AB²−AC²)/2 is the SAME scalar identity trig-lawofsines must close.
  The outliner acknowledges this. The bet — that routing through clean sub-triangles telescopes
  by hand where raw CAS elimination did not — is a legitimate different route, but it is NOT a
  different wall. Builder should attempt product-to-sum / hand-telescoping BEFORE any CAS, and
  must NOT fall back to plain Gröbner ideal-membership on the doubled system (recorded false
  negative). Note: G3 also inherits dependence on E2′,E3′, which are only numerically confirmed,
  not yet rigorously derived — flag if the builder relies on them as proven.
- Do not re-assume the recorded dead ends (φ_L=γ, φ_K=β FALSE; A' on BK/BL/CK/CL; BKLC
  concyclic; BK tangent) — all still barred.

## trig-lawofsines — CHANGES REQUESTED (advance; build)

Technique sound; the Weierstrass branch-kill is genuinely correct and IS the right fix.

- **Branch separation is valid.** tan((γ+π)/2) = −cot(γ/2) ≠ tan(γ/2), so t=tan(γ/2)
  distinguishes γ from γ+π — this genuinely dissolves the doubled-angle ghost (the ghost lives
  at a large-magnitude t of opposite sign, excluded by the physical interval 0<γ<C−θ ⟹ t small
  positive). The spurious branch does NOT survive. Good.
- **Correction: the degree bound "≤2 in t" is WRONG — E3′ maps to degree 4** (sympy-verified).
  The products of two single-γ sines (e.g. sinγ·sin(A+2θ+γ)) generate 2γ terms on expansion, so
  the Weierstrass image is quartic, not quadratic. Degree 4 is still bounded and tractable, and
  the interval branch-selection still isolates the unique physical root, so this is a correction,
  not a fatal flaw — but the builder must NOT rely on the "≤2, easy resultant" framing; plan for
  a degree-4 resultant / direct substitution.
- Keep θ a free continuum; never re-double to (cos2γ,sin2γ).

## inversion-at-A — APPROVE (new; register + build)

Registered at cold-start Elo. Valid whole-problem attempt, genuinely different framing
(circle→line), not circular, not a recorded dead end. Skeleton checks out:

- Step 3 incidence A'=ι(P*), P*=AB∩ℓ*, is correct: ι fixes line AB (through centre A),
  ι(ω)=ℓ*, so ι(ω∩AB)=ℓ*∩AB; AA'·AP*=r². Standard, low-risk. Core-in-feet algebra (step 5)
  is determinate once ℓ* is pinned.
- **G-main (step 4, pin ℓ* from E1–E3 via reversed similarity) is the real work and is
  honestly labeled as such, with the risk it may still bottom out in a scalar identity.**
  Adversarial read: inversion preserves angles, so the angle conditions translate to angle
  conditions among inverted points — the orientation/branch bookkeeping does NOT automatically
  vanish (the "opposite handedness K-side vs L-side" warning is the same orientation-sign trap
  that bit complex-swap in R1). So it is NOT guaranteed to escape a scalar wall. BUT the object
  is genuinely lower-dimensional (one line ℓ*, 2 DOF, needing only AP*,AQ*) rather than the full
  β,γ,θ identity, and it is a structurally distinct reduction. As the field's diversity hedge it
  is exactly what CLAUDE.md's shared-gap guidance calls for. Approved to build; the gap is a
  valid open gap for a population member, not a defect.

## complex-swap-symmetry — not built (dormant, agreed)

Correctly parked: shares trig's CAS-elimination wall (Tnum=0 saturation), and the Weierstrass
fix targets that whole computational family more cleanly. Rules bar a 4th CAS bash. Stays live
in the population (ranked), revisit with the t-substitution only if Weierstrass resolves the class.

---

## Field-level diversity note (for the orchestrator)

power-of-point-BC (G3) and trig-lawofsines (T) converge on the SAME final scalar identity —
they reach it by different routes (structured sub-triangles vs Weierstrass), which is worth
running both, but if BOTH stall at that identity next round it is one shared wall, not two.
inversion-at-A is the genuine diversity anchor (different object). complex-swap is a fourth
that shares the CAS wall. So effective diversity is: {two routes to one identity} + {one
genuinely different reduction}. If power's hand-telescoping and trig's degree-4 resultant both
fail to close the identity, the identity itself — not the routing — is the wall, and next round
should lean on inversion-at-A (or challenge the E2′/E3′-injection framing directly) rather than
open a fifth route to the same identity.

## Ranking (Elo after this round)

power-of-point-BC 1559.6 > trig-lawofsines 1527.5 > inversion-at-A 1486.0 >
complex-swap-symmetry 1427.0. Power leads (cleanest synthetic route + independent G1/G2 content
+ concrete plan); trig strong second (branch-kill sound, finish now degree-4 but tractable);
inversion third (fresh, sound skeleton, hard-but-honest main gap); complex last (dormant,
duplicative CAS wall, only numeric).

build set: power-of-point-BC, trig-lawofsines, inversion-at-A
