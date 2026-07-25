# Proof-reviewer adjudication — imo-2026-02, round 4

Reviewed all three built approaches. Independently rebuilt every
load-bearing symbolic/numeric claim from scratch (own `sympy`/`scipy`
scripts, not trusting the files' or explorers' reported numbers) before
adjudicating.

## 1. `coordinate-bash-resultant-boundary` — CHANGES REQUESTED (partial)

**Claims checked:**
- Resultant factorization `Res_{s2}(G2a,G2b)=64u²(u²+1)⁴·F1·F2·F3`.
  **Independently reproduced from scratch** (own script rebuilding `eq2`
  via the cross-product-square construction, dividing by `t1²`,
  factoring, extracting the degree-4-in-`u` cofactor `G2a`, computing
  `sp.resultant(G2a,G2b,s2)`): matches the file's `F1,F2,F3` exactly,
  including `F3=(2a-b)u^4-(4a+2b)u^2+(2a-b)`.
- `F2=0⟺β=∠ACB` (§7). Independently solved `F2=0` for `u`, evaluated
  `tanβ=2u/(1-u²)`, got `a·cc/(b²+cc²-ab)`; independently computed
  `tan(∠ACB)` via signed cross/dot and got the identical expression.
  Confirmed exact match. The uniqueness/exactness argument (tan is
  injective on `(0,π)`, and both `β` and `∠ACB` lie in `(0,π)`, so the
  only common zero of `sin(β-∠ACB)` in the domain is `β=∠ACB` itself,
  ruling out the "supplementary" alternative) is simple, sound reasoning
  — no gap found. **This closes the item flagged open in round 3's
  `branch-crossing-locus-equals-angle-B.md`** for both `F1` and `F2`.
  Certified as new `lemmas/branch-crossing-locus-equals-angle-C.md`;
  updated `lemmas/branch-crossing-locus-equals-angle-B.md` to record the
  now-closed exactness.
- Ray-direction monotonicity (§8). Straightforward rotation-geometry
  argument; correct. The file's own caveat — that this alone doesn't
  finish range-connectedness because a point on a valid-direction ray can
  still overshoot the finite triangle through the far edge — is a real
  and correctly identified additional gap (a magnitude bound
  `t1<t1max(β)`), not resolved this round.
- `F3,F3'` counterexample (§9). Independently reproduced the counterexample
  triangle `A=(0,0),B=(1,0),C=(0.9,0.2)`: confirmed `∠ABC≈63.435°`,
  `∠ACB≈104.036°`, `b/(2a)=0.45`, `F3=0` at `β≈47.870°` — strictly inside
  the valid range `(0,63.435°)`, contradicting the round-3 working
  assumption. Independently tracked the true (unsquared) hypothesis-2
  root `s2(β)` through this crossing via continuation and confirmed
  `G2a≈0` (`<10⁻¹³`) throughout, while the two branches' shared root at
  the crossing (`s2≈0.745`, computed by finding the common root of
  `G2a(s2)` and `G2b(s2)` at `β=47.870°`) is a *different* value from the
  genuine branch's own root (`s2≈0.0502`) — matching the file's own
  "harmless crossing" interpretation exactly. This is real, correctly
  diagnosed new information; genuine general non-swap proof is still
  missing (correctly reported as open). Certified the algebraic
  identification and counterexample as `lemmas/f3-f3prime-resultant-factors.md`
  (the "always harmless" claim left explicitly uncertified).

**Verdict: gap 2 (branch selection) is not closed.** No overclaiming
found anywhere in the file; every claimed result was independently
reproduced, and every open item is honestly flagged as open. Status
`partial` is accurate. **CHANGES REQUESTED** — re-dispatch to close the
magnitude bound and/or the general F3-crossing-is-harmless argument.

## 2. `coordinate-bash-resultant` — CHANGES REQUESTED (partial)

**Claims checked:**
- Acute-angle-bound refutation. Independently reconstructed the reported
  counterexample (`a=0.9959,b=2.0302,cc=1.1413,t1=0.1522,t2=1.2001,
  β≈9.72°`) from the rotation parametrization: reproduced `∠LBK≈∠LNC≈
  95.18°` (obtuse) and confirmed both containments hold with real margin.
  **Refutation is sound** (this is the third independent confirmation,
  after the explorer and the outline-reviewer). Retiring this sub-route
  is correct.
- `lemmas/isosceles-case-symmetry.md`'s existence/uniqueness argument
  (Step 3). **Independently rebuilt from scratch**: symbolically
  differentiated `f(x)=\sin x/\sin(\theta+x)` and
  `g(x)=\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta-x)}{\sin(A+2\theta+x)}`
  under the isosceles substitution `A=\pi-2B` (i.e. `C=B`), and confirmed
  `f'(x)=\sin\theta/\sin^2(\theta+x)` and
  `g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin^2(A+2\theta+x)}`
  match the file's claims exactly (symbolic residual 0 in both cases).
  Independently confirmed the required boundary sign pattern
  `Φ(θ,0⁺)<0<Φ(θ,(B-θ)⁻)` over 3000 random `(θ,B)` samples spanning the
  valid domain, zero exceptions. The monotonicity + IVT argument for a
  unique shared root `ψ=φ=x(θ)` is genuinely rigorous, not merely
  plausible. Step 6(ii)'s non-collinearity argument (elementary convexity/
  height bound ruling out `AK∥BC`) is also sound. The one open point,
  Step 6(i) (`K≠L` not independently proved for this sub-case), is
  honestly disclosed and is an inherited standing assumption shared by
  every approach in the population (none independently proves `A,K,L`
  non-collinear in general either) — an acceptable basis for
  certification of the stated conditional result.
  **Certified `lemmas/isosceles-case-symmetry.md`** — this closes the
  round-1-flagged isosceles gap for the whole population.

**Verdict: real, valuable progress (a dead sub-route correctly retired; a
population-wide gap fully closed modulo one inherited assumption). No
overclaiming.** Status `partial` accurate (this file's own branch-selection
lever is now dead; the population's live branch-selection route is fully
handed to the sibling). **CHANGES REQUESTED** — no further immediate task
for this specific gap-2 lever, but the file stays live for any future
redirection.

## 3. `ptolemy-trig-identity` — CHANGES REQUESTED (partial)

**Claims checked:**
- Branch-selection theorem for (III)/(IV), Steps 2–3. Independently
  rebuilt the degree-2-homogeneity claim numerically (confirmed
  `G(ψ)=a_1\sin^2ψ+b_1\sinψ\cosψ+c_1\cos^2ψ` with the file's exact
  `a_1,b_1,c_1` formulas, residual `<10⁻¹⁶` at 5 random samples).
  Independently confirmed the required sign pattern (`c_1<0`,
  `G(0⁺)<0`, `G((C-θ)⁻)>0`) over **2000** random `(θ,A,C)` triangle-angle
  samples spanning the full valid domain, **zero exceptions**. The IVT +
  quadratic-degree-counting logic chain (existence via sign change, at
  most 2 roots since it's a genuine quadratic in `cotψ`, a real quadratic
  with ≥1 real root has exactly 2, an odd number of them in the
  sign-change subinterval forces exactly 1) is valid, complete reasoning
  with no gap — **this is a genuine, rigorous, general theorem**, not
  numerics dressed up as a proof (contrast with the coordinate route's
  still-numerical branch selection). Certified as new
  `lemmas/ptolemy-trig-branch-selection.md`.
- Step 4 (positivity of `F`). Confirmed the file is honest: explicitly
  labeled "verified... not proved symbolically," backed by 500,000
  samples with reported margin ≈11.3, with an explicit diagnostic
  (branch-choice sign dichotomy) also honestly labeled as checked
  numerically only. No overclaiming found — this is exactly the
  "prove, don't conjecture" line drawn correctly.
- Isosceles-case handoff: correctly notes the case was resolved by this
  round's ptolemy-lens explorer and written up (by
  `coordinate-bash-resultant`, per the outliner's redirect) rather than
  duplicating it here — consistent with the population's records.

**Verdict: real, rigorous new progress (a genuine branch-selection
theorem, independently verified), correctly and honestly reported
positivity gap.** Status `partial` accurate. **CHANGES REQUESTED** — the
sole remaining gap for a complete, independent solution via this route is
Step 4's positivity claim.

## Lemma certifications this round
- `lemmas/branch-crossing-locus-equals-angle-C.md` (new) — certified.
- `lemmas/branch-crossing-locus-equals-angle-B.md` (updated) — exactness
  claim now also certified.
- `lemmas/isosceles-case-symmetry.md` — certified (modulo the inherited
  `K≠L` non-degeneracy point).
- `lemmas/f3-f3prime-resultant-factors.md` (new) — algebraic
  identification and counterexample certified; "always harmless" claim
  explicitly left open/uncertified.
- `lemmas/ptolemy-trig-branch-selection.md` (new) — certified.

## Overall round outcome
No APPROVE this round (whole problem is not solved). All three built
approaches are honestly `partial`, each with real, independently-verified
progress and no overclaiming. `current.md` updated accordingly. The
population now has **two** largely-complete, structurally different
routes to a full solution, each down to a single well-isolated remaining
piece: (1) the coordinate/rotation-parametrization route, needing a
magnitude bound plus a general F3-crossing-is-harmless argument for branch
selection; (2) the independent Ptolemy-trig route, needing one explicit
symbolic positivity inequality. The isosceles edge case, open since round
1, is now fully resolved for the whole population.
