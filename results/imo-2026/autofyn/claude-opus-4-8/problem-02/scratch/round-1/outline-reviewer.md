# Outline review — imo-2026-02 (IMO 2026 P2, geometry), round 1

Problem: with M,N midpoints of AB,AC and K,L constrained by three angle
conditions (E1 ∠KBA=∠ACL, E2 ∠LBK=∠LNC, E3 ∠LCK=∠BMK), prove OM=ON where
O=circumcentre(AKL). Proof-only, continuous 1-parameter family (4 unknowns, 3
constraints — confirmed by all three explorers; any proof must hold for the
whole family, never pin K,L).

## Shared free reduction — checked, sound
All three approaches open with the same two-line reduction, and it is genuinely
free (not a disguised assumption of the conclusion):
- `OM=ON ⟺ pow(M,ω)=pow(N,ω)` with `ω=⊙(AKL)`, since `OX²−R²=pow(X,ω)`, same
  `R=OA` — correct.
- Along line AB (A at 0, B at AB), power is the quadratic `x(x−a')`; I verified
  symbolically (sympy) that `pow(M) = pow(B)/2 − AB²/4` exactly, and by mirror
  `pow(N)=pow(C)/2−AC²/4`. Hence `OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2`, and
  equivalently the fixed-line target `(O−½(M+N))·(C−B)=0`. This is a real
  simplification (kills the moving circumcentre), not circular. Approved as the
  common foundation.

The reduction being shared is NOT the single-gap trap: each approach then attacks
a genuinely different object to close the remaining content (see per-approach
below). Flagged for the orchestrator: monitor that trig and complex do not
collapse into "the same CAS elimination" in practice (see diversity note).

## power-of-point-BC — APPROVE
- Technique (power of a point / directed-angle chase) is appropriate and matches
  the knowledge-base synthetic toolkit. Reduction L1/L2 verified exact above.
- Load-bearing gap (L3): `pow(B,ω)−pow(C,ω)=(AB²−AC²)/2`. Mechanism is stated and
  sound in principle: K,L ∈ ω, so line BK meets ω again at K₂ giving
  `pow(B)=BK·BK₂` (signed), line CL meets ω again at L₂ giving `pow(C)=CL·CL₂`;
  the three angle conditions locate the second intersections by inscribed angles.
  This is a legitimate handle, not a bare label.
- Issue to close while building: the explorers verified numerically that A' (and
  by extension the second intersections) do NOT lie on any simple incidence
  (lines BK/BL/CK/CL), so the characterization of K₂,L₂ needs actual
  metric/inscribed-angle content — this route has NO CAS fallback, so the
  builder must produce the directed-angle argument in full. Watch signs (A' lands
  between M and B, not A and M). Do NOT re-assume BK tangent, BKLC concyclic, or
  any spiral-similarity side-ratio equality — all four are recorded numeric dead
  ends (explorer reports); the outline correctly avoids them.

## trig-lawofsines — APPROVE
- Technique (Law of Sines in sub-triangles + metric elimination toward
  `(O−½(M+N))·(C−B)=0`) is appropriate. Cevian formulas
  `BK=(AB/2)sinγ/sin(θ+γ)`, `CL=(AC/2)sinβ/sin(θ+β)` are correct (∠MBK=∠ABK=θ,
  BM=AB/2, Law of Sines) and were verified exact by the explorers.
- Load-bearing gap (L3): the projection identity, after substituting the closed
  forms. CAS-certifiable since the family is 1-parameter — legitimate.
- Issue to close while building: step 3 (the "closing relations" from E2,E3 that
  fix β,γ and the free length as functions of θ) is under-specified in the
  outline — this is where the real coupling lives and it is labelled "mechanical"
  but not written. The builder must actually derive it; it is not obviously free.
  Keep θ a free continuum (do not over-constrain to one θ). Organize by the B↔C
  swap so terms cancel visibly.

## complex-swap-symmetry — APPROVE (with the sharpest caveat)
- Technique (complex numbers with σ: B↔C,K↔L,M↔N as reflection across the
  imaginary axis) is appropriate; the frame B=−p,C=p,A=a makes σ manifest.
  L1 (`OM=ON ⟺ Re(O)=Re(a)/2`, since N−M=p real, ½(M+N)=a/2) is correct.
- Load-bearing gap (L3): `Re(O)=Re(a)/2` from the reality conditions. The outline
  is HONEST that symmetry alone is insufficient (σ only puts O on a σ-invariant
  line; the reality/argument encodings of E1–E3 are what pin the real part) — this
  is the correct, non-circular reading and avoids the trap of claiming L3 from
  symmetry.
- Issue to close while building: the argument/orientation encodings in step 2 are
  the risk. E1 has opposite handedness for K vs L, so the reality condition
  `(K−B)/(A−B)·(L−C)/(A−C) ∈ ℝ₊` depends on getting the orientation sign right; a
  wrong sign silently turns a true condition false. The builder MUST fix all three
  encodings against the numeric solver before trusting the algebra. Heaviest
  algebra of the three; CAS-certifiable but the encoding step is the real content,
  not the determinant grind.

## Diversity note (for the orchestrator)
The three walls are genuinely different objects: a synthetic inscribed-angle
identity (power route), a trig projection identity (trig route), an algebraic
real-part identity (complex route). Good spread for round 1. One watch item:
trig-lawofsines and complex-swap-symmetry both bottom out on a CAS elimination
over the 1-parameter family, and the computational explorer warned the angle
system may be intractable in closed form. If both stall on "can't set up / grind
the parametrization," they share a practical wall despite different framings —
in that case next round should push ≥1 approach onto the purely synthetic power
identity (or a new framing entirely) rather than a fourth CAS bash. The
power-of-point route is the diversity anchor: it is the one with no CAS fallback
and the cleanest final target.

## Ranking
Registered all three (cold-start 1500). Ranked head-to-head: trig ≈ power-of-point
(draw — both have exact, verified reductions and clear certifiable endgames),
both beat complex (heaviest algebra + orientation-sign risk + explicit
"symmetry-alone-insufficient" caveat). Result: power-of-point 1517, trig 1515,
complex 1469. Tight cluster — appropriate for an empty round-1 population; keep
the field broad.

build set: power-of-point-BC, trig-lawofsines, complex-swap-symmetry
