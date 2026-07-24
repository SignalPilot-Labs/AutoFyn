# Outline review — round 10 — imo-2026-06

Read: `current.md`, all three round-10-touched approach files in full
(`covering-system-construction.md` Steps 11/11.5, `greedy-exchange-cost-potential.md`
ROUND 10 section plus its round-7 Lemma K discussion, new
`confined-competitor-construction.md`), `/tmp/round-10/proof-outliner.md`, and the
certified lemmas cited by all three (`confined-gcd-lemma.md`,
`cofinite-sufficiency-lemma.md`, `successor-transport-reduction-lemma.md`,
`generalized-bounded-gap-lemma.md`). Ran independent numeric checks (Python,
trial-division factorization, no sympy) on `a_1=4807` (the standing |F'|,|F''|≥2
rogue-pair seed) to sanity-test the reasoning, not just trust the write-ups.

## Context recap
The whole problem is unconditionally reduced (certified, unconditional chain: Free
Facts → Bounded/Generalized Bounded Gap Lemmas → Finite Core Theorem → Generalized
Bounded Witness Lemma → Projection Lemma → Collateral-Safety Theorem → Lemma G →
Confined-GCD Lemma → Cofinite Sufficiency Lemma) to exactly one open hypothesis:
Joint Cofinite FAH / the Successor Claim (does `q*` eventually divide every
subsequent occurrence of the rogue-pair's persistent type, all-but-finitely-often).
Nine prior mechanisms are dead (Lemma I's four-tool diagnosis, plus 5 more since).
All three of this round's approaches target exactly this crux, from three different
proof shapes. This is fine per CLAUDE.md — they're not fragments, they all target
the whole problem via the same certified, unconditional reduction chain, and prior
rounds established that reduction is the entire remaining content of the problem.

## 1. `covering-system-construction` — Step 11 "Growth-Forced Divisibility" — APPROVE (build)

- **Not circular, not already-falsified.** Step 11.0–11.2 build a genuinely new
  quantitative use of the Generalized Bounded Gap Lemma (as a numeric value-vs-index
  ceiling, not merely an existence bound) — Lemma I's diagnosis specifically says no
  certified tool LINKS two occurrences' divisor-class data; this is the first attempt
  to do so via magnitude, not existence. It imports only certified, unconditional
  facts (Confined-GCD Lemma, Cofinite Sufficiency Lemma, Generalized Bounded Gap
  Lemma) — no dependence on any previously-falsified claim (Universal Glue Prime,
  PUCL, Universal Singleton Hypothesis, Recruitment-Budget Lemma, etc. are all
  correctly avoided).
- **The central "Escape-Cost Lemma" (Step B) is honestly unproved and correctly
  flagged as speculative**, with the exact right self-diagnosed risk in 11.4: linear
  value-ceiling growth vs. linear index-gap growth may simply cancel, giving no net
  squeeze. I checked this arithmetic independently: Step A's sandwich is
  `g ≤ V ≤ g·a_1` (g = index gap, V = value gap) — both bounds are LINEAR in g with
  FIXED constants, so nothing in Step A alone forces the "cost of repeating the same
  bad class grows with repetition count k" claim of Step B; that growth would have to
  come entirely from the "recursively constrains earlier terms" hand-wave, which Step
  11.3 admits is not yet a mechanism ("only the tautological restatement that the
  greedy rule skipped it"). This is a real, currently-unclosed gap, but it is the
  outline's own honestly-declared target, not smuggled past as if solved — correctly
  scoped as CHANGES-REQUESTED-style content the builder must attempt, with an
  explicit numeric premise-check (11.2c) to run first. No fix needed before build.
- **Step 11.5's rejection of a standalone Return-Time Boundedness Lemma is sound
  reasoning.** It correctly identifies that Persistent-Type Pigeonhole gives only
  infinitude, no density/gap bound, and that the natural route to a gap bound (a
  residue-mod-`S₀` density argument) requires exactly the "eventually legality is
  governed by residue mod `S₀`" fact — which round 5's `reversible-transition-map`
  proved is logically equivalent to (†) itself. One caution for the record: that
  equivalence result was **not certified** as a portable lemma (round 5: "correct
  mathematical conclusion, but not certified — informal proof style"); using an
  uncertified-but-almost-certainly-correct result to justify NOT opening a target is
  the conservative, low-risk direction (avoiding wasted build effort, not overclaiming
  a proof), so this is an acceptable use, but the builder/future rounds should not cite
  "S-sufficiency ⟺ V=∅" as if it were a certified fact elsewhere.
- **Numeric spot check (this review).** I regenerated `a_1=4807` to N=8000 terms from
  scratch (fresh trial-division script) and confirmed Q={19,11,23}, `a_{n_A}=4845`
  (3·5·17·19), `a_{n_B}=4862` (2·11·13·17) — exact match to every prior round's
  reported values for this seed, corroborating that the object Step 11 operates on is
  real and consistently computed across rounds. (My own quick pass using a loose
  "Q-superset" proxy for A′-occurrences, rather than the exact extended-type
  `ρ(n)=A′` equality, produced a noisy, high-failure-rate table — this is a
  methodological artifact of the sloppy proxy, not a counterexample to any certified
  claim; it reinforces this workspace's own memory rule to always use the correctly
  RECRUITED, exact extended type, not a cardinality/superset proxy, before treating any
  count as a real FAH statistic.)
- **Verdict: APPROVE.** Sound, non-circular, genuinely new mechanism; the flagged gap
  is real and openly owned, with a concrete cheap-kill instruction. Build it.

## 2. `greedy-exchange-cost-potential` — ROUND 10 "Escape-Budget attack on the Successor Claim" — APPROVE (build)

- **Genuinely different from round-7's dead Lemma K / Blocking-Data Bridging, not a
  restatement.** I compared the two constructions directly. Lemma K (round 7) rounds
  `a_n` DOWN to the nearest multiple of a non-dividing prime `q` (an artificial,
  retrospective competitor with no forced relationship to `a_n`'s own factorization —
  this is precisely why it died: "no established relationship between P(c) and
  P(a_n)"). This round's Escape-Budget mechanism instead examines the REAL, actually
  realized next term(s) of the sequence in the window `(a_{n_j}, a_{n_j}+a_1]` using
  the greedy rule's own minimality directly — no artificial constructed integer at
  all. That is a structurally different object (the actual next choice vs. a
  retrospective round-down), and it is anchored to the NOW-CONTROLLED alphabet
  `Div(b)` (Confined-GCD Lemma), unavailable in round 7. This matches the dispatch's
  request for "the concrete repair of Lemma K's exact defect."
- **One imprecision worth flagging to the builder (not fatal, already partly
  self-flagged).** Step 2's window `(a_{n_j}, a_{n_j}+a_1]` is stated via the
  single-step Bounded Gap Lemma (`a_{m+1} ≤ a_m + a_1`), but the quantity the
  Successor Claim needs constraints on is `a_{n_{j+1}}` — the NEXT *A′-occurrence*,
  which can be many real sequence-steps away from `a_{n_j}`, not necessarily the
  literal next term of the whole sequence. The skeleton doesn't yet clarify whether
  "the window" means one real step or the full telescoped window up to the next
  A′-occurrence (approach 1's Step A handles exactly this telescoping explicitly;
  approach 2 does not). This should be made precise early, since it changes what
  "every `q*`-multiple in the window is illegal" is actually asserting. The file
  already flags the deeper version of this same imprecision under "Watch out for" and
  "UNPROVED... only the tautological restatement" — I'm sharpening it, not
  discovering a new fatal flaw. Builder should resolve this FIRST (cheap, structural)
  before any general-case attempt.
- **Circularity risk is explicitly named and appropriately scoped** (Open Gaps,
  third bullet): the builder is told to check the illegality witness is a FINITE,
  already-certified fact (e.g. Free Facts against one term), not full
  S₀-sufficiency. Correct caution, not itself a flaw in the outline.
- **Verdict: APPROVE.** Genuinely new mechanism (verified against the actual Lemma K
  construction, not just by the file's own say-so); real open gaps, honestly flagged,
  buildable.

## 3. `confined-competitor-construction` — NEW — APPROVE, with a strong caution (build, but flag the risk explicitly)

- **Genuinely distinct proof shape from 1 and 2** (constructive existence + greedy
  minimality contradiction, vs. approach 1's far-index magnitude squeeze and
  approach 2's local window-illegality argument about the sequence's own actual
  choices) — satisfies CLAUDE.md's diversity mandate on mechanism, even though (as
  the outliner and the file itself say) all three are expected to converge on the
  same underlying "control an arbitrary earlier term's shared prime" wall. This is
  acceptable diversity of proof shape, not fake diversity of labeling.
- **However, this is structurally very close to the already-dead Lemma K, and the
  file's own honesty is the main thing saving it.** Lemma K rounded `a_n` DOWN to the
  nearest non-dividing-prime multiple below it; this approach's `c` rounds UP to the
  smallest `q*`-multiple exceeding `a_{n_j-1}` — essentially the mirror construction,
  now with ONE coordinate (`q*`-divisibility, plus `gcd(c,a_{n_B})` via Confined-GCD)
  controlled, but Step 2/3 explicitly and correctly admits `gcd(c, a_i)` for
  arbitrary OTHER `i < n_j` is NOT pinned down by Confined-GCD Lemma (which only
  controls the relationship to `a_{n_B}` specifically) — this is exactly Lemma K's
  fatal gap, restated honestly rather than hidden. The file's own "Watch out for"
  section says explicitly: if Step 2 fails for the same reason, RETHINK cleanly, do
  not force a rescue. I agree this is the right standard to hold it to, and it is
  right that the reviewer's role here is to make sure this instruction survives into
  the build round loudly, not to block the attempt (the Confined-GCD Lemma genuinely
  is new relative to round 7, so testing whether it actually changes the outcome is
  legitimate, not pure repetition).
- **Additional gap the builder must check early (not flagged in the file): whether
  `c` is even well-defined as smaller than `a_{n_j}`** — Step 3 admits "must be
  checked case by case, not assumed for large `q*`" but doesn't give a first
  numeric check. Builder's first move should be a direct computation of `c` and
  `a_{n_j}` on the standing `a_1=4807`/`11305` rogue-pair data (same seeds used
  throughout this workspace) to see whether `c < a_{n_j}` even holds before
  attempting Step 2's harder legality claim — cheaper kill than jumping straight to
  Controlled-Competitor Legality.
- **Verdict: APPROVE for build, with the explicit expectation (shared with the
  outliner) that this is the highest-risk of the three and most likely to reduce to
  a documented RETHINK matching Lemma K's exact failure mode** — that outcome is
  still valuable (confirms Confined-GCD Lemma alone is insufficient to repair the
  constructive-competitor family), so it is worth the build slot this round.

## Diversity assessment across the build set
All three approaches funnel into the same certified reduction (Joint Cofinite FAH is
the sole remaining gap for the WHOLE problem, established over 9 rounds) — this is
expected and correct, not a sign of fragmentation (CLAUDE.md's "whole attempt"
requirement is about each approach targeting the problem's actual claim end-to-end,
which all three do via the certified chain, not about avoiding a shared crux once
one has been rigorously isolated). Within that shared target, the three proof
SHAPES are genuinely different: (1) a magnitude/AP-style far-index squeeze, (2) a
local window-illegality argument using the sequence's own real next choices, (3) an
explicit constructive competitor + minimality contradiction. This satisfies the
diversity mandate. Flag for next round if all three converge on the identical
"uncontrolled factorization against an arbitrary earlier index `i`" wall (as
happened to Lemma K, Lemma F, and Lemma I already) — per CLAUDE.md's plateau-breaking
rule, if that happens for a 4th time, next round's explorers should be told to find a
mechanism that supplies information about an arbitrary earlier term's factorization
directly (not via a single fixed witness or a counting/pigeonhole argument over one
divisor value), since that is now the precisely-diagnosed missing ingredient no
tool in this workspace supplies.

## Registration and ranking
- Registered new approach `confined-competitor-construction` (cold-start Elo 1500).
- Ranked this round: `covering-system-construction` vs `greedy-exchange-cost-potential`
  drawn (both made comparably honest, comparably-scoped progress this round, both
  remain the two established leaders); both beat `confined-competitor-construction`
  (new, cold-start, and structurally closer to an already-dead mechanism) and beat
  `cofinite-window-capacity-bound` (its content is now folded into
  `covering-system-construction` Step 11, correctly left stale/unbuilt this round);
  `confined-competitor-construction` beats the three confirmed-dead approaches
  (`reversible-transition-map`, `recruitment-round-charging`, `seed-coupling-induction`)
  as a live, freshly-scoped mechanism outranks confirmed dead ends. Post-update Elo:
  covering-system-construction ~1834 (leader), greedy-exchange-cost-potential ~1782,
  confined-competitor-construction ~1535 (new), seed-coupling-induction ~1530,
  cofinite-window-capacity-bound ~1528 (correctly below the two leaders it was folded
  into), recruitment-round-charging ~1453, reversible-transition-map ~1405 (both
  confirmed dead-ends, correctly at the bottom of the live-ish tier).
- No copy_approach needed this round — no approach proposed two viable parallel
  gap-fills within itself.

## build set: covering-system-construction, greedy-exchange-cost-potential, confined-competitor-construction
