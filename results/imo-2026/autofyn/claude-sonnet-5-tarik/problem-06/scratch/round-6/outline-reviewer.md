## imo-2026-06 — Round 6 outline review

Read: `/tmp/round-6/proof-outliner.md`, all four touched approach files (full),
`results/imo-2026-06/current.md` (Round 5 update), and all three round-6
explorer reports. Independently re-derived/re-simulated the load-bearing
claims (not just trusted the write-ups) — see verification notes under each
item.

### 0. Independent verification performed

- **Lemma FOM re-derived by hand** (the algebra in both the explorer report
  and `persistent-backbone-monovariant.md`'s Step 1 checks out: admissibility
  of a candidate depends only on its radical; a direct argument — cleaner than
  the outline's own phrasing — gives an immediate contradiction `a_{i+1}≤T_C<
  a_{i+1}` without needing the outline's extra "forces equality, then i+1=n"
  detour, but both routes are valid and the conclusion `a_n=T_C` is correct).
- **Lemma FOM re-tested numerically on 9 fresh `a_1` values never used by any
  prior round's explorer** (`39,210,77,286,1001,30030,385,102,285`, exact
  radical-generation via a heap-based smooth-number search for `T_C`, not
  brute force): **1442 first-occurrence checks, zero violations.** Confirms
  the lemma independently, not just trusting the fan-structural explorer's
  own 6000+-instance claim.
- **`a_1=247` freeze mechanism (motivating `forced-primes-well-ordering`'s
  Round-6 outline) reproduced from scratch** with a correct antichain
  simulator (validated first against the already-solved `a_1=15` case: exact
  match `a_9=45`, `a_10=48`, i.e. `T=8,L=30`). Confirmed exactly: `S={13}`
  and `S={19}` each reach 3 minimal elements by `n=5` and **never change again
  through `n=5999`, zero collapse events** — matches the outline's claim
  precisely. Also confirmed the causal mechanism: the first `S={19}`-imprint
  term (`a_3=266`, `rad={2,7,19}`) is disjoint from `T_{\{13\}}=2197=13^3`,
  permanently blocking it via the (elementary, correctly stated)
  Permanent-Inadmissibility Lemma.
- **`a_1=2747`, `S={41}` self-check reproduced**, confirming (as the outline
  itself demands before trusting the Freeze Criterion) that this channel
  genuinely does NOT freeze: real collapse events at `n=11,12,13,162`,
  contradicting the freeze hypothesis, exactly as the outline predicted.
  (Note: my first attempt at this check had a bookkeeping bug — conflating
  "every realized radical with imprint `S`" with "every radical that was
  ever inclusion-minimal with imprint `S`" — corrected before drawing any
  conclusion; flagging this because it is an easy trap for a builder to fall
  into too, see "Watch out" below.)
- **Grepped all four approach files for resurrected refuted mechanisms**
  ("increasing order", "max(S)", "smallest available", etc.) — none found;
  all four outlines correctly avoid the two mechanisms this round's
  explorers just refuted (`a_1=105` kills "extra primes `<max(S)`",
  `a_1=2747` kills "companions recruited in increasing order").
- **Confirmed FOM is genuinely new**, not a restatement of the already-
  certified Record Characterization Lemma (that lemma gives an order-
  theoretic membership criterion for `𝓥`, with no reference to an exact
  numeric value; FOM adds the exact value `T_C` and the conditional
  fan-size bound — different content).

### 1. persistent-backbone-monovariant (revise) — Lemma FOM, Fan-Size
Corollary, Generation-Chain Lemma, open Growth-Budget Lemma

**Verdict: CHANGES REQUESTED.**

- Lemma FOM's proof is sound (independently re-derived and re-tested, see
  §0). This is legitimate, provable, foundational new content, correctly the
  designated certification home for it.
- Generation-Chain Lemma is correctly scoped as a "free" three-line
  consequence of the already-certified No-Resurrection Lemma — the outline
  is explicit that chain LENGTH is not new difficulty, only chain COUNT is.
  This framing is honest, not inflated.
- Growth-Budget Lemma (Step 4) is honestly marked open, with the exact
  obstruction named ("pointwise-in-`n` control ≠ cumulative finiteness" —
  citing the already-known Markov/Cauchy-Schwarz insufficiency from round
  3/4). No overclaiming.
- **Concern (see §4 below): this Step-4 mechanism is very close to
  `imprint-automaton-periodicity`'s Step-3 mechanism** — both combine Lemma
  1's linear growth with FOM's fan-size corollary via a
  density/pigeonhole-style argument to try to convert a pointwise bound into
  a cumulative one. This is the SAME missing bridge, not two independent
  attempts at it.

### 2. core-depth-induction (new) — strong induction on |S|

**Verdict: CHANGES REQUESTED**, with an explicit early-verification
instruction for the builder (see below) — not RETHINK, because nothing false
is claimed and the induction schema itself is legitimate, but there is real,
articulable doubt about whether it can work at all that the builder must
resolve FIRST, not paper over.

**Well-foundedness check (dispatch item 2).** The measure `|S|∈\{1,\dots,
k-1\}`, `k=ω(a_1)` fixed once `a_1` is fixed, IS a genuine well-founded
finite order — this part is sound and not circular as a *schema*. The
concern is different from circularity: **it is currently unknown, and not
even sketched, whether the schema's inductive step corresponds to an actual
logical dependency.** Concretely:

- The outline's own obstacle (a) is exactly right and, on inspection, looks
  serious: Theorem CD's core decomposition partitions *radical values* by
  `S(C):=C∩P_1`, a fixed finite index set — but it says nothing about a
  hierarchy or dependency *between* different cores `S`. There is no
  established map from "depth-`d` unknowns" to "depth-`(d-1)` knowns"; the
  only evidence offered is a structural *resemblance* (absorbing radicals at
  depth 2 have the shape `S∪{q}`, same shape as depth 1) — the outline
  itself, correctly, refuses to call this a reduction.
- **A further concern the outline does not fully surface**: the base case
  (`|S|=1`) is not obviously *easier* than the general case. The very
  difficulty flagged for the inductive step — "companions `q` are unbounded
  in magnitude, no fixed ambient set" — is *already present at depth 1* (a
  singleton channel's companions are just as unbounded). The worked examples
  in this round's reports bear this out: `a_1=21528751`'s singleton channel
  `S=\{103\}` (depth 1) has *three* separate absorption events and a
  1090-element fan, strictly more complex than the same `a_1`'s depth-2
  channel `S=\{197,103\}` (two events). So `|S|` does not obviously track
  proof difficulty, which weakens (without refuting) the rationale for using
  it as the inductive measure. If the base case turns out to be exactly as
  hard as attacking `𝓥_S`-finiteness for an arbitrary proper core directly
  (which is exactly what the three sibling approaches already do), the
  "induction" buys nothing beyond re-labeling — worth having the builder
  confront this directly and report honestly if so, not build ornamental
  structure around it.
- **Instruction for the builder**: before elaborating Step 3's machinery,
  spend effort trying to construct — or definitively fail to construct — a
  concrete injective/count-preserving map from `a_1=21528751`'s `S=\{197,
  103\}` depth-2 absorption events (`\{2,103,197\}`, `\{3,103,197\}`) into
  some object derived from the *already known* singleton results for
  `S=\{197\}` or `S=\{103\}`. If no such map can be found even in this one
  concrete case, report this as evidence the induction schema itself is
  unsound (RETHINK-worthy for next round), rather than proceeding to write
  general machinery on an unconfirmed premise.
- Case coverage and multi-companion bundling (obstacle (b), `S=\{197\}`'s
  4-prime bundle) are correctly flagged as needing to be handled, not
  assumed away.
- This is a genuinely different top-level architecture from the three
  siblings (not a fragment of another approach's proof — it targets the full
  headline via the same imported chain, just via a distinct organizing
  principle), so it satisfies CLAUDE.md's "whole attempt" requirement.

### 3. imprint-automaton-periodicity (revise) — companion-event count 𝒜_S

**Verdict: CHANGES REQUESTED**, but flagged for **deferral this round** (see
§5 build-set rationale) due to mechanism overlap with
`persistent-backbone-monovariant`.

- Step 2's reformulation (`𝓥_S=𝒜_S∪(𝓥_S∩\{S\})`) is a clean, correct
  bookkeeping step.
- The outline explicitly tests and kills its own most tempting shortcut
  ("permanent survivors pairwise intersect via Lemma P′") as a dead end
  *before* the builder can waste time on it — good practice, exactly what
  round 5's memory rule about "sub-lemma covers only one branch" style traps
  warns against; here the outline pre-empts a genuinely vacuous argument
  (any two supersets of `S` trivially intersect in `S`) rather than letting
  a builder present it as progress.
- Step 3's genuinely open content — pigeonhole over primes below an
  `a_1`-dependent threshold, forced by Lemma 1's growth rate, combined with
  FOM's fan-size corollary — is, on inspection, **the same underlying
  bridge** `persistent-backbone-monovariant`'s Growth-Budget Lemma attempts
  (see §4). Both use identical certified ingredients (FOM's fan-size
  corollary + Lemma 1's linear bound) combined via a
  density/counting-versus-growth-rate collision. This is not a fatal flaw —
  nothing false is claimed — but it is weak diversity for this round's
  build-effort allocation.

### 4. forced-primes-well-ordering (revise) — Permanent-Freeze Dichotomy

**Verdict: CHANGES REQUESTED.** This is this round's most genuinely distinct
mechanism — an **extremal/permanent-blocking argument**, not a
counting/pigeonhole one — and its two elementary pieces check out:

- Permanent-Inadmissibility Lemma: trivial and correct (admissibility only
  ever adds constraints as `n` grows; a single disjoint-radical witness is a
  permanent obstruction). Independently re-verified in the `a_1=247` example
  (see §0): `T_{\{13\}}=2197` is blocked by `a_3=266`'s radical `\{2,7,19\}`
  from index 3 onward, and indeed `S=\{13\}` never grows past 3 elements.
- The Freeze Criterion itself (Step 2) is correctly left open, and — this is
  the strongest piece of process discipline in this round's whole field —
  the outline **mandates** the builder verify the criterion's hypothesis
  genuinely FAILS on the known non-freezing example (`a_1=2747`, `S=\{41\}`)
  before trusting it further. I ran that check myself and confirmed it: real
  collapse events occur at `n=11,12,13,162` for that channel, so the Freeze
  Criterion's hypothesis must (and does, per the outline's own honesty
  section) fail to apply there — the mechanism is correctly scoped as a
  partial dichotomy, not oversold as universal.
- The "Honesty warning" at the end (most hard channels absorb, not freeze;
  don't oversell coverage) is appropriate and matches what this round's
  fan-structural explorer actually found.
- Falls back, for non-freezing cores, to the same open absorption-count
  bound the other approaches attack — explicitly and correctly noted, not
  smuggled in as new progress.

### 5. Diversity assessment (dispatch item 4 — this matters more than usual,
round 3+ on the same gap family)

**Genuine diversity: 3 mechanisms, not 4.**
- `forced-primes-well-ordering`'s Permanent-Freeze Dichotomy is a real,
  independently-checkable extremal argument, distinct in kind from
  counting/induction.
- `core-depth-induction`'s strong induction on `|S|` is a real, distinct
  top-level architecture (structural reduction, not counting), though its
  central premise (a genuine depth-to-depth reduction) is unconfirmed and
  possibly infeasible (see §2).
- `persistent-backbone-monovariant`'s Growth-Budget Lemma and
  `imprint-automaton-periodicity`'s Companion-Count Bound are, on close
  reading, **the same attempted bridge** — both combine the *identical*
  certified tools (Lemma FOM's fan-size corollary + Lemma 1's linear growth
  bound) via a density/pigeonhole argument to try to convert a
  pointwise-in-`n` bound into a cumulative one. This is precisely the
  "pointwise ≠ cumulative" obstruction already flagged as insufficient in
  isolation across rounds 3–4 (the Markov/Cauchy-Schwarz finding). Running
  both this round risks spending two builder-slots discovering the identical
  wall in two notations.

**Explicit trigger for next round (per CLAUDE.md's single-gap-trap
guidance):** if the builder(s) working this bridge report the same stuck
pointwise-to-cumulative inequality again, do **not** spawn a third variant
of it (e.g. a "generation-count" or "event-density" relabeling) — that would
be the single-gap trap CLAUDE.md warns against. At that point, pivot fully
to `core-depth-induction`'s structural reduction (if its premise survives
the builder's early feasibility check above) or `forced-primes-well-
ordering`'s dichotomy generalized beyond the freeze case, or bring in a
genuinely orthogonal framing — this round's `math-explorer-analytic-tools`
report already confirms no ready-made analytic/probabilistic tool exists in
`knowledge_base.md` or the crux corpus, so "genuinely orthogonal" likely
means a new structural idea, not a new named theorem to import.

### 6. No resurrected dead ends

Checked against `current.md`'s full list and this round's two new
refutations (`a_1=105` kills "extra primes `<max(S)`", `a_1=2747` kills
"companions in increasing order") — none of the four outlines rely on either
mechanism (grepped, confirmed clean). No approach relies on the plain
cardinality monovariant on `|𝓜_n|`/`|𝓥_S|` (refuted, non-monotone), on
`H=rad(L_per)` (circular, refuted round 5), or on DM-multiset-order alone
(necessary-but-insufficient, correctly cited only as one ingredient among
several by `imprint-automaton-periodicity`).

### 7. Watch out for (builders, this round)

- **The antichain-vs-realized-radical distinction is an easy bug trap.**
  `𝓥_S` is the union of values ever *inclusion-minimal*, not the set of all
  realized radicals with imprint `S` — I made exactly this mistake in an
  early verification pass (got 1037 "elements" for `a_1=247`'s `S=\{13\}`
  before realizing I was counting all-ever-realized instead of
  all-ever-minimal). Any builder computation must track domination/removal
  correctly, not just insertion.
- `core-depth-induction`'s builder should report early and honestly if the
  depth-reduction premise cannot even be sketched on the one concrete
  example available (`a_1=21528751`, `S=\{197,103\}`) — do not spend the
  full round building Step 2/3 scaffolding around an unconfirmed premise.
- `imprint-automaton-periodicity` is deferred this round (see build set
  below), not cut — its already-certified Theorem V-MRS/Theorem CD/Lemma TC
  remain fully valid and importable by every sibling; only its new Step 3
  attempt is paused pending evidence the shared bridge with
  `persistent-backbone-monovariant` is actually different in substance.

### Ranking

Registered `core-depth-induction` (new this round, cold-start 1500).
Ran `update_ranking` anchoring the new/revised cohort against the established
field: `intersecting-family-covering-construction` (unchanged, top,
complete-conditional-proof) beats both `forced-primes-well-ordering` and
`persistent-backbone-monovariant`; `forced-primes-well-ordering` (freshest
genuinely distinct mechanism this round, verified) edges out
`persistent-backbone-monovariant` (owns FOM's certification but shares the
weaker bridge with `imprint-automaton-periodicity`); both beat
`imprint-automaton-periodicity` and `core-depth-induction`;
`core-depth-induction` drew with `imprint-automaton-periodicity` (both
genuinely open, roughly comparable risk) and beat the long-parked
`explicit-window-backbone-construction`. Resulting Elo (post-update):
`intersecting-family-covering-construction` 1688.4 (top),
`forced-primes-well-ordering` 1611.7, `persistent-backbone-monovariant`
1573.9, `explicit-window-backbone-construction` 1487.4 (parked),
`core-depth-induction` 1487.5 (new), `imprint-automaton-periodicity` 1445.9,
`backbone-existence-crt` 1411.5 (parked), `bounded-gap-density-covering`
1322.0 (parked, dead-end).

### Build-set rationale

Four outlines were revised/opened this round; none is fatally flawed
(no RETHINK). Per CLAUDE.md's "few strongest (normally 1–3)" guidance and
the diversity finding in §5, I am trimming to **3** rather than building all
four: `persistent-backbone-monovariant` (must be built regardless — it is
the designated, now-verified-sound home for certifying the foundational
Lemma FOM that three of the four approaches depend on), `core-depth-
induction` (genuinely new architecture, worth testing this round with the
explicit early-feasibility instruction above), and `forced-primes-well-
ordering` (this round's most independently-distinct mechanism, with its own
mandatory self-check already passing). `imprint-automaton-periodicity` is
deferred, not cut — its Companion-Count Bound attempt substantially
duplicates `persistent-backbone-monovariant`'s Growth-Budget Lemma with the
same two certified ingredients; once FOM is certified this round, it is
cheap to revisit `imprint-automaton-periodicity` next round if the other
three approaches all stall, ideally with a mechanism that does not just
re-run the same pointwise-to-cumulative pigeonhole in different notation.

build set: persistent-backbone-monovariant, core-depth-induction, forced-primes-well-ordering
