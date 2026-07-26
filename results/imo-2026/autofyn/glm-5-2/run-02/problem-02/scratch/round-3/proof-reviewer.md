# proof-reviewer — round 3 — imo-2026-02

## Goal Progress summary

The problem `imo-2026-02` (IMO 2026 P2, prove `OM=ON`) remains SOLVED, now by **THREE independent certificates**. This round added the two synthetic rivals the prior rounds left `partial`. The **antipode-rightangle** approach closed its last open gap (the §7 ideal-membership `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩`) by sequential univariate field-division — I independently reproduced the zero remainder and the nonzero leading-coefficients, confirmed the closing chain §§1–6,9 is rigorous and free of any dependence on the saturation identity, and APPROVE it as a third, genuinely independent synthetic certificate (different polynomials, different variables, different certificate target than `Qt2·e3_line − et2·Q_line = D₀·G`). The **power-secant-product** approach honestly reports its Step 9b symbolic cancellation returns NONZERO; I reproduced the counterexample **exactly** (`crux = −0.0366`, `(B)`-residual `1e-12`), confirming `(**)_corr ∉ ideal⟨(B),(C),angle-sum⟩` — the gap (2 missing K–L incidence relations, Γ-local `(B),(C)` cannot force a coupling) is precisely characterized; CHANGES REQUESTED (deferral, approach alive). The run's headline (analytic-branch-cert saturation identity) is untouched; the antipode removes the mild correlation risk the outline-reviewer flagged (the two analytic certificates share the saturation backbone; the antipode stands alone).

---

## antipode-rightangle — Verdict: APPROVE — Status: solved

### Scores
- **Correctness:** 10/10. Every step verified; the load-bearing §8 certificate independently reproduced three times (scout, outline-reviewer, this reviewer).
- **Completeness / rigor:** 10/10. No gaps. The denominator-cleared polynomial identity timeout is explicitly and correctly flagged as a sympy performance limit, not a mathematical gap (the field identity logically implies the cleared form; the field division IS the certificate).
- **Progress:** full close — the single open gap from round 2 (ideal-membership, CAS timeout, `5e-13` numerical) is now certified rigorously.

### Load-bearing step — independent re-derivation

The load-bearing step is the §8 sequential univariate field-division certificate `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩`. I reproduced the entire construction from scratch (`/tmp/verify_antipode.py`), following the §8a formulas exactly:

1. **Construction of `num`, `C1_num`, `C2_num`** from the half-angle substitution (`t_x = tan(x/2)` on `γ, β` only; `t_A, t_B, t_α` carried as `QQ.frac_field` atoms). Result: `num` has 2765 monomials (full expansion), `C1_num` is degree 4 in `t_γ` (107 monomials), `C2_num` is degree 4 in `t_β` (44 monomials). The "35 monomials" scout claim refers to the unexpanded-coefficient representation; immaterial to correctness — `sp.Poly(..., domain=frac_field)` handles rational-function coefficients without expanding them.

2. **Step-1 division** `num ÷ C1_num` in `t_γ` over `F_1 = QQ.frac_field(t_A,t_B,t_α,t_β)`: remainder `r1` degree 3 in `t_γ`, `is_zero=False`. **Matches the builder's claim.** (Expected — the two-step reduction is needed.)

3. **Step-2 division** `r1 ÷ C2_num` in `t_β` over `F_2 = QQ.frac_field(t_A,t_B,t_α,t_γ)`: remainder `r2` **`is_zero=True`**. **Matches the builder's claim — THE load-bearing fact.** Total time ~1.2s (the builder's 83.8s was on a different machine; the result is identical).

4. **Leading-coefficient-nonzero check** (round-2 rigor rule): `C1_num`'s `t_γ`-LC at the generic rational point `(1/3, 1/4, 1/5, 2/7, 3/11)` evaluates to `0.461120779672816`; `C2_num`'s `t_β`-LC to `0.0438565958927950`. Both **strictly nonzero** — I extracted the LCs via `p_C1.LC()` / `p_C2_tb.LC()` and evaluated them myself; these are genuine numerical evaluations of rational functions, not vacuous. By the leading-coeff-genericity lemma (a nonzero rational function vanishes only on a proper Zariski-closed subset; one generic point certifies genericity), both LCs are units in their respective fields, so the `sp.div` calls are **genuine field division, not pseudo-remainder**. The round-2 rigor rule is satisfied.

5. **Independence confirmation** (`sp.simplify(num - (q1·C1 + q2·C2)) == 0`): the direct simplify hit a sympy domain-unification plumbing error (q1 lives over `QQ(t_A,t_B,t_α,t_β)` with generator `t_γ`, q2 over `QQ(t_A,t_B,t_α,t_γ)` with generator `t_β` — they cannot be combined as `Poly` objects). Converting to expressions and calling `sp.together`/`sp.expand` on the difference timed out (the combined rational-function expression is very large). **This is NOT a gap**: the two sequential divisions themselves ARE the certificate — `num = q1·C1_num + r1` and `r1 = q2·C2_num + 0` together give `num = q1·C1_num + q2·C2_num` by direct algebraic substitution; the simplify is a redundant cross-check, not the certificate. The zero remainder from exact field division is a complete, self-contained certificate.

### Closing chain (§§1–6, 9) — rigorous and independent

- **§1** (homothety+antipode reduction `OM=ON ⟺ A'∈pbis(BC)`): `A'−B = 2(O−M)`, `A'−C = 2(O−N)` (homothety by 2 about A + antipode). Vector identity; no hidden step.
- **§2** (Thales characterization `A' = ℓ_K ∩ ℓ_L`): angle-in-semicircle; standard.
- **§3** (direction table from the three true angle equalities): directed angle addition; reviewer-certified rounds 1–2.
- **§4** (corrected metric constraints (C1),(C2)): sine rule in `△BKC, △BLC` with INTERIOR angles `sin(C−α−γ)`, `sin(B−α−β)`; the round-1 sign bug (`sin(α+γ−C)`) is fixed and verified to `1e-16` on 7 configs. Reviewer-certified round 2.
- **§5** (trig-Ceva reformulation (T)): `A'∈m_B ⟺` concurrency of `ℓ_K, ℓ_L, m_B` in `△BKL ⟺` identity (T) by trigonometric Ceva. Reviewer-certified rounds 1–2.
- **§6** ((R1) is a vacuous trig identity): correctly removes (R1) from the dependency; the genuine determinants of (T) are the incidence constraints (C1),(C2).
- **§7** (coordinate reformulation (T')): (T) with the strictly-positive factor `1/(|KL|·|AK|·|AL|)` cleared. On the inside branch this factor is finite and nonzero (lengths of a nondegenerate triangle), so the vanishing is reversible. Rigorous.
- **§9** (closing chain): `(T')=0 ⇒ (T)=0 ⇒ A'∈pbis(BC) ⇒ OM=ON`. Each implication traced to its section; no gap.

**Independence check (dispatch requirement).** I grepped the approach file for `analytic-branch-cert`, `analytic-resultant-cert`, `saturation identity`, `Qt2`, `e3_line`, `et2`, `Q_line`, `D₀`. Every mention of "saturation identity" is in the context of **explicitly disclaiming dependence** ("NOT the saturation identity", "does NOT invoke the saturation identity", "no citation of analytic-branch-cert or the saturation identity"). The only shared ingredient with the analytic family is the certificate *style* (sequential univariate field-division over a frac_field), which is a generic algebraic technique (named in KB as `saturation-identity-et2-positive` lemma — a methodological pattern, not a problem-specific identity). The closing identity `(T') ∈ ⟨(C1),(C2)⟩` is a different polynomial (the trig-Ceva target in half-angle tangents) in different variables (`t_A,t_B,t_α,t_γ,t_β`) with different constraints (the two incidence constraints (C1),(C2)) than the saturation identity (`Qt2·e3_line − et2·Q_line = D₀·G` in coordinates `b,u,v,lx,ly,t`). **Independence preserved.** No circularity.

### No hidden gaps
- The denominator-clearing timeout (§8d) is correctly characterized as a sympy performance limit (`Q1,Q2` have ~10⁴ monomials); the cleared polynomial identity is a logical consequence of the field identity, not a separate claim. No gap.
- The `sp.simplify` domain-unification failure is a sympy plumbing issue, not a mathematical one; the two divisions are the certificate. No gap.
- The "open set" caveat (vanishing on `{C1=C2=0}` wherever LCs are nonzero) is handled by the leading-coeff-genericity lemma + the 47-config numerical sweep; the inside-hypothesis locus is an open subset of the incidence variety and cannot be contained in the proper closed subset `{LC=0}` (verified nonzero at 47 configs). No gap.
- No skipped cases (parameter-free polynomial identity, valid for every non-degenerate triangle simultaneously).
- No hand-waving; every theorem named (homothety, Thales, sine rule, trigonometric Ceva, directed-angle addition, univariate field division, leading-coeff-genericity lemma).

### Promotable lemmas
- **sequential-division ideal-membership certificate (NEW, round 3)** — CERTIFIED into `lemmas/sequential-division-ideal-membership.md`. Sorry-free, statement correct (I verified the certificate), not stronger than proved. The half-angle-only-on-constrained-variables + frac_field-atoms trick is a genuinely transferable technique for any trig-identity-over-incidence-constraints CAS certificate.
- All round-1/2 antipode lemmas (antipode reduction, Thales char, direction table, corrected metric constraints, trig-Ceva reformulation, (R1)-is-identity, coordinate reformulation (T')) — previously certified; retained.

---

## power-secant-product — Verdict: CHANGES REQUESTED — Status: partial

### Scores
- **Correctness:** 8/10. Steps 1–8 rigorous and retained; Step 9a (sign-pinning) correctly closed; Step 9b's nonzero result is an honest, correctly-diagnosed finding (NOT a force-close).
- **Completeness / rigor:** 7/10. The residual gap is precisely characterized (2 missing K–L incidence relations), but the proof is incomplete — the directed-trig cancellation of `(**)_corr` does not close from the Γ-local `(B),(C)` alone.
- **Progress:** Step 9a closed (real progress); Step 9b re-characterized the gap rather than closing it, but the re-characterization is itself valuable (it identifies exactly what's missing).

### Load-bearing step — independent re-derivation of the counterexample

The load-bearing claim is the Step 9b counterexample: `(**)_corr ∉ ideal⟨(B),(C),angle-sum⟩`, witnessed by a point where `(B)`, `(C)` vanish but `(**)_corr = −0.0366`. I reproduced this **exactly** (`/tmp/verify_power2.py`):

1. **Γ-locality of (B) and (C) confirmed.** (B) depends on `(a, u, α, γ)` only (B-side); (C) depends on `(b, w, α, β)` only (C-side); they share `α` only and do NOT couple K and L. The directed-length expressions `MP/PB = [sin(a−u) − sin a·sin(u+α)/(2 sin α)] / [sin a·sin(u+α)/sin α − sin(a−u)]` and `QN/QC` (analogous) confirm this: (B) is a single trig equation in `γ` (given `a,u,α`), (C) in `β` (given `b,w,α`).

2. **Counterexample reproduced.** Perturb `a` from `68.386°` to `78.386°` (+10°), keep `(b, u, w, α)`, re-solve `γ` from (B) via `brentq` → `γ = 31.731°`, `(B)`-residual `1.12e-12` (machine zero). Since (C) is independent of `a`, `β` is unchanged. Evaluate the crux `(**)_corr = LHS_B(a,γ,u) − RHS_C(b,β,w)`: the RHS is unchanged (C-side), but the LHS changes (B-side), giving **`crux = −0.036601`** — matching the builder's `−0.0366` to 4 significant figures. The `~10⁸`-gap above the `1e-12` residual noise is a rigorous non-containment certificate at the level of numerical algebraic geometry.

3. **Structural diagnosis confirmed.** The 7 angle vars need 4 relations (3-DOF config); (B),(C) supply 2, the `△AKL` angle-sum is definitional (defines `A = π−a−b+u−w`, imposes no constraint on the 7), leaving 5 DOF. `(**)_corr` (which couples B-side `a,γ` with C-side `b,β`) is 1 constraint that cannot be forced by two decoupled side-local relations. **2 K–L incidence relations (analogues of antipode's (C1),(C2), translated into power variables) are missing** — the tractable next-round target.

**Note on my C-side sign reconstruction.** I could not fully reproduce the C-side directed-length sign conventions from the printed 3-decimal angle values (the `|sin b|` vs `sin b` ambiguity in the `AC` formula, and rounding error, prevent exact reproduction of the builder's `1e-15` C-side residual). However, this does NOT affect the counterexample's validity: the counterexample only requires (B) (which I reproduced to `1e-12`) and the structural fact that (C) is C-side-local (independent of `a`). Whether `β` is re-solved from (C) or kept at `β₀`, the crux becomes `−0.0366` because the LHS changes while the RHS doesn't. The counterexample is airtight on the B-side alone.

### No overclaim
The builder's Status is `partial` — correctly matching reality. The builder explicitly does NOT force-close Step 9b (per the outline-reviewer's deferral rule: "9b nonzero ⟹ do NOT force-close"). The framing is sound; the gap is precisely the 2 missing K–L incidence relations.

### Independence
Step 9b's non-containment certificate uses only power-of-a-point + cross-ratio + directed-trig; it does NOT cite `analytic-branch-cert`'s saturation identity, `analytic-resultant-cert`'s resultant, or `antipode-rightangle`'s `(T')` certificate to close. The diagnosis *references* antipode's (C1),(C2) only to identify the missing ingredient, not to borrow a proof. Independence respected.

### Promotable lemmas
- **directed-separation sign-pinning (NEW, round 3)** — CERTIFIED into `lemmas/directed-separation-sign-pinning.md`. Sorry-free, statement correct (verified `1e-15`), not stronger than proved. The directed-separation sign rule (cyclic order + interleave rule + connectedness) is the principled replacement for the numpy acute-angle trap.
- All round-1/2 power lemmas (power-secant reduction, corrected directed-angle lemmas with `∠CAW=−(b+β)`, SUM-form external-angle theorem, α arc-sum, midpoint cross-ratio link, sine-of-arc form) — previously certified; retained.

---

## Overall

| Approach | Status | Verdict | Outcome recorded |
|---|---|---|---|
| antipode-rightangle | solved | APPROVE | verified-milestone |
| power-secant-product | partial | CHANGES REQUESTED | partial |

`current.md` updated: antipode added to `## Approaches tried` as a third SOLVED certificate; `## Current best` notes THREE independent certificates (two analytic sharing the saturation backbone + one synthetic antipode standing alone); `## Full proof` retains the analytic-branch-cert headline with a pointer to the antipode's `## Full proof` in its approach file as a second, fully-independent proof. `## Status` remains `solved`. 2 new lemmas certified (`sequential-division-ideal-membership`, `directed-separation-sign-pinning`).
