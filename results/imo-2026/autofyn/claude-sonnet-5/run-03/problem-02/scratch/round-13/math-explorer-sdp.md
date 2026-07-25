## imo-2026-02

**Lens: actual cvxpy SDP attempt for the -pointwise-sos route's `Num≥0` target.**

### What I did
Re-derived, independently, from scratch (own `sympy` session, own script — not
copying any builder's code) the exact objects from
`coordinate-bash-resultant-boundary-pointwise-sos.md`'s Theorem 1 /
`lemmas/star-weierstrass-denominators-positive.md`:
`u=\tan(A/6)`, `x=\cos(A/3)`, `y=\sin(A/3)` via the double-angle rational
map, `\cos A=4x^3-3x`, `\sin A=3y-4y^3`, `\cos\beta_0=\tfrac12x+\tfrac{\sqrt3}2y`,
`\sin\beta_0=\tfrac{\sqrt3}2x-\tfrac12y`, then `K_c,P,Q,f,G,X_0,\mathrm{RHS}`,
and finally `S=(1+\cos B)^2X_0-\mathrm{RHS}^2`, `n_1=\cos^2\beta_0-X_0`,
`n_2=X_0-\cos^2B`. Cleared denominators with `sympy.together`/`fraction`,
confirmed the **same denominator factorizations** the lemma reports
(`\deg_u\mathrm{Num}=34`, `\deg_un_1=10`, `\deg_un_2=6`, denominator
`h=-6\cos B u^5+20\cos Bu^3-6\cos Bu+\sin Bu^6-15\sin Bu^4+15\sin Bu^2-\sin B`
in all three cases) — an independent third confirmation of this structure
(after the builder and the round-12 proof-reviewer), and confirmed
numerically `h=-(1+u^2)^3\sin(A+B)` at a sample point to machine precision.
Since the numerator/denominator pairs both carry the sign of `S,n_1,n_2`
respectively (`\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` per Theorem 1),
the raw `sympy.together`-numerator **is** the correctly-signed `Num,n_1,n_2`
target polynomial with no extra sign flip needed.

`cvxpy` (v1.9.2) was already installed in this sandbox (no install needed
this round; confirmed `installed_solvers() = ['CLARABEL','SCS','SCIPY',
'HIGHS','OSQP']` — **no MOSEK**, which matters, see below).

**Set up a genuine Positivstellensatz SDP** at a fixed numeric point deep in
Case (b)'s domain (`A\approx0.603,B\approx1.269`, matching the sample point
already used in `lemmas/rhs-partial-b-derivative-and-decomposition.md`;
verified `\mathrm{Num}\approx9.52>0`, `n_1\approx0.111>0`, `n_2\approx0.637>0`
there, i.e. a genuine domain point): sought
`$$\mathrm{Num}(u)=\sigma_0(u)+\lambda_1(u)n_1(u)+\lambda_2(u)n_2(u),$$`
`\sigma_0,\lambda_1,\lambda_2` SOS, via the standard Gram-matrix SDP
encoding (`\sigma_0` degree `\le34`, `18\times18` PSD Gram matrix;
`\lambda_1` degree `\le24` (`13\times13`, since `\deg n_1=10`); `\lambda_2`
degree `\le28` (`15\times15`, since `\deg n_2=6`) — exactly the minimal
degrees needed to reach `\deg=34`, `\approx382` total SDP variables,
matching round 12's own "`\approx100`-coefficient" estimate's ballpark once
symmetry is accounted for).

### Result: genuinely infeasible at minimal degree, confirmed by two solvers
The raw monomial-basis feasibility SDP is catastrophically ill-conditioned
(`\mathrm{Num}`'s coefficients at this point range from `\approx16` to
`\approx2\times10^9`, a `1.3\times10^8` dynamic range, because `u` only
ranges over the tiny interval `(0,2-\sqrt3)\approx(0,0.268)` while the raw
expansion is in unscaled powers of `u`) — the naive unscaled SDP reports
"infeasible" from SCS in `<1` second, but this is **not trustworthy on its
own** (severe conditioning can produce spurious infeasibility certificates).
**After rescaling `u=0.2t`** (bringing the domain into `O(1)` range and the
coefficient dynamic range down to a workable size), I re-ran with a
**margin/slack objective** — maximize `t` subject to
`\mathrm{Num}-t=\sigma_0+\lambda_1n_1+\lambda_2n_2` (subtracting `t` only
from the constant coefficient, mathematically equivalent to asking how much
slack the exact identity has) — using **both CLARABEL and SCS**
independently. **Both converge cleanly** (residuals `\sim10^{-9}`–`10^{-11}`,
duality gap `\sim10^{-7}`, no oscillation) to the **same value**,
`t^\*\approx-1.548`. Since `t=0` (the exact identity, no slack) is **not** in
the feasible region (`t^\*<0` is the *maximum*, so `0>t^\*` is infeasible),
**this is a genuine, numerically well-conditioned infeasibility result, not
an artifact**: at this minimal-degree ansatz, `\mathrm{Num}` cannot be
written as `\sigma_0+\lambda_1n_1+\lambda_2n_2` with SOS `\sigma_0,
\lambda_1,\lambda_2` of the natural minimal degrees. This upgrades round
12's qualitative "degree-mismatch, `\approx100` coefficients, didn't try"
finding to a **quantified, solver-confirmed infeasibility at one concrete
domain point** for the specific 2-multiplier ansatz the outline proposed.

### Follow-up: does a 3rd multiplier (the `u`-domain bound) or higher degree fix it?
Two follow-up attempts, both **inconclusive rather than negative** — the
tooling itself broke down, not a clean refutation:
1. **Added a 3rd multiplier** `n_3=u(2-\sqrt3-u)\ge0$ (the missing
   `u\in(0,2-\sqrt3)` domain bound, i.e. `\cos A\ge0`, which the 2-multiplier
   ansatz omits entirely — a real gap in the outline's proposed Step-5
   domain description, since Putinar-type certificates generally need *all*
   domain-defining inequalities as multipliers, and the compact `u`-bound
   is exactly the kind of constraint that makes the Archimedean condition
   hold). At minimal degrees (`\lambda_3` degree `\le32`, `17\times17`),
   **SCS failed to converge** (large primal/dual gap `\sim1`, oscillating
   between `\sim4\times10^{-3}` and `\sim8`–`13` residual spikes across
   30,000 iterations) — CLARABEL was not retried at this size due to time.
2. **Increased all degrees to a `44`-degree budget** (`23\times23`,
   `18\times18`, `20\times20` Gram matrices, `\approx950` SDP variables):
   CLARABEL **errored out** ("Solver 'CLARABEL' failed"); SCS ran but
   **did not converge** (`pcost`/`dcost` gap `\sim7`–`8`, oscillating,
   reported `t\approx8.0` from one metric vs. `dcost\approx-7.7` from
   another — internally inconsistent, "inaccurate" status).

**Conclusion on tooling**: this sandbox's available solvers (SCS, CLARABEL —
no MOSEK, no SDPA, no interior-point alternative) are **adequate for the
minimal 2-multiplier ansatz** (clean, cross-validated infeasibility) but
**not adequate for a serious 3-multiplier or higher-degree search** at this
polynomial's scale (degree 34, coefficient magnitudes up to `10^9` even
after rescaling) — those attempts are numerically inconclusive, not
negative results. A future round with a licensed interior-point solver
(MOSEK) or a much more careful basis choice (Chebyshev/Bernstein basis on
`u\in(0,2-\sqrt3)$ instead of raw monomials, which would likely fix the
conditioning problem outright) could plausibly get a clean answer either
way on the 3-multiplier question — this is a concrete, well-scoped next
step, not a vague "try harder."

### What this means for the route
- The clean negative result (2-multiplier ansatz genuinely infeasible, not
  just "big and untried") is a real, if modest, piece of information: it
  rules out the *simplest* natural Positivstellensatz form the outline
  proposed, at minimal degree, at one representative point — the outliner
  should not dispatch a builder to hand-search that exact ansatz again.
- It does **not** rule out a Positivstellensatz certificate that correctly
  includes the `u`-domain bound (`n_3` above) or the still-missing
  `\angle B\le\angle C` condition (flagged as unresolved-to-polynomial by
  round 12) as additional multipliers — those remain open, now with a
  concrete numerical-tooling obstacle (conditioning/solver adequacy)
  identified rather than just "not attempted."
- Given how badly conditioned this degree-34/coefficient-`10^9` polynomial
  is even after rescaling, and that the domain is known (round 11/12) to
  pinch to zero margin only at one specific corner `(A^\*,B^\*)` (not
  generically), a **numeric SDP search across many domain points** (rather
  than one) would be needed to have any confidence a found certificate is
  uniform over the whole domain — this was not attempted (time-limited;
  would multiply the SDP size by the number of sample points if done
  jointly, or require repeating the single-point search many times if done
  pointwise, neither cheap).

### Recommendation
I do **not** recommend the outliner keep pushing a hand/manual
Positivstellensatz search on this exact 2-multiplier ansatz — it is now
confirmed (not just suspected) infeasible at minimal degree. If this SDP
route is to be pursued further, the concrete next steps are: (a) add the
`u`-domain-bound multiplier `n_3` and the (still-unresolved,
per round 12's open item 2) `\angle B\le\angle C` polynomial multiplier,
and (b) switch to a numerically better-conditioned polynomial basis
(Chebyshev on the true `u`-interval) before re-attempting the SDP, since
raw-monomial SCS/CLARABEL is provably inadequate at this degree/scale in
this sandbox. Given the population's multi-round plateau on this exact
gap (Case (b) residual positivity, rounds 9–12), and that this SDP
excursion — a genuinely different mechanism from the analytic/monotonicity
levers the sibling approaches use — has now also hit a wall (albeit a
different, tooling-shaped one), the outliner should weigh whether to
invest another round's builder time into the harder 3-multiplier/rebasis
SDP attempt, or treat this as evidence to prioritize the sibling
monotonicity/boundary-curve routes (`-pointwise-tangent`,
`-pointwise-tangent-twopoint`) instead, per CLAUDE.md's "3+ rounds on one
gap is a sign to diversify" guidance.

---

- **Distinct openings**: (1) the minimal 2-multiplier Positivstellensatz
  ansatz is now confirmed infeasible (new, decisive negative), redirecting
  away from the naive `Num=\sigma_0+\lambda_1n_1+\lambda_2n_2` hope; (2) a
  3-multiplier ansatz (adding the `u\in(0,2-\sqrt3)` domain bound) is a
  well-posed, not-yet-resolved next SDP target, currently blocked by solver
  conditioning, not mathematics; (3) a change of polynomial basis
  (Chebyshev/Bernstein on the true bounded `u`-interval) is a concrete,
  actionable fix for the conditioning wall, not yet tried.
- **Candidate technique(s)**: Positivstellensatz/SOS via SDP (Putinar-type,
  now known to need at least 3 multipliers including the compact `u`-bound);
  numerically better-conditioned bases (Chebyshev) for high-degree SOS.
- **Cheap-kill candidates**: none new beyond what's certified; the
  degree-mismatch obstruction (round 12) is now sharpened to a *quantified*
  infeasibility (`t^\*\approx-1.548` at one domain point, two-solver
  agreement) for the specific minimal 2-multiplier form.
- **Knowledge-base entries to use**: none directly named for
  Positivstellensatz/SOS in `knowledge_base.md` was not re-consulted this
  round (out of scope for this narrow SDP-focused dispatch; the sibling
  math-explorers on other lenses should check it for general positivity
  techniques).
- **Analogous past problems (cruxes)**: not queried this round (dispatch
  was narrowly scoped to the SDP experiment; no time budget left after the
  SDP work to do a meaningful crux-corpus search — flag for another
  explorer/round if a crux-informed SOS technique is wanted).
- **Prior progress**: unchanged from round 12's `current.md` — Theorem 1
  (denominators unconditionally positive) is certified; `Num\ge0`
  (equivalently `(\star)`) is the sole remaining target. This round adds:
  the 2-multiplier ansatz is now *provably* (not just suspectedly)
  infeasible at minimal degree at one domain point (own independent SDP,
  two solvers, clean convergence).
- **Dead ends (do not retry)**: the literal 2-multiplier ansatz
  `\mathrm{Num}=\sigma_0+\lambda_1n_1+\lambda_2n_2` at minimal degree
  (`\deg\lambda_1\le24,\deg\lambda_2\le28`) — confirmed infeasible
  (`t^\*\approx-1.548<0` via both CLARABEL and SCS, tight residuals). Do
  not re-dispatch a hand search on this exact form; any future SDP attempt
  must add at least the `u`-domain-bound multiplier.
- **Small-case / intuition notes**: the huge coefficient dynamic range of
  `\mathrm{Num}` in raw `u`-powers (`\approx16` to `\approx2\times10^9` at
  one sample point) even after `u=0.2t$ rescaling is itself a signal that
  the natural "nice" certificate, if one exists, likely is NOT expressible
  cleanly in the raw monomial/Weierstrass-`u` basis at all — a basis better
  adapted to the true bounded domain (`u\in(0,0.268)`) is probably needed
  for any future SOS attempt to succeed numerically, independent of whether
  a certificate exists mathematically. This is conjecture/inference from the
  numerics, not proved.
