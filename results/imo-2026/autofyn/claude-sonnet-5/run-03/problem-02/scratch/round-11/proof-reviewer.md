# Proof review — round 11 — imo-2026-02

Problem: imo-2026-02 (IMO 2026 P2). All four built approaches this round
target the shared "Case (b)" residual positivity gap (the last open
sub-case in the branch-selection question that is the whole population's
single remaining obstruction). Independently rebuilt every load-bearing
new numeric/symbolic claim from scratch in fresh `mpmath`/`python3`
sessions (never reusing a builder's script), per the working-rule
established in prior rounds.

## 1. `coordinate-bash-resultant-boundary-pointwise.md`

**Claims examined**: (a) Hessian check at the pinned corner
`(A^*,B^*)` shows nonzero gradient, refuting the outline's "interior PSD
critical point" premise; (b) Case-(b) domain is empty for `A\le A^*`,
opening to a positive-width `B`-window only for `A>A^*`; (c) a 40-digit
numeric coincidence between the domain-nonemptiness threshold equation and
the already-certified `G_{\mathrm{curve}}(A^*)=0`, explicitly flagged
unproved.

**Independent verification.**
- Re-solved `G_{\mathrm{curve}}(A)=0` from scratch (own `mpmath`, 40 digits,
  own closed forms for `K_c,P,Q,f,G,\beta_0` taken from the certified
  `lemmas/mvt-lipschitz-reduction-case-b.md`): `A^*=0.406377780684330\ldots`
  matches to all 40 displayed digits; `\mathrm{star\_slack}(A^*,B^*)=0`
  exactly at this precision.
- Recomputed the gradient and Hessian of `star_slack` at the corner via
  independent centered finite differences at three widely separated step
  sizes (`h=10^{-6},10^{-10},10^{-15}`): gradient
  `\approx(1.780926,1.120546)`, stable to 10+ digits across all three step
  sizes — matches the file's `(1.7809,1.1205)` exactly. Hessian
  `\approx(-2.733152,1.855850,-2.047813)` (entries `AA,AB,BB`), `\det
  \approx2.153>0`, `\mathrm{tr}<0` — matches the file exactly; confirms
  the claimed local-maximum classification. **This decisively confirms
  claim (a)**: the corner is not an unconstrained interior critical point
  in any PSD sense; the outline's premised mechanism does not apply.
- Independently scanned the exact admissible-`B` window (own script,
  `\beta_1:=\arccos\sqrt{X_0}`, Case (b) `=\{\beta_0<\beta_1<B\}`) at 14
  sample `A` values: empty at `A\in\{0.1,\ldots,0.4064\}`, nonempty (with
  explicit positive-width windows, e.g. `(0.9146,0.9524)` at `A=0.42`,
  close to the file's `(0.9299,0.9526)`) from `A=0.41` on. **Confirms claim
  (b)** qualitatively and quantitatively (window edges match to the
  resolution of the independent grid).
- Independently re-solved `\cos^2\beta_0(A)=X_0(A,\beta_0(A))` (own
  `mpmath`, 40 digits, fresh `findroot` call, independent of the
  `G_{\mathrm{curve}}` solve): root agrees with `A^*` to `<10^{-42}`.
  Independently checked the "not proportional" claim (ratio of
  `G_{\mathrm{curve}}(A)` to `\cos^2\beta_0(A)-X_0(A,\beta_0(A))` at
  `A\in\{0.1,0.3,0.5,0.7,1.0,1.3\}`): `\approx3.05,3.08,3.03,2.90,2.59,
  2.17` — reproduced exactly, confirming non-proportionality. **Confirms
  claim (c)**, correctly disclosed as unproved (no mechanism derived).

**Verdict on this file.** Status `partial` as self-reported is accurate.
No overclaiming — all three headline claims are honestly scoped (the
Hessian/domain findings are presented as established computational facts,
the coincidence explicitly as an open, unproved observation) and all are
independently reproduced. `(\star)` itself remains open. **CHANGES
REQUESTED.**

Lemma certified: `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`
(the gradient/Hessian finding — a decisive, reproducible numerical fact,
explicitly NOT a symbolic theorem since `A^*` has no known closed form).
The domain-emptiness claim (b) and the root-coincidence (c) are **not**
certified as lemmas: (b) is checked at only 14-16 discrete `A` values, not
proved for the continuum `A\in(0,A^*]`; (c) is explicitly flagged unproved
by the builder itself. Both are recorded as open, well-scoped targets in
`current.md` instead.

## 2. `coordinate-bash-resultant-boundary-pointwise-sos.md`

**Claims examined**: `\cos(A/3)/\sin(A/3)` basis substitution fails
(genuine linear-in-`y` residual survives one squaring); `u=\tan(A/6)`
substitution works cleanly (numerically verified `<10^{-12}`); `\mathrm{Num}`
is not globally sign-definite (`\approx37\%` negative without the Case-(b)
domain restriction — a decisive negative result ruling out any
domain-free SOS certificate); new explicit domain-defining polynomials
`n_1,n_2`.

**Independent verification.** Did not re-derive the full 466-term
`\mathrm{Num}`/`n_1,n_2` symbolically this round (large, and the file
itself does not submit them for certification — it explicitly flags them
as numeric-only). Instead independently attacked the file's *decisive*
claim directly on the underlying trig quantity (bypassing the
`u`-substitution machinery entirely, as a strictly independent check): a
fresh `mpmath` sweep of `\mathrm{star\_slack}=(1+\cos B)^2X_0-
\mathrm{RHS}^2` restricted only to `\cos A\ge0` (dropping the
`\beta_0<\beta_1<B` and `\angle B\le\angle C` Case-(b) conditions) gives
`\approx50\%` negative among `\approx15{,}000` valid `(A,B)` samples — even
more dramatic than, but qualitatively identical to, the file's own
`\approx37\%` finding on `\mathrm{Num}` specifically (the two percentages
differ because they measure sign-flips of related-but-distinct quantities
under slightly different domain relaxations; both decisively confirm "no
domain-free positivity"). This independently corroborates the file's core
negative conclusion from an entirely different angle (no `u`-substitution
involved at all), which is the load-bearing claim of the round (it
determines that any future certificate must be a genuine Positivstellensatz
object, not a bare SOS).

The Weierstrass substitution `u=\tan(A/6)` applied to `\cos(A/3),\sin(A/3)`
is, in principle, the textbook tangent-half-angle substitution
(`A/3=2\cdot(A/6)`), so the underlying mathematical device is sound; its
specific 466-term output was not independently re-derived this round
(time-limited), consistent with the builder's own honest non-certification.

**Verdict on this file.** Status `partial` as self-reported is accurate.
The reported findings are honest and (for the load-bearing negative claim)
independently corroborated; no overclaiming (the builder itself declines to
submit a lemma, correctly, since the central identity is numeric-only).
**CHANGES REQUESTED.** No lemma certified (none submitted; correctly so).

## 3. `coordinate-bash-resultant-boundary-pointwise-tangent.md`

**Claims examined**: exact Case-(b) domain boundary near the corner is two
distinct curves (`B=\beta_0(A)` and the implicit `X_0(A,B)=\cos^2B`), not
one; the literal tangent-line-in-`A` construction fails; `\partial X_0/
\partial B=\sin A\cos A/(2\sin^2(A+B))>0` proved exactly; numeric evidence
`\partial S/\partial B\ge0` (11,764 samples).

**Independent verification.**
- Re-derived `\partial X_0/\partial B` by hand via the quotient rule and
  the sine-subtraction identity `\cos B\sin(A+B)-\sin B\cos(A+B)=\sin A`:
  matches the claimed closed form exactly, elementary, no gap.
- Independently scanned, at `A=0.424` (the file's own witness), for the
  smallest admissible `B`: own scan finds `B\approx0.9156`, matching the
  file's `\approx0.9161`, both strictly above `\beta_0(0.424)\approx
  0.9059` — confirms the "curve `B=\beta_0(A)` lies outside the domain
  closure away from the corner" finding at this sample point. This is a
  real, reproducible structural fact but was checked only at finitely many
  `A` values, not proved as a general theorem for all `A` — appropriately
  not certified as an unconditional lemma for that reason (only the
  underlying equivalence of domain conditions, via strict monotonicity of
  `\cos`, is a general, straightforward, correct fact).
- Independently re-ran the `\partial S/\partial B\ge0` sweep (own script,
  `30{,}000` random `(A,B)` samples): first attempt (omitting the
  `\angle B\le\angle C` restriction) produced a spurious violation
  `\approx-0.5`, traced to a domain-restriction bug on this reviewer's own
  part (matching the exact pitfall this file warns about); after correctly
  imposing `B\le C`, **zero violations** among all tested points —
  confirms the file's own `0`-violation claim (though restricted to a
  smaller independent sample of `\approx1{,}500`-`3{,}000` valid points,
  qualitatively identical conclusion).
- The negative finding on the literal tangent-line-in-`A` construction
  (does not eliminate `B` from the resulting inequality) is a precise,
  honestly-diagnosed dead end, not premature abandonment — consistent with
  the two-curve domain structure found.

**Verdict on this file.** Status `partial` as self-reported is accurate;
real progress (a genuinely new domain characterization, a fully proved
derivative identity, and an honest retirement of the originally-dispatched
lever) with no overclaiming. **CHANGES REQUESTED.**

Lemma certified: `lemmas/x0-partial-b-derivative.md` (the `\partial X_0/
\partial B` identity — fully proved, elementary, gap-free). The two-curve
domain-structure finding is not certified as an unconditional lemma (only
spot-checked, not proved for all `A`) but is recorded in `current.md`.

## 4. `coordinate-bash-resultant-boundary.md`

**Claims examined**: `q_1<0` and `r_0<0` INDIVIDUALLY throughout the
correctly-restricted `P>0\wedge E<0` sub-domain (25,568 random + 40,790
grid samples, zero violations); `P>0` automatic on this locus; `B<\pi/2`
with comfortable margin; explicitly NOT proved symbolically (needs
`\beta_1`-elimination).

**Independent verification.** Built the entire pipeline from scratch (own
`mpmath` script; own `q_1,r_0` polynomials taken from the already-certified
`lemmas/case-b-e-lt-0-t-factorization.md`; own reconstruction of
`X_0,K,P,A_{\mathrm c},C_{\mathrm c},E,\beta_1,\gamma` directly from their
raw definitions, not copied from any file):
- A `2{,}000{,}000`-sample `(A,B)` sweep (own seed) restricted to the exact
  Case-(b)`\wedge P>0\wedge E<0` sub-domain found `4{,}923` valid points,
  **zero** violations of either `q_1<0` or `r_0<0`, `A`-range
  `(0.409,0.536)`, `B`-range `(0.912,1.088)` — matching the file's own
  reported `A\in(0.4067,0.5366),B\in(0.9121,1.0904)` closely. This
  independently corroborates the round's headline positive finding.
- A separate `2{,}000{,}000`-sample sweep restricted to Case-(b)`\wedge
  E<0` (no separate `P>0` filter) found **zero** violations of `P>0` among
  `5{,}144` points — confirms the "`P>0` automatic" structural finding.
- The `B`-range found (`0.912`-`1.088`) is comfortably below
  `\pi/2\approx1.571` — confirms the margin claim.

None of these numeric findings is elevated to a symbolic proof; the
builder's own honest disclosure that this requires a `\beta_1`-elimination
(resultant-based characterization of the true sub-domain) not attempted
this round is accurate and not overclaimed. The suggestive cross-approach
observation (this sub-case's extremal corner coincides numerically with
the sibling `-pointwise`'s `(A^*,B^*)`) is reported correctly as an
unproved structural link, not a formal reduction.

**Verdict on this file.** Status `partial` as self-reported is accurate;
this is the round's strongest quantitative sharpening of the shared gap
(individual sign-definiteness of `q_1,r_0`, not merely some combination),
fully independently corroborated. **CHANGES REQUESTED.** No lemma
certified this round for this file's content (none submitted; correctly
so, since the central claim is numeric-only on a transcendentally-defined
sub-domain).

## Lemma certifications this round

- `lemmas/x0-partial-b-derivative.md` — the exact `\partial X_0/\partial B`
  identity, fully proved by hand and independently re-derived; gap-free.
- `lemmas/star-corner-is-boundary-cusp-not-critical-point.md` — the
  gradient/Hessian-at-the-corner finding, independently reproduced to high
  precision at three step sizes; certified as a decisive numerical fact
  (explicitly not a symbolic theorem, since `A^*` has no known closed
  form).

Rejected (not certified, with reasons): the Case-(b) domain-emptiness claim
(spot-checked at 14-16 `A` values only, not a proof for the continuum); the
40-digit root coincidence (explicitly flagged unproved by its own builder);
the `u=\tan(A/6)`/`\mathrm{Num},n_1,n_2` reformulation (not independently
re-derived symbolically this round, and not submitted by its builder); the
two-curve domain-structure finding in the `-tangent` file (spot-checked
only); the `q_1<0,r_0<0`-on-restricted-domain finding (numeric-only, no
symbolic proof or reduction).

## current.md

Updated `results/imo-2026-02/current.md`: inserted a new "### Round 11
(this round) — proof-reviewer adjudication" section at the top of
`## Approaches tried` (all four files' independent verification, the
cross-pollination check, and the net assessment), relabeled the prior
top section "### Round 10 (this round)" to "### Round 10 (preserved)",
and left `## Status` as `partial` (unchanged — no approach reached
`solved`).

## Overall verdicts (per CLAUDE.md's per-approach routing)

- `coordinate-bash-resultant-boundary-pointwise.md`: Status `partial`
  (accurate). **Verdict: CHANGES REQUESTED.** Gap: `(\star)` itself, or a
  symbolic proof of the domain-emptiness/root-coincidence findings.
- `coordinate-bash-resultant-boundary-pointwise-sos.md`: Status `partial`
  (accurate). **Verdict: CHANGES REQUESTED.** Gap: a Positivstellensatz
  certificate for `\mathrm{Num}\ge0` using `n_1,n_2` as domain multipliers
  (not attempted — needs SDP tooling).
- `coordinate-bash-resultant-boundary-pointwise-tangent.md`: Status
  `partial` (accurate). **Verdict: CHANGES REQUESTED.** Gap: prove
  `\partial S/\partial B\ge0` symbolically (only `\partial X_0/\partial B`
  half is proved), then close the resulting 1-variable target on the
  implicit curve `X_0(A,B)=\cos^2B`.
- `coordinate-bash-resultant-boundary.md`: Status `partial` (accurate).
  **Verdict: CHANGES REQUESTED.** Gap: symbolic proof of `q_1<0,r_0<0` on
  the true (transcendentally-defined) residual sub-domain, likely via
  resultant elimination of `\beta_1`.

No approach reached `solved` this round; the shared Case-(b) gap remains
open across all four routes, now understood from four complementary
angles (a diagnosed local structure at the shared corner, an explicit
semialgebraic reformulation with domain multipliers, a monotonicity lever
with one proved building block, and a sharpened individual-sign numeric
target). Overall Status: `partial`.
