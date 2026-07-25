## imo-2026-02

**Lens for this report**: not a new top-level framing (per instructions — 4 prior negative
searches for that). Instead: known inequality-proving TECHNIQUES that could close the
"positive except at one degenerate boundary corner" trig target(s) that every live route
now shares, plus a fresh check of the dormant Ptolemy `Ψ>0` residual.

### Terrain recap (verified, not re-derived from scratch — cross-checked numerically)

All live routes (coordinate/resultant, its `-pointwise` fork, fixed-point/bilinear via
`Rem=0`, inversion-at-A) are proven (rounds 3-9, independently re-verified each round) to
stand or fall together on the coordinate route's own branch-selection gap, now narrowed
(round 10) to **Case (b)** of Theorem 16.2, with two live final-target formulations:

1. `coordinate-bash-resultant-boundary`'s **`T≥0`**, scoped only to the sub-case
   `P>0 ∧ E<0` (≈4.5% of Case-(b) domain), an explicit radical-free polynomial condition
   `T = c(dQ₁(σ,τ) − cR₀(σ,τ))/(4sin²(A+B))` in `σ=sin²A, τ=sin²B` (degree (4,3) pieces
   `Q₁,R₀`), with `c,d,s,t` explicit sign-known prefactors.
2. `coordinate-bash-resultant-boundary-pointwise`'s **`(★): (1+cos B)²X₀ ≥ RHS²`**,
   scoped to the ENTIRE Case-(b) domain (strictly larger, hence higher-priority per
   round 10's own cross-pollination analysis — closing `(★)` alone finishes the whole
   problem via this route). Here `X₀ = sin B cos A /(2 sin(A+B))`,
   `RHS = (1+cos B)cos β₀ − sin β₀ · G(β₀)`, `β₀=(π−A)/3`,
   `G(β)=2K_c−f(β)`, `K_c=2 sin A sin(A+B)`, `f(β)=K_c+P sinβ+Q cosβ`,
   `P=½sin(A−B)+3/2 sin(A+B)`, `Q=−sinA sinB`.

**Independent numeric re-verification I ran this round** (own `mpmath`/Python, not reusing
either builder's script): confirmed `G(β₁)≥0` over 300,000 domain-respecting random
`(A,B)` samples (min ≈ 0.0022, no violation), and separately confirmed `(★)`'s companion
quantities. I traced the reported degenerate global-minimum corner explicitly: it is
**not** literally a point on the naive boundary curve `B=β₀(A)` (i.e. `γ=β₀`) — spot
checks along that curve give both large positive AND large negative `(★)`-type values
(e.g. at `A=1.2`: value ≈ −0.127) at points where `G(β₀)>0` — so a first hypothesis "the
whole boundary curve `γ=β₀` is where tightness lives" is **false**; those points are
outside the domain closure that matters (the interior condition `β₀<β₁<γ` fails/empties
there in a way that does not connect continuously to interior domain points with the same
`A`). The genuine minimizer is an **interior** point of the `(A,B)` domain where `β₀, β₁,
γ` all converge together (domain width `γ−β₀→0` while `β₁` stays squeezed between) —
solving `B=(π−A)/3` together with `G(β₀(A))=0` simultaneously pins a specific transcendental
point `A*≈0.40638, B*≈0.91174` (angles ≈23.28°, 52.24°, 104.48° — **not** a recognizable
special triangle; `G(β₀)` vanishes there, confirmed to `mpmath` machine precision via
`findroot`). This is a genuine codimension-2 corner (two simultaneous scalar conditions in
the 2-parameter `(A,B)` family), consistent with round 10's own diagnosis, now confirmed
independently and pinned to an explicit (if not closed-form-nice) numeric root.

### Candidate technique(s) for the outliner

- **Tangent-line trick at the transcendental corner**: since the corner point solves the
  system `{B=(π−A)/3, G(β₀(A))=0}` implicitly (no nice closed form), a literal "tangent
  line at x=x₀" substitution (the classical technique for asymmetric-equality-case
  inequalities) would need to keep `A*` symbolic/implicit rather than substitute a numeric
  value — feasible in principle (prove a linear-in-`(A−A*,B−B*)` lower bound using the
  *defining equation* `G(β₀(A*))=0` as a algebraic hypothesis, without ever solving for
  `A*` explicitly) but nobody in the population has attempted this; flag as untried, not
  dead.
- **Degenerate-limit (width) expansion**: reparametrize by `w:=γ−β₀` (domain width, →0 at
  the corner) and `θ:=(β₁−β₀)/w∈(0,1)` (position within the shrinking interval). Taylor-
  expand `G(β₁)` (or `(★)`) in `w` at fixed `θ` and fixed limiting angle data; if the
  leading (`w⁰` or `w¹`) term is a manifest square or a provably nonnegative expression in
  `θ` and the limiting angle, this would be a genuine "case analysis exploiting the
  specific degenerate limit" per the dispatch — this is a concrete, not-yet-tried
  computation (nobody has done a local expansion at the corner; round 10 only did global
  numerical optimization, which found the corner but did not analyze its local structure).
  Cheap to test numerically first (fit `G(β₁)` vs `w` at fixed nearby `θ`, check power of
  leading term) before committing to a symbolic expansion.
- **SOS after the specific clearing substitution already in hand**: `(★)` is *already*
  radical-free (one squaring, per round 10) — a natural next step untried by any approach
  file: substitute `x=cos(A/3)` (via `β₀=(π−A)/3`, using triple-angle formulas to write
  `cosβ₀,sinβ₀` as cubics in `cos(A/3),sin(A/3)`) and attempt `sympy.simplify`/`factor` or
  a numerically-fitted SOS decomposition of `(1+cos B)²X₀ − RHS²` in the resulting
  polynomial ring — round 10 says this "resisted `sympy.simplify`/`factor` in the time
  available," i.e. was tried briefly and stalled, not proven impossible; a dedicated
  attempt (e.g. `sympy.Poly.is_zero` after full multiple-angle clearing, or numerically
  fitting a Gram-matrix PSD certificate at a handful of sample points and then verifying
  it symbolically) is a concrete next step.
- **Schur-like / smoothing arguments**: the KB's "piecewise-concavity smoothing" entry
  (see below) is built for sums of `|A cos kφ + B sin kφ|` terms — `G(β)` and `f(β)` are
  literally of that shape (`f(β)=K_c+P sinβ+Q cosβ`, a single sinusoid plus constant).
  This machinery is already implicitly used for the *unconditional* part of the proof
  (`f'>0` monotonicity, `f(β₀)>0`), but has NOT been applied to the harder Case-(b) target
  itself (`(★)` or `T≥0`), which mixes `β₀,β₁` nonlinearly (via `cosβ₁=√X₀`) rather than
  being a pure sinusoid-sum inequality — likely not directly transferable, but worth a
  15-minute check by the outliner before ruling it out, since it is the one KB entry
  purpose-built for exactly this population's recurring sinusoid shape.
- **Chebyshev/majorization**: no natural two-sequence pairing was found; I don't recommend
  this route — the target isn't obviously a rearrangement/majorization statement.

### Cheap-kill candidates
None obvious beyond what's already used (the domain-width sanity check that killed the
cruder bound `G(β₀)≥(1+cosB)(γ−β₀)` in round 10 — confirmed still correctly dead, I did
not find a way to revive it). No new parity/pigeonhole/injection angle surfaced this
round for either `T≥0` or `(★)`.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (`knowledge_base.md` line ~20): built for exactly the
  `|A cosφ+B sinφ|`-sum shape that `f(β),G(β)` already have; worth a targeted retry on the
  Case-(b) residual specifically (not yet tried there — only used for the already-closed
  unconditional monotonicity part).
- **Sum of squares (SOS) / completing the square** (line 17): the natural next tool for
  `(★)` after its one clean squaring — untried in the triple-angle-cleared polynomial ring.
- **Standard inequalities (AM-GM, Cauchy-Schwarz, Schur)** (line 33): no concrete
  application found this round; flagged as a candidate only if a Cauchy-Schwarz-shaped
  shortcut for `(1+cosB)²X₀≥RHS²` (e.g. `RHS` as a dot product bound) turns up — not found
  by me this round, worth a quick look since `(★)` has exactly the "square ≥ square"
  shape Cauchy-Schwarz targets.
- **Resultants / Sturm sequences**: already the population's main tool (all the `G_{2a}`,
  `G_{2b}`, `T`-factorization work); for `T≥0`'s residual `q_1,r_0` (explicit
  degree-(4,3) polynomials in `σ=sin²A,τ=sin²B`), a genuine Sturm-sequence sign-count on
  the specific 2-variable region `(σ,τ)∈(0,1)²` (not yet attempted symbolically — only
  200,000-sample sign census in `coordinate-bash-resultant-boundary.md`) is a concrete,
  named-technique next step for that sub-target specifically.

### Analogous past problems (cruxes)
I queried the crux corpus subtopics for geometry/inequality problems with a "tight only at
one degenerate configuration, need a clearing substitution + case split" shape (per
`crux_moves_documentation.md`'s subtopic index). No entry in the corpus matches this
problem's specific structure (three-way angle-equality construction reducing to a
single-parameter trig inequality with a transcendental tight point) closely enough to call
genuinely analogous — the corpus's inequality-flavored geometry entries are mostly
Cauchy-Schwarz/AM-GM on lengths, not this kind of "MVT/Lipschitz-reduced sinusoid
inequality with an implicit-equation tight corner." Reporting **none** rather than forcing
a weak match, per the instructions.

### Prior progress
See `results/imo-2026-02/current.md` round 10 entry (full detail) and the two approach
files read in full this round:
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md` (residual `T≥0` on
`P>0∧E<0`, ≈4.5% of Case-(b)) and
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md`
(residual `(★)`, 100% of Case-(b), the recommended priority target). Both are `partial`,
CHANGES REQUESTED, no gap closed this round by me (exploration only).

### Dead ends (do not retry)
- The naive "full domain-width" bound `G(β₀)≥(1+cosB)(γ−β₀)` — confirmed false (round 10,
  re-confirmed conceptually this round): don't retry without the finer `β₁−β₀` structure.
- Treating the boundary curve `γ=β₀` as *the* locus of tightness for `(★)` — I checked
  this directly this round and it is **false** in general (values both far above and
  below 0 occur along that curve at points with `G(β₀)>0`); the true tight locus is the
  specific interior codimension-2 point `A*≈0.40638,B*≈0.91174` where `γ−β₀→0` **and**
  `G(β₀)→0` simultaneously — any future symbolic attempt should target this specific
  joint condition, not the naive single-equation boundary.
- Direct `sympy.factor`/`simplify` on `(★)` after `β₀=(π−A)/3` substitution "in the time
  available" (round 10) — stalled on mixed `tan(β/2)`/triple-angle forms; a fresh attempt
  should use an explicit `cos(A/3),sin(A/3)` polynomial basis (not `tan`) per the
  suggestion above, rather than repeating the same substitution route.
- Ptolemy's `Ψ(τ,A,C)>0`: dormant since round 7 (odd-parity-of-4-branch-values reduction,
  Step 4, numeric-only at 2000-20000 samples with 0 violations). No shared machinery from
  10 rounds of the coordinate route was found to transfer to `Ψ` this round — the
  coordinate route's `G_{2a}/G_{2b}` objects are proven (round 7,
  `lemmas/yb2z-trig-identification.md`) to be trig-expressible, but Ψ lives in a
  genuinely different parametrization (`τ=tanθ`, direct resultant elimination of two
  nested radicals, not the rotation/coordinate `s_2,t_1` setup), and no identity linking
  `Ψ` to `G_{2a}G_{2b}`, `T`, or `(★)` has been found or attempted by anyone — it remains
  exactly as stuck as in round 7: a degree-6-in-`τ` positivity claim reduced to "an odd
  number of 4 branch values exceed 4," with the direct-coefficient-extraction route
  (Step 0, round 6) explicitly diagnosed as intractable ("does not factor into
  recognizable pieces"). Not recommended as this round's priority (the coordinate/
  pointwise route's `(★)` is closer to closing and is the more actionable target), but
  flagged as genuinely dormant, not disproven — a fresh SOS/SOS-after-SOS-substitution
  attempt on `Ψ`'s explicit sextic coefficients (not yet tried with modern `sympy`
  Gram-matrix PSD tooling) is a legitimate, undispatched option if the coordinate route
  stalls again next round.

### Small-case / intuition notes (conjectural, numeric only)
- `(★)`'s global infimum over the full Case-(b) domain is `≈1.5×10⁻⁹` (numerically 0),
  attained uniquely (to solver precision) at `A*≈0.40638, B*≈0.91174` — conjectured exact
  zero at this point (algebraically: `G(β₀(A*))=0` by construction, and `(★)`'s RHS at
  that same corner reduces so that the inequality becomes tight — not proved that `(★)`'s
  own LHS−RHS² has a genuine double zero there vs. simply passing through 0, i.e. whether
  a local Taylor expansion in `(A−A*,B−B*)` gives a PSD quadratic form (a true smooth
  minimum) has NOT been checked by me this round — a cheap, valuable next numerical step
  before any symbolic attempt (fit the local Hessian numerically; if PSD, that's strong
  evidence a tangent-line/SOS-at-the-corner argument can work; if indefinite/saddle, the
  true minimum path is more subtle and a naive local expansion won't suffice).
- `T≥0`'s residual sub-case is empirically small (≈4.5% of Case-(b)) and `q_1,r_0` have no
  fixed sign individually (confirmed round 10, re-confirmed matches the file's own
  percentages) — consistent with `T≥0` being a genuine joint/combined sign fact, not
  reducible to either factor alone.
