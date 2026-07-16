# Outline Review — imo-2026-03, Round 13

Field: three "advance" plans (no new slug, no copy). All already registered. I independently
spot-checked each load-bearing claim with off-grid exact Fractions / large float scans, then
Fraction-confirmed. Verdicts, ranking, build set below.

---

## geometric-selfsimilar — VERDICT: APPROVE (advance; PRIMARY deliverable HS-A2)

Target: close HS-A2 (pair2_3 gives A(Y'',3) ≤ t in the Sub-A-P branch, δ>2t) → T5's δ>2t branch.

**Checks (all off-grid, Σ=31, t=1):**
- **HS-A2 claim is TRUE.** Over 8.7k–10.4k genuine pair1_2 failures that are truly Sub-A-P
  (menu(Y')>t, bottom(Y')=δ, P fires, δ>2t), the pair2_3 R/S/P/C menu closes **0 failures**.
  The technique works.
- **The Σ-P bound [*]** `2d₂ ≤ 31−7δ−6d₄−4d₃` — re-derived from scratch (D1_{Y'}=d₁−p₃=31−6δ−5d₄−4d₃−2d₂,
  Sub-A-P condition D1_{Y'}≥δ+d₄) and verified **0 violations** on genuine Sub-A-P configs. Matches
  the outliner's "31−2p₂−4δ−3d₄−2d₃ ≥ δ+d₄".
- **Case A constant** `E2 ≤ (31−9δ−8d₄−4d₃)/2 < t/2` — verified 0 violations.
- **R12 witness X={157/5,13,46/5,34/5,23/5}**: Σ=65, t=65/31; pair1_2 fails (menu S=2.2>t=2.097),
  pair2_3 closes (menu S=0.8≤t). Falls in **Case C1** (δ−t=2.503 ≤ d₂=3.8 < δ=4.6), E3=δ−d₂=0.8=0.381t,
  S closes. Exactly as the outliner states.
- **6-case coverage is exhaustive & disjoint.** p₁ is always max(Y'') (d₂<p₂≤p₁, p₄,p₅<p₁);
  p₄>p₅ always; the split is on d₂'s position: d₂>p₄ (A), δ≤d₂≤p₄ (B1/B2 by d₂ vs δ+t),
  d₂<δ (C1/C2/C3 by δ−t and 3t). Covers all d₂. Confirmed.
- **Forced ordering:** every genuine Sub-A-P failure has Y' ordering d₁>p₃>p₄>p₅ (8688/8688), so
  the outliner's assumption bottom=δ, e₃=d₄ IS valid — it is forced by the branch definition
  (D1_{Y'}≥δ+d₄>0 ⇒ d₁>p₃). Good; this must be written as a step, not assumed.

**Issues for the builder (CHANGES-level within the build, not blockers):**
1. Justify the **pair2_3 reduction** (cut p₂ at offset p₃ ⇒ invisible pair ⇒ Y''={p₁,d₂,p₄,p₅}
   at budget 3) via the certified Lemma R1 — the outliner marks it "DONE by R1"; it is the
   analogue of the certified pair1_2 reduction, but write the R1 instance explicitly.
2. Prove that Sub-A-P failures FORCE the Y' ordering d₁>p₃>p₄>p₅ (so [*] and the bottom=δ,
   e₃=d₄ identification are valid). This is the linchpin — do not leave it implicit.
3. Write **Case C2** (P fires on Y'': D1_{Y''}=p₁−p₄≥δ, A_P=d₂/2<t) and **Case C3** vacuousness
   rigorously with every constant in units of t.
4. **Honesty flag (must be preserved):** even with HS-A2 closed, **T5 is NOT complete.** The other
   ~40k of ~50k genuine pair1_2 R/S/P/C failures are the merge-family gap **G1** (Sub-A-C / Sub-B),
   which is conjectural (numerics only, no analytic write-up). Do NOT claim n=4 UB rigorous this
   round. G3 (m≥6) stays deferred. This is an advance, delivering HS-A2 as a certified sub-lemma.

No forbidden route is used (SB-monotone, R3-cascade, complement-cut, p₁@p₂ all avoided). Off-grid
Fractions throughout. Sound to build.

---

## ll-inclusion-gap — VERDICT: APPROVE (advance; PRIMARY band-accounting size≥3)

- **Size-2 equal-pair forcing THEOREM is CORRECT.** Verified: for a∈[1,2^j), j=1,2,3, **0**
  non-equal admissible pairs exist (18911 configs). (For a<1 non-equal pairs DO exist — the a≥1
  hypothesis is load-bearing and correctly stated, since it gives ΣR_lo≥2^{j+1}.) The mechanism
  (Case A p₁>2^j ⇒ band (2^j,p₁) is R-even ⊄ S_{R_lo}; Case B p₁≤2^j ⇒ p₂>2^j≥p₁ contra) is sound.
  Then A(Q_lo)=0 and A(R)−A(Q)=deficit_top+A(R_lo)≥A(G_{j−1})≥1 via the certified Floor Lemma.
  **Closes size-2 all j and all even j — write it.**
- **Band-accounting (★) for size≥3 (PRIMARY GAP):** the route is `A(Q_lo)=measure(S_{Q_lo})≤measure(S_{R_lo})=A(R_lo)`
  (certified alt-sum-integral) + sum constraint (σ_lo<2) + top-pair forcing (p₁≤2^j). This is a
  **DIRECT** argument, NOT the perturbed T'(j) mutual induction (Opening B), which the outliner
  explicitly DECLINES — correct, since T'(j)'s descent {a}∪G_{j−2} re-treads the R10-refuted
  {Claim_R,T_R} class. So the route is **non-circular and avoids the refuted class.** Good.
- **Target is TRUE with large slack:** verified min(A(R_lo)−A(Q_lo)) = **9/4** for size-3 odd j=3
  (needs ≥1−deficit_top); size-4 Opening D gives ≥1 concretely. The band bound "should close"
  is a plausibility claim (the honest open crux), but the ingredients are concrete and the slack
  is comfortable.

**Issue for the builder:** pure measure-monotonicity only gives ≥0; the ≥1−deficit_top must come
from the sum constraint + top-pair forcing bounding the UNCOVERED measure from below. That step is
the genuine gap — do not let it collapse to bare monotonicity. Do NOT use "perturbed L1 without sum
constraint" (FALSE: j=1,a=1,Q={2}). Do NOT re-open T'(j) mutual induction. Sound to build as advance.

---

## ll-dyadic-symdiff — VERDICT: APPROVE (advance; PRIMARY R-cut-pairing generalization)

- **n=3 R-cut-piece-2 pairing identity is RIGOROUS.** Verified via measure{g odd}: with R={b,2−b,1,4},
  Q={q1≤q2≤q3}⊂(2,4), A = b + (1−b) + (q2−q1) + (4−q3) = 1 + (q2−q1) + (4−q3) > 1, **0 mismatches**
  (2000 configs). The paired R-fragment contributions (odd-g on (0,b) measure b, on (1,2−b) measure
  1−b) sum to exactly 1 regardless of b. Mechanism template is sound.
- **Valid BYPASS:** the mechanism is a DIRECT geometric level-decomposition, not routed through the
  alternating-tail crux A(Q'∪R'')≥1 nor the R11 circular target B₊≤A₋+B₋. Max|g|-agnostic. Satisfies
  the intent of a genuine rival bypass.
- **Generalization (steps i,ii,iii) is the PRIMARY GAP — honestly flagged.** The per-cut pairing is
  clean; the genuinely hard parts are correctly identified: (ii) cancellation-avoidance (paired
  measures not double-counted / cancelled by Q breakpoints) and (iii) the multi-cut level-decomposition
  A=Σ_k A_k with A_k≥0. These are far from proven.

**Caveat (affects ranking, not verdict):** the "rigorous n=3 sub-case" is a re-derivation of the
n=3 bucket-(iii) that was already FULLY CLOSED in R9 — the deliverable value is the NEW mechanism as
a template, whose generalization is unproven. Weakest certain-deliverable of the three, but a
legitimate live rival. Builder must keep it max|g|-agnostic, use N_R(x)=#{r∈R:r>x} (values not
positions), and NOT rely on the non-rigorous budget-forcing/odd-mult argument. Sound to build.

---

## Ranking (updated; stale flags cleared)

geometric-selfsimilar **1771.7** > ll-inclusion-gap **1644.7** > ll-dyadic-symdiff **1501.6**
> alternating-sum-value **1368.4** > extremal-smoothing **~1220**.

Head-to-head evidence: geometric > incgap (UB is one verified sub-lemma + a large-but-flagged gap
from a complete bound; HS-A2 checks clean) ; incgap > dyadic (incgap PROVED a real sub-case this
round — size-2 forcing verified 0-viol — while dyadic re-derived already-closed n=3 and its
generalization is far) ; dyadic > alternating-sum-value (dyadic live/advancing vs alt-sum unbuilt
since R3, greedy proven sub-optimal) ; alternating-sum-value > extremal-smoothing (S1 stuck 5+
rounds, last). Order unchanged from R12 — well-supported, not inertia.

No register/copy this round (all three advancing slugs already in the population; the outliner
correctly declined a copy — the three cruxes are distinct and each is one step from its track).

build set: geometric-selfsimilar, ll-inclusion-gap, ll-dyadic-symdiff
