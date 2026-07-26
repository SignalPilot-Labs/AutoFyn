# imo-2026-02 — round 2 outline field

**Problem.** Let ABC be a triangle, M midpoint of AB, N midpoint of AC. K inside △BMC, L inside △BNC, with K inside angle LBA, L inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. Let O be circumcentre of △AKL. Prove OM = ON.

**Field verdict this round.** Round-2 scouting established:
- (complex lens) The round-1 verdict "saturation identity (Prop 4) is FALSE" was itself an arithmetic slip: at the alleged counterexample `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3`, the cleared target `Q` evaluates to `320/3`, NOT `256` (independently re-confirmed by recomputing `Q` from the cleared-target formula). With the corrected `Q`, the saturation LHS `Qt2·e3 − et2·Q` vanishes at that point (the wrong `Q=256` gave `35840/3 ≠ 0`). Field-division over `Q(b,u,v,lx,t)[ly]` reportedly returns remainder `0` with an explicit quotient `G` (linear in `t`). The analytic route is the leading solve candidate, BUT round 1 was burned by a false "verified" (ring pseudo-remainder misled), so the builder MUST re-verify from scratch (recompute Q, re-run field division, state G explicitly) — not trust the round-2 report alone.
- (alpha lens) The α-condition `∠KBA=∠ACL` is the load-bearing closing step for BOTH synthetic cruxes. The directed external-angle theorem on Γ is the **SUM** form `2α = arc(RA)+arc(KP) = arc(AS)+arc(QL)` (NOT the round-1 difference form). A CONFIRMED sign error in `power-secant-product` Step 4(iv): `∠CAW = -(b+β)`, not `b−β`; the corrected crux (**) has `sin(b+β)` (verified ~1e-13). α is necessary AND sufficient (drop-test: both (**) and OM=ON fail in lockstep when α is dropped). Bridge from α arc-sum to (**) needs midpoint projective structure (pencil-at-K cross-ratio `(A,P;R,V)=(A,P;B,M)`) + Ptolemy on cyclic quads.
- (inversion lens) Inversion at A (r²=AB·AC) reduces `OM=ON ⟺ P∈A-Apollonius circle of △AB'C'` — this is the antipode reduction conjugated by inversion (same wall, one step later, different shape). NO cleaner closing lemma found; 4-point concyclities all fail; rotation-composition REJECTED numerically. Honest verdict: rival framing, not a bypass.

**Decisions.** (1) ADVANCE `analytic-branch-cert` — nominate for a builder to re-verify the corrected saturation identity from scratch and write the complete rigorous proof. Leading solve candidate; treat round-1 false-verified as caution. (2) REVISE `power-secant-product` — fix the sign error, restate corrected crux with `sin(b+β)`, attempt closing via α arc-sum + pencil cross-ratio + Ptolemy. (3) ADVANCE `antipode-rightangle` — close (T) via the α arc-sum mechanism (note (T) ⟺ (**)_corr, so a closing of one transfers). (4) OPEN NEW `analytic-resultant-cert` — a genuinely different closing certificate (resultant-in-`t` factorisation `res_t(e3,Q)` divisible by `D₀²` + et2>0 branch selection) inside the analytic family; insurance against the saturation identity being false again. Do NOT open the inversion slug (same wall, no cleaner closing). Do NOT open a 5th speculative framing (no confirmed-viable genuinely-new framing exists; rotation-composition and spiral-sim both rejected numerically).

---

## imo-2026-02

### analytic-branch-cert
**Action:** advance
**Target:** Prove OM = ON (the whole theorem), via the coordinate reduction `OM=ON ⇔ Q=0` and the saturation identity forcing `Q_line=0` from `e3_line=0` on the curve `D₀=0`.
**Technique:** Coordinate geometry (A=0, B=b real, C=(u,v)) + directed-angle polynomial encoding (`e1,e2,e3`) + minimal-polynomial field reduction mod the cubic `D₀(L)` + **ideal saturation / Rabinowitsch trick** (the certificate `Qt2·e3_line − et2·Q_line = D₀·G`), KB `Algebra & Polynomials — minimal-polynomial reduction`, `Linear Algebra — ideal saturation`.
**Skeleton:**
  1. Coordinate normalisation `A=(0,0), B=(b,0), C=(u,v)`, `b>0, v>0`; `M=(b/2,0), N=(u/2,v/2)` (similarity WLOG). — KB `Geometry — coordinates/complex/barycentric`.
  2. Circumcentre `O` of `△AKL` via `2O·K=|K|², 2O·L=|L|²`; compute `OM²−ON² = O·(C−B) + (|B|²−|C|²)/4`; clear by `2·det(K,L)` to get `OM=ON ⟺ Q(kx,ky,lx,ly)=0` (the explicit cleared polynomial `Q`). — `analytic-target-line` lemma (round-1, proved).
  3. Encode the three directed-angle equalities `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK` as polynomials `e1,e2,e3` via the tangent form `cross(p,q)·dot(r,s) − cross(r,s)·dot(p,q)=0`. — KB `Gröbner / Rabinowitsch` (tangent-of-directed-angle form).
  4. `e1,e2` are homogeneous-linear in `K−B`; for `K≠B` the determinant `D(L)=−(b/4)|C|²·D₀(L)` vanishes (a cubic in `L`), and `K=B+t·d(L)` with `d=(b1,−a1)`; on `D₀=0`, `e1≡0`, `e2=−t·D`. — `angle-linearity-cubic-reduction` lemma (round-1, proved).
  5. Substitute `K=B+t·d(L)` into `e3` and `Q`; reduce mod `D₀=0` (over the FIELD `Q(b,u,v,lx,t)[ly]`, NOT the ring `Z[...][ly]` — ring pseudo-remainder misled round 1). Both become quadratics in `t`: `e3_line=et2·t²+et1·t+et0`, `Q_line=Qt2·t²+Qt1·t+Qt0`. — KB `Algebra & Polynomials — minimal-polynomial reduction`.
  6. **Leading-coefficient identity (proved):** `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² − b²·D(L)` as a genuine polynomial identity over `Q(b,u,v,lx,t)`; ON `D=0` it factorises as `(b³/2)·|C|²·(v−ly)·|L−C|²`. — `et2-on-D-zero-relation` lemma (round-1, proved by direct subtraction).
  7. **Positivity (proved):** `L∈△BNC` strictly ⟹ `ly<v` (barycentric argument: `ly=(1−λ_B−λ_N/2)·v < v`) and `L≠C ⟹ |L−C|²>0`; with `b>0, |C|²>0` this gives `et2>0` on `D=0` at the configuration. — Lemma 5 (round-1, proved).
  8. **Degenerate exclusion (proved):** `d(L)=0 ⇔ L=C`; at `L=C`, `e3_line≡0` for all `t` while `Q_line=b·v·(|C|²−|B|²)≠0` generically, and `K=B` — excluded by `K∈△BMC` strictly and `L∈△BNC` strictly. — Lemma 6 (round-1, proved).
  9. **THE CLOSING STEP (GAP — builder re-verifies and writes):** the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` with `G` linear in `t` (and at most linear in `ly`). Round-2 complex explorer reports this is GENUINELY TRUE: round-1's "FALSE" verdict used the wrong value `Q=256` at the alleged counterexample (correct `Q=320/3`, re-confirmed here independently); field division `sp.Poly(LHS, ly, domain=QQ.frac_field(b,u,v,lx,t)).rem(Poly(D₀,...))` returns remainder `0` with explicit quotient `G`; 6-point substitution re-verified. **Builder must re-verify from scratch:** (a) recompute `Q` at the round-1 counterexample from the cleared-target formula and confirm `320/3`; (b) re-run the field-division remainder check and STATE the explicit quotient `G`; (c) confirm `G` is linear in `t`. KB `Linear Algebra — ideal saturation`.
  10. On `D=0`, the saturation identity gives `et2·Q_line = Qt2·e3_line`. At the configuration `D=0`, `e3_line=0` (third angle condition), `et2>0` (Step 7), and `L≠C` (Step 8). Hence `Q_line=0`, so `Q=0`, so `OM=ON`. ∎
**Key lemmas (claim + mechanism):**
  - `et2 = (b³/2)|C|²(v−ly)|L−C|² − b²·D` — because the `t²`-coefficient of the field-reduced `e3_line` factorises on `D=0` (the `−b²·D` correction vanishes there); verified by direct subtraction over `Q(b,u,v,lx,t)`.
  - Saturation `Qt2·e3_line − et2·Q_line = D₀·G` — because field division over `Q(b,u,v,lx,t)[ly]` leaves remainder `0` with explicit quotient `G`; round-1's nonzero remainder was the ring pseudo-remainder trap fed by the wrong `Q=256` (correct `Q=320/3`).
  - `et2>0` on the inside arc — because `L∈△BNC` gives `ly<v` (barycentric) and `L≠C` gives `|L−C|²>0`.
**Open gaps:** Step 9 — the saturation identity must be re-verified from scratch (recompute Q, field division, explicit G) and stated as a proved polynomial identity. All other steps are already proved.
**Cases to cover:** none beyond the degenerate `L=C` (excluded, Step 8).
**Watch out for:**
  - Round-1 false-verified trap: do NOT trust `sp.rem` over `Z[...][ly]` (pseudo-remainder); use `sp.Poly(..., ly, domain=QQ.frac_field(b,u,v,lx,t)).rem(...)`. The leading coefficient `−(b/4)|C|²` of `D` is not a unit in the ring.
  - Round-1 arithmetic slip: at the counterexample `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3`, the correct `Q=320/3` (NOT `256`); recomputed independently this round. Recompute from the cleared-target formula `Q := 2·(|K|²·ly − |L|²·ky)·(u−b) + 2·(kx·|L|² − lx·|K|²)·v − det(K,L)·(|C|²−|B|²)` with `K=(8/3,8/3), L=(1/2,7/2)`.
  - The saturation identity is the LAST load-bearing step; if it fails again, this approach dies and the resultant-twin (below) is the fallback.
**Gap to close this round:** Step 9 — re-verify and write the saturation identity with explicit `G`; conclude `Q_line=0 ⟹ OM=ON`.

---

### analytic-resultant-cert
**Action:** new
**Target:** Prove OM = ON (the whole theorem), via the SAME coordinate reduction as `analytic-branch-cert` but a DIFFERENT closing certificate: the resultant-in-`t` of `e3_line` and `Q_line` is divisible by `D₀²`, so on `D₀=0` the two quadratics share a common root; `et2>0` + inside hypotheses select the configuration's `t` as that root, forcing `Q_line=0`.
**Technique:** Coordinate geometry (same normalisation) + directed-angle polynomial encoding + minimal-polynomial reduction mod `D₀` + **resultant / "transform the roots"** (KB `Algebra & Polynomials — resultants`) as the closing certificate (instead of saturation). This is a rival certificate inside the analytic family — a genuinely different mechanism for the last step, not a re-verification of saturation.
**Skeleton:**
  1.–5. Identical to `analytic-branch-cert` Steps 1–5: coordinate normalisation, `OM=ON⇔Q=0`, `e1,e2,e3` encoding, cubic `D₀(L)=0` + line `K=B+t·d(L)`, field-reduced quadratics `e3_line, Q_line` in `t`. (Import the three promotable lemmas `analytic-target-line`, `angle-linearity-cubic-reduction`, `et2-on-D-zero-relation` from `analytic-branch-cert` — they are reviewer-certified.)
  6. **Resultant factorisation (the closing certificate — builder verifies and states):** `res_t(e3_line, Q_line) = (b⁸/16)·v²·|C|²·(|C|²−b²)·D₀²·R(lx,ly,u,v,b)` for an explicit factor `R`. Round-2 complex explorer reports this factorisation. The factor `D₀²` proves: at every point of `D₀=0` (over the algebraic closure), `e3_line` and `Q_line` share at least one common root in `t`. — KB `Algebra & Polynomials — resultants`.
  7. **Root-selection step (GAP — builder argues):** at the configuration, `D₀=0` and `e3_line=0` (third angle condition). The shared root in `t` is the configuration's `t` (selected by `K∈△BMC` strictly, `K≠B`, `det(K,L)≠0`). Use `et2>0` (Lemma 5) + `e3_line` quadratic-in-`t` structure + inside hypotheses to show the configuration's `t` IS the shared root, hence `Q_line(t)=0`. (The resultant gives existence of a shared root; the selection argument pins it to the configuration's branch.) — this is the genuinely new mechanism vs saturation.
  8. `Q_line=0 ⟹ Q=0 ⟹ OM=ON`. ∎
  9. Degenerate exclusion: same `L=C` component (Lemma 6), excluded by strict inside hypotheses.
**Key lemmas (claim + mechanism):**
  - `res_t(e3_line, Q_line)` divisible by `D₀²` — because two quadratics-in-`t` sharing a root on `D₀=0` is exactly what `D₀=0` enforces (the cubic relation between `lx,ly`); the resultant detects common roots, KB `resultants`.
  - Root selection — because `et2>0` on the inside arc makes `e3_line`'s `t²`-leading coefficient nonzero, so `e3_line=0` has a finite root set; the inside hypotheses + `K≠B` pick the configuration's `t`, which the resultant forces to be a `Q_line`-root.
**Open gaps:** Step 6 (state the resultant factorisation and the explicit `R`; verify over the field); Step 7 (the root-selection argument — the resultant gives a common root but NOT that the configuration's `t` is that root; this needs the inside-hypothesis branch-pinning, which is the hard part).
**Cases to cover:** degenerate `L=C` (excluded); the exceptional sub-case `|C|²=|B|²` where `Q_line|_{L=C}=0` (harmless — the degenerate component is excluded anyway).
**Watch out for:**
  - The resultant only gives a common root over the ALGEBRAIC CLOSURE; the configuration's `t` is a REAL root. The builder must argue the real-locus correspondence (the inside hypotheses select a real branch, as in round-1's 5256-config numerical check where `|Q|≤6.1e-9`).
  - This is INSURANCE against the saturation identity being false again. If `analytic-branch-cert`'s saturation holds, this approach is unnecessary — but it is a genuinely different closing mechanism and worth one builder.
**Gap to close this round:** Step 6 (resultant factorisation) + Step 7 (root-selection argument — the hard step).

---

### power-secant-product
**Action:** revise
**Target:** Prove OM = ON via the power-of-a-point reduction `OM=ON ⟺ MK·MV=NL·NW` and the corrected crux identity (**) `_corr` with `sin(b+β)`, closed by the α arc-sum + pencil cross-ratio + Ptolemy.
**Technique:** Power of a point (secant + intersecting chords) + inscribed-chord formula + **directed external-angle theorem, SUM form** (KB `Geometry — synthetic toolkit, angle chasing` / `circle/triangle configuration facts`) + **projective cross-ratio** (KB `Geometry — synthetic toolkit, projective ideas`) + **Ptolemy** (KB `circle/triangle configuration facts`).
**Skeleton (revised):**
  1. **Reduction (proved):** `OM=ON ⟺ AB·MP=AC·NQ ⟺ MK·MV=NL·NW` (directed), with Γ=(AKL), P=2nd∩(AB,Γ), Q=2nd∩(AC,Γ), V=2nd∩(MK,Γ), W=2nd∩(NL,Γ). — `power-secant reduction` lemma (round-1, proved).
  2. **Sine-rule expressions (proved):** `MK·MV = 4R²·sin a·sin(γ−u)·sin u·sin(γ−a)/sin²γ`; `NL·NW = 4R²·sin b·sin(b+β)·sin w·sin(w+β)/sin²β` — where `a=∠ALK, b=∠AKL, u=∠BAK, w=∠CAL, α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK`. — round-1 Step 3, with the CORRECTED Step 4(iv) sign (see Step 3' below).
  3. **CORRECTED directed-angle lemmas (REVISE):** (i) `∠ALV=γ−u` ✓; (ii) `∠AKW=−(w+β)` ✓; (iii) `∠BAV=γ−a` ✓; (iv) **`∠CAW=−(b+β)`** (CORRECTED from round-1's `b−β` — the round-1 sign-trap the rules warned about; `∠CAW` in directed form is `−b−β`, two minus signs cancel in the product). — `directed-angle lemmas` lemma (round-1, REVISED). Verify (iv) at the corrected `−(b+β)` to 1e-13 across configs.
  4. **Corrected crux identity (**) _corr (REVISE):** the equality `MK·MV=NL·NW` is equivalent to
     > `sin a·sin(γ−a)·sin u·sin(γ−u)/sin²γ = sin b·sin(b+β)·sin w·sin(w+β)/sin²β`
     (RHS uses `sin(b+β)`, NOT `sin(b−β)`). Verified ~1e-13 across 11 configs. Necessity+sufficiency: dropping α makes both (**) _corr and OM=ON fail in lockstep (alpha explorer Finding 3).
  5. **α arc-sum (the entry point — proved mechanism):** directed external-angle theorem on Γ, **SUM** form `∡(secant₁,secant₂)=½[arc(far₁→far₂)+arc(near₁→near₂)]` (mod π) — KB `circle/triangle configuration facts`. Corollary (the α-condition on Γ):
     > `2α = arc(RA)+arc(KP) = arc(AS)+arc(QL)` (mod 2π)
     with R=2nd∩(BK,Γ), S=2nd∩(CL,Γ). Equivalently `arc(RA)=2(α+u)`, `arc(AS)=2(α−w)`. — `directed external angle, SUM form` + `α arc-sum` lemmas (round-2 explorer, to certify).
  6. **Midpoint projective link (the bridge — GAP):** with M midpoint of AB, the pencil at K projectively maps line AP to Γ, sending `(A,P;B,M) ↦ (A,P;R,V)`; hence the cross-ratio `(A,P;R,V)=(A,P;B,M)` (M midpoint fixes this cross-ratio). Symmetrically `(A,Q;S,W)=(A,Q;C,N)`. — KB `Geometry — synthetic toolkit, projective ideas / cross-ratio`. This eliminates R in favour of V (and S in favour of W), feeding the α arc-sum into the (**) _corr variables.
  7. **Ptolemy on cyclic quads (the algebraic closer — GAP):** Ptolemy on (A,V,P,K): `AV·PK + VP·KA = AP·KV`; and on (A,W,Q,L): `AW·QL + WQ·LA = AQ·LW`. Combined with `sin(½arc(XY))=|XY|/(2R)` and the α arc-sum (Step 5), the cross-ratio links (Step 6) eliminate R,S and yield the corrected (**)_corr. — KB `circle/triangle configuration facts, Ptolemy`.
  8. Conclude `MK·MV=NL·NW ⟹ OM=ON`. ∎
**Key lemmas (claim + mechanism):**
  - `∠CAW=−(b+β)` (CORRECTED) — because W=2nd∩(NL,Γ) and `∠CAW` is the inscribed angle at A subtending QW, with `2β=arc(AW)+arc(QL)` (SUM form, intersecting-chords interior angle at N); the directed sign is `−b−β`, not `b−β` (the round-1 trap was numpy's acute-angle pick).
  - `2α=arc(RA)+arc(KP)=arc(AS)+arc(QL)` (SUM form) — because the directed external angle at B (resp. C) is the average of the two intercepted arcs (far+near), NOT the difference; verified as the ONLY arc combination reproducing `∡(BA,BK)=−α`.
  - `(A,P;R,V)=(A,P;B,M)` — because M is the midpoint of AB (so `(A,P;B,M)` is fixed) and the pencil at K sends line AP to Γ (so cross-ratios are preserved).
  - Ptolemy absorbs the arc-form LHS/RHS of (**)_corr once R,S are eliminated — because `sin(½arc(XY))=|XY|/(2R)` and Ptolemy is the natural identity for products of chord lengths on a cyclic quad.
**Open gaps:** Step 6 (the pencil cross-ratio link — stated but unproven; needs the projectivity argument); Step 7 (the Ptolemy+arc-sum+cross-ratio algebraic derivation of (**)_corr — the genuinely hard combination, named but not derived).
**Cases to cover:** none (directed angles mod π throughout; inside hypotheses select branches).
**Watch out for:**
  - Do NOT use the DIFFERENCE-form `2α=arc(KP)−arc(AR)` (round-1, WRONG); the SUM form is correct.
  - Do NOT use `sin(b−β)` (round-1, FALSE); the corrected crux is `sin(b+β)`.
  - The bridge (Steps 6–7) is genuinely hard — the α arc-sum involves R,S which do NOT appear in (**)_corr (which involves only A,K,P,V / A,L,Q,W); the cross-ratio link is the necessary elimination. If the bridge stalls, this approach stays partial; the analytic route is the fallback.
**Gap to close this round:** fix the sign (Step 3' (iv)) + attempt the bridge (Steps 6–7): cross-ratio link + Ptolemy derivation of (**)_corr.

---

### antipode-rightangle
**Action:** advance
**Target:** Prove OM = ON via the homothety+antipode reduction `OM=ON ⟺ A'∈pbis(BC)` (where `A'=2O−A`) and the trigonometric-Ceva identity (T) in `△BKL`.
**Technique:** Homothety + Thales (angle in semicircle) + **trigonometric Ceva** (KB `Geometry — synthetic toolkit, trig cevians`) + the α arc-sum mechanism (SUM form, since (T) ⟺ (**)_corr ⟺ OM=ON — all equivalent).
**Skeleton (unchanged down to the gap; the closing attempt now uses the round-2 α arc-sum):**
  1. **Reduction (proved):** `OM=ON ⟺ A'B=A'C ⟺ A'∈pbis(BC)` (homothety by 2 about A sends M↦B, N↦C; `A'=2O−A`). — `antipode reduction` lemma (round-1, proved).
  2. **Thales characterisation (proved):** `A'=(line through K ⊥ AK)∩(line through L ⊥ AL)=ℓ_K∩ℓ_L`. — `Thales characterisation` lemma (round-1, proved).
  3. **Direction table (proved):** `dir(BK)=−α, dir(BL)=−α−β, dir(CL)=A+α, dir(CK)=A+α+γ, dir(MK)=γ, dir(LN)=A−β` (mod π, ref AB=0). — `direction table` lemma (round-1, proved).
  4. **Metric constraints (proved):** the incidence content beyond the direction table is `(C1),(C2)` (sine-rule equations from `△BKC`, `△BLC`); `α` free, `(C1)` gives `γ=γ(α)`, `(C2)` gives `β=β(α)`. — `metric constraints` lemma (round-1, proved).
  5. **Trig-Ceva reformulation (proved):** `OM=ON ⟺` identity (T) `cos C·cos∠AKL·cos∠BLA = cos(C+β)·cos∠BKA·cos∠ALK` (directed line-angles mod π). — `trig-Ceva reformulation` lemma (round-1, proved).
  6. **Sine-rule relation (proved):** `sin∠ALK·sin∠BKA·sin(α+β) = sin∠AKL·sin∠BLA·sin α` (R1), from the sine rule in `△ABK, △ABL, △AKL`. — round-1, proved.
  7. **Closing (T) from (R1)+(C1)+(C2) (GAP — builder attempts):** the α arc-sum mechanism (round-2: `2α=arc(RA)+arc(KP)=arc(AS)+arc(QL)`, SUM form) applies to identity (T) too, since (T) ⟺ (**)_corr ⟺ OM=ON (all equivalent). Two candidate routes the builder should try in parallel:
     (a) **CAS-assisted derivation:** substitute the explicit `(C1),(C2)` sine-rule equations + (R1) + the `△BKL` angle sum into (T) and verify the trig identity cancels (sympy `trigsimp` on the substituted LHS−RHS). Round-1's sympy attempt did not terminate; try again with the explicit `(C)` equations and the `α,β,γ,A,B,C` angle variables (not the coordinate variables).
     (b) **Synthetic via α arc-sum:** (T) is a trig-Ceva concurrency; the α arc-sum + Ptolemy on the cyclic quads (A,V,P,K), (A,W,Q,L) (the SAME mechanism as `power-secant-product` Step 7) should close it, since (T)⟺(**)_corr. The builder may import the cross-ratio link `(A,P;R,V)=(A,P;B,M)` from `power-secant-product` once certified.
  8. Conclude (T) ⟹ `A'∈pbis(BC)` ⟹ `OM=ON`. ∎
**Key lemmas (claim + mechanism):**
  - `A'=ℓ_K∩ℓ_L` with `ℓ_K⊥AK, ℓ_L⊥AL` — because `AA'` is a diameter of `(AKL)`, so `∠AKA'=∠ALA'=90°` (Thales).
  - `A'∈m_B ⟺ (T)` — because `ℓ_K,ℓ_L,m_B` are cevians of `△BKL` and trig Ceva gives the concurrency condition as (T).
  - (T) ⟺ (**)_corr — because both are ⟺ `OM=ON` (the antipode reduction and the power-secant reduction are both equivalences with `OM=ON`); so closing one closes the other.
**Open gaps:** Step 7 — derive (T) from (R1)+(C1)+(C2), via the α arc-sum + Ptolemy OR a CAS trig cancellation.
**Cases to cover:** none (directed angles mod π; inside hypotheses select branches).
**Watch out for:**
  - (T) and (**)_corr are EQUIVALENT — a builder closing one closes both `antipode-rightangle` and `power-secant-product`. If the cross-ratio link is certified in `power-secant-product`, import it here rather than re-deriving.
  - The sympy termination issue (round-1): use the angle variables `α,β,γ,A,B,C` with (C1),(C2) as the constraint system, not the coordinate variables; reduce mod the angle-sum `A+B+C=π`.
**Gap to close this round:** Step 7 — derive (T) from (R1)+(C1)+(C2), via the α arc-sum mechanism or a CAS trig cancellation.

---

### (Considered and rejected this round)

- **inversion-apollonius (new) — NOT opened.** The inversion lens confirmed `OM=ON ⟺ P∈A-Apollonius circle of △AB'C'` (inverted antipode reduction), but its own honest verdict: "same crux, inverted variables; rival framing, not a bypass." The closing step is a sine-product identity `sin∠PC'B'·sin∠AB'C' = sin∠PB'C'·sin∠AC'B'` — the same α-crux in inverted dress, with NO cleaner closing lemma found (4-point concyclities all fail; rotation-composition rejected). Per the rules, do NOT open a sibling that hits the same wall. The Apollonius-circle target and the inverted circumcentre-image lemma are recorded in the explorer report for future reference.
- **A 5th genuinely-new framing (new) — NOT opened.** No confirmed-viable genuinely-new framing exists this round: rotation-composition REJECTED numerically (8 compositions, all fail); spiral-sim at the Miquel point of BK,CL REJECTED (sends B→C, K→L but NOT M→N); inversion is the antipode route conjugated. Per the round-1 per-role rule "hold the most speculative framing out of the build set until an explorer confirms its load-bearing conjecture numerically," no 5th slug is opened. IF the synthetic approaches stall again on the α-condition this round (the shared-gap plateau condition), next round's outliner should open ≥1 genuinely different framing (candidates: a direct-coordinate trigonometric-identity proof on the `(C1),(C2)` system; a Möbius/cross-ratio-only proof on Γ; a pure-projective proof exploiting the midpoint pencil structure as the spine rather than a bridge).

---

**Field handed to the outline-reviewer (4 approaches):**
- `analytic-branch-cert` — advance (leading solve candidate; builder re-verifies saturation from scratch with corrected `Q=320/3`, explicit `G`, et2 proof, degenerate exclusion; treat round-1 false-verified as caution).
- `analytic-resultant-cert` — new (rival analytic closing via resultant-in-`t` factorisation `res_t(e3,Q)` divisible by `D₀²` + root selection; insurance against saturation being false again).
- `power-secant-product` — revise (fix sign `∠CAW=−(b+β)`, restate corrected crux `sin(b+β)`, attempt α arc-sum + cross-ratio + Ptolemy bridge).
- `antipode-rightangle` — advance (close (T) via α arc-sum mechanism or CAS trig cancellation; note (T)⟺(**)_corr so power's closing transfers).

**Build set (suggested):** `analytic-branch-cert`, `analytic-resultant-cert`, `power-secant-product`, `antipode-rightangle`. (The two analytic approaches share the reduction machinery but have DIFFERENT closing certificates — saturation vs resultant — so they are rival closings, not a single-gap trap; both are worth building in parallel as insurance. The two synthetic approaches share the α-crux but have different framings — antipode vs power-secant — and their closings are equivalent ((T)⟺(**)_corr); a builder should attempt both since a closing of one transfers.)
