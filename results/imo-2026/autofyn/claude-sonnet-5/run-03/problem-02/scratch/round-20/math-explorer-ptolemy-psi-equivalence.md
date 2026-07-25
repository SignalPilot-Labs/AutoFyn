## imo-2026-02

### 1. Exact statement of `Ψ>0` (ptolemy-trig-identity route)

Setup (triangle angles A,B,C; θ:=∠KBA=∠ACL is a genuine **free real parameter**
ranging over `0<θ<min(B,C)` for fixed A,B,C — this is the ptolemy route's one
degree of freedom describing the whole family of valid (K,L) configurations).
Write `τ:=tanθ`. Certified in `lemmas/ptolemy-resultant-elimination-to-sextic.md`:

```
P1 = sinA·τ(τcosC − sinC),  Q1 = sinA sinC(τ²+1) + 2τ sinB,
R1 = −2τ²sinC cosA − τ sinA sinC + sinA cosC        (and P2,Q2,R2 = same with B↔C)
m := sinA·U − cosA,  n := −cosA·U − sinA − 4
Φ(U) := P2·n² − Q2·n·m + R2·m²
Res_U(P1U²+Q1U+R1, Φ) = sin²A·(τcosC−sinC)(sinB−τcosB)·Ψ(τ,A,C)
```

`Ψ` is an explicit degree-6-in-`τ` polynomial with trig coefficients in A,C
(B=π−A−C eliminated). `Ψ(0,A,C)=4sin³A sinB sinC>0` is the one point proved
exactly. The two linear cofactors are strictly signed on the domain (proved),
so **`Ψ(τ,A,C)>0` for all `0<θ<min(B,C)`, all valid A,B,C** is, by the file's
own reduction chain (Lemmas R, Q1, Red, S1–S4, the general-Ptolemy-equality
theorem, the branch-selection theorem), **equivalent to `α+α'<A`**
(`α=∠BAK,α'=∠CAL`), which is **the single remaining gap for the ENTIRE
ptolemy-trig-identity route** — i.e. closing `Ψ>0` finishes that whole proof
of OM=ON (modulo the shared, separately-handled isosceles case AB=AC). This is
confirmed by `approaches/ptolemy-trig-identity-synthetic.md` (round 5/16),
an independent copy dispatched specifically at this same gap via synthetic
(auxiliary-circle, cross-product) methods — it reduces to the identical wall
and stayed open through round 16, at which point the outliner explicitly
noted three independent reformulations (radical-clearing sextic, synthetic
cross-product, parity-decomposition) all converge on the same `Ψ>0`-type
polynomial obstruction.

I independently re-built `Ψ` numerically (fresh `numpy`, own resultant-via-
roots evaluation, not copying any file's script) at 6 random domain points
(A,C random, θ random in `(0,min(B,C))`) and got Ψ ∈ {3.13, 3.36, 5.34,
18.0, 108.7, 335.0} — always positive, consistent with the population's
20,000+/2,000+-sample sweeps (this is a **conjecture**, not a proof).

### 2. Exact statement of `T≥0` / `−q1,−r0` (coordinate-bash-boundary family)

From `lemmas/case-b-p-le-0-and-e-ge-0-closed.md` + `case-b-e-lt-0-t-factorization.md`:
this is the residual sub-case (`P>0 ∧ E<0`) of Case (b) of the `G(β1)≥0`
target, where `β1 := arccos(√X0)` is **not a free parameter** — it is
*determined* by `X0(A,B) := sinB cosA/(2sin(A+B))`, a function of the
triangle shape alone. With `s=sinA,c=cosA,t=sinB,d=cosB,σ=s²,τ=t²`:

```
T := Bc²X0 − E² = c(d·Q1 − c·R0)/(4sin²(A+B)),   Q1 = −4st·q1(σ,τ),  R0 = r0(σ,τ)
q1 = 512σ⁴τ² − 512σ⁴τ + 96σ⁴ − 928σ³τ² + 856σ³τ − 144σ³ + 506σ²τ² − 392σ²τ + 48σ²
     − 85στ² + 40στ + 3τ²
r0 = 2048σ⁴τ³ − 3072σ⁴τ² + 1152σ⁴τ − 64σ⁴ − 2688σ³τ³ + 3744σ³τ² − 1248σ³τ + 64σ³
     + 936σ²τ³ − 1092σ²τ² + 240σ²τ − 80στ³ + 60στ² + τ³
T≥0 ⟺ c=0 or 4dst·q1(σ,τ) + c·r0(σ,τ) ≤ 0
```

Domain: `(σ,τ)=(sin²A,sin²B) ∈ (0,1)²` subject to `A≤π/2` and the standing
triangle constraints — a **2-real-parameter** (A,B only) target, no extra
free angle. Neither `q1` nor `r0` has a fixed sign alone (each is positive on
~25–55% of the box); the target is the joint sign of `4dst·q1+c·r0`.

### 3. Are `Ψ>0` and `T≥0` the same inequality in disguise? **No — different objects, checked structurally, not literally equivalent.**

Key structural facts, cross-checked from the raw definitions in both families:

- **Dimension count differs.** `Ψ(τ,A,C)>0` must hold on a genuinely
  **3-real-parameter** domain (θ free, plus A,C determining the triangle
  shape — θ ranges over an open interval for *every* fixed shape). `T≥0`
  is stated on a **2-real-parameter** domain (A,B only) — `β1` in this
  sub-case is *pinned* to a specific function `X0(A,B)` of the shape, not
  a free angle. A target that must hold on a 3-parameter family cannot be
  literally the same polynomial identity as one on a 2-parameter slice
  (a dimension mismatch, not just cosmetic variable-naming).
- **The variable-name collision is a coincidence, not a clue.** Both routes
  independently used the letter `τ` for an unrelated quantity: ptolemy's
  `τ:=tanθ` (a ranging trig value of the *free angle*), coordinate-bash's
  `τ:=sin²B` (a fixed function of the *triangle shape*). Checked: swapping
  in either convention does not make the two polynomials' coefficient
  patterns line up (Ψ's coefficients are transcendental in A,C via
  `sinA,cosA,sinC,cosC`; q1,r0 are honest rational polynomials in σ,τ with
  no further trig dependence) — Ψ genuinely retains an extra free variable
  (θ) that q1,r0 simply do not have.
- **They arise from unrelated case-splits in unrelated global framings.**
  Ψ is the *sole* remaining gap of an entirely different top-level proof
  strategy (the K,L/Ptolemy-equality construction reducing OM=ON to one
  clean concyclicity fact). `T` is one leaf of coordinate-bash's own nested
  case tree (Case (b), sub-case `P>0∧E<0`) — and (round 19) the *same* `T`
  was independently found load-bearing for Case (a) too, but that is a
  convergence **within** the coordinate-bash family (two of its own cases
  reduce to the same polynomial), not a link to Ψ.
- **Conclusion:** these are genuinely different sub-targets from
  independent reductions of the same underlying geometric problem — not
  a shared disguised inequality. Closing either one would independently
  make progress; there is no known substitution turning one into the other
  (and the dimension mismatch makes such a substitution structurally
  implausible, though I did not attempt an exhaustive search for a
  degenerate-slice correspondence, e.g. "does Ψ at some special θ(A,B)
  reduce to T" — this is conceivable but unproven and not suggested by
  any existing file).

### 4. Is `Ψ>0` more tractable, and is there a new lever?

**Why Ψ is the higher-value target to prioritize:**
- Closing `Ψ>0` alone completes an *entire independent proof route*
  (ptolemy-trig-identity), whereas closing `T≥0` closes only one leaf of
  coordinate-bash's multi-case tree (other open sub-targets — the
  Case-(a) `f>0`-on-full-interval chain, gap 6/7 bookkeeping — sit in the
  same family and would still need auditing even if `T` fell).
- `Ψ>0` has a genuinely clean **equivalent restatement already proved**
  (Step 4 of `ptolemy-trig-identity.md`, round 4): `Ψ>0 ⟺ α+α'<A ⟺
  F(p,x,y):=sinA(p+2x)(p+2y) − sinA − cosA(2p+2x+2y) > 0` where
  `p=cotθ, x=cotψ, y=cotφ` are cotangents of three angles of the actual
  triangle-decomposition (θ,ψ,φ are honest sub-triangle angles, all in
  `(0,π)`), constrained by two certified quadratics ((III)′,(IV)′, Step 2)
  pinning `x=cotψ,y=cotφ` as roots of explicit quadratics in `p=cotθ` and
  the fixed angles. This is a **3-cotangent symmetric-in-(x,y) bilinear
  form** — a much more recognizable shape than `T`'s raw degree-(4,3)
  bivariate polynomial mess in `(σ,τ)=(sin²A,sin²B)`.
- The `F>0` form is a genuine candidate for a **Cauchy–Schwarz / AM-GM on
  cotangents** or a **tangent-line / SOS-in-(cotψ−cotφ)** approach: since
  `x,y` are each roots of an explicit quadratic (Step 2), `x+y` and `xy`
  are known symbolically (Vieta), so `F>0` reduces further to a purely
  **algebraic (no more trig, no more root-finding)** inequality in the
  Vieta symmetric functions of the two quadratics plus `p`. This reduction
  is *sitting unexploited* — no approach file has yet substituted Vieta's
  formulas from Step 2's quadratics into `F` to eliminate x,y entirely in
  favor of `p` and the fixed angles A,B,C. This is a concrete, cheap next
  lever: turn `F(p,x,y)>0`, given `c1x²+b1x+a1=0` and `c2y²+b2y+a2=0`
  (both certified, Step 2), into a **resultant/Vieta elimination of x,y**,
  producing a target purely in `p=cotθ` (1 free variable) and A,B,C — the
  same style of reduction that has worked repeatedly elsewhere in this
  population (memory rule 8/9/13), but *not yet tried on Ψ/F itself*
  (the existing resultant route went through `U=cotα` instead, producing
  the transcendental-coefficient `Ψ(τ,A,C)`; eliminating via `x,y` directly
  from `F`'s own quadratic form may give a cleaner low-degree-in-`p` target).

**Crux corpus check.** Filtered `algebra`/`inequalities-SOS-and-convexity`
(149 cruxes) and keyword-searched (`sin`,`cos`,`triangle inequality`,
`acute triangle`,`trigonometric`) across all 2434 cruxes. **No genuinely
analogous crux found.** The geometry domain is explicitly absent from the
corpus (per `crux_moves_documentation.md`), and every keyword hit
(`aimo-0159`, `aimo-0355`, `aimo-0527`, `aimo-0824`, `aimo-0861`, etc.) is
either pure number-theory/algebra with trig incidental (e.g. Chebyshev
polynomials, root-of-unity coefficient arguments, telescoping sine sums) —
none involves a triangle-angle-parametrized rational/trigonometric
Positivstellensatz of this shape. Do not force a match; report honestly
that this specific lever (Vieta-elimination-then-SOS on `F(p,x,y)`) is not
crux-corpus-derived, it is a direct extension of this population's own
memory-rule-8-style technique.

### Summary table

| | `Ψ>0` (ptolemy) | `T≥0` (coordinate-bash) |
|---|---|---|
| Free params | θ (free), A,C (shape) — 3 real dof | A,B (shape) only — 2 real dof |
| Role | sole remaining gap, whole route | one leaf of a nested case tree |
| Form | degree-6-in-τ=tanθ, trig coeffs in A,C | degree-(4,2)/(4,3) rational poly in σ=sin²A,τ=sin²B |
| Equivalent form | `F(p,x,y)>0`, p,x,y cotangents, x,y roots of two quadratics (Vieta-ready) | `4dst·q1+c·r0 ≤ 0`, no simpler symmetric form found |
| Verdict | different object from T; more tractable-looking (lower effective dimension once x,y eliminated via Vieta; higher payoff) |

## Recommendation for outliner
Treat `Ψ>0`/`T≥0` as **two independent, unrelated open sub-targets**, not
one gap in two guises — do not merge or "solve one to get the other" in
the outline. Prioritize a **new build** on the ptolemy-trig-identity route:
substitute Step 2's Vieta relations for `x=cotψ,y=cotφ` into `F(p,x,y)`
(certified boxed formula, round 4) to eliminate x,y symbolically, producing
a 1-free-variable (`p=cotθ`) target in A,B,C — untried by any approach file
so far — as a genuinely new, cheap lever distinct from the already-exhausted
radical-clearing/resultant-to-Ψ route and the exhausted synthetic
auxiliary-circle route.
