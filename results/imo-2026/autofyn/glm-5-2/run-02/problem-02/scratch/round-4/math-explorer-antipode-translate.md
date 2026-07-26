## imo-2026-02 — lens: TRANSLATION (scout how antipode's (C1),(C2) translate into the power/secant variable system)

Context recap. The problem is SOLVED (3 certificates). This round pursues an OPTIONAL fourth, fully-synthetic certificate by closing `power-secant-product`'s Step 9. The round-3 diagnosis (reviewer-confirmed counterexample `crux = −0.0366`) proved `(**)_corr ∉ ideal⟨(B),(C),angle-sum⟩`: (B),(C) are Γ-local (B-side `(a,u,α,γ)`, C-side `(b,w,α,β)`, share `α` only) and do NOT couple K and L. The 7 angle vars `(a,b,u,w,α,β,γ)` need 4 relations for the 3-DOF config; (B),(C) give 2, the △AKL angle-sum is definitional (defines `A = π−a−b+u−w`, imposes no constraint on the 7), so **2 K–L coupling relations are missing**.

Variable dictionaries (so the translation is unambiguous).
- Antipode variables: `(A,B,C,α,β,γ)` with `A,B,C` the TRIANGLE angles of `△ABC` (`A+B+C=π`), `α=∠KBA=∠ACL`, `β=∠LBK=∠LNC`, `γ=∠LCK=∠BMK`.
- Power variables: `(a,b,u,w,α,β,γ)` with `a=∠ALK`, `b=∠AKL` (inscribed angles of `Γ=(AKL)` at L, K), `u=∠BAK=∡(AB,AK)`, `w=∠CAL=∡(AC,AL)`. `α,β,γ` are SHARED (same three given angle equalities).

### 1. Antipode's (C1) and (C2), quoted exactly

From `approaches/antipode-rightangle.md` §4 (CORRECTED round-2 interior-angle form):
> **(C1):** `2 sin A · sin(C−α−γ) · sin(α+γ) = sin C · sin γ · sin(A+2α+γ)`
> **(C2):** `2 sin A · sin(B−α−β) · sin(α+β) = sin B · sin β · sin(A+2α+β)`
with `(C1)` encoding the incidence `∠LCK = γ` (K lies on the `γ`-ray from C; sine rule in `△BKC` with interior angles `∠KBC=B−α`, `∠BCK=C−α−γ`, `∠BKC=A+2α+γ`, combined with the position formula `BK=(AB/2)·sin γ/sin(α+γ)` and `BC=AB·sin A/sin C`), and `(C2)` encoding `∠LBK = β` (L lies on the `β`-ray from B; sine rule in `△BLC` with `∠LBC=B−α−β`, `∠BCL=C−α`, `∠BLC=A+2α+β`, combined with `CL=(AC/2)·sin β/sin(α+β)`).

### 2. Geometric facts encoded (the K–L coupling)

- **(C1)** says: the `K` determined purely from the B-side (via `(K-pos)`, i.e. `∠KBA=α` and `∠BMK=γ`) ALSO lies on the ray from `C` making the `γ`-angle with `CL`. I.e. the C-side computation of `∠LCK` (the angle at C between the secants `CL` and `CK`) must equal the B-side value `γ`. This is the K–L incidence through vertex C.
- **(C2)** says: the `L` determined purely from the C-side (via `(L-pos)`, i.e. `∠ACL=α` and `∠LNC=β`) ALSO lies on the ray from `B` making the `β`-angle with `BK`. I.e. the B-side computation of `∠LBK` must equal the C-side value `β`. This is the K–L incidence through vertex B.

So both are **exterior-angle equalities on `Γ`** (angles at the exterior points B, C between two secants to `Γ`), each equated to a value (`β`, `γ`) that was DEFINED on the opposite side. That is exactly the K–L coupling that (B),(C) lack.

### 3. Rewriting each as a relation in POWER/SECANT variables

The translation is **not** a literal variable substitution. The obstruction: antipode's (C1),(C2) are written in the TRIANGLE angles `A,B,C`, but the power variables give only `A = π−a−b+u−w` and `B+C = a+b−u+w` — they do NOT determine `B` and `C` individually (the triangle shape `(A,B)` is 2 of the 3 configuration DOF; the power vars `(a,b,u,w)` carry `A` plus 2 further DOF, not `B,C` separately). So one cannot just substitute `B,C` into (C1),(C2). Instead the analogues are derived DIRECTLY in the power framing via **(i) the secant involution on `Γ`** and **(ii) the SUM-form directed exterior-angle theorem** (power file Step 5, KB `angle chasing`). The geometric content is the SAME incidence as antipode's (C1),(C2) (verified numerically below), but the algebraic form is the secant/exterior-angle form, not the `△BKC`/`△BLC` sine-rule form.

Introduce the auxiliary points (all on `Γ`, all ELIMINABLE):
- `T := 2nd∩(BL, Γ)` (the second intersection of line `BL` with `Γ`),
- `U := 2nd∩(CK, Γ)` (the second intersection of line `CK` with `Γ`).

These are NOT new degrees of freedom: `T` is the image of `L` under the **secant involution on `Γ` induced by the exterior point `B`** (the involution swapping `A↔P`, `K↔R` — the two known B-side pairs on `Γ`); `U` is the image of `K` under the **involution induced by `C`** (swapping `A↔Q`, `L↔S`). A projective involution on a conic is determined by two pairs, so `T` is a Möbius (fractional-linear) function of the half-angle-tangent `t_L` with coefficients determined by `(A,P),(K,R)` — hence purely B-side + `L`-position, and **eliminable** by substitution of that Möbius formula.

#### (C2)' — the power-variable analogue of (C2): `∠LBK = β`

Two secants from `B` to `Γ`: line `BL` (meets `Γ` at `T` near, `L` far) and line `BK` (meets `Γ` at `K` near, `R` far). By the SUM-form directed exterior-angle theorem (power file Step 5):
> **(C2)'** `½[arc(L, R) + arc(T, K)] = β   (mod π)`,
where the arcs are directed CCW on `Γ`. The LHS involves: `arc(L,R)` (R is B-side from `arc(R,A)=2(α+u)` Step 6; L is C-side), `arc(T,K)` (K is B-side; T is the Möbius image of L under the B-involution). Substituting the involution formula for `T` and the half-arc data `arc(R,A)=2(α+u)`, `arc(A,K)=2a`, `arc(A,P)=2(a−u)` etc., this becomes a trig-polynomial relation on `(a,b,u,w,α,β)` — a genuine K–L coupling (the only purely-B-side input is `(a,u,α)`; the L-position `(b,w)` enters through `L` itself and through `T`'s dependence on `L`).

#### (C1)' — the power-variable analogue of (C1): `∠LCK = γ`

Two secants from `C` to `Γ`: line `CL` (meets `Γ` at `L` near, `S` far) and line `CK` (meets `Γ` at `U` near, `K` far). SUM-form:
> **(C1)'** `½[arc(S, K) + arc(L, U)] = γ   (mod π)`,
with `U` the Möbius image of `K` under the C-involution (pairs `(A,Q)`, `(L,S)`, where `arc(A,S)=2(α−w)` Step 6, `arc(A,Q)=2(b−w)`). Substituting gives a trig-polynomial relation on `(a,b,u,w,α,γ)` — again a genuine K–L coupling.

#### Numerical verification (verified config `A=(0,0),B=(4,0),C=(1,3),K=(2.8,0.49465),L=(1.0479,2.3099)`, angles `a=68.386°, b=−56.033°, u=10.019°, w=−5.965°, α=22.402°, β=15.640°, γ=31.729°`)

- **(C2)'**: `½[arc(L,R)+arc(T,K)] = 15.6399°` vs `β = 15.640°` ✓ (residual ~1e-4° from angle rounding).
- **(C1)'**: `½[arc(S,K)+arc(L,U)] = 31.7253°` vs `γ = 31.729°` ✓ (residual ~4e-3°, angle-rounding).
- **Involution check**: the Möbius involution `t' = (p·t+q)/(r·t+1)` on the half-angle-tangent `t=tan(θ/2)` fitted to the two B-side pairs `(t_A,t_P),(t_K,t_R)` predicts `t_T` (and hence `θ_T`) matching the actual second-intersection `T` to 4 decimals; least-squares residual machine-zero. So `T` IS a Möbius function of `t_L` with B-side-determined coefficients — eliminable by substitution. (Same holds for `U` via the C-involution.)

### 4. Does the translation close `(**)_corr ∈ ideal⟨(B),(C),angle-sum,(C1)',(C2)'⟩`?

**Plausibly YES, with a caveat on the algebraic form.** Counting DOF: the 7 angle vars `(a,b,u,w,α,β,γ)` need 4 relations for the 3-DOF config. The set `{(B), (C), (C1)', (C2)'}` supplies exactly 4:
- (B): Γ-local on `(a,u,α,γ)`,
- (C): Γ-local on `(b,w,α,β)`,
- (C2)' = `∠LBK = β`: couples the B-side `(a,u,α)` to the C-side `(b,w,α,β)` (through `T`'s dependence on `L`),
- (C1)' = `∠LCK = γ`: couples the C-side `(b,w,α)` to the B-side `(a,u,α,γ)` (through `U`'s dependence on `K`).

This is the right SHAPE of closure: the two new relations do couple K and L, which is exactly what the round-3 counterexample proved was missing. `(**)_corr` (= `Pow(M)=Pow(N)` in sine-product form, coupling `(a,γ,u)` to `(b,β,w)`) should lie in the ideal once the couplings (C1)',(C2)' are added, **provided** the four relations are independent and the Möbius-elimination of `T,U` is carried through to pure trig-polynomial form. The angle-sum is definitional (defines `A`); it need not be added as a separate generator — its content (the link between `A` and `(a,b,u,w)`) is already encoded in the arc data (`arc(AK)=2a`, `arc(AL)=2b`, hence `∠KAL = π−a−b` as an inscribed angle, equivalent to `A = π−a−b+u−w` once `u,w` fix the `AB,AC` directions). So the target ideal is effectively `⟨(B), (C), (C1)', (C2)'⟩`.

**Caveat (algebraic, not geometric).** Whether `(**)_corr` is in the ideal as a trig-POLYNOMIAL depends on the elimination of `T,U` producing *polynomial* (not just rational) relations. The Möbius formula for `T` is rational in `t_L`; clearing the (generically-nonzero) denominator yields a polynomial relation. The exterior-angle relation `½[arc(L,R)+arc(T,K)]=β` becomes, after half-angle-tangent substitution and the Möbius substitution, a trig-POLYNOMIAL in `(a,b,u,w,α,β)`. So the algebraic form is achievable, but the outliner/builder must (a) carry the Möbius substitution for `T,U` explicitly, and (b) re-run the sympy cancellation of `(**)_corr` mod `⟨(B),(C),(C1)',(C2)'⟩` (using the round-3 frac_field-atoms + half-angle-only-on-constrained-variables technique, lemma `sequential-division-ideal-membership`). I have NOT run that symbolic check (it is the outliner/builder's job, not the scout's); the DOF count and numerical verification of (C1)',(C2)' are the evidence that it should close.

### 5. Obstructions / flags

1. **No literal substitution.** The triangle angles `B,C` are NOT individually recoverable from `(a,b,u,w)` (only `A` and `B+C` are). So the antipode (C1),(C2) cannot be translated by writing `B = f(a,b,u,w)`, `C = g(a,b,u,w)` and substituting — that path is blocked. The translation MUST go via the secant involution + SUM-form exterior-angle theorem (the route in §3 above). This is the load-bearing finding for the outliner: do NOT attempt `B,C`-substitution; derive the analogues directly as `∠LCK=γ`, `∠LBK=β` via exterior angles on `Γ`.
2. **Auxiliary points `T = 2nd∩(BL,Γ)`, `U = 2nd∩(CK,Γ)`** are introduced and must be eliminated. They are eliminable (Möbius functions of `t_L`, `t_K` resp., with B-side / C-side coefficients), but the elimination adds algebraic bulk. The Möbius coefficients come from solving the 2-pair involution (`(A,P),(K,R)` for B; `(A,Q),(L,S)` for C); these pairs are themselves determined by the Step-6 arc data (`arc(R,A)=2(α+u)`, `arc(A,S)=2(α−w)`, plus `arc(A,P)=2(a−u)`, `arc(A,Q)=2(b−w)`).
3. **Directed-sign subtlety (inherited)**. The SUM-form exterior-angle theorem carries directed-mod-`π` signs (the round-2 sign-trap, rule in run_state). My numerical check used directed arcs CCW and matched `β,γ` to ~1e-3° (rounding), but the sign of `arc(T,K)` and `arc(L,U)` (short-way vs long-way) must be pinned by directed-separation (lemma `directed-separation-sign-pinning`) on the inside-hypothesis branch, exactly as Step 9a pinned (B),(C). The C-side analogue will again carry one extra overall sign flip (as (C) did vs (B)) — expect `∠LCK` and `∠LBK` to have opposite cross-ratio signs, mirroring the (B)−/(C)+ asymmetry.
4. **Independence of (C1)',(C2)' from (B),(C)**. The four relations should be independent (they cut different variable-tuples), but the outliner/builder should verify independence before trusting the 4-relations→3-DOF count (a hidden dependence would leave 4 DOF and `(**)_corr` would still escape). The round-3 counterexample technique (perturb a free angle, re-solve the constrained ones, check the crux) is the right probe to re-run AFTER adding (C1)',(C2)' — it should now fail to find a counterexample.
5. **A third relation?** I do NOT think a third coupling relation is needed: 4 relations on 7 vars gives the right 3 DOF, and the two exterior-angle equalities `∠LBK=β`, `∠LCK=γ` are precisely the two remaining angle conditions not yet encoded in Γ-local form. But if the symbolic cancellation still returns nonzero after adding (C1)',(C2)' (with T,U eliminated), the next suspect is a SIGNED branch mismatch between the (C1)',(C2)' exterior-angle signs and the (B),(C) signs — NOT a missing third relation. Re-pin all four signs by directed-separation on one representative before adding a third relation.

### Report-style summary

- **Distinct openings:**
  1. **Secant-involution + SUM-form exterior angle** (the route above): derive `∠LBK=β` and `∠LCK=γ` as `½[arc(L,R)+arc(T,K)]` and `½[arc(S,K)+arc(L,U)]`, with `T,U` Möbius-eliminable via the B- and C-secant involutions on `Γ`. The principled, geometrically-faithful translation.
  2. **Re-derive antipode's (C1),(C2) in power vars via the chord lengths** (alternative, messier): express `BK,CL,BC,AB,AC` through the chord/secant-power structure of `Γ` (e.g. `BK = Pow(B)/BR`, etc.), substitute into the sine-rule forms of (C1),(C2). Algebraically heavier; same incidence content.
  3. **Bypass the translation entirely**: re-derive the 2 coupling relations as `Pow(B)=Pow(B)` and `Pow(C)=Pow(C)` written across the two sides (B's power via `BA·BP` AND via `BK·BR` already gives (B)-local; the CROSS-side version `Pow(B)` expressed using an L-side chord would couple). Less canonical than opening 1; flag as a fallback.
- **Candidate technique(s):** secant involution on a conic (projective, Möbius on `t=tan(θ/2)`); SUM-form directed exterior-angle theorem (power file Step 5, already proved); directed-separation sign-pinning (lemma `directed-separation-sign-pinning`); sympy ideal-membership via sequential univariate field-division over `QQ.frac_field` atoms (lemma `sequential-division-ideal-membership`).
- **Cheap-kill candidates:** none — the gap is structural (missing coupling relations), not a parity/bound issue; the work is deriving and algebraically eliminating `T,U`.
- **Knowledge-base entries to use:** `power of a point` (secant form — the (B),(C) base); `angle chasing` (directed inscribed + exterior angle, SUM form); `projective ideas / cross-ratio` (the secant involution IS a projective involution on `Γ`; perspectivity preserves cross-ratio — already used in Step 7); `trig cevians` (only if opening 2 is taken, for the sine-rule-in-`△BKC` route). The SUM-form exterior-angle theorem and the midpoint cross-ratio link are already certified lemmas in `results/imo-2026-02/lemmas/`.
- **Analogous past problems (cruxes):** none retrieved — the crux here is internal (translate one framing's incidence constraints into another framing's variables via a conic involution), not a known olympiad crux move. The closest transferable technique is the antipode approach's own §4 (sine-rule incidence in `△BKC,△BLC`) and §8 (sequential field-division) — both already in-repo.
- **Prior progress:** power file Steps 1–8 rigorous; Step 9a (sign-pinning of (B),(C)) CLOSED; Step 9b returns NONZERO with the counterexample reproduced by the reviewer. The current best is the diagnosis itself: 2 K–L incidence relations are missing. This scout has DERIVED the two relations in geometric form ((C1)',(C2)' above) and verified them numerically — they were previously identified only as "analogues of antipode's (C1),(C2)" without a concrete power-variable form.
- **Dead ends (do not retry):**
  - Symbolic cancellation of `(**)_corr` mod `⟨(B),(C),angle-sum⟩` ALONE — counterexample-confirmed nonzero (round 3). Do not re-run without adding (C1)',(C2)'.
  - Literal substitution of `B,C` into antipode's (C1),(C2) — blocked (B,C not individually recoverable from power vars). Do not attempt.
  - Force-closing Step 9b (per outline-reviewer's deferral rule) — never.
- **Small-case / intuition notes (CONJECTURE, not proved):** the numerical matches `(C2)' → 15.6399° ≈ β` and `(C1)' → 31.7253° ≈ γ` to angle-rounding precision, plus the machine-zero Möbius-involution residual, suggest that (C1)',(C2)' ARE the correct power-variable incidence relations and that, once `T,U` are eliminated and signs pinned by directed-separation, the symbolic cancellation of `(**)_corr` mod `⟨(B),(C),(C1)',(C2)'⟩` will return zero — yielding the fourth, fully-synthetic (cross-ratio + secant-power) certificate. This is a CONJECTURE based on DOF-counting + numerical evidence; the symbolic check itself is the outliner/builder's job.
