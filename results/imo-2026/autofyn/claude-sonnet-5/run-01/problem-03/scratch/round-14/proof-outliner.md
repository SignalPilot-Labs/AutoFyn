## imo-2026-03

**No new slug opened.** Per CLAUDE.md's single-gap-trap warning, this round's revision stays inside
the sole live approach, `potential-weighting-upper-bound` (only redundant field is
`dyadic-cascade-induction`/`concavity-minimax-duality`, both re-confirmed benched — none of the three
round-14 explorer reports (Gap1a/Gap1b/Gap1c lenses) surfaced anything usable by either: the lower
bound is already unconditional (round 8) and no report produced an `A`-generic upper-bound
statement). `elementary-exchange-smoothing` stays retired.

`potential-weighting-upper-bound`: **advance** (existing live approach, gaps re-planned in place —
new §21 appended to `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`, §19-20 left
intact as history).
Target: the whole theorem's upper bound (`g(D_m,m)=e_m\cdot S(D_m)`, i.e. Liu Bang cannot do better
than the dyadic construction guarantees) — closing the residual "Gap 1" (existence of a non-`w_1`-
matching optimal witness on the non-dominated prefix of the scope family `\mathcal F`) closes Claim A,
which closes Sharp Argmin Recovery, which closes the entire upper bound (the lower bound is already
unconditional since round 8).
Technique: same overall route as before (D/M operation reformulation + recursive DELETE/KEEP/MATCH
peeling on the scope family `\mathcal F`, reduced via the certified Background-Splitting Corollary to
`|C_{\mathrm{lo}}|\in\{1,2\}`), now with three sharper/simpler sub-mechanisms for the residual case
split.

Skeleton (new §21, reconciling the three round-14 explorer reports):
  1. **Gap 1a (No-Gap Lemma base case) — new, much simpler elementary route.** Step 1 (proved,
     no hypothesis): for any `j`, `A_1\le|b_0-z_j|$ via the single selection "keep `z_j`, delete
     everything else." Step 2 (the one open sub-lemma, new this round): **Deletion-Suffices-for-`k^*`**
     — conjectures `M=A_{3,k^*}=|b_0-d_{k^*}|` exactly (`k^*`'s own recursive sub-problem is always
     optimized by deleting its entire residual list), conditional on trigger+global-argmin. Step 3
     (proved, given Step 2): monotonicity of `|b_0-\cdot|` plus Step 1 gives `A_1\le|b_0-z_j|\le
     |b_0-d_{k^*}|=M`, contradicting the strict trigger — a 3-line closure of the half-open No-Gap
     Lemma, replacing round 13's stuck Coincidence-Identity sign argument as the primary mechanism.
  2. **Gap 1b (Sum Bound) — piecewise-linear/breakpoint mechanism, sharper tightness.** Corrected
     round 13's "comfortable margin" claim further: both the multiplicative ratio (`\to2`) AND the
     additive gap (`\to0`) can vanish (new 2-parameter family), and exact equality of the *full* Sum
     Bound occurs at genuine finite instances (`21/822`, exact witness on file), always at a
     `\mathrm{KEEP}=\mathrm{DEL}` tie or a Lemma-P duplicate configuration. Recommended mechanism:
     freeze one coordinate, observe `w_1-\mathrm{OPT}_{+1}-\mathrm{OPT}_{-1}` is piecewise-linear in
     it (finite min/max of affine branches), so its minimum is at a breakpoint — same technique family
     that closed the all-cycles gap (Shared-Value Cycle-Breaking Lemma / Vertex Lemma). Enumerate 3
     breakpoint types (A_1-branch tie -> Lemma P; KEEP=DEL tie -> Rank-Extraction; `d_{k^*}` colliding
     with another `z` -> untested) and reduce the Sum Bound to each, not yet attempted.
  3. **Gap 1c (MATCH-vs-DEL/KEEP) — Shrink-List Monotonicity Lemma (certified outright) + retargeted
     half-step sub-lemma.** New fully general lemma, proved by a one-line bijection ("optimal
     selection of the smaller list, plus delete the extra element, is a valid selection of the bigger
     list with the same value since deletion contributes 0"): `\mathrm{OPT}_{+1}(C,W)\le
     \mathrm{OPT}_{+1}(C,W\setminus\{x\})` for ANY `C,W,x` — no `\mathcal F`-restriction, 14,000+
     arbitrary-instance corroboration. This isolates Gap 1c's entire remaining difficulty into one
     narrower "half-step" claim: `\mathrm{OPT}_{+1}(C\cup\{d\},X)\ge\mathrm{OPT}_{+1}(C,X)` for
     `d=w_1-w_m`, genuine `\mathcal F`-provenance (0/3400+ violations within `\mathcal F`, ~15% failure
     the instant provenance is dropped, even keeping the exact structural relation `d=w_1-w_m`
     intact). Corrected an internal inconsistency in the explorer's own report: this half-step is
     background-shrinking (not list-shrinking) and is NOT the free Shrink-List lemma nor the already-
     dead general background-insertion monotonicity — it is the one genuinely open, provenance-
     specific sub-lemma.

Key lemmas (claim + mechanism):
  - Deletion-Suffices-for-`k^*` (Gap 1a's Step 2) — conjectured, NOT proved; mechanism if true: the
    trigger `M<A_1` forces `k^*`'s recursive sub-problem toward its "floor" value `e({b_0,d_{k^*}})`
    because any improving selection inside `Z_1` could be re-embedded (two untried directions: into
    `A_1`'s own bigger search space, or into a rival partner's `A_{3,l}$) to contradict either the
    trigger or `k^*`'s global minimality — neither embedding is worked out yet; this is the precise
    open gap, not hand-waved.
  - Shrink-List Monotonicity Lemma — proved in full this round (one-line bijection via the
    deletion-contributes-0 convention); recommend certifying to `lemmas/` immediately, pending only a
    builder's one-line check that this convention matches the file's own `\mathrm{OPT}_\sigma`
    definition (§13.2/§17.2) exactly.
  - Half-step lemma (Gap 1c's real content) — conjectured, NOT proved; because it fails ~15% of the
    time outside `\mathcal F` even with the exact structural relation `d=w_1-w_m` preserved, and two
    cheap sufficient conditions (domination `d\ge\max(C)`; general background-insertion monotonicity)
    are both refuted, the true mechanism must be a *positional* fact about where `d` sits relative to
    the working list — structurally the same flavor as Gap 1a's No-Gap Lemma. A concrete untested
    hypothesis (flagged, not run): does a generalized No-Gap property directly imply the half-step?
  - Sum Bound tight-instance diagnosis — proved this round (not conjectural): every located exact-
    equality witness of the Sum Bound is, verifiably via the certified Rank-Extraction identity, a
    `KEEP=DEL` tie or a Lemma-P duplicate configuration — grounds the recommended breakpoint mechanism
    in an actual verified pattern, not just intuition.

Open gaps (unchanged in count, sharpened in content — this is a re-plan, not a closure):
  - Gap 1a: Deletion-Suffices-for-`k^*` (Step 2 above) — **PRIORITY BUILD TARGET 1**, most promising:
    27,000+ corroborating checks, a concrete non-vacuity counterexample confirming it's a real
    hypothesis, and a 3-line path to the full Gap 1a closure once it's proved.
  - Gap 1c: the retargeted half-step lemma — **PRIORITY BUILD TARGET 2**, comparably well-isolated
    (3400+ checks, 0 violations within scope) with a suspected (untested) shared mechanism with Gap 1a.
  - Gap 1b: the Sum Bound via the breakpoint/piecewise-linear mechanism — **PRIORITY BUILD TARGET 3**
    (concrete mechanism, reuses certified Vertex Lemma technique, but requires a full breakpoint-type
    enumeration not yet attempted — more remaining work than 1/2).
  - Shrink-List Monotonicity Lemma — **recommend immediate certification**, not really a "gap":
    already proved, just needs the one-line convention check and write-up.
  - `\sigma=-1` mirrors of the Sum Bound and the half-step lemma — queued, cheap, not yet formulated/
    attempted; lower priority than the `\sigma=+1` primaries above.

Cases to cover: `|C_{\mathrm{lo}}|=0` (already fully closed, Empty-Background Lemma); `|C_{\mathrm{
lo}}|=1` (vacuous within `\mathcal F`, conditional on Gap 1a/No-Gap — if a future deeper sweep ever
finds a genuine `|C_{\mathrm{lo}}|=1` node, the shelved general fallback lemma `math-explorer-
shallowest-case.md`'s Gap 1d from round 13 becomes live again); `|C_{\mathrm{lo}}|=2`, both signs
`\sigma=\pm1` (the sole remaining live case, split into Gap 1b (KEEP-vs-DEL) and Gap 1c (MATCH-vs-
DEL/KEEP), per the already-certified split).

Watch out for: (i) do not conflate the free, general Shrink-List Monotonicity Lemma (background
fixed, list shrinks) with the retargeted half-step lemma (list fixed, background shrinks) — they look
superficially similar, the explorer's own write-up initially mislabeled them as the same general
lemma, and I corrected this explicitly in §21.3; a builder who doesn't notice the correction could
waste a whole round "proving" the half-step by misciting the free lemma. (ii) Any "fully general /
provenance-free" version of Deletion-Suffices, the half-step, or the Sum Bound is now confirmed FALSE
in every tested case (this round and last) — every valid proof must explicitly use the trigger
`M<A_1` and/or `k^*`'s *global* argmin-ness, never a generic domination/size bound alone. (iii) Do not
report any "comfortable margin" for the Sum Bound in any sub-case — this round's exact finite
equality witness (ratio AND additive gap both driven to their limits) supersedes round 13's own
already-once-corrected note; any proof must be genuinely tight, zero slack. (iv) Gap 1a's Step 2 and
Gap 1c's half-step are both suspected (not proved) to hinge on the same underlying positional
mechanism tied to `k^*`'s global argmin-ness — worth testing the implication directly, but do not
assume closing one automatically closes the other without checking.

**Did not un-bench `dyadic-cascade-induction` or `concavity-minimax-duality`** — reconfirmed no new
leverage from any of this round's three reports (the lower bound is done; none of the three findings
produces an `A`-generic statement usable by `concavity-minimax-duality`'s machinery). Did not open a
5th slug — all three explorer leads target the same single residual gap of the same whole-problem
approach, exactly the case CLAUDE.md's single-gap-trap warning describes; opening rival slugs for
Gap 1a vs. Gap 1b vs. Gap 1c would fragment one proof's remaining case split across multiple "whole
attempts," which is not what a slug is for.

**Priority build targets for this round's builder(s), in order:** (1) certify Shrink-List
Monotonicity Lemma outright (cheap, essentially done); (2) attempt Deletion-Suffices-for-`k^*` (Gap
1a) — highest expected payoff, most corroborated, shortest remaining path to a full sub-proof; (3)
attempt the retargeted half-step lemma (Gap 1c) — comparably ready, worth trying alongside/after (2)
given the suspected shared mechanism; (4) the Sum Bound breakpoint enumeration (Gap 1b) — concrete but
more work, third priority. All three of (2)-(4) are realistic single-round targets if a builder
follows the concrete embedding/breakpoint constructions sketched in §21, but none should be assumed
solvable — if a builder gets stuck, report exactly which embedding/breakpoint direction fails and why,
per CLAUDE.md's "no hand-waving" and the population's established "report the counterexample, not
just 'may need more care'" practice.
