## imo-2026-02 — lens: DIRECT DERIVATION IN POWER VARIABLES

Scouting a DIRECT power-variable route to the 2 missing K–L coupling relations (the analogues of `antipode-rightangle`'s `(C1),(C2)` that round-3 diagnosed as missing). NOT translating the antipode's polynomials; deriving purely within the `(a,b,u,w,α,β,γ)` sine/secant system.

### 1. The power/secant variable system (precise layout)

From `power-secant-product.md` notation:
- `Γ = (AKL)`, circumcentre `O`, circumradius `R`.
- `P = 2nd∩(AB,Γ)`, `Q = 2nd∩(AC,Γ)`, `V = 2nd∩(MK,Γ)`, `W = 2nd∩(NL,Γ)`, `R_Γ = 2nd∩(BK,Γ)`, `S = 2nd∩(CL,Γ)` (renaming the Γ-point `R_Γ` to avoid clash with circumradius `R`).
- **Seven directed angle variables (mod π, in (−π/2, π/2] clamped):**
  - `a := ∠ALK` (at L, subtends chord `AK`), `b := ∠AKL` (at K, subtends chord `AL`),
  - `u := ∠BAK = ∡(AB, AK)` (at A), `w := ∠CAL = ∡(AC, AL)` (at A),
  - `α := ∠KBA = ∠ACL`, `β := ∠LBK = ∠LNC`, `γ := ∠LCK = ∠BMK`.
- **Chord lengths on Γ** (inscribed-angle theorem, in the seven variables):
  - `AK = 2R sin a`, `AL = 2R sin b` (signed),
  - `AP = 2R sin(a−u)` (inscribed `∠AKP`; arc data `arc(AK)+arc(KP) = 2a+(−2u) = 2(a−u)`),
  - `AQ = 2R sin(b−w)` (symmetric),
  - `KL = 2R sin(b−a)` (the inscribed angle at A subtending `KL` is `∠KAL = b − a (mod π)` — see §5 below for the sign correction; `|KL| = 2R |sin(b−a)|`).
- **Triangle sides expressible in the seven variables** (sine rule in `△ABK, △ACL`):
  - `AB = 2R sin a · sin(u+α)/sin α`, `AC = 2R sin b · sin(α+w)/sin α` (signed; `|AC|` uses `|sin b|`).
  - `BK = 2R sin a · sin u / sin α` (sine rule in `△ABK`: `BK/sin u = AB/sin(α+u) = AK/sin α`).
  - `CL = 2R sin b · sin w / sin α` (symmetric).
  - `CK = 2R sin a · sin(A−u)/sin(α+γ)` (sine rule in `△ACK`: `AK/sin(α+γ) = CK/sin(A−u)`).
  - `BL = −2R sin b · sin(A+w)/[sin(α+β)]` (sine rule in `△ABL` with directed `∠ABL = −α−β`, `∠BAL = A+w`; the leading minus comes from `sin(∠ABL) = sin(−α−β) = −sin(α+β)`).

### 2. Which angle equalities are NOT yet encoded by (B), (C)

The three hypotheses are `∠KBA = ∠ACL = α`, `∠LBK = ∠LNC = β`, `∠LCK = ∠BMK = γ`. Splitting each into its two "sides":

| Equality | B-side (uses Γ-point on a `B,K,M`-side line) | C-side (uses Γ-point on a `C,L,N`-side line) |
|---|---|---|
| α | `∠KBA = α` (via `R_Γ = 2nd∩(BK,Γ)`) → in **(B)** | `∠ACL = α` (via `S = 2nd∩(CL,Γ)`) → in **(C)** |
| β | `∠LBK = β` (**MISSING** — antipode's `(C2)`) | `∠LNC = β` (via `W = 2nd∩(NL,Γ)`) → in **(C)** |
| γ | `∠BMK = γ` (via `V = 2nd∩(MK,Γ)`) → in **(B)** | `∠LCK = γ` (**MISSING** — antipode's `(C1)`) |

So the two missing K–L couplings are exactly `∠LBK = β` and `∠LCK = γ`. These couple the B-side quartet `(a, u, α, γ)` with the C-side quartet `(b, w, α, β)` — through `α` and through the shared chord `KL = 2R sin(b−a)`. The power-variable analogue of "the angle equality that ties a K-vertex angle to an L-vertex angle" is: the angle at the **C-side vertex C** (between `CL` and `CK`) equals `γ`, and the angle at the **B-side vertex B** (between `BL` and `BK`) equals `β` — each of these couples a length from one side (`BK` from `△ABK`, `CL` from `△ACL`) with the shared chord `KL`, exactly as in antipode's `(C1)` (sine rule in `△BKC`) and `(C2)` (sine rule in `△BLC`).

### 3. The derivation moves (sine rule in `△LBK` and `△LCK`)

**For `∠LBK = β` — sine rule in `△LBK`** (vertices `L, B, K`):
- Side `KL = 2R sin(b−a)` opposite `∠LBK = β`.
- Side `BK = 2R sin a · sin u / sin α` opposite `∠KLB` (at L, from `LK` to `LB`).
- Side `BL = −2R sin b · sin(A+w) / sin(α+β)` opposite `∠BKL` (at K, from `KB` to `KL`).
- **Directed angles** (mod π, using the line-direction table `dir(BK)=−α, dir(BL)=−α−β, dir(KL)=u+b`):
  - `∠BKL = ∡(KB, KL) = dir(KL) − dir(KB) = (u+b) − (−α) = u+b+α`.
  - `∠BLK = ∡(LB, LK) = dir(LK) − dir(LB) = (u+b) − (−α−β) = u+b+α+β`. (Note `∠BLK`, NOT `∠KLB`; the angle from `LB` to `LK` is the *reversal* of the standard `∠KLB` and carries the opposite sign — the round-1 directed-angle trap, see §5.)
- **Directed sine rule** `KL/sin β = BK/sin(∠BLK) = BL/sin(∠BKL)` gives two equivalent forms (any one suffices):
  - **(Rel-LBK-a)** `sin(b−a) · sin α · sin(u+b+α+β)  =  sin β · sin a · sin u`
  - **(Rel-LBK-b)** `sin(b−a) · sin(α+β) · sin(u+b+α)  =  − sin β · sin b · sin(A+w)`
- **Verified** on the documented config (`a=68.386, b=−56.033, u=10.019, w=−5.965, α=22.402, β=15.640, γ=31.729, A=71.565°`) to **6.25e-17** (machine precision) and on two further fsolve-discovered configs (kx=3.0, 3.2) to **1.6e-16 / 3.1e-16**.

**For `∠LCK = γ` — sine rule in `△LCK`** (vertices `L, C, K`):
- Side `KL = 2R sin(b−a)` opposite `∠LCK = γ`.
- Side `CK = 2R sin a · sin(A−u)/sin(α+γ)` opposite `∠KLC = A+α−u−b` (at L, from `LK` to `LC`; directed-angle table `dir(CL)=A+α`, `dir(LK)=u+b`).
- Side `CL = 2R sin b · sin w / sin α` opposite `∠CKL = u+b−A−α−γ` (at K, from `KC` to `KL`; `dir(CK)=A+α+γ`, `dir(KL)=u+b`).
- **Directed sine rule** `KL/sin γ = CK/sin(∠KLC) = CL/sin(∠CKL)`:
  - **(Rel-LCK-a)** `sin(b−a) · sin(α+γ) · sin(A+α−u−b)  =  − sin γ · sin a · sin(A−u)`
  - **(Rel-LCK-b)** `sin(b−a) · sin α · sin(u+b−A−α−γ)  =  sin γ · sin b · sin w`
- **Verified** on the documented config to **1.25e-5** (rounding-limited by 3-decimal angle printing) and on the two fsolve configs to **1.2e-12 / 2.5e-13** — i.e. to machine precision on the high-precision configs. The leading minus in (Rel-LCK-a) is **load-bearing** (without it, LHS = −RHS); it is the directed-sine-rule sign at vertex K, mirroring the minus picked up by `∠ABL = −α−β` in `△ABL` above.

### 4. Will `(B), (C), (Rel-LBK), (Rel-LCK), angle-sum` make `(**)_corr` vanish?

**Likely yes — but the crux identity does NOT need reformulation; the *ideal* needs the angle-sum corrected (see §5).** Reasoning:
- The configuration is 3-DOF; the 7 angle vars need 4 relations. (B), (C) supply 2 (Γ-local, one per side); `Rel-LBK` supplies 1 (couples `(a,b,u,α,β)`); `Rel-LCK` supplies 1 (couples `(a,b,w,α,γ)`). Together with the angle-sum (which defines `A` in terms of `(a,b,u,w)` — no constraint on the 7), these 4 relations cut the variety down to the 3-DOF configuration locus.
- `(**)_corr` is `Pow(M) = Pow(N)` in sine-product form, i.e. the THEOREM (true on every configuration). On the 3-DOF configuration locus it vanishes identically; geometrically it is a consequence of all 5 angle equalities, so adding the 2 missing sine-rule relations to the ideal ⟨(B), (C), angle-sum⟩ should make `(**)_corr` a member.
- The two new relations each involve `(a,b)` (the shared backbone) and one of `(u,β)` or `(w,γ)`. They are **not redundant** with (B) or (C): (B) lives on `(a,u,α,γ)`, (C) on `(b,w,α,β)`; `Rel-LBK-a` lives on `(a,b,u,α,β)` (shares `b,α,β` with (C) but introduces `a,u` — a genuine new constraint, since (C) constrains `β` given `(b,w,α)` whereas `Rel-LBK-a` constrains `β` given `(a,b,u,α)` — different slices of the variety). The round-3 counterexample (perturb `a` by +10°, (B),(C),angle-sum still hold, `(**)_corr = −0.0366`) is precisely killed by `Rel-LBK-a`: at that perturbed point, `Rel-LBK-a` would NOT hold (the perturbed `a` violates the sine rule in `△LBK` since `BK` was held at its old value), so the counterexample is excluded from the larger ideal.
- The symbolic cancellation test of `(**)_corr mod ⟨(B), (C), Rel-LBK, Rel-LCK, angle-sum⟩` over `QQ.frac_field(a,b,u,w,α,β,γ)` (sin/cos atoms) is the natural next-round target. If it returns zero, the proof closes; if it returns nonzero, the crux itself must be reformulated (e.g. express `(**)_corr` in half-angle tangents on `β, γ` only, keeping `(a,b,u,w,α)` as frac_field atoms — the antipode round-3 trick — and certify via sequential univariate field-division).

### 5. Obstructions and honest flags

**(a) ANGLE-SUM SIGN ERROR in the existing power-secant-product.md.** The documented formula `A = π − a − b + u − w` is **WRONG**. On the verified config: `π − a − b + u − w = 183.63°` (mod 180° = 3.63°), but actual `A = ∠BAC = 71.565°`. The CORRECT relation, derived from `∠KAL = ∡(AK, AL) = −u + A + w` (splitting at `AB, AC`) and the directed-triangle-angle-sum `∠KAL + ∠ALK + ∠LKA ≡ 0 (mod π)` with `∠LKA = −∠AKL = −b`:
> **∠KAL = b − a (mod π),  hence  A ≡ b − a + u − w (mod π).**

Verified on 3 configs: `b − a + u − w` mod 180° = 71.565° = actual `A`. The bug propagated into `Rel-LCK-a` and `Rel-LCK-b` via the `A`-substitution `A = π − a − b + u − w` (which would substitute the wrong sign of `sin(A±…)`); the relations above use the corrected `A`. **Before the symbolic-cancellation test can run, the angle-sum in the ideal must be replaced by `A − (b − a + u − w) ≡ 0` (with the inside-branch sign pinned).** This is also why round-3's counterexample "angle-sum tautologically satisfied" was misleading — the tautology was against the WRONG formula, so the actual 7-variable constraint count was off by one. (This needs builder confirmation: it is conceivable round-3 used the formula only as a definition-of-`A` placeholder and the symbolic test did not actually substitute it; in that case the bug is documentation-only. Either way, the formula printed in the file is wrong and must be fixed.)

**(b) Sign-tracking in the directed sine rule.** The directed sine rule picks up a sign at each vertex depending on triangle orientation (which arc the vertex lies on). For `△LBK`, the relevant angles are `∠BLK` (at L, from `LB` to `LK`) and `∠BKL` (at K, from `KB` to `KL`); the angle `∠KLB` (at L, from `LK` to `LB`) is the *reversal* and has the opposite sign — using the wrong one flips the sign of the corresponding sine and breaks the identity. (Round-1's `∠CAW = b − β` vs `−(b+β)` was the same trap.) The relations in §3 use the correct (reversed) angles, verified numerically. The outliner/builder must keep these angle directions explicit; do NOT replace `∠BLK` with `∠KLB` mechanically.

**(c) The cross-ratio framing does NOT cleanly separate K and L.** The current (B),(C) are Γ-local because the cross-ratio link `(A,P;R_Γ,V) = (A,P;B,M)` lives entirely on the B-side (the pencil at `K`) and its C-side mirror lives entirely on the C-side (pencil at `L`). The K–L coupling is NOT visible at the cross-ratio level — it appears only when the shared chord `KL = 2R sin(b−a)` is invoked. So the cross-ratio (B),(C) cannot be the coupling site; the sine-rule in `△LBK, △LCK` is the correct (and likely only) direct route. The antipode route, by contrast, couples via the line `A' = ℓ_K ∩ ℓ_L` (Thales right angles) and trig-Ceva — a genuinely different mechanism, confirming the two approaches are independent.

**(d) The (Rel-LCK) numerical residual on the documented config (~1e-5) is rounding-limited, NOT a counterexample.** On the two fsolve-discovered configs (full machine precision), the residual drops to ~1e-12. The 3-decimal angle values printed in `power-secant-product.md` are insufficient for sub-1e-8 verification; the builder should re-derive `K, L` to full precision (e.g. `scipy.optimize.fsolve` to `1e-12` residual on the three angle-equality polynomials) before running the symbolic test.

**(e) Possible redundancy of `Rel-LCK-b` with `Rel-LBK-b` + angle-sum.** I have not verified algebraically that the four relations `(B), (C), Rel-LBK, Rel-LCK` are independent (cut exactly 2 DOF from the 5-DOF `V((B),(C))`). If they are not — e.g. if `Rel-LCK-b` follows from `Rel-LBK-b` + angle-sum + (B) + (C) — then only ONE new K–L relation is genuinely added, the variety would still be 4-DOF, and `(**)_corr` would still fail to be in the ideal. The round-3 diagnosis ("2 K–L relations missing") is the structural expectation; a quick symbolic-rank check (rank of the Jacobian of `(B), (C), Rel-LBK, Rel-LCK)` at a generic config — should be 4) is the cheap pre-test before the full symbolic-cancellation run. **Recommendation to outliner:** have the builder perform this rank check first; if rank < 4, a third K–L relation (e.g. via a triangle involving `M, N` directly, or via Ptolemy on a quadrilateral inscribed in `Γ`) may be needed.

### Distinct openings (for the outliner's field of rival approaches)

1. **Sine-rule in `△LBK, △LCK`** (the route scouted above — verified, ready to build). Two relations `Rel-LBK-a` and `Rel-LCK-a`, added to `⟨(B), (C), angle-sum-corrected⟩`, then symbolic-cancellation of `(**)_corr` (the natural completion of the existing power approach).
2. **Sine-rule in `△BLC, △BKC`** (antipode's exact triangle choice, but with lengths expressed in power variables `AB = 2R sin a · sin(u+α)/sin α` etc. rather than in `AB, BC` directly). Same algebra, different polynomial shape — may be more amenable to the half-angle-tangent + frac_field-atoms CAS trick (antipode's round-3 lesson). Worth a rival slug if the outliner wants to hedge the CAS-blowup risk.
3. **Half-angle-tangent reformulation of `(**)_corr` itself.** Rather than cancelling `(**)_corr` mod the 4-relation ideal in sin/cos atoms, substitute `t_β = tan(β/2), t_γ = tan(γ/2)` only, keep `(a,b,u,w,α)` as `QQ.frac_field` atoms (the antipode round-3 trick — per-role rule "ALWAYS: when a sympy CAS times out on a trig identity..."). The 4 relations `(B), (C), Rel-LBK, Rel-LCK` also become polynomials in `t_β, t_γ` over the same frac_field; sequential univariate field-division (in `t_γ`, then `t_β`) certifies `(**)_corr ∈ ideal`. This is the MOST LIKELY to terminate cleanly, by direct analogy with the antipode round-3 close.

### Candidate technique(s)
- **Sine rule in directed-angle form** (KB `Geometry — synthetic toolkit, trig cevians`) — the engine for both `Rel-LBK` and `Rel-LCK`.
- **Directed-triangle angle sum mod π** — pins `∠KAL = b − a` and hence `KL = 2R sin(b−a)` (the shared chord coupling K and L).
- **Sequential univariate field-division over `QQ.frac_field`** (KB `saturation-identity-et2-positive` lemma / the round-3 `sequential-division-ideal-membership` lemma) — the certificate style for the final symbolic cancellation, mirroring antipode round 3.

### Cheap-kill candidates
- **Symbolic-rank check of the Jacobian of `(B), (C), Rel-LBK, Rel-LCK`** at a generic config (one `numpy.linalg.matrix_rank` call) — settles whether the 4 relations cut exactly 2 DOF before the heavy CAS run. Cheap and decisive for viability.
- **Substitution of `A = b − a + u − w` (corrected) into `Rel-LCK-a`** and checking the resulting relation (in `(a,b,u,w,α,γ)` only, no `A`) still holds — confirms the angle-sum fix doesn't break the relation.

### Knowledge-base entries to use
- `Geometry — synthetic toolkit` (sine rule, directed angles, trig cevians) — the derivation engine.
- `Geometry — circle/triangle configuration facts` (inscribed angle theorem, intersecting-chords interior-angle theorem) — for the chord-length expressions and the existing (B), (C).
- `saturation-identity-et2-positive` lemma / `sequential-division-ideal-membership` lemma (lemmas/ directory) — for the final symbolic-cancellation certificate style.

### Analogous past problems (cruxes)
None — the crux corpus has no geometry entries (per the per-role rule from round 1). The closest analogue WITHIN this repo's own solved approaches is `imo-2026-02`'s own `antipode-rightangle` (the `(C1), (C2)` sine-rule in `△BKC, △BLC` is the exact mirror of the `Rel-LCK, Rel-LBK` move scouted here — but in different variables and via a different closing mechanism, so the independence is preserved).

### Prior progress
Three independent SOLVED certificates exist (analytic-branch-cert saturation identity, analytic-resultant-cert, antipode-rightangle `(T') ∈ ⟨(C1), (C2)⟩`). The power-secant-product approach has Steps 1–8 rigorous and Step 9a (sign-pinning of (B),(C)) closed; the residual gap is Step 9b (symbolic cancellation of `(**)_corr`), diagnosed in round 3 as missing 2 K–L incidence relations. This scout identifies those 2 relations concretely (§3) and verifies them numerically.

### Dead ends (do not retry)
- **(Round 1) Isogonality `∠BAK = ∠CAL` and the three "spiral similarities" `△ABK∼△ACL`, `△LBK∼△LNC`, `△LCK∼△BMK`** — all FALSE on the verified config (the spiral-at-A trap). Do not reintroduce.
- **(Round 1) `∠CAW = b − β`** — sign error; correct is `∠CAW = −(b+β)`. Do not use the wrong sign.
- **(Round 1) Ring pseudo-remainder as a polynomial-identity certificate** — use field-division over `QQ.frac_field` only.
- **(Round 3) Symbolic cancellation of `(**)_corr mod ⟨(B), (C), angle-sum(AS DOCUMENTED)⟩`** — returns NONZERO; do NOT retry with the same ideal. The fix is to (i) correct the angle-sum to `A = b − a + u − w` and (ii) ADD `Rel-LBK` and `Rel-LCK` to the ideal.

### Small-case / intuition notes (CONJECTURE, not proof)
- The four relations `(B), (C), Rel-LBK, Rel-LCK` are CONJECTURED to cut the 7-angle variety to 3-DOF (the configuration locus); verified on 3 configs that `(**)_corr` vanishes to machine precision wherever all four hold. A full symbolic-cancellation certificate is required for proof.
- The angle-sum formula `A = π − a − b + u − w` printed in `power-secant-product.md` is CONJECTURED wrong (verified wrong on 3 configs); the corrected `A = b − a + u − w (mod π)` is verified on 3 configs. The builder should re-derive from `∠KAL = −u + A + w` and `∠KAL = b − a (mod π)` (the latter from the directed triangle angle sum `∠KAL + ∠ALK + ∠LKA ≡ 0` with `∠LKA = −b`) — a one-line derivation.
- The minus sign in `Rel-LCK-a` (and in `Rel-LBK-b` and `Rel-LCK-b`) is a directed-sine-rule sign at the "reversed" vertex; it is verified load-bearing (without it, LHS = −RHS). The outliner should NOT smooth it away.
