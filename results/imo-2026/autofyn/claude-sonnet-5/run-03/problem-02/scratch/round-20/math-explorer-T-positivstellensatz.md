## imo-2026-02 — lens: attack the T≥0 / -q1,-r0 gap directly (new technique)

### 1. Exact restatement of the target

Setup (from `lemmas/case-b-e-lt-0-t-factorization.md` and
`case-b-p-le-0-and-e-ge-0-closed.md`): for a triangle with `A≤π/2`, WLOG
`B≤C` (so `γ=B`), Case (b) (`Y(γ)<0`) restricted further to the residual
sub-case `P>0∧E<0`, the needed fact `G(β1)≥0` is *exactly equivalent* (an
honest iff, via two successive valid squarings since all quantities
squared have known sign) to

  `T := Bc²·X0 − E² ≥ 0`,

with `Bc=2K sinA sinB`, `K=2 sinA sin(A+B)`, `P=½sin(A−B)+3/2 sin(A+B)`,
`X0=sinB cosA /(2 sin(A+B))`, `Ac=sin²A sin²B+P²`, `Cc=K²−P²`,
`E=Ac·X0+Cc`. `T` factors exactly (certified) as
`T = c(dQ1−cR0)/(4 sin²(A+B))`, `Q1=−4st·q1(σ,τ)`, `R0=r0(σ,τ)`,
`σ=sin²A,τ=sin²B`, with `q1,r0` the explicit degree-(4,3) polynomials
displayed in `case-b-e-lt-0-t-factorization.md`. So `T≥0 ⟺ c=0` or
`4dst·q1+c·r0 ≤ 0`.

**Important correction / sharpening found this round: the true domain is
narrower than "P>0∧E<0∧Case(b)".** The full exact Case-(b) domain
(from `coordinate-bash-resultant-boundary-pointwise-tangent.md`,
"Exact Case-(b) domain") is
`D := {0<A≤π/2, 0<B≤C=π−A−B, B>β0(A), cos²B < X0(A,B) < cos²β0(A)}`,
`β0(A)=(π−A)/3`. **The upper bound `X0<cos²β0(A)` is essential** — I
verified numerically (own fresh `numpy` sweep) that if this upper bound is
dropped (keeping only `cos²B<X0`, `P>0`, `E<0`), `T` becomes hugely
negative (down to `T≈−1/4` as `A→0⁺`, and still `T≈−0.15` at `A=0.3`,
`B≈0.887`) — a large, non-degenerate violation, NOT a boundary artifact.
Once the correct upper bound is restored, this violation disappears
entirely: a `1500×2000`-point dense sweep of the *correctly restricted*
domain `D∩{P>0,E<0}` (`≈46,000` domain points) finds `T>0` everywhere
except a global minimum `T_min ≈ 5×10⁻⁴` at `(A,B)≈(0.40663,0.91188)` —
**no violation found**. (This resolves what could otherwise look like a
counterexample; flagging it explicitly since it is easy to mis-scope the
domain and conclude `T≥0` is false — it is a genuine, tight fact, not
false.)

### 2. Why the Gram-matrix degeneracy recurs: it is structural, not a solver artifact

**New finding (high-precision `mpmath`, 50 digits, then symbolic `sympy`
confirmation to 166 digits):** the global minimum of `T` over the true
domain `D` is attained *exactly* at the corner where the domain itself
degenerates (its lower cutoff curve `B=β0(A)` is approached), at
`A* = 3·arcsin(√6/4) − π/2 ≈ 0.406378`, `B* = β0(A*) = (π−A*)/3 ≈
0.911738` — **the identical corner point already established in round
17/18's `lemmas/d1-nonnegative-on-boundary-curve.md`** (same closed form
for `A*`, independently re-confirmed here from a *different* starting
polynomial, `T`, not `D1`). At this point:

  `T(A*, β0(A*)) = 4.34×10⁻⁵¹ ≈ 0` (50-digit `mpmath`, effectively exact),

and, remarkably, **`X0(A*,β0(A*)) = cos²(β0(A*)) = 3/8` exactly** — a
clean rational value. Symbolic check (`sympy`): `g(A):=X0(A,β0(A)) −
cos²(β0(A))` simplifies to `−sin²(A/3+π/6) + cos(A)cos(A/3+π/6)/(2
sin(2A/3+π/3))`, and substituting the closed-form `A*` gives `0` to 166
displayed digits (`sympy.N`), and `X0` there evaluates to exactly
`0.375000...` (166 digits) — i.e. `X0=3/8` is very likely an *exact*
algebraic identity at `A*`, not numerical coincidence (worth a short
resultant/`gcd`-based symbolic proof, in the same style as round 17-18's
recommendation for the `D1` corner — this looks tractable given the clean
rational target value `3/8`).

**Order of vanishing (new numerical experiment, own script):** perturbing
`A=A*+ε` and re-minimizing `T` over the (now nonempty, shrinking) domain
slice near the corner gives `T_min(ε)/ε ≈ 1.87–2.14` (roughly constant)
for `ε∈{10⁻²,...,10⁻⁵}` — i.e. **`T` vanishes to first order (linearly),
not as a tangential double root**, as `A→A*⁺` along the domain's active
boundary curve `B=β0(A)`. This is the classic signature of a
**boundary-active constraint** (the domain shrinks to width `0` exactly
at this corner, and `T→0` linearly as the corner is approached along the
domain's own edge) — **not** an interior critical point of a smooth
unconstrained positivity problem. This exactly matches, and explains, the
round-16/18 diagnosis ("complementary slackness at an active boundary
constraint `n1=0`"): **any valid global Positivstellensatz/SOS
certificate for `T≥0` (or `-q1,-r0`) must itself vanish at this exact
point** (since `T(A*,B*)=0` and the certificate equals `T` there), which
forces the moment/evaluation vector at `(A*,B*)` into the kernel of every
Gram matrix in the decomposition — a structural, unavoidable rank
deficiency, reproducible at any degree, not a numerical/solver artifact.
This is worth stating explicitly to the outliner: **stop treating the
near-null eigenvalue cluster as something to "fix" by better solvers or
rational rounding — it is mathematically forced by the fact that `T=0` is
attained (not just approached) at a genuine domain corner.**

### 3. New technique tried (not in the prior list): reduce to the already-successful LOCAL near-corner method

Since `T`'s (and hence `G(β1)`'s) tightness is concentrated at the *same*
corner `(A*,B*)` where `D1` (round 17-18) and `Tgt` (round 16) were both
already closed — by a **local** Taylor-expansion + certified
Lagrange-remainder argument near the corner, glued to a coarse global
sweep away from it — the natural, concrete, NOT-yet-tried new technique
is: **apply that exact same two-part method directly to `T` (or better,
to `G(β1)` itself, avoiding the extra algebraic complexity introduced by
the two squarings in the `T`-reduction)**, instead of continuing to search
for a global SOS/Gram-matrix certificate. Concretely:
- Away from the corner (say `|A−A*|>δ` for some fixed small `δ`), a dense
  interval-arithmetic sweep (`mpmath.iv`, as already used successfully for
  `Tgt`/`D1`) should show a clean, non-vanishing positive margin — my own
  sweep at `ε=10⁻²` already shows `T_min≈0.0187`, giving real room.
- Near the corner (`|A−A*|≤δ`), do a Taylor expansion of `T` (or `G`) in
  `(A−A*, B−β0(A))` to first order along the domain's own active boundary
  curve, exactly mirroring round 16's `Tgt` near-corner Taylor+Lagrange
  argument (which handled an analogous linear-vanishing degeneracy at a
  different corner, `(π/3,π/3)`) and round 17-18's `D1` corner closure
  (the *same* corner as here). This sidesteps SOS/SDP entirely and has
  twice already succeeded on structurally identical local degeneracies in
  this same population.

This is a genuinely different route from every generator-search/SDP
approach tried in rounds 10-19: it targets `T`/`G(β1)` with the
**already-validated local technique**, rather than another variant of
global Positivstellensatz search (LP over generator families, SDP/Lasserre
relaxations, parity/grading obstructions) — all of which have now been
tried and diagnosed (see Dead ends below) without success, and all of
which are fighting the same unavoidable boundary-degeneracy the sign
analysis above explains.

### 4. Candidate technique(s)
- **Primary recommendation:** local Taylor/Lagrange-remainder argument at
  the corner `(A*,β0(A*))` (reusing the exact machinery of
  `lemmas/d1-nonnegative-on-boundary-curve.md` and
  `lemmas/tgt-strictly-positive-throughout-D-full.md`), applied to `T` (or
  `G(β1)` directly) — a concrete, previously-successful-on-this-exact-
  corner method, not yet applied to this specific target.
- Secondary: a short symbolic proof that `X0(A*,β0(A*))=cos²β0(A*)=3/8`
  exactly (a resultant/minimal-polynomial argument in `A`, analogous to
  round 17's recommendation for the `D1` corner's "shared root" fact,
  which — per round 18 — was in fact resolved via an explicit closed-form
  substitution and cofactor argument, not a resultant computation; the
  same style of argument is likely to work here too, and the clean target
  value `3/8` makes it more tractable than the `D1` case, which had no
  such clean rational target).
- knowledge_base.md: Positivstellensatz/SOS entries (if present) should be
  read for a "boundary-active constraint" / "Lagrange-remainder near a
  degenerate point" pattern — worth checking by the outliner if not
  already cited elsewhere in the population.

### 5. Cheap-kill candidates
- **Domain-scoping check** (done here): before any further certificate
  search, ALWAYS use the *full* three-part domain restriction (`B>β0(A)`
  AND `cos²B<X0` AND `X0<cos²β0(A)`), not just the two-sided
  `cos²B<X0∧P>0∧E<0` used in some earlier explorer scans — dropping the
  upper bound manufactures large spurious "violations" that look like a
  disproof but are domain-scoping errors, not real. This is a concrete
  process fix worth flagging to future explorers/builders on this target.
- Order-of-vanishing check (linear, not quadratic) is itself a cheap
  diagnostic: confirms boundary-active degeneracy vs. interior tangency,
  and rules out wasting more effort on rank-relief tricks (shim+ε*I,
  rank-13 truncation, etc.) that implicitly assume an interior double
  root.

### 6. Knowledge-base entries to use
Not independently re-checked against `knowledge_base.md` in full this
round (focus was the direct computation per dispatch); the outliner
should cross-check whichever Positivstellensatz/SOS/Lagrange-remainder
entries are already cited by `d1-nonnegative-on-boundary-curve.md` and
`tgt-strictly-positive-throughout-D-full.md`, since the same entries are
the right ones to cite for a `T`/`G(β1)` version of the same argument.

### 7. Analogous past problems (cruxes)
Not queried this round (dispatch focused on direct symbolic/numeric probing
of the target); the crux corpus is unlikely to have a close analogue to
this specific multi-case trigonometric Positivstellensatz — the load-bearing
move here is internal (reuse of this population's own certified local
near-corner technique), not an external crux.

### 8. Prior progress
- `T≥0` (equivalently `-q1,-r0` sign target) reduced exactly to a rational
  function of `σ=sin²A,τ=sin²B,c,d,s,t` (certified,
  `case-b-e-lt-0-t-factorization.md`).
- Parity/grading obstruction proving no constant/`(σ,τ)`-only-multiplier
  certificate can work (certified, `parity-obstruction-q1-r0-certificate.md`).
- 2-generator (`n1,n2`-only) ansatz proved unconditionally infeasible via
  an exact `ℚ(√3)` witness (certified,
  `n1n2-minimal-ansatz-unconditionally-infeasible.md` — NB this is for the
  *sibling* `-sos` route's `Num,n1,n2,n4` formulation, a related but
  distinct polynomial encoding via `u=tan(A/6)`, not literally the same
  `q1,r0`; still relevant context for the same underlying obstruction
  pattern).
- **New this round:** exact identification of `T`'s global tight point
  with the already-known `D1`/`Tgt` corner `(A*,β0(A*))`,
  `A*=3arcsin(√6/4)−π/2`; the clean value `X0=cos²β0(A*)=3/8` there; and
  the linear (not quadratic) order of vanishing, explaining the recurring
  Gram-matrix degeneracy as structurally forced.

### 9. Dead ends (do not retry)
- LP over generator families (parity-basis `B1-B6`, `NewGen(H,H')` degree
  10-17): proved insufficient / infeasible at the attempted degrees
  (rounds 10-17), and the parity obstruction (certified) proves an entire
  *class* of low-degree ansätze can never work — don't re-attempt
  constant/`(σ,τ)`-only multiplier searches.
- SDP/Lasserre via `cvxpy` (CLARABEL/SCS) at fixed witness points: reliably
  reproduces a near-null 3-5 dimensional Gram-matrix eigenspace at every
  witness tried (rounds 16-18); per this round's finding, **this is
  expected and will keep recurring at any degree** — do not keep
  re-running bigger SDPs hoping the degeneracy resolves; it won't, because
  it reflects `T=0` being genuinely attained at a domain corner.
- Degree-matching schemes assuming homogeneity of `q1,r0`: already
  confirmed wrong (`q1,r0` are not homogeneous) — do not revisit.
- Complex-conjugate-pair explanation for the near-null eigenspace (round
  17): ruled out in round 18 in favor of a near-double-real-root finding
  at a *different* generator's Gram matrix (not the same corner
  phenomenon documented here — that finding concerns the `-sos` route's
  own `σ0` Gram matrix, a distinct object from `T`'s domain-corner
  degeneracy identified in this report; the two may or may not be the
  same underlying cause — worth a follow-up check but not conflated here).

### 10. Small-case / intuition notes (labeled conjecture where not proved)
- **Conjecture, strong numeric support (50+166 digits): `T` and `G(β1)`
  are both `≥0` throughout the true domain `D`, with equality exactly at
  one point, the corner `(A*,β0(A*))`.** Not yet a proof.
- **Conjecture, very strong symbolic-numeric support (166 digits):
  `X0(A*,β0(A*)) = cos²(β0(A*)) = 3/8` exactly.** This is a clean enough
  rational value that an exact symbolic proof (e.g. via the Weierstrass
  substitution `w=tan(A/2)` already used elsewhere in this population, or
  via `A*`'s minimal polynomial over `ℚ(√6)`) looks tractable and is a
  concrete, well-scoped sub-target for next round, narrower than anything
  attempted on this specific fact before.
- The domain-scoping bug identified in §1 (dropping the upper bound
  `X0<cos²β0(A)`) is a good general lesson: **always re-derive the FULL
  three-part domain from the tangent-file's own "Exact Case-(b) domain"
  before running any positivity sweep on `T`/`q1`/`r0`** — several rounds'
  worth of LP/SDP work may have implicitly used slightly different domain
  cuts; worth a quick cross-check by the outliner that all live approaches'
  numeric sweeps use the correct three-part domain.
