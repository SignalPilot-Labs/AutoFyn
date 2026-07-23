## imo-2026-02

Round 1, empty population. Opening a field of THREE rival approaches, each a
complete attempt at proving `OM = ON` end to end. All three share the free,
two-line reduction `OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL)` (ground truth), but from
there they diverge into genuinely different machinery and hit DIFFERENT walls —
they do not collapse to one gap.

Shared numeric ground truth I re-verified myself (θ=0.3,0.45,0.6 on a scalene
triangle, exact to 1e-10): `OM=ON`; the core reduction below; and the cevian
formulas. These are reliable but still to be PROVEN.

---

power-of-point-BC: new
Target: `OM = ON` (the whole claim).
Technique: power of a point + radical-axis / directed-angle chase (synthetic).
Skeleton:
  1. `OM=ON ⟺ pow(M,ω)=pow(N,ω)`, `ω=⊙(AKL)` — power of a point.
  2. `pow(M)=pow(B)/2 − AB²/4`, `pow(N)=pow(C)/2 − AC²/4` — power is the quadratic
     `x(x−a')` along a line with `A` at `0`, `A'` at `a'`; eliminate `a'`.
  3. Reduce to core: `pow(B,ω) − pow(C,ω) = (AB²−AC²)/2`.
  4. GAP: prove the core from (E1)-(E3), via `pow(B)=BK·BK₂`, `pow(C)=CL·CL₂`
     and locating second intersections by inscribed angles + the angle conditions.
Key lemmas:
  - `pow(M)=pow(B)/2 − AB²/4` — proved, exact (verified numerically).
  - Core `pow(B)−pow(C)=(AB²−AC²)/2` — verified numerically (=2.625 constant
    across the whole family), UNPROVEN. Cross-check: equivalent to
    `(B−C)·(A+½(B+C)−2O)=0`, i.e. O on perp-bisector of MN — matches fixed line.
Open gaps: step 4 / the core identity — the single wall.
Cases to cover: none (continuous family).
Watch out for: signed lengths (A' lies between M and B); do NOT assume BK tangent,
BKLC cyclic, or spiral side-ratio equality (all ruled out).

---

trig-lawofsines: new
Target: `OM = ON`.
Technique: Law of Sines in the sub-triangles + direct metric elimination, aiming
at the fixed-line invariant `(O−½(M+N))·(C−B)=0`. Never forms ω's second
intersections — distinct machinery from power-of-point-BC.
Skeleton:
  1. Free param `θ=∠KBA=∠ACL`; K on ray θ-off-BA from B, L on ray θ-off-CA from C.
  2. `BK=(AB/2) sinγ/sin(θ+γ)`, `CL=(AC/2) sinβ/sin(θ+β)` (γ=∠BMK=∠LCK,
     β=∠LNC=∠LBK) — Law of Sines in △BMK, △CNL. VERIFIED exact.
  3. Close the system with sine rule in △BKL (E2), △CKL (E3); write K,L in θ.
  4. GAP: compute `O=circumcentre(AKL)` and show `(O−½(M+N))·(C−B)=0`.
  5. Conclude.
Key lemmas:
  - Cevian formulas (step 2) — proved, exact.
  - Projection identity (step 4) — UNPROVEN wall; a trig identity in θ,β,γ,
    CAS-certifiable since the family is 1-parameter.
Open gaps: step 3 (mechanical closing relations) and step 4 (the wall).
Cases to cover: none.
Watch out for: θ is the free parameter (a continuum), not a given; do not
over-constrain to one θ. Organize by the B↔C swap so terms cancel visibly.

---

complex-swap-symmetry: new
Target: `OM = ON`.
Technique: complex numbers exploiting the involution σ (B↔C, K↔L, M↔N). Angle
conditions become reality/argument conditions; target becomes a real-part
equality. Genuinely different machinery from both above.
Skeleton:
  1. Frame: midpoint(BC) at origin, BC on real axis, `B=−p, C=p` real, `A=a`;
     σ = reflection across imaginary axis + K↔L.
  2. Encode E1,E2,E3 as three reality/argument conditions on ratios of
     `A,B,C,K,L,M,N`.
  3. `OM=ON ⟺ Re(O)=Re(a)/2` (since `N−M=p` real, `½(M+N)=a/2`).
  4. GAP: with `O` from the standard complex circumcentre determinant, prove
     `Re(O)=Re(a)/2` using the three reality conditions.
  5. Conclude.
Key lemmas:
  - `OM=ON ⟺ Re(O)=Re(a)/2` — proved in this frame.
  - σ preserves hypotheses ⇒ `O↦−Ō` — proved.
  - `Re(O)=Re(a)/2` — UNPROVEN wall; symmetry alone only gives O on a σ-invariant
    line, the reality conditions pin the real part.
Open gaps: step 4 — the wall. CAS-certifiable with symbolic a,p and free param.
Cases to cover: none.
Watch out for: orientation signs in the `arg` encodings (E1 has opposite handed-
ness for K vs L); symmetry alone is insufficient — the reality conditions are
required.

---

### Why these three are far apart (no shared wall)
- power-of-point-BC's wall is a **synthetic identity about ω's second intersections
  from B and C** (`pow(B)−pow(C)=(AB²−AC²)/2`) — pure directed-angle/power content,
  no coordinates.
- trig-lawofsines's wall is a **metric/trig elimination** of an explicit projection
  in the angle variables θ,β,γ — it never constructs ω's second intersections.
- complex-swap-symmetry's wall is an **algebraic real-part identity** driven by the
  σ-involution — different representation entirely.
If the power identity resists a synthetic proof, the trig and complex routes attack
completely different objects and can succeed independently. The B↔C, K↔L, M↔N swap
symmetry is the one organizing thread common to all three (it should shape every
candidate lemma), but each route realizes it through different tooling.

build set: power-of-point-BC, trig-lawofsines, complex-swap-symmetry
</content>
