## imo-2026-02 (lens: Tgt symbolic push)

### Exact target reconstructed (from the approach file, rebuilt from scratch in sympy)
Setup: `X0(A,B) = sin(B)cos(A)/(2 sin(A+B))`, `beta0(A) = (pi-A)/3`,
`Kc = 2 sin(A) sin(A+B)`, `P = (1/2)sin(A-B) + (3/2)sin(A+B)`, `Q = -sin(A)sin(B)`,
`G(beta0) = Kc - P sin(beta0) - Q cos(beta0)`,
`RHS = (1+cos B)cos(beta0) - sin(beta0) G(beta0)`,
`D2 := d(RHS)/dB` (closed form, certified in the approach file — I re-derived it
independently, `sympy` residual 0, matches file's D2 exactly),
`T1' := (1+cos B)cos(A)/(2 sin²(A+B)) · [(1+cos B) sin A − 2 sin²B sin(A+B)]`
(the file's exact radical-free `T1` factorization — I independently re-verified
`T1 − T1' = 0` in sympy).

`Tgt(A,B) := 4(1+cos B)² X0 D2² − T1'²`. I built this literally from the pieces
above (own fresh sympy session) and confirmed it matches the file's boxed
formula.

### What I tried
1. **Direct sympy simplify/factor on Tgt(A,B)** — as the file reports, this
   produces a large expression (`beta0=(pi-A)/3` gives fractional-angle
   `sin(A/3+...)` terms) that does not visibly collapse under
   `simplify`/`trigsimp(method='fu')`/`factor`.
2. **Eliminate the fractional angle**: substituted `A = pi − 3·b0` (i.e. work
   directly in `b0=beta0` and `B`, since `beta0` **is** the natural variable —
   this removes all `A/3`-type arguments). This is a genuine simplification:
   `expand_trig` + `simplify` collapses Tgt from an unmanageable blob to a
   ~260-character closed form in `sin(b0),cos(b0),sin(B),cos(B)` (multiple-angle
   arguments `B±3b0, B±5b0, B±6b0, 3B−3b0`), with one clean visible factor
   `(4cos²b0 − 3)·cos(b0) = cos(3b0) = −cos(A)` pulled out. Still not a
   manifest SOS/positivity certificate — six-term trig-polynomial numerator,
   no single dominant term.
3. **Further substitution `B = 3b0 − C`** (using `C = pi−A−B`, and noting
   `3b0 = pi − A`, so `B − 3b0 = A+B−pi = −C`, i.e. `sin(A+B)=sin C` exactly —
   this identifies the mysterious `sin(B−3b0)` denominators with `sin C`,
   the natural angle). This re-expresses Tgt in `(b0, C)` — comparably
   compact (~390 chars) but not simpler than the `(b0,B)` form; no new
   cancellation found.
4. **Full Weierstrass rationalization** (`u=tan(b0/2)`, `v=tan(B/2)`,
   clearing all denominators to get a genuine bivariate polynomial
   `Num(u,v)>0`) — attempted via `sympy.rewrite(tan)` + `simplify`: **timed
   out after 2 minutes** (this is a real computational wall, not a triviality
   — the polynomial degree in `u,v` would be substantial, ~12 in each
   variable given the `sin(3b0)` triple-angle content). Did not attempt an
   SDP/SOS fit on this basis (ran out of budget before reaching a usable
   polynomial form) — this remains open for a future round with more time,
   ideally rescaling per rule 32 in `math-explorer.md` memory (Chebyshev
   basis, not raw monomials).
5. **Bounding/structural**: no simple termwise dominance found in the
   6-term compact form.

### The one genuinely new and useful finding: the global minimum is exactly the equilateral corner

Running a fresh global optimization (own script, Nelder-Mead ×300 restarts +
a 300,000-point domain-restricted random scan, own from-scratch domain
membership test rebuilt from the raw `X0,beta0` definitions — not reused
from the file) confirms the file's `min≈1.574` **and pins the exact
minimizer**: `(A,B) = (pi/3, pi/3)` **exactly** — i.e. the equilateral
triangle (`A=B=C=pi/3`), which is precisely the domain's already-known "far
corner" (where the boundary curve `C` meets `B=C`, per the file's own
"Round 13" numeric remark "attained near the domain's far corner
`(A,B)≈(1.047,1.047)`" — I confirm this is *exactly* `pi/3`, not merely
near it, and identify what happens there).

**At this exact point, `T1' = 0` identically** — a clean symbolic fact, not
just numeric coincidence. Proof: the bracket `(1+cos B) sin A − 2 sin²B
sin(A+B)`, evaluated at `B=(pi−A)/2` (i.e. on the boundary curve `B=C`),
simplifies (own sympy session) to `sin A − cos(A/2) − cos(3A/2) =
2cos(A/2)(sin(A/2) − cos A)` (sum-to-product), which vanishes exactly when
`sin(A/2) = cos A = sin(pi/2 − A)`, i.e. `A/2 = pi/2 − A` (principal
solution), i.e. **`A = pi/3` exactly** — matching the numeric minimizer
precisely, not approximately.

At `(A,B)=(pi/3,pi/3)`: `X0 = 1/4` exactly (also verified symbolically), so
`Tgt` **collapses to a pure square**:
`Tgt|_{corner} = 4·(1+cos(pi/3))²·(1/4)·D2² = (9/4)·D2²`,
with `D2|_{corner} = −sqrt(3)sin(5pi/18)/2 − [...]cos(5pi/18)/4` (a concrete
closed-form algebraic number in `cos(50°), sin(50°)`, since `beta0(pi/3) =
2pi/9 = 40°`), numerically `≈ −0.8364`, giving `Tgt|_{corner} ≈ 1.5741` —
matching the file's reported global minimum to 4 significant figures. This
is the *exact* value of the numeric minimum the file only reported
numerically.

### Why this matters for the outliner
This converts "prove `Tgt(A,B)>0` throughout the 2-variable domain `D`"
into two structurally much smaller sub-targets:
(a) **prove the corner `(pi/3,pi/3)` is where `Tgt` attains its global
minimum over the closed domain `D`** (a boundary/extremal-point argument —
e.g. via partial-derivative sign analysis pointing toward the corner, or a
convexity/monotonicity argument in each variable separately — NOT yet
attempted or proved this round, but now a concretely-targetable claim,
since the minimizer location is pinned exactly rather than merely
numerically), and
(b) **prove `Tgt` is strictly positive at that single point** — since
`Tgt|_{corner} = (9/4)D2(corner)²`, this reduces to proving `D2(corner)≠0`
(equivalently `D2(pi/3,pi/3)≠0`), a single concrete algebraic-number
nonvanishing claim (numerically `≈−0.836`, comfortably away from 0), far
easier than a full 2-variable inequality — e.g. provable via an explicit
rational interval bound on `sin(50°),cos(50°)` or via the minimal
polynomial of `cos(10°)`/`cos(pi/18)`.

Sub-target (a) is NOT proved and is the real remaining gap; it is a
genuinely different (and likely more tractable) shape of gap than the raw
`Tgt>0` inequality, since it is now "where is the extremum," not "is a
6-term trig blob positive everywhere."

### Cheap-kill / sanity checks
- Confirmed (own sympy) `T1'` is **not** identically zero along all of
  `B=C` — only at the single point `A=pi/3` — so this is a genuine isolated
  minimum structure, not a hidden identity making `T1'≡0` on a whole curve
  (which would have been an even bigger simplification but is false).
- The corner is exactly the "far corner" of `D` already referenced by the
  file (`A_max ≈ pi/3`, where the curve `C` meets `B=C`) — consistent with,
  not contradicting, prior rounds' domain characterization.

### Candidate technique(s) for the outliner
- Attack sub-target (a) via a monotonicity/boundary argument (e.g. show
  `∂Tgt/∂A ≥ 0` as `A→A_max` at fixed admissible `B`, or a Lagrange/KKT-style
  argument that the unconstrained gradient of `Tgt` never vanishes in the
  interior of `D`, forcing the min to the boundary, then a 1-variable
  argument along `B=C` toward `A=pi/3`).
- Sub-target (b): direct numeric-to-rigorous conversion (interval
  arithmetic / minimal polynomial of `cos(pi/18)`) — should be quick once
  targeted.
- The Weierstrass-polynomial route (item 4 above) remains available for a
  future round with more compute budget; per `math-explorer.md` rule 32,
  rescale variables before any SDP/SOS attempt.

### Knowledge-base entries
Not directly consulted this round (pure computational/algebraic push per
dispatch); the relevant machinery is internal to this approach's own
certified lemmas (`lemmas/f-minus-g-reduction-and-t1-factorization.md`,
`lemmas/rhs-partial-b-derivative-and-decomposition.md`).

### Dead ends (do not retry as-is)
- Blind `sympy.simplify`/`factor` on the raw `A,B`-form of `Tgt` (fractional
  `A/3` angles obscure structure) — retry only after the `b0`-substitution.
- Full `sympy.rewrite(tan)` Weierstrass rationalization on the `b0,B`-form
  in one shot — times out at 2 minutes; needs a more targeted/staged
  substitution (build the polynomial by explicit triple-angle substitution
  into `u=tan(b0/2)` term-by-term, not a blind `rewrite`).

### Prior progress (unchanged from file)
`Tgt(A,B)>0` on `D`, strong numeric margin `≈1.574` (now pinned exactly to
the equilateral corner `(pi/3,pi/3)`), still not proved symbolically. The
sibling `D1(A)≥0` on `C` gap is untouched by this round's work.
