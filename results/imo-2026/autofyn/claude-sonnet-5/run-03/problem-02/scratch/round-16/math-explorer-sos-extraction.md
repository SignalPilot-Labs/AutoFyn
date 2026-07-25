## imo-2026-02

**Lens: exact-certificate extraction from a converged numeric SDP, and pointwise → joint
Positivstellensatz upgrade, for the `Num≥0` central gap of
`coordinate-bash-resultant-boundary-pointwise-sos`. Scouting only — no proof attempted.**

### Where the population stands (read in full before this report)

Round 15 proved Theorem 4 (`n4≥0 ⟺ n4sq≥0`, a plain polynomial in `(u,cosB)`, no
algebraic extension — fully certified, case-free). This collapses the ansatz to
`Num = σ0 + λ1·n1 + λ2·n2 + λ3·n4sq` (degree 34 in `u`, `n1` deg 10 over `ℚ(√3)`, `n2`
deg 6 over `ℚ`, `n4sq` deg 6 over `ℚ`), and a 3-generator SDP (`σ0` half-degree 17,
`λ1` half-degree 12, `λ2,λ3` half-degree 14, ≈630 scalar SDP variables) now converges
**cleanly** — both CLARABEL and SCS report `optimal` (not `optimal_inaccurate`), agree
to 5–6 significant figures, PSD satisfied to ~1e-8, and the reconstructed identity
matches `Num` to a max residual ~1.6e-9 — at four independent witness points, including
the previously-hardest point `(0.603,1.269)` where the 2-generator ansatz is proved
unconditionally infeasible (Theorem 3, exact rational witness `u=1/4`). This reverses
round 14's inconclusive, solver-disagreeing evidence. **No exact rational Gram matrix
has been extracted, and the SDP is run separately at each fixed `B`-value — it is a
pointwise feasibility check, not a joint certificate over the whole `(u,cosB,sinB)`
domain.** `/tmp/round-15/sos_work/` contains the working scripts
(`sdp_solve.py`…`sdp_solve4.py`, `sdp_cheb.py`, `build_polys.py`, `polys.pkl`,
`rescaled_coeffs.pkl`) — reusable starting point, not re-run here.

### Distinct techniques for (a): exact rational certificate from a numeric SDP

1. **Rounding-and-projecting onto the exact affine feasible subspace ("round, then
   project, then re-verify") — the standard, most tractable route here.** This is the
   textbook method (used in computational real algebraic geometry, e.g. Parrilo's SOS
   tools, and in "exact certificates from numeric SDP" work by Peyrl–Parrilo and
   others): (i) round the numerically-converged Gram matrices `G0,G1,G2,G3` to nearby
   rationals with small denominators (e.g. via `sympy.nsimplify` with a bounded
   denominator, or simple continued-fraction rounding of each entry); (ii) the rounded
   matrices will *not* exactly satisfy the linear equality constraints (`σ0+λ1n1+λ2n2+
   λ3n4sq = Num` coefficient-by-coefficient) — compute the residual defect vector `r =
   target_coeffs − reconstructed_coeffs` exactly in `sympy`; (iii) since the equality
   constraints are *linear* in the Gram-matrix entries, project the rounding error back
   onto the affine constraint set by solving a small exact linear system for a
   correction `ΔG` (the "SOS-CERT" trick: parametrize the affine null-space of the
   linear map "Gram matrix ↦ polynomial coefficients", solve for the minimal correction
   using the *numeric* solution as a starting point, then re-check PSD-ness of `G+ΔG`
   exactly via `sympy`'s `is_positive_semidefinite` or an exact LDL^T/Cholesky-with-
   rational-pivots decomposition). This is the single most promising concrete next
   step, because: the affine map is linear (so the correction is a small *exact* linear
   solve, not another SDP), the ansatz sizes here (~630 variables total, but each Gram
   matrix is only 15×15–18×18) are within reach of exact linear algebra, and — crucially
   — Theorem 4 already reduced everything to the *plain* ring `ℚ(√3)[u,cosB,sinB]`, so
   there is no extra algebraic-extension bookkeeping to carry through the exact step.
   **Concrete risk to flag for the outliner**: if the true optimal-slack point sits
   exactly on the PSD boundary (rank-deficient Gram matrix, i.e. the true certificate is
   only feasible with `t*=0` exactly, not with slack), the rounding-then-projection can
   fail to preserve PSD-ness; the clean, comfortably-positive numeric slacks reported in
   round 15 (`t*` from `0.24` up to `8.5`, well away from 0) make this unlikely to be an
   issue here — a genuine reason for optimism specific to this problem's numerics.
2. **LLL-based / PSLQ-based rational reconstruction of individual Gram-matrix entries.**
   Less suited here than method 1: LLL/PSLQ finds a small integer relation for a *single*
   real number (or vector) given high precision, but does not by itself respect the
   *joint* linear constraint structure across all four Gram matrices simultaneously — it
   would need to be run per-entry and then the whole thing re-projected onto the
   constraint affine subspace anyway (method 1's step iii), making it a strictly worse
   version of method 1 unless method-1 rounding is empirically unstable. Worth trying
   only as a fallback if naive `nsimplify` rounding in method 1 produces a badly
   ill-conditioned correction system.
3. **Exploit sparsity/symmetry to shrink the unknowns before solving exactly.** The
   round-15 report does not mention checking whether the converged Gram matrices are
   (numerically) sparse, block-diagonal, or low-rank beyond the raw PSD requirement. A
   concrete, cheap diagnostic for next round: print the numeric Gram matrices'
   eigenvalue spectra in full (not just the minimum eigenvalue already reported) — if
   `G1,G2,G3` are effectively low-rank (say rank 2–4 out of 15–18), the true exact
   certificate likely lives in a much smaller-dimensional family (write each Gram matrix
   as `V^T V` with `V` a small `k×n` matrix instead of a full symmetric matrix — this is
   exactly how one turns "SOS with an `n×n` PSD Gram matrix" into "an explicit sum of
   `k` squares", which is both easier to verify by hand and much better-conditioned for
   exact rational rounding). This should be the *first* diagnostic run next round, since
   it is essentially free (just inspect eigenvalues already computed) and directly tells
   the outliner whether method 1's correction system will be small or large.
4. **Direct hand/`sympy` re-derivation bypassing the SDP entirely, using the exact `u=1/4`
   witness structure from Theorem 3 as a template.** Theorem 3's exact rational
   counterexample point suggests the true certificate (if one exists) may have
   recognizably simple structure near the domain boundary. A cheaper alternative to full
   Gram-matrix extraction: fix the smallest-margin witness point, symbolically expand
   `Num − λ1·n1 − λ2·n2` (using the *numeric* `λ1,λ2` as a guide for the rational
   `λ` to try, e.g. simple values like `λ = p/q` with small `q` near the SDP's reported
   optimal multiplier), and check by hand whether the residual factors as an explicit,
   visibly-nonnegative combination. This is a much smaller ambition (a single-point
   certificate, explicitly, without SDP machinery) but may be faster to get exactly
   right and would still be useful as a stepping stone / sanity check for method 1's
   projection step.

### Distinct techniques for (b): pointwise → joint multivariate Positivstellensatz

5. **Promote λ_i and σ0 from numbers to explicit low-degree polynomial multipliers in
   the remaining free variables `(cosB, sinB)`, and re-run the SDP as a genuine
   bivariate-coefficient SOS program.** This is the standard move to go from "numeric
   SDP feasible at finitely many sample points" to "a Positivstellensatz certificate
   valid on the whole domain": instead of solving `Num(u,B_i) = σ0 + λ1(B_i)n1(u,B_i) +
   λ2(B_i)n2(u,B_i) + λ3(B_i)n4sq(u,B_i)` separately at each sampled `B_i` (what round 15
   did), set up ONE SDP where `λ1(u,cosB,sinB), λ2(...), λ3(...)` are themselves SOS (or
   at least polynomial) in `(cosB,sinB)` of some small degree `d`, and `σ0(u,cosB,sinB)`
   is a joint SOS polynomial in all three variables — then the equality constraint
   `Num − σ0 − λ1n1 − λ2n2 − λ3n4sq ≡ 0` becomes a set of *polynomial identities in three
   variables*, i.e. many more scalar linear equality constraints on a (correspondingly
   larger) set of Gram-matrix entries, but still a single SDP feasibility problem, not
   four separate ones. **Concrete recommended parametrization for the outliner**: since
   `n1,n2,n4sq` themselves have low degree in `(cosB,sinB)` (jointly degree ≤3 per round
   12's report), a first attempt should try `λ_i` of degree ≤2 jointly in `(cosB,sinB)`
   (or even degree ≤1, i.e. affine, as the cheapest possible test) before going higher —
   round 15's own pointwise data (the table of four `t*` values, which vary smoothly and
   substantially with `(A,B)`, from `0.24` to `8.5`) suggests the true multipliers are
   NOT constant across the domain, so a constant-λ joint certificate is likely infeasible
   by construction, but a low-degree polynomial λ should have a real chance. The `sos_work`
   scripts already parse `Num` as a function of `(u,cosB,sinB)` jointly (per `build_polys.py`
   / `build_polys2.py`), so this is a natural, low-friction extension of existing
   infrastructure, not a from-scratch rebuild.
6. **Use the `cosB²+sinB²=1` relation as a genuine (non-SOS, free-sign) ideal-membership
   multiplier**, exactly as round 12 flagged (item (ii) of its Step-C-6 list) but never
   implemented: when setting up the joint SDP, add a free-sign polynomial multiplier
   `μ(u,cosB,sinB)·(cosB²+sinB²−1)` to the certificate (this term is allowed to be any
   polynomial, not required to be SOS, since it is identically zero on the real domain of
   interest — this is the standard Positivstellensatz device for equality constraints,
   distinct from the inequality-defining generators `n1,n2,n4sq` which must have
   nonnegative/SOS multipliers). Omitting this in a joint `(u,cosB,sinB)`-degree SDP (as
   opposed to trig-substituted single-variable-`u`-at-fixed-`B` runs, where `cosB,sinB`
   are just numbers and this issue doesn't arise) is a likely source of either
   infeasibility or unnecessarily high required degree if forgotten — flag this
   explicitly to whichever round attempts item 5, since it is an easy place to
   introduce a silent, hard-to-diagnose bug (cf. round 15's own Part 5 finding about a
   different silent-bug class in the SDP constraint-construction code).
7. **A cheaper, weaker intermediate goal before the full joint-SOS program: prove the
   `t*(B)` slack function itself is bounded below by an explicit positive constant using
   only a handful of the already-computed pointwise SDP solutions plus a Lipschitz/
   continuity argument.** Rather than solving the much harder joint SOS program directly,
   note that if `t*(B)` (the optimal slack of the pointwise 3-generator SDP, as a function
   of the fixed `B`-value) can be shown continuous and the *domain* of valid `B` is a
   compact interval (which it is, per round 11/13's certified domain description), then a
   finite covering argument — evaluate the pointwise SDP at finitely many `B`-values with
   a proven modulus of continuity connecting nearby points — could in principle establish
   `t*(B) > 0` for ALL `B` in the domain without ever constructing a single joint
   certificate. This is analytically closer to the rest of the population's existing
   toolkit (interval arithmetic / dense sampling with certified bounds, as already used
   successfully in the `-pointwise-tangent` sibling's Theorem B/C, `mpmath.iv` directed
   rounding) than to a fresh Positivstellensatz construction, and could be a faster
   route to a *complete* proof even though it is mathematically weaker (a covering
   argument, not a closed-form certificate) — worth flagging to the outliner as an
   alternative "finish line" if item 5's joint SDP proves intractable at low degree.
   Caveat: this still needs an EXACT (not floating-point) per-point pointwise
   certificate at each covering point (method 1 above), or a rigorous interval-arithmetic
   lower bound on `t*(B)` at each point, not just a numeric "optimal" solver flag — so it
   does not avoid the exact-extraction problem, only avoids the joint-multivariate SOS
   construction.

### Cheap-kill / sanity checks to run before committing an approach slot to this route
- Before attempting the full joint SOS (item 5), do the eigenvalue/rank diagnostic
  (item 3) on the existing round-15 Gram matrices — if they turn out to be *not*
  low-rank, the exact-extraction step (item 1) will be harder and the outliner should
  budget more time/risk for it.
- Re-run the round-15 pointwise SDP at 2-3 more `B`-values bracketing the domain
  boundary (near `A≈A*≈0.4064`, the certified empty-domain threshold from round 11) to
  see whether `t*(B)→0` there (expected, since Case (b) pinches to a corner) — if so,
  any joint polynomial certificate (item 5) must itself have `t*` vanish at the domain
  boundary, which constrains the achievable λ-degree and is useful information to give
  the SDP solver as a sanity check on its own output.

### Knowledge-base / crux corpus check (as directed)
- `knowledge_base.md` has only a one-line generic "SOS / completing the square" entry
  (lines 17-19) — no Positivstellensatz-specific, exact-extraction, or numeric-SDP
  guidance exists there; nothing to adapt directly.
- Queried the crux corpus (`algebra`/`inequalities-SOS-and-convexity`, 149 cruxes, plus
  a keyword sweep for "Positivstellensatz", "rational reconstruction", "LLL", "Gram
  matrix", "exact SOS", "resultant", "round to" across all domains): **no crux
  addresses extracting an exact certificate from a numeric SDP, or promoting a pointwise
  numeric feasibility result to a joint multivariate Positivstellensatz** — this is a
  computational-algebra technique outside the corpus's Olympiad-solution-move scope (the
  corpus's SOS entries are all explicit hand-constructed sums of squares for competition
  inequalities, e.g. Schur-type bounds, tangent-line tricks, AM-GM completions — not
  SDP-numerics-to-exact-certificate pipelines). Confirms round 15's own explorer's
  assessment that this lens is not corpus-answerable; the two concrete techniques above
  (rounding-and-projection for (a), polynomial-multiplier joint SDP for (b)) come from
  general computational real algebraic geometry practice, not from any specific crux.

### Recommendation for next round's outliner
Two genuinely separate, parallel next steps, either of which is concrete enough to
assign to a builder:
1. **Exact extraction at the existing witness points** (technique 1, with the rank
   diagnostic of technique 3 run first) — a self-contained, bounded task using only
   already-computed numeric data in `/tmp/round-15/sos_work/`, no new SDP runs required.
   If successful, this at minimum produces a fully rigorous, hand-verifiable
   POINTWISE certificate at 1-4 specific `(A,B)` values — not the full proof, but a
   genuine, certifiable lemma (e.g. "Num(u, B=1.269...) ≥ 0 for all valid u, proved by
   explicit SOS decomposition"), useful both as a stepping stone and as independent
   confirmation the ansatz shape is right before investing in the harder joint version.
2. **The joint bivariate-multiplier SDP** (technique 5, with the ideal-membership
   caveat of technique 6 built in from the start) — this is the one that could actually
   close the gap, but is a materially larger undertaking (an SDP with more variables,
   possibly hitting the same numerical-conditioning issues round 15's Part 3/5 already
   struggled with at fixed-B degree 34, now compounded by extra multiplier-degree
   freedom). Should be attempted only after low-degree multiplier trials (constant,
   then degree ≤1, then degree ≤2 in `(cosB,sinB)`) are tried in increasing order, per
   the parametrization note in technique 5, to keep the SDP small enough to stay
   numerically reliable.
Do NOT re-attempt a bare higher-degree monomial-basis pointwise SDP without either of
these upgrades — round 15 already achieved a clean pointwise result at the natural
degree; further pointwise runs at more points would only add more numeric-only evidence
of the same kind already judged (correctly) as insufficient for `solved` status.
