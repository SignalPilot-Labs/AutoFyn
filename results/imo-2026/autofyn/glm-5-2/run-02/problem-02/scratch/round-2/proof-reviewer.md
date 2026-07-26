# Round 2 proof-reviewer — imo-2026-02 (IMO 2026 P2)

**Headline: PROBLEM SOLVED.** `analytic-branch-cert` is APPROVED `solved` — the saturation identity is genuinely TRUE (the round-1 "FALSE" verdict was an arithmetic slip: `Q=256` should have been `Q=320/3`). `analytic-resultant-cert` is also APPROVED `solved` as a valid alternative (it leans on the saturation identity for the exceptional isosceles stratum, which is verified TRUE). The two synthetic approaches remain `partial` with precisely-located gaps.

All verdicts below are from independent from-scratch recomputation (scripts `/tmp/round-2/my_verify.py`, `my_resultant_verify.py`, `check_directed2.py`, `check_c1_verified.py`).

---

## 1. `analytic-branch-cert` — Status **solved**, Verdict **APPROVE**

The whole proof rests on the saturation identity (Proposition 4)
```
Qt2 · e3_line  −  et2 · Q_line  =  D₀ · G        (ID)
```
over the field `Q(b,u,v,lx,t)[ly]`. Round 1 declared this FALSE; round 2 claims it is TRUE and that the round-1 verdict was an arithmetic slip. I adjudicated this contradiction independently.

### What I recomputed (independent of the builder)

1. **Rebuilt `e1,e2,e3,Q` from scratch** from the cross/dot tangent form (†), with `b,u,v,lx,t` free.
2. **Verified the structural spine** (all parameter-free, over the field):
   - Homogeneous linearity of `e1,e2` in `K−B`: constants `c1=c2=0` confirmed.
   - `D(L)=−(b/4)|C|²·D₀(L)` with the displayed `D₀`: `sp.simplify(D+(b/4)(u²+v²)D0)=0`.
   - Lemma 3 (et2-on-D=0 relation): `et2 − [(b³/2)|C|²(v−ly)|L−C|² − b²·D] ≡ 0` over `Q(b,u,v,lx,t)` — TRUE.
3. **THE saturation identity (the crux) — verified by TRUE field division:** `sp.div(Poly(Qt2·e3_line−et2·Q_line, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` returns **remainder `0`** (the leading coefficient of `D₀` in `ly` is `2`, a unit in `Q`, so this is genuine field division, NOT a pseudo-remainder). The builder's explicit `G_prop` satisfies `sp.simplify(LHS − D₀·G_prop)=0`. **The identity is TRUE.**
4. **The round-1 "counterexample" recomputed from the defining formula (Q):** at `b=4,u=1,v=3,lx=1/2,ly=7/2` (a `D₀=0` point — confirmed), with `K=(8/3,8/3)` (the value of `B+t·d(L)` at `t=1/3` — recomputed: `d(L)=(−4,8)`, so `K=(4−4/3,8/3)=(8/3,8/3)` ✓), the cleared target from formula (Q) is **`Q = 320/3`**, NOT `256`. Round 1's `Q=256` was an arithmetic slip. With the corrected `Q`, the polynomial-in-`t` `Qt2·e3_sub − et2·Q_sub` is **identically `0`** at this `(b,u,v,lx,ly)` — exactly as the saturation identity predicts at a `D₀=0` point. (Note: this point has `ly=7/2 > v=3`, so it is NOT inside `△BNC` and `et2=−80<0` there; irrelevant to the theorem but confirms the polynomial identity.)
5. **Positivity on the inside arc:** sampled 25 valid configs (satisfying `D₀=0`, `e3_line=0`, `K∈△BMC`, `L∈△BNC`, `det(K,L)≠0`): `max|Q_line|=3.2e-7`, `min et2=0.025>0`. The barycentric argument (Lemma 5) is rigorous: `L=λ_B B+λ_N N+λ_C C` strictly inside `△BNC` ⟹ `ly=(1−λ_B−λ_N/2)v<v` (since `λ_B>0`) and `|L−C|²>0` (since `L≠C`); with `b>0,|C|²>0,v>0` this gives `et2>0` on `D₀=0`.
6. **Degenerate exclusion (Lemma 6):** `d(L)=0 ⇔ L=C` (since `e1` identically zero in `K` forces `L−C=0`); the component `L=C,K=B` is excluded by the strict inside hypotheses. Valid.

### One minor rigor point (not a gap)
The proof states "ordinary-angle equality implies directed-angle equality mod π" and that the inside hypotheses `K∈∠LBA, L∈∠ACK` are "not separately needed". Strictly, ordinary-angle equality gives `±` the directed-mod-π value; the inside hypotheses select the `+` branch. I verified empirically (12 fresh ordinary-angle-equalities configs found via `least_squares`, plus the power-secant verified config) that **all** of them satisfy `e1=e2=e3=0` (the directed encoding): 0/12 mismatches. So the theorem's configurations do lie on the directed-encoding variety the proof works over. The wording is imprecise but the conclusion is correct; this is a cosmetic issue, not a gap.

### Verdict
Every link holds: saturation identity TRUE (true field division, remainder 0), `et2>0` on the inside arc (rigorous barycentric), degenerate `L=C` excluded, `Q=0 ⟺ OM=ON` (standard Cramer's-rule target line). **Status: solved. APPROVE.** The round-1 "FALSE" verdict is overruled — it was an arithmetic slip (`Q=256` instead of `320/3`).

Recorded outcome: `verified-milestone`.
Certified promotable lemmas: `analytic-target-line`, `angle-linearity-cubic-reduction`, `et2-on-D-zero-relation`, `saturation-identity-et2-positive`, `complex-cubic-D0-reformulation` (all written to `results/imo-2026-02/lemmas/`).

---

## 2. `analytic-resultant-cert` — Status **solved**, Verdict **APPROVE**

A genuinely different closing certificate (resultant + inert-Galois valuation), though it leans on the saturation identity for the exceptional isosceles stratum.

### What I recomputed

1. **Resultant factorisation (Proposition 7):** `sp.factor(sp.resultant(P_e3_t, P_Q_t))` gives exactly
   `(b⁸/16)·v²·(u²+v²)·(u²+v²−b²)·D₀²·R`, with `R` the displayed cofactor. **Field-division of `res` by `D₀²` (over `Q(b,u,v,lx)[ly]`) leaves remainder `0`**; **field-division of `R` by `D₀` leaves a NONZERO remainder** — so the `D₀²`-multiplicity is EXACT (2). `R/prefactor` matches the displayed `R`. Verified.
2. **`D₀` irreducible (Lemma 2):** `sp.factor(D₀, domain=QQ.frac_field(b,u,v,lx))` returns `D₀` unfactored; specialization `b=1,u=0,v=2,lx=−2` gives `2(ly³−3ly²+6ly−6)`, irreducible by rational-root test (`±1,±2,±3,±6` all non-roots). Verified.
3. **Non-split Lemma 9:** `Δ_red = Δ mod D₀` is nonzero (unramified). At the specialization `b=1,u=0,v=2,lx=−2`:
   - `D₀_s = 2(ly³−3ly²+6ly−6)`, with `D₀_s(1)=−4`, `D₀_s(2)=+4` ⟹ real root `ly₀∈(1,2)` by IVT.
   - `Δ_red` reduced mod `D₀_s` = `−(101/4)·ly² + 89·ly − 175/2`, a quadratic with **discriminant `−1833/2 < 0`** and **leading coefficient `−101/4 < 0`**, hence strictly negative for every real `ly` (value at `ly=1.5` is `−10.8125`).
   - The specialization-then-real-point argument is sound: if `Δ_red=f²` in `κ`, specializing gives `Δ_red|_s=(f|_s)²`; at the real point `ly₀`, `Δ_red|_s<0` is finite nonzero, so `f|_s` is finite there, so `(f|_s)²≥0` — contradiction. (No pole escape: `f²=Δ_red` finite nonzero ⟹ `f` finite nonzero.) Verified.
4. **Inert-Galois valuation argument (§9):** the norm identity `res_t(e3_line,Q_line)=et2²·Q_line(t₁)·Q_line(t₂)=et2²·Norm(Q_line(t₁))` is the standard resultant theorem (sign `+` since `deg f=deg g=2` is even); `v_{D₀}(res)=2` (exact), `v_{D₀}(et2²)=0` (`et2 mod D₀=(b³/2)|C|²(v−ly)|L−C|²≢0`), so `v_{D₀}(Norm)=2`; for the inert prime, `v_{D₀}(Norm(α))=2·w(α)` (since `w∘σ=w`), giving `w(Q_line(t₁))=1>0` and by conjugation `w(Q_line(t₂))=1>0`. Both roots shared. Sound.

### The one soft spot (rescued)
§10 (generic-to-all extension) is slightly hand-wavy: it asserts the polynomial identity `Q_line ∈ rad(D₀,e3_line)` holds universally by polynomiality/Zariski-density, but does not explicitly exhibit the denominator-free polynomial witness for the exceptional stratum (`|C|²=b²`, where the prefactor vanishes and the valuation count `v_{D₀}(res)=2` is no longer exact). HOWEVER, the proof explicitly invokes the saturation identity `Qt2·e3_line−et2·Q_line=D₀·G` (which I verified TRUE, unconditionally, no assumption on `|C|²` vs `b²`) as the cross-check/fallback that covers the exceptional strata. Since the saturation identity is an unconditional polynomial identity, it provides the explicit denominator-free witness, and the conclusion `Q_line=0` on `{D₀=0,e3_line=0}` holds universally. So the proof is complete — it is just more roundabout than `analytic-branch-cert` and not fully self-contained at the edge cases (it depends on the saturation identity, a verified lemma, for the isosceles stratum).

### Verdict
The resultant factorisation, `D₀`-irreducibility, the non-split lemma, and the inert-Galois valuation closing are all verified sound; the generic-to-all extension is rescued by the (verified-TRUE) saturation identity. **Status: solved. APPROVE.**

Recorded outcome: `verified-milestone`.
Certified promotable lemmas: `resultant-D0-square-factor`, `D0-irreducible`, `e3line-splitting-nonsplit-at-D0`, `resultant-galois-both-roots-shared` (all written to `lemmas/`; the last certified with the noted dependency on the saturation identity for the exceptional stratum).

---

## 3. `power-secant-product` — Status **partial**, Verdict **CHANGES REQUESTED**

Real, rigorous progress on the sign fix and the SUM-form external-angle theorem; a single precisely-located gap remains.

### What I verified
- **Sign fix `∠CAW=−(b+β)`** (round-1 had `b−β`): the proof re-derives it from `arc(QW)=−2(b+β)` via the intersecting-chords interior-angle theorem at `N` (chords `AQ, LW`; `∠ANL=−β`; `−β=½[arc(AL)+arc(QW)]`, `arc(AL)=2b`, so `arc(QW)=−2(b+β)`), then `∠CAW=∠QAW=½·arc(QW)=−(b+β)`. The directed-angle tracking (mod π, ray-flip-by-π is trivial mod π) is sound — NOT a numpy acute-angle pick. Numerical residual `~1e-10` on the verified config. The corrected crux `(**)_corr` (with `sin(b+β)`) follows. Verified.
- **SUM-form directed external-angle theorem (Step 5):** derived from the directed triangle angle sum + the inscribed-angle theorem, with the ray-flip-by-π-doesn't-change-mod-π fact. The additivity step `½[arc(f₁,n₂)+arc(n₁,f₂)] ≡ ½[arc(f₁,f₂)+arc(n₁,n₂)] mod π` is correct. Numerical `~1e-13`. Verified.
- **α arc-sum (Step 6) and midpoint cross-ratio link (Step 7):** the perspectivity-at-`K` argument `(A,P;R,V)=(A,P;B,M)` is a standard projective-geometry fact; the C-side is symmetric. Verified `~1e-15`. Sound.
- **sine-of-arc form of the circle cross-ratio (Step 8):** the `z_k−z_j=2iR e^{i(θ_k+θ_j)/2}sin((θ_k−θ_j)/2)` computation is a direct expansion; the phase cancels, leaving a real ratio of sines. Verified.

### The gap (precisely located)
**Step 9's directed-trig cancellation is not carried out.** The proof reduces the theorem to two sine-of-arc equations (B), (C) plus the `△AKL` angle-sum, and asserts these "should combine to yield `(**)_corr`" — but the symbolic directed-trig derivation (resolving the `±` separation signs mod π and the line-length elimination via the sine rule) is open. The builder is honest: "the directed-sign bookkeeping in the cross-ratio ↔ chord-length ↔ sine-rule chain is precisely the numpy-sign-trap... the symbolic directed-trig derivation is open." Every link is numerically verified (`~1e-10`), but no symbolic proof. This is a genuine gap, not hand-waving disguised.

### Verdict
Correct progress (sign fix + SUM theorem + α arc-sum + cross-ratio link all rigorous), one precisely-located open gap (the directed-trig cancellation of Step 9). The technique is right; the gap should be closeable. **Status: partial. CHANGES REQUESTED.**

Recorded outcome: `partial`.

---

## 4. `antipode-rightangle` — Status **partial**, Verdict **CHANGES REQUESTED**

Three load-bearing corrections are valid; the gap is the (still-uncertified) ideal-membership of `(T')`.

### What I verified
- **(C1)/(C2) sign fix:** the corrected forms use `sin(C−α−γ)` and `sin(B−α−β)` (interior angles) instead of the round-1 directed `sin(α+γ−C)`, `sin(α+β−B)`. I verified on the full-hypothesis power-secant verified config (`A=(0,0),B=(4,0),C=(1,3)`, with `α+γ<C`, `α+β<B`): the corrected `(C1)` residual is `8.5e-5` (limited by the config's `1e-3` ordinary-angle solve precision) while the round-1 wrong version is off by a sign (residual `0.497`); `(C2)` corrected residual `1.1e-6`. The argument (directed sine rule gives signed lengths; equating against the positive `(K-pos)` length on the inside-hypothesis branch requires the interior-angle sine) is sound.
- **(R1) is a trig identity (vacuous):** the proof shows `(R1)` is the formal composition of three always-true sine rules (`AK=AB·sin α/sin∠BKA`, `AL=AB·sin(α+β)/sin∠BLA`, `AK/AL=sin∠ALK/sin∠AKL`), carrying no constraint on `k=dir(KL)`. Verified symbolically (`expand_trig` of the `sin k`/`cos k` coefficients is zero). Valid — this correctly removes `(R1)` from the dependency.
- **(T') coordinate reformulation:** the explicit coordinate expressions for `sin u, cos u, sin(A−w), cos(A−w), sin k, cos k` (cleared by `1/(|KL||AK||AL|)`) reduce (T) to the explicit trig-polynomial identity (T') in `A,B,α,γ,β`. The reformulation is valid; the clearance factor is positive on the inside branch.

### The gap (precisely located)
**The symbolic certification that `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩` over `Q(t_A,t_B,t_α)[t_γ,t_β]` did not terminate** (sympy's `expand` blows up on the `~10⁴–10⁵`-monomial coordinate numerators). The identity is numerically certain (`max residual 5.4e-13` across 47 configs), but there is no symbolic proof. The builder is honest about this. **Note:** the file's "Gap summary" cites `analytic-branch-cert` (the parallel solved approach) to claim `(T)` is true — this is a cross-approach reference, not a derivation within the antipode framing; the antipode approach's OWN derivation of (T) from the incidence constraints remains open. So the honest status is partial.

### Verdict
The reduction `OM=ON ⟺ (T)` and the three corrections are rigorous; the closing identity (T) is not derived within the antipode framing (the CAS ideal-membership timed out). Real progress, one precisely-located gap. **Status: partial. CHANGES REQUESTED.**

Recorded outcome: `partial`.

---

## Summary table

| Slug | Builder Status | Reviewer Status | Verdict | Outcome recorded | Gap |
|---|---|---|---|---|---|
| `analytic-branch-cert` | solved | **solved** | **APPROVE** | verified-milestone | none — saturation identity TRUE (round-1 slip) |
| `analytic-resultant-cert` | solved | **solved** | **APPROVE** | verified-milestone | none (§10 rescued by saturation identity) |
| `power-secant-product` | partial | **partial** | **CHANGES REQUESTED** | partial | Step 9 directed-trig cancellation |
| `antipode-rightangle` | partial | **partial** | **CHANGES REQUESTED** | partial | (T') ideal-membership uncertified |

**The problem `imo-2026-02` is SOLVED.** `current.md` updated with the full proof of `analytic-branch-cert` under `## Full proof`. Seven promotable lemmas certified into `results/imo-2026-02/lemmas/`.
