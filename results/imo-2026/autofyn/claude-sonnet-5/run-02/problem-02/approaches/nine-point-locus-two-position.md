## Status
partial

## Approaches tried
- **Round 1 (initial skeleton).** Set up Lemma 0 (imported from the shared reduction
  established in outline review) and proposed Lemma A (parametrize the 1-parameter
  family of valid (K,L) by θ = ∠KBA = ∠ACL) plus Lemma B (the circumcenter O(θ)
  is affine in some reparametrization t(θ), by analogy with the second official
  solution to IMO SL 2023 G5 / aimo-1007). Flagged CHANGES REQUESTED by outline
  review: Lemma B had no configuration-specific mechanism, only an analogy.
- **Round 1 (this build).** Built a correctly-branched numerical solver (Python,
  `scipy.optimize.fsolve`, same construction as the round-1 explorers) for the
  1-parameter family of valid (K,L), confirmed the branch is correct by
  cross-checking OM=ON to 1e-9–1e-15 residual along the whole admissible θ-range
  on two independent scalene triangles (reproducing and extending the explorers'
  findings, resolving the outline-reviewer's own failed spot-check — see "Branch
  verification" below). Then **directly tested Lemma B**: sampled O(θ) at 40–60
  θ-values per triangle and tested affineness (and, more generally, degree-1
  rational/Möbius-ness) of O(θ) — equivalently of its non-constant coordinate,
  since the other coordinate turns out to be *exactly* invariant, see below —
  against more than a dozen candidate reparametrizations (θ itself, tan θ, cot θ,
  tan(θ/2), sin θ, cos θ, the ray-lengths r_K, r_L and various algebraic
  combinations of them, and K's/L's own coordinates). **Result: Lemma B is
  numerically refuted.** No tested reparametrization makes O affine — residuals
  are 0.01–0.5 in absolute terms, four to eleven orders of magnitude above the
  solver's own noise floor (≤1e-9), and stable/reproducible across two distinct
  triangles. Even a general Möbius (linear-fractional) fit of the free coordinate
  of O against θ, r_K, r_L fails with residuals ~0.01–0.02, well above noise.
  This is a genuine, quantitative refutation, not an inconclusive null result.
  As a byproduct, derived an alternative O-free vector reformulation of the
  target (see Promotable lemmas) and verified it numerically as an identity
  along the whole family — this is algebraically equivalent to Lemma 0 (not new
  information), but is a computationally cleaner target for any future symbolic
  attempt, since it avoids the circumcenter's rational (division) formula.

## Current best

**Lemma 0 (imported, proved in outline / re-verified sound by outline review).**
Let N9 be the nine-point center of triangle ABC. Since M, N are midpoints of
sides AB, AC, both lie on the nine-point circle, so N9M = N9N. For any point P,
`PM² − PN² = (2P−M−N)·(N−M)`; applying this at P=O and P=N9 and subtracting
(the P=N9 instance vanishes since N9M=N9N) gives
`OM² − ON² = 2(O−N9)·(N−M)`. Since M, N are midpoints of AB, AC, `N−M ∥ C−B`
(midline theorem), so:

  **OM = ON ⟺ (O − N9)·(C − B) = 0.**

This is unconditional (independent of the K, L conditions) and reduces the
problem to a perpendicularity target against the fixed point N9. This part of
the approach stands and is reused by other approaches in the population.

**Branch verification (this round).** I built a numerical solver, parametrizing
the family of valid (K,L) by θ = ∠KBA = ∠ACL, ranging over rays from B and C
at angle θ to BA and CA respectively (directions chosen to point into the
interior of triangles BMC, BNC), with the remaining two unknowns r_K = BK,
r_L = CL solved from the two conditions ∠LBK = ∠LNC and ∠LCK = ∠BMK via
`scipy.optimize.fsolve`, continued along θ by warm-starting each solve from the
previous θ's solution. I filtered to solutions with K strictly inside triangle
BMC and L strictly inside triangle BNC (barycentric-sign test). On triangle
A=(0,4), B=(−3,0), C=(2.5,0): 38 valid θ ∈ [0.10, 0.92] found, and
`OM − ON` was between `1e-15` and `1e-9` in magnitude at every one — matching
the round-1 explorers' reported precision and independently confirming the
theorem numerically along the *entire* admissible 1-parameter family for this
triangle (not an isolated point). Repeated on a second triangle
A=(0.5,4), B=(−3,0), C=(2,0) with the same result (41 valid θ, `OM−ON` at
solver-noise level throughout). This resolves the outline-reviewer's earlier
failed spot-check: the correct branch requires (a) signed, not unsigned, angle
equations built directly from the geometric ray directions (not `arccos`-based
absolute-value equations with ambiguous sign) and (b) explicit filtering by the
containment inequalities (K ∈ int(BMC), L ∈ int(BNC)) plus continuation in θ
from a known-good seed, exactly as flagged.

**Refutation of Lemma B (this round, load-bearing finding).** With the
branch established, I recorded O(θ) = circumcenter(A, K(θ), L(θ)) at every
valid θ on both triangles. Two findings:

1. **The BC-projection of O is exactly constant.** Writing coordinates with
   BC horizontal (so `(O−N9)·(C−B) = 0` becomes `O_x = N9_x` = the fixed
   x-coordinate of the midpoint of MN), `O_x` was constant to `1e-9`–`1e-13`
   across every θ sampled on both triangles (e.g. triangle 1: `O_x ≡ −0.125`
   for all 38 samples; triangle 2: `O_x ≡ 0` for all 41 samples, matching
   `(M_x+N_x)/2` exactly in each case). This is exactly Lemma 0's target,
   confirmed as an identity along the whole family — strong evidence for the
   theorem itself, but not evidence for Lemma B.
2. **The complementary coordinate O_y is a genuinely nonlinear, non-Möbius
   function of every natural parameter tried.** I fit `O_y` against θ,
   `tan θ`, `cot θ`, `tan(θ/2)`, `sin θ`, `cos θ`, `r_K`, `r_L`, `1/r_K`,
   `1/r_L`, `r_K + r_L`, `r_K − r_L`, `r_K r_L`, `r_K/r_L`, `r_K²`, `r_L²`,
   `√r_K`, `K_x`, `K_y`, `L_x`, `L_y`, and combinations thereof, by
   least-squares affine (degree-1 polynomial) regression; every fit left a
   maximum residual between 0.01 and 0.6 (triangle 1) and 0.01–0.03
   (triangle 2) — four to eleven orders of magnitude larger than the ~1e-9
   solver noise floor established by finding 1 above. I additionally fit a
   general linear-fractional (Möbius) model
   `O_y = (a·x + b)/(c·x + d)` (nonlinear least squares) against θ, `r_K`,
   `r_L`; every fit again left residuals ~0.01–0.02, still far above noise.
   Second differences of `O_y` along the θ-sample (a discrete proxy for
   curvature) are smooth, non-oscillating, and of consistent sign
   (`~1e-4`, decreasing monotonically across the range shown), i.e. genuine
   smooth curvature, not solver jitter.

   **Conclusion: Lemma B, as stated ("O(θ) is affine in some natural
   reparametrization t(θ)"), is false for every reparametrization tested,
   robustly across two independent triangles.** The SL 2023 G5 mechanism
   (a moving point whose associated circumcenter traces a straight line)
   does not transplant to this configuration under the θ-parametrization
   used by the outline, nor under any of the ~15 natural alternative
   parameters tried, nor under the more permissive Möbius/degree-1-rational
   hypothesis. I could not identify, within this round's budget, any
   reparametrization under which O(θ) becomes affine; I have no evidence
   that one exists, and substantial evidence (robust nonlinearity across a
   wide net of natural candidates on two triangles) that none of the
   "obvious" ones work.

   Consequently **the "two special positions + affine interpolation"
   architecture of this approach cannot be completed as designed.** The
   fact actually witnessed numerically — `(O−N9)·(C−B) ≡ 0` identically
   along the whole family, not merely agreeing at two points on an affine
   curve — is a *stronger* statement than what Lemma B was built to
   deliver, and proving an identity that strong requires exhibiting the
   cancellation directly from the defining angle conditions (i)–(iii), which
   is the same order of difficulty as a direct symbolic derivation (the
   territory of the `complex-number-argument-bash` approach), not a shortcut
   over it.

**Byproduct: an O-free reformulation of the target (verified, not a
mechanism).** Since O is the unique point with `O·(K−A) = (|K|²−|A|²)/2` and
`O·(L−A) = (|L|²−|A|²)/2` (from `OA=OK` and `OA=OL` respectively, expanding
`|O−A|²=|O−K|²` etc.), and `K−A, L−A` form a basis of the plane whenever
`A,K,L` are non-collinear (guaranteed since `A,K,L` form a genuine triangle
with circumcenter O), one can write `C − B = α(K−A) + β(L−A)` with
`α = det(C−B, L−A)/det(K−A, L−A)`, `β = det(K−A, C−B)/det(K−A, L−A)`
(Cramer's rule, `det` the 2D cross product `u_xv_y−u_yv_x`), giving

  `O·(C−B) = ½·[α(|K|²−|A|²) + β(|L|²−|A|²)]`.

Substituting into Lemma 0's target, the theorem becomes equivalent to the
identity

  `2·N9·(C−B) = α(|K|²−|A|²) + β(|L|²−|A|²)`.

I verified this numerically (both triangles, all valid θ): agreement to
`1e-9`–`1e-14`, consistent with `OM−ON` at those same points. This is
**algebraically equivalent to Lemma 0**, not new information about the
theorem — but it replaces the rational circumcenter formula (which has a
determinant in the denominator, awkward for symbolic elimination) with a
single scalar identity in `K, L` linear in `α, β`, and could be a cleaner
starting point for a future direct symbolic attack than bashing the
circumcenter formula outright. I flag it as a promotable lemma below since it
is proved in full generality (no dependence on the specific (i)–(iii)
conditions) and is reusable by any future approach that wants an O-free
target.

**Open gap.** No mechanism has been found (this round or prior) that
completes a two-special-position argument for this configuration; Lemma B is
refuted, not merely unproven. Closing the theorem via this approach's
architecture would require either (a) finding a genuinely different
reparametrization not yet tried under which O — or some fixed linear
functional of O other than its BC-projection — is provably affine (no
candidate identified), or (b) abandoning the two-position shortcut and
directly deriving `(O−N9)·(C−B) ≡ 0` (or the equivalent O-free identity
above) from the angle conditions (i)–(iii) by full symbolic elimination,
which is not a "two positions suffice" argument any more and duplicates the
`complex-number-argument-bash` approach's task. I do not have, within this
round's budget, a route that keeps this approach's distinguishing technique
(moving points + two positions) while producing a genuine proof.

## Full proof
(not established — Status: partial. Lemma 0 is proved; Lemma B, the
load-bearing claim of this approach's original architecture, is refuted by
the numerical tests above; no substitute mechanism specific to the
two-position technique has been found.)

## Promotable lemmas

**Lemma 0 (nine-point-center reduction).** For triangle ABC with M, N the
midpoints of AB, AC and N9 the nine-point center of ABC: for any point O,
`OM = ON ⟺ (O − N9)·(C − B) = 0`. *(Already established in outline review as
sound and shared across the approach population; restated here for
completeness, not re-certifying — it already appears to be in common use.)*

**Lemma O-free reformulation (new, proved in full this round).** Let A, K, L
be any three non-collinear points with circumcenter O, and let `C, B` be any
two further points. Writing `det(u,v) = u_xv_y − u_yv_x` and
`D = det(K−A, L−A) ≠ 0`, define
`α = det(C−B, L−A)/D`, `β = det(K−A, C−B)/D` (the unique scalars with
`C − B = α(K−A) + β(L−A)`, which exist and are unique because `K−A, L−A` are
linearly independent). Then
`O·(C−B) = ½·[α(|K|²−|A|²) + β(|L|²−|A|²)]`.
*Proof.* Since O is the circumcenter of A,K,L, `|O−A|=|O−K|=|O−L|`. Expanding
`|O−A|² = |O−K|²` gives `−2O·A+|A|² = −2O·K+|K|²`, i.e.
`2O·(K−A) = |K|²−|A|²`; identically `2O·(L−A) = |L|²−|A|²`. Since
`C−B = α(K−A)+β(L−A)`, linearity of the dot product in its second argument
gives `O·(C−B) = αO·(K−A) + βO·(L−A) = ½[α(|K|²−|A|²)+β(|L|²−|A|²)]`
as claimed. ∎ This is a fully general vector-geometry fact (no dependence on
this problem's specific angle conditions) and is reusable by any future
approach to this problem (or others) that wants to eliminate an explicit
circumcenter coordinate formula from a "prove PX=PY for the circumcenter P"
target.
