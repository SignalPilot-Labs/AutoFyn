## imo-2026-06 — thread-unification lens (bundle-count (a) vs escape-depth (b))

**Bottom line (verified by fresh computation, not just re-reading): (b) is a
cheap, provable ONE-DIRECTIONAL consequence of the workspace's already-certified
master reduction ("𝓥 finite ⟺ (MRS)", Theorem V, `lemmas/theorem-V-veto-
finite-iff-MRS.md`, round 5) applied core-by-core, NOT an independent
sub-problem, and NOT (as the round-7 builder guessed) something that "(b)
reduces to (a)" in the literal sense of `persistent-backbone-monovariant`'s
chosen target. More precisely: (b) [bounded escape depth] follows from
**full `𝓥_S`-finiteness / (MRS_S)** — the pre-existing master gap — via a
short new lemma (not yet written down anywhere: "antichain-freeze ⟹
bounded depth"). But (a) as `persistent-backbone-monovariant` has literally
scoped it (bounding the COUNT of *permanent* `D_S`-disjoint bundles only) is
a strictly weaker, proper SUBSET of what `𝓥_S`-finiteness requires — it
ignores *transient* (eventually-dominated) antichain members, whose count is
a separate, still-wide-open piece (the round-6 "Growth-Budget"/chain-count
question). So solving (a) exactly as scoped would NOT by itself close (b) or
`𝓥_S`-finiteness either. Both threads should be re-targeted at the single
object `𝓥_S` (permanent + transient), not kept as two parallel programs.**

### The concrete check requested (both known depth-3 instances, regenerated from scratch)

Built an independent greedy-sequence generator (fresh Python, minimal-radical-
antichain admissibility, no code reused from any prior round) and cross-
checked it against 7 known hand-verified values of `a_1=247` (exact match,
`n=1..10`) before trusting it on the two target cases. Generated `a_1=2747`
to `n=19620` (values to `~1.15M`) and `a_1=21528751` to `n=30100` (values to
`~26M`); all cited factorizations in `current.md`/the two approach files
reproduced **exactly**: `a_2=21528854=2·41·103·2549`, `a_3=21528948=2·3·7·
197·1301`, `a_1291=21710976=2·3·7·41·197`, `a_5844=22356348=2·3·7·193·197`,
`a_7831=22637664=2·3·7·19·197`, `a_19617=1100274=2·3·7·17·23·67`,
`a_30017=25781784=2·3·7·19·41·197`. Then, for both flagged depth-3 instances,
directly searched the generated sequence for the first exact occurrence of
the *relevant permanent bundle's* bare value:

- `a_1=2747, S={67}`, bucket `{17,23,67}` (depth 3, occupant `a_19617`).
  `{2,3,7,67}` (the already-certified Permanent Pair Lemma bundle for this
  exact `S`, `lemmas/lemma-permanent-bundle.md`) is realized **at index 3**
  — essentially at the start. `a_19617`'s radical `{2,3,7,17,23,67}` is a
  **proper superset** of `{2,3,7,67}`, so it is dominated **the instant it
  appears** — it never becomes a minimal/antichain element even transiently.
  Same story for the two depth-2 buckets of this core: `{3,17,67}` (occupant
  `a_807={2,3,7,17,67}`) and `{2,23,67}` (occupant `a_1110={2,3,7,23,67}`)
  are *also* immediate supersets of `{2,3,7,67}` (realized at `n=3`), hence
  also immediately dominated on arrival. **All three "escape" events for
  this core (depth 1, 2, and the corrected depth 3) are the *same* single
  already-established permanent bundle reappearing in dominated form — zero
  new bundles.**
- `a_1=21528751, S={197}`, bucket `{19,41,197}` (depth 3, occupant
  `a_30017`). The relevant bundle here is `{2,3,7,197}` (`Q={2,3,7}` for
  singleton `S={197}` — *not* the `D_S={2,3,7}` cited elsewhere for the
  different, non-singleton core `S={103,197}`; computed `D_S` for the
  singleton `{197}` directly from the generated data and it is **empty**
  within the tested range, confirming `Q_S⊆D_S=∅` is consistent with this
  bundle being a genuine *multi*-companion bundle, not a sole-companion
  case). `{2,3,7,197}` is first realized exactly at **`a_2575`** — this
  matches the text's own "collapse at `n≈2575`" note exactly. `a_30017`'s
  radical `{2,3,7,19,41,197}` is a proper superset of `{2,3,7,197}` and
  `2575<30017`, so again **immediately dominated on arrival, contributing
  nothing new**. The two depth-2 occupants `a_5844` and `a_7831` are
  likewise proper supersets of `{2,3,7,197}` realized *after* `n=2575`, so
  they too are immediately-dominated, zero-new-content escapes. Only
  `a_1291` (depth-2 bucket `{3,41,197}`, occupant `{2,3,7,41,197}`) is
  realized **before** `n=2575`, so it *was* a genuine (if transient)
  antichain member from `n=1291` to `n=2575`, at which point it got
  dominated and removed once `{2,3,7,197}` appeared.

**Conclusion of the check.** No instance of "depth increment ⟹ new
`D_S`-disjoint permanent bundle" was found; the opposite holds in every
single one of the 6 escape events checked across both cores: depth is
explained either by (i) reuse, at a much later and immediately-dominated
index, of an *already permanent* bundle established earlier for the *same*
core (`a_19617`, `a_30017`, `a_5844`, `a_7831`, `a_807`, `a_1110`), or (ii) a
genuinely transient (not permanent) antichain member that later gets
dominated by that same eventual permanent bundle (`a_1291`). **No map
"escape-depth increment ↦ new permanent bundle" exists on this data — in
fact the map runs backwards: every deep escape is downstream of an already-
settled bundle, not a source of a new one.**

### Why (b) still reduces to the master gap, cleanly, in one direction

Short structural fact (not previously stated anywhere in the workspace,
should be cheap to certify): **if the class-`S` antichain `𝓜_n^S` freezes at
some finite index `n^*` (i.e. `(MRS_S)` holds), then every index `i>n^*` in
`I_S` has `rad(a_i)` a superset of some fixed element of the frozen
antichain `𝓜_{n^*}^S`.** Proof sketch: in the poset of realized class-`S`
radicals ordered by `⊆`, maintaining minimal elements as more sets are
added, a newly added set either (i) is a new minimal element (joins the
antichain), (ii) is a strict subset of an existing minimal element (removes
that element, an antichain change), or (iii) is a proper superset of some
existing minimal element (no antichain change). If the antichain has
genuinely stopped changing forever past `n^*`, only (iii) can occur for
`i>n^*`. This immediately bounds `d(C)` (the escape-depth function forced-
primes-well-ordering defines) by `max_{C'∈𝓜_{n^*}^S}|C'\setminus S|` for any
bucket escaped after `n^*`, plus a trivial finite max over the (finitely
many, since `n^*` is finite) pre-freeze escapes. **So `(MRS_S)` ⟹ uniform
depth bound**, cheaply. This is consistent with, and explains, both round-7
files' empirical finding that depth stayed small everywhere tested — it is
small *because* the antichain has (empirically) already frozen very early in
every tested instance (matches `persistent-backbone-monovariant`'s own §5
antichain-freeze findings on the identical five cases), not because of any
depth-specific mechanism.

### Why (a) as currently scoped is NOT the same as, or sufficient for, this

`persistent-backbone-monovariant`'s Permanent Pair/Bundle Lemma only ever
proves a bundle `Q` is **never dominated once realized** — i.e. it is about
elements that, once minimal, stay minimal forever. It says nothing about
**how many bundles are ever transiently minimal and later dominated** (like
`a_1291`'s `{2,3,7,41,197}` above) before the antichain settles. `𝓥_S`
(already-certified object, Theorem V) is the union of *all* ever-minimal
values, permanent and transient; `(MRS_S)`⟺`𝓥_S` finite (Theorem V, exact
equivalence, not just sufficiency). Bounding only the permanent subset
(`persistent-backbone-monovariant`'s literal target) leaves the transient
subset's count completely open — and it is exactly the transient subset's
potential unboundedness that was flagged, unresolved, as the round-6
"Growth-Budget Lemma"/"Generation-Chain count" gap
(`forced-primes-well-ordering`'s own Round 6 Outline §Step 4, and
`persistent-backbone-monovariant`'s Round 6 build item 2(d), Multi-Companion
Reduction Proposition) — i.e. this transient-count question is *already on
record in this workspace as unsolved*, just not previously connected
explicitly to the depth-bound target. So: **(a) as scoped ⊊ `𝓥_S`-finiteness
⟹ (b)**; solving (a) alone does not give (b), and (b) does not give (a)
either (a uniform depth bound says nothing about how many *distinct* buckets
or permanent bundles exist — it is entirely about reachability/timing, not
count).

### Recommendation for the outliner

1. **Do not keep (a) [permanent bundle count] and (b) [escape depth] as two
   separate rival top-level targets.** They are not independent sub-problems
   requiring separate arguments in the sense the round-7 builder wondered;
   (b) is logically downstream of the pre-existing master gap `𝓥_S`-finiteness/
   `(MRS_S)`, already certified equivalent (Theorem V) — and the
   Freeze-Confinement Corollary above is a genuine, cheap (probably ~15-line),
   certifiable new lemma unifying them, worth having a builder write up this
   round (it costs little and closes the "are these the same gap" open
   question cleanly, with a real proof, not just intuition).
2. **The actually-missing piece, precisely located by this check, is bounding
   the *transient* member count of `𝓥_S`** (not the permanent-bundle count
   `persistent-backbone-monovariant` has been attacking) — this is the
   already-on-record but not-recently-directly-attacked Growth-Budget/
   Generation-Chain-count gap. A round-8 approach should retarget explicitly
   at "bound the total number of distinct radical values *ever* minimal for
   class `S`, not just the ones that survive forever" — this is a strictly
   harder, more complete target than either thread currently pursues, but it
   is the one that actually closes the gap if solved.
3. **`forced-primes-well-ordering`'s round-8 dispatch should stop searching
   for a self-contained depth-bound mechanism independent of `(MRS_S)`**
   (§G Step 4 of that file already found, independently, that the "naive
   branching escape tree" does not visibly terminate — this check now
   explains *why* rigorously: the true small depths observed are not
   produced by any internal well-foundedness of the escape recursion, they
   are a byproduct of the (already-mysterious) early antichain freeze). Do
   not resurrect the Recruiter-Alignment/`W(a_1)` pattern (already
   independently refuted for nested cores, `current.md` round 7) as a
   depth-bound mechanism — it would be redundant with the Freeze-Confinement
   Corollary above even if resuscitated, since it presupposes exactly the
   freeze fact the corollary already extracts what's needed from.
4. **Cheap correctness note for the builder writing up the Freeze-
   Confinement Corollary**: it needs the antichain-freeze fact for `n^*`
   *finite but arbitrary* (does not need an explicit bound on `n^*` itself,
   consistent with `(MRS_S)`'s existential phrasing) — do not conflate
   "uniform in `a_1`" with "uniform in `n`"; the depth bound produced is
   uniform **for a fixed core `S`** (a fixed, finite `max_{C'∈𝓜_{n^*}^S}
   |C'\setminus S|`), not a bound valid across all `a_1,S` simultaneously —
   that stronger claim would need `(MRS_S)` itself to be uniformly
   effective, which is not established and not needed for what
   `forced-primes-well-ordering`'s own target actually asks.

### Distinct openings (for the outliner to weigh, beyond the unification finding itself)

- **Opening 1 (primary, per above): retarget both threads at bounding the
  transient member count of `𝓥_S`** — i.e. attempt the round-6 Growth-Budget
  Lemma / Generation-Chain-count question directly, now correctly identified
  as the one piece neither thread has actually closed, using the
  newly-clarified fact that "permanent bundle count finite" + "transient
  member count finite" together are exactly `𝓥_S` finite (Theorem V).
- **Opening 2: certify the Freeze-Confinement Corollary** as cheap, real,
  reusable content this round regardless of whether Opening 1 succeeds — it
  formally resolves this round's assigned "are (a) and (b) the same
  problem" question with a real proof, which is valuable population content
  even standing alone (it is the kind of small, clean, certifiable lemma
  this workspace has consistently rewarded).
- **Opening 3 (not attempted here, flagged for a future round): the
  transient-count question might be more tractable focusing specifically on
  bundles realized *before* the earliest-known permanent bundle for a core**
  (as `a_1291` was before `a_2575`) — i.e. is there a clean argument bounding
  "how many candidates can be minimal before the first sole/dual permanent
  absorber appears," tying back to Lemma FOM's `T_C` machinery (already
  certified) rather than a fresh mechanism. Not developed further here (out
  of this lens's scope, per dispatch instructions), but flagged as the
  natural next concrete sub-target if Opening 1 is picked up.

### Candidate technique(s)

Elementary poset/antichain-maintenance argument (freeze ⟹ every later
element comparable to a frozen minimal element) — no new named external tool
needed; this is a direct generalization-in-spirit of the already-certified
No-Resurrection Lemma / Interval Lemma (`persistent-backbone-monovariant`,
round 5) applied per-core rather than globally. For the *actual* remaining
open content (transient-member-count bound), the workspace's own round-6
Growth-Budget attempt (Lemma FOM + Fan-Size Corollary + Lemma P′ +
Generalized Lemma C) remains the most on-point starting machinery, already
certified and reusable — no crux-corpus or knowledge-base tool beyond what
is already in play was found relevant to this specific structural question.

### Cheap-kill candidates

None new beyond what's already certified — this was a structural/logical
question, not a search for a pruning shortcut. (The computation above *is*
itself a cheap kill: it rules out, by direct counterexample from real data,
the "depth increment ⟹ new bundle" map that would have been the natural
first guess for unifying the two threads.)

### Knowledge-base entries to use

None beyond what the two approach files already cite (Theorem V / Lemma
MS-family equivalences are internal, not KB-sourced). This is a workspace-
internal structural-relationship question; no external KB technique applies
directly to it.

### Analogous past problems (cruxes)

Not applicable to this specific lens — the assigned task was a structural
comparison of two internal sub-targets, not a fresh attack needing external
crux-corpus retrieval. (Prior rounds' explorers already searched the corpus
broadly for this problem's core FCBC/`(MRS)` gap and found nothing
genuinely analogous; no reason to expect a match for this narrower
structural sub-question either.)

### Prior progress

Both approaches' round-7 certified content stands: Escape-Confinement Lemma
(`lemmas/lemma-escape-confinement.md`) and Permanent Pair/Bundle Lemma
(`lemmas/lemma-permanent-bundle.md`) are both correct and reusable as-is —
nothing in this check contradicts either certified lemma. What this check
adds is the missing *relationship* between the two files' chosen top-level
targets, previously only guessed at ("might be an artifact"), now settled
with an explicit one-directional implication and a concrete counterexample
to the naive two-directional/equivalence guess.

### Dead ends (do not retry)

- **Do not pursue "escape-depth bound as a self-contained target independent
  of `(MRS_S)`"** — confirmed here, on top of `forced-primes-well-ordering`'s
  own §G Step 4 finding, that the natural mechanisms (naive branching
  recursion; Recruiter-Alignment/`W(a_1)` pattern) do not work and that the
  observed shallow depths are fully explained as byproducts of already-
  established permanent bundles, not an independent phenomenon with its own
  well-founded structure to exploit.
- **Do not treat "bound permanent bundle count" (persistent-backbone-
  monovariant's literal Round 7 target) as sufficient for `𝓥_S`-finiteness**
  — confirmed here to be a proper subset of the requirement; solving it
  alone leaves the transient-member-count question, already flagged as open
  since round 6, completely untouched.

### Small-case / intuition notes (conjecture, from this round's data only)

Both fully-traced hardest instances show the *same* qualitative shape: one
"cheap" permanent bundle (companion set size 2–3, drawn from small primes
like `{2,3,7}`) gets established very early (index 3, or index 2575 out of
tens of thousands) relative to the instance's full simulated range, and
essentially everything realized afterward in that class is either dominated
immediately or (rarely, only before the early absorber appears) a short-
lived transient member. This is *consistent with* (but does not prove) the
already-standing conjecture that `𝓥_S` is finite in general — the mechanism
suggested by this data is "one small absorbing bundle per core, found early,
swallows essentially everything after it," which if provable in general
would resolve both threads and, likely, the whole problem — but no general
proof of *why* such an early absorber must exist (as opposed to a core
where absorption never happens or happens arbitrarily late/never) was found
or attempted here; this remains exactly the round 5–7 "same essential
difficulty as global FCBC" residual, now viewed through one more lens.
