## imo-2026-02

**Lens: 3/4-generator SDP attempt for the central `Num≥0` target (`n1,n2,n4` /
`n1,n2,n3,n4`), scouting only — no proof, no outline.**

### Distinct openings

1. **New structural simplification (the round's main finding): `n4` does NOT
   need the algebraic extension `w=√(1+u²)`.** On Case (b)'s actual domain,
   `B<π/2` unconditionally (proof: if `B≥π/2` then, since `B≤C`, `C≥B≥π/2`
   gives `B+C≥π`, but `A+B+C=π` with `A>0` forces `B+C<π` — contradiction),
   so `cosB>0` throughout. Also `u(3−u²)>0` throughout (`u∈(0,2−√3)⊂(0,√3)`,
   so `u>0` and `3−u²>0`). Since `n4=w³cosB−u(3−u²)` compares two
   **nonnegative** quantities (`w³cosB≥0`, `u(3−u²)>0`) whenever `n4≥0` is
   in question, squaring is a valid **iff** (monotone on nonnegatives), giving
   $$n_4\ge0\iff n_4^{sq}:=(1+u^2)^3\cos^2B-u^2(3-u^2)^2\ge0,$$
   a **pure polynomial in `(u,\cos B)` alone, degree 6 in `u`** — no `w`, no
   algebraic extension. Verified by exact algebra (the squaring-validity
   argument above) and corroborated numerically: `0/500{,}000` sign mismatches
   between `n₄` and `n₄^{sq}` when correctly restricted to Case (b)'s domain
   `B≤(π−A)/2` (an earlier, incorrectly-domain-restricted `300k`-sample test
   using only `B<π−A` gave `56{,}930/300{,}000` mismatches — a reminder that
   the `B≤(π−A)/2` restriction, not merely `B<π/2`, is essential, matching the
   file's own "watch out" item (i)). This is new, reusable, likely-easily-
   certifiable structure: a genuine simplification of the 4-generator ansatz
   down to a 3-generator one, all living in the plain ring `ℚ[u,\cos B,\sin
   B]` (well, `ℚ(√3)[u,\cos B,\sin B]` for `n1`), avoiding the more delicate
   `(u,w)/(w²−1−u²)` extended-ring SOS machinery entirely.
2. **Degree-34 SDP for `Num=σ0+λ1n1+λ2n2(+λ3n4sq)` at the witness point
   `(A,B)≈(0.603,1.269)` (round 13/14's known 2-generator-infeasible point):
   inconclusive with available tooling, but suggestively favorable to `n4sq`.**
   Ran the exact ansatz sizes round 13 used (`σ0` half-degree 17, `λ1`
   half-degree 12, `λ2` half-degree 14, `λ3` (new, for `n4sq`) half-degree 14),
   via `cvxpy`, both CLARABEL and SCS, in three different numerical
   formulations (per-generator self-normalized monomial basis; single global
   raw-scale monomial basis; Chebyshev basis on the rescaled `s∈[−1,1]`
   variable). Result: **all runs at this degree are numerically unstable —
   solver status is `optimal_inaccurate` in every trial except the trivial
   per-generator-normalized one, and the two solvers frequently disagree even
   in sign** (e.g. Chebyshev-basis 3-generator run: CLARABEL `t*≈+18.0`,
   SCS `t*≈−159.6`, same problem). **However, a consistent qualitative
   pattern across most trials**: the 2-generator (`n1,n2`-only) baseline
   consistently returns a comfortably negative slack (`t*≈−5.4` to `−834`,
   solver/basis-dependent but always negative when the run isn't stuck at
   the `~1e-6` noise floor), matching the known-true unconditional
   infeasibility (Theorem 3 / `lemmas/n1n2-minimal-ansatz-unconditionally-
   infeasible.md`); **adding `n4sq` moved the optimal slack upward in every
   trial**, and in two of three trials (raw-scale monomial: CLARABEL `+18.1`,
   SCS `+2.87`; Chebyshev: CLARABEL `+18.0`) it crossed into **positive**
   territory. This is **not** a certified feasibility result (both solvers
   flag the solution inaccurate, the Gram matrices' extracted eigenvalues
   sometimes go mildly negative, i.e. the numerical solution doesn't
   literally satisfy PSD, and the reconstructed polynomial identity has a
   nontrivial max-residual `≈0.72` in the one run I checked in detail) — but
   the *consistent direction* of the effect (n4sq always helps, sometimes by
   a lot) across 3 independent numerical formulations and 2 independent
   solvers is itself a real, corroborating diagnostic pointing the same way
   as round 13's own Finding 3 (the infeasible witness sits almost exactly on
   the `n4=0` boundary), now via direct SDP evidence rather than just a
   proximity observation.
3. **Root cause of the instability, diagnosed (useful for a future round,
   contradicts round 13's own conditioning claim somewhat).** The raw `Num`
   polynomial (after applying round 13's own affine rescaling `u=\frac{2-
   \sqrt3}2(s+1)` to `s∈[−1,1]`, at this witness `B`) has coefficients
   ranging from `≈2.5×10^{-5}` (degree 34) to `≈1.7×10^6` (mid-degree,
   around degree 4) — an intrinsic `~7×10^{10}` dynamic range **in the
   rescaled variable itself**, not an artifact of monomial-vs-Chebyshev basis
   choice (I tried both; Chebyshev-basis coefficients of `Num` span
   `≈3×10^{-15}` to `≈8×10^5`, i.e. **worse**, not better). This is
   substantially larger than round 13's own claimed post-rescaling range
   (`≈3×10^{-29}` to `≈16$–`24`) for what it called the same ansatz —
   **this discrepancy is worth a future round's attention**: either round
   13's reported range referred to a different (smaller-degree or
   differently-normalized) object than the raw degree-34 `Num` I built here
   (plausible — round 13's report is not fully explicit about which
   polynomial's coefficients it is describing), or there is a genuine
   inconsistency between the two derivations that should be reconciled
   before trusting either SDP's numerics further. I did **not** have time to
   track down the exact source of this discrepancy this round — flagging it
   as an open methodological question, not resolving it.
4. **Cross terms (`n1·n4sq`, `n2·n4sq`) not attempted** — time-limited. Given
   the degree-34 ansatz is already at the edge of solver reliability with
   only 3 generators, adding cross-term generators (raising the ansatz's
   effective size further) is likely to be even less numerically tractable
   without first resolving the conditioning question above.

### Candidate technique(s)
Positivstellensatz / SOS certificate search for `Num≥0` on Case (b)'s domain,
now with domain fully specified in the *plain* polynomial ring `ℚ(√3)[u,\cos
B,\sin B]` — no algebraic extension needed at all, since `n4` has a clean
polynomial-in-`u`-and-`cosB` equivalent (`n4sq`, finding 1 above). This
removes what would otherwise be a nontrivial extra piece of SOS-in-an-
extension-ring machinery from any future attempt.

### Cheap-kill candidates
None new this round beyond what's already known (round 14's exact `u=1/4`
witness already kills the 2-generator ansatz unconditionally). The `n4sq`
finding is a *simplification*, not a kill — it does not itself resolve
feasibility of the 3-generator ansatz.

### Knowledge-base entries to use
Positivstellensatz / SOS certificate techniques (as already identified by
prior rounds); no new KB entry identified this round beyond what the
approach file already invokes.

### Analogous past problems (cruxes)
Not queried this round — the lens was purely a computational SDP scout on an
already-well-scoped internal target; the crux corpus is unlikely to contain
a directly analogous multivariate Positivstellensatz numerical search. Skipped
to preserve time budget for the SDP work itself, per dispatch focus.

### Prior progress
As documented in `results/imo-2026-02/current.md` and the approach file:
Theorem 1 (Weierstrass denominators positive, certified), Theorem 2 (`∠B≤∠C`
polynomial encoding via `w=√(1+u²)`, certified as
`lemmas/angle-b-le-c-weierstrass-encoding.md`), Theorem 3 (exact rational
counterexample proving the 2-generator `n1,n2` ansatz unconditionally
infeasible, certified as `lemmas/n1n2-minimal-ansatz-unconditionally-
infeasible.md`). The central gap `Num≥0` (equivalently `(⋆)`) remains open.

### Dead ends (do not retry)
- **2-generator (`n1,n2`-only) ansatz** — proved unconditionally infeasible
  (Theorem 3, any degree). Do not retry in any form.
- **Naive monomial-basis SDP at degree 34 without a resolved conditioning
  strategy** — reproduces the exact "numerical artifact" pattern round 14
  already diagnosed and warned about (near-noise-floor or solver-disagreeing
  results). Do not report a bare "SDP says feasible/infeasible" at this
  degree as decisive; treat any single-solver, single-basis result at deg 34
  as unreliable until the conditioning discrepancy (finding 3 above) is
  resolved or an exact/interval-arithmetic certificate is extracted.

### Small-case / intuition notes (labeled as conjecture / suggestive evidence)
- **Conjecture, essentially proved by elementary case-free algebra (should be
  easy to formally certify next round): `n4≥0⟺n4^{sq}≥0` unconditionally on
  Case (b)'s domain**, via `B<π/2` (itself provable elementarily from
  `B≤C` and the angle-sum) and `u(3−u²)>0` on `u∈(0,2−√3)`. This looks like
  a clean, complete, three-line proof, not a deep numerical claim — a good
  candidate for the outliner to fold into the next SOS approach's setup
  directly (replacing `n4` with `n4sq` throughout, dropping the `w`
  extension).
- **Suggestive (not proved) numeric trend: adding `n4sq` as a third generator
  consistently increases the achievable slack `t*` at the known-hard witness
  point `(0.603,1.269)`, crossing into positive territory in 2 of 3 attempted
  numerical formulations.** This is corroborating, not decisive, evidence
  that the 4-generator (now: 3-generator, post-simplification) ansatz
  `Num=σ0+λ1n1+λ2n2+λ3n4sq` may be feasible — but no run converged cleanly
  enough (both solvers `optimal_inaccurate`, PSD violated at the
  floating-point level, `≈0.72` max identity residual in the one run checked)
  to treat this as anything beyond a lead. **Recommended next step for a
  future round**: (a) resolve the coefficient-scaling discrepancy noted in
  finding 3, (b) if a numerically "solved" SDP is obtained, extract the Gram
  matrices, round to nearby exact rationals, and verify the resulting
  polynomial identity **exactly** in `sympy` (not trust the solver's report),
  since CLAUDE.md's rigor rules require an exact, hand-verifiable
  certificate, not a floating-point "solved" flag.
