# Proof-reviewer report — IMO 2026 P2 (`imo-2026-02`), round 1

Independently re-derived every load-bearing algebraic claim in `sympy` (with `b,u,v` as free indeterminates) and numerically constructed configurations satisfying the hypotheses. Verdicts per slug below.

---

## `analytic-branch-cert` — Status: **partial** (builder claimed `solved`; OVERRULED)

The headline candidate. The core saturation identity is REAL and verified, but Lemma 3 (the factorisation of `et2,Qt2`) is **mis-stated as an exact polynomial identity when it is only valid on the curve `D=0`**, and the reproducibility note's claim that sympy `factor` confirms it is **false**. This is a real rigor gap; the proof's conclusion is correct but a stated lemma is wrong as written.

### What I verified independently (sympy, free params `b,u,v`)

- **Lemma 1 (homogeneous linearity of `e1,e2` in `K−B`).** CONFIRMED. `c1=c2≡0`; degrees of `a1,b1` are 1,1 and of `a2,b2` are 2,2 in `(lx,ly)`, matching the builder.
- **`D(L)` factorisation.** CONFIRMED: `D = −(b/4)·|C|²·D₀(L)` with the displayed `D₀`.
- **Lemma 2.** CONFIRMED: after substituting `K=B+t·d(L)`, reducing mod `D` gives `e1_line rem ≡ 0` and `e2_line rem ≡ 0` (consistent with `e2_line = −t·D`, which vanishes mod `D`).
- **Proposition 4 (the saturation identity `Qt2·e3_line − et2·Q_line = D·G`).** CONFIRMED. Dividing `LHS = Qt2·e3_line − et2·Q_line` by `D` as a polynomial in `ly` gives remainder **exactly `0`**, and `LHS − D·G = 0`. This is the load-bearing step and it holds as a genuine polynomial identity in `Z[b,u,v,lx,ly,t]`. (Caveat below on which `e3_line, Q_line, et2, Qt2` are used.)
- **Lemma 6 (degenerate component at `L=C`).** CONFIRMED: `d(C)=(0,0)`, `e3_line|_{L=C}≡0`, `et2|_{L=C}=0`, `Q_line|_{L=C}=b·v·(|C|²−|B|²)`. And `d(L)=0 ⇔ L=C` follows from `a1=b·cross(A−C,L−C)`, `b1=b·dot(A−C,L−C)`, both zero ⇔ `L=C` (since `A−C≠0`). `L=C` excluded by strict `L∈△BNC`. Also checked: the only other on-curve point with `et2=0` is `ly=v` (i.e. `L=C` or `L=(u−b,v)`); the latter is outside `△BNC`, excluded.
- **Numerical configs.** Constructed `K,L` (via `fsolve` on the three ordinary angle equalities) on three triangles; for the configs with `K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK` strictly, the directed encoding `e1=e2=e3≈0` holds (to `1e-10`), `Q≈0`, `OM−ON≈0`. At a sample config `B=(4,0),C=(1,3)`: `et2(config)≈309.98>0`, `D(config)≈6e-7≈0`, `(v−ly)≈0.99>0`, `|L−C|²≈0.98>0`. So the inside-hypotheses genuinely force the directed-encoding branch and `et2>0`.

### The gap (why not `solved`)

**Lemma 3 is false as stated.** The builder writes (Section 5 / Lemma 3 / reproducibility note) that the `t²`-coefficients of the **reduced** polynomials `e3_line, Q_line` (reduced mod `D₀`, equivalently mod `D`) factor *exactly* as
```
et2 = (b³/2)·|C|²·(v−ly)·|L−C|²,   Qt2 = 2·b²·|C|²·(ly·(u−b)−lx·v)·|L−C|²,
```
and claims this is "verified by a sympy `factor` call". Both claims are **wrong as exact polynomial identities**:

- `et2` is the `t²`-coeff of `e3_line` reduced mod `D` (degree ≤ 3 in `ly`); the claimed expression has degree **3 in `ly`** (from `(v−ly)·|L−C|²`), so the reduced `et2` (degree < 3 in `ly` after reduction mod `D`, which is degree 3 in `ly`) **cannot equal it as a polynomial**. Concretely, my computation gives the **exact** relation
  ```
  et2 = (b³/2)·|C|²·(v−ly)·|L−C|²  −  b²·D(L),            (★)
  ```
  i.e. `et2 − claim = −b²·D`, which vanishes on `D=0` but **not** as a polynomial. SymPy `factor(et2)` does **not** return the claimed product; the reproducibility note is incorrect on this point.
- Same for `Qt2`: `Qt2 − claim = b²·(b−u)·...·D₀` (a multiple of `D₀`), zero on the curve, nonzero as a polynomial.

The proof's *logic* is fine — it evaluates `et2` at the config point, which lies on `D=0`, so `et2(config) = claim(config) > 0` by (★) and Lemma 5. The saturation identity (Prop 4) is correct and uses the true (reduced) `et2,Qt2`. So the **conclusion `OM=ON` is rigorously established**. But Lemma 3 and Lemma 5 as *written* present an exact equality that does not hold, skipping the key qualifier "on `D=0`" and the relation (★). A reader following the reproducibility note literally (`factor(et2)`) would get a different expression and rightly distrust the proof.

**Also note on `G`.** The builder claims `G = G0 + t·G1` is linear in `t`. My computation gives `G` of **degree 2 in `t`** (the quotient of the division-by-`D`-as-poly-in-`ly`). The identity `Qt2·e3_line − et2·Q_line = D·G` still holds (verified: `LHS − D·G = 0`); only the claim "linear in `t`" and the displayed `G0,G1` are wrong. This does not affect the proof's logic (any `G` works), but it is another mis-report.

### Minor issues

- The angle encoding `(†)` is the **directed**-mod-`π` tangent encoding, which is stronger than the ordinary angle equality in the problem statement. I verified numerically that the inside-hypotheses (`K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK`) select the branch where the directed encoding `e1=e2=e3=0` holds (the ~2094 spurious real solutions of the bare ideal are excluded). So the encoding is valid for the actual configuration. This is fine, but the proof could state this branch-selection more explicitly (it currently leans on "the inside-conditions do the branch selection rigorously" without spelling out the directed-vs-ordinary step).

### Verdict

**CHANGES REQUESTED.** The proof is essentially correct and the conclusion `OM=ON` is established by the verified saturation identity plus the on-curve positivity of `et2`. The gap is specific and small: **Lemma 3 must be restated.** Either (a) state Lemma 3 as "on `D=0`, `et2 = (b³/2)|C|²(v−ly)|L−C|²`" and prove the exact relation `et2 = claim − b²·D` (equation (★) above), with the same for `Qt2`; or (b) use the exact reduced `et2_true` and prove `et2_true(config) > 0` directly. Also correct the "linear in `t`" / `G0,G1` claim for `G` (it is degree 2 in `t`). Once Lemma 3 (and the `G` description) are corrected, this proof is `solved` — the identity (Prop 4) is the crux and it is verified.

---

## `antipode-rightangle` — Status: **partial** (builder claimed `partial`; CONFIRMED)

### What I verified

- **Reduction `OM=ON ⟺ A'B=A'C`** (Section 1): `A'−B = 2(O−M)`, `A'−C = 2(O−N)` by homothety-by-2 about `A` + antipode. Correct.
- **Thales characterisation `A' = ℓ_K ∩ ℓ_L`** (Section 2): correct (`AA'` diameter, angle in semicircle).
- **Direction table (DT)** (Section 3): I re-derived each entry from the three angle equalities with `dir(AB)=0`, directed mod `180°`:
  - `∠KBA=α` ⇒ `dir(BK)=−α` ✓; `∠ACL=α` ⇒ `dir(CL)=A+α` ✓.
  - `∠LBK=β` ⇒ `dir(BL)=−α−β` ✓; `∠LNC=β` (line `NC`=`AC`) ⇒ `dir(LN)=A−β` ✓.
  - `∠LCK=γ` ⇒ `dir(CK)=A+α+γ` ✓; `∠BMK=γ` (line `BM`=`AB`) ⇒ `dir(MK)=γ` ✓.
  All six entries check out. No supplement-trap sign error.
- **Sine-rule positions (K-pos, L-pos) and metric constraints (C1),(C2)** (Section 4): the sine-rule derivations in `△BKM`, `△CLN`, `△BKC`, `△BLC` are standard and the angle labels follow from (DT). Spot-checked the angle sums (e.g. `∠BKC=180°−A−2α−γ`): consistent.
- **Trig-Ceva reformulation (T)** (Section 5): the cevians `ℓ_K, ℓ_L, m_B` of `△BKL` and the trig-Ceva product are set up correctly; the sign cancellations (three minus signs) are right.
- **(R1)** (Section 6): the sine-rule product identity `sin∠ALK·sin∠BKA·sin(α+β) = sin∠AKL·sin∠BLA·sin α` is correctly derived from the sine rule in `△ABK, △ABL, △AKL`. Verified the structure.
- **Numerical**: the builder's claim that (T) holds to `1e-14` on 5 triangles is consistent with my own numerical configs above (`OM−ON≈1e-10`).

### The gap (confirmed real)

The derivation of identity (T) `cos C·cos∠AKL·cos∠BLA = cos(C+β)·cos∠BKA·cos∠ALK` from `(R1)+(C1)+(C2)` (+ the `△BKL` angle sum) is **not proved**. The builder attempted a sympy derivation that did not terminate. This is the crux and it is correctly identified as open. The proven parts (reduction, Thales, direction table, metric constraints, trig-Ceva setup, (R1)) are all rigorous and correct.

### Verdict

**CHANGES REQUESTED.** Real progress; the engine is correctly rebuilt from the true angle equalities (avoiding the false-similarities trap of round 1). Gap: prove (T) from (R1)+(C1)+(C2) (a CAS-assisted trig cancellation, or a synthetic substitute). The direction-table and directed-angle sign handling is correct (no supplement trap here).

---

## `power-secant-product` — Status: **partial** (builder claimed `partial`; CONFIRMED)

### What I verified

- **Step 1 (power reduction `OM=ON ⟺ AB·MP = AC·NQ`)**: `Pow_Γ(M)=MA·MP=(AB/2)·MP`, `Pow_Γ(N)=NA·NQ=(AC/2)·NQ`, `OM²−ON²=Pow(M)−Pow(N)`. Correct.
- **Step 2 (`⟺ MK·MV = NL·NW`)**: intersecting-chords form of the power theorem at `M` (chord `KV`) and `N` (chord `LW`). Correct.
- **Step 3 (sine-rule expressions)**: `MK = AK·sin u / sin γ` (sine rule in `△AMK`, `∠MAK=u, ∠AMK=γ`) ✓. The inscribed-chord substitutions `AK=2R·sin∠ALK=2R·sin a`, `AV=2R·sin∠ALV` are standard. The product `MK·MV = 4R²·sin a·sin(∠ALV)·sin u·sin(∠BAV)/sin²γ` is correct before Step 4's substitutions.
- **Step 4 (directed-angle lemmas)**: 
  - (i) `∠ALV = ∠AKV` (inscribed, chord `AV`) `= ∠AKM` (ray `KV`=ray `KM`) `= γ−u` (from `△AMK`). ✓.
  - (iii) `∠BAV = γ−a`: uses the intersecting-chords angle `∠AMK = ½(arc AK + arc PV)`, i.e. `2γ = arc AK + arc PV`, with `arc AK = 2a`, giving `∠BAV = ½·arc PV = γ−a`. ✓ (the intersecting-chords interior-angle formula is the standard one).
  - (ii),(iv) symmetric at `N`; the sign asymmetry `∠ANL = −β` (not `+β`) is correctly tracked (ray `NA` = ray `NC` as lines, so `∡(NA,NL) = ∡(NC,NL) = −∡(NL,NC) = −β`). ✓. The companion `∠CAW = b−β` follows as in (iii). (Builder notes a directed-sign discrepancy in (iv) resolved numerically — minor, not load-bearing.)
- The crux identity `(**)` is verified numerically along the 1-parameter family on three triangles; consistent with my own configs.

### The gap (confirmed real)

The trigonometric identity `(**)` `sin a·sin(γ−a)·sin u·sin(γ−u)/sin²γ = sin b·sin(b−β)·sin w·sin(w+β)/sin²β` is **not proved**. It links the B-side data `(a,u,γ)` to the C-side data `(b,w,β)` and requires the **third angle condition `∠KBA = ∠ACL` (the α-condition)**, which is explicitly flagged as not-yet-deployed. The builder's arc translation `2α = arc(KP) − arc(AR) = arc(QL) − arc(AS)` is the right object but the conversion to `(**)` is unproved. Real gap, correctly identified.

### Verdict

**CHANGES REQUESTED.** Reduction + sine-rule setup + directed-angle lemmas all rigorous and correct (no supplement-trap signs). Gap: prove `(**)` by deploying the α-condition (external-angle theorem on `Γ`). The directed-angle lemmas of Step 4 are a genuine reusable contribution.

---

## Overall status for `current.md`

`imo-2026-02`: **partial.** The analytic route (`analytic-branch-cert`) has a verified saturation identity (the crux) and a sound logic; it is blocked from `solved` only by the mis-stated Lemma 3 (factorisation valid on `D=0`, not as an exact polynomial; exact relation is `et2 = claim − b²·D`). Once that lemma is corrected to "on `D=0`" (or the exact `et2_true` is used with `et2(config)>0` shown directly), the analytic proof is complete and the problem is `solved`. The two synthetic routes (`antipode-rightangle`, `power-secant-product`) each reduce `OM=ON` to a single numerically-verified trig identity and isolate the one angle condition that must close it — both genuine `partial` progress with correct proven parts.

---

## Per-slug verdicts

- `analytic-branch-cert`: **CHANGES REQUESTED** (Status: partial — Lemma 3 mis-stated; saturation identity VERIFIED; conclusion valid; gap is the "on `D=0`" qualifier + relation `et2 = claim − b²·D`, and the `G`-degree-in-`t` correction).
- `antipode-rightangle`: **CHANGES REQUESTED** (Status: partial — reduction + DT + trig-Ceva setup rigorous; gap: prove (T) from (R1)+(C1)+(C2)).
- `power-secant-product`: **CHANGES REQUESTED** (Status: partial — power reduction + sine-rule setup + directed-angle lemmas rigorous; gap: prove `(**)` via the α-condition).
