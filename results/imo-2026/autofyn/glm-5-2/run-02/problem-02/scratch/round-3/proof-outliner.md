## imo-2026-02

**Context.** Problem is SOLVED (round 2: `analytic-branch-cert` + `analytic-resultant-cert` both APPROVE; full proof in `results/imo-2026-02/current.md`). This round strengthens the solution with **independent synthetic rival certificates** that do NOT lean on the saturation-identity backbone the two analytic proofs share. Two synthetic approaches are alive and `partial`; each has one precisely-located gap. The antipode scout (`/tmp/round-3/math-explorer-antipode-tactic.md`) verified a clean closing certificate for `antipode-rightangle` (replicated above: 81.6s, remainder zero). The power scout did NOT find a clean directed-trig chase. The two `analytic-*` slugs are SOLVED — no revision needed; they stay as-is in the population.

---

### antipode-rightangle: revise (close the §7 gap)

Target: Prove `OM = ON` for the configuration of IMO 2026 P2, via the homothety+antipode+Thales route, with the closing identity (T) certified by an **independent symbolic ideal-membership certificate** that does NOT invoke the saturation identity of `analytic-branch-cert`. (The whole end-to-end claim; the antipode framing's own derivation of (T) is what closes here.)

Technique: **Sequential univariate polynomial field-division** over rational-function fields — the same certificate style that closed `analytic-branch-cert` Prop 4 over `Q(b,u,v,lx,t)[ly]`, applied here to the antipode's coordinate-crux `(T')`. Spine: `sp.Poly(expr, var, domain=sp.QQ.frac_field(...))` + `sp.div`, treating `t_A,t_B,t_α` as frac_field atoms (NEVER `expand_trig` — that was the round-2 blowup).

Skeleton:
1. *(Already rigorous, retain)* Reduction `OM=ON ⟺ A'B=A'C ⟺ A'∈pbis(BC)` — by homothety `h` ratio 1/2 about A sends `B→M, C→N`, and `A'=2O−A` is the antipode of A on `(AKL)`. (Approach §1.)
2. *(Already rigorous, retain)* Thales characterisation `A' = ℓ_K ∩ ℓ_L` with `ℓ_K ⊥ AK through K`, `ℓ_L ⊥ AL through L` — by angle-in-semicircle (`AA'` diameter). (Approach §2.)
3. *(Already rigorous, retain)* Direction table (DT) from the three bare angle equalities `α,β,γ` + midpoint structure `BM∥AB, CN∥AC`. (Approach §3.)
4. *(Already rigorous, retain)* Corrected incidence constraints `(C1): 2 sin A sin(C−α−γ) sin(α+γ)=sin C sin γ sin(A+2α+γ)` and `(C2): 2 sin A sin(B−α−β) sin(α+β)=sin B sin β sin(A+2α+β)` (INTERIOR angles; round-1 directed versions carried an overall minus — fixed round 2). (Approach §4.)
5. *(Already rigorous, retain)* Trig-Ceva reformulation: `A'∈pbis(BC) ⟺` identity `(T): cos C·cos∠AKL·cos∠BLA = cos(C+β)·cos∠BKA·cos∠ALK`. (Approach §5.)
6. *(Already rigorous, retain)* (R1) is a vacuous trig identity — removes (R1) from the dependency; the determinants of `k=dir(KL)` (hence of (T)) are (C1), (C2) + the coordinate relation. (Approach §6.)
7. *(Already rigorous, retain)* Coordinate reformulation `(T')`: under `A=(0,0), B=(1,0), C=(d cos A, d sin A)` with `d=sin B/sin C`, identity (T) is equivalent (after clearing `1/(|KL||AK||AL|)`) to the explicit trig-polynomial identity `(T'): cos C·(M−|AK|²)·Lfac = cos(C+β)·(cos α−par)·(|AL|²−M)` of Approach §7.
8. **(GAP TO CLOSE — the revise target)** Certify `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩` over `Q(t_A,t_B,t_α)[t_γ,t_β]` by **sequential univariate field-division** (scout-verified, 81.6s, remainder zero):
   - (a) Construct `(C1)_num, (C2)_num, (T')_num` by half-angle substitution `t_x = tan(x/2)` applied to `γ, β` ONLY, keeping `sin A, cos A, sin B, cos B, sin α, cos α` (equiv. `t_A,t_B,t_α`) as **unexpanded frac_field atoms** — NOT `expand_trig` (the round-2 blowup was a coefficient-expansion artifact: 35 monomials when atoms are kept vs. 10⁴–10⁵ under `expand_trig`).
   - (b) Step 1: `sp.div((T')_num, (C1)_num, t_γ, domain=QQ.frac_field(t_A,t_B,t_α,t_β))` → quotient `q1`, remainder `r1` (degree 3 in `t_γ`, NOT zero — that's expected; the two-step reduction is needed).
   - (c) Step 2: `sp.div(r1_expr, (C2)_num, t_β, domain=QQ.frac_field(t_A,t_B,t_α,t_γ))` → quotient `q2`, remainder `r2` **`is_zero = True`** (scout-verified; replicate `/tmp/probe_reduce.py`).
   - (d) **Leading-coefficient-nonzero check**: certify `(C1)_num`'s `t_γ`-leading coeff and `(C2)_num`'s `t_β`-leading coeff are generically nonzero rational functions — a one-point numerical evaluation suffices (a nonzero rational function vanishes only on a Zariski-closed proper subset; the 47 prior configs at ~5e-13 confirm genericity). Print the leading coeffs and one numeric eval.
   - (e) **Denominator-clearing for the polynomial-ring certificate**: the field-division yields `(T')_num = q1·(C1)_num + q2·(C2)_num` with `q1,q2` having rational-function coefficients; multiply through by the LCM of the coefficient denominators (mechanical, `sp.together`+`sp.fraction`) to obtain a polynomial identity `(T')_num·D = Q1·(C1)_num + Q2·(C2)_num` over `Z[t_A,t_B,t_α,t_γ,t_β]` with `Q1,Q2,D` polynomial. State this explicitly.
9. *(Conclusion)* `(T')=0` on `{(C1)=0,(C2)=0}` (the incidence variety selected by the inside hypotheses) ⇒ `(T)=0` (Step 7 equivalence, clearing factor `1/(|KL||AK||AL|) > 0` on the inside branch) ⇒ `A'∈pbis(BC)` (Step 5) ⇒ `OM=ON` (Step 1). ∎

Key lemmas (claim + the one-line mechanism that makes it true):
- **Sequential-division ideal-membership lemma.** *If `f ∈ F[t_γ,t_β]`, `g1 ∈ F[t_γ,t_β][t_γ]` has unit leading coeff in `t_γ` over `F = Q(t_A,t_B,t_α,t_β)`, and `g2` has unit leading coeff in `t_β` over `Q(t_A,t_B,t_α,t_γ)`, then sequential remainder `rem_{g2}(rem_{g1}(f)) = 0` ⇒ `f` vanishes on `{g1=g2=0}` wherever both leading coeffs are nonzero.* — because univariate polynomial division over a field is exact (the leading-coeff-is-a-unit condition makes `sp.div` genuine field division, not pseudo-remainder; this is the round-2 lesson codified in `run_state.md`).
- **Leading-coeff-genericity lemma.** *A nonzero rational function in `Q(t_A,...)` vanishes only on a Zariski-closed proper subset; one numerical evaluation at a generic point (e.g. any of the 47 prior configs) certifies genericity.* — because the zero locus of a nonzero rational function is a proper closed subvariety.
- **Blowup-is-coefficient-expansion-only (scout finding).** *`(T')_num` is genuinely small (35 monomials, total degree 10 in `(t_γ,t_β)`) when `t_A,t_B,t_α` are kept as field atoms; the round-2 timeout was purely a `expand_trig`-induced coefficient-explosion artifact (10³× monomial multiplication), NOT inherent problem size.* — because half-angle expansion of `sin A, cos A` into `t_A`-polynomials multiplies every monomial by a ~10-term polynomial, and the field-atom treatment sidesteps this entirely.

Open gaps: Step 8 only — every other step is rigorous (rounds 1–2). The scout has already verified Step 8 numerically (remainder zero, 81.6s); the builder's job is to reproduce `/tmp/probe_reduce.py` in the approach file, print both quotients + the zero remainder, add the leading-coeff-nonzero check (one numeric eval), and clear denominators for the polynomial-ring certificate. This is mechanical and well within one builder round.

Cases to cover: none (the inside-hypothesis branch is fixed; the certificate is a parameter-free polynomial identity valid for every non-degenerate triangle simultaneously).

Watch out for:
- **Do NOT call `expand_trig` on the full multivariate numerator** — the round-2 blowup (10⁴–10⁵ monomials) is the documented dead end. Keep `t_A,t_B,t_α` as `QQ.frac_field` atoms throughout; apply half-angle ONLY to `γ, β`.
- **Field division, not ring pseudo-remainder** — `sp.div` over a `frac_field` domain IS genuine field division when the divisor's leading coeff is a unit (round-2 rule). Verify the leading coeffs of `(C1)_num` in `t_γ` and `(C2)_num` in `t_β` are nonzero (Step 8d) BEFORE relying on the division.
- **The step-1 remainder `r1` is NOT zero** (degree 3 in `t_γ`) — this is expected and correct; the certificate requires BOTH divisions. Do not panic if `r1 ≠ 0`.
- **Independence**: this approach must NOT cite `analytic-branch-cert`'s saturation identity to close (T). The whole point of round 3 is a rival synthetic certificate. The ideal-membership certificate (Step 8) is the independent close. (Tactic (c) of the scout — invoke `analytic-branch-cert` as a black box — is the FALLBACK ONLY, to be used if Step 8 is blocked; flag this explicitly in the build report if it becomes necessary, since it forfeits independence.)

---

### power-secant-product: revise (Step 9 — directed-trig cancellation)

Target: Prove `OM = ON` for the configuration of IMO 2026 P2, via the secant-power route `OM=ON ⟺ MK·MV = NL·NW`, with the crux identity `(**)_corr` certified by an **independent symbolic cancellation** that does NOT lean on the antipode's `(T')` certificate nor the saturation identity. (The whole end-to-end claim; the power framing's own derivation of `(**)_corr` from the cross-ratio + arc-sum + sine-rule chain is what closes here.)

Technique: **Mechanical directed-trig symbolic check over a rational-function field with sin/cos atoms** — mirroring the antipode scout's frac_field-atom trick, applied to the power approach's Step 9 cancellation. The pure directed-angle chase (option (b)) was assessed HARD by the scout and is NOT recommended for one round; option (a) is the tractable close.

Skeleton (Steps 1–8 already rigorous; only Step 9 is revised):
1. *(Already rigorous, retain)* Reduction `OM=ON ⟺ MK·MV = NL·NW` (power of a point at M, N). (Approach Step 1.)
2. *(Already rigorous, retain)* Sine-rule expressions `MK·MV = 4R²·sin a·sin(γ−u)·sin u·sin(γ−a)/sin²γ` and `NL·NW = 4R²·sin b·sin(b+β)·sin w·sin(w+β)/sin²β` (CORRECTED `sin(b+β)`, not `sin(b−β)`). (Approach Step 2.)
3. *(Already rigorous, retain)* Directed-angle lemmas (i)–(iv), sign-fixed: `∠ALV=γ−u`, `∠BAV=γ−a`, `∠AKW=−(w+β)`, `∠CAW=−(b+β)`. (Approach Step 3.)
4. *(Already rigorous, retain)* Corrected crux `(**)_corr: sin a·sin(γ−a)·sin u·sin(γ−u)/sin²γ = sin b·sin(b+β)·sin w·sin(w+β)/sin²β`, equivalent to `OM=ON` (verified ~1e-10). (Approach Step 4.)
5. *(Already rigorous, retain)* SUM-form directed external-angle theorem: `∡(secant₁,secant₂) at X = ½[arc(far₁→far₂)+arc(near₁→near₂)] (mod π)`. (Approach Step 5.)
6. *(Already rigorous, retain)* α arc-sum: `2α = arc(R,A)+arc(K,P) = arc(A,S)+arc(Q,L)`, giving `arc(R,A)=2(α+u)`, `arc(A,S)=2(α−w)`. (Approach Step 6.)
7. *(Already rigorous, retain)* Midpoint cross-ratio link `(A,P;R,V)=(A,P;B,M)=2·MP/PB` and C-side `(A,Q;S,W)=(A,Q;C,N)=2·QN/QC` (perspectivity at K / at L). (Approach Step 7.)
8. *(Already rigorous, retain)* Sine-of-arc form of the circle cross-ratio: `(z₁,z₂;z₃,z₄) = [sin½(θ₃−θ₁)·sin½(θ₄−θ₂)]/[sin½(θ₃−θ₂)·sin½(θ₄−θ₁)]`, sign by directed separation. (Approach Step 8.)
9. **(GAP TO CLOSE — the revise target)** The directed-trig cancellation taking `{(B), (C), △AKL angle-sum} → (**)_corr`. Two sub-steps:
   - **(9a) Sign-pinning by directed-separation (the load-bearing sub-step, the numpy-sign-trap).** For the inside-hypothesis branch, the cyclic order of `{A,P,R,V}` (resp. `{A,Q,S,W}`) on Γ is fixed (the branch is connected). Compute this cyclic order on ONE representative config (the verified config `A=(0,0),B=(4,0),C=(1,3),K=(2.8,0.49465),L=(1.0479,2.3099)` already in the approach file), apply the directed-separation rule (mod π throughout — NOT acute-angle `arccos` picks), and pin the `±` signs of (B) and (C) to definite `+`/`−`. This makes (B), (C) into polynomial equations in sin/cos atoms with NO unresolved signs.
   - **(9b) Mechanical symbolic verification.** With signs pinned, substitute the sine-rule side-length expressions `|AB|=2R sin a·sin(u+α)/sin α`, `|AC|=2R·sin b·sin(α−w)/sin α`, `|AP|=2R|sin(a−u)|`, `|AQ|=2R|sin(b−w)|`, `|MP|=|AP|−|AB|/2`, `|PB|=|AB|−|AP|` (directed, signs from 9a) into (B), (C). Form `LHS−RHS` of `(**)_corr`. Verify it vanishes over `QQ.frac_field(t_a,t_b,t_u,t_w,t_α,t_β,t_γ)` (half-angle tangent for each angle, OR sin/cos as frac_field atoms with `sin²+cos²=1` as a constraint) modulo the constraint ideal `⟨(B)−2MP/PB, (C)−2QN/QC, angle-sum⟩` — by sequential univariate field-division (the antipode scout's pattern). Expected: remainder zero.

Key lemmas (claim + the one-line mechanism that makes it true):
- **Directed-separation sign rule (load-bearing).** *For four concyclic points, the sign of the cross-ratio `(z₁,z₂;z₃,z₄)` is `−` iff the pairs `{z₁,z₂}` and `{z₃,z₄}` separate on Γ (interleave in cyclic order); this sign is constant on each connected component of the configuration space, so it is determined by the inside-hypothesis branch.* — because the sine-of-arc form (Step 8) acquires its `±1` factor exactly when a directed angular difference crosses a `2π` boundary, which is the separation condition.
- **Branch-connectedness lemma.** *The inside-hypothesis configuration space (`K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK`) is connected, so the directed-separation signs are constant across it.* — the inside region is a convex (hence connected) open subset of the configuration space, and the cross-ratio sign is a locally constant function on configurations with four distinct concyclic points.

Open gaps: Step 9 only — every other step is rigorous (rounds 1–2). The hard sub-step is **9a (sign-pinning)** — this is the exact numpy-sign-trap the round-2 builder stalled on. 9b is mechanical once 9a is done (mirrors the antipode scout's verified pattern).

Cases to cover: the two separation cases (`±`) for each of (B), (C) — but the inside-hypothesis branch selects ONE of each; the other case is on a spurious mod-π branch excluded by the inside hypotheses (round-1 rule: spurious branches are not removable equalities but the inside hypotheses kill them).

Watch out for:
- **The numpy-sign-trap is the single risk.** Round-2 stalled here. The builder MUST pin signs by directed-separation (mod π, cyclic-order-based), NOT by `numpy.arccos`/`arctan2` acute-angle picks (the round-1/round-2 trap codified in `run_state.md`). If 9a cannot be closed rigorously in one round, **defer power** — do not force a half-baked symbolic check with unresolved signs (the dispatch explicitly forbids this).
- **Do NOT cite antipode's `(T')` certificate** to close — that forfeits independence (the dispatch's whole purpose). If `(**)_corr` is derived by invoking `(T) ⟺ (**)` + antipode's (T)-certificate, mark this explicitly as a fallback that loses independence, and flag for deferral instead.
- **`expand_trig` blowup risk** — same lesson as antipode: keep sin/cos (or `t_x`) as frac_field atoms; do NOT expand coefficients into `t_a,t_b,...` polynomials.
- **Honest deferral path.** If 9a stalls, the recommended action is: mark `power-secant-product` for deferral to a future round (with the sign-pinning as the named blocker), NOT to force-close via antipode. The approach stays alive (`partial`); it does not die. State this in the build report.

**Recommendation on power for this round's build set:** attempt option (a) (sign-pin then symbolic check) for ONE builder round. If the builder's report shows 9a could not be rigorously closed (signs still unresolved, or the symbolic check ran with guessed signs), the reviewer should mark power `CHANGES REQUESTED → deferral` (not RETHINK — the framing is sound, the gap is just hard). Antipode is the high-confidence build target this round.

---

### analytic-branch-cert: advance (no change — SOLVED)
Status: `solved` (round 2 APPROVE). Full proof in `current.md`. No revision; stays in population as the headline certificate.

### analytic-resultant-cert: advance (no change — SOLVED)
Status: `solved` (round 2 APPROVE). Independent resultant+Galois certificate (leans on saturation identity for the isosceles stratum). No revision; stays as the second analytic certificate.

---

build set: antipode-rightangle, power-secant-product
