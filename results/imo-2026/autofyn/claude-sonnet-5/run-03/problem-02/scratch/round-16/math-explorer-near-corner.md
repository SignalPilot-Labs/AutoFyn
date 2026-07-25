# imo-2026-02 — lens: closing the near-corner interior gluing gap
## (coordinate-bash-resultant-boundary-pointwise-tangent, Open gap 5's residual)

Scope note: pure scouting, no proof attempted. Read `current.md` in full,
the live approach file in full (rounds 11–15, including New results 6–9,
Theorems A/B/C, and the round-15 2-D adaptive interval sweep), and
`/tmp/round-14/`, `/tmp/round-15/` reports (explorers, outline-reviewer,
proof-builder, proof-reviewer). Also scanned `knowledge_base.md` (no
problem-specific entry beyond the generic EVT/Lagrange-multiplier-on-a-
compact-manifold entry already in the file) — the crux corpus was not
re-queried (the file's own round-15 note and round-1 finding both record
no relevant geometry-domain crux exists for this problem; nothing in this
gap's shape — quantitative local-to-global gluing near a boundary corner —
suggests a new subtopic worth querying).

## Exactly what is open, restated precisely

The approach has reduced the whole route to a single quantitative gap. Two
facts are **already fully certified**, independently of each other:

1. **(Theorems B, C, round 15).** `Tgt(A,B) ≥ Tgt(π/3,π/3)` for every point
   of `𝒞_hi∩D` and every point of `𝒞_lo∩D` — proved by certified
   directed-rounding interval-arithmetic branch-covering (not sampling),
   gap-free over each entire boundary curve.
2. **(New result 9, round 14).** `(π/3,π/3)` is a *strict local minimum* of
   `Tgt` relative to `D`: the directional derivative into every direction of
   the tangent cone at the corner is certified `≥ δ := 3.5023…> 0` (interval
   arithmetic, `mpmath.iv`, 60-dps). But the proof of "strict local min"
   only says this holds "for `ε` small enough" — the radius is asserted to
   exist via a compactness/boundedness-of-second-derivatives argument, but
   **no explicit numeric value of that radius was produced**.
3. **(Round 15, 2-D adaptive interval sweep).** A certified quadtree sweep
   (depth 22, boxes down to side `≈4×10⁻⁹`) finds **zero** violations of
   `Tgt ≥ Tgt(corner)` anywhere in the closure of `D`, down to boxes whose
   distance from the corner is `≲5×10⁻⁸` — an interval-arithmetic
   resolution floor, not a real ambiguity (the boxes' `Tgt` enclosures
   already agree with `Tgt(corner)` to 7–8 digits).

**The gap is exactly: produce an explicit `r₀ > 0` (any `r₀ ≥ 5×10⁻⁸`
suffices, since the sweep already covers everything outside that) such
that `Tgt(A,B) ≥ Tgt(π/3,π/3)` is proved — not just numerically observed —
for every `(A,B) ∈ D` with `∥(A,B)-(π/3,π/3)∥ ≤ r₀`.** This is a much
weaker ask than a fully sharp local analysis: because `δ≈3.5` is a large,
comfortable margin, essentially any honest explicit second-order bound will
give an `r₀` many orders of magnitude larger than the `5×10⁻⁸` needed.

## Recommended technique: quantitative Taylor + certified curvature/Hessian bound, framed as a two-piece compactness gluing

This is the standard fix for exactly this situation (a local-min argument
whose "small enough" is qualitative, needing to be glued to a numerically-
resolved exterior region) and it reuses machinery already certified in this
file almost entirely as-is.

**Step 1 — make the domain's near-corner shape quantitative, not just to
first order.**
`𝒞_hi: B=(π-A)/2` is *exactly* linear — zero curvature, nothing to bound.
`𝒞_lo` is the implicit curve `h(A,B):=X₀(A,B)-cos²B=0`; round 14 already
computed its exact tangent slope at the corner (`dB_lo/dA=1/4`, New result
8, via `h_A/h_B` at the corner). The natural next step is a **second**
implicit differentiation of `h=0` to get `d²B_lo/dA²` in closed form (an
elementary, mechanical extension of the same computation — quotient rule
applied twice, using the already-certified `∂X₀/∂A` (D6) and `∂X₀/∂B`
formulas plus their own further derivatives). This gives an exact rational
or closed-trig value for the curvature at the corner, and a certified
interval-arithmetic *bound* on `d²B_lo/dA²` over a small box
`A∈[π/3-r₀,π/3]` gives, via Taylor's theorem with Lagrange remainder (a
single scalar function of one variable now, `B_lo(A)`), an explicit
inequality of the form
`|B_lo(A) - (π/3 - (π/3-A)/4)| ≤ K·(π/3-A)²` for an explicit constant `K`.
This quantifies exactly how far the true domain deviates from the tangent
cone `t∈[-1/4,1/2]` used in New result 9's argument.

**Step 2 — a certified second-order (or even a cruder first-order-plus-
uniform-Lipschitz) bound on `Tgt` itself near the corner.**
`Tgt` is already known in exact closed form (`4(1+cosB)²X₀D₂²-T₁'²`, all
constituents closed-form trig expressions, `C^∞` near the corner since
`sin(A+B)=sin(2π/3)≠0` there). A **direct, mechanical extension of the same
`mpmath.iv` 60-dps interval-arithmetic technique already used for the
gradient in New result 9** (and for Theorems B/C's derivative sweeps) can
certify a bound `M` on the operator norm of the Hessian (or, more simply,
on the third partial derivatives, if a plain Lagrange-remainder-of-degree-1
bound is preferred) of `Tgt` over a small box around the corner, e.g.
`[π/3-r₀,π/3+r₀]²` for a first candidate `r₀` (say `10⁻³` or `10⁻⁴` —
this can be chosen generously since only `≥5×10⁻⁸` is actually needed, so
there is no pressure to make the box small/tight).

**Step 3 — combine into an explicit quantitative one-sided bound and solve
for `r₀`.**
Along a ray from the corner in direction `(-1,t)` at parameter `ε>0`
(i.e. `A=π/3-ε`, `B=π/3+tε`), Taylor's theorem with the certified Hessian
bound `M` gives
`Tgt(π/3-ε,π/3+tε) - Tgt(corner) ≥ ε·(-g_A+t·g_B) - (M/2)ε²`,
and `-g_A+t·g_B ≥ δ=3.5023…` was *already proved* (New result 9) for all
`t` in the tangent-cone interval `[-1/4,1/2]`. Using Step 1's curvature
bound to show the *true* admissible `t`-range at parameter `ε` lies inside
a slightly widened interval `[-1/4-Kε, 1/2+Kε]` (rather than exactly
`[-1/4,1/2]`), and re-certifying (via the same interval technique) that
`-g_A+t·g_B` stays `≥ δ' := δ - O(ε)` on this widened interval for small
`ε`, gives
`Tgt(π/3-ε,·) - Tgt(corner) ≥ ε·δ' - (M/2)ε² > 0` for all `0<ε≤r₀`
whenever `r₀ < 2δ'/M`. Since `δ≈3.5` is large and `M` (a bound on second
derivatives of a bounded, smooth trig-rational expression over a tiny box)
will almost certainly come out as a modest double- or triple-digit number
in absolute value, `2δ'/M` will very plausibly land far above `10⁻³`,
comfortably beating the `5×10⁻⁸` actually required. **This is the key
reason this gap looks tractable and close to closing**: the margins already
proved (δ≥3.5, boundary curvature machinery already half-built) are
enormous relative to the tiny radius that needs beating.

**Step 4 — glue.** `D̄ = (D̄∖B(corner,r₀)) ∪ (D̄∩B(corner,r₀))`. The first
piece is covered by re-running (or literally reusing, if `r₀` is chosen to
match) the round-15 2-D adaptive interval sweep restricted to exclude only
the tiny ball; the second piece is covered by Step 3's explicit inequality.
This is a completely standard compactness-style case split (not a new
technique — it is exactly the "(ii)" option the file's own round-15 "Honest
assessment" paragraph already flags as the way to close this) but it has
not yet been executed with an explicit `r₀`.

## A sharper variant of the same idea, avoiding the two-step Taylor+curvature bookkeeping

Instead of expanding in `(ε,t)` symbolically to only first order and
bounding a remainder, a cleaner and likely *faster-to-execute* route,
reusing exactly the Theorem B/C machinery style already in the file:

Define the **quotient** function
`q(A,B) := (Tgt(A,B) - Tgt(π/3,π/3)) / dist((A,B),(π/3,π/3))`
(or, more concretely, parametrize by the exact boundary curves — Theorem A
already gives `A(B)` in closed form on `𝒞_lo`, and `𝒞_hi` is exactly
linear — and work with `ε := π/3-A` as the single scalar parameter, using
the true domain's `t`-range at each `ε`, not an idealized cone). The reason
the round-15 sweep chokes near the corner is that `Tgt-Tgt(corner)→0`
there, so any finite-width interval enclosure straddles zero once the box
is smaller than the true value. But the **directional-derivative quotient**
`(Tgt(π/3-ε,π/3+tε)-Tgt(corner))/ε` extends *continuously to `ε=0`* with
limiting value `-g_A+t·g_B`, which is bounded *away* from zero (certified
`≥3.5`) uniformly over the relevant `t`-range. An interval sweep of *this
quotient* (built directly and symbolically from the exact closed forms —
no numerical differentiation needed, `sympy`/`mpmath.iv` handle a quotient
expression just as well as a plain one) over a small box `ε∈(0,r₀]`,
`t∈[t_lo(ε),t_hi(ε)]` (true domain range) does **not** suffer the
equality-point degeneracy that defeated the direct `Tgt-Tgt(corner)` sweep,
because the quotient itself never gets close to zero — it should certify
cleanly with the *same* interval-arithmetic technique already used for
Theorems B and C, likely with far fewer sub-intervals than the failed 2-D
sweep needed (which had to bisect down to `4×10⁻⁹` precisely because it was
chasing a vanishing target). This variant avoids ever computing an explicit
Hessian bound by hand — it lets the certified interval machinery do the
"second-order" work implicitly, the same way Theorem B's Step 2 already
used a derivative-sign sweep (not a value sweep) to handle the "approaching
the corner" sub-case. **This is the closest analog to what already worked
twice in this file (Theorem B Step 2, Theorem C Step 2) and is the
single most promising concrete next step.**

## Other techniques considered and their status

- **Lagrange-multiplier / KKT uniqueness argument.** Framing the corner as
  the unique KKT point of `Tgt` subject to the (locally linear/curved)
  active constraints is essentially a restatement of New result 9's
  first-order argument; without a second-order sufficiency bound (i.e.
  without the Hessian/curvature work above) it cannot upgrade "local" to a
  quantitative radius. Not a distinct route — it collapses into the
  Taylor/Hessian technique above once made rigorous. Not recommended as a
  separate line of attack.
- **Convexity of `Tgt` or of `D` near the corner.** The sibling round-15
  explorer (`math-explorer-tgt-global-min.md`) already flagged that `Tgt`
  shows no sign of joint convexity globally (it is a difference of two
  nontrivial pieces, `4(1+cosB)²X₀D₂²` minus `T₁'²`), and `D` itself is a
  curvilinear, non-convex-looking region. A convexity argument is not
  ruled out *locally* (a small enough neighbourhood of a strict local min
  of a smooth function is often "locally convex-looking" in the sense that
  the Hessian is PSD there) — but proving the Hessian is PSD at/near the
  corner is again exactly the same certified-interval-Hessian-bound
  computation as Step 2 above, just packaged differently. Not a
  meaningfully different technique from the recommended one; do not spend
  a separate round on "prove convexity" as if it were independent.
- **A direct algebraic (non-numeric) bound using the corner's exact
  defining equation.** `T₁'(π/3,π/3)=0` is already an *exact* algebraic
  fact (a sum-to-product identity, proved in round 13/14, not numeric).
  One could hope to find an exact algebraic factorization of
  `Tgt - Tgt(corner)` (or a lower bound for it) valid in a full 2-D
  neighborhood, not just via a Taylor expansion — e.g. writing
  `Tgt-Tgt(corner) = 4(1+cosB)²X₀D₂² - (9/4)D₂(corner)² - T₁'²` and hunting
  for an SOS-type or monotonicity-type argument that this is `≥0` exactly,
  the same style as the file's own certified `T1'` factorization (New
  result 3). This would be strictly stronger (an exact proof, no radius
  needed at all) but the population has *repeatedly* found that this whole
  family of `Tgt`/`Ψ`-type targets is **not** globally SOS/positive off the
  true domain (round 6, round 11, reconfirmed round 15's explorer) — so an
  unconditional algebraic proof valid off-domain is very unlikely to exist,
  and the "off-domain" failure mode is exactly what would bite a naive
  2-variable SOS attempt near the corner (where the domain is pinched to a
  single point, so an algebraic identity would have to secretly encode the
  domain constraints). **Worth a bounded-effort attempt** (it would be the
  strongest possible resolution if found) but should not block dispatching
  the quantitative-Taylor route in parallel, which is far more likely to
  land given the enormous existing margins.
- **Morse-theory-style local-to-global argument.** Not applicable in the
  form textbook Morse theory usually takes (that needs global structure —
  e.g. classifying all critical points and their indices on a compact
  manifold without boundary); `D` has boundary and the "no interior
  critical point" fact is itself only numerically confirmed so far (round
  15 explorer's opening 2, `2000` `fsolve` restarts, 3 total critical
  points of the unconstrained function, none inside `D` — not proved). If
  a future round *does* prove "no interior critical point of `Tgt` in `D`"
  symbolically (via resultant/Gröbner elimination of `∇Tgt=0` against the
  domain's defining polynomials — flagged as tractable by the round-15
  explorer, reusing the population's existing elimination toolkit), that
  would be a genuinely different, complementary route: it would reduce the
  *whole* global-min question (not just the near-corner sliver) to the
  boundary, which is already handled by Theorems B/C plus the corner
  itself. This is a good candidate for a **second, parallel sub-effort**
  next round, independent of the near-corner quantitative-Taylor route —
  if it succeeds it makes the near-corner-specific gluing argument
  unnecessary (Theorems B/C would then cover 100% of the possible minimum
  locations by themselves, corner included as their shared endpoint).

## Concrete next-round plan for the outliner

Two genuinely different, both tractable, sub-efforts to put in the build
set (not mutually exclusive — either alone would close the gap):

1. **(Primary recommendation) Quotient-based certified interval sweep near
   the corner**, per the "sharper variant" section above: build
   `q(ε,t):=(Tgt(π/3-ε,π/3+tε)-Tgt(corner))/ε` symbolically from the exact
   closed forms (reusing `X₀,D₂,T₁'` exactly as already certified), extend
   it continuously to `ε=0` (value `-g_A+t·g_B`, already certified `≥δ`),
   and certified-interval-sweep it (à la Theorem B/C's derivative-sign
   Step 2) over `ε∈(0,r₀]` for some modest `r₀` (e.g. `10⁻³` or `10⁻⁴`,
   generous relative to the `5×10⁻⁸` actually needed), using the *true*
   domain's `t`-range at each `ε` (built from Theorem A's exact
   parametrization of `𝒞_lo` for the lower edge and the exactly-linear
   `𝒞_hi` for the upper edge — no approximation needed for the range
   itself, only for confirming `q>0` throughout it). This should reuse
   ~90% of already-written interval-arithmetic infrastructure from
   Theorems B/C and New result 9.
2. **(Secondary, complementary) Symbolic elimination proof of "no interior
   critical point of `Tgt` in `D`"**, per the round-15 explorer's opening 2
   — a resultant/Gröbner elimination of `∂Tgt/∂A=∂Tgt/∂B=0` against the
   domain's polynomial/trig inequality constraints, in the style of the
   population's existing `Q(m)`-discriminant and parity-obstruction
   machinery. If completed, this independently closes the *entire* global-
   min gap (not just the corner neighbourhood) by reducing it fully to the
   already-certified boundary theorems, making the near-corner-specific
   argument unnecessary.

Both are concrete, build on already-certified machinery, and neither
requires inventing new mathematical technique — the underlying tools
(certified `mpmath.iv` interval sweeps, implicit differentiation, resultant
elimination) are all already in active use elsewhere in this file and its
siblings.
