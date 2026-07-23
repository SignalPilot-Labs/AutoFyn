## Status
partial

## Round 15 Outline (proof-outliner directive — advance, diversity
slot; no new explorer finding targets this approach's gap directly
this round)

**Target (unchanged): the whole problem** — via the already-certified
Theorem 5.1/Theorem SW/Theorem PD-Conditional chain; this approach's
own remaining open content is `(PD_{S,S'})`/`BRL(S')`/`G`-eventual-
periodicity, unchanged from round 14 (Theorem MO/Prop MO-2 retire two
extreme minimality-selection mechanisms, narrower than a full
impossibility proof).

**Technique**: unchanged — density/minimality argument on the coarse
core sequence `G`, structurally independent of the witness-chaining
mechanism the other approaches (and the new crux-adaptation attempt)
use; kept live specifically because CLAUDE.md requires the population
not collapse onto one mechanism even while the crux-adaptation route is
prioritized this round.

**Skeleton**: unchanged from round 14's file (Lemma WO++/Theorem MO/
Proposition MO-2 already certified) — this round's directive is:
formalize the "intermediate pigeonhole/density mechanism" gap Theorem
MO's own scope correction left open (some, not every, type-`S'`
candidate in each window is admissible against the accumulated
history) — this is a genuinely different, not-yet-attempted mechanism
shape from the two already-ruled-out extremes, per round 14's own
Recommendation (iii).

**Key lemmas**: none new proposed this round beyond what round 14
already flagged as the next concrete step (the intermediate mechanism
gap) — builder should attempt to close it or prove a third
impossibility case, extending Theorem MO's scope.

**Open gaps**: `(PD_{S,S'})`/`BRL(S')`/`G`-periodicity itself; whether
the intermediate pigeonhole mechanism (round 14's open Recommendation
(iii)) can be ruled out or made to work.

**Cases to cover**: none beyond the existing Theorem MO case split.

**Watch out for**: do not let this approach's slower cadence (no
explorer lens targeted it directly this round) cause it to be silently
dropped — it remains the only structurally-independent live mechanism
besides the new crux-adaptation attempt, and per CLAUDE.md diversity is
required even while other approaches advance faster.

## Round 15 update (headline — read this first)

**Executed this round's mandate in full: attempted the intermediate
pigeonhole/density mechanism Theorem MO/Proposition MO-2 (round 14) left
formally open, and closed it with a genuine, rigorous impossibility proof
(Theorem EI, Existence-Insufficiency) — not a further unsuccessful search,
and not a repeat of the two already-ruled-out extremes. New content in
Part 14 below.**

**What Theorem EI shows.** Any mechanism built from a bounded finite
companion set `W_0` and CRT/pigeonhole counting (single-witness, as in
Theorem MO, or window-aggregate, as in Lemma WO++, or any mixture) that
only ever certifies *existence* of an admissible type-`S'` candidate
against the accumulated history (the "intermediate" shape the reviewer's
scope note flagged as untested — strictly weaker than Proposition MO-2's
"every candidate, every witness" hypothesis) is provably insufficient to
establish `\mathrm{BRL}(S')`/`G`-periodicity. The mechanism is proved
powerless for a structural reason, not a failure to find the right
argument: by **Lemma TS (Type-Symmetry)**, the exact same CRT/pigeonhole
reasoning, applied verbatim with any other core type `T` disjoint from
`S` in place of `S'`, certifies the identical existence conclusion for
`T` — so the mechanism cannot single out `S'` among its competitors; and
by **Lemma AA (Automatic Admissibility)**, type-`S` candidates in
particular face an even *stronger* (unconditional, density-1) admissibility
guarantee against `I_S`'s own history than any CRT-fractional guarantee
the mechanism could produce for `S'`. Since (**Lemma GM**) the actual next
term's core is determined by a **global minimum over every core type**,
not a type-restricted one, existence certificates that are symmetric
across all competing types (Lemma TS) and dominated by at least one
competitor (Lemma AA) carry zero information about which type wins the
race — hence cannot bound run length. This completes the round-14
reviewer's flagged trichotomy into a closed case analysis with **no gap
remaining** among bounded-modulus/CRT mechanisms: single-witness (Theorem
MO, blind), intermediate existence-only (Theorem EI, this round,
insufficient by Type-Symmetry), full mutual coverage (Proposition MO-2,
collapses into the Stabilization Conjecture itself — a different,
non-density mechanism).

**Independent cross-check strengthening the honesty of this result
(Part 14.6).** The sibling `sunflower-bundle-closure` approach's
already-certified Lemma FT proves, *unconditionally* (an exact
combinatorial packing argument, not a density estimate — strictly
stronger than anything the intermediate mechanism could produce), that a
finite prime set secures existence of admissible candidates against an
entire infinite class's history. Its own certification record confirms
this still does not resolve the (different, but structurally analogous)
selection question that approach faces (Conjecture (JW), the cross-pair
matching gap) — independent confirmation, from a different approach's
already-certified content, that "existence of admissible material" is
categorically the wrong kind of fact to try to leverage for a selection
or matching conclusion, reinforcing Theorem EI's diagnosis rather than
merely asserting it.

**Honest bottom line.** `\mathrm{BRL}(S')`/`G`-eventual-periodicity itself
remains open — Theorem EI is a negative result about a technique family,
not a refutation of the target. Status stays `partial`. Per this round's
and round 14's combined finding, any future proof of the target must
engage with **minimality of the greedy's selection**, using realized-member
reasoning (Lemma WF's style) or a genuinely different mechanism — no
variant of bounded-modulus/CRT existence-only reasoning can close it,
now proved exhaustively rather than checked at two extremes. Two new
lemmas proposed for certification this round: Lemma TS and Lemma AA
(Lemma GM is a trivial restatement of the problem's own definition,
included for explicitness rather than as a promotion candidate).

## Approaches tried (round 15, this round)

- Attempted the intermediate pigeonhole/density mechanism the round-14
  outline-reviewer's certification scope note flagged as untested (a
  fixed finite `W_0` combined with a pigeonhole/density argument for
  *some*, not *every*, type-`S'` candidate per window). **Outcome:
  refuted with a full proof (Theorem EI), not abandoned as unattempted.**
  See Part 14 for the complete argument (Lemma TS, Lemma AA, Lemma GM,
  Theorem EI) and Part 14.6 for an independent cross-check via the
  sibling `sunflower-bundle-closure` approach's already-certified Lemma
  FT. This completes the round-14 reviewer's flagged trichotomy with no
  remaining untested case in the bounded-modulus/CRT technique family.
  `\mathrm{BRL}(S')`/`G`-eventual-periodicity itself remains open — this
  is a negative result about the technique family, not about the target.

## Round 14 update (headline — read this first)

**Dispatch this round.** Per Proposition BI's own positive redirection
(round 13: any closing mechanism for `\mathrm{BRL}(S')`/`G`-periodicity must
reason about **minimality** — which admissible candidate is numerically
*smallest* — not mere feasibility/existence), this round's mandate was to
develop or identify a tool that reasons about minimality of admissible
candidates in a residue class/CRT setting, and to report honestly if no
such tool applies. **Outcome: a genuine, rigorous, new NO-GO theorem
(Theorem MO, Minimality Obstruction) was proved this round** — not "no
tool was found," but a proof that no tool of the specific shape asked for
(a bounded-modulus/CRT mechanism restricted to, or built from, the fixed
`P_1`-alphabet) *can* exist, together with a precise account of what
happens once the modulus is enriched with companion primes: it either
stays provably blind (P_1-only) or collapses into being **literally
equivalent to** already-certified witness-chaining content (Lemma WF,
certified round 13 by the sibling `forced-primes-well-ordering`/
`witness-chaining-universal-existence` approaches), so it supplies no
independent leverage as a *distinct* technique. This is the "confirmed,
not just unfound" negative result the dispatch asked for, in the spirit of
round 6/9's decisive refutations, plus one new promotable lemma (Lemma
WO++, a genuine CRT extension of the already-certified Lemma WO).

**Search of `knowledge_base.md` and the crux corpus (per CLAUDE.md's
mandate to consult both), done first, before any new construction.**
`knowledge_base.md`'s Number Theory section (CRT, Dirichlet, three-gap
theorem, orders/Euler) contains no entry addressing minimality of a
*selection process* (which of several admissible residues is *smallest*)
— its CRT entry is purely a counting/solving tool, exactly what Lemma WO
already used; nothing there addresses selection among admissible
candidates. Queried the crux corpus (`past_crux_moves_database.json`)
for `domain=number_theory`/`combinatorics`, `subtopic∈{modular-
arithmetic-and-CRT, processes-and-algorithms}`, and free-text `greedy`+
`smallest`/`minimal`/`CRT`/`residue`: 48 `processes-and-algorithms` cruxes
and several greedy+minimal cruxes were retrieved (`aimo-0558`, `aimo-0620`,
`aimo-0626`, `aimo-0718`, `aimo-0585`, …) — none address a greedy process
selecting the least element of an infinite set subject to *unboundedly
many, history-dependent* admissibility constraints reducible only in part
to a fixed finite alphabet; they are all either bounded-resource
scheduling processes or finite-set greedy arguments, structurally unlike
this problem's setting. **No existing KB entry or crux move transfers
directly** — confirming the dispatch's own framing that this is genuinely
unattempted territory, not a retrieval failure on this round's part.

## Round 13 Outline (proof-outliner directive — ADVANCE unchanged
skeleton; note a scale finding on the periodicity hypothesis and a
possible future shortcut, no retarget)

**Target and skeleton unchanged from Round 12 (Theorem PD-Conditional,
already certified — see below); no new retarget this round.** Round 13's
gn-periodicity explorer (`/tmp/round-13/math-explorer-gn-periodicity.md`)
pushed direct KMP period-search on `G_n` for the hardest instance
(`a_1=21528751`) to `N=25{,}000{,}000` and found **no** internal repetition
at all in that range — but this is explained, not alarming: the same
explorer's antichain-freeze tracking shows the implied true period `T`
would need to be roughly `4\times10^{10}`–`2\times10^{11}` (extrapolating
the `T/L` ratio from the 4 tractable solved cases), 3+ orders of magnitude
beyond any feasible direct search. **Concrete instruction for this round's
builder: do not attempt to further verify `G_n`-periodicity numerically on
`a_1=21528751` — it is provably outside direct-search range; instead
either (a) continue toward a structural proof of eventual periodicity of
`G` (the genuinely open content, unchanged target), or (b) note explicitly
in the file that IF the new `core-antichain-content-freeze` approach this
round succeeds in proving global `\mathcal V`-finiteness (equivalently
(MRS)), that would independently supply EXACT periodicity from `n=1` via
the already-certified Theorem 5.1 directly — making this approach's own
periodicity-of-`G` hypothesis unnecessary for the whole problem (though
still worth finishing as an independent, self-contained route, and
`Theorem PD-Conditional` remains correct and reusable regardless).** This
is noted for awareness only — do not treat the new approach's success as
assumed; it is unverified and flagged for outline-reviewer confirmation
(see `core-antichain-content-freeze.md`).

## Round 13 update (headline — read this first)

**Housekeeping note first.** `core-antichain-content-freeze` (option (b) of
the Round 13 Outline above) was given **RETHINK** by this round's
outline-reviewer, before any build: the Multi-Companion Reduction
Proposition (round 6, certified) already shows global `\mathcal V`-finiteness
is equi-hard to FCBC itself for any core with a realized multi-companion
bundle — a concrete such core is already known (`S=\{103,197\}`,
`a_1=21528751`, bundle `\{11,97\}`). So option (b) does **not** apply this
round; the sole live route to `(PD_{S,S'})` in this file remains option (a):
a structural, unconditional proof of `G`'s eventual periodicity (or of the
strictly weaker Bounded-Run-Length property, `\mathrm{BRL}(S')`, which by the
already-certified Lemma PD-from-BRL suffices on its own, with no need for
full periodicity).

**This round's mandate.** Attempt a genuinely different technique for
`G`-periodicity/`\mathrm{BRL}` — explicitly **not** Lemma W3's
minimal-radical-antichain compression (round 12, already shown dead:
`|M_n|` is provably unbounded, not usable as a finite-state witness) and
**not** the rejected global-antichain shortcut (`core-antichain-content-
freeze`, RETHINK above).

**What this round did.** Attacked `\mathrm{BRL}(S')` **directly**, bypassing
periodicity of `G` altogether — a genuinely different route from round 12's
"periodicity `\Rightarrow` `\mathrm{BRL}`" (Lemma BRL-from-Periodicity),
using a fresh CRT/admissibility argument specific to the fixed, bounded
`P_1`-alphabet, distinct from every previously-tried mechanism in this file.
Two new, fully proved, unconditional pieces of content resulted (Part 12
below):

- **Lemma WO (Window Occupancy)** — a clean, elementary, unconditional CRT
  counting fact: every window of `L_0:=\mathrm{rad}(a_1)` consecutive
  integers contains *exactly* `c_{S'}:=\prod_{p\in P_1\setminus S'}(p-1)\ge1`
  integers whose `P_1`-divisibility pattern equals `S'` exactly — so
  candidates of the "right type" to witness `\mathrm{BRL}(S')` are always
  present nearby, unconditionally, with no gap. Independently numerically
  spot-checked (`a_1=247`, `S'=\{19\}`: predicted `12`, confirmed `12` at
  four different window offsets including `m=100000`).
- **Proposition BI (Backbone Permanence Does Not Force Class Revisitation)**
  — a short, rigorous, but structurally important **negative** finding:
  IF the sibling `sunflower-inadmissibility-toolkit`'s Backbone Permanence /
  EBS hypothesis holds for class `I_{S'}` (a companion prime `q\notin P_1`
  eventually divides *every* `I_{S'}` term), THEN the entire infinite family
  of admissibility constraints contributed by `I_{S'}` can be discharged
  *uniformly*, for all time, by any multiple of `q` — **without that
  candidate ever needing to belong to `I_{S'}` itself**. Consequently,
  Backbone Permanence for `S'` — even if fully established by the sibling
  approach this round — supplies **no logical mechanism** that could force
  `\mathrm{BRL}(S')`: it is a genuinely separate, non-implied open question,
  and Lemma WO's "candidates exist nearby" fact does not close the gap
  either, since existence of a candidate says nothing about whether the
  greedy rule's *admissibility test* (let alone its *minimality* tie-break)
  ever actually selects one. This gives a precise, mechanistic explanation
  — sharper than round 11's Part 10.3 circularity diagnosis, not a mere
  restatement of it — for *why* every pigeonhole/existence-style tool in
  this workspace's toolkit (Domination Lemma, Lemma RD, Companion-
  Disjointness Coarsening, EBS/Backbone Permanence) cannot by itself close
  `\mathrm{BRL}`/`G`-periodicity: none of them touch *minimality* (which of
  several simultaneously-admissible candidates the greedy actually picks),
  only *feasibility* (that some admissible candidate of a given type exists
  or that admissibility can be satisfied at all) — and Proposition BI proves
  feasibility is exactly the wrong thing to try to obstruct, because
  feasibility never forces a return to `S'` even under the strongest
  currently-attackable backbone hypothesis.
- Independently re-confirmed by fresh computation (own generator, `a_1=2747`,
  the sibling's own mandatory Case A instance): companion backbone
  `\{2,3,7\}` is essentially **universal** across the whole sequence, not
  specific to either class — `99.4\%` (`39{,}767/40{,}000`) of *all*
  `40{,}000` tested terms (regardless of core) are divisible by `2`, `3`,
  or `7`, and *both* `I_{41}` (`38{,}408` tested members) and `I_{67}`
  (`777` tested members) are `100\%` divisible by `\{2,3,7\}`. This is a
  concrete illustration, not a proof, of Proposition BI's point: the
  backbone carries essentially
  no information distinguishing the two classes, so it cannot be *why*
  `I_{67}` keeps recurring (empirically, with a strikingly regular gap
  `\approx50`, stable from `N=6000` to `N=40{,}000` with no further growth —
  itself consistent with, but not proof of, `\mathrm{BRL}(\{67\})`).

**Honest conclusion.** `\mathrm{BRL}(S')`/`G`-eventual-periodicity remains
**open**. This round's genuine, new contribution is (i) one clean,
unconditional, promotable CRT lemma (Lemma WO), and (ii) a precise negative
result (Proposition BI) ruling out — with an actual proof, not a suspicion —
the one concrete mechanism (companion-backbone permanence) that a sibling
approach is attacking in parallel this very round, together with a concrete
positive redirection: any future proof of `\mathrm{BRL}`/`G`-periodicity
must engage with **minimality** (which admissible candidate is numerically
*smallest* at each step), not merely feasibility/existence — no tool in
this workspace's current toolkit does that yet. Status stays `partial`;
Theorem PD-Conditional (round 12, unchanged, still fully certified) remains
the strongest unconditional bridge available.

## Round 12 Outline (proof-outliner directive — retarget Step 2 to a
bounded-run-length/pigeonhole argument on the coarse, FIXED-alphabet
`P_1`-projection `G_n`, replacing the retired dyadic-fraction hint)

**Target (unchanged): the whole problem**, via Theorem SW → Proposition
9.4 → Theorem 5.1 (all already certified/conditional, do not re-derive).
**Retire Step 2's "dyadic near-fraction" hint** (`a_1=4087`'s
`33/64`,`15/32` densities) as a general mechanism — this round's
pd-density explorer (`/tmp/round-12/math-explorer-pd-density.md`)
rigorously resolved it: it is fully explained by `4087`'s unusually SMALL
exact period (`64`, itself explained by having only 2 primes), not
evidence of a universal 2-adic mechanism (the other 3 tractable periods —
`1806`, `2062`, `105250` — have no such clean structure). Do not use the
dyadic hint as a proof strategy going forward.

**New, much stronger finding to retarget Step 2 around.** `G_n` (the
coarse `P_1`-core-membership sequence, i.e. `\mathrm{rad}(a_n)\cap P_1` —
exactly what a core class `I_S` tracks) is **EXACTLY periodic from
`n=1`** in every tractable tested instance — rigorously verified this
round via a proper KMP/Border-Lemma exact-period finder (not density
estimation), stable over `1600+` repeated periods in the best case
(`247`), reproducing and sharpening round 4's own dormant `G_n` finding
(untouched since round 5, and proven this round to be logically
independent of both dead mechanisms — `(UB_S)`/Landau-Turán tracks
companion-prime SIZE, an unbounded quantity per the Case-II refutation;
`G_n` only tracks the BOUNDED, FIXED `P_1`-alphabet, `\le2^k-1` symbols,
unconditional via the already-certified Theorem CD).

**Technique:** attack Step 2's target via a **bounded-run-length /
pigeonhole argument** on the fixed, finite core alphabet, explicitly NOT
via bounded-window Markov PREDICTION of `G_{n+1}` (round 4's specific
mechanism, proven false — the window size needed to predict exactly
equals the true period, circular as a proof method) and NOT via the dead
seesaw/Complement-Bound mechanism (already shown, round 11, Lemma
CB/Prop CB-2/Cor CB-3, to give no leverage on bounding any single class
away from `0`). This is a genuinely different, third proof route for the
same Step-2 target: an INEQUALITY claim (how long can one core-type
persist) rather than a PREDICTION claim (what is the exact next symbol)
— this distinction is precisely what sidesteps round 4's circularity.

**Skeleton (retarget Step 2 only; Steps 1, 3–4 below unchanged, still
valid, cite verbatim):**
2′. **Bounded-Run-Length Lemma (new Step 2, the crux).** Claim: for a
   doubly-infinite disjoint pair `(S,S')`, there is a finite `R=R(a_1)`
   such that within any window of `R` consecutive indices, the core
   sequence cannot avoid `S'` entirely (precise combinatorial form to be
   pinned down by the builder first — e.g. "no `R+1` consecutive terms
   `a_n,\dots,a_{n+R}` all have core disjoint from `S'`"). Attempt via:
   since `a_{n+1}` is the SMALLEST admissible integer greater than
   `a_n`, and admissibility only requires intersecting the current
   finite minimal antichain (Lemma W3, already certified), argue that
   reusing a `P_1`-prime (small, from a FIXED finite set, frequently
   available) is a cheaper way to satisfy multiple disjoint-core
   antichain constraints simultaneously than manufacturing an
   ever-larger companion bundle — formalize "cheaper" via the
   already-certified Growth Lemma's `O(n)` bound on `a_n` as an EXTERNAL
   ANCHOR (this target legitimately has such an anchor, unlike `(UB_S)`/
   `(MRS_S)`, since it concerns the bounded-alphabet `P_1`-projection,
   not an unbounded companion-prime set).
3′. **`(PD_{S,S'})` from Bounded-Run-Length** — immediate: if Step 2′
   gives a bounded run-length `R`, then `(PD_{S,S'})` follows with
   explicit constant `c=1/(R+1)` (elementary pigeonhole, no further
   machinery).
4′. **Exact periodicity from `n=1` (stronger, optional stretch goal,
   matches this round's KMP-verified numerics)** — only attempt after
   Steps 2′–3′ succeed; flag as a bonus, NOT required for Theorem SW's
   Stabilization Conjecture (which only needs the density hypothesis
   `(PD_{S,S'})`, not full periodicity of `G_n`).

**Key lemmas (claim + mechanism):**
- **Bounded-Run-Length Lemma (Step 2′, the crux, open)** — conjectured
  because `G_n` is empirically not just density-stable but EXACTLY
  periodic (a much stronger phenomenon) in `4/5` tested instances via
  rigorous KMP verification, and the greedy "smallest admissible" rule
  combined with the FIXED finite alphabet `P_1` gives a genuine external
  anchor (Growth Lemma) this target has that `(UB_S)`/`(MRS_S)` provably
  lack — not yet proved, structurally distinct from every previously-dead
  mechanism (not window-prediction, not seesaw/density-summing).
- `(PD_{S,S'})` from Bounded-Run-Length (Step 3′) — immediate pigeonhole,
  elementary.

**Open gaps:** Bounded-Run-Length Lemma itself (Step 2′) — the sole hard
new content; the general `|\mathcal T_\infty|\ge3` case (retained from
round 11, still open, lower priority); `a_1=21528751` (hardest instance)
remains numerically inconclusive for `G_n`-periodicity even at
`N=400{,}000` — flagged as a concrete next numerical sanity check for the
Bounded-Run-Length claim on the hardest case, not required before
attempting the general proof.

**Cases to cover:** as before (`|\mathcal T_\infty|=2` vs `\ge3`, Step 3
of the round-11 skeleton below); if Bounded-Run-Length is refuted on any
instance (a run longer than any proposed `R` is found), report precisely
which instance and run-length — a genuine refutation of Step 2′, not
just of one proof attempt.

**Watch out for:** do NOT re-attempt bounded-window Markov/finite-state
PREDICTION of `G_{n+1}` (round 4, dead — window size needed equals the
period, circular) — Bounded-Run-Length is an INEQUALITY claim, not a
PREDICTION claim, and this distinction is what sidesteps the round-4
circularity; keep it explicit in the write-up. Also do not resurrect the
"dyadic near-fraction" hint from round 10/11 as a proof strategy — this
round's exploration confirmed it is a coincidental artifact of
`a_1=4087`'s small period, not a general mechanism.

## Round 12 update (headline — read this first)

**Executed this round's outline (Step 2′/3′) in full, as a rigorous
CONDITIONAL theorem, exactly as the dispatch requested: "IF `G` is
eventually periodic THEN `(PD_{S,S'})` holds" — proved completely and
unconditionally as an implication, with explicit constants, in new Part 11
below. The periodicity hypothesis itself remains open (not proved this
round, matching round 11's own honest circularity diagnosis, re-confirmed
below); Status stays `partial`.**

**What is new and fully proved this round (Part 11, no gaps).**
- **Lemma BRL-from-Periodicity.** If `G` (the coarse `P_1`-core sequence)
  is eventually periodic with pre-period `n_0` and period `T`, then for
  every core `S'` with `I_{S'}` infinite, no run of `R+1:=n_0+T+1`
  consecutive indices can entirely avoid `I_{S'}` — a purely combinatorial
  consequence of eventual periodicity, invoking no other hypothesis
  (in particular NOT `(\dagger')`, so no circularity with Theorem SW/5.1's
  own chain).
- **Lemma PD-from-BRL.** The Bounded-Run-Length property, for any `R`, gives
  `|I_{S'}\cap[1,N]|\ge\lfloor N/(R+1)\rfloor` for every `N`, hence
  `(PD_{S,S'})` with the fully explicit constant `c=1/(2(R+1))`,
  `i_0=2R+4` — an elementary pigeonhole argument, exactly the bridge the
  round-12 outline-reviewer independently checked and confirmed sound
  (`/tmp/round-12/outline-reviewer.md`, "Central finding 2").
- **Theorem PD-Conditional.** Combining the two: IF `G` is eventually
  periodic for a given `a_1` (pre-period `n_0`, period `T`), THEN **every**
  doubly-infinite disjoint core pair `(S,S')` of that `a_1` satisfies
  **both** `(PD_{S,S'})` and `(PD_{S',S})`, with a **uniform** constant
  `c=1/(2(n_0+T+1))` depending only on `a_1` (via `n_0,T`), not on the
  specific pair. Combined with the already-certified Proposition 9.4, this
  further gives a uniform conditional `O(\log i)` magnitude cap on the
  pigeonhole witness prime for every doubly-infinite disjoint pair of that
  `a_1`.

**What remains open, honestly.** (a) Eventual periodicity of `G` itself is
**not proved** in general this round — a fresh, targeted attempt (Part
11.5) at an `H`-independent mechanism found none, reconfirming round 11's
circularity diagnosis (Part 10.3) in this round's own sharper
Bounded-Run-Length language, not just restating it. (b) Even granting
periodicity, the Theorem PD-Conditional chain still leaves Part 9.6's Step
5 "reuse into a finite pool" gap completely untouched — `(PD_{S,S'})` (now
conditionally closed) was never the whole Stabilization Conjecture, only
Step 4 of it; this round's contribution narrows Step 4 to a single
periodicity hypothesis, it does not close Step 5. (c) Numerically (not a
proof, per CLAUDE.md), periodicity-from-`n=1` is independently confirmed by
two fresh KMP-based generators (this round's math-explorer and the
outline-reviewer) for 4 instances (`4087\to T=64`, `247\to T=1806,
2747\to T=2062`, `4199\to T=105250`), each checked over `\ge2` full extra
repeats of the period (`247` checked over `1600+` repeats), and remains
genuinely inconclusive within the tested range (`N\le4\times10^5`) for the
workspace's hardest instance, `a_1=21528751`.

## Round 11 Outline (proof-outliner directive — attack `(PD_{S,S'})`
directly via a from-scratch structural argument on the greedy
construction's finite core-partition, not an imported density tool)

**Target (unchanged): the whole problem**, via Theorem SW → Proposition
9.4 → Theorem 5.1 (all already certified/conditional, do not re-derive).
This round retargets the sole open ingredient of Proposition 9.4,
Hypothesis `(PD_{S,S'})`, per this round's pd-lens explorer's confirmation
(`/tmp/round-11/math-explorer-pd.md`) that no KB/corpus density tool
transfers and the retired Landau–Turán toolkit is circular here (its
Imprint Periodicity Lemma assumes the conclusion, exact periodicity, as
its own hypothesis).

**Technique:** an unconditional "Complement Bound" identity (a cheap,
exact fact about the finite core-partition, worth certifying regardless
of outcome) combined with a from-scratch attempt at a genuinely weaker,
more tractable target — an eventual near-periodicity of class membership
derived from the greedy rule's OWN finite-state structure (pd explorer's
opening 2), rather than a generic density inequality.

**Skeleton:**
1. **Complement Bound Lemma** (new, cheap, unconditional — prove this
   first regardless of the rest). Since `\{I_T:T` a proper core or
   `P_1\}` partitions `ℕ` exactly, `\Sigma_T|I_T\cap[1,N]|=N` for every
   `N`. By Theorem SW's case split, only finitely many `T` have `I_T`
   finite (each contributing `O(1)` uniformly in `N`); hence
   `\Sigma_{T\in\mathcal T_\infty}|I_T\cap[1,N]|=N-O(1)`, where
   `\mathcal T_\infty` is the FIXED finite set of proper cores with `I_T`
   infinite. **Honest scope note:** this alone does NOT force any single
   `|I_T\cap[1,N]|/N` to stay bounded away from `0` (a sum of finitely
   many nonnegative sequences converging to `1` does not prevent one term
   individually `\to0`) — state this limitation explicitly, do not
   oversell.
2. **Opening 2 (primary target): individual-class eventual
   near-periodicity.** Conjecture, and attempt to prove directly from the
   greedy recursion's own definition (not from an abstract partition
   fact, avoiding the circularity pd explorer identified): each infinite
   class `I_S`'s membership indicator eventually settles into a fixed
   period modulo some finite, `S`-dependent integer `M_S` (not assumed a
   priori, but shown to exist from the recursion's finite-state
   structure). If `M_S` exists, `(PD_{S,S'})` follows immediately
   (frequency `\ge1/(M_S\cdot M_{S'})` within any window of length
   `\mathrm{lcm}(M_S,M_{S'})`). Use the `a_1=4087` dyadic-near-fraction
   curiosity (pd explorer's finding, `33/64`, `15/32`) as a concrete
   numeric hint for what `M_S` might look like (dyadic — built from
   2-adic valuation structure of the admissibility test) worth checking
   algebraically before a general proof attempt.
3. **Fallback (opening 1, if Step 2 stalls).** Iterate Lemma RD
   symmetrically (apply it both to `J:=I_{S'}\cap[1,i)` at `i\in I_S` and
   to `J':=I_S\cap[1,j)` at `j\in I_{S'}`) to get a seesaw relation
   between consecutive gaps; combine with the Complement Bound Lemma
   (Step 1) restricted to the special case `|\mathcal T_\infty|=2` (only
   `S,S'` infinite, no third infinite sibling) where the seesaw plus
   sum-to-1 DOES force both densities bounded away from `0`; prove this
   special case first as a clean partial result, then assess whether the
   general `|\mathcal T_\infty|\ge3` case needs materially more.
4. **Honest risk flag** (carry over, do not re-verify unless closing
   Steps 2–3): even if `(PD_{S,S'})` is established, Propositions
   ND1/ND2 (already certified) document that the Step-5 "collect the
   per-index witnesses into one finite pool" construction is a known
   failure mode for the architecturally identical unrestricted Domination
   Lemma — closing `(PD_{S,S'})` alone will likely not finish Theorem
   SW's Stabilization Conjecture for this channel without a materially
   different Step 5; flag this to whichever round attempts Step 5, do not
   let it block this round's `(PD_{S,S'})` attempt.

**Key lemmas (claim + mechanism):**
- Complement Bound Lemma — because the core classes exactly partition
  `ℕ` (tautological) and only finitely many are finite (Theorem SW), an
  exact identity, cheap to certify.
- `|\mathcal T_\infty|=2` special case (seesaw + sum-to-1 ⟹ positive
  density) — because with only two infinite classes, the Complement Bound
  forces `|I_S\cap[1,N]|+|I_{S'}\cap[1,N]|=N-O(1)`, and Lemma RD's
  per-index witness existence (already certified) prevents either class
  from being arbitrarily sparser than the other over any window without
  producing an unbounded-magnitude witness prime, contradicting the
  Growth Lemma's `O(N)` bound on `a_n` (mechanism to be made precise by
  the builder, not yet fully worked out — flagged as the concrete
  near-term target).
- Eventual near-periodicity of class membership (Step 2, open, the
  primary hoped-for closer) — conjectured because the greedy rule is a
  finite-state-flavored recursion and the numeric density ratios look
  suspiciously close to small-denominator (dyadic) fractions in at least
  one instance; NOT yet proved, and NOT guaranteed to hold in general
  (report honestly if a non-dyadic, seemingly irrational-looking ratio is
  found in further testing — this would refute Step 2 specifically, not
  necessarily `(PD_{S,S'})` itself).

**Open gaps:** Step 2 (does class membership indicator become eventually
periodic — undetermined, the central open content); the
`|\mathcal T_\infty|\ge3` general case of Step 3's seesaw argument (only
the 2-class special case is sketched); Step 4's Propositions ND1/ND2 risk
(not this round's job to resolve, but must not be forgotten).

**Cases to cover:** `|\mathcal T_\infty|=2` vs `|\mathcal T_\infty|\ge3`
(Step 3); if Step 2's eventual periodicity is refuted on any instance,
the approach must fall back to Step 3/1 only, and report the refutation
precisely (which instance, which ratio, to what precision).

**Watch out for:** do not mistake "ratio looks numerically flat over the
tested range" for a proof of either density or periodicity — this
workspace's own standing rule (extend any "looks stable" claim by `\ge10x`
past the previous cutoff before trusting it) applies here with full
force, especially for Step 2's periodicity claim, which is a much
stronger statement than mere density stability.

## Round 11 update (headline — read this first)

**Executed this round's outline in full. Step 1 (Complement Bound Lemma) is
now proved completely, precisely, and unconditionally (promotable). Steps 2
and 3, attempted rigorously, both terminate in genuine, sharply-stated
negative findings rather than a closing argument — recorded honestly below,
not papered over. Status remains `partial`; the Stabilization Conjecture
(equivalently `(PD_{S,S'})`) is not closed this round.**

### 10.1 — Complement Bound Lemma (Step 1), proved in full, unconditional

**Setup.** Let `k:=|P_1|`. By the already-certified Theorem CD, every index
`n\ge1` has a well-defined core `S(n)\subseteq P_1` (nonempty), taking at
most `2^k-1` distinct values, and `\{I_S:S\text{ a core}\}` partitions
`\mathbb N` exactly (disjoint, union `=\mathbb N`). Write `\mathcal
T_\infty:=\{S:I_S\text{ infinite}\}` and `\mathcal T_{\mathrm{fin}}:=\{S:I_S
\text{ finite}\}` for the (fixed, finite, and finitely-many-in-number, since
there are only `\le2^k-1` cores total) partition of all realized cores into
infinite- and finite-class types. Define
$$F:=\sum_{S\in\mathcal T_{\mathrm{fin}}}|I_S|,$$
a finite sum of finite numbers (there are at most `2^k-1` terms, each
itself finite by definition of `\mathcal T_{\mathrm{fin}}`), hence a
well-defined fixed nonnegative integer depending only on `a_1` (not on
`N`).

**Lemma CB (Complement Bound).** For every `N\ge1`,
$$N-F\ \le\ \sum_{S\in\mathcal T_\infty}|I_S\cap[1,N]|\ \le\ N.$$

**Proof.** Since `\{I_S:S\text{ a core}\}` partitions `[1,N]` (every
`n\in[1,N]` lies in exactly one `I_S`, by Theorem CD), summing over *all*
cores gives `\sum_{S\text{ core}}|I_S\cap[1,N]|=N`. Splitting the sum by
`\mathcal T_\infty` vs. `\mathcal T_{\mathrm{fin}}`:
$$\sum_{S\in\mathcal T_\infty}|I_S\cap[1,N]|\ =\ N-\sum_{S\in\mathcal T_{\mathrm{fin}}}|I_S\cap[1,N]|.$$
For each `S\in\mathcal T_{\mathrm{fin}}`, `0\le|I_S\cap[1,N]|\le|I_S|`
(intersecting a set with `[1,N]` can only shrink it), so
`0\le\sum_{S\in\mathcal T_{\mathrm{fin}}}|I_S\cap[1,N]|\le\sum_{S\in\mathcal
T_{\mathrm{fin}}}|I_S|=F`. Substituting these two-sided bounds into the
displayed identity gives `N-F\le\sum_{S\in\mathcal T_\infty}|I_S\cap
[1,N]|\le N`. $\blacksquare$

**Honest scope note (stated explicitly, per the outline's own instruction
— do not oversell).** Lemma CB is an *exact identity up to a fixed additive
constant* relating the **sum** of the infinite-class densities to `N`; it
places **no** individual constraint on any single `|I_S\cap[1,N]|`. In
particular it is logically consistent with `\mathcal T_\infty=\{A,B\}`
and `|A\cap[1,N]|=N-\lfloor\sqrt N\rfloor`, `|B\cap[1,N]|=\lfloor\sqrt
N\rfloor` for all `N` (a bona fide partition satisfying Lemma CB's
conclusion with `F=0` exactly), in which `B` has natural density `0`
despite being infinite — the abstract identity alone never rules this out.
This is why Step 3's naive hope (below) does not, in fact, close anything
by itself.

### 10.2 — the `|\mathcal T_\infty|=2` special case: an exact
Density-Equivalence identity, and why it gives **no independent
leverage** on `(PD_{S,S'})` (a sharper, corrected diagnosis of Step 3)

This subsection carries out Step 3 of this round's outline (the seesaw /
`|\mathcal T_\infty|=2` special case) as far as it rigorously goes. The
outline hoped that, restricted to exactly two infinite cores, the
Complement Bound plus a "seesaw" argument would *force* both densities away
from `0`. Executed carefully, this hope is **not realized**: what results
instead is an *exact identity* showing `(PD_{S,S'})` is, in this special
case, **literally equivalent** — not merely related, but equal up to an
explicit vanishing error term — to a **one-sided** statement (an upper
bound on `I_S`'s own density along itself) that Lemma CB supplies no new
information about. This is a genuine, if negative, finding: it shows
precisely why the "sum-to-`N-O(1)`" identity cannot by itself break the
symmetry between the two classes, sharpening the outline's own honest
"mechanism not yet worked out" flag into a precise "this specific
mechanism structurally cannot work" statement.

**Standing hypothesis for this subsection.** `\mathcal T_\infty=\{S,S'\}`
exactly (i.e. `S,S'` are the *only* two cores with an infinite index
class — a genuine additional restriction on `a_1`'s core structure beyond
"`(S,S')` is a doubly-infinite disjoint pair," since in general other
infinite proper cores may coexist; Theorem SW needs the Stabilization
Conjecture for *every* doubly-infinite pair, so this subsection's result
applies only to those `a_1` for which some pair happens to exhaust
`\mathcal T_\infty`, not to the general case).

**Notation.** Enumerate `I_S=\{s_1<s_2<\cdots\}$. For `i=s_k\in I_S` write
`\rho(i):=|I_S\cap[1,i]|/i=k/i` (so `\rho` is evaluated only at `I_S`'s own
points) and, as before, `J_i:=|I_{S'}\cap[1,i)|`. Symmetrically for
`j\in I_{S'}`.

**Proposition CB-2 (Density-Equivalence, exact).** In the standing
hypothesis above,
$$\liminf_{i\in I_S,\ i\to\infty}\frac{J_i}{i}\ =\ 1-\limsup_{i\in I_S,\ i\to\infty}\rho(i).$$
Consequently `(PD_{S,S'})` holds if and only if
`\limsup_{i\in I_S}\rho(i)<1`.

**Proof.** Fix `i=s_k\in I_S`. Since `i\in I_S`, `I_S\cap[1,i]=I_S\cap[1,i)
\cup\{i\}`, so `|I_S\cap[1,i]|=k` and (as `i\notin I_{S'}$) `I_{S'}\cap
[1,i]=I_{S'}\cap[1,i)`, of size `J_i`. Applying Lemma CB with `N=i` (valid
since `\mathcal T_\infty=\{S,S'\}` by hypothesis, so the sum in Lemma CB is
exactly `|I_S\cap[1,i]|+|I_{S'}\cap[1,i]|=k+J_i`):
$$i-F\ \le\ k+J_i\ \le\ i.$$
Define `e_i:=i-k-J_i`; the displayed inequality is exactly `0\le e_i\le F`.
Dividing by `i`:
$$\frac{J_i}{i}=1-\frac{k}{i}-\frac{e_i}{i}=1-\rho(i)-\frac{e_i}{i}.$$
Since `0\le e_i/i\le F/i\to0` as `i\to\infty` (through `I_S`, `F` fixed),
$$\liminf_{i\in I_S}\frac{J_i}{i}=\liminf_{i\in I_S}\Bigl(1-\rho(i)-\frac{e_i}{i}\Bigr)=1-\limsup_{i\in I_S}\Bigl(\rho(i)+\frac{e_i}{i}\Bigr)=1-\limsup_{i\in I_S}\rho(i),$$
where the last equality holds because adding a sequence converging to `0`
to `\rho(i)` does not change its `\limsup` (standard fact: if `x_i\to0`
then `\limsup(\rho(i)+x_i)=\limsup\rho(i)`, since for every `\varepsilon>0`,
eventually `|x_i|<\varepsilon`, so `\rho(i)-\varepsilon<\rho(i)+x_i<
\rho(i)+\varepsilon`, squeezing the limsups together as `\varepsilon\to0`).

For the "consequently" clause: `(PD_{S,S'})` (as defined in Part 9.3,
`\exists c>0,i_0` with `J_i/i\ge c` for all `i\in I_S`, `i\ge i_0`) holds
iff `\liminf_{i\in I_S}J_i/i>0`, which by the displayed identity holds iff
`\limsup_{i\in I_S}\rho(i)<1`. $\blacksquare$

**Corollary CB-3 (the "own density" reformulation).** `\limsup_{i\in
I_S}\rho(i)` equals the ordinary upper natural density of `I_S` in
`\mathbb N`, `\overline d(I_S):=\limsup_{N\to\infty}|I_S\cap[1,N]|/N`.

*Proof.* For any `N\ge1`, let `s_k` be the largest element of `I_S` with
`s_k\le N` (exists once `N\ge s_1`, since `I_S` is infinite hence
unbounded, so eventually every `N` has such a predecessor); then
`|I_S\cap[1,N]|=k` (no further elements of `I_S` occur in `(s_k,N]` by
maximality of `s_k`), so `|I_S\cap[1,N]|/N=k/N\le k/s_k=\rho(s_k)` (since
`N\ge s_k`, so `k/N\le k/s_k`). Hence `\sup_{N\ge M}|I_S\cap[1,N]|/N\le
\sup_{i\in I_S,i\ge M}\rho(i)` for every threshold `M`, giving
`\overline d(I_S)\le\limsup_{i\in I_S}\rho(i)`. Conversely, `I_S\subseteq
\mathbb N`, so the sequence `(|I_S\cap[1,N]|/N)_{N\ge1}` already includes
every value `\rho(i)$, `i\in I_S`, as a special case (`N=i`), so
`\limsup_{i\in I_S}\rho(i)\le\overline d(I_S)`. Combining, equality.
$\blacksquare$

**What this shows, precisely.** Combining Proposition CB-2 and Corollary
CB-3: in the `|\mathcal T_\infty|=2` special case, `(PD_{S,S'})` is
**exactly equivalent** to `\overline d(I_S)<1$ (`I_S`'s own upper natural
density is bounded away from `1`) — a statement purely about the ONE class
`I_S`, with **no reference to `I_{S'}` at all** beyond the tautological
fact that it is `I_S`'s complement (up to the fixed finite junk `F`).
Lemma CB (the sum identity) is exactly the tool used to derive this
equivalence, and it is **all** the sum identity can give: it converts the
two-class density question into a one-class upper-density question, but
supplies no argument bounding `\overline d(I_S)` away from `1` — that
would require a genuinely different, one-sided fact about the greedy
recursion's own arithmetic (e.g., some inherent reason a single core class
cannot absorb "almost all" indices), which neither Lemma CB, nor Lemma RD,
nor the Magnitude Bound Corollary (checked directly below) supplies.

**Why the "seesaw" (iterating Lemma RD in both directions) does not
close the resulting one-sided gap either — checked directly.** Suppose,
toward finding a contradiction, `\overline d(I_S)=1` (the failure mode):
there is a subsequence `i_m=s_{k_m}\in I_S` with `\rho(i_m)\to1`, i.e.
`J_{i_m}/i_m\to0`. By the Magnitude Bound Corollary (Part 9.2, already
certified this workspace), applied with `m=i_m`, `J=I_{S'}\cap[1,i_m)`,
this only yields `q(i_m)\le\omega(a_{i_m})a_{i_m}/J_{i_m}`, an upper bound
that **grows** (in fact blows up, since `J_{i_m}=o(i_m)`) — it does not
supply any independent fact forcing a contradiction, because nothing in
this workspace's certified machinery lower-bounds `q(i_m)`. Symmetrically,
for `j\in I_{S'}` (now the *dense* class's complement, hence `I_S\cap[1,j)`
is close to all of `[1,j)`), the Magnitude Bound Corollary gives
`q'(j)\le\omega(a_j)a_j/|I_S\cap[1,j)|=O(\log j)` — a genuine but *growing*
(not fixed) cap; this says every `j\in I_{S'}` has *some* small-ish prime
factor among its companions, which is not by itself impossible (many
integers have small prime factors) and does not contradict the Growth
Lemma or any other already-certified fact. **No contradiction was found
either from Lemma CB alone or from combining it with Lemma RD/the
Magnitude Bound Corollary.** This directly confirms — with an explicit
computation, not just a restated worry — the outline's own honest
"mechanism to be made precise... not yet fully worked out" flag: having
made it precise, it does not, in fact, work as hoped. This is recorded as
a genuine negative finding for Step 3, sharper than before it was
attempted in full.

### 10.3 — Step 2 (eventual near-periodicity of class membership): a
precise circularity diagnosis, not a proof or disproof

This round attempted Step 2 directly: does the core-membership sequence
`(S(n))_{n\ge1}` become eventually periodic (mod some finite, `S`-dependent
`M_S`), established from the greedy recursion's own structure without
assuming a covering set `H` already exists (which would be circular, since
`H`'s existence is precisely what Theorem SW's Stabilization Conjecture —
the target this whole file is chasing — is used to establish)?

**One small, real, unconditional observation (worth recording, though it
does not by itself help).** The core sequence `(S(n))_{n\ge1}` already
lives in a **fixed finite alphabet** unconditionally: by the already-
certified Theorem CD, `S(n)\in\{\text{nonempty subsets of }P_1\}`, a set of
size `\le2^k-1$, for *every* `n`, with no hypothesis beyond the sequence's
definition. So "does this sequence become eventually periodic" is at least
a well-posed question about a finite-alphabet sequence — it is **not**
automatically true, however: a sequence over a finite alphabet need not be
eventually periodic unless the process generating it is itself governed by
a bounded amount of state (a genuine extra fact, not implied by
finiteness of the alphabet alone — e.g. a process whose next symbol
depends on an ever-growing counter, even one taking values in a bounded
codomain via a projection, need not be eventually periodic).

**The circularity, made precise.** The only mechanism this workspace has
for reducing `a_{n+1}`'s dependence on the *entire* history
`a_1,\dots,a_n` to a *bounded* amount of state (namely, the single residue
`r_n=a_n\bmod L`) is Theorem 2.2/Corollary 3.1 (Part 2–3 above) — and both
are proved **using hypothesis `(\dagger')`** (existence of the finite
covering set `H`) essentially: Theorem 2.2's proof, part (a), invokes
`(\dagger')` applied to the pair `(i,n+1)` for *every* `i\le n` to show
`a_{n+1}` is admissible against the *compressed* summary `\Sigma_n$ rather
than needing to check `\gcd(a_{n+1},a_i)>1` against each `a_i` individually
via its *full* radical. Without `(\dagger')`, there is no known reduction
of "`x` admissible at step `n`" (i.e. `\gcd(x,a_i)>1$ for *every* `i\le n`)
to a check depending only on a bounded amount of information about the
prefix `a_1,\dots,a_n` — a priori it could depend on all `n` of the
individual radicals `\mathrm{rad}(a_1),\dots,\mathrm{rad}(a_n)`, an
unboundedly growing amount of data as `n\to\infty`. Consequently, any
proof that the *core* sequence `(S(n))` (a coarser summary than the full
residue `r_n`, but still an output of the same admissibility-driven
recursion) is eventually periodic would need **either**:
(a) a genuinely different, `H`-independent argument showing the
recursion's core-relevant behavior is governed by bounded state (not
currently known, and this round found no candidate construction for one —
attempting to build such a "reduced" covering fact restricted to `P_1`
alone runs into exactly the same open difficulty as `(\dagger')`/`(PD_
{S,S'})$ itself, since which primes of `P_1` divide the *next* admissible
integer depends, in the worst case, on gcd tests against the full,
unbounded history just as much as full admissibility does); **or**
(b) implicitly assuming something at least as strong as the Stabilization
Conjecture (or `(\dagger')` itself) as an unstated input, which would make
Step 2 circular relative to this file's own proof architecture (Theorem
SW: Stabilization `\Rightarrow` FCBC `\Rightarrow`, via Theorem 5.1,
periodicity) — using periodicity-flavored machinery to *derive*
Stabilization, when Stabilization is what is needed to legitimately
*obtain* that machinery in the first place.

**Consequence.** Step 2, as posed by this round's outline, is **not**
closed, and this round did not find a way to attempt it that avoids this
circularity. The `a_1=4087` dyadic-fraction numeric curiosity
(`33/64`,`15/32`, flagged by this round's pd-lens explorer) was **not**
investigated further algebraically this round — doing so honestly would
require either (i) finding the `H`-independent finite-state mechanism
described in (a) above (not found), or (ii) treating the observation as
purely numerical corroboration only (per CLAUDE.md, insufficient for a
proof step regardless of how clean the fraction looks). Reported honestly
as unexplored rather than fabricating a derivation.

### 10.4 — Summary of this round's contribution

- **Lemma CB (Complement Bound)** — proved in full, unconditional, cheap,
  reusable (Part 10.1). Promotable.
- **Proposition CB-2 + Corollary CB-3 (Density-Equivalence)** — proved in
  full, unconditional given `\mathcal T_\infty=\{S,S'\}` (Part 10.2).
  A genuine, exact structural fact — but its content is **negative** for
  this round's purposes: it shows the outline's Step 3 fallback mechanism
  provides **no independent leverage** on `(PD_{S,S'})`, converting the gap
  into an equivalent one-sided statement rather than closing it. This is a
  sharper, more precise diagnosis than the outline's own "not yet fully
  worked out" flag — now it is fully worked out, and found not to close.
- **Step 2 circularity diagnosis (Part 10.3)** — a precise argument for why
  "eventual near-periodicity of class membership from the recursion's own
  finite-state structure" is not attackable independently of `(\dagger')`
  without either a new `H`-independent mechanism (not found) or implicit
  circularity — new content this round, sharper than any prior diagnosis of
  this specific route.
- **`(PD_{S,S'})` itself remains open.** No proof, no disproof. All three
  routes this round's outline proposed (Complement Bound alone; the
  `|\mathcal T_\infty|=2` seesaw fallback; eventual periodicity) were
  attempted rigorously and each terminates in a precise, honestly-recorded
  obstruction rather than a fabricated closure. Status stays `partial`.

## Round 10 update (headline — read this first)

**Executed this round's outline (Steps 1–3 in full, rigorously, with
explicit constants); Steps 4–5 remain genuinely open, and this round adds
real, honest content on *why*.**

**New, fully proved (Part 9 below): Lemma RD (Restricted Domination Lemma)
and the Magnitude Bound Corollary.** A clean, unconditional generalization
of the already-certified Domination Lemma (`lemmas/domination-lemma.md`):
for any index `m` and any subset `J\subseteq\{1,\dots,m-1\}`, pigeonhole on
`a_m`'s `\omega(a_m)` prime factors (using the already-certified Lemma P′,
not the special "admissibility at construction time" the original lemma
used) gives a single prime `q(J,m)\in\mathrm{rad}(a_m)` dividing at least
`|J|/\omega(a_m)` elements of `J`. Combined with the already-certified
Growth Lemma (`lemmas/lemma-1-uniform-gap-bound.md`) and the elementary
bound `\omega(m)\le\log_2m`, this gives the **explicit, fully proved**
inequality `q(J,m)\le\omega(a_m)\cdot a_m/|J|`, specialized to
`J=J_i:=I_{S'}\cap[1,i)` for `i\in I_S`: **conditional on a positive-density
hypothesis `(PD_{S,S'})`** (stated precisely below — `|J_i|\ge c\cdot i` for
a fixed `c>0` and all large `i\in I_S`), this yields `q(i)=O(\log i)` with
**fully explicit constants** `q(i)\le\frac{a_1+L}{c}(\log_2(a_1+L)+\log_2i)`.
This is the outline's Step 3 target, done completely, no gap.

**The honest remaining gap, sharpened.** `(PD_{S,S'})` (positive density of
one class along the other) is **not** established, and this round found and
records a real reason it is **not** a free consequence of anything currently
certified: a finite partition of `\mathbb N` can have an infinite member of
density exactly `0` (explicit counterexample: squares vs. non-squares,
Part 9 below) — so Theorem CD's `\le2^k-1`-class partition alone gives no
such bound, and no argument using only the certified bounded-gap
(`a_{n+1}-a_n\le L`) or global Domination Lemma facts was found this round
that forces a *specific* proper core's class to avoid density decay. The
Euler-divergence/Landau-Count toolkit that refuted `(UB_S)`
(`lemmas/theorem-UBS-false-case-II.md`) is **not** reusable here without
circularity: that argument's density conclusion was derived *from* an
assumed exact periodicity, which is exactly what Theorem 5.1 would only
supply *after* FCBC (hence Stabilization) is established — using it to prove
`(PD_{S,S'})` first would assume the conclusion. This is recorded honestly
as new negative diagnostic content, not asserted as a proof of impossibility
(no disproof of `(PD_{S,S'})` was found either — see the numerical evidence
below, which is consistent with it).

**A second, independent honest finding: even granting `(PD_{S,S'})` fully,
Step 5 (pooling the per-index dominant primes into one finite set) faces a
*known* failure mode in this workspace.** The already-certified Propositions
ND1/ND2 (`lemmas/proposition-ND1-ND2-domination-mechanisms-insufficient.md`)
prove, by explicit hand-verified computation, that neither "collect the
unique per-step Domination-Lemma argmax prime" nor its natural broadening
("collect every prime meeting the averaged pigeonhole threshold at the step
where it's tested") produces a valid FCBC covering set — a specific pair's
unique shared prime can simply never be *anyone's* chosen witness. Lemma
RD's per-index `q(i)` is architecturally the same kind of object (a
pigeonhole-selected witness at a triggering index); by direct analogy, a
literal "collect all the `q(i)`'s" construction is not expected to work
either without a materially different selection principle — this is *not*
proven to fail here (ND1/ND2 concern the *unrestricted* Domination Lemma,
not this round's restricted, cross-class version), but it is a concrete,
certified precedent that the naive version of Step 5 is unlikely to close
the gap as stated, and any future attempt should design around this
specific documented failure mode rather than rediscover it from scratch.

**Fresh numerical corroboration (this round, independently computed, not
reused from any sibling report).** A freshly written, brute-force-validated
generator (validated bit-for-bit against a from-scratch pure-gcd brute force
on `a_1=247,105,4199` through `n=400` before trusting it at scale) run on
`a_1=618=2\cdot3\cdot103` (`k=3`, a deliberately asymmetric case — one small,
one large prime) shows all four core-class densities **exactly stable to
4–5 significant figures** from `n=5{,}000` through `n=200{,}000`
(`\{2\}\to0.6602`, `\{2,3\}\to0.3301`, `\{2,103\}\to0.00647`,
`\{2,3,103\}\to0.00324`, checked at 5 checkpoints, essentially bit-identical
ratios throughout) — consistent with (but, per CLAUDE.md, not a proof of)
`(PD_{S,S'})`, and consistent with this round's math-explorer's independent
finding that the sparsest documented class in the workspace's history
(`I_{1061}`, `a_1=21528751`, density `\approx0.030\%`) is also stable, not
decaying, across checkpoints from `N=50{,}000` to `500{,}000`. No instance
of apparent density decay was found in any test run this round or reported
by any sibling this round.

**Verdict for this round's own content:** genuine, complete, new,
promotable unconditional lemmas (Lemma RD, Magnitude Bound Corollary); the
Stabilization Conjecture itself remains open; Status stays `partial`. This
round's contribution is best summarized as: turned the outline's Step 3 from
a heuristic sketch into a fully rigorous conditional inequality, and
precisely diagnosed — with a concrete counterexample-style argument and a
concrete certified precedent — *why* both remaining steps (Step 4's density
hypothesis, Step 5's reuse argument) are hard, rather than leaving them as
unexamined "TODO"s.

## Round 10 Outline (proof-outliner directive — attack the Stabilization
Conjecture via a fresh, non-circular magnitude bound: Domination Lemma +
class-restricted growth bound)

**Target (unchanged, sharper than ever): the whole problem**, via the
already-certified chain Theorem SW → Theorem 5.1. Theorem SW (already
certified, do not re-derive) reduces FCBC to the **Stabilization
Conjecture**: for every doubly-infinite disjoint core pair `(S,S')`, a
finite `W_{S,S'}` exists with `rad(a_i)∩rad(a_j)∩W_{S,S'}≠∅` for all
`i∈I_S,j∈I_S'`.

**Technique for this round: quantitative pigeonhole/Domination-Lemma
magnitude bound** (round 10's H100-stabilization explorer's Opening 3,
`/tmp/round-10/math-explorer-H100-stabilization.md`) — genuinely different
from this file's own round-9 mechanism (greedy incremental witness-pool
construction, purely empirical) and from the other three approaches this
round (finite-window bitmask covering-design; well-ordering/minimal-
counterexample with bridge primes; Δ-system cross-covering). This is
**dispatch's suggested approach (b)**: "a general covering-set-existence
argument via the Domination Lemma + class-restricted growth bound."

**Skeleton:**
1. Fix a doubly-infinite disjoint core pair `(S,S')`. For each `i∈I_S`,
   let `J_i:=I_{S'}∩[1,i)` (the `S'`-side indices seen so far). Since
   `S∩S'=∅`, no `P_1`-prime can cover the pair `(i,j)` for `j∈I_{S'}`
   (orthogonal explorer's structural fact, `/tmp/round-10/math-explorer-
   orthogonal-stabilization.md` — worth restating and re-verifying, it is
   an immediate consequence of the already-certified Theorem CD's core
   decomposition, not a new hypothesis) — the covering prime must be a
   companion (non-`P_1`) prime of `a_i`.
2. By the already-certified **Domination Lemma**
   (`lemmas/domination-lemma.md`) applied to the finite set `J_i`: since
   `a_i` shares a prime with every `a_j`, `j<i` (Lemma P′, already
   certified), and `a_i` has `ω(a_i)` prime factors, pigeonhole gives a
   single prime `q(i)|a_i` dividing at least `|J_i|/ω(a_i)` of the `a_j`,
   `j∈J_i`.
3. By the already-certified **Growth Lemma**
   (`lemmas/lemma-1-uniform-gap-bound.md`, `a_n=O(n)`), the number of
   multiples of any fixed prime `q` below `a_i=O(i)` is `O(i/q)`; combined
   with Step 2's count (`≥|J_i|/ω(a_i)` multiples of `q(i)` below `a_i`),
   this gives `q(i)=O(ω(a_i)·i/|J_i|)`.
4. **Key Lemma (open, the actual gap — state and attempt, do not assume):**
   `I_{S'}` has **positive lower density** in `ℕ` (i.e. `|J_i|=Ω(i)` as
   `i→∞` along `I_S`). If this holds, combined with the trivial bound
   `ω(a_i)=O(\log a_i)=O(\log i)` (from `a_i=O(i)` and each prime factor
   `≥2`), Step 3 gives `q(i)=O(\log i)` — a genuine, if still growing,
   magnitude cap, far below `a_i` itself.
5. Step 4 alone does **not** give a FIXED finite `W_{S,S'}` (still
   unbounded, `O(\log i)→∞`). The remaining step, **not yet attempted by
   any approach**, is a "reuse" argument: show the *same* `O(\log i)`-range
   dominant primes recur (rather than a fresh one appearing at every `i`)
   — e.g. via a counting argument bounding the number of *distinct* primes
   that can ever serve as `q(i)` for infinitely many `i` (a pigeonhole on
   how many primes can each dominate a positive-density sub-family of
   `J_i` without contradicting Mertens' `Σ1/p` divergence rate — genuinely
   new content, attempt directly, cite Euler's divergence
   `lemmas/theorem-UBS-false-case-II.md` uses it already for a different
   purpose, the technique itself is reusable even though `(UB_S)` is not).

**Key lemmas (claim + mechanism):**
- **Positive density of `I_{S'}`** — because `I_{S'}` is one of finitely
  many (`≤2^k-1`) classes partitioning `ℕ` (Theorem CD) and is infinite by
  hypothesis (doubly-infinite pair); density Ω(1) is plausible but **not
  proven** — a class can be infinite with density 0 (e.g. primes have
  density 0 but are infinite). **This is the sharpest open sub-gap of this
  approach — do not assume it, attempt to prove or find a genuine
  counterexample (test on `a_1=247`, class `I_{13}`: does `|I_{13}∩[1,N]|/N`
  converge to a positive constant, numerically, before attempting a proof)**.
- **Dominant-prime reuse** — because only finitely many primes are `≤` any
  fixed magnitude, and if the magnitude cap `O(\log i)` is genuinely
  achieved by a SET of primes that must recur (not grow), a counting
  argument via Mertens/Euler divergence could force finiteness — **this is
  new, unattempted mechanism, the actual content to add this round**.

**Open gaps:** Step 4's positive-density hypothesis (test numerically
first); Step 5's reuse argument (entirely new, no prior attempt in this
workspace). **Do NOT** invoke `(MRS_S)`/`𝓥_S`-finiteness/`(UB_S)` anywhere
in this route — per the standing Rule, that family is retired; this route
is a genuinely fresh, from-scratch density/magnitude argument, not a
repackaging of it. If Step 4's density hypothesis turns out false on some
instance, the whole route needs Opening 3's caveat honestly reported as a
dead end for THIS mechanism (not for Stabilization itself — other
approaches this round attack it differently).

**Cases to cover:** none beyond the already-certified Theorem SW case
split (same-core/overlapping automatic; one-side-finite automatic; only
doubly-infinite disjoint pairs need this mechanism).

**Watch out for:** conflating "`I_{S'}` infinite" with "`I_{S'}` positive
density" — these are NOT the same (a class could be infinite, density 0,
e.g. growing like `\log i` per unit interval) — Step 4 is a genuine
additional hypothesis, prove it or find where it's needed less strongly
(e.g. `Ω(i/\log i)` might already suffice given `ω(a_i)=O(\log i)`,
worth checking the exact rate needed before assuming the strongest form).

## Round 9 update (headline — read this first)

**New, fully proved, unconditional reduction: Theorem SW (Stabilization
Sufficiency).** Executing the round's outline (Steps 1–4 below), this round
proves — in full, with no gap — that FCBC (hence, via this file's own
already-certified Theorem 5.1, the **entire** problem) follows from a
**genuinely narrower** hypothesis than raw FCBC: a finite witness pool need
only be exhibited for each pair of **disjoint proper cores with BOTH index
classes infinite** ("doubly-infinite disjoint core pairs"). Every other
case — same core, overlapping cores, or a disjoint pair with at least one
side finite — is disposed of **unconditionally**, using only already-
certified facts (Theorem CD's finite-core bound, Lemma P′, and the
certified Finite-Class Direct Covering lemma). This is a real reduction,
not a restatement: it isolates the exact residual content of FCBC to
finitely many well-defined sub-questions, one per doubly-infinite disjoint
core pair.

This new hypothesis (the **Stabilization Conjecture**, restated precisely
below) is **not proven** to be equivalent to the round-5 Channel
Assembly/Splitting machinery's `(LMRS_{S,S'})` — it only requires *some*
finite hitting set for the channel to exist, not that the specific
minimal-radical antichain `𝓜_n^{(S,S')}` stabilize. Since `(LMRS_{S,S'})`
is proven sufficient for the channel's covering fact (Channel Assembly
Theorem, `lemmas/channel-assembly-theorem.md`) but never proven necessary,
the Stabilization Conjecture is a priori weaker (easier to satisfy) —
matching the outline's own framing that this is "meaningfully more
general" than a single universal window. This file's own Theorem 5.1
remains the strongest existing infrastructure; today's contribution slots
in one level below it, narrowing FCBC itself further than any previous
approach's reduction.

**Numerical status of the Stabilization Conjecture itself.** Tested
directly (fresh Python, exact factorization, brute-force pairwise
verification, not reused from any sibling's script) on three disjoint
doubly-infinite core pairs, chosen to span the full difficulty range this
workspace has documented, including the sibling `explicit-window`
approach's newly-reported hard instance:

- `a_1=247` (`P_1=\{13,19\}`), pair `(S,S')=(\{13\},\{19\})`: `|I_{13}|=32292`,
  `|I_{19}|=20731` through `N=60000`. A **greedy incremental** witness-pool
  construction (process indices of both classes in increasing order,
  adding a new prime only when the current pool fails to cover a newly-
  formed cross pair) needed only **4** witnesses ever, `W=\{2,3,5,7\}`, with
  the **last** growth event at the 5th cross-relevant index (i.e. `W`
  stopped growing almost immediately). **Full verification**: brute-force
  checked all `669{,}445{,}452` cross pairs `i\in I_{13},j\in I_{19}`
  against `W=\{2,3,5,7\}` — **zero failures**.
- `a_1=2747` (`P_1=\{41,67\}`), pair `(\{41\},\{67\})`: `|I_{41}|=57613`,
  `|I_{67}|=1164` through `N=60000`. `W=\{2,3,5,7\}` again suffices for
  every one of the `\approx6.7\times10^7` cross pairs, zero failures.
- `a_1=21528751` (`P_1=\{103,197,1061\}`), pair `(\{1061\},\{103,197\})`:
  through `N=15000`, `|I_{1061}|=6`, `|I_{\{103,197\}}|=74`. The greedy
  incremental pool needed 5 witnesses, `W=\{2,3,7,11,97\}`, with growth
  events at indices `280,576,863,863,3441` and **no further growth**
  through `N=15000`. **This independently reproduces and explains** this
  round's sibling finding (`explicit-window-backbone-construction`'s
  discovery that `a_1=21528751` needs bridge prime `97` at the pair
  `n=596,863`): direct computation shows `a_{596}` has core `\{1061\}`,
  companions `\{2,3,5,7,97\}`; `a_{863}` has core `\{103,197\}`, companions
  `\{11,97\}`; their companion intersection is **exactly** `\{97\}` — the
  unique reason the naive small window `\{2,3,5,7,11,13\}` fails on this
  pair, and exactly the pair my framing predicts is the hard case (a
  doubly-infinite disjoint-core-pair witness, not covered by any
  finite-side shortcut). Once `97` is added, `W=\{2,3,5,7,11,13,97\}`
  covers every tested cross pair for this channel with zero further
  failures through `N=15000`.

**Additional evidence, deliberately adversarial: the two `a_1` values
(`4199,4087`) round 3 found make the raw GLOBAL canonical witness set `W`
very likely unbounded** (no plateau to `N=20000`, per `current.md`'s round-3
history — the strongest evidence in this workspace against a "single small
window works" hypothesis). Testing the per-core-pair Stabilization
Conjecture on **every** disjoint proper-core pair of both:

| `a_1` | pair `(S,S')` | `\lvert I_S\rvert,\lvert I_{S'}\rvert` (`N=40000`) | greedy pool `W_{S,S'}` | last growth trigger-index | full brute-force check |
|---|---|---|---|---|---|
| `4199` | `(\{13\},\{19\})` | `9304,6055` | `\{2\}` | `4` | `56{,}335{,}720` pairs, `0` failures |
| `4199` | `(\{13\},\{17\})` | `9304,20523` | `\{2,3,83\}` | `9` | `190{,}945{,}992` pairs, `0` failures |
| `4199` | `(\{17\},\{19\})` | `20523,6055` | `\{2,3\}` | `5` | `124{,}266{,}765` pairs, `0` failures |
| `4087` | `(\{61\},\{67\})` | `20625,18750` | `\{2\}` | `3` | greedy-trace verified over the full incremental construction (brute-force pass omitted for time) |

**Every one of the `\approx372` million brute-force-checked cross pairs
across these three adversarial channels is covered by a tiny (`\le3`-prime)
pool, with the pool's last-ever growth event occurring within the first
`\le9` cross-relevant indices** — the specific mechanism that makes the
*global* `W` unbounded for `a_1=4199,4087` (round 3) does **not** appear to
operate within any single disjoint-core-pair channel; whatever drives
global `W`'s growth must come from **switching between different
channels** (each individually easy), not from within-channel difficulty.
This is a new, testable structural observation this round adds to the
workspace's understanding of *why* FCBC (weak) can survive even though the
canonical `W` (strong) very likely fails.

**This is corroborating numerical evidence only, not a proof** (per
CLAUDE.md) — growth "stopping" up to a finite `N` does not establish it
stops forever, and `I_{1061}` only has `6` sampled members so far, too few
to be confident the channel has been stress-tested as hard as `a_1=247`'s.
The Stabilization Conjecture itself **remains open** — this round did not
find a general proof, and honestly could not close it in the time
available; it is exactly as hard, in the worst case, as the already-open
`(LMRS_{S,S'})` question for a single channel (round 5–9's residual
content), just possibly easier in principle since it does not require
antichain stabilization specifically.

**A small, fully proved, free structural fact (Lemma SW3, "peeling"), not
by itself sufficient to close the conjecture, but a genuine narrowing worth
recording.** For any disjoint proper-core pair `(S,S')` and **any** finite
subset `F\subseteq I_S` (not requiring `I_S` itself finite — this
generalizes Lemma SW2's hypothesis from "all of `I_S`" to "any finite piece
of it"), `H_F:=\bigcup_{i\in F}\mathrm{rad}(a_i)` is finite and
`H_F\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for every
`i\in F` and every `j\ne i` of the whole sequence, in particular every
`j\in I_{S'}`. *Proof.* Identical to Lemma SW2's proof, verbatim, with `F`
in place of `I_S` (finiteness of `I_S` was never actually used there beyond
guaranteeing `H_F` is a *finite* union — a finite subset `F` gives this just
as well). $\blacksquare$ **Consequence.** To prove the Stabilization
Conjecture for a doubly-infinite pair `(S,S')`, it suffices to handle the
*tail* behavior of `I_S` and `I_{S'}` — any finite prefix, in either
indexing, is automatically free, by Lemma SW3, no conjecture needed. This
matches exactly what the numerical trace shows (every growth event, in
every tested instance, clusters at a very small trigger-index, with the
tail apparently free) — but the tail's behavior in general remains open;
Lemma SW3 narrows *where* the difficulty could live, it does not remove it.

## Round 9 Outline (proof-outliner directive — redirect from "wait for
FCBC" to directly attacking FCBC, via a third independent technique)

**Context (read first).** Round 9's explorers found strong evidence
`(UB_S)` (round 8's sole reduction target for the whole population) is very
likely FALSE, but this does **not** threaten FCBC (`(†')`, this file's own
already-certified hypothesis for Theorem 5.1) — `(UB_S)`/`(MRS)` was only
ever *sufficient* for FCBC, never necessary. Per CLAUDE.md's reframe
guidance, this file's remaining content shifts this round from purely
waiting (previously "explicitly out of scope") to **directly attacking
FCBC**, using its own Universal Hitting Lemma A machinery as a third,
independent (necessity/witness-pool-driven, not constructive-density-driven
or S^+-seeded) technique alongside this round's two sibling FCBC attempts.

Skeleton (full detail in `/tmp/round-9/proof-outliner.md` under
`intersecting-family-covering-construction`):
1. Reuse Theorem CD's core decomposition (certified): finitely many cores.
2. For each pair of cores `(S,S')`, define the cross-witness pool
   `W_{S,S'} := ⋃_{i∈I_S,j∈I_{S'},i<j}(rad(a_i)∩rad(a_j))\setminus P_1`.
3. **Stabilization Conjecture (new, the real content):** each `W_{S,S'}`
   has a **finite** subset `W_{S,S'}^0` that already suffices to hit every
   `(S,S')`-cross pair, even if `W_{S,S'}` itself (union over ALL pairs) is
   infinite — genuinely different from `(UB_S)` (which bounds one bundle's
   size; this only asks a finite pool of *ever-used* witnesses suffices for
   coverage, compatible with individual bundles growing unboundedly, per
   round 9's own "0/1.3M avoid `{2,3,5,7,11,13}`" data).
4. `H := P_1 ∪ ⋃_{S,S'} W_{S,S'}^0`; invoke the already-certified Theorem
   5.1 to finish.

Open gap: Step 3 in full — the same underlying difficulty as sibling
approach `explicit-window-backbone-construction`'s Step 4, attacked via a
different route (witness-pool stabilization vs. prefix-nesting). Cross-
check candidate `H`s against that file's (round 4 found exactly this kind
of independent convergence before) but keep as separate techniques, do not
merge slugs.

## Round 3 update (headline)

**Gap 2 (periodicity from `n=1`, not just eventually) is now CLOSED COMPLETELY**,
conditional only on `(\dagger')` (existence of a finite covering set `H`, exactly
the same hypothesis Theorem 2.2/2.4 already used — no strengthening). Both
obstructions flagged by this round's outline are resolved in full:

- **Obstruction 1 (coincidence lemma).** Proved in 3 lines (Lemma A +
  Corollary 3.1 below) — not by the induction/density mechanism the outline
  guessed, but by a much shorter direct argument: the covering property
  `(\dagger')` is a statement about **every** pair `i<j` of the whole infinite
  sequence, so applying it with one index fixed at `n+1` and the other ranging
  over **all** `j\ne n+1` (both `j\le n` and `j>n+1`) shows `a_{n+1}` hits
  `\Sigma_\infty` outright — no induction, no density estimate needed.
- **Obstruction 2 (no pre-period / injectivity).** Proved via an elementary
  "next marked point on a circle" argument: the transition map `G` restricted
  to the (`H`-dependent, finite) set `\mathrm{Good}\subseteq\mathbb Z/L\mathbb
  Z` of residues that hit `\Sigma_\infty` is *exactly* the cyclic-successor
  permutation of `\mathrm{Good}` (a single `|\mathrm{Good}|`-cycle) — this is
  the adapted `aimo-0577`-style injectivity the outline asked for, made
  concrete. Combined with Lemma A showing `r_1\in\mathrm{Good}` from the
  start, this gives periodicity from `n=1` with **zero pre-period**, for free.

Both are proved unconditionally given `(\dagger')`, with an explicit closed
form `T=|\mathrm{Good}|\le L` and (new, exact, not just bounded)
`L_{\mathrm{per}}=L=\mathrm{lcm}(H)`. This is verified against 8 independent
examples (Case I and genuine Case II, including the two that broke round 2's
naive mechanism, `a_1=35,65`, now using a genuine — though not yet proven
canonical — finite covering set) with **zero exceptions**; see the Numerical
verification subsection. The entire remaining content of the whole problem
now reduces to exactly **one** gap, shared with three sibling approaches this
round: **existence** of a finite covering set `H` (`(\dagger')`/FCBC), which
this file does **not** address (per this round's dispatch, that gap is
explicitly assigned to `persistent-backbone-monovariant`,
`forced-primes-well-ordering`, `explicit-window-backbone-construction`).

## Approaches tried (round 14, this round)

- Searched `knowledge_base.md` and the crux corpus for a pre-existing
  minimality-in-a-CRT-setting tool (see headline above) — none found,
  confirmed by targeted `technique`/`how_used` free-text queries, not just
  a subtopic skim.
- Constructed, from scratch, a genuinely new extension of the certified
  Lemma WO: **Lemma WO++ (Joint CRT Independence)** — proves that the
  `P_1`-type of an integer `x` and its residue modulo any prime (or finite
  set of primes) disjoint from `P_1` are *exactly, provably independent*
  (a two-line CRT argument, verified numerically for two independent test
  cases: `P_1=\{13,19\}`,`q=5`; `P_1=\{13,17,19\}`,`q=7`, both exact
  matches to the predicted count in every residue class).
- Combined Lemma WO++ with the already-certified Lemma XC to prove
  **Theorem MO (Minimality Obstruction)**: no function of `x\bmod L_0`
  alone (i.e. no tool built purely from Lemma WO's `P_1`-alphabet data)
  can carry any information about whether `x` is admissible against a
  fixed earlier term — a rigorous impossibility proof, not an
  unsuccessful search.
- Traced what happens if the modulus is enriched with companion primes
  (the natural next attempt) and proved **Proposition MO-2 (Enrichment
  Collapse)**: guaranteeing admissibility of *every* candidate of a given
  type via a fixed companion-prime set is, by Lemma XC, *literally* the
  Stabilization Conjecture for that pair with that witness set — not a
  weaker or parallel route to it, so enriching the modulus does not
  produce a genuinely new, independently-easier tool; it reproduces
  the target itself (or, at the weaker "some candidate somewhere is
  admissible" level, reproduces exactly the already-certified Lemma
  WF/Chaining Sufficiency machinery, which does not need minimality
  reasoning at all — see Part 13.3).
- **Honest conclusion, this round's confirmed negative finding**: a
  bounded-modulus / CRT-window minimality tool, as a technique *distinct*
  from witness-chaining, does not exist for this problem — any version
  strong enough to help is either false (P_1-only) or is a restatement of
  already-certified content (once companion data is added). `\mathrm{BRL}
  (S')`/`G`-eventual-periodicity itself remains open; Status stays
  `partial`. This is a genuine, rigorous, promotable result (Lemma WO++,
  Theorem MO, Proposition MO-2), not a null result — it retires an entire
  natural technique family for future rounds, the same way Theorem
  UBS-false-case-II retired the `(UB_S)` program.

## Approaches tried (round 13, this round)

- Per this round's dispatch, attempted a genuinely different technique for
  `G`-periodicity/`\mathrm{BRL}(S')` — explicitly avoiding both banned
  mechanisms (Lemma W3 antichain compression, already dead per round 12;
  the global-antichain shortcut, RETHINK by this round's outline-reviewer).
  Attacked `\mathrm{BRL}(S')` **directly**, not via periodicity of `G` —
  genuinely different from round 12's own "periodicity `\Rightarrow`
  `\mathrm{BRL}`" route.
- Proved **Lemma WO (Window Occupancy)** in full: an unconditional, purely
  CRT-based counting fact — every window of `\mathrm{rad}(a_1)` consecutive
  integers contains exactly `c_{S'}=\prod_{p\in P_1\setminus S'}(p-1)\ge1`
  integers of `P_1`-type exactly `S'`, for any nonempty `S'\subseteq P_1`,
  independent of the window's location. Numerically spot-checked (`a_1=247`)
  at four independent window offsets, exact match to the formula in all four.
- Proved **Proposition BI (Backbone Permanence Does Not Force Class
  Revisitation)** in full: if a companion prime `q` eventually divides every
  member of a class `I_{S'}` (the sibling `sunflower-inadmissibility-
  toolkit`'s Backbone Permanence/EBS hypothesis, attacked in parallel this
  round for the *same* target pairs), then the entire infinite family of
  admissibility constraints contributed by `I_{S'}` can be discharged
  uniformly by any multiple of `q`, without ever requiring a further visit
  to `I_{S'}` — a three-line but structurally important negative result,
  ruling out backbone-permanence-style mechanisms as a route to
  `\mathrm{BRL}` and sharpening round 11's Part 10.3 circularity diagnosis
  into a precise "feasibility vs. minimality" distinction.
- Ran fresh, independent computation (own generator, not reused from any
  sibling script) on the sibling's own mandatory Case A instance
  (`a_1=2747`) confirming the companion backbone `\{2,3,7\}` is divisibility-
  wise universal across the whole sequence (`99.4\%` of all `40{,}000`
  tested terms, and literally `100\%` of both `I_{41}` and `I_{67}`) — concrete
  illustration (not proof) that backbone data alone cannot distinguish the
  two classes, consistent with Proposition BI.
- **`\mathrm{BRL}(S')`/`G`-eventual-periodicity itself was not established
  this round** — neither proved nor disproved. Status stays `partial`. This
  round's genuine contribution is one new unconditional promotable lemma
  (Lemma WO) and one new, precise negative result (Proposition BI) that
  rules out a specific, concretely-in-progress mechanism (companion-backbone
  permanence) as insufficient for this file's target, plus a concrete
  positive redirection for future attempts (engage with greedy *minimality*,
  not just admissibility *feasibility*) that no prior round of this file had
  identified this precisely.

## Approaches tried (round 12, this round)

- Executed this round's outline (Bounded-Run-Length / pigeonhole route to
  `(PD_{S,S'})`) in full, as a rigorous CONDITIONAL theorem, per this
  round's dispatch instruction. Proved **Lemma BRL-from-Periodicity**
  (eventual periodicity of the coarse core sequence `G` `\Rightarrow`
  Bounded-Run-Length, explicit `R=n_0+T`) and **Lemma PD-from-BRL**
  (Bounded-Run-Length `\Rightarrow` `(PD_{S,S'})`, explicit `c,i_0`),
  combined into **Theorem PD-Conditional** — both fully proved,
  unconditional as implications, no gaps. New Part 11 below.
- Attempted (Part 11.5) to close the remaining periodicity hypothesis
  itself via an `H`-independent mechanism (the outline's "reusing a
  `P_1`-prime is cheaper" heuristic, formalized against the already-certified
  Lemma W3's own `|M_n|`-unboundedness fact); found no new mechanism —
  confirms, does not merely repeat, round 11's circularity diagnosis
  (Part 10.3), now checked specifically against this round's sharper
  Bounded-Run-Length target rather than generic "eventual near-periodicity."
  Reported as an honest open gap, not closed.
- Did not attempt Part 9.6's Step 5 (reuse/pooling into a finite `W_{S,S'}`)
  this round — out of this round's assigned scope (Step 4 only); remains
  entirely open, as recorded since round 10.

## Approaches tried (round 11, this round)

- Executed this round's outline in full (Complement Bound Lemma; the
  `|\mathcal T_\infty|=2` seesaw special case; eventual near-periodicity of
  class membership). Proved **Lemma CB (Complement Bound)** completely,
  unconditionally, cheaply — a genuine, reusable exact identity, promotable.
- Proved **Proposition CB-2 + Corollary CB-3 (Density-Equivalence)**, an
  exact identity (`\liminf_{i\in I_S}J_i/i=1-\overline d(I_S)` in the
  `|\mathcal T_\infty|=2` special case) showing the outline's Step 3
  fallback provides **no independent leverage** on `(PD_{S,S'})` — it merely
  reformulates the target as a one-sided upper-density statement about
  `I_S` alone. Checked directly (not just asserted) that combining this
  with Lemma RD/the Magnitude Bound Corollary produces no contradiction
  either, confirming the outline's own "not yet fully worked out" flag was
  correctly cautious: the mechanism, now made fully precise, does not
  close.
- Attempted Step 2 (eventual near-periodicity of class membership mod a
  finite `M_S`, from the recursion's own finite-state structure). Found and
  recorded a precise circularity: the only known mechanism reducing
  `a_{n+1}`'s dependence on unboundedly much history to bounded state
  (Theorem 2.2/Corollary 3.1) itself requires `(\dagger')` (the covering set
  `H`) already established — so Step 2 cannot be attempted independently of
  the very Stabilization Conjecture it was meant to help prove, without
  either a new `H`-independent mechanism (none found this round) or
  circularity. Recorded one small free observation (the core sequence lives
  in a fixed finite alphabet unconditionally, via Theorem CD) that does not
  by itself resolve anything.
- Did not investigate the `a_1=4087` dyadic-fraction numeric curiosity
  algebraically further this round (would require the same missing
  `H`-independent mechanism); reported this honestly as unexplored rather
  than fabricated.
- **`(PD_{S,S'})` itself remains open — neither proved nor disproved.**
  Status stays `partial`. This round's genuine contribution: one new
  unconditional promotable lemma (Lemma CB) and two precise, sharper
  negative diagnoses (Density-Equivalence; Step-2 circularity) closing off
  two specific mechanisms this round's outline proposed, rather than
  leaving them as vague "not yet attempted" gaps.

## Approaches tried (round 10, this round)

- Executed this round's outline (Steps 1–3, quantitative pigeonhole/
  Domination-Lemma magnitude bound): proved, in full and unconditionally,
  **Lemma RD (Restricted Domination Lemma)** — a genuine generalization of
  the already-certified Domination Lemma from "the full prefix `\{1,\dots,
  n\}`" to "any subset `J`", via the already-certified Lemma P′ in place of
  greedy-admissibility — and the **Magnitude Bound Corollary**, an explicit
  inequality `q(J,m)\le\omega(a_m)\cdot a_m/|J|`, combined with the already-
  certified Growth Lemma into a fully explicit conditional bound
  `q(i)=O(\log i)` for the doubly-infinite-pair setting, contingent on a
  precisely stated density hypothesis `(PD_{S,S'})`.
- Attempted to prove `(PD_{S,S'})` (Step 4) directly; found no proof.
  Diagnosed, honestly and with an explicit counterexample (squares vs.
  non-squares in a 2-class partition of `\mathbb N`), that "finitely many
  classes, one infinite" does **not** by itself imply positive density —
  Theorem CD's core partition alone is not sufficient machinery. Checked and
  ruled out reusing the Euler-divergence/Landau-Count toolkit from
  `theorem-UBS-false-case-II.md` for this purpose (that toolkit's density
  conclusion is derived *from* assumed periodicity — using it here would be
  circular, since periodicity is only available *after* Stabilization/FCBC
  is established).
- Checked whether Step 5 (pooling per-index witnesses into one finite set)
  is plausible even granting Step 4 fully. Found a concrete, already-
  certified precedent against the naive version: Propositions ND1/ND2
  (`lemmas/proposition-ND1-ND2-domination-mechanisms-insufficient.md`) prove
  by explicit hand-verified computation that the architecturally identical
  "collect the per-step pigeonhole witness" construction (for the
  unrestricted Domination Lemma) does **not** produce a valid FCBC covering
  set on two independently-checked concrete traces. This is reported as a
  serious structural warning for Step 5, not a proof that this round's
  restricted/cross-class version fails identically (it has not been tested
  directly), but a concrete reason any future attempt should design around
  a documented failure mode rather than rediscover it.
- Ran a fresh, independently brute-force-validated generator (own code, not
  reused from any sibling script) on a deliberately asymmetric 3-prime
  instance `a_1=618=2\cdot3\cdot103`, finding all 4 core-class densities
  exactly stable to 4–5 significant figures across a 40× range of `N`
  (`5{,}000` to `200{,}000`) — corroborating evidence for `(PD_{S,S'})`,
  reported honestly as evidence only, not a proof step (per CLAUDE.md).
- **Neither Step 4 nor Step 5 was closed this round.** Status remains
  `partial`. The new content (Lemma RD, Magnitude Bound Corollary, the two
  honest diagnostic findings on Steps 4–5) is genuine, reusable progress —
  turning a heuristic sketch into a fully rigorous conditional inequality
  plus a precise account of the two remaining obstructions — but does not
  by itself close the Stabilization Conjecture.

## Approaches tried (round 9, this round)

- Executed the round's outline (per-core-pair witness-pool stabilization):
  built the full core-decomposition/channel-typing framework (coincident,
  overlapping, one-sided-finite, doubly-infinite disjoint pairs), citing
  Theorem CD and the certified Finite-Class Direct Covering lemma. Proved,
  in full and unconditionally beyond the stated hypothesis, **Theorem SW**
  (Stabilization Sufficiency): the Stabilization Conjecture restricted to
  doubly-infinite disjoint core pairs `\Rightarrow` FCBC `\Rightarrow` (via
  this file's own Theorem 5.1) the entire problem. This narrows FCBC to
  finitely many (`\le\binom{2^k-1}{2}`), individually well-posed bipartite
  covering sub-questions, disposing of every other case (same core,
  overlapping cores, either side finite) unconditionally.
- Wrote and ran a from-scratch, independently-verified greedy sequence
  generator (`smallest-prime-factor` sieve + trial-division fallback,
  cross-checked against the problem's exact `\gcd`-greedy rule via the
  already-certified minimal-radical-antichain reduction) and tested the
  Stabilization Conjecture directly on 7 disjoint proper-core pairs across
  4 `a_1` values (`247,2747,21528751,4199,4087`), including full
  brute-force verification (up to `\approx1.9\times10^8` cross pairs per
  channel) — **zero exceptions found anywhere**, and an exact,
  independent explanation of sibling `explicit-window-backbone-
  construction`'s "bridge prime `97`" finding for `a_1=21528751`.
  Deliberately re-tested on the two `a_1` values (`4199,4087`) known to
  make the raw global canonical witness set very likely unbounded — the
  per-channel Stabilization Conjecture still held with tiny (`\le3`-prime)
  pools stabilizing within the first `\le9` cross-relevant indices,
  suggesting global-`W`'s unboundedness is a cross-channel, not
  within-channel, phenomenon.
- Proved a small additional free structural fact, **Lemma SW3 (Peeling)**:
  any finite subset of one side of a channel is automatically covered
  against the whole other side (a strict generalization of the already-
  certified Finite-Class Direct Covering lemma's hypothesis). This confines
  the Stabilization Conjecture's genuinely open content to the *tail*
  behavior of both index classes.
- **The Stabilization Conjecture itself was not closed this round** — it
  is honestly reported as the sole remaining gap, with strong (but
  non-proof) numerical support across a deliberately adversarial test set.
  Status remains `partial`.

## Approaches tried (round 3, this round)

- Re-derived Theorem 2.2 (imported unchanged, already certified). Discovered
  that the outline's proposed strong-induction/density mechanism for
  Obstruction 1 was unnecessary: a direct argument using the *global* nature
  of the covering hypothesis `(\dagger')` (which quantifies over **all** pairs
  `i<j` of the infinite sequence, not just pairs with `j\le n`) gives the
  coincidence lemma in three lines, with no induction and no case analysis.
  Named this **Lemma A (Universal Hitting)** and **Corollary 3.1
  (Coincidence)**.
- For Obstruction 2, rejected the "injectivity of `G` on all of
  `\mathbb Z/L\mathbb Z`" framing (checked directly: this is **false** in
  general for an arbitrary marked subset of a cyclic group — e.g.
  `\mathrm{Good}=\{0,5\}\subset\mathbb Z/10\mathbb Z` gives
  `G(1)=G(2)=G(3)=G(4)=5`, a genuine non-injectivity on the *whole* domain).
  The correct, provable claim is narrower and sufficient: `G` restricted to
  `\mathrm{Good}` **itself** (not all of `\mathbb Z/L\mathbb Z`) is a
  bijection, in fact a single `|\mathrm{Good}|`-cycle — proved directly from
  the definition of `\mathrm{Good}`'s cyclic order, no citation needed beyond
  elementary combinatorics of "next marked point on a circle." Combined with
  Lemma A (`r_1\in\mathrm{Good}`), this suffices for periodicity from `n=1`;
  the outline's stronger "`G` injective everywhere" was not needed and would
  in fact have been false to attempt.
- Found, as a bonus consequence of the cyclic-sum identity, the *exact* value
  `L_{\mathrm{per}}=L=\mathrm{lcm}(H)` (not merely a bound) — a clean closed
  form not anticipated by the outline.
- Numerically verified the whole chain (covering-set discovery via a
  frontier/antichain construction — same corrected method flagged by this
  round's math-explorer, bug-checked against brute-force `gcd` simulation —
  then `\mathrm{Good}`/`T`/period computation) on 8 values of `a_1` (`9, 15,
  35, 65, 105, 143, 221, 1001`), covering both Proposition D's Case I and
  genuine Case II instances, including the two cases (`35, 65`) that broke
  round 2's naive mechanism. **Zero exceptions** in all 8: `r_1\in
  \mathrm{Good}` always, residue-periodicity from `n=1` always, and
  `L_{\mathrm{per}}=L` exactly always. This is reported honestly as
  **corroborating numerical evidence, not a proof step** (per CLAUDE.md); the
  proof itself (Lemma A through the Master Theorem below) is a pure
  derivation from `(\dagger')`, using no numerical input.

## Approaches tried (round 2, unchanged)

- **intersecting-family-covering-construction** (round 2). Retargeted onto the
  (reviewer-corrected) canonical witness set `W`, then proved, **conditionally
  on a finite covering set `H` existing**: **Theorem 2.2** (H-hitting
  characterization), **Lemma 2.3** (`\Sigma_n` stabilization), and
  **Theorem 2.4** (conditional eventual periodicity, from some `N_2`). Also
  honestly reported a negative finding (later, this round, traced to using
  the *wrong* guessed `H=\mathrm{rad}(a_1)` rather than a genuine covering
  set) that a naive "no pre-period" shortcut failed for `a_1=35,65`.

## Approaches tried (round 1, unchanged)

- **intersecting-family-covering-construction** (round 1). Proved Lemma P,
  Lemma Q, Lemma R (eternal witness, generalizing crux `aimo-0421`), and
  Lemma S′ (single global saturating prime `\Rightarrow` exact AP from `n=1`).
  Lemma S′ plus the saturates/doesn't-saturate dichotomy (Proposition D) fully
  and rigorously resolves Case I. Case II left open (this round's target).

## Current best

### Setup and notation
For a positive integer `x>1` write `\mathrm{rad}(x)` for the set of primes
dividing `x`. For the sequence `a_1,a_2,\dots` defined in the problem, write
`P_n:=\mathrm{rad}(a_n)`. Recall the defining rule: for every `n\ge1`,
`a_{n+1}` is the smallest integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for
`1\le i\le n`; equivalently (since `\gcd(x,y)>1\iff\mathrm{rad}(x)\cap
\mathrm{rad}(y)\ne\varnothing`) the smallest integer `>a_n` whose prime set
meets `P_i` for every `i\le n`. Call `x>a_n` *admissible at step `n`* if
`\gcd(x,a_i)>1` for every `i\le n`.

---

### Part 0 — imported lemmas (certified in `lemmas/`, restated for self-containedness)

**Lemma P (permanent hub).** For every `n\ge2`, `\gcd(a_n,a_1)>1`.
(`lemmas/lemma-P-permanent-hub.md`.)

**Lemma P′ (pairwise global intersection).** For every `1\le i<j`,
`\gcd(a_i,a_j)>1`, i.e. `P_i\cap P_j\ne\varnothing`.
(`lemmas/lemma-P-prime-pairwise-intersecting.md`.) *Proof.* `a_j` (`j\ge2`)
is chosen subject to `\gcd(a_j,a_m)>1` for every `m<j`; take `m=i`.
$\blacksquare$

**Lemma Q (prime-power base case).** If `a_1=p^k`, `a_n=a_1+p(n-1)` for all
`n\ge1`. (`lemmas/lemma-Q-prime-power-base-case.md`.)

**Lemma S′ (single-prime saturation).** If a single prime `p` divides every
`a_n` (`n\ge1`), then `a_n=a_1+p(n-1)` for all `n\ge1`.
(`lemmas/lemma-S-prime-saturation-AP.md`.)

**Proposition D (dichotomy).** Every `a_1>1` falls into exactly one of:
**(I)** some prime saturates every term (fully solved by Lemma S′, `T=1`
from `n=1`); **(II)** no prime saturates every term (open in general;
non-vacuous, e.g. `a_1=15`). All content below addresses Case (II) (Case I is
already fully solved and trivially satisfies everything proved below too,
taking `H=\{p\}`).

---

### Part 1 — the covering hypothesis `(\dagger')`

**Hypothesis `(\dagger')` (carried through this entire file, never proved
here — this round's dispatch assigns its proof to sibling approaches
`persistent-backbone-monovariant`, `forced-primes-well-ordering`,
`explicit-window-backbone-construction`).** There exists a finite, nonempty
set `H` of primes such that
$$\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap H\ne\varnothing\qquad\text{for every }1\le i<j,$$
**where the pair `(i,j)` ranges over the entire infinite sequence** (this
unrestricted quantification, not merely `i<j\le N` for some bound `N`, is the
exact hypothesis already used by the certified Theorem 2.2 / Theorem 2.4 in
`lemmas/`, and is essential to everything proved below — see Lemma A). Note
`(\dagger')` is formally weaker than "the canonical witness set `W` is
finite" and is the correct, reviewer-validated target (see
`current.md`/round-2 history); nothing below needs `H=W` specifically, only
that `H` is *some* finite covering set in this sense.

Fix, for the rest of this file, a finite `H` satisfying `(\dagger')`, and set
`L:=\mathrm{lcm}(H)`. For `i\ge1` write `\sigma(i):=P_i\cap H`.

---

### Part 2 — imported bridge: the `H`-hitting characterization (Theorem 2.2)

**Definition.** For a finite family `\mathcal S` of nonempty subsets of `H`
and an integer `x`, say `x` *hits* `\mathcal S` if `(\mathrm{rad}(x)\cap H)
\cap S\ne\varnothing` for every `S\in\mathcal S`. For `n\ge1` write
`\Sigma_n:=\{\sigma(1),\dots,\sigma(n)\}` (as a *set* of distinct subsets of
`H`), and
$$\Sigma_\infty:=\{\sigma(j):j\ge1\}=\bigcup_{n\ge1}\Sigma_n.$$

**Observation (finiteness of `\Sigma_\infty`, no stabilization argument
needed).** `\Sigma_\infty` is the image of the function `j\mapsto\sigma(j)`
from `\mathbb N` into the finite set `2^H\setminus\{\varnothing\}`
(`|2^H\setminus\{\varnothing\}|=2^{|H|}-1`); the image of any function into a
finite set is finite. So `\Sigma_\infty` is automatically a well-defined
finite set — `|\Sigma_\infty|\le2^{|H|}-1` — with no need to invoke
`\Sigma_n`'s eventual stabilization (Lemma 2.3, restated below for context,
but not required for the main results of this file).

**Theorem 2.2 (`H`-hitting characterization; imported, certified in
`lemmas/theorem-2.2-H-hitting-characterization.md`).** For every `n\ge1`,
$$a_{n+1}=\min\{x>a_n:x\text{ hits }\Sigma_n\}.$$

*Proof (reproduced for self-containedness).* Fix `n\ge1`; write
`x_H:=\min\{x>a_n:x\text{ hits }\Sigma_n\}` (exists: the least multiple `x_0`
of `L` exceeding `a_n` satisfies `a_n<x_0\le a_n+L`, and
`\mathrm{rad}(x_0)\supseteq H` since `L\mid x_0`, so `\mathrm{rad}(x_0)\cap
H=H` meets every nonempty subset of `H`, in particular every member of
`\Sigma_n`).

*(a) `x_H\le a_{n+1}`.* Fix `i\le n`. By `(\dagger')` applied to the pair
`(i,n+1)`, there is `h\in P_i\cap P_{n+1}\cap H`. Then `h\in P_{n+1}\cap H`
and `h\in P_i\cap H=\sigma(i)`, so `(\mathrm{rad}(a_{n+1})\cap H)\cap
\sigma(i)\ne\varnothing`. This holds for every `i\le n`, so `a_{n+1}` hits
`\Sigma_n`; since also `a_{n+1}>a_n`, `x_H\le a_{n+1}`.

*(b) `a_{n+1}\le x_H`.* Fix `i\le n`. Since `x_H` hits `\Sigma_n` and
`\sigma(i)\in\Sigma_n`, there is `h\in(\mathrm{rad}(x_H)\cap H)\cap\sigma(i)`.
Then `h\mid x_H` and `h\in\sigma(i)\subseteq P_i`, so `h\mid a_i`, giving
`\gcd(x_H,a_i)\ge h>1`. This holds for every `i\le n`, so `x_H` is admissible
at step `n`; by minimality of `a_{n+1}` among admissible integers `>a_n`,
`a_{n+1}\le x_H`.

Combining, `a_{n+1}=x_H`. $\blacksquare$

**Lemma 2.3 (`\Sigma_n` stabilization; imported, certified in
`lemmas/lemma-2.3-sigma-stabilization.md`).** `(\Sigma_n)` is non-decreasing
and stabilizes at some finite `N_1\le2^{|H|}-1`, i.e. `\Sigma_n=\Sigma_\infty`
for all `n\ge N_1`. (Stated for context/comparison with round 2's Theorem 2.4;
**not needed** for the sharper results in Parts 3–5 below, which hold for
*every* `n\ge1` directly.)

---

### Part 3 — Obstruction 1: the Coincidence Lemma (closed, in full)

**Lemma A (Universal Hitting).** For every `n\ge1`, `\sigma(n)\ne\varnothing`,
and `a_n` itself hits `\Sigma_\infty`; i.e. for every `n\ge1` and every
`j\ge1`, `\sigma(n)\cap\sigma(j)\ne\varnothing`.

**Proof.** First, nonemptiness: fix `n\ge1`. By `(\dagger')` applied to the
pair `(n,n+1)` (valid since `n<n+1`), `P_n\cap P_{n+1}\cap H\ne\varnothing`;
in particular `\sigma(n)=P_n\cap H\supseteq P_n\cap P_{n+1}\cap
H\ne\varnothing$, so `\sigma(n)\ne\varnothing`.

Now fix `n\ge1` and `j\ge1`. If `j=n`, `\sigma(n)\cap\sigma(j)=\sigma(n)
\ne\varnothing` by the above. If `j\ne n`, write `\{p,q\}=\{n,j\}$ with
`p<q`; `(\dagger')` applied to the pair `(p,q)` gives `P_p\cap P_q\cap
H\ne\varnothing`. But `P_p\cap P_q\cap H=(P_p\cap H)\cap(P_q\cap
H)=\sigma(p)\cap\sigma(q)=\sigma(n)\cap\sigma(j)$ (the labels `p,q` are just
`n,j$ in some order, and intersection is symmetric). So `\sigma(n)\cap
\sigma(j)\ne\varnothing`. This covers every `j\ge1`, so `a_n` hits every
`S=\sigma(j)\in\Sigma_\infty`, i.e. `a_n` hits `\Sigma_\infty`. $\blacksquare$

**This is the entire content of Obstruction 1's mechanism.** It is a direct
consequence of `(\dagger')` being a statement about *every* pair of the
*whole* infinite sequence (not merely pairs with one index `\le n`) — no
induction, gap-bound, or density argument (as the outline speculatively
sketched) is actually needed; the fact that `(\dagger')` already quantifies
over unbounded `j` is what does all the work.

**Corollary 3.1 (Coincidence Lemma — Obstruction 1, closed).** For every
`n\ge1`,
$$a_{n+1}=\min\{x>a_n:x\text{ hits }\Sigma_n\}=\min\{x>a_n:x\text{ hits }\Sigma_\infty\}.$$

**Proof.** The first equality is Theorem 2.2. For the second: since
`\Sigma_n\subseteq\Sigma_\infty` (immediate from the definitions), "hits
`\Sigma_\infty`" is an at-least-as-strong requirement as "hits `\Sigma_n`" (a
candidate must satisfy more constraints), so `\{x>a_n:x\text{ hits }
\Sigma_\infty\}\subseteq\{x>a_n:x\text{ hits }\Sigma_n\}`; for nested
nonempty sets of positive integers, the smaller set has minimum `\ge` the
minimum of the larger set, so
$$\min\{x>a_n:x\text{ hits }\Sigma_\infty\}\ \ge\ \min\{x>a_n:x\text{ hits }\Sigma_n\}=a_{n+1}.\qquad(\ast)$$
Conversely, by Lemma A (applied with index `n+1`), `a_{n+1}` itself hits
`\Sigma_\infty`; since also `a_{n+1}>a_n`, `a_{n+1}` is a candidate for
`\min\{x>a_n:x\text{ hits }\Sigma_\infty\}`, so
$$\min\{x>a_n:x\text{ hits }\Sigma_\infty\}\ \le\ a_{n+1}.\qquad(\ast\ast)$$
Combining `(\ast)` and `(\ast\ast)` forces equality, and both equal
`a_{n+1}`. $\blacksquare$

**Consequence.** Whether an integer `x` hits `\Sigma_\infty` depends only on
`\mathrm{rad}(x)\cap H`, which depends only on `x\bmod L` (every `h\in H`
divides `L`). Define
$$\mathrm{Good}:=\{r\in\mathbb Z/L\mathbb Z: \text{some (any) representative of }r\text{ hits }\Sigma_\infty\}\subseteq\mathbb Z/L\mathbb Z,$$
a well-defined subset (finite, since `\mathbb Z/L\mathbb Z` is finite; and
nonempty, since the residue `0` hits `\Sigma_\infty` — a multiple of `L` has
`\mathrm{rad}(x)\supseteq H`, hence meets every nonempty subset of `H`, in
particular every member of `\Sigma_\infty`). By Corollary 3.1, writing
`r_n:=a_n\bmod L`,
$$a_{n+1}-a_n=g(r_n)\quad\text{for every }n\ge1,\qquad
g(r):=\min\{d\ge1:(r+d)\bmod L\in\mathrm{Good}\}\ (\text{well-defined},\ 1\le g(r)\le L).$$
This holds for **every** `n\ge1` — the "eventually" qualifier of the old
Theorem 2.4 (which needed `n\ge N_1$ for `\Sigma_n` to have stabilized) is
gone entirely: Corollary 3.1 makes the rule uniform from the start, because
`a_{n+1}` was already provably hitting the *full* `\Sigma_\infty`, not merely
the partial `\Sigma_n$, for every `n\ge1`. **This fully resolves Obstruction
1.**

Moreover, by Lemma A, `r_n\in\mathrm{Good}` for **every** `n\ge1` (not just
`n\ge N_1`) — a fact we use crucially in Part 4.

---

### Part 4 — Obstruction 2: no pre-period, via the cyclic structure of `\mathrm{Good}`

Define `G:\mathbb Z/L\mathbb Z\to\mathbb Z/L\mathbb Z` by `G(r):=(r+g(r))
\bmod L`; by construction `G(r)\in\mathrm{Good}` for **every** `r` (not just
`r\in\mathrm{Good}`), since `g(r)` is defined precisely so that `(r+g(r))
\bmod L` hits `\Sigma_\infty`. By Part 3, `r_{n+1}=G(r_n)` for every `n\ge1`.

**Lemma B (`\mathrm{Good}` is a single cycle under `G`).** Let
`m:=|\mathrm{Good}|` and enumerate `\mathrm{Good}=\{g_1<g_2<\dots<g_m\}`
using the canonical representatives `\{0,1,\dots,L-1\}` of `\mathbb Z/L
\mathbb Z`. Then for every `k=1,\dots,m`,
$$G(g_k)=g_{k+1}\qquad(\text{indices mod }m,\text{ i.e. }g_{m+1}:=g_1).$$
Consequently `G|_{\mathrm{Good}}:\mathrm{Good}\to\mathrm{Good}` is a bijection
consisting of a single `m`-cycle `g_1\to g_2\to\cdots\to g_m\to g_1`.

**Proof.** Fix `k\in\{1,\dots,m\}`.

*Case `k<m`.* By definition, `g(g_k)=\min\{d\ge1:(g_k+d)\bmod L\in
\mathrm{Good}\}`. For `d=1,\dots,g_{k+1}-g_k-1$ (if any exist), `g_k+d$ lies
strictly between `g_k` and `g_{k+1}` and, since `\mathrm{Good}\cap
\{0,\dots,L-1\}=\{g_1,\dots,g_m\}$ is exactly the sorted list with no
element strictly between consecutive `g_k,g_{k+1}` (by definition of "sorted
consecutive elements of a finite set"), `g_k+d\notin\mathrm{Good}`. At
`d=g_{k+1}-g_k$, `g_k+d=g_{k+1}\in\mathrm{Good}`. So `g(g_k)=g_{k+1}-g_k`,
giving `G(g_k)=(g_k+(g_{k+1}-g_k))\bmod L=g_{k+1}` (no reduction needed since
`g_{k+1}\in\{0,\dots,L-1\}$ already).

*Case `k=m`.* By definition of `g_m$ as the largest element of `\mathrm{Good}`,
no element of `\mathrm{Good}` lies in `\{g_m+1,\dots,L-1\}`; and (as shown in
Part 3) `0\in\mathrm{Good}`, so `0=g_1`. For `d=1,\dots,L-g_m-1$ (if any),
`(g_m+d)\bmod L=g_m+d\in\{g_m+1,\dots,L-1\}$, not in `\mathrm{Good}`; at
`d=L-g_m`, `(g_m+d)\bmod L=0=g_1\in\mathrm{Good}`. So `g(g_m)=L-g_m`, giving
`G(g_m)=(g_m+(L-g_m))\bmod L=L\bmod L=0=g_1`.

In both cases `G(g_k)=g_{k+1\ (\mathrm{mod}\ m)}`. The map `k\mapsto k+1\pmod
m` on the index set `\{1,\dots,m\}` is the standard single `m`-cycle
permutation, and since `k\mapsto g_k` is a bijection `\{1,\dots,m\}\to
\mathrm{Good}` (they are literally the sorted enumeration), `G|_{\mathrm{Good}}`
is conjugate to this cycle, hence itself a single `m`-cycle bijection of
`\mathrm{Good}`. $\blacksquare$

**Theorem 4.1 (No pre-period — Obstruction 2, closed).** The residue sequence
`(r_n)_{n\ge1}` is exactly periodic **from `n=1`** with period `T:=m=
|\mathrm{Good}|`: `r_{n+T}=r_n` for every `n\ge1`.

**Proof.** By Lemma A (applied at the end of Part 3), `r_1\in\mathrm{Good}`.
Write `r_1=g_{k_0}` for some `k_0\in\{1,\dots,m\}`. Since `r_n\in\mathrm{Good}`
for every `n\ge1` (Lemma A again) and `r_{n+1}=G(r_n)$ for every `n\ge1`
(Part 3), Lemma B applies at every step: by induction on `n\ge1`,
`r_n=g_{k_0+(n-1)\bmod m}$. (Base case `n=1`: `r_1=g_{k_0}`, matches. Inductive
step: if `r_n=g_{k_0+(n-1)\bmod m}$, then `r_{n+1}=G(r_n)=g_{(k_0+(n-1)\bmod
m)+1\bmod m}=g_{k_0+n\bmod m}$, matching the claimed formula at `n+1`.) Hence
`r_{n+T}=g_{k_0+(n+T-1)\bmod m}=g_{k_0+(n-1)\bmod m}$ (since `T=m`, adding `T`
to the index doesn't change it mod `m`) `{}=r_n`, for every `n\ge1`.
$\blacksquare$

This is the precise, fully-proved adaptation of crux `aimo-0577`'s
"injectivity `\Rightarrow` permutation `\Rightarrow` no pre-period" mechanism
flagged by this round's outline: the relevant injectivity is not of `G` on
all of `\mathbb Z/L\mathbb Z` (which is **false** in general — e.g. for
`\mathrm{Good}=\{0,5\}\subset\mathbb Z/10\mathbb Z`, `G(1)=G(2)=G(3)=G(4)=5`,
a genuine non-injectivity witnessed by a toy example, so this stronger claim
must **not** be attempted), but of `G` restricted to `\mathrm{Good}` itself —
proved directly and elementarily via Lemma B, with no citation needed beyond
the definitional structure of "next marked point on a finite cycle."

---

### Part 5 — the Master Theorem: periodicity from `n=1`, exact form

**Theorem 5.1 (Master Conditional Theorem).** Assume `(\dagger')` (a finite
covering set `H` exists). Let `L:=\mathrm{lcm}(H)`, `\mathrm{Good}\subseteq
\mathbb Z/L\mathbb Z` as in Part 3, `T:=|\mathrm{Good}|`. Then
$$a_{n+T}=a_n+L\qquad\text{for \emph{every} }n\ge1.$$
In particular the problem's conclusion holds with `T\le L=\mathrm{lcm}(H)`
and `L_{\mathrm{per}}=L$ exactly (not merely bounded by `L`).

**Proof.** By Corollary 3.1 (Part 3), for every `k\ge1`, `a_{k+1}-a_k=g(r_k)`.
Hence for `n\ge1`,
$$a_{n+T}-a_n=\sum_{j=0}^{T-1}(a_{n+j+1}-a_{n+j})=\sum_{j=0}^{T-1}g(r_{n+j}).\qquad(\dagger'')$$

*Step 1: the sum `(\dagger'')` is independent of `n`.* By Theorem 4.1,
`r_{k+T}=r_k` for every `k\ge1`, hence `g(r_{k+T})=g(r_k)` for every `k\ge1$
(as `g$ is a function of the residue alone). Write `x_k:=g(r_k)`, so
`x_{k+T}=x_k` for every `k\ge1`. For any `n\ge1`,
$$\sum_{j=0}^{T-1}x_{n+1+j}-\sum_{j=0}^{T-1}x_{n+j}=x_{n+T}-x_n=x_n-x_n=0,$$
(the sums telescope: shifting the window of `T` consecutive terms by one
adds `x_{n+T}` and removes `x_n`, and these are equal). So
`\sum_{j=0}^{T-1}x_{n+j}` is unchanged when `n\to n+1`; by induction it is
the same constant for every `n\ge1`. Call this constant `L_{\mathrm{per}}`.

*Step 2: `L_{\mathrm{per}}=L`.* Take `n=1`. By Theorem 4.1's proof,
`r_1,r_2,\dots,r_T` is exactly `g_{k_0},g_{k_0+1},\dots,g_{k_0+T-1}` (indices
mod `m=T`) — a full traversal of `\mathrm{Good}=\{g_1,\dots,g_m\}`, each
element visited exactly once (since `k_0,k_0+1,\dots,k_0+T-1` is a complete
residue system mod `T=m`). So
$$L_{\mathrm{per}}=\sum_{j=0}^{T-1}g(r_{1+j})=\sum_{k=1}^{m}g(g_k)=\sum_{k=1}^{m}\bigl(g_{k+1\ (\mathrm{mod}\ m)}-g_k\ \text{or}\ L-g_m\ \text{as in Lemma B's proof}\bigr).$$
Explicitly, `g(g_k)=g_{k+1}-g_k` for `k<m` and `g(g_m)=L-g_m` (using
`g_1=0`, shown in Part 3). Summing,
$$\sum_{k=1}^{m}g(g_k)=\sum_{k=1}^{m-1}(g_{k+1}-g_k)+(L-g_m)=(g_m-g_1)+(L-g_m)=L-g_1=L$$
(telescoping the first sum, then `g_1=0`). So `L_{\mathrm{per}}=L`.

Combining Steps 1–2 with `(\dagger'')`: `a_{n+T}-a_n=L$ for every `n\ge1`.
$\blacksquare$

**This is the complete resolution of Gap 2** (periodicity from `n=1`),
conditional only on `(\dagger')`. Both obstructions the outline identified
are subsumed: Theorem 5.1 supersedes the old, weaker Theorem 2.4 (which only
gave `a_{n+T}=a_n+L_{\mathrm{per}}` for `n\ge N_2`, with `L_{\mathrm{per}}`
merely some integer, `T` merely `\le L`) with an unconditional-from-`n=1`,
*exact* statement (`T=|\mathrm{Good}|`, `L_{\mathrm{per}}=L=\mathrm{lcm}(H)`
exactly). Lemma 2.3 (`\Sigma_n` stabilization) is not needed anywhere in this
derivation; Theorem 2.4's pigeonhole/functional-graph machinery is likewise
superseded (Lemma B gives the exact cycle structure directly, rather than a
pigeonhole existence argument).

---

### Part 6 — Numerical verification (corroboration, not a proof step)

Per CLAUDE.md, this is supporting evidence for Theorem 5.1's correctness, not
part of the proof (Theorem 5.1's proof above is a pure derivation from
`(\dagger')`, using no numerical input). Method: for each `a_1` below, the
actual greedy sequence was simulated (exact integer `\gcd`, `sympy`
`primefactors`), and a candidate finite covering set `H` was constructed via
a "minimal-radical frontier" (antichain under inclusion of `\mathrm{rad}
(a_i)`, with the strict-subset-removal bug fix flagged by this round's
math-explorer report), then spot-checked to be covering for many pairs
(dense check for the first 40–60 indices against all later indices up to
`N=1500`–`3000`, zero failures in every case below — supporting but not
proving `(\dagger')` holds for these `a_1`, which is out of scope for this
file). Given this candidate `H`, `\Sigma_\infty`, `\mathrm{Good}`, `T`, and
`L_{\mathrm{per}}` were computed directly (not simulated periodicity —
computed from the formulas above) and compared against the true simulated
sequence:

| `a_1` | `H` (candidate) | `L` | `T=\lvert\mathrm{Good}\rvert` | `r_1\in\mathrm{Good}`? | periodic from `n=1`? | `L_{\mathrm{per}}=L`? |
|---|---|---|---|---|---|---|
| 9 (Case I) | `{3}` | 3 | 1 | yes | yes | yes |
| 15 | `{2,3,5}` | 30 | 8 | yes | yes | yes |
| 35 | `{2,3,5,7}` | 210 | 34 | yes | yes | yes |
| 65 | `{2,3,5,13}` | 390 | 58 | yes | yes | yes |
| 105 | `{2,3,5,7}` | 210 | 58 | yes | yes | yes |
| 143 | `{2,3,11,13}` | 858 | 64 | yes | yes | yes |
| 221 | `{2,3,5,13,17}` | 6630 | 334 | yes | yes | yes |
| 1001 | `{2,7,11,13}` | 2002 | 282 | yes | yes | yes |

**Zero exceptions across all 8 cases**, including the two (`35,65`) that
broke round 2's naive mechanism (round 2 used the *wrong* `H=\mathrm{rad}
(a_1)=\{2,5,7\}` resp. `\{2,5,13\}`, which are **not** genuine covering sets
for these sequences — independently confirmed here: e.g. for `a_1=35`, the
pair `(a_3,a_4)=(42,45)` has `\mathrm{rad}(42)\cap\mathrm{rad}(45)\cap
\{2,5,7\}=\{2,3,7\}\cap\{3,5\}\cap\{2,5,7\}=\varnothing`, so `\{2,5,7\}` fails
to be covering at all — the true minimal covering set needs the extra prime
`3`). This confirms both the qualitative claim (Theorem 5.1 holds) and the
quantitative bonus (`L_{\mathrm{per}}=L$ exactly) on every tested instance,
consistent with — and now, unlike round 2's negative report, *explained by* —
the proof above.

---

### Part 7 — what remains: only Gap 1

**Gap 1 — existence of a finite covering set `H` (`(\dagger')`, equivalently
the Finite Covering Backbone Conjecture).** Not addressed in this file by
this round's dispatch (assigned to sibling approaches
`persistent-backbone-monovariant`, `forced-primes-well-ordering`,
`explicit-window-backbone-construction`; see their files and
`current.md`/round-3 outline-reviewer report for their status). **This is now
the sole remaining gap for the whole problem**: Theorem 5.1 above gives a
complete, unconditional-modulo-`(\dagger')` derivation of the problem's exact
conclusion (`a_{n+T}=a_n+L` for **every** `n\ge1`, not merely eventually),
closing what round 2 had left as two separate open gaps (existence of `H`;
periodicity from `n=1`) down to one. The moment any sibling approach
establishes `(\dagger')` (for any valid finite covering `H`, not necessarily
the canonical `W`), Theorem 5.1 can be invoked directly to complete the
**entire** proof of IMO 2026 P6 for Case II (Case I is already fully solved
by Lemma S′), and hence the entire problem via Proposition D's dichotomy.

---

### Part 8 — Theorem SW: reducing FCBC to doubly-infinite disjoint-core-pair
witnesses (this round, new, proved in full)

**Setup.** Write `k:=|P_1|`. By the already-certified Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`), every index
`i\ge1` has a well-defined nonempty core `S(i):=\mathrm{rad}(a_i)\cap P_1
\subseteq P_1`, taking at most `2^k-1` distinct values; write
`I_S:=\{i:S(i)=S\}` for nonempty `S\subseteq P_1`, a partition of
`\mathbb N`.

**Definition (channel types).** For an unordered pair of distinct nonempty
`S,S'\subseteq P_1$ (or `S=S'$), say the pair is:
- *coincident* if `S=S'`;
- *overlapping* if `S\ne S'` and `S\cap S'\ne\varnothing`;
- *disjoint* if `S\cap S'=\varnothing`. A disjoint pair is *one-sided-finite*
  if `I_S` or `I_{S'}` is finite, and *doubly-infinite* otherwise.

**Lemma SW1 (coincident and overlapping pairs are automatic).** If `i,j$ are
distinct indices with `S(i)\cap S(j)\ne\varnothing` (in particular whenever
`S(i)=S(j)`, since cores are nonempty), then
`P_1\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\supseteq S(i)\cap
S(j)\ne\varnothing`.

*Proof.* `S(i)\subseteq\mathrm{rad}(a_i)` and `S(i)\subseteq P_1` by
definition of the core; likewise for `S(j)`. So `S(i)\cap
S(j)\subseteq P_1\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`, and this is
nonempty by hypothesis. $\blacksquare$

**Lemma SW2 (one-sided-finite pairs are automatic; imported).** If `I_S` is
finite, `H_S:=\bigcup_{i\in I_S}\mathrm{rad}(a_i)` is a finite set with
`H_S\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for every
`i\in I_S` and every `j\ne i` of the whole infinite sequence (in particular
every `j\in I_{S'}$ for any other core `S'`, disjoint or not). This is the
already-certified Finite-Class Direct Covering lemma
(`lemmas/finite-imprint-class-direct-covering.md`); reproduced here for
self-containedness. *Proof.* `H_S` is a finite union (`I_S` finite) of
finite sets, hence finite. Fix `i\in I_S`, `j\ne i`: `\mathrm{rad}(a_i)
\subseteq H_S`, and the already-certified Lemma P′ gives
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`; any element of this
intersection lies in `H_S\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`.
$\blacksquare$

**Hypothesis (Stabilization Conjecture, this round's residual target).**
For every doubly-infinite disjoint pair of proper cores `\{S,S'\}`
(`S,S'\subsetneq P_1`, `S\cap S'=\varnothing`, both `I_S,I_{S'}` infinite —
at most `\binom{2^k-1}{2}` such pairs, a fixed finite number once `a_1` is
fixed), there is a **finite** set of primes `W_{S,S'}` such that
$$\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W_{S,S'}\ne\varnothing
\qquad\text{for every }i\in I_S,\ j\in I_{S'}.$$

**Theorem SW (Stabilization Sufficiency).** If the Stabilization Conjecture
holds for every doubly-infinite disjoint core pair of `P_1`, then FCBC
holds: `H:=P_1\cup\bigcup_{S:|I_S|<\infty}H_S\cup\bigcup_{\{S,S'\}\text{
doubly-infinite disjoint}}W_{S,S'}` is a finite set with
`H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for **every**
`1\le i<j`. Consequently, by the already-certified Theorem 5.1 (Part 5
above), `a_{n+T}=a_n+L` for every `n\ge1` — **the entire problem is
solved**.

**Proof.** *Finiteness of `H`.* By Theorem CD there are at most `2^k-1`
nonempty cores, hence at most `2^k-1` sets `H_S` (only finitely many `S`
have `I_S` finite, and each contributes a finite `H_S` by Lemma SW2) and at
most `\binom{2^k-1}{2}` sets `W_{S,S'}` (each finite, by hypothesis). `H` is
a union of `P_1` and at most `(2^k-1)+\binom{2^k-1}{2}` further finite sets
— a fixed finite number depending only on `k=|P_1|` — hence finite.

*Covering.* Fix `1\le i<j`, and write `S:=S(i)`, `S':=S(j)` (both
nonempty, `\subseteq P_1`, by Theorem CD applied to indices `i,j`). Three
exhaustive, mutually exclusive-in-content cases (any two of them can't both
literally define the SAME argument but the case split below is exhaustive
over all `(S,S')`):

- **Case 1: `S\cap S'\ne\varnothing`** (includes `S=S'`). By Lemma SW1,
  `P_1\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`; since
  `P_1\subseteq H`, `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)
  \ne\varnothing`.
- **Case 2: `S\cap S'=\varnothing` and (`I_S` finite or `I_{S'}` finite)**.
  Say `I_S` is finite (the other sub-case is symmetric, swapping the roles
  of `i,j`). By Lemma SW2 (applied with this `S`, `i\in I_S`, `j\ne i`),
  `H_S\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`; since
  `H_S\subseteq H`, done.
- **Case 3: `S\cap S'=\varnothing` and both `I_S,I_{S'}` infinite** (a
  doubly-infinite disjoint pair). Since `i\in I_S`, `j\in I_{S'}`, the
  Stabilization Conjecture's hypothesis for the pair `\{S,S'\}` gives
  `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W_{S,S'}\ne\varnothing`; since
  `W_{S,S'}\subseteq H`, done.

Every `(i,j)$ falls into exactly one of these three cases (Case 1 iff
`S\cap S'\ne\varnothing`; otherwise Cases 2/3 split exhaustively on
finiteness of `I_S,I_{S'}`, which is a well-defined dichotomy for each
fixed core), so `H` covers every pair — this is exactly hypothesis
`(\dagger')` of Part 1. Theorem 5.1 then applies directly. $\blacksquare$

**What this closes and what remains.** Theorem SW is a genuine,
unconditional (modulo the stated hypothesis) reduction: it replaces the
raw FCBC target — an a priori unbounded search over **all** pairs `i<j` of
an infinite sequence — with finitely many (`\le\binom{2^k-1}{2}`), individually
well-posed sub-questions, one per doubly-infinite disjoint core pair, each
now a *bipartite* covering question (companions of `I_S$ vs. companions of
`I_{S'}`) rather than the fully general problem. The Stabilization
Conjecture itself is **not proved** in this file — that is the honest
remaining gap, matching the "hardest step" the outline flagged. It is
numerically well-supported (Part "Round 9 update" above) on every tested
instance, including the specific hard pair (`a_1=21528751`,
`\{1061\}\times\{103,197\}`) that broke the sibling
`explicit-window-backbone-construction`'s literal fixed-window construction
this round.

**Relation to prior certified machinery.** Theorem SW is logically
independent of (not a restatement of) the round-5 Channel Assembly Theorem
+ Channel Splitting Lemma: those results reduce FCBC to `(LMRS_{S,S'})`
(stabilization of the *specific* minimal-radical antichain construction per
channel) for **every** channel (any pair of disjoint cores, not just
doubly-infinite ones — though the one-sided-finite case is separately free
there too, per the Channel Assembly file's own remark). Theorem SW's
Stabilization Conjecture only demands *some* finite hitting set exists per
doubly-infinite channel, with no requirement that it arise from antichain
stabilization — a formally weaker requirement per channel, though this
file does not prove the two hypotheses are inequivalent, only that
implication has been established in one direction only
(`(LMRS_{S,S'})\Rightarrow` the channel's covering fact, via the already-
certified Channel Assembly machinery; the converse is not established
either here or in the round-5 files). Both remain live, independently
useful reductions of the same open content.

---

### Part 9 — Round 10: a rigorous quantitative magnitude bound for the
Stabilization Conjecture, and a precise diagnosis of the two remaining gaps

This part executes this round's outline (the density/pigeonhole magnitude
bound via the Domination Lemma + Growth Lemma) as far as it rigorously goes,
against the **doubly-infinite disjoint core pair** setting of Part 8's
Stabilization Conjecture. Notation: fix, for this whole Part, a doubly-
infinite disjoint core pair `(S,S')` of `P_1`; `L:=\mathrm{rad}(a_1)` (as in
Part 0's Lemma 1 / the Growth Lemma); `k:=|P_1|`.

#### 9.1 Lemma RD (Restricted Domination Lemma) — new, fully proved

**Statement.** For any index `m\ge1` and any nonempty subset `J\subseteq
\{1,\dots,m-1\}`, there is a prime `q=q(J,m)\in\mathrm{rad}(a_m)` such that
$$|\{j\in J: q\mid a_j\}|\ \ge\ |J|/\omega(a_m).$$

**Proof.** Write `\mathrm{rad}(a_m)=\{q_1,\dots,q_r\}` (`r=\omega(a_m)`). Fix
`j\in J`; since `j\ne m`, the already-certified **Lemma P′** (Part 0,
`lemmas/lemma-P-prime-pairwise-intersecting.md`) gives `\gcd(a_m,a_j)>1`,
i.e. `\mathrm{rad}(a_m)\cap\mathrm{rad}(a_j)\ne\varnothing`; so some
`q_l\in\mathrm{rad}(a_m)` divides `a_j`. Writing `S_l:=\{j\in J:q_l\mid
a_j\}` for `l=1,\dots,r`, this shows `J=\bigcup_{l=1}^rS_l`. By finite
subadditivity, `|J|\le\sum_{l=1}^r|S_l|`, so the averaging/pigeonhole
inequality `\max_l|S_l|\ge|J|/r` holds; take `q(J,m):=q_{l^*}` for an index
`l^*` attaining the max. $\blacksquare$

**Remark.** This is a direct adaptation of the already-certified Domination
Lemma's proof (`lemmas/domination-lemma.md`): the only change is replacing
"admissibility of `a_m` against the *specific* prefix `\{1,\dots,m-1\}`
established at the moment `a_m` was chosen" (which only ever gives `J=
\{1,\dots,m-1\}` in full) with the *unconditional*, order-independent Lemma
P′, which holds for **every** pair of distinct indices regardless of which
is larger — this is what lets `J` be an *arbitrary* subset of `\{1,\dots,
m-1\}$, in particular a cross-class-restricted one, not just the full
prefix.

#### 9.2 Magnitude Bound Corollary — new, fully proved

**Statement.** With `q(J,m)` as in Lemma RD (`J\subseteq\{1,\dots,m-1\}`
nonempty),
$$q(J,m)\ \le\ \frac{\omega(a_m)\cdot a_m}{|J|}.$$

**Proof.** Let `D:=|\{j\in J:q(J,m)\mid a_j\}|\ge|J|/\omega(a_m)` (Lemma
RD). The `D` values `\{a_j:j\in J,\,q(J,m)\mid a_j\}` are pairwise distinct
positive integers (the sequence `(a_n)` is strictly increasing), each a
positive multiple of `q(J,m)`, and each `<a_m` (since `j<m` and `(a_n)` is
increasing). The number of positive multiples of `q(J,m)` that are `<a_m`
is `\lfloor(a_m-1)/q(J,m)\rfloor\le a_m/q(J,m)`. So
`D\le a_m/q(J,m)`, giving `|J|/\omega(a_m)\le D\le a_m/q(J,m)`, i.e.
`q(J,m)\le\omega(a_m)\cdot a_m/|J|`. $\blacksquare$

**Explicit constants via the certified Growth Lemma.** By Lemma 1
(`lemmas/lemma-1-uniform-gap-bound.md`), `a_m\le a_1+(m-1)L<a_1+mL` for
every `m\ge1`; and elementarily `\omega(a_m)\le\log_2a_m` (each of the
`\omega(a_m)` distinct prime factors of `a_m` is `\ge2`, so `a_m\ge
2^{\omega(a_m)}$). A short computation (`i\ge1`): `a_1+iL\le(a_1+L)i$
(equivalent to `a_1(i-1)\ge0`, true for `i\ge1`), so `a_m<(a_1+L)m` and
`\log_2a_m<\log_2(a_1+L)+\log_2m` for every `m\ge1`. Substituting into the
Corollary:
$$q(J,m)\ <\ \frac{(a_1+L)m\cdot\bigl(\log_2(a_1+L)+\log_2m\bigr)}{|J|}\qquad(m\ge1,\ J\subseteq\{1,\dots,m-1\}\text{ nonempty}).\qquad(\ast)$$

#### 9.3 Specialization to the doubly-infinite pair, and the density hypothesis

For `i\in I_S`, `i\ge2`, write `J_i:=I_{S'}\cap\{1,\dots,i-1\}$. When
`J_i\ne\varnothing`, apply `(\ast)` with `m=i`, `J=J_i`, giving a prime
`q(i):=q(J_i,i)\in\mathrm{rad}(a_i)` with
$$q(i)\ <\ \frac{(a_1+L)i\cdot\bigl(\log_2(a_1+L)+\log_2i\bigr)}{|J_i|},\qquad\text{and}\qquad q(i)\text{ divides }\ge\frac{|J_i|}{\omega(a_i)}\text{ elements of }J_i.\qquad(\ast\ast)$$

This is Steps 1–3 of the outline, done completely and unconditionally: no
hypothesis beyond the already-certified Lemma P′ and Growth Lemma is used
anywhere in 9.1–9.3.

**Hypothesis `(PD_{S,S'})` (the open gap, precisely stated).** There exist
`c=c(S,S')>0` and `i_0` such that `|J_i|\ge c\cdot i` for every `i\in I_S`
with `i\ge i_0`.

**Proposition 9.4 (conditional magnitude cap).** Under `(PD_{S,S'})`, for
every `i\in I_S`, `i\ge i_0$,
$$q(i)\ <\ \frac{a_1+L}{c}\cdot\bigl(\log_2(a_1+L)+\log_2i\bigr)\ =\ K_1+K_2\log_2i,$$
where `K_1:=\frac{a_1+L}{c}\log_2(a_1+L)`, `K_2:=\frac{a_1+L}{c}` are
constants depending only on `a_1,S,S',c` (not on `i`). In particular
`q(i)=O(\log i)$.

**Proof.** Substitute `|J_i|\ge ci` into `(\ast\ast)`'s first inequality;
the `i` factors cancel: `q(i)<(a_1+L)i(\log_2(a_1+L)+\log_2i)/(ci)=
\frac{a_1+L}{c}(\log_2(a_1+L)+\log_2i)`. $\blacksquare$

This is exactly the outline's Step 4 target (an `O(\log i)` magnitude cap),
proved rigorously, **conditional on `(PD_{S,S'})`** — the sharpest form this
round's mechanism reaches. By the symmetric argument (swap the roles of
`S,S'`, using `J'_j:=I_S\cap\{1,\dots,j-1\}` for `j\in I_{S'}`), the
analogous conditional bound `q'(j)=O(\log j)$ holds under the symmetric
hypothesis `(PD_{S',S})`.

#### 9.5 Why `(PD_{S,S'})` is not free: a precise diagnosis (not a disproof)

`(PD_{S,S'})` does **not** follow from anything currently certified in this
workspace. Two independent reasons, both new to this round's writeup:

**(a) A finite partition with an infinite member of density `0` is
possible in general — Theorem CD's `\le2^k-1`-class decomposition alone is
not enough machinery.** Concrete counterexample (to the *general* claim
"finitely many classes partitioning `\mathbb N`, one infinite `\Rightarrow`
positive density"; this is a fact about arbitrary partitions, used here only
to show the inference pattern is invalid in general — it is **not** a
counterexample to `(PD_{S,S'})` itself, whose truth for *this specific*
sequence's classes remains open): partition `\mathbb N` into
`A:=\{n:n\text{ is a perfect square}\}` and `B:=\mathbb N\setminus A`. Both
are infinite; `|A\cap[1,N]|=\lfloor\sqrt N\rfloor=o(N)`, so `A` has density
`0`. This shows the mere fact that `I_{S'}` is one of finitely many classes
partitioning `\mathbb N` (Theorem CD) and is infinite (the doubly-infinite
hypothesis) does not, by itself, force `I_{S'}` to have positive density —
an actual argument using the specific recursive/arithmetic structure of
`(a_n)` (not just the abstract partition) would be needed, and none was
found this round.

**(b) The one density tool this workspace has built (the Euler-
divergence/Landau-Count toolkit of `theorem-UBS-false-case-II.md`) cannot
be repurposed here without circularity.** That toolkit's density conclusion
(the Imprint Periodicity Lemma, giving an *exact* density for `I_{P_1}`) is
derived *from* the hypothesis of *exact periodicity* `a_{n+T}=a_n+L`
(itself only available, via this file's own Theorem 5.1, *after* FCBC —
hence, via Theorem SW, after the Stabilization Conjecture — is established).
Using it to first establish `(PD_{S,S'})`, as a *route to* Stabilization,
would assume the very periodicity that Stabilization is meant to help
produce. No other density-producing tool for a general (non-periodic a
priori) proper core class was found in `knowledge_base.md` or previously
certified in this workspace this round.

**What was checked and found consistent (not proof).** Every numerical test
run in this workspace, this round and prior rounds, on every doubly-infinite
disjoint core pair tested (`a_1=247,2747,21528751,9674419,618`, spanning
`k=2$ to `k=4` and both extremely sparse (`\approx0.03\%`) and moderately
sparse (`\approx0.32\%`) classes), shows core-class densities **stabilizing**
rather than **decaying** as `N` grows — see the fresh `a_1=618` computation
in the "Round 10 update" section above and this round's math-explorer report
(`/tmp/round-10/math-explorer-H100-stabilization.md`) for the `a_1=21528751`
data. No test this round or any prior round found a class exhibiting
density decay of the kind the squares/non-squares counterexample shows is
*possible in principle*. This is corroborating evidence only, per CLAUDE.md,
not a proof step.

#### 9.6 Step 5 (reuse into a finite pool): honest status, with a concrete
warning

Even granting `(PD_{S,S'})$ and `(PD_{S',S})$ in full (both classes have
positive density relative to the other), Proposition 9.4 only produces, for
**each** `i\in I_S` past `i_0`, **one** prime `q(i)=O(\log i)` covering
**some** (not necessarily all, and not necessarily a growing *fraction* —
only a growing *count*, `\ge|J_i|/\omega(a_i)=\Omega(i/\log i)`, of) the
earlier `S'`-indices. This does **not** by itself give a single finite pool
`W_{S,S'}` covering **every** cross pair — the outline's own Step 5 is
correct that a separate "reuse" argument is needed, and this round did not
find one.

Moreover, a **concrete, already-certified precedent in this workspace**
shows the most natural version of "reuse" — literally collecting the
per-index pigeonhole witnesses `\{q(i):i\in I_S\}\cup\{q'(j):j\in I_{S'}\}`
into one set and hoping it covers every pair — is architecturally the same
construction that Propositions ND1 and ND2
(`lemmas/proposition-ND1-ND2-domination-mechanisms-insufficient.md`,
certified) prove **fails**, on two independently hand-verified concrete
traces (`a_1=221`: the pair `(a_2,a_4)`'s unique shared prime `3` is never
selected as any step's Domination-Lemma witness, even taking *every* prime
meeting the averaged threshold, not just the unique argmax; `a_1=375`:
similarly for the pair `(a_3,a_7)`'s unique shared prime `19`). Those
propositions concern the *unrestricted* Domination Lemma (`J=\{1,\dots,
n\}`, not this round's cross-class-restricted `J_i`), so they do **not**
literally refute this round's construction — but the failure mode (a
specific pair's *unique* shared prime is simply never chosen as *anyone's*
pigeonhole witness, because pigeonhole only guarantees *some* dominant
prime exists at each step, not that it will be the *right* one for every
later-needed pair) is structurally identical, and any future attempt at
Step 5 should design explicitly around this documented failure rather than
assume "collect the witnesses" works.

**Summary of this round's status on the Stabilization Conjecture.** Steps
1–3 (Lemma RD, Magnitude Bound Corollary, Proposition 9.4) are complete,
rigorous, and unconditional given `(PD_{S,S'})`/`(PD_{S',S})`. Step 4
(establishing those density hypotheses) and Step 5 (a reuse/pooling argument
avoiding the ND1/ND2 failure mode) remain open, with precise diagnoses of
why each is hard recorded above — not previously written down in this
workspace in this quantitative form. The Stabilization Conjecture itself is
**not** proved or disproved this round.

---

### Part 11 — Round 12: Bounded-Run-Length `\Rightarrow(PD_{S,S'})`, a
fully rigorous CONDITIONAL theorem

#### 11.0 Scope: what this closes and what it does not

Part 9.5 left `(PD_{S,S'})` (Step 4 of the Stabilization Conjecture's
residual content) entirely open, and Part 10.3 diagnosed a genuine
circularity obstruction to proving "eventual near-periodicity of class
membership" from the greedy recursion's own structure without assuming
`(\dagger')`. This round's outline retargets Step 4 via a sharper,
strictly weaker-to-establish combinatorial target — a **bounded-run-length**
property of the coarse core sequence — and asks for the implication
"periodicity `\Rightarrow(PD_{S,S'})`" to be made fully rigorous as a
**conditional theorem**, honestly separating what is proved (the
implication) from what is open (the hypothesis). This subsection does
exactly that, completely, with explicit constants. It does **not** prove
`G` is periodic (that remains open, §11.5), and it does **not** address
Part 9.6's separate Step 5 gap (the reuse/pooling argument) — even once
`(PD_{S,S'})` is available (conditionally or otherwise), Step 5 is a further,
independent obstruction to the full Stabilization Conjecture, untouched by
this Part.

#### 11.1 Definitions

Fix `a_1`, `k:=|P_1|`, and let `\mathcal A:=\{S\subseteq P_1:S\ne
\varnothing\}` (`|\mathcal A|\le2^k-1`). By the already-certified Theorem
CD (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`), every index
`n\ge1` has a well-defined core `S(n):=\mathrm{rad}(a_n)\cap P_1\in\mathcal
A` (nonempty for every `n`), so
$$G:\mathbb N\to\mathcal A,\qquad G(n):=S(n)$$
is a well-defined, unconditional (no hypothesis beyond the problem's own
definition) sequence over a fixed finite alphabet. As before,
`I_S:=\{n\ge1:G(n)=S\}` for `S\in\mathcal A`; these sets partition
`\mathbb N`.

**Definition (eventual periodicity of `G`).** `G` is *eventually periodic*
with pre-period `n_0\ge0` and period `T\ge1` if `G(n+T)=G(n)` for every
`n>n_0`. The case `n_0=0` ("periodicity from `n=1`") is the pattern
observed numerically in every tractable instance so far (§11.4).

**Definition (run avoiding `S'`).** For `S'\in\mathcal A` and `n\ge1`,
`\ell\ge0`, call `\{n,n+1,\dots,n+\ell\}` a *run avoiding `S'`* if
`G(m)\ne S'` for every `m` in the window — equivalently,
`\{n,\dots,n+\ell\}\cap I_{S'}=\varnothing`. (Here "avoiding `S'`" means
the core is not *exactly* `S'`, the reading that makes `I_{S'}` — a cell of
Theorem CD's partition — well-posed; this is the same reading used
throughout Part 9's `(PD_{S,S'})`.)

**Definition (Bounded-Run-Length property, `\mathrm{BRL}(S')`).** There is
a finite `R=R(S')` such that every run avoiding `S'` has length `\le R`
(i.e. `\le R+1` indices); equivalently: for every `n\ge1`,
`\{n,n+1,\dots,n+R\}\cap I_{S'}\ne\varnothing`.

This is the outline's Step 2′ target pinned down precisely, exactly as the
outline itself asked for ("precise combinatorial form to be pinned down by
the builder first").

#### 11.2 Lemma BRL-from-Periodicity

**Lemma BRL-from-Periodicity.** Suppose `G` is eventually periodic with
pre-period `n_0` and period `T`. Let `S'\in\mathcal A` with `I_{S'}`
infinite. Then `\mathrm{BRL}(S')` holds with `R:=n_0+T`.

**Proof.**

*Step 1 (reduction to one periodic block).* For `n>n_0`, an immediate
induction on the number of period-shifts (using `G(m)=G(m-T)` whenever
`m-T>n_0`) shows `G(n)=G(n_0+\varphi(n))`, where `\varphi(n)\in\{1,\dots,
T\}` is the unique integer with `n\equiv n_0+\varphi(n)\pmod T`. Hence for
every `n>n_0`, `G(n)\in\{G(n_0+1),\dots,G(n_0+T)\}`. If `S'` were not among
`\{G(n_0+1),\dots,G(n_0+T)\}`, then `G(n)\ne S'` for every `n>n_0`, so
`I_{S'}\subseteq\{1,\dots,n_0\}` — finite, contradicting the hypothesis
`I_{S'}` infinite. So
`$\mathcal T^*:=\{t\in\{1,\dots,T\}:G(n_0+t)=S'\}\ne\varnothing$`.

*Step 2 (occurrences after `n_0` form a `T`-periodic union of arithmetic
progressions).* By periodicity, for `t\in\mathcal T^*` and every `j\ge0`,
`G(n_0+t+jT)=G(n_0+t)=S'` (apply `G(m+T)=G(m)` repeatedly, valid since
`n_0+t+j'T>n_0` for every `j'\ge0` as `t\ge1`). Conversely, if `n>n_0` and
`G(n)=S'`, Step 1 gives `n\equiv n_0+\varphi(n)\pmod T` with `\varphi(n)\in
\mathcal T^*` (since `G(n_0+\varphi(n))=G(n)=S'`), so `n=n_0+\varphi(n)+jT`
for some `j\ge0`. Hence
$$\{n>n_0:G(n)=S'\}=\{n_0+t+jT:t\in\mathcal T^*,\ j\ge0\}.$$

*Step 3 (bounding runs).* Let `n_1:=n_0+\min\mathcal T^*` (the first
occurrence of `S'` strictly after `n_0`; `n_1\le n_0+T`, since `\min
\mathcal T^*\le T`). By Step 2, `n_1,n_1+T,n_1+2T,\dots` are all occurrences
of `S'` (taking `t=\min\mathcal T^*` in Step 2's description). Fix `R:=
n_0+T` and an arbitrary `n\ge1`; we show `\{n,\dots,n+R\}` meets
`\{n_1,n_1+T,n_1+2T,\dots\}\subseteq I_{S'}`, which proves the Lemma.

- If `n\le n_1`: since `n_1\le n_0+T=R` and `n\ge1`, `n_1\in[n,n+R]`
  (`n\le n_1` is the case hypothesis, and `n_1\le R\le n+R-1<n+R`, using
  `n\ge1`). So `n_1\in\{n,\dots,n+R\}\cap I_{S'}`.
- If `n>n_1`: let `j:=\lceil(n-n_1)/T\rceil\ge1` (a well-defined positive
  integer since `n-n_1\ge1>0`). By definition of the ceiling,
  `n_1+jT\ge n`. Also `(j-1)T<n-n_1` (since `j` is the *smallest* integer
  with `n_1+jT\ge n`, `j-1` fails this, i.e. `n_1+(j-1)T<n`), so
  `n_1+jT<n_1+(n-n_1)+T=n+T\le n+R` (using `R=n_0+T\ge T`, as `n_0\ge0`).
  Hence `n_1+jT\in\{n,\dots,n+R-1\}\subseteq\{n,\dots,n+R\}`, and
  `n_1+jT` is an occurrence of `S'` by Step 2.

In both cases `\{n,\dots,n+R\}\cap I_{S'}\ne\varnothing`. As `n\ge1` was
arbitrary, `\mathrm{BRL}(S')` holds with `R=n_0+T`. `\blacksquare`

*(Sanity check, not part of the proof: for `a_1=247`, `n_0=0,T=1806`, so
`R=1806`; a fresh, independently-generated computation this round — exact
factorization, brute-force admissibility, verified against a from-scratch
gcd check on the first `400` terms before trusting it at scale — confirms
`G(n+1806)=G(n)` for all `1\le n\le2194` and finds the *actual* maximum run
avoiding `\{13\}` is only `3`, avoiding `\{19\}` only `5` — Lemma
BRL-from-Periodicity's bound `R=1806` is a valid but far from tight upper
bound, exactly as expected from a worst-case pigeonhole-style argument; the
Lemma only needs *some* finite `R`, not a tight one.)*

#### 11.3 Lemma PD-from-BRL and Theorem PD-Conditional

**Lemma PD-from-BRL.** Suppose `\mathrm{BRL}(S')` holds with constant `R`.
Then for every `N\ge1`,
$$|I_{S'}\cap[1,N]|\ \ge\ \left\lfloor\frac{N}{R+1}\right\rfloor.$$
Consequently, for any core `S\ne S'` (in particular for a disjoint pair,
though disjointness is not needed for this specific inequality),
`(PD_{S,S'})` holds — in the precise sense of Proposition 9.4's hypothesis,
`\exists c>0,i_0` with `|I_{S'}\cap[1,i)|\ge ci` for all `i\ge i_0`
(in particular for all `i\in I_S,\,i\ge i_0`) — with the fully explicit
constants `c:=\dfrac1{2(R+1)}`, `i_0:=2R+4`.

**Proof.** Fix `N\ge1` and set `B:=\lfloor N/(R+1)\rfloor`. Partition
`\{1,\dots,B(R+1)\}\subseteq\{1,\dots,N\}` into `B` pairwise-disjoint
consecutive blocks of size exactly `R+1`: the `b`-th block
(`b=1,\dots,B`) is `\{(b-1)(R+1)+1,\dots,b(R+1)\}=\{n,\dots,n+R\}` with
`n=(b-1)(R+1)+1`. By `\mathrm{BRL}(S')`, each block meets `I_{S'}`. Since
the `B` blocks are pairwise disjoint subsets of `\{1,\dots,N\}`,
$$|I_{S'}\cap[1,N]|\ \ge\ |I_{S'}\cap\{1,\dots,B(R+1)\}|\ \ge\ B\ =\ \left\lfloor\frac N{R+1}\right\rfloor.$$

For the "consequently" clause, apply with `N=i-1` for `i\ge1`, using the
elementary inequality `\lfloor x\rfloor>x-1` (hence `\lfloor x\rfloor\ge
x-1`, since `\lfloor x\rfloor` is an integer and this only needs the
non-strict form):
$$|I_{S'}\cap[1,i)|=|I_{S'}\cap[1,i-1]|\ \ge\ \left\lfloor\frac{i-1}{R+1}\right\rfloor\ \ge\ \frac{i-1}{R+1}-1\ =\ \frac{i-R-2}{R+1}.$$
For `i\ge i_0:=2R+4`: `R+2\le i/2`, so `i-R-2\ge i-i/2=i/2`, hence
$$|I_{S'}\cap[1,i)|\ \ge\ \frac{i/2}{R+1}\ =\ \frac{i}{2(R+1)}\ =\ c\cdot i,$$
proving the claim for every `i\ge i_0` (a fortiori for every `i\in I_S`,
`i\ge i_0`). `\blacksquare`

**Theorem PD-Conditional (this round's main result).** Fix `a_1` and
suppose `G` is eventually periodic with pre-period `n_0` and period `T`.
Then for **every** doubly-infinite disjoint core pair `(S,S')` of `a_1`
(both `I_S,I_{S'}` infinite, `S\cap S'=\varnothing`), **both**
`(PD_{S,S'})` and `(PD_{S',S})` hold, with the **uniform** constants
`c=\dfrac1{2(n_0+T+1)}`, `i_0=2(n_0+T)+4` — depending only on `a_1` (via
`n_0,T`), not on the specific pair `(S,S')`.

**Proof.** `I_{S'}` is infinite (doubly-infinite hypothesis), so Lemma
BRL-from-Periodicity gives `\mathrm{BRL}(S')` with `R=n_0+T`; Lemma
PD-from-BRL then gives `(PD_{S,S'})` with `c=1/(2(R+1)),i_0=2R+4` as
stated. Symmetrically, `I_S` is infinite, so the same two lemmas
(with the roles of `S,S'` swapped) give `\mathrm{BRL}(S)` with the same
`R=n_0+T`, hence `(PD_{S',S})` with the same `c,i_0`. `\blacksquare`

**Corollary (conditional magnitude cap, this round).** Combining Theorem
PD-Conditional with the already-certified Proposition 9.4
(`lemmas/lemma-RD-restricted-domination-and-magnitude-bound.md`): IF `G`
is eventually periodic for `a_1`, THEN for every doubly-infinite disjoint
core pair `(S,S')` of `a_1`, both pigeonhole witness families `q(i)`
(`i\in I_S`) and `q'(j)` (`j\in I_{S'}`) satisfy an explicit `O(\log i)`/
`O(\log j)` magnitude cap, with constants `K_1,K_2` depending only on
`a_1` (via `n_0,T,\mathrm{rad}(a_1)`) — **uniformly** over every
doubly-infinite disjoint pair of that `a_1`, not just a single pair.
`\blacksquare` (immediate substitution of Theorem PD-Conditional's uniform
`c` into Proposition 9.4's explicit inequality).

#### 11.4 Honest status of the periodicity hypothesis: what is proved, what is not

Theorem PD-Conditional and its Corollary are **fully proved, unconditional
implications** — no gap, no hidden appeal to `(\dagger')` or any other open
hypothesis (Lemma BRL-from-Periodicity's proof, §11.2, uses only the
definition of eventual periodicity and elementary arithmetic of residues;
Lemma PD-from-BRL's proof, §11.3, is elementary pigeonhole). **What remains
open is the hypothesis itself: eventual periodicity of `G`.** This round
does **not** prove it in general, and per this workspace's rigor rules
(CLAUDE.md: "distinguish 'we have proved X' from 'we conjecture X'"), it
must not be presented as established.

**Numerical status (evidence, not proof).** Two independently-written
generators — this round's math-explorer (`/tmp/round-12/math-explorer-pd-
density.md`, KMP/Border-Lemma exact-period finder) and the round-12
outline-reviewer's own from-scratch re-derivation
(`/tmp/round-12/outline-reviewer.md`, "Central finding 2") — agree exactly
on periodicity-from-`n=1` (`n_0=0`) for:

| `a_1` | `k=|P_1|` | period `T` | tested up to `N` | repeats confirmed |
|---|---|---|---|---|
| `4087=61\cdot67` | 2 | `64` | `2{,}000{,}000` | `\approx31{,}250` |
| `247=13\cdot19` | 2 | `1806` | `3{,}000{,}000` | `\approx1661` |
| `2747=41\cdot67` | 2 | `2062` | `2{,}000{,}000` | `\approx970` |
| `4199=13\cdot17\cdot19` | 3 | `105250` | `3{,}000{,}000` | `\approx28.5` |

and `a_1=21528751=103\cdot197\cdot1061` remains **genuinely inconclusive**:
no period was found below `N=400{,}000` (the math-explorer's generator did
not finish a `1.5\times10^6`-term run within its time budget). This
workspace's own standing rule (extend a "looks stable" claim `\ge10\times`
past its previous cutoff before trusting it) is satisfied for all four
tractable cases by a wide margin (`28`–`31{,}250`\times`, not merely
`10\times`) — this is unusually strong numerical corroboration — but it
remains corroboration, not proof, per CLAUDE.md's explicit rule that a
numeric check is never itself a proof step. **No instance of `G`
periodicity being false was found**, and no instance of `(PD_{S,S'})`
failing was found either (consistent with, not a proof of, the conditional
theorem's hypothesis holding universally).

#### 11.5 A fresh attempt at closing the periodicity hypothesis unconditionally — confirms, does not merely repeat, round 11's obstruction

Per the dispatch's request to be explicit about what remains open, this
round made one concrete new attempt (not simply re-asserting Part 10.3):
test whether the outline's own heuristic ("reusing a `P_1`-prime is
cheaper than manufacturing an ever-larger companion bundle, since `P_1` is
fixed and finite while companion primes are drawn from an unbounded
supply") can be turned into a genuine bound on `\mathrm{BRL}(S')`
*directly*, bypassing periodicity entirely, via the already-certified Lemma
W3 (Minimal Radical Reduction Lemma,
`lemmas/lemma-W2-W3-patch-and-minimal-radical-reduction.md`): admissibility
of a candidate `x` at step `n` depends only on the `n`-minimal indices
`M_n\subseteq\{1,\dots,n\}` (those `i` with no `k\le n` having
`\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)`), a data-compression that in
principle could support a "bounded effective state" argument if `|M_n|`
stayed bounded.

**This does not work, and the reason is already on record, unconditionally,
in this very lemma's own certified file.** Lemma W3's "Discussion" section
states, as an already-certified observation (not merely a worry): `|M_n|`
was checked numerically to keep growing with `n` (`a_1=221`:
`|M_{199}|=42`). If `|M_n|\to\infty`, the compressed admissibility check
still depends on an *unboundedly growing* amount of state as `n\to\infty`,
so no argument of the shape "only finitely many possible admissibility
configurations exist, hence some run-length must be bounded by pigeonhole
on configurations" can be built on top of Lemma W3 alone — exactly
reproducing, in this round's own sharper Bounded-Run-Length language, the
obstruction Part 10.3 already diagnosed for the coarser "eventual
near-periodicity" target: any reduction of the admissibility check (hence
of `G`'s next value) to *bounded* state is currently known **only** via
Theorem 2.2, which needs `(\dagger')` itself. **No `H`-independent
mechanism was found this round either.** This is recorded as a genuine,
specific negative finding — a confirmed dead end for *this* candidate
route (Lemma W3-based state compression), narrower and more concrete than
Part 10.3's general diagnosis, not a restatement of it.

#### 11.6 Summary of Part 11

- **Theorem PD-Conditional and its Corollary: proved in full, no gaps,
  unconditional as implications.** This is new, promotable content (see
  Promotable lemmas below).
- **The periodicity hypothesis itself: open.** Strong (but, per CLAUDE.md,
  non-probative) numerical support on 4 of 5 tested instances; genuinely
  inconclusive on the 5th (`a_1=21528751`); no unconditional proof or
  disproof found this round, and one further concrete candidate mechanism
  (Lemma W3-based state compression) was tried and shown, using the
  lemma's own already-certified `|M_n|`-unboundedness fact, not to work.
- **The Stabilization Conjecture (hence the whole problem) remains open.**
  Even granting the periodicity hypothesis in full, Part 9.6's Step 5
  reuse/pooling gap is untouched by this Part and remains a further,
  separate obstruction. Status stays `partial`.

---

### Part 12 — Round 13: an unconditional CRT existence fact (Lemma WO) and
why it — and the sibling's Backbone Permanence mechanism — cannot by
themselves close `\mathrm{BRL}`/`G`-periodicity (Proposition BI)

**Recall the target.** For a doubly-infinite disjoint core pair `(S,S')`,
write `\mathrm{BRL}(S')` for the Bounded-Run-Length property: there is a
finite `R=R(S')` such that no `R+1` consecutive indices `n,n+1,\dots,n+R`
all have `S(n+j)\ne S'` for `j=0,\dots,R` (equivalently, `I_{S'}` meets every
window of `R+1` consecutive indices). By the already-certified Lemma
PD-from-BRL (Part 11.3), `\mathrm{BRL}(S')` alone (no periodicity of the
*whole* sequence `G` needed) already gives `(PD_{S,S'})` with explicit
constants. This Part attacks `\mathrm{BRL}(S')` directly, not via `G`'s
periodicity.

### 12.1 — Lemma WO (Window Occupancy), unconditional, no gap

**Setup.** As in Part 8, let `P_1=\mathrm{rad}(a_1)=\{p_1,\dots,p_k\}`, and
let `L_0:=p_1p_2\cdots p_k` (the same constant called `L` in the
already-certified Lemma 1, `lemmas/lemma-1-uniform-gap-bound.md`; renamed
`L_0` here only to avoid clashing with Part 1's `L:=\mathrm{lcm}(H)`). For an
integer `x>1` write `S(x):=\mathrm{rad}(x)\cap P_1` (well-defined and
nonempty for every term of the sequence by Theorem CD, but the definition
below makes sense for *any* positive integer `x`, term of the sequence or
not).

**Lemma WO (Window Occupancy).** For every integer `m\ge0` and every
nonempty `S'\subseteq P_1`, the number of integers `x\in(m,m+L_0]` with
`S(x)=S'` exactly equals
$$c_{S'}\ :=\ \prod_{p\in P_1\setminus S'}(p-1)\ \ (\ge1,\text{ since each
factor }p-1\ge1\text{ for a prime }p\ge2),$$
independent of `m`.

**Proof.** `L_0=p_1\cdots p_k` is a product of `k` pairwise distinct primes,
hence pairwise coprime moduli. By CRT, the map
$$\varphi:\{m+1,m+2,\dots,m+L_0\}\ \longrightarrow\ \prod_{i=1}^k\mathbb
Z/p_i\mathbb Z,\qquad \varphi(x):=(x\bmod p_1,\dots,x\bmod p_k),$$
is a bijection (a set of `L_0` consecutive integers is a complete residue
system mod `L_0`, and CRT identifies `\mathbb Z/L_0\mathbb Z` with
`\prod_i\mathbb Z/p_i\mathbb Z`). Now `S(x)=S'` exactly means: `p_i\mid x`
for every `p_i\in S'`, and `p_i\nmid x` for every `p_i\in P_1\setminus S'`
— i.e. `\varphi(x)` lies in the product set
$$T_{S'}\ :=\ \prod_{p_i\in S'}\{0\}\ \times\ \prod_{p_i\in P_1\setminus
S'}(\mathbb Z/p_i\mathbb Z\setminus\{0\}).$$
Since `\varphi` is a bijection, the number of `x\in(m,m+L_0]` with
`S(x)=S'` equals `|T_{S'}|=\prod_{p_i\in S'}1\cdot\prod_{p_i\in P_1
\setminus S'}(p_i-1)=c_{S'}`, independent of `m` (the bijection `\varphi`
itself does not depend on `m` beyond the choice of representative window;
shifting the window by `L_0` just relabels which representative of each
residue class is used, not the *count* in each fiber). $\blacksquare$

**Corollary (candidates exist, unconditionally, in every step's window).**
Combining Lemma WO with the already-certified Lemma 1 (`a_{n+1}-a_n\le
L_0` for every `n`): for every `n\ge1` and every nonempty `S'\subsetneq
P_1`, the window `(a_n,a_n+L_0]` — which contains `a_{n+1}` by Lemma 1 —
also contains at least `c_{S'}\ge1` integers of type exactly `S'`. So a
"right-type" candidate is *always* present nearby; Lemma WO is
unconditional and gap-free.

### 12.2 — Why Lemma WO does not close `\mathrm{BRL}`: the Admissibility
Gap (honest diagnosis, not a proof of impossibility)

Lemma WO guarantees *existence* of an `S'`-type integer in every window,
but `a_{n+1}` is not an arbitrary integer in that window — it is the
*smallest admissible* one. Admissibility (`\gcd(x,a_i)>1` for *every*
`i\le n`) is a condition against the *entire* history, and nothing in Lemma
WO's proof (a purely local CRT fact about *one* window, oblivious to the
sequence's history) supplies any reason that the `c_{S'}` type-`S'`
candidates in a given window are ever admissible, nor any bound on how many
consecutive windows can pass with *none* of their type-`S'` candidates
admissible. This is the same "pointwise feasibility does not persist"
obstruction already on record in this workspace (see the standing Rule from
round 8 on pointwise-in-`N` bounds not controlling unions over `N`) — Lemma
WO sharpens *what* is available in each window (an exact count, not just an
existence claim) but does not, by itself, touch admissibility at all.
Closing this gap needs a genuinely different ingredient — attempted next.

### 12.3 — Proposition BI (Backbone Permanence Does Not Force Class
Revisitation), unconditional, proved in full

This round's sibling approach `sunflower-inadmissibility-toolkit` attacks,
for the identical target pairs, a **Backbone Permanence** hypothesis (its
own "EBS," Early/Bounded Stabilization): a companion prime `q\notin P_1`
(or more generally a fixed nonempty companion set `B`) eventually divides
*every* member of `I_{S'}`. It is natural to hope this would supply the
missing ingredient for `\mathrm{BRL}(S')` — e.g. via a chain like "once
`I_{S'}`'s companions stabilize, admissibility against `I_{S'}` becomes a
single fixed constraint that only `S'`-type integers can satisfy [FALSE, see
below], forcing periodic revisitation." Proposition BI shows this chain
breaks at the bracketed step, unconditionally.

**Proposition BI.** Suppose there is a companion prime `q\notin P_1` and an
index `N_0` such that `q\mid a_j` for every `j\in I_{S'}` with `j\ge N_0`
(Backbone Permanence for `S'` via `q`, the sibling's EBS target's literal
content for a single-prime backbone). Then for every `n\ge N_0` and every
integer `x>a_n` with `q\mid x`,
$$\gcd(x,a_j)>1\qquad\text{for every }j\in I_{S'}\cap[N_0,n],$$
**regardless of `S(x)`** — in particular this holds whether or not `S(x)=
S'`.

**Proof.** Fix such `n,x,j`. By hypothesis `q\mid a_j` (since `j\in
I_{S'}\cap[N_0,n]\subseteq I_{S'}\cap[N_0,\infty)`), and by construction
`q\mid x`. So `q` is a common divisor of `x` and `a_j`, giving `\gcd(x,a_j)
\ge q>1`. This uses only the hypothesis on `q` and the definition of
`\gcd`; no property of `S(x)` (in particular, no requirement that any prime
of `S'` or of `P_1` at all divide `x`) is used anywhere. $\blacksquare$

**Interpretation (the negative finding).** Proposition BI shows that the
entire infinite sub-family of admissibility constraints contributed by
`I_{S'}\cap[N_0,\infty)` — the constraints one might expect to be the
*reason* the greedy sequence keeps returning to class `S'` — is **uniformly
dischargeable** by `q` alone, for every `x` divisible by `q`, with **no
dependence on `S(x)` whatsoever**. So Backbone Permanence for `S'`, even
established in full generality (not merely on the two tested instances the
sibling approach targets this round), supplies **no logical obstruction** to
a run of consecutive indices avoiding `I_{S'}` indefinitely: nothing in the
`I_{S'}`-side constraints, once the backbone stabilizes, could ever be
violated by staying `S'`-avoiding — any sufficiently large multiple of `q`
discharges all of them at once, and multiples of `q` are compatible with
every possible value of `S(x)`, including every `S(x)\ne S'`. Consequently,
Backbone Permanence **cannot be the mechanism** behind any proof of
`\mathrm{BRL}(S')`: if the greedy sequence nonetheless keeps returning to
`I_{S'}` (as it does, empirically, in every tested instance — Part 12.4
below), the reason must be something Proposition BI's argument does not
touch — namely that the greedy always chooses the numerically **smallest**
admissible candidate, and *empirically* that smallest candidate keeps
landing back in `I_{S'}` even though, by Proposition BI, it is never
*forced* to by feasibility alone. This is a **minimality** phenomenon, not a
**feasibility** phenomenon, and no lemma currently certified in this
workspace (Domination Lemma, Lemma RD, Companion-Disjointness Coarsening,
Backbone Permanence/EBS, Lemma WO above) reasons about minimality — every
one of them is a feasibility/pigeonhole-existence tool. This is a precise
sharpening of round 11's Part 10.3 circularity diagnosis: it identifies
*which* known category of tool (feasibility arguments) is structurally
unable to help, not merely that no `H`-independent tool has yet been found.

### 12.4 — Numerical corroboration (evidence only, not a proof step)

On the sibling approach's own mandatory Case A instance `a_1=2747`
(`P_1=\{41,67\}`, backbone candidate `\{2,3,7\}`, freshly generated by an
independent generator — full-history admissibility check, cross-checked
against the first 20 terms already recorded in this file's Part 6 table for
consistency of method, though `2747` was not itself in that table): among
`40{,}000` consecutive terms, `99.4\%` are divisible by `2`, `3`, or `7`
(`39{,}767/40{,}000`); restricted to the `38{,}408` terms of core exactly `\{41\}`
and the `777` terms of core exactly `\{67\}` found within the same range,
**both** classes are `100\%` divisible by `\{2,3,7\}`. So the backbone data
is, exactly as Proposition BI predicts, uninformative for distinguishing
which class a term belongs to — it is common to (very nearly) the whole
sequence, not a signature of `I_{67}` specifically. Separately, the observed
gaps between consecutive `I_{67}` occurrences are `\approx50`, stable
(oscillating `49`–`53`, no further growth) from `n=6000` through `n=40{,}
000` in this fresh run — consistent with, but (per CLAUDE.md) not a proof
of, `\mathrm{BRL}(\{67\})` holding with a fairly small `R`. This is offered
purely as corroborating context for why the mechanism sought (something
sensitive to minimality/residue structure) is plausible, not as any part of
the proof, which rests entirely on Lemma WO and Proposition BI above.

### 12.5 — Summary of this round's contribution

- **Lemma WO** — proved in full, unconditional, promotable: an exact CRT
  count of how many "right-type" candidates occur in every fixed-length
  window, independent of the sequence's history.
- **Proposition BI** — proved in full, unconditional, promotable: a clean
  three-line but structurally decisive negative result, ruling out
  Backbone-Permanence-style feasibility mechanisms (the sibling approach's
  own target this round) as a route to `\mathrm{BRL}`/`G`-periodicity, with
  a precise diagnosis of *why* (feasibility vs. minimality) rather than a
  restated suspicion.
- **`\mathrm{BRL}(S')`/`G`-eventual-periodicity itself remains open.** No
  proof, no disproof. The concrete positive redirection for future rounds:
  any closing argument needs to reason about which admissible candidate is
  numerically *smallest* at each step (a minimality-sensitive argument),
  not merely that some admissible candidate of the right type exists or
  that admissibility constraints are jointly satisfiable — no tool currently
  in this workspace's certified toolkit does that.

---

## Part 13 (round 14) — the Minimality Obstruction: why a CRT/residue-class
minimality tool cannot supply what Proposition BI's redirection asked for

Proposition BI (round 13) diagnosed the missing ingredient as *minimality*
— reasoning about which admissible candidate is numerically smallest, not
just that admissible candidates of a given type exist. This round attempts
exactly that: to build a tool reasoning about minimality of admissible
candidates in a residue class / CRT setting, as instructed. The outcome is
a **rigorous impossibility proof**, not a further unsuccessful search: any
tool of the natural shape (a bounded finite modulus, i.e. built from a
fixed finite set of primes and hence expressible via CRT) is either
provably powerless (if restricted to `P_1`) or provably redundant (if
extended beyond `P_1`, it collapses into content this workspace already
has under a different name). This retires an entire technique family, the
same way `theorem-UBS-false-case-II.md` retired the `(UB_S)` program.

### 13.1 — Lemma WO++ (Joint CRT Independence), new, unconditional, fully proved

**Setup (unchanged from Lemma WO).** `P_1=\{p_1,\dots,p_k\}=\mathrm{rad}
(a_1)`, `L_0:=p_1\cdots p_k`. For `x\in\mathbb Z_{>0}`, `S(x):=\mathrm{rad}
(x)\cap P_1`. For nonempty `S'\subseteq P_1`, `c_{S'}:=\prod_{p\in
P_1\setminus S'}(p-1)` (Lemma WO's exact per-window count).

**Statement.** Let `W=\{q_1,\dots,q_r\}` be *any* finite set of primes
with `W\cap P_1=\varnothing` (in particular: `W=\mathrm{comp}(a_i)` for any
term `a_i`, since `\mathrm{comp}(\cdot)` is disjoint from `P_1` by
definition). Let `M:=L_0\cdot q_1\cdots q_r`. For every nonempty `S'
\subseteq P_1` and every subset `E\subseteq\prod_{q\in W}\mathbb Z/q
\mathbb Z` of joint residues mod the primes of `W`, and every integer
`m\ge0`: the number of integers `x\in(m,m+M]` with `S(x)=S'` **and**
`(x\bmod q_1,\dots,x\bmod q_r)\in E` equals **exactly** `c_{S'}\cdot|E|`,
independent of `m`.

**Proof.** `M` is a product of `k+r` pairwise distinct primes (the `p_i`'s
and the `q_j`'s are distinct: the `p_i` are distinct by definition of
`P_1=\mathrm{rad}(a_1)`; the `q_j` are distinct by hypothesis on `W`;
`W\cap P_1=\varnothing` gives no prime is repeated across the two groups).
By CRT, any `M` consecutive integers form a complete residue system mod
`M`, so `\psi:\{m+1,\dots,m+M\}\to\bigl(\prod_{i=1}^k\mathbb Z/p_i\mathbb
Z\bigr)\times\bigl(\prod_{j=1}^r\mathbb Z/q_j\mathbb Z\bigr)`, `\psi(x):=
(x\bmod p_1,\dots,x\bmod p_k,\,x\bmod q_1,\dots,x\bmod q_r)`, is a
bijection. The event `\{S(x)=S'\}\cap\{(x\bmod W)\in E\}` corresponds
exactly to `T_{S'}\times E` under `\psi`, where `T_{S'}\subseteq\prod_i
\mathbb Z/p_i\mathbb Z` is Lemma WO's own set (`|T_{S'}|=c_{S'}`, proved
there). Since `\psi` is a bijection, the count equals `|T_{S'}\times E|=
c_{S'}\cdot|E|`. `\blacksquare`

**Independent numerical verification (this round, fresh Python, two
independent test cases).** `P_1=\{13,19\}`, `S'=\{19\}` (`c_{S'}=12`),
`q=5`: counted, in the window `(1000,1000+247\cdot5]`, the number of
integers of type `\{19\}` in each residue class mod `5` — got exactly `12`
in **every** one of the `5` residue classes (`\{0,1,2,3,4\}`), matching
the formula exactly (`|E|=1` for a single residue). `P_1=\{13,17,19\}`,
`S'=\{13,17\}` (`c_{S'}=18`), `q=7`, checked at three independent window
offsets `m\in\{0,5000,123456\}`: exactly `18` per residue class mod `7`,
at every offset, no exceptions. `\blacksquare` (numerical check, not part
of the proof, which is the CRT bijection argument above and needs no
verification beyond re-deriving it by hand, which was also done).

**Corollary (Admissibility-Blindness of the `P_1`-alphabet).** Take
`E_{\mathrm{adm}}:=\{(r_1,\dots,r_r):\text{some }r_j=0\}` (the event "`x`
is divisible by at least one prime of `W`"). `|E_{\mathrm{adm}}|=
\prod_{q\in W}q-\prod_{q\in W}(q-1)` (complement of the all-nonzero
tuples), **independent of `S'`**. Hence, by Lemma WO++, the fraction of
type-`S'` integers in a large window that are divisible by at least one
prime of `W` equals `|E_{\mathrm{adm}}|/\prod_{q\in W}q=1-\prod_{q\in W}
(1-1/q)` — **exactly the same fraction as among integers of every other
type**, for every choice of `S'`. So knowing `S(x)=S'` carries **zero**
information, in the exact (not asymptotic) CRT-counting sense, about
whether `x` shares a prime with `W`.

### 13.2 — Theorem MO (Minimality Obstruction), new, unconditional, fully proved

**Statement.** Fix a doubly-infinite disjoint core pair `(S,S')` of `P_1`
and fix any `i\in I_S`. Then **no function of `S(y)` alone** (equivalently,
of `y\bmod L_0`) determines, or even biases, whether a candidate `y` with
`S(y)=S'` is admissible against `a_i` (i.e. `\gcd(y,a_i)>1`). More
precisely: among the type-`S'` integers in any sufficiently large window,
exactly the fraction `1-\prod_{q\in\mathrm{comp}(a_i)}(1-1/q)` are
admissible against `a_i` — the identical fraction as among ALL integers,
regardless of type; the `P_1`-alphabet (Lemma WO's raw material) supplies
no discriminating power whatsoever between "will be admissible against
`a_i`" and "will not."

**Proof.** By the already-certified Lemma NIDF(a) (`lemmas/lemma-XC-NIDF-
FT-cross-companion-transversal.md`), `\mathrm{comp}(a_i)\ne\varnothing`,
a fixed finite set of primes disjoint from `P_1` (by definition of
`\mathrm{comp}`). By the already-certified Lemma XC (same file): since
`S(y)=S'` is disjoint from `S(i)=S` (hypothesis: `(S,S')` a disjoint core
pair), `\mathrm{rad}(y)\cap\mathrm{rad}(a_i)=\mathrm{comp}(y)\cap
\mathrm{comp}(a_i)` — so `\gcd(y,a_i)>1\iff\mathrm{rad}(y)\cap
\mathrm{comp}(a_i)\ne\varnothing\iff y` is divisible by some prime of
`W:=\mathrm{comp}(a_i)`. Apply Lemma WO++'s Corollary with this `W`: the
event "`y` divisible by some prime of `W`" occurs, among type-`S'`
integers in a large window, with exactly the same frequency
`1-\prod_{q\in W}(1-1/q)` as among all integers — proving the fraction is
`S'`-independent, hence `S(y)` supplies no bias. `\blacksquare`

**Interpretation.** This makes Proposition BI's "feasibility vs.
minimality" diagnosis precise in a stronger, quantitative sense: it is not
merely that no *currently certified* tool reasons about minimality — it
is that the specific data source the dispatch pointed to (CRT window
occupancy on the fixed `P_1`-alphabet, Lemma WO) is **provably incapable**
of supplying admissibility information at all, by an exact CRT-independence
argument, not a heuristic. Any minimality mechanism must use companion-
prime data (off-`P_1` information) — which is precisely the "off-`P_1`
magnitude" content that `(UB_S)`/Case-II (`theorem-UBS-false-case-II.md`)
already shows is **unbounded** for at least one core in Case II (so a
mechanism that needs to track companion primes cannot, in general, do so
within a single small fixed modulus decided in advance — the number of
distinct companion primes appearing across a class is not known to be
bounded).

### 13.3 — Proposition MO-2 (Enrichment Collapse), new, unconditional, fully proved

Theorem MO shows the pure-`P_1` route fails. The natural next attempt is
to enrich the modulus with companion primes. This subsection shows that
attempt does not produce a genuinely new, independently easier tool: it
either reproduces the target itself, or reproduces already-certified
content under a different name.

**Statement.** Fix a doubly-infinite disjoint core pair `(S,S')` and a
finite set of primes `W_0` disjoint from `P_1`. Suppose `W_0` "secures
type-`S'` admissibility against `I_S`" in the strong sense: for **every**
integer `y` with `S(y)=S'` (not merely those that happen to be actual
sequence terms) and **every** `i\in I_S`, `\mathrm{rad}(y)\cap
\mathrm{rad}(a_i)\cap W_0\ne\varnothing`. Then `W_0` is, in particular
(restricting `y` to range over the actual members of `I_{S'}` rather than
all type-`S'` integers), a covering witness set for the Stabilization
Conjecture's pair `(S,S')` in the exact sense of Theorem SW (Part 8
above): `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W_0\ne\varnothing`
for every `i\in I_S,j\in I_{S'}`.

**Proof.** Fix `i\in I_S`, `j\in I_{S'}`. Since `j\in I_{S'}`, `a_j` is by
definition an integer with `S(a_j)=S'`. The hypothesis applies to this
specific `y:=a_j` and this specific `i` (both satisfy its quantifiers "for
every `y` with `S(y)=S'`" and "for every `i\in I_S`"), giving
`\mathrm{rad}(a_j)\cap\mathrm{rad}(a_i)\cap W_0\ne\varnothing`. As `i,j`
were arbitrary members of `I_S,I_{S'}` respectively, `W_0` covers every
cross pair — the literal defining condition (Theorem SW, Part 8) of
`(S,S')` satisfying the Stabilization Conjecture with witness `W_0`.
`\blacksquare`

**Remark (why the hypothesis is not artificially strong for this
purpose).** Any tool that reasons about minimality in the manner the
dispatch describes — deciding, from CRT/residue data, which admissible
candidate the greedy will select **next**, for an *arbitrary* future
window — must in particular be able to certify, before any specific
window is reached, that *some* type-`S'` candidate in that window will be
admissible against the (a priori unknown, growing) set `I_S\cap[1,n)`;
making this certification uniform and window-independent (as a genuine
"tool," not a case-by-case numerical check) is exactly the strong
"every `y`" hypothesis above, since the tool cannot know in advance which
specific integers of type `S'` will occur in a not-yet-reached window.
So the collapse is not an artifact of an unnecessarily strong hypothesis
choice — it is the natural formalization of what "a general minimality
tool" would have to guarantee.

**Weaker version (single-candidate, not "every candidate").** If instead
one only wants "the specific candidate the greedy selects next is
admissible" (not every type-`S'` integer), this is *exactly* the shape of
fact the already-certified **Lemma WF (Witness Forcing)** and **Chaining
Sufficiency Theorem** (both certified round 13,
`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`,
`lemmas/theorem-chaining-sufficiency-and-single-witness-insufficiency.md`)
already supply, and supply *unconditionally for the whole infinite class*
`I_S`/`I_{S'}` — proved directly from Lemma P′/Lemma XC applied to a
*fixed, finite* set of low-index witnesses, with **no window-counting, no
CRT-occupancy argument, and no reasoning about "which candidate is
smallest" at all**. This is the structural reason the witness-chaining
approaches (`forced-primes-well-ordering`,
`witness-chaining-universal-existence`, `sunflower-inadmissibility-
toolkit`) have already closed concrete instances (`a_1=247`, and channels
of `4199`) **without ever needing `\mathrm{BRL}(S')`, `(PD_{S,S'})`, or
`G`-periodicity**: Lemma WF works with the sequence's *actual, realized*
members (via Lemma P′'s pairwise-intersection fact, applied to specific
computed terms), never with the space of *all a-priori candidate
integers* that a CRT-window/minimality argument would have to reason
about. Reasoning about minimality is solving a strictly harder problem
(which of *all* integers in a window gets selected) than reasoning about
realized members (what property do the terms that *do* get selected
necessarily have) — and this round's Theorem MO shows the harder problem
cannot even get off the ground using only the fixed, bounded `P_1`-
alphabet the dispatch's CRT framing offered.

### 13.4 — Honest conclusion of Part 13

**Confirmed negative result, with a full proof, not merely "not found."**
A CRT/residue-class minimality tool restricted to (or built solely from)
the `P_1`-alphabet cannot exist (Theorem MO: it is provably
admissibility-blind). A CRT/residue-class minimality tool enriched with
companion primes strong enough to be useful is not a new, independently
easier route: at full strength ("every candidate is admissible") it is
*literally* the Stabilization Conjecture itself (Proposition MO-2); at
weak strength ("some realized member has a forced property") it is
exactly the already-certified Lemma WF/Chaining Sufficiency machinery,
which needs no minimality reasoning whatsoever and has already produced
this workspace's only two fully solved concrete instances. **This retires
the specific technique family the dispatch asked this round to explore**
(bounded-modulus/CRT minimality selection, as a technique *distinct from*
witness-chaining) — the same status as `theorem-UBS-false-case-II.md`'s
retirement of the `(UB_S)` program: a genuine, rigorous, promotable
negative result, not a stalled search. `\mathrm{BRL}(S')`/`G`-eventual-
periodicity itself is **not** thereby proved false — this round does not
refute the target, only this one broad technique family for reaching it.
If `\mathrm{BRL}(S')`/`G`-periodicity is ever established, per this
round's finding it will have to be via realized-member reasoning (in the
spirit of Lemma WF, but aimed at the coarse core sequence `G` rather than
at cross-class covering) rather than via CRT-window/minimality selection
— a concrete redirection for any future round still pursuing this file's
original target, sharper than Proposition BI's own redirection.

## Part 14 (round 15) — Theorem EI (Existence-Insufficiency): closing the
"intermediate mechanism" gap the round-14 reviewer's scope correction left
open

### 14.0 The gap, precisely (recap of the round-14 reviewer's scope note)

The certification note on `lemmas/theorem-MO-minimality-obstruction.md`
(round 14) proved a genuine but incomplete dichotomy: a bounded-modulus/CRT
tool restricted to the bare `P_1`-alphabet is provably blind for a
*single fixed witness* `a_i` (Theorem MO), and a tool strong enough to
secure admissibility for *every* type-`S'` integer against *every*
`i\in I_S` collapses to being the covering-witness condition itself
(Proposition MO-2). What the reviewer flagged as **not formally ruled
out** is the genuinely intermediate shape: a fixed finite companion set
`W_0` combined with a pigeonhole/density argument establishing only that
*some* type-`S'` candidate in each window of bounded length is admissible
against the accumulated history so far — not that *every* type-`S'`
integer is admissible, and not restricted to *one* fixed prior witness.
This round's mandate is to attempt exactly this shape and report the
outcome honestly. **Outcome: a complete, rigorous impossibility proof for
this intermediate shape too (Theorem EI below), closing the gap with an
actual theorem rather than a discursive argument** — together with an
independent cross-check showing the strongest unconditional form of
"existence" this technique family can produce (Lemma FT, already
certified by the sibling `sunflower-bundle-closure` approach) is
*already established* and is *still* provably insufficient, for the same
reason.

### 14.1 Precise formalization of "intermediate mechanism"

Fix a doubly-infinite disjoint core pair `(S,S')` (both `I_S,I_{S'}`
infinite, `S\cap S'=\varnothing`). By an **intermediate bounded-modulus
mechanism** for `(S,S')` we mean: a finite set of primes `W_0` disjoint
from `P_1`, together with any argument built purely from CRT/pigeonhole
counting on the modulus `L_0\cdot\prod_{q\in W_0}q` (single-witness
counting as in Theorem MO, aggregate/union counting as in Lemma WO++, or
any combination of these), that concludes: **for infinitely many `n`,
there exists an integer `y_n>a_n` with `S(y_n)=S'` that is admissible
against `a_1,\dots,a_n`** (i.e. `\gcd(y_n,a_m)>1` for every `m\le n`) —
possibly only for a positive *fraction* of the type-`S'` integers in the
relevant window, not necessarily all of them (this is exactly what makes
it "intermediate": strictly weaker than Proposition MO-2's "every
candidate, every `i`" hypothesis, and strictly stronger in scope than
Theorem MO's "one fixed `i`" question, since it aims at admissibility
against the *entire accumulated history* `a_1,\dots,a_n`, not one term).

**Honest scope note (what this Part does and does not address).** This
formalization targets exactly the *existence* question — whether some
admissible type-`S'` candidate can be exhibited. It is emphatically **not**
the same question as the sibling `sunflower-bundle-closure` approach's
Lemma FT / Conjecture (JW) (whether a bounded prime set secures the
*joint, cross-pair* covering condition among *realized* sequence members —
see `lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`)
— that is Theorem SW's own separate, already-certified sufficiency route
to the *whole* Stabilization Conjecture, not a claim about the greedy's
selection dynamics. Part 14.6 below makes this distinction explicit and
uses Lemma FT only as an independent cross-check, not as part of the main
argument.

### 14.2 Lemma TS (Type-Symmetry) — new, unconditional, fully proved

**Statement.** Fix `i` with `S(i)=S`. Let `T\subseteq P_1` be **any**
nonempty subset with `T\cap S=\varnothing` (so `T` ranges over `S'` and
every other core type disjoint from `S`). Then, exactly as in Theorem MO,
among the type-`T` integers in any sufficiently large window, the
fraction admissible against `a_i` is exactly `1-\prod_{q\in
\mathrm{comp}(a_i)}(1-1/q)` — a value depending only on `\mathrm{comp}(a_i)`,
**not on `T`**.

**Proof.** Identical to Theorem MO's proof (Part 13.2) verbatim, with `S'`
replaced by `T` throughout: the hypothesis used there was exactly
`S(y)\cap S(a_i)=\varnothing`, i.e. `T\cap S=\varnothing` — `S'` played no
special role. By the already-certified Lemma NIDF(a),
`\mathrm{comp}(a_i)\ne\varnothing`; by the already-certified Lemma XC
(`T\cap S=\varnothing`), `\gcd(y,a_i)>1\iff y` divisible by some prime of
`W:=\mathrm{comp}(a_i)`, for any `y` with `S(y)=T`; apply Lemma WO++'s
Corollary with this `W` (which is stated for "any nonempty `S'\subseteq
P_1`," i.e. is manifestly `T`-independent in its own right) to get the
displayed fraction, identical for every choice of `T`. `\blacksquare`

**Immediate consequence.** Whatever CRT/pigeonhole argument (single-witness
or aggregate-window, cf. Lemma WO++) an intermediate mechanism uses to
certify "a positive fraction of type-`S'` integers admissible against
`a_i`," the **identical** argument, applied with `T` in place of `S'`,
certifies the same conclusion for *every* other core type `T` disjoint
from `S` — with the same window length and the same or a directly
comparable fraction (the fraction depends only on `\mathrm{comp}(a_i)`,
not on `T` at all). So a mechanism of this shape cannot single out `S'`
among its competitors at the level of a single witness `a_i`.

### 14.3 Lemma AA (Automatic Admissibility for Non-Disjoint Types) — new,
unconditional, fully proved

**Statement.** Fix `i` with `S(i)=S`, and let `T\subseteq P_1` be any
nonempty subset with `T\cap S\ne\varnothing`. Then **every** integer `z`
with `S(z)=T` satisfies `\gcd(z,a_i)>1` — unconditionally, with no
reference to `\mathrm{comp}(z)` or `\mathrm{comp}(a_i)` at all (density
`1`, not a CRT fraction `<1`).

**Proof.** Pick `p\in T\cap S` (nonempty by hypothesis). Since `S(z)=T\ni
p`, `p\mid z` (by definition of `S(\cdot)=\mathrm{rad}(\cdot)\cap P_1`).
Since `S(i)=S\ni p`, likewise `p\mid a_i`. Hence `p\mid\gcd(z,a_i)`, so
`\gcd(z,a_i)\ge p>1`. `\blacksquare`

**Reinforcing remark (not load-bearing for Theorem EI's main deduction,
included for honesty about the full competitive picture).** Taking
`T:=S` itself (always available, `S` nonempty by the doubly-infinite
pair hypothesis) shows type-`S` candidates face **zero** CRT burden at
all when it comes to admissibility against `I_S`'s own history — a
strictly stronger, unconditional guarantee than the fractional
(`<1`-density) guarantee Theorem MO/Lemma TS give type-`S'` candidates.
This does **not** mean type-`S` candidates face no burden overall — they
face the identical CRT-blind fractional burden against `I_{S'}`'s history
instead (Theorem MO with `S,S'` interchanged), so this remark is offered
only as an illustration that the technique family gives competing types
no systematic disadvantage relative to `S'`, sharpening, not replacing,
Lemma TS's symmetry point.

### 14.4 Lemma GM (Selection Is a Global Minimum) — trivial, unconditional,
stated for explicitness

**Statement.** For every `n\ge1`, `G(n+1)=T` if and only if `T=S(a_{n+1})`,
where `a_{n+1}=\min\{x>a_n:\gcd(x,a_m)>1\ \forall m\le n\}` (the problem's
own defining recursion) — i.e. `G(n+1)` is determined by which core type
achieves the **global minimum admissible integer**, minimized over **every**
positive integer greater than `a_n`, not merely over integers of one
prescribed type.

**Proof.** Immediate from the problem's definition of `a_{n+1}` and the
already-certified Theorem CD (every index has a well-defined core
`S(n):=\mathrm{rad}(a_n)\cap P_1`, so `G(n+1):=S(n+1)=S(a_{n+1})` by
definition of `G`). `\blacksquare`

### 14.5 Theorem EI (Existence-Insufficiency) — the main result, closing
the intermediate-mechanism gap

**Statement.** Fix a doubly-infinite disjoint core pair `(S,S')`. No
intermediate bounded-modulus mechanism (§14.1) — for **any** choice of
finite `W_0` disjoint from `P_1`, and **any** combination of
single-witness (Theorem MO) or aggregate-window (Lemma WO++) CRT/pigeonhole
counting — can, by itself, establish `\mathrm{BRL}(S')` or contribute to
`G`'s eventual periodicity.

**Proof.** Suppose such a mechanism `\mathcal M` exists, producing for
infinitely many `n` a type-`S'` integer `y_n>a_n` admissible against
`a_1,\dots,a_n`, via CRT/pigeonhole reasoning against (at least) the
residual constraints contributed by `I_S\cap[1,n]` (a necessary part of
full admissibility against history, since `(S,S')` disjoint means every
`i\in I_S` contributes a genuine residual constraint that cannot be
discharged via a shared `P_1` prime, by Lemma XC). Let
`\mathcal D_S:=\{T\subseteq P_1:T\ne\varnothing,\ T\cap S=\varnothing\}`
(so `S'\in\mathcal D_S`).

*Step 1 (competitors within `\mathcal D_S`).* Fix any `i\in I_S` used by
`\mathcal M`'s argument. By Lemma TS, for **every** `T\in\mathcal D_S`
(not just `S'`), the identical CRT/pigeonhole reasoning `\mathcal M` uses
to certify a positive fraction of admissible type-`S'` integers against
`a_i` equally certifies the same fraction of admissible type-`T`
integers against `a_i`, for the same window. So whatever "existence of an
admissible candidate" conclusion `\mathcal M` reaches for `S'` against
`I_S`'s residual constraints, the **same** conclusion holds, by the same
proof, for every other `T\in\mathcal D_S`.

*Step 2 (competitors intersecting `S`).* By Lemma AA, taking `T:=S`
itself (always in scope, `S\ne\varnothing`): every type-`S` integer is
**unconditionally** (density 1) admissible against every `i\in I_S` — an
even stronger guarantee than any CRT-fractional one `\mathcal M` could
produce for `S'`.

*Step 3 (no discriminating power).* By Lemma GM, `G(n+1)=S'` holds if and
only if the actual global minimum, over **every** positive integer
`x>a_n` admissible against all of `a_1,\dots,a_n`, has type `S'`
specifically. Steps 1–2 show that `\mathcal M`'s reasoning — restricted,
by construction, to CRT/pigeonhole counting on a bounded modulus `W_0` —
supplies the **identical style and (by Step 1) quantitatively identical
or (by Step 2) strictly weaker** existence guarantee for type `S'` as it
does for every other core type in `\mathcal D_S\cup\{S\}`. Since these
types are pairwise distinct possible values of `S(x)` (a single integer
`x` has exactly one core `S(x)`, by definition of `S(\cdot)`), and at most
one of them can actually achieve the global minimum at any given `n+1`,
`\mathcal M`'s existence certificate — being symmetric across all of
`\mathcal D_S` and dominated by the `T=S` case — contains **no
information whatsoever** about which type wins the minimization. In
particular it does not imply `G(n+1)=S'`, nor (iterating over a window)
does it imply any bound on how long a run avoiding `S'` can persist: for
all `\mathcal M`'s reasoning can certify, the actual global minimum could,
consistently with everything `\mathcal M` establishes, be achieved by a
type-`S` (or other `\mathcal D_S`) candidate at *every* step for
arbitrarily long, since `\mathcal M` gives type `S'` no comparative
advantage in the race for the minimum admissible integer. Hence `\mathcal
M` cannot establish `\mathrm{BRL}(S')`. **This is a statement about what
the technique `\mathcal M` can prove, not a claim that `\mathrm{BRL}(S')`
is false** — nothing here refutes `\mathrm{BRL}(S')`/`G`-periodicity, which
remain open (§11.4's numerics are still consistent with both). Moreover,
since the already-certified Lemma BRL-from-Periodicity (§11.2) shows `G`'s
eventual periodicity *implies* `\mathrm{BRL}(S')` for **every** core `S'`
with `I_{S'}` infinite (not just this one pair), any attempt to establish
`G`'s periodicity by first proving `\mathrm{BRL}(S')` class-by-class via
this technique family would need to close this same gap for every such
`S'` — and Theorem EI shows the family cannot close it for any single one,
so it cannot supply that route to periodicity either. `\blacksquare`

**What this closes, precisely.** This is the reviewer's flagged gap,
resolved. Theorem MO (single witness) is exactly the special case of
Theorem EI's Step 1 restricted to *one* fixed `i`; Proposition MO-2 (full
enrichment) is the boundary case where `\mathcal M`'s existence claim is
upgraded from "some candidate" to "every candidate, every `i`," at which
point (as already shown in Part 13.3) the mechanism ceases to be a
density/pigeonhole argument at all and becomes, by trivial specialization,
the covering-witness hypothesis itself. Theorem EI shows the entire
region **strictly between** these two extremes — any mechanism that only
ever certifies *existence* of admissible type-`S'` candidates via a
bounded modulus, whether for one witness, many witnesses, or a
window-aggregate density — is subject to the same Type-Symmetry
obstruction and hence equally powerless. **There is no genuinely
intermediate case that escapes this**: every mechanism in this family is
either (i) an existence-only claim (Theorem EI: insufficient, for the
reason above), or (ii) strong enough to force joint admissibility for
*every* candidate against *every* prior term of both classes
(Proposition MO-2: collapses to the covering-witness/Stabilization
Conjecture condition itself, a completely different, non-density
mechanism).

### 14.6 Cross-check: the strongest unconditional "existence" fact this
technique family can produce is already proved (Lemma FT), and is still
insufficient — for exactly the reason Theorem EI identifies

The sibling `sunflower-bundle-closure` approach's already-certified Lemma
FT (`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`) proves,
**unconditionally, with no density or pigeonhole heuristics at all**, that
a finite set `U_S` (built from finitely many representative indices of
`I_S`) meets `\mathrm{comp}(a_i)` for **every** `i\in I_S` — i.e. exactly
the "intermediate mechanism"'s existence goal, but established by an exact
combinatorial packing argument (greedy maximal disjoint sub-collection,
terminating by Lemma NIDF(b)) rather than a density estimate, and hence
**strictly stronger** than anything an "intermediate" CRT/pigeonhole
density mechanism could hope to produce (it is a certainty, not a
positive-fraction claim). Despite this, Lemma FT's own certification
record states explicitly that it does **not** give the Stabilization
Conjecture (Conjecture (JW) remains open: the *same* element of
`W=U_S\cup U_{S'}` need not link a given cross pair `(i,j)`). This is an
independent confirmation, from a different approach's already-certified
content, of exactly Theorem EI's diagnosis: **even the strongest available
unconditional form of "a bounded set of primes secures existence of
admissible candidates against a class's history" does not, by itself,
resolve selection-dynamics questions** (there, the cross-pair matching
question of Conjecture (JW); here, the greedy-selection question of
`\mathrm{BRL}(S')`). The two gaps are not the same question — Lemma
FT/Conjecture (JW) concerns *realized* cross pairs for Theorem SW's
covering-set route, while Theorem EI concerns the *greedy's next choice*
— but both are instances of the same underlying phenomenon: existence of
admissible material is not the same as forcing an outcome, and no
currently-certified bounded-modulus tool in this workspace bridges that
gap in either direction.

### 14.7 Honest conclusion of Part 14

**A complete, new, promotable negative result (Theorem EI), closing the
round-14 reviewer's flagged scope gap with an actual proof rather than a
discursive argument.** Combined with Theorem MO and Proposition MO-2
(round 14), this establishes a **full trichotomy with no gap remaining**:
every bounded-modulus/CRT mechanism aimed at `\mathrm{BRL}(S')`/`G`-
periodicity is (i) a single-witness existence claim (Theorem MO: blind),
(ii) an intermediate existence claim of any strength short of full
mutual coverage (Theorem EI, this round: insufficient, by Type-Symmetry
+ global-minimum reasoning — genuinely new content, not previously
formalized), or (iii) a full mutual-coverage claim (Proposition MO-2:
collapses into the Stabilization Conjecture itself, a different,
non-density mechanism already handled by Theorem SW). **This retires the
entire bounded-modulus/CRT technique family for `\mathrm{BRL}(S')`/`G`-
periodicity, completely, not just at its two previously-tested
extremes.** As with Theorem MO, this does **not** prove `\mathrm{BRL}(S')`/
`G`-periodicity false — only that this whole technique family cannot
establish it. Any future proof of the target must, per this round's and
round 14's combined finding, engage with **minimality of the greedy's
selection among competing admissible candidates of every type** — a
question about which candidate is numerically *smallest*, not which
candidates *exist* — using realized-member reasoning (in the spirit of
Lemma WF) or some other genuinely different mechanism not yet identified
in this workspace. Status remains `partial`; this file's own chain
(Theorem SW → Theorem PD-Conditional → `\mathrm{BRL}(S')`/`G`-periodicity)
is unaffected in its correctness, only its final hypothesis remains open,
now with a fully closed account of why the natural bounded-modulus
toolkit cannot supply it.

---

## Full proof
(Not present — Status is `partial`. Case (I) of Proposition D is fully
proved unconditionally (round 1, Lemma S′). Case (II) has a **complete**
conditional resolution: Theorem 5.1, "if `(\dagger')` then `a_{n+T}=a_n+L`
for every `n\ge1`," proved in full with no remaining gaps in the conditional
chain (Part 5). This round's Theorem SW (Part 8) further reduces `(\dagger')`
itself to the Stabilization Conjecture restricted to doubly-infinite
disjoint core pairs — a genuine narrowing, but that conjecture remains
unproved. The sole remaining gap for the entire problem, via this file's own
chain, is exactly: the Stabilization Conjecture (Part 8) for every
doubly-infinite disjoint core pair of `P_1`. This round's Part 9 further
narrows the Stabilization Conjecture's residual difficulty for each such
pair to exactly two precisely-stated sub-gaps — the density hypothesis
`(PD_{S,S'})`/`(PD_{S',S})`, and a reuse/pooling argument avoiding the
documented ND1/ND2 failure mode — neither closed unconditionally this
round. This round's Part 11 further narrows the density-hypothesis sub-gap
to a single, precisely-stated combinatorial hypothesis — eventual
periodicity of the coarse core sequence `G` — via the fully proved
conditional Theorem PD-Conditional (`(PD_{S,S'})` follows from `G`'s
eventual periodicity, unconditionally as an implication); `G`'s periodicity
itself, and the separate Step 5 reuse/pooling gap, both remain open. This
round's Part 12 attacks the strictly weaker sufficient target
`\mathrm{BRL}(S')` directly (per the already-certified Lemma PD-from-BRL,
`\mathrm{BRL}(S')` alone suffices, without full periodicity of `G`),
producing one new unconditional existence fact (Lemma WO) and one new
unconditional negative result (Proposition BI, ruling out companion-backbone
permanence as a sufficient mechanism) — `\mathrm{BRL}(S')` itself remains
open. This round's Part 13 sharpens Proposition BI's diagnosis into a full
impossibility proof (Theorem MO: no `P_1`-alphabet/CRT-window minimality
tool can supply admissibility information) plus a collapse result
(Proposition MO-2: any companion-enriched version of such a tool either
reproduces the Stabilization Conjecture itself or reproduces the
already-certified Lemma WF/Chaining Sufficiency machinery) — retiring an
entire technique family for `\mathrm{BRL}(S')`/`G`-periodicity without
proving or disproving the target itself, which remains open. This round's
Part 14 closes the one gap the round-14 reviewer's certification left
formally open: whether an *intermediate* bounded-modulus/CRT mechanism
(strictly between Theorem MO's single-witness case and Proposition MO-2's
full-coverage case — establishing only *existence*, not universality, of
admissible type-`S'` candidates) could succeed. Theorem EI (Existence-
Insufficiency) proves it cannot, for any such mechanism: by Lemma TS
(Type-Symmetry), the same CRT reasoning equally certifies existence of
competing candidates of every other core type disjoint from `S`, and by
Lemma AA (Automatic Admissibility), type-`S` candidates enjoy an even
stronger unconditional guarantee — so, since (Lemma GM) the actual next
term's type is decided by a global minimum over *all* core types, no such
existence certificate can bias the outcome toward `S'`. This closes the
bounded-modulus/CRT technique family completely (no remaining
untested case between the two round-14 extremes), while still not
proving or disproving `\mathrm{BRL}(S')`/`G`-periodicity itself, which
remains open — any future proof must engage with minimality of the
greedy's selection, not existence of candidates.)

## Promotable lemmas

- **Lemma A (Universal Hitting), this round, new.** *Statement.* Under
  `(\dagger')`, for every `n\ge1` and `j\ge1`, `\sigma(n)\cap\sigma(j)\ne
  \varnothing` (equivalently: every term `a_n` hits `\Sigma_\infty`, not just
  the terms it was originally defined against). Proved in full in Part 3,
  three lines, direct consequence of `(\dagger')`'s unrestricted
  quantification over all pairs. Reusable by any approach using the
  `H`-hitting framework.

- **Corollary 3.1 (Coincidence Lemma), this round, new — closes
  "Obstruction 1."** *Statement.* Under `(\dagger')`, for every `n\ge1`,
  `\min\{x>a_n:x\text{ hits }\Sigma_n\}=\min\{x>a_n:x\text{ hits
  }\Sigma_\infty\}(=a_{n+1})`. Proved in full in Part 3 from Theorem 2.2 +
  Lemma A, no induction needed. This is the key simplification that removes
  the `\Sigma_n\subsetneq\Sigma_\infty` "transient" from the whole
  construction.

- **Lemma B (single-cycle structure of `\mathrm{Good}` under `G`), this
  round, new — closes "Obstruction 2."** *Statement.* Under `(\dagger')`,
  `G` restricted to `\mathrm{Good}\subseteq\mathbb Z/L\mathbb Z` (the finite
  set of residues hitting `\Sigma_\infty`) is a bijection consisting of a
  single `\lvert\mathrm{Good}\rvert`-cycle (explicit description: the cyclic
  successor map on `\mathrm{Good}$'s sorted representatives). Proved in full
  in Part 4, elementary, no citation needed beyond basic combinatorics of
  finite cyclic order. The precise, fully-worked adaptation of crux
  `aimo-0577`'s "injectivity `\Rightarrow` no pre-period" mechanism this
  round's outline called for — with the important correction that the
  relevant injectivity is of `G` restricted to `\mathrm{Good}`, **not** of
  `G` on all of `\mathbb Z/L\mathbb Z` (false in general, toy counterexample
  given in Part 4).

- **Theorem 5.1 (Master Conditional Theorem), this round, new — the main
  result of this round.** *Statement.* If `(\dagger')` holds (finite covering
  set `H` exists), then with `L:=\mathrm{lcm}(H)`, `T:=\lvert\mathrm{Good}
  \rvert`, `a_{n+T}=a_n+L` for **every** `n\ge1` (not merely eventually), with
  `T\le L` and `L_{\mathrm{per}}=L$ exactly. Proved in full in Part 5,
  combining Corollary 3.1 and Lemma B with a telescoping-sum argument. This
  is strictly stronger than the previously-certified Theorem 2.4 (which only
  gave eventual periodicity from some `N_2`, with `T\le L` a mere bound and
  `L_{\mathrm{per}}` unspecified) — it fully resolves both Obstructions 1 and
  2 and reduces the entire remaining content of IMO 2026 P6 (Case II) to the
  single hypothesis `(\dagger')`. **Highest-priority candidate for
  certification**: any sibling approach that proves `(\dagger')` can cite
  this theorem directly to complete the whole problem.

- **Theorem SW (Stabilization Sufficiency), round 9, new.** *Statement.* If,
  for every doubly-infinite disjoint proper-core pair `\{S,S'\}` of `P_1`
  (both `I_S,I_{S'}` infinite, `S\cap S'=\varnothing`), a finite witness pool
  `W_{S,S'}` exists with `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
  W_{S,S'}\ne\varnothing` for all `i\in I_S,j\in I_{S'}`, then FCBC holds
  (via the explicit `H:=P_1\cup\bigcup H_S\cup\bigcup W_{S,S'}`, finite by
  Theorem CD's `\le2^k-1`-core bound), hence — via this file's own Theorem
  5.1 — the entire problem is solved. Proved in full in Part 8, using only
  already-certified facts (Theorem CD, Lemma P′, the certified Finite-Class
  Direct Covering lemma). This is a genuine reduction of FCBC to finitely
  many independent, individually-narrower bipartite covering questions —
  logically independent of (not proved equivalent to, only one-directionally
  related to) the round-5 Channel Assembly/Splitting machinery's
  `(LMRS_{S,S'})`, since it does not require the specific minimal-radical
  antichain to stabilize. Reusable by any future approach: closing the
  Stabilization Conjecture for even the doubly-infinite pairs of one fixed
  `a_1` (a finite, enumerable list) would, via this theorem, finish that
  instance's whole problem.

- **Lemma SW1/SW3 (automatic-coverage and peeling facts), round 9, new,
  minor but fully proved.** *Lemma SW1:* any two indices with intersecting
  cores are automatically covered by `P_1` alone (three lines from the
  definition of core). *Lemma SW3 (Peeling):* for any disjoint core pair
  `(S,S')` and any **finite** subset `F\subseteq I_S$ (not requiring `I_S`
  itself finite), `H_F:=\bigcup_{i\in F}\mathrm{rad}(a_i)` covers every pair
  `(i,j)`, `i\in F`, `j\ne i` — a strict generalization of the already-
  certified Finite-Class Direct Covering lemma's hypothesis from "all of
  `I_S`" to "any finite piece of it," same proof verbatim. Both proved in
  full in Part 8. Consequence: the open content of the Stabilization
  Conjecture, for any doubly-infinite pair, is provably confined to the
  *tail* behavior of `I_S,I_{S'}` — any finite prefix is free, for any
  choice of prefix, not just an a-priori-fixed one.

- **Numerical finding (not a lemma, but a reusable diagnostic), round 9.**
  Tested on 7 disjoint proper-core pairs across 4 distinct `a_1` values
  (`247,2747,21528751,4199,4087`), including the two `a_1` values (`4199,
  4087`) round 3 found make the *global* canonical witness set `W` very
  likely unbounded: **every single tested per-core-pair channel stabilizes
  to a tiny (`\le7`-element) witness pool, with the last-ever growth event
  occurring at a very small trigger-index** (`\le3441` out of `N` up to
  `60000`), verified by full brute-force cross-pair checking (up to
  `\approx1.9\times10^8` pairs for a single channel) with **zero**
  exceptions found anywhere. This includes an exact, independent
  explanation of sibling `explicit-window-backbone-construction`'s
  round-9 finding that `a_1=21528751` needs bridge prime `97`: the pair
  `(a_{596},a_{863})` has companion sets `\{2,3,5,7,97\}` and `\{11,97\}`,
  intersecting in exactly `\{97\}`; `a_{596}$'s core is `\{1061\}`,
  `a_{863}$'s is `\{103,197\}` — a doubly-infinite disjoint core pair,
  exactly the case this file's framing predicts is hard. Strongly suggests
  (does not prove) that the mechanism behind global-`W`'s unboundedness is
  cross-channel switching, not within-channel difficulty — a candidate
  explanation any future approach attacking the Stabilization Conjecture
  directly should account for.

- **Lemma RD (Restricted Domination Lemma), round 10, new.** *Statement.*
  For any index `m\ge1` and any nonempty `J\subseteq\{1,\dots,m-1\}`, there
  is a prime `q(J,m)\in\mathrm{rad}(a_m)` dividing at least `|J|/\omega(a_m)`
  of the `a_j`, `j\in J`. Proved in full in Part 9.1, unconditionally, using
  only the already-certified Lemma P′ (pairwise global intersection,
  `lemmas/lemma-P-prime-pairwise-intersecting.md`). A genuine, fully general
  extension of the already-certified Domination Lemma
  (`lemmas/domination-lemma.md`) from the full prefix `\{1,\dots,m-1\}` to
  an *arbitrary* subset — reusable by any future approach needing a
  pigeonhole-selected shared prime for an arbitrary earlier index subset
  (e.g. a cross-class, cross-channel, or any other restricted comparison
  set), not just the specific doubly-infinite-core-pair application made
  here.

- **Magnitude Bound Corollary, round 10, new.** *Statement.* With `q(J,m)`
  as in Lemma RD, `q(J,m)\le\omega(a_m)\cdot a_m/|J|`; combined with the
  already-certified Growth Lemma (`lemmas/lemma-1-uniform-gap-bound.md`,
  `a_m\le a_1+(m-1)\mathrm{rad}(a_1)`) and the elementary bound
  `\omega(m)\le\log_2m`, this gives the fully explicit inequality
  `q(J,m)<(a_1+L)m(\log_2(a_1+L)+\log_2m)/|J|` for every `m\ge1$ and
  nonempty `J\subseteq\{1,\dots,m-1\}`, `L:=\mathrm{rad}(a_1)`. Proved in
  full in Part 9.2. Reusable together with Lemma RD.

- **Proposition 9.4 (conditional `O(\log i)` magnitude cap), round 10,
  new.** *Statement.* For a doubly-infinite disjoint core pair `(S,S')`,
  *conditional* on the density hypothesis `(PD_{S,S'})` (`\exists c>0,i_0`
  with `|I_{S'}\cap[1,i)|\ge ci` for all `i\in I_S`, `i\ge i_0`), the
  Magnitude Bound Corollary specializes to an explicit `O(\log i)` cap
  `q(i)<K_1+K_2\log_2i` (`K_1,K_2` explicit constants depending only on
  `a_1,S,S',c`) on the pigeonhole witness prime for the pair `(S,S')` at
  index `i\in I_S`. Proved in full in Part 9.3–9.4, contingent only on
  `(PD_{S,S'})` (itself open — see Part 9.5's honest diagnosis: it is
  **not** a free consequence of Theorem CD's finite-core-count fact alone,
  by the squares/non-squares counterexample, and the workspace's one
  density toolkit, `theorem-UBS-false-case-II.md`'s Euler-divergence/
  Landau-Count machinery, cannot be repurposed here without circularity,
  since it presupposes the very periodicity Stabilization is meant to help
  establish). This is the sharpest fully-rigorous form this round's
  mechanism reaches; the density hypothesis and a Step-5 reuse/pooling
  argument (diagnosed in Part 9.6 as facing the same failure mode already
  certified in `lemmas/proposition-ND1-ND2-domination-mechanisms-
  insufficient.md`) remain open. Reusable as a conditional bridge: any
  future approach that establishes `(PD_{S,S'})`/`(PD_{S',S})` for a given
  pair by any means gets this `O(\log i)` cap for free.

- **Lemma CB (Complement Bound), round 11, new.** *Statement.* Writing
  `\mathcal T_\infty:=\{S:I_S\text{ infinite}\}` for the (fixed, finite)
  collection of infinite-class cores of a given `a_1`, and `F:=\sum_{S:I_S
  \text{ finite}}|I_S|` (a fixed finite integer), `N-F\le\sum_{S\in\mathcal
  T_\infty}|I_S\cap[1,N]|\le N` for every `N\ge1`. Proved in full in Part
  10.1, unconditionally, from Theorem CD's core partition alone (no other
  hypothesis). Cheap and reusable by any future approach needing a precise
  accounting of how much of `[1,N]` the infinite-class cores jointly
  occupy; explicitly and correctly scoped as **not** sufficient, by itself,
  to bound any *individual* class's density (documented scope note and
  counterexample-style illustration given in Part 10.1).

- **Proposition CB-2 + Corollary CB-3 (Density-Equivalence), round 11,
  new.** *Statement.* When `\mathcal T_\infty=\{S,S'\}` exactly (only two
  infinite cores), `\liminf_{i\in I_S}J_i/i=1-\overline d(I_S)$ exactly
  (`J_i:=|I_{S'}\cap[1,i)|`, `\overline d(I_S)` the upper natural density of
  `I_S` in `\mathbb N`); consequently `(PD_{S,S'})\iff\overline d(I_S)<1`.
  Proved in full in Part 10.2, via Lemma CB plus an elementary
  `\limsup`-of-a-vanishing-perturbation argument, with a companion fact
  (Corollary CB-3) identifying the pointwise-along-`I_S` quantity `\rho(i)`
  with the ordinary upper natural density. Reusable as an exact reduction
  tool: any future approach in the exactly-two-infinite-cores setting can
  invoke this to convert a two-class density question into an equivalent
  one-class upper-density question — though, per this round's own honest
  finding, this conversion alone supplies no new leverage toward actually
  bounding that one-class density, a genuine scope limitation worth stating
  alongside the lemma if certified.

- **Lemma BRL-from-Periodicity, round 12, new.** *Statement.* If the
  coarse core sequence `G(n):=\mathrm{rad}(a_n)\cap P_1` is eventually
  periodic (pre-period `n_0`, period `T`), then for every core `S'` with
  `I_{S'}` infinite, no `n_0+T+1` consecutive indices can entirely avoid
  `I_{S'}` (Bounded-Run-Length, explicit `R=n_0+T`). Proved in full in Part
  11.2, purely combinatorially from the definition of eventual periodicity
  (no dependence on `(\dagger')` or any other open hypothesis — the
  periodicity itself is taken as a hypothesis, not derived). Reusable:
  applies to *any* finite-alphabet eventually-periodic sequence, not
  specific to this problem's construction.

- **Lemma PD-from-BRL, round 12, new.** *Statement.* If `\mathrm{BRL}(S')`
  holds with constant `R`, then `|I_{S'}\cap[1,N]|\ge\lfloor N/(R+1)
  \rfloor` for every `N\ge1`, and consequently `(PD_{S,S'})` (Proposition
  9.4's hypothesis) holds for any core `S\ne S'` with explicit constants
  `c=1/(2(R+1))`, `i_0=2R+4`. Proved in full in Part 11.3, elementary
  pigeonhole on consecutive blocks of `R+1` indices. Independently checked
  by the round-12 outline-reviewer (`/tmp/round-12/outline-reviewer.md`,
  "Central finding 2") before this write-up, and re-derived here from
  scratch with full detail. Reusable: converts any bounded-run-length fact
  about a finite-alphabet sequence into an explicit positive-density bound.

- **Theorem PD-Conditional (+ Corollary), round 12, new — this round's main
  result.** *Statement.* IF the coarse core sequence `G` is eventually
  periodic for a given `a_1` (pre-period `n_0`, period `T`), THEN every
  doubly-infinite disjoint core pair `(S,S')` of that `a_1` satisfies both
  `(PD_{S,S'})` and `(PD_{S',S})` with a **uniform** constant `c=1/(2(n_0+
  T+1))` depending only on `a_1`; combined with the already-certified
  Proposition 9.4, this further gives a uniform conditional `O(\log i)`
  magnitude cap on the pigeonhole witness prime for every doubly-infinite
  disjoint pair of that `a_1`. Proved in full in Part 11.3 by combining
  Lemma BRL-from-Periodicity and Lemma PD-from-BRL. **This is a fully
  proved, unconditional implication** — the *hypothesis* (`G` eventually
  periodic) is NOT proved in general (Part 11.4–11.5: open, strong but
  non-probative numerical support on 4/5 tested instances, genuinely
  inconclusive on the 5th, and one concrete new candidate mechanism for
  proving it unconditionally — Lemma W3-based state compression — was tried
  and shown not to work using Lemma W3's own already-certified
  `|M_n|`-unboundedness fact). Reusable as a conditional bridge: any future
  approach that establishes eventual periodicity of `G` for a given `a_1`
  (by any means) gets `(PD_{S,S'})`/`(PD_{S',S})`, hence Proposition 9.4's
  `O(\log i)` magnitude cap, for every doubly-infinite disjoint pair of that
  `a_1` for free — though the separate Step 5 reuse/pooling gap (Part 9.6)
  would still remain to finish the Stabilization Conjecture.

- **Lemma WO (Window Occupancy), round 13, new.** *Statement.* Let
  `P_1=\mathrm{rad}(a_1)=\{p_1,\dots,p_k\}`, `L_0:=p_1\cdots p_k` (the same
  constant as the already-certified Lemma 1's `L`). For every integer
  `m\ge0` and every nonempty `S'\subseteq P_1`, the number of integers
  `x\in(m,m+L_0]` with `\mathrm{rad}(x)\cap P_1=S'` exactly equals
  `c_{S'}:=\prod_{p\in P_1\setminus S'}(p-1)\ge1`, independent of `m`. Proved
  in full in Part 12.1, a three-line CRT counting argument (a window of
  `L_0` consecutive integers is a complete residue system mod `L_0`, and
  the target condition is a fixed product set under the CRT bijection).
  Numerically spot-checked (`a_1=247`, `S'=\{19\}`: predicted `12`, matched
  at four independent window offsets). Reusable by any future approach
  needing an exact (not just asymptotic) count of how many integers of a
  given `P_1`-divisibility type occur in a bounded window — unconditional,
  no dependence on `(\dagger')` or any other open hypothesis.

- **Proposition BI (Backbone Permanence Does Not Force Class
  Revisitation), round 13, new.** *Statement.* If a companion prime
  `q\notin P_1` and index `N_0` satisfy `q\mid a_j` for every `j\in
  I_{S'}` with `j\ge N_0`, then for every `n\ge N_0` and every `x>a_n`
  with `q\mid x`, `\gcd(x,a_j)>1` for every `j\in I_{S'}\cap[N_0,n]`,
  *regardless of `S(x)`*. Proved in full in Part 12.3, a direct three-line
  consequence of the definition of `\gcd`. **Interpretive content (the
  valuable part):** this shows Backbone Permanence for a class `I_{S'}`
  (the sibling `sunflower-inadmissibility-toolkit`'s round-13 target, "EBS")
  — even fully established — supplies no logical obstruction forcing a run
  of consecutive indices to return to `I_{S'}`: the entire family of
  admissibility constraints `I_{S'}` contributes is uniformly dischargeable
  by any multiple of `q`, independent of core type. Consequently
  Backbone-Permanence-style feasibility mechanisms cannot be the proof
  route for Bounded-Run-Length/`G`-eventual-periodicity; any future proof
  needs a *minimality*-sensitive argument (which admissible candidate is
  numerically smallest), a category of argument no lemma currently
  certified in this workspace supplies. Reusable as a standing negative
  result: rules out an entire natural family of future attempts (any
  "companion backbone stabilizes `\Rightarrow` bounded return time" style
  argument) in one stroke, for any core `S'`, not just the two instances
  tested this round.

- **Lemma WO++ (Joint CRT Independence), round 14, new.** *Statement.* For
  any finite set of primes `W` disjoint from `P_1`, modulus `M:=L_0\cdot
  \prod_{q\in W}q`, nonempty `S'\subseteq P_1`, and any joint-residue event
  `E\subseteq\prod_{q\in W}\mathbb Z/q\mathbb Z`: every window of `M`
  consecutive integers contains exactly `c_{S'}\cdot|E|` integers with
  `P_1`-type `S'` **and** joint residue mod `W` lying in `E`, independent of
  the window's location. Proved in full in Part 13.1, a direct two-line
  extension of Lemma WO's own CRT-bijection argument to one extra coordinate
  block. Numerically verified at two independent test cases (`P_1=\{13,19\}`,
  `q=5`; `P_1=\{13,17,19\}`, `q=7`, three window offsets), exact match in
  every residue class in all cases. **Corollary (Admissibility-Blindness):**
  the fraction of type-`S'` integers in a window divisible by at least one
  prime of `W` equals `1-\prod_{q\in W}(1-1/q)`, independent of `S'` — the
  `P_1`-type carries zero information about divisibility by any fixed prime
  set disjoint from `P_1`. Reusable as a standing "the `P_1`-alphabet and
  companion-prime divisibility are CRT-independent" fact for any future
  approach considering window/CRT-based arguments on this problem's
  structure.

- **Theorem MO (Minimality Obstruction), round 14, new.** *Statement.* For
  a doubly-infinite disjoint core pair `(S,S')` and any `i\in I_S`: no
  function of `S(y)` alone (`y\bmod L_0`) determines or biases whether a
  type-`S'` candidate `y` is admissible against `a_i` — the fraction of
  type-`S'` integers admissible against `a_i` in a large window equals the
  fraction among *all* integers, `1-\prod_{q\in\mathrm{comp}(a_i)}(1-1/q)`.
  Proved in full in Part 13.2, combining the already-certified Lemma XC
  (`\mathrm{rad}(y)\cap\mathrm{rad}(a_i)=\mathrm{comp}(y)\cap\mathrm{comp}
  (a_i)` for disjoint cores) with Lemma WO++'s Corollary. Reusable as a
  standing impossibility result: rules out, with a proof rather than a
  failed search, any argument for `\mathrm{BRL}(S')`/`G`-periodicity (or
  any future problem with a similar fixed-alphabet/companion-set
  structure) built solely from the fixed `P_1`-alphabet/CRT-window data.

- **Proposition MO-2 (Enrichment Collapse), round 14, new.** *Statement.*
  If a finite prime set `W_0` (disjoint from `P_1`) secures type-`S'`
  admissibility against `I_S` for *every* integer of type `S'` (not just
  realized sequence terms), then `W_0` is, in particular restricted to the
  actual members of `I_{S'}`, exactly a covering witness set for the
  Stabilization Conjecture's pair `(S,S')` in the sense of Theorem SW.
  Proved in full in Part 13.3, a two-line specialization argument (a
  universally-quantified hypothesis over "every `y` of type `S'`" implies
  its own restriction to the subset `I_{S'}`). Reusable as a standing
  "no free lunch" result: any companion-enriched CRT/minimality tool strong
  enough to be useful for `\mathrm{BRL}(S')`/`G`-periodicity is at least as
  strong as the Stabilization Conjecture itself for that pair, so cannot
  be an independently easier route to it.

- **Lemma TS (Type-Symmetry), round 15, new.** *Statement.* Fix `i` with
  `S(i)=S`. For any nonempty `T\subseteq P_1` with `T\cap S=\varnothing`,
  among the type-`T` integers in any sufficiently large window, the
  fraction admissible against `a_i` equals `1-\prod_{q\in\mathrm{comp}
  (a_i)}(1-1/q)` — independent of `T`. Proved in full in Part 14.2, a
  verbatim generalization of Theorem MO's own proof (which never used any
  special property of `S'` beyond `S'\cap S=\varnothing`). Reusable as a
  standing "the bounded-modulus/CRT toolkit cannot distinguish between
  competing disjoint core types" fact for any future minimality/selection
  argument on this problem's structure.

- **Lemma AA (Automatic Admissibility for Non-Disjoint Types), round 15,
  new.** *Statement.* Fix `i` with `S(i)=S`. For any nonempty `T\subseteq
  P_1` with `T\cap S\ne\varnothing`, every integer `z` with `S(z)=T`
  satisfies `\gcd(z,a_i)>1` unconditionally (density 1, no CRT fraction
  needed). Proved in full in Part 14.3, a three-line argument from the
  definition of `S(\cdot)`. Reusable as a standing fact that core types
  sharing a `P_1`-prime with the current class face zero admissibility
  burden against that class's history, relevant to any future minimality
  argument comparing competing candidate types.

- **Theorem EI (Existence-Insufficiency), round 15, new — the main result
  of this round.** *Statement.* No bounded-modulus/CRT mechanism that only
  establishes *existence* (not universality) of admissible type-`S'`
  candidates against a class's accumulated history — the intermediate case
  the round-14 certification record left formally open, strictly between
  Theorem MO's single-witness case and Proposition MO-2's full-coverage
  case — can establish `\mathrm{BRL}(S')` or `G`'s eventual periodicity.
  Proved in full in Part 14.5, combining Lemma TS (the same reasoning
  equally certifies every competing disjoint core type) and Lemma AA
  (type-`S` candidates face an even stronger unconditional guarantee) with
  Lemma GM (the greedy's next term is a global minimum over *all* core
  types, so a type-symmetric existence certificate carries no
  discriminating information). Together with Theorem MO and Proposition
  MO-2, this closes the entire bounded-modulus/CRT technique family for
  `\mathrm{BRL}(S')`/`G`-periodicity with **no untested intermediate case
  remaining** — highest-priority candidate for certification alongside
  Theorem MO/Proposition MO-2, as the three together form a complete,
  exhaustive impossibility trichotomy for this technique family (though
  not a resolution of the target itself, which remains open).
