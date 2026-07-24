## Round 14 outline review — imo-2026-06

Read: `/tmp/round-14/proof-outliner.md`, `results/imo-2026-06/current.md`,
`results/imo-2026-06/approaches/n1-periodicity-reconciliation.md`,
`results/imo-2026-06/approaches/covering-system-construction.md` (Step 5 and the (†)
sections), `.ranking.json`.

### 1. n1-periodicity-reconciliation (revise) — CHANGES REQUESTED, but the outline's
proposed FIX MECHANISM IS FICTITIOUS; a much simpler, correct fix exists and is given
below so the builder does not waste the round chasing a non-existent tool.

The outline instructs the builder to fix the "combining both parts" gap (current.md's
diagnosis: the theorem's proof hand-waves the "landing" direction — that the real
`a_{n+1}` always lands in the broader set `G*` — by citing "Step 5's construction") by
**"re-running, verbatim in structure, the same-base/overlapping-base/disjoint-base
trichotomy already used in Step 5's own proof, against G*'s broader membership test."**

I grepped the entire workspace (`covering-system-construction.md`, `current.md`, every
approach file) for this trichotomy. **It does not exist anywhere.** Step 5's actual
proof (`covering-system-construction.md` lines 303-338) is a one-paragraph argument
with no case split at all: it defines `G := {r : sig(r) ∈ 𝒫'}` directly in terms of
membership in `𝒫'`, so "landing" is automatic by definition (ρ(n) ∈ 𝒫' for n large,
by the already-certified Extended Persistent-Type Pigeonhole — no separate argument
needed). The phrase "same-base/overlapping-base/disjoint-base trichotomy" appears to
be the round-13 reviewer's own paraphrase in `current.md` of what a fix MIGHT look
like, misread by this round's outliner as a literal existing proof technique to
"re-run." Dispatching the builder to hunt for and re-derive a trichotomy that isn't
in Step 5 would waste the round.

**The actual, much simpler fix (verified by me from scratch this round).** `G*`'s
definition (n1-periodicity-reconciliation.md lines 134-135) has two conjuncts, and the
"landing" claim — that the real `a_{n+1}` satisfies both — splits into two independent,
already-available facts, neither requiring new machinery:

- **First conjunct** (`sig(r) ∩ P(a_j) ≠ ∅` for every `j ≤ N(S*)`): since `a_{n+1}` is
  literally defined by the problem's own recursive rule to satisfy
  `gcd(a_{n+1}, a_j) > 1` for **every** `j ≤ n`, and `j ≤ N(S*) ≤ n` for the range in
  question, this holds automatically — it is exactly the certified, unconditional
  **Free Facts Lemma** (`lemmas/free-facts-gcd.md`), not a new derivation. Combined with
  `P(a_j) ⊆ S*` (self-absorption), `gcd(a_{n+1},a_j)>1 ⟺ sig(a_{n+1} mod L*) ∩ P(a_j) ≠ ∅`
  as already shown in the file's own CRT step.
- **Second conjunct** (`sig(r) ∩ B ≠ ∅` for every `B ∈ 𝒫'(S*)`): `ρ_{S*}(n+1)` is itself
  some element `A' ∈ 𝒫'(S*)`, and the theorem's own HYPOTHESIS is "FAH holds at level
  S*" — i.e. every two elements of `𝒫'(S*)` intersect. Applying this hypothesis with
  the pair `(A', B)` for every `B ∈ 𝒫'(S*)` gives exactly the needed conjunct, directly,
  with no further argument.

So "combining both parts" is not a hard gap needing a trichotomy — it is a one-line
consequence of (i) the already-certified Free Facts Lemma and (ii) directly unpacking
the theorem's own stated FAH-at-S* hypothesis for the specific type `ρ_{S*}(n+1)`. I
recommend the builder replace the vague citation at lines 158-172 with exactly this
two-line argument, re-verify the "sufficiency" direction (already correctly done in the
file, lines 145-156, unaffected), and then the Self-Absorbing Core Theorem's proof is
fully closed and certifiable, conditional only on (a) FAH-at-S* and (b) existence of a
self-absorbing S* itself — both honestly still open per the file's own §4, correctly
not attempted this round.

**Verdict: CHANGES REQUESTED**, with the outline's proposed mechanism corrected as
above (do not hunt for a trichotomy in Step 5 — it isn't there). This closes the
theorem's proof gap and should let it be certified this round.

### 2. integer-monovariant-difference-identity (new) — APPROVE for build (exploratory)

Independently re-verified the outline's aimo-0134 transplant analysis from scratch:
aimo-0134's `b_k := (a_1+...+a_k)/k` monotonicity crucially uses `a_{k+1} ≤ k` (a
per-step bound from that problem's OWN recurrence), converting `(k+1)b_{k+1} ≤ kb_k+k`
into `b_{k+1} < b_k+1` and then, by integrality of `b_{k+1}`, `b_{k+1} ≤ b_k`. Our
sequence has no such bound on `a_{n+1}` itself (`a_n → ∞`); only the GAP `g_n` is
bounded (certified Bounded Gap Lemma, `1 ≤ g_n ≤ a_1`). The outline correctly diagnoses
that the naive transplant (average the `a_n`) fails outright, and correctly redirects to
averaging the gap sequence — but then correctly and honestly identifies that the
natural averaged-gap statistic has no analogous per-step integer-forcing inequality.

I independently checked the outline's two pre-rejected candidates:
- (a) persistent-type count `|𝒫_n|` — correctly identified as literally the already-
  certified Persistent-Type Pigeonhole restated as a monovariant; no new content,
  correctly rejected.
- (b) recruited-core size `|S_n^core|` — correctly identified as circular: boundedness
  of this statistic IS gap (†) itself (the recruitment-process termination question);
  "prove it stabilizes via integrality" gives no traction since integrality doesn't
  help prove boundedness, only exploits it once already known. Correctly rejected, and
  this is not a disguised existence-shaped argument — it's a genuine restatement of
  the crux, correctly caught pre-build rather than smuggled through.

Given round 12's independent finding that EEA (a structurally similar
pigeonhole/monovariant-flavored reformulation) is provably equivalent-difficulty to
FAH, I judge it fairly likely a genuine "third candidate" statistic here will, if
found, also either collapse into (a)-shaped (a restatement of an already-certified
pigeonhole fact) or (b)-shaped (circular with (†)) — but this is a prediction, not a
proof, and the outline's own framing is honest about this risk ("if no such statistic
is found... report RETHINK honestly, itself useful information"). This is exactly the
kind of genuinely-new-vocabulary attempt CLAUDE.md's plateau-break guidance wants, it
is not a restated dead mechanism (no prior round tried an averaged-gap monovariant),
and the pre-screening was done carefully rather than skipped. **Verdict: APPROVE** for
build, with the mandatory first deliverable being the search for a third statistic
(not assumed to exist) and an honest RETHINK if none is found — do not accept a
"per-step inequality" that is asserted "by analogy" rather than derived from the
actual `gcd(a_{n+1},a_i)>1`-plus-minimality rule.

### 3. covering-system-construction (advance) — no new work proposed, kept live in
ranking for continuity. Not selected for this round's build set (matches round 13's
precedent of not dispatching a builder when "no new step proposed").

### 4. greedy-exchange-cost-potential (advance) — same as above, no new work, kept
live in ranking, not selected for build.

### Diversity check

The two build-set approaches attack genuinely different parts of the problem: (1) is
a purely conditional, secondary-gap (n=1 literal periodicity) repair, independent of
whether FAH itself is ever closed; (2) is a fresh top-level attack on FAH/periodicity
via an entirely new vocabulary (integer monovariant + difference identity) not
previously tried in 13 rounds. No shared-gap duplication between them. The two
"advance" slugs remain the field's main-crux carriers, unchanged, so the population's
overall diversity is preserved without wasting a build slot on unchanged content.

### Ranking

Registered `integer-monovariant-difference-identity` (new, cold-start). Ran
`update_ranking` anchoring the newcomer against established approaches (loses to
n1-periodicity-reconciliation and cofinite-window-capacity-bound, beats confirmed
dead-ends confined-competitor-construction and sieve-density-exception-bound), kept
covering-system-construction/greedy-exchange-cost-potential roughly drawn at the top,
n1-periodicity-reconciliation slotted just below them (real theorem-shaped progress
this round, still conditional), and cleared the stale flag on
subword-complexity-periodicity (untouched since round 12, correctly still ranked
above confirmed dead-ends and below the leaders).

build set: n1-periodicity-reconciliation, integer-monovariant-difference-identity
