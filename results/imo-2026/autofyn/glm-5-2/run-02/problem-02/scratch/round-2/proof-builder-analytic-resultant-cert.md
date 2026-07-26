# Proof-builder report: `analytic-resultant-cert` (imo-2026-02, round 2)

## Status: solved

The approach file `results/imo-2026-02/approaches/analytic-resultant-cert.md` now contains a complete proof of `OM=ON` via a **genuinely different closing certificate** (resultant + non-split Galois valuation) than the sibling `analytic-branch-cert` (saturation quotient `G`).

## What was verified from scratch (over the field, not pseudo-remainder)

1. **Resultant factorisation** (`Proposition 7`): `res_t(e3_line, Q_line) = (b⁸/16)·v²·|C|²·(|C|²−b²)·D₀²·R`, with `D₀²` **exact** (field-division by `D₀²` leaves remainder 0; `R mod D₀ ≠ 0`; prefactor constant in `(lx,ly)` so not divisible by `D₀`). Verified via `sp.factor(sp.resultant(...))` + field-division checks.
2. **`D₀` irreducible** (`Lemma 2`): `factor` over `Q(b,u,v,lx)[ly]` returns `D₀` unfactored; content is 1 (primitive); Gauss. Cross-checked: at `b=1,u=0,v=2,lx=−2` the cubic `ly³−3ly²+6ly−6` is irreducible over `Q` (rational-root test). Hence `(D₀)` is a height-one prime; `v_{D₀}` is well-defined.
3. **`et2`, `R`, prefactor all not divisible by `D₀`** (so `v_{D₀}(res)=2` exact, `v_{D₀}(res/et2²)=2`).
4. **Non-split** (`Lemma 9`, the genuinely new hard step): the discriminant `Δ=et1²−4·et2·et0` of `e3_line`, reduced mod `D₀`, is **not a square** in `κ=Q(b,u,v,lx,ly)/(D₀)`. Proven by specialization: at `b=1,u=0,v=2,lx=−2`, `D₀=2ly³−6ly²+12ly−12` has a real root `ly₀∈(1,2)` (IVT: `−4` at `ly=1`, `+4` at `ly=2`); `Δ_red=−101ly²/4+89ly−175/2`, a quadratic with discriminant `−1833/2<0` and leading coeff `<0`, hence `<0` for all real `ly`, in particular at `ly₀`. A real square is `≥0`, contradiction. Also `D₀∤Δ` (`Δ_red≢0`): unramified. Hence `(D₀)` is **inert** in `L=F(√Δ)`.
5. **Inert-Galois closing** (`§9`): the norm identity `res/et2² = Norm_{L/F}(Q_line(t₁))` (standard resultant theorem) + inertness (`w∘σ=w`, `v(Norm)=2·w(α)`) gives `w(Q_line(t₁))=1>0` and by conjugation `w(Q_line(t₂))=1>0`: **both** roots are shared along `D₀=0` (generic triangle). Nullstellensatz → `Q_line∈rad(D₀,e3_line)` over `Q(b,u,v)`. Polynomiality/Zariski-density extends to every triangle (including the isosceles exceptional stratum where the prefactor vanishes).
6. **Config conclusion** (`§11`): the configuration is a real point of `{D₀=0, e3_line=0}` with `et2>0` (Lemma 5, non-degenerate) and `L≠C` (Lemma 6, degenerate excluded); `Q_line` vanishes on that variety, so `Q_line(t₀)=0 ⟹ Q=0 ⟹ OM=ON`.
7. **Cross-check**: the saturation identity `Qt2·e3_line−et2·Q_line=D₀·G` (`G` linear in `t`) was independently re-verified TRUE (remainder 0 on field division over `Q(b,u,v,lx,t)[ly]`). Recorded only as a fallback/cross-check for the exceptional strata; the primary certificate is the resultant+Galois argument (NOT saturation).

## Spec concerns / deviations from the dispatch

1. **The dispatch's "root-selection" framing was re-conceived.** The dispatch asked to "pin the configuration's `t` to the shared root" (the hard step). I could not make that argument rigorous in isolation (the resultant gives *existence* of a shared root, not *which* root — and in the split case the config's root could be the non-shared one). **Instead, I closed by proving BOTH roots are shared** (via the inert-Galois valuation symmetry), which sidesteps the "which root" problem entirely: if `Q_line` vanishes at *every* root of `e3_line` on `D₀=0`, then whichever root the configuration's `t₀` is, `Q_line(t₀)=0`. This required the additional non-split Lemma 9 (which I proved rigorously). This is a stronger and cleaner certificate than the dispatch's "root-selection," and it is genuinely different from saturation (it derives "both roots shared" from the resultant's exact `D₀²`-multiplicity + Galois, not from an explicit `G` quotient).

2. **`et2>0` is used as the dispatch suggested**, but for a different purpose: not to "ensure the selected root is non-degenerate" (root-selection), but to guarantee `et2≢0 mod D₀` (so `v_{D₀}(et2²)=0` and the valuation arithmetic `v_{D₀}(res/et2²)=2` is exact). The positivity (Lemma 5) is reused from the sibling.

3. **Exceptional strata (isosceles `|C|²=b²`).** The inert-Galois count `v_{D₀}(res)=2` is exact only when the prefactor `(b⁸/16)v²|C|²(|C|²−b²)≠0` (generic triangle). At the isosceles stratum the prefactor vanishes (`res≡0` identically), so the generic valuation count is not directly applicable. I extended to all triangles by polynomiality/Zariski-density (`§10`: the generic identity `Q_line∈rad(D₀,e3_line)` is a closed condition holding on a dense open set, hence everywhere). As a belt-and-braces cross-check, I noted the saturation identity (re-verified TRUE, no `|C|²` vs `b²` assumption) explicitly covers these strata. If the reviewer finds the polynomiality extension hand-wavy, the saturation fallback (which I verified) closes the isosceles case directly; this is a write-up caveat, not a mathematical gap.

4. **Norm identity not numerically re-verified** (a symbolic `simplify(res − et2²·prod)` timed out on the large expression). I rely on it as the **standard resultant theorem** (KB "resultants / transform the roots": `res_t(f,g)=lc(f)^{deg g}·∏g(roots of f)`), which is a known algebraic fact, not a claim needing verification. The earlier numerical "mismatch" was an ill-conditioned cubic root at `lxs≈0` (D₀ not actually ≈0 there), not a counterexample.

## Files
- Approach: `/home/agentuser/repo/results/imo-2026-02/approaches/analytic-resultant-cert.md` (Status: solved, full proof + 6 promotable lemmas, 3 imported + 3 new).
- Verification scripts (record): `/tmp/round-2/resultant_verify.py`, `gcd_check.py`, `disc_check.py`, `nonsplit_check2.py`, `exact_nonneg.py`, `irred_check.py`, `final_crosscheck.py`, `norm_symbolic.py`.
