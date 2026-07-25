# Round 21 proof-reviewer report — imo-2026-02

## Approach 1: coordinate-bash-resultant-boundary-pointwise-tangent (claimed Status: solved)

**Verdict: CHANGES REQUESTED. True Status: partial (not solved).**

### What I independently verified as correct

The round-21 "Case (a) is a phantom gap" argument is genuinely correct.
I re-derived and re-checked every load-bearing piece from scratch, independent
of the builder's own scripts:

1. **Fact 0** (`Y(\beta)=2\cos^2\beta-m\cos A=2\cos^2\beta-2X_0` identically):
   confirmed symbolically with a fresh `sympy` session (`sp.simplify` gives
   exactly `0` residual).
2. **Monotonicity** `Y'=-2\sin2\beta`: confirmed symbolically (fresh `sympy`,
   `0` residual).
3. **Fact 2** (`\beta_1\le\beta_0(A)\iff Y(\beta_0(A))\le0`): confirmed
   numerically over 298 valid random triangle samples with `0` mismatches
   (own `mpmath`, 50 digits, own bisection-based computation of `\beta_1`,
   not reusing the builder's code).
4. **The Lemma** (`\beta_1\le\beta_0(A)\implies Y(\beta)<0` for all
   `\beta\in(\beta_0(A),\gamma)`) and the **vacuity conclusion**
   (`(\mathrm{II})`'s hypothesis conjunction is false for every
   `\beta\in(0,\gamma)` in Case (a)): confirmed with two independent scripts,
   ~500 Case-(a) samples, each tested against ~20-30 further random `\beta`
   values — **zero violations** of either the Lemma or the vacuity claim.
5. I also traced this argument's citations against the ORIGINAL derivation
   (`coordinate-bash-resultant-boundary.md` §§15-17), not just this file's
   own round-13 restatement, and confirmed: §15's `(\mathrm{I})/(\mathrm{II})`
   system quoted verbatim matches the original text exactly; Theorem 16.1
   (`(\mathrm{I})` unconditional) and Theorem 16.2 (`Y` monotone, plus
   the `Y(\gamma)\ge0` branch) are accurately cited;
   `lemmas/mvt-lipschitz-reduction-case-b.md`'s Setup genuinely restricts to
   `\beta_0<\beta_1<\gamma` (its Step 2/3 MVT bounds use `\beta_1>\beta_0`
   essentially, so it mathematically cannot be stretched to Case (a)) —
   confirming the round-21 diagnosis that `G(\beta_1)\ge0` was never a valid
   universal target, only a Case-(b)-scoped derived simplification.

This is real, certified progress — the population's Case (a) treatment (open
since round 11, mis-diagnosed across rounds 11-20) is finally closed
correctly for the sub-case it actually addresses.

### The gap that blocks `solved`: a skipped third case, `Y(\gamma)\ge0`

The "Full proof" section's Step 2 defines `\beta_1\in(0,\gamma)` as "the
unique angle with `\cos\beta_1=\sqrt{X_0(A,B)}`" and splits into exactly two
cases: Case (a) `\beta_1\le\beta_0(A)` and Case (b) `\beta_1\in(\beta_0(A),
\gamma)` (Step 4's literal statement: "the remaining target is `G(\beta_1)
\ge0` for `\beta_1\in(\beta_0(A),\gamma)`"). But `\beta_1`, properly defined
via `\cos\beta_1=\sqrt{X_0}` with `\beta_1\in[0,\pi/2)`, need **not** lie in
`(0,\gamma)` at all — this holds iff `Y(\gamma)<0` (equivalently
`\beta_1<\gamma`, since `\cos` is decreasing and `\cos\gamma\ge\cos\beta_1
\iff Y(\gamma)=2\cos^2\gamma-2X_0\ge0\iff\gamma\le\beta_1`).

**Whenever `Y(\gamma)\ge0` (i.e. `\beta_1\ge\gamma`), neither Case (a) nor
Case (b) as literally stated applies**: Case (a)'s own criterion
`Y(\beta_0(A))\le0` is false in this regime (since `Y` decreasing and
`\beta_0(A)<\gamma` gives `Y(\beta_0(A))>Y(\gamma)\ge0`), and Case (b)'s
`G(\beta_1)` for `\beta_1\in(\beta_0(A),\gamma)` doesn't even parse (the
actual `\beta_1\ge\gamma` here is outside that stated interval). This third
scenario IS already resolved — by Theorem 16.2's *first* branch
(`Y(\gamma)\ge0\implies(\mathrm{II})` holds unconditionally throughout
`(0,\gamma)`, with no reference to `\beta_1$/`G` needed at all) — but this
branch is **never cited or mentioned anywhere in "Full proof" Steps 2-4**.

**This is not a negligible edge case.** I ran a fresh 200,000-sample sweep
(own script, `mpmath`, 30 digits) restricted to the domain-nonempty region
`\beta_0(A)<\gamma`: of 33,340 valid samples, **17,087 (≈51%)** have
`Y(\gamma)\ge0`. Concrete non-degenerate witness triangle:
`A\approx1.55400,B\approx0.74664,C\approx0.84094` (`B\le C`, `\beta_0(A)
\approx0.52920<\gamma\approx0.74664`): `Y(\beta_0(A))\approx1.475>0` (so
**not** Case (a)), and `\beta_1\approx1.48321\ge\gamma\approx0.74664` (so
**not** in Case (b)'s stated interval `(\beta_0(A),\gamma)` either) — I
directly verified `(\mathrm{II})`'s hypothesis is genuinely satisfied for
some `\beta\in(0,\gamma)` at this witness (e.g. `\beta\approx0.580`,
`0.730`), and that the target inequality does hold there (consistent with,
but not itself proved by, anything currently written in "Full proof" — it
follows only via Theorem 16.2's separately-certified first branch, which the
Full Proof text never invokes).

**Conclusion.** The Case (a) vacuity fix genuinely closes what it addresses,
but it does not make the "Full proof" section gap-free: a third, common
(~51% of the relevant domain) branch (`Y(\gamma)\ge0`, `\beta_1\ge\gamma`) is
silently omitted from the case split and never explicitly closed in the
assembled argument, even though the underlying fact needed
(Theorem 16.2's first branch) is already proved and certified elsewhere in
the population. Per CLAUDE.md's "No skipped cases" rule, this is a genuine
gap. True Status: **partial**, not `solved`. This is very likely a
one-paragraph fix for round 22 (state the trichotomy `Y(\gamma)\ge0` /
`Y(\beta_0(A))\le0<Y(\gamma)` (Case b) / `Y(\beta_0(A))>0` (Case a, this
round's fix covers `Y(\beta_0(A))\le0` — note Case (a) and the new branch
are NOT mutually exclusive complements of Case (b); the exact trichotomy
needs to be restated precisely as `Y(\gamma)\ge0` vs `Y(\gamma)<0`, and
within the latter, `\beta_1\le\beta_0(A)` (round 21's Case a) vs
`\beta_1>\beta_0(A)` (Case b) — the round-21 builder should double check
this exact partition is exhaustive and disjoint when writing the fix).

**Files updated:** reverted the file's own `## Status` header from `solved`
to `partial` with a proof-reviewer correction note explaining the finding
(preserving the round-21 builder's text below, unmodified, for the audit
trail — matching this population's established convention from rounds 17-20).
Updated `results/imo-2026-02/current.md` with the full round-21 adjudication.

**Promotable lemma certified**: the file's own "Case (a) vacuity lemma"
(Promotable lemmas, Round 21 addition) is correctly stated (properly scoped
to the `\beta_1\le\beta_0(A)` hypothesis, no overclaiming) and is certified
as valid — already resident in the approach file's own promotable-lemmas
section; no separate `lemmas/` file needed since its statement already
carries the precise hypothesis.

## Approach 2: spiral-similarity-bootstrap (claimed Status: partial)

**Verdict: APPROVE the Status as filed (partial, not overclaiming). CHANGES REQUESTED
in the routing sense (real progress, gap remains) — no RETHINK, approach is sound.**

### Verified independently

1. **New lemma `\angle(AQ,AB)=-\angle B\pmod\pi`, `\angle(AQ,AC)=-\angle C
   \pmod\pi`** (where `Q` is the already-certified fixed point with
   `AQ\parallel BC`): the hand proof (three-line chain-rule/antisymmetry
   argument from `AQ\parallel BC` alone) is elementary and correct. I
   independently reconstructed the entire configuration numerically from
   scratch (own `numpy` script, concrete triangle `A=(0.3,1.1),B=(-1,0),
   C=(1.3,-0.1)`, own circumcenter formula, own foot-of-perpendicular
   computation for `Q` — not reusing the builder's code) and got exact
   matches to 14 significant digits for both identities. **Certified** —
   written to `results/imo-2026-02/lemmas/aq-angle-with-ab-ac.md`.

2. **The "vantage-pair equivalence" structural finding** (part (c)-(d)):
   the claim that all three vantage-pair forms of the four-point
   concyclicity criterion for `A,K,L,Q` are logically equivalent, and that
   (given the current certified toolkit's facts are all of the syntactic
   shapes (i)-(iii) listed) none of them can be closed by chain-rule
   combination alone, is a correct piece of elementary reasoning (concyclicity
   is a single well-defined property; the three "which pair is vantage"
   inscribed-angle criteria are standard and mutually equivalent). The
   syntactic-shape argument in part (d) is an honest, carefully-scoped
   negative finding, not a proof of impossibility for all future approaches
   (it only rules out chain-rule combinations of the *currently certified*
   facts, which is exactly what it claims — no overclaiming).

3. **Status accuracy**: the file correctly states Status `partial`, does not
   claim to have closed any gap this round beyond the new lemma, and clearly
   flags the load-bearing gap (a relation tying a line through `A`/`Q` to a
   line through `K`/`L`) as still open. This matches CLAUDE.md's
   `partial` definition exactly — a proven lemma/reduction, real progress,
   proof not complete.

No issues found. This file's self-assessment is accurate.

## Ranking tool calls

- `record_outcome(imo-2026-02, coordinate-bash-resultant-boundary-pointwise-tangent, round 21, outcome=partial, ...)` —
  recorded (a false `solved` claim caught and corrected, real sub-lemma
  advance retained).
- `record_outcome(imo-2026-02, spiral-similarity-bootstrap, round 21, outcome=partial, ...)` —
  recorded (accurate partial, one new certified lemma, one honest negative
  structural finding).

## current.md

Updated `results/imo-2026-02/current.md`: `## Status` remains `partial`
(unchanged from round 20 — no APPROVE this round). Added a new "Round 21 —
proof-reviewer adjudication" section documenting: (1) the Case (a) vacuity
fix's independent re-verification and certification, (2) the newly-found
`Y(\gamma)\ge0` skipped-case gap that blocks `solved`, with the numeric
evidence (51% frequency, explicit witness triangle), (3) the
spiral-similarity-bootstrap round's accurate self-report and the newly
certified lemma. Population note: this is (at least) the fourth instance
across rounds 17-21 of a near-`solved` claim on this exact route being
caught and corrected by the proof-reviewer before landing — the gap is now
very narrowly diagnosed (one omitted branch, whose closing fact is already
proved) and should be closable quickly in round 22.

## Files touched this round
- `/home/agentuser/repo/results/imo-2026-02/current.md` (updated, Round 21 section added)
- `/home/agentuser/repo/results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
  (Status header corrected from `solved` to `partial`, reviewer-correction note added)
- `/home/agentuser/repo/results/imo-2026-02/lemmas/aq-angle-with-ab-ac.md` (new, certified)
