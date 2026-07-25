## imo-2026-02

All four fields below share the already-proven backbone (central identity
`O·(C−B)=(|C|²−|B|²)/4` fully general, isosceles case closed, branch
selection reduced via the coordinate/rotation parametrization to Case (b)
of Theorem 16.2). They differ only in the mechanism attacking the single
remaining shared target. Per this round's dispatch: no new top-level
framing (4 independent searches, rounds 3/5/8/10, found none) — all four
entries below are revise/advance/copy on the two live coordinate-route
siblings.

---

coordinate-bash-resultant-boundary-pointwise: revise
Target: OM = ON for every triangle ABC (the whole problem), via the
coordinate/rotation-parametrization route, culminating in closing the
sole remaining gap `(⋆): (1+cos B)²X₀ ≥ RHS²` on the entire Case-(b) domain.
Technique: degenerate-limit (domain-width) Taylor expansion at the
identified codimension-2 corner, per this round's star-lens/technique-lens
findings — a genuinely different mechanism from the already-used MVT/
Lipschitz reduction (that produced `(⋆)` itself) and from raw global SOS
(refuted, round 6, on the related Ψ target; and `(⋆)`'s own naive
domain-width bound already refuted round 10).
Skeleton:
  1. [inherited, certified] Central identity, genericity, isosceles case,
     magnitude bound, all branch-selection sub-lemmas up through
     `lemmas/mvt-lipschitz-reduction-case-b.md` — reduce the WHOLE problem
     to `(⋆)` on Case (b)'s domain `{(A,B): A,B>0, A+B<π}` restricted to
     where Case (b) applies (`sin(A+3β1)<0`, i.e. `β1>β0`).
  2. **New Step (this round): locate and verify the local structure of the
     tight corner.** The corner is the codimension-2 point solving the
     SIMULTANEOUS system `{B=(π−A)/3 (i.e. γ=β0), G(β0(A))=0}` — confirmed
     this round (star-lens) at `A*≈0.40638, B*≈0.91174` via `mpmath.findroot`
     to machine precision, and confirmed (technique-lens) that the naive
     single-equation boundary curve `γ=β0` alone is NOT the tight locus
     (large positive AND negative `(⋆)`-slack values occur along it away
     from `A*`). First: numerically fit the local Hessian of
     `(1+cos B)²X₀ − RHS²` at `(A*,B*)` (finite differences, no symbolic
     work yet) to determine whether it is a genuine smooth local minimum
     (PSD Hessian) or a more subtle degenerate (e.g. saddle-along-a-curve)
     structure — this determines whether a plain local Taylor/PSD argument
     can possibly work before committing to the symbolic version.
  3. **If PSD (this round's primary bet): reparametrize by
     `w := γ − β0` (domain width, → 0 at the corner) and
     `θ := (β1 − β0)/w ∈ (0,1)` (position within the shrinking interval).**
     Expand `(1+cos B)²X₀ − RHS²` in powers of `w` at fixed `θ` and the
     limiting angle data (i.e. expand around `A=A*` jointly, since `w→0`
     and `A→A*` together define the corner — NOT a 1-variable expansion in
     `w` alone at generic `A`). Show: (i) the zeroth-order (in `w`) term is
     `≥0` for every `A` in the domain and vanishes only at `A=A*` (reduces
     to a genuine 1-variable trig inequality in `A` alone, since at `w=0`,
     `β0=β1=γ` collapse and all quantities become closed forms of `A`
     only); (ii) the first-order term in `w` is `≥0` (or the whole
     expression is manifestly a sum of a nonnegative `A`-dependent term
     plus a nonnegative `w`-dependent correction) — establishing global
     nonnegativity via the local expansion plus a separate global argument
     that the function doesn't dip negative away from the corner (reuse
     the already-certified 300k-sample zero-violation numerics as a
     consistency check, not a substitute for the symbolic bound).
  4. **Fallback mechanism (if Step 3 does not close cleanly): tangent-line
     trick pinned at the corner, keeping `A*` implicit.** Per crux
     `aimo-0005` (adapted, not cited as authority): construct a linear
     lower bound for the harder side (e.g. `X₀` or `cos²β0`) in a
     convenient variable (`cos A` or `t = B − β0`) that is exact at the
     corner and one-sided elsewhere, using the DEFINING EQUATION
     `G(β0(A*)) = 0` as an algebraic hypothesis rather than ever solving
     for `A*` in closed form (since `A*` is transcendental, not
     constructible) — then verify the resulting bound reduces `(⋆)` to a
     polynomial/rational inequality provable by direct factoring or a
     Sturm-sequence sign count on the reduced quantity.
  5. Conclude: `(⋆)` holds on all of Case (b) ⟹ `G(β1)≥0` on all of
     Case (b) ⟹ the coordinate route's own branch-selection Case-(b) gap
     is fully closed ⟹ (combined with the already-closed backbone) the
     whole problem OM=ON is proved for every triangle.
Key lemmas (claim + mechanism):
  - The tight-corner system `{B=(π−A)/3, G(β0(A))=0}` pins a UNIQUE
    codimension-2 point — because `G(β0(A))` is (per certified closed
    forms) a real-analytic function of `A` alone on the curve `γ=β0`, and
    numerics (this round, `findroot`) show a single sign change / simple
    root at `A*≈0.40638`.
  - IF the Hessian at `(A*,B*)` is PSD: `(⋆)` follows from a local Taylor
    argument PLUS a global "no other dip" argument — because a smooth
    function on a compact-closure domain with one interior critical point
    where it vanishes, PSD there, and strictly positive on the (compact)
    boundary and away from the corner, attains its infimum only at that
    point (Extreme Value Theorem, `knowledge_base.md`'s EVT/compact-domain
    entry).
Open gaps: the Hessian check itself (Step 2) is not yet done; the
Taylor-expansion argument (Step 3) is not yet carried out even after the
Hessian check; the tangent-line fallback (Step 4) is a genuinely untried
mechanism, not yet attempted at all.
Cases to cover: PSD-Hessian branch (Step 3) vs. non-PSD/degenerate branch
(would require the tangent-line fallback, Step 4, or a case-split
argument the builder must design if Step 2's numeric check comes back
negative).
Watch out for: the corner is a SIMULTANEOUS two-equation system, not a
single boundary curve — technique-lens explicitly found the single-curve
version false (`γ=β0` alone gives both signs away from `A*`); any
expansion must hold `A→A*` and `w→0` together, not treat them as
independent perturbations. Also: `A*` has no known closed form — any
symbolic argument must keep it implicit (defined by its equation), never
substitute a decimal.

---

coordinate-bash-resultant-boundary-pointwise-sos: copy-of coordinate-bash-resultant-boundary-pointwise
Target: same as above — OM=ON for every triangle, via closing `(⋆)` on
all of Case (b).
Technique: SOS-after-triple-angle-clearing, a genuinely different
mechanism from the width-expansion above — algebraic (polynomial-ring)
rather than analytic (local-expansion) — run in parallel per this round's
star-lens/technique-lens recommendation (round 10 tried this substitution
route only briefly and it "resisted simplify/factor in the time
available," i.e. stalled, not refuted).
Skeleton:
  1-1(inherited). Same backbone reduction to `(⋆)` as the sibling.
  2. **New Step: clear all trig via an explicit `cos(A/3), sin(A/3)`
     polynomial basis (NOT `tan(β/2)`).** Since `β0 = (π−A)/3` exactly,
     `cos β0, sin β0` are cubics in `cos(A/3), sin(A/3)` via the
     triple-angle formulas (`cos A = 4cos³(A/3) − 3cos(A/3)`, etc.) — use
     this explicit substitution (not the mixed `tan(β/2)` form that
     stalled `sympy.simplify` in round 10) to rewrite `X₀, RHS` as
     rational functions of `x := cos(A/3)` (with `sin(A/3) = √(1−x²)`
     appearing only to even powers after squaring, since `(⋆)` is already
     one clean squaring away from radical-free) and of `B` directly.
  3. Attempt `sympy.factor`/`Poly.is_zero` on `(1+cos B)²X₀ − RHS²` in this
     new polynomial ring; if that stalls, numerically fit a Gram-matrix
     PSD certificate at a grid of sample points (own script) and then
     attempt to verify the resulting SOS decomposition symbolically term
     by term.
  4. If a genuine SOS decomposition (sum of squares, possibly with
     positive-coefficient monomial multipliers using known-positive
     quantities like `sin A, sin B, 1+cos B`) is found, this directly
     proves `(⋆)` unconditionally — no case split, no corner-locality
     argument needed at all (stronger than the sibling's local approach if
     it succeeds).
  5. Conclude as in the sibling's Step 5.
Key lemmas (claim + mechanism):
  - `(⋆)` becomes a genuine two-variable polynomial (or ratio of
    polynomials with a manifestly positive denominator) inequality in
    `(x, B)` — because triple-angle clearing removes ALL residual
    dependence on `A/3` as a transcendental angle, replacing it with an
    algebraic variable `x=\cos(A/3)\in(\cos(π/6),1)` (bounded interval
    matching `A\in(0,π/2)`).
Open gaps: whether the polynomial-ring inequality actually admits an SOS
certificate is completely open — this is a genuine attempt, not a proven
reduction; may fail to terminate or may find no PSD Gram matrix, in which
case this copy is a documented negative result (still valuable) rather
than a closure.
Cases to cover: none beyond the single global inequality (this is the
"strong form" attempt — if it works, no case split is needed at all,
unlike the sibling's PSD/non-PSD branch).
Watch out for: `sympy.factor` stalling silently for a long time on
high-degree multivariate polynomials — cap attempts and fall back to a
numeric Gram-matrix fit (least-squares PSD, e.g. via `scipy` or `cvxpy` if
available) before declaring failure; do not spend the whole round on one
non-terminating `simplify` call.

---

coordinate-bash-resultant-boundary-pointwise-tangent: copy-of coordinate-bash-resultant-boundary-pointwise
Target: same as above — OM=ON for every triangle, via closing `(⋆)` on
all of Case (b).
Technique: the tangent-line trick (crux `aimo-0005`, adapted) applied
directly and independently (not merely as this round's fallback inside
the width-expansion approach) — bound one troublesome factor (`X₀` or
`cos²β0`, whichever is more tractable) below/above by a line tangent at
the transcendental corner, engineered so the bound is provably one-sided
using ONLY the corner's DEFINING EQUATION (`G(β0(A*))=0`) as an algebraic
hypothesis, never solving for `A*` numerically.
Skeleton:
  1. [inherited] Same backbone reduction to `(⋆)`.
  2. **New Step: identify which single factor to linearize.** Candidates:
     `X₀ = sin B cos A/(2 sin(A+B))` (as a function of `A` at fixed `B`,
     or vice versa) or `cos²β0` (as a function of `A` alone, since
     `β0=(π−A)/3`). Choose the one whose tangent-line bound, substituted
     into `(⋆)`, produces the SIMPLEST resulting inequality (test both by
     direct symbolic substitution before committing).
  3. Construct the tangent line `L(A) := X₀(A*,B) + X₀'(A*,B)·(A−A*)` (or
     the analogous construction for `cos²β0`), and prove `X₀(A,B) ≥ L(A)`
     (or `≤`, whichever direction the corner's local behavior requires,
     informed by the sibling's Hessian check if available) for all `A` in
     the domain — using ONLY algebraic manipulation plus the hypothesis
     `G(β0(A*))=0` (never substituting `A*≈0.40638` as a decimal; treat it
     as "the root of `G∘β0`" symbolically throughout).
  4. Substitute the tangent bound into `(⋆)` and check whether the
     resulting (now one-sided-linearized) inequality is provable directly
     (e.g. reduces to a manifestly nonnegative combination once `A*`'s
     defining equation is invoked to cancel the corner term exactly, the
     hallmark of a correctly-pinned tangent-line construction per
     `aimo-0005`'s pattern).
  5. Conclude as in the sibling's Step 5.
Key lemmas (claim + mechanism):
  - A tangent line pinned exactly at the (implicit) corner, using the
     corner's own defining equation as a substitutable identity, converts
     a transcendental two-variable inequality into an algebraic one — the
     `aimo-0005` mechanism: equality at the pinned point is automatic (by
     construction of the tangent), and one-sidedness elsewhere follows from
     a single convexity/monotonicity check on the linearized factor, not a
     re-derivation of the whole global inequality.
Open gaps: which factor to linearize (Step 2) is undetermined without
trying both; the sign/direction of the tangent bound is undetermined
without either the sibling's Hessian result or independent local analysis;
the final algebraic verification (Step 4) is entirely open.
Cases to cover: two candidate linearization targets (`X₀` vs `cos²β0`) —
try both, keep whichever succeeds or yields more information.
Watch out for: a tangent-line bound that is one-sided only LOCALLY near
the corner but false globally (the same failure mode that already killed
the cruder "domain-width" bound, round 10) — any claimed one-sidedness
must be checked (numerically first, then symbolically) over the WHOLE
Case-(b) domain, not just near `A*`.

---

coordinate-bash-resultant-boundary: advance
Target: same overall problem (OM=ON for every triangle), via closing the
narrower residual `T≥0` on the sub-case `P>0 ∧ E<0` (≈4.5% of Case (b)) —
kept alive in parallel to the `(⋆)`-based siblings since it is a smaller,
possibly cheaper target even though `(⋆)` (if proved) would subsume it.
Technique: restrict the already-attempted linear-combination-of-`q1,r0`
search to the TRUE sub-case (not the full `(A,B)` square) — a cheap,
previously-unchecked lever flagged explicitly by this round's star-lens
explorer (the 1.5M-sample sweep showing "no sign-definite combination"
was run on the FULL domain, not restricted to `P>0∧E<0`).
Skeleton:
  1. [inherited] Backbone reduction to `T = c(dQ1−cR0)/(4sin²(A+B))`,
     `Q1,R0` explicit polynomials in `σ=sin²A,τ=sin²B`
     (`lemmas/case-b-e-lt-0-t-factorization.md`), with `c,d,s,t` explicit
     sign-known prefactors — so `T≥0` on `P>0∧E<0` reduces to a sign claim
     on `dQ1 − cR0` (equivalently a combination of `q1,r0`) restricted to
     the exact sub-region where `P>0∧E<0` (closed forms available from
     `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`).
  2. **New Step: re-run the numeric sign-combination sweep restricted to
     the TRUE `P>0∧E<0` region** (using the exact `P,E` formulas, not just
     the full unit square) — check whether `q1, r0`, or a simple linear/
     bilinear combination, becomes sign-definite once properly scoped
     (flagged this round as untested; the existing 1.5M/2M-sample negative
     results were NOT restricted this way).
  3a. If Step 2 finds a sign-definite combination: prove it symbolically
      (Sturm-sequence sign-count on the 2-variable region `(σ,τ)`, per
      technique-lens's suggestion, or direct algebraic factoring if the
      combination turns out to have a recognizable closed form) — this
      would close the WHOLE problem via this smaller-scope route,
      independent of whether the `(⋆)`-based siblings succeed.
  3b. If Step 2 still finds no sign-definite combination even restricted:
      report this as a genuine (narrower, more precise) negative result —
      still valuable, narrows the search space for any future attempt at
      this specific residual, and confirms `(⋆)` (not `T≥0`) is the
      correct priority target for this route.
Key lemmas (claim + mechanism):
  - If a sign-definite combination exists once restricted to `P>0∧E<0`, it
    would be because the extra constraints `P>0,E<0` (each an explicit
    polynomial-sign condition on `σ,τ` per the certified factorizations)
    carve out a sub-region where `q1,r0`'s individually-varying signs
    become correlated — the mechanism is a genuine domain restriction, not
    a new algebraic identity.
Open gaps: entirely open — this is a fresh (cheap) numeric check followed
by, contingent on its outcome, either a symbolic sign proof or a documented
negative result.
Cases to cover: 3a (positive) vs 3b (negative) branches of Step 2's
outcome, both must be reported honestly.
Watch out for: do not reuse the existing `q1>0`-25.6%/`r0>0`-54.8%
full-domain sign census as if it already answers this — those samples were
NOT filtered to `P>0∧E<0`; the restricted census must be run fresh with the
exact `P,E` closed forms from the certified lemma, otherwise the "cheap
unchecked lever" this round's explorer flagged is not actually being
checked.

build set: coordinate-bash-resultant-boundary-pointwise, coordinate-bash-resultant-boundary-pointwise-sos, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary
