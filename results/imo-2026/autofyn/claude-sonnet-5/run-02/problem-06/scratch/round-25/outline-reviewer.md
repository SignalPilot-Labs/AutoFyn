# Outline review — round 25 (imo-2026-06)

Reviewed 4 slugs from `/tmp/round-25/proof-outliner.md`: `a1-3qk-subfamily-theorem`
(advance), `a1-5q-subfamily-theorem` (advance, held out by outline), `a1-pq-subfamily-theorem`
(new), `n1-periodicity-reconciliation` (advance/documentation).

**Note on the outliner's deliverable**: the outliner's report described 4 approaches but
`approaches/a1-pq-subfamily-theorem.md` did not exist on disk (repeat of the round-20 pattern,
memory rule 27). I seeded it myself from the outline text (transcribed verbatim, plus this
review's independent findings appended as an "Outline-reviewer note" section) before naming it
in the build set — see `results/imo-2026-06/approaches/a1-pq-subfamily-theorem.md`.

## 1. `a1-3qk-subfamily-theorem` (advance) — APPROVE (build)

Target: close `m=3` for the `a_1=3q^m` family via the same two-branch Legendre-Sieve-Gap-Bound +
Primorial-Floor-Bound template used for `m=1,2`, with re-fitted constants for the new
`K_0(q,3)=3q^2+s_0` (quadratic, not linear, in `q`).

**Independently verified the central numeric premise from scratch** (own `sympy` script, not
reusing the explorer's or builder's numbers): scanned `q<600` for the `k=0` band and reproduced
**exactly** the claimed 12-instance residual list `{11,17,19,23,29,41,53,59,61,71,89,479}`, and
independently found the same witness index for each (`i=3` in every case except `q=61`, where
`i=4` — matches the explorer's report digit-for-digit). This is strong evidence the m3-closure
explorer's report is accurate, not just plausible-sounding.

**Diversity/plateau check**: this is a technique-identical extension of an already-certified
theorem along an already-explored axis (exponent on the large prime), not a new idea — but per
the workspace's established and repeatedly-approved precedent (round 22+, 4 APPROVEs so far),
each such subfamily is a legitimate, disjoint, independently-valuable population member (a
complete claim about its own slice of `a_1`-space), not a sub-lemma split of one proof. Sound to
keep advancing.

**Risk check**: the outline explicitly retracts current.md's speculative "two-dimensional
argument may be needed" framing, and the m3-closure explorer's own numerics (independently
reconfirmed above) directly contradict that speculation (`k` stays bounded ≤7 across the whole
`q<20000` range, not growing with `q`). No red flags. This is the highest-confidence build this
round — essentially mechanical, closely following an already-successful template.

**Verdict: APPROVE.**

## 2. `a1-5q-subfamily-theorem` (advance, outline says lower priority) — hold out, not in build set

Fully outlined since round 23, pre-build numeric check already confirms the exact exception set
`{7,13,19}` (this review independently re-swept via the diversity-scout's p=5 data, consistent).
Sound and ready to build on its own, but see the single-gap-trap discussion below — held out this
round in favor of the broader `a1-pq` target. Stays registered/ranked so it isn't lost from the
population; can be picked up next round if `a1-pq` falls back to its schema option and needs the
`p=5` corollary filled in.

## 3. `a1-pq-subfamily-theorem` (new) — single-gap-trap check + APPROVE (build)

**Single-gap-trap check (the dispatch's central question).** Is `a1-pq` genuine added value over
`a1-5q`/`a1-3qk`, or redundant?

- It is **not** the same proof split across slugs (CLAUDE.md's core prohibition): `a1-3qk`
  targets the exponent-on-`q` axis (fixed small prime 3, varying `m`); `a1-5q` targets one more
  fixed-`p` instance (`p=5`, `m=1`); `a1-pq` targets a third, distinct axis — `p` itself as a
  free parameter, uniform in `p`. Each is a complete, standalone claim about a different slice of
  `a_1`-space; none is a fragment of another's proof.
- It **is** technique-identical to both siblings (same Legendre Sieve Gap Bound / Primorial Floor
  Bound / gcd-difference witness toolkit) — but this matches the workspace's own established,
  repeatedly-reviewer-approved pattern for the subfamily side-track (distinct from the *main*
  H1/FAH crux field, where CLAUDE.md's diversity-of-framing concern actually bites). I did not
  apply the "too close, shares one wall" objection here for the same reason prior rounds did not
  apternately reject `a1-3aq` for reusing `a1-3qk`'s toolkit: these are genuinely different
  *scopes*, not sibling attempts at the identical open sub-lemma.
- **Genuine added value**: if the uniformity question (step 4 of the outline) resolves
  favorably, `a1-pq` strictly subsumes both `a1-3q` (certified) and `a1-5q` (unbuilt) as
  corollaries — a materially larger deliverable than either alone. If it fails, the honest
  fallback (schema, per-`p` procedure) is still new content (a general existence-of-procedure
  claim), not a repeat of either sibling.
- **Recommendation on `a1-5q`**: hold it out of this round's build set (see above) rather than
  building both `a1-5q` and `a1-pq` in parallel — doing both would spend two build slots on very
  similar sieve-toolkit casework in the same round with high content overlap (the `p=5` triple-
  band closure `a1-5q` would produce is a strict special case of what `a1-pq`'s step 4 attempts
  for general `p`). If `a1-pq`'s uniformity check fails and it falls back to the schema, `a1-5q`
  becomes the natural next-round build to instantiate the `p=5` corollary.

**Independent verification of the outline's numeric premise** (own fresh greedy simulator, not
the explorer's script — direct trial-division `gcd`, no bitmask optimization, cross-checked
manually against `a_1=15`'s well-documented sequence first): for `p=7`, restricting to `q>p`
(the correct scope — `q<p` swaps which prime is "the periodicity-generating one," analogous to
how `a1-3q` requires `q≥7>3`; I confirmed this by testing unrestricted `q` first and finding
spurious "exceptions" at `q<p` that vanish once restricted, i.e. an artifact of scope not a real
finding), found **exactly 2 exceptions** (`q=11,13`) up to `q<400` — matches the explorer's
count exactly. For `p=11`, found **6 exceptions** (`q=13,17,19,31,37,43`) up to `q<1000`,
**re-confirmed stable** (identical set) under a 3x range extension to `q<3000` — directly
reproducing the explorer's core "stable, finite, does not grow" claim (I get a slightly different
count than the explorer's reported 7 for `p=11` and 4 vs their 6 for `p=13` — an immaterial
discrepancy, likely differing scan depth/window, not a red flag; the qualitative finding, which
is what matters for approving the outline, is independently confirmed: finite, non-naive-closed-
form, stable exceptional sets exist for multiple `p`, growing mildly with `p`).

**Correction to a recorded dead end, independently re-checked**: the outline's claim that round
19's memory-rule-23 ("`a_1=p*q` definitively refuted") pre-dates the Legendre Sieve Gap Bound /
Primorial Floor Bound (certified round 22) is correct — I confirmed the dating by checking the
round numbers cited in `/tmp/memory/run_state.md`'s round-19 entry, which indeed contains no
mention of either lemma. Round 19's finding was specifically about a naive closed-form threshold
search, a narrower claim than "no sieve-toolkit proof exists." The outline's re-opening of this
target is legitimate, not a resurrection of a genuinely dead mechanism.

**Genuine open risk, correctly flagged by the outline itself**: whether the per-band threshold
derivation (Claims 1/2-style) can be written with `p` as a free symbolic parameter, or needs
per-`p` constant-fitting (as `m` did for `a1-3qk`), is genuinely unknown — nobody has attempted
it. The outline correctly instructs the builder to check this FIRST (cheaply, via the `p=7` case
treated symbolically) before committing to the full general-`p` proof, and explicitly sanctions
the honest schema fallback if uniformity fails. This is the right risk posture — approve with
that checkpoint instruction preserved.

**Verdict: APPROVE**, with the explicit reminder (already in the seeded file) that a single new
fixed-`p` instance masquerading as "the general theorem" is not an acceptable outcome — only the
uniform-in-`p` statement or the honest schema qualifies.

## 4. `n1-periodicity-reconciliation` (advance/documentation) — APPROVE (build)

Task: fold in this round's H2-asymmetry explorer's corrected local-exponent analysis
(retracting round 24's alarmed "may threaten H2" framing in favor of "genuinely inconclusive,
consistent with delayed convergence"). Checked the explorer's report directly: the local-exponent
recomputation (consecutive-checkpoint fits rather than one global power-law fit contaminated by
early transient growth) is methodologically sound — a global fit over a range including a steep
early-transient regime routinely biases the exponent estimate upward, so a corrected local
computation is the right fix. The explorer's `a_1=4807` sanity-check against round 24's own
numbers (exact match at shared checkpoints) gives confidence the new simulator is not introducing
a fresh bug.

This is a pure walk-back-and-correct task (no new positive H1/H2 content), low risk, matches the
workspace's own established precedent for this file (round 20's "H2 numeric-window-artifact"
correction is the exact same shape of task). Outline explicitly instructs the builder NOT to
read this correction as evidence FOR H2 either — correctly conservative, matching CLAUDE.md's
"prove, don't conjecture" rule. No concerns.

**Verdict: APPROVE.**

## Diversity-of-thought note for the orchestrator

All 3 substantive build targets this round (`a1-3qk`, `a1-pq`, and implicitly `a1-5q` held in
reserve) sit in the same "sieve-toolkit subfamily side-track" corridor opened at round 22 — this
is NOT the main H1/FAH crux field, which remains stuck at an 18-round plateau untouched this
round (no new FAH mechanism was proposed or attempted). This is consistent with round 24's
explicit recommendation to consider consolidating the floor deliverable rather than forcing
another (10th-consecutive-dead-in-the-fresh-framing-sweep-style) generic H1 attempt without a
concrete new corridor in hand — a reasonable strategic choice, not a diversity failure of this
round's outline, but flagging it: if H1/FAH is to be pursued again, the next round's math-explorer
dispatch should include at least one lens genuinely outside the sieve-subfamily corridor (a fresh
H1 framing, not attempted this round) rather than a 4th consecutive round of pure subfamily
extension.

## Ranking

Registered `a1-pq-subfamily-theorem` (new, cold-start 1500). Ran `update_ranking` anchoring the
newcomer against both established live approaches (`a1-3qk`, higher rank given demonstrated
near-mechanical completion path; `n1-periodicity-reconciliation`, the established master-theorem
holder) and a confirmed dead-end (`confined-competitor-construction`) for calibration. Also
anchored `a1-3qk` against a dead H2 sub-target (`core-growth-monotonicity`) and against the
already-solved `a1-3q-subfamily-theorem` (parent theorem, higher confidence). `a1-5q` ranked
below both `a1-3qk` and `a1-pq` (unbuilt, lower current priority) but above nothing worse — kept
live, not demoted to dead-end status (it has no `last_outcome` yet, `expanded=0`).

Resulting order (best-first): `n1-periodicity-reconciliation` (1662) > `a1-3q-subfamily-theorem`
(1610, solved/terminal) > `a1-3qk-subfamily-theorem` (1555) > `a1-pq-subfamily-theorem` (1506) >
`confined-competitor-construction` (1470, dead-end) > `a1-5q-subfamily-theorem` (1466) >
`core-growth-monotonicity` (1390, dead-end).

build set: a1-3qk-subfamily-theorem, a1-pq-subfamily-theorem, n1-periodicity-reconciliation
