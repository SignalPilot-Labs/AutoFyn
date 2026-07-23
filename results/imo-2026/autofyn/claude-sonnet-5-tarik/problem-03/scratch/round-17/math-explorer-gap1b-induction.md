## imo-2026-03

**Lens: Gap 1b's general inductive step (Sum Bound beyond `rest=∅`).**

### Headline finding (new this round)

The general Sum-Bound induction is **not independent new content** — it is the same open
mechanism as Gap 1a's still-unproved "Deletion-Suffices-for-`k*`" / "Per-Partner Domination
Lemma" (`potential-weighting-upper-bound.md` §21.1 Step 2 / §22.2), extended to arbitrary `q`.
Concretely: at recursion level `k=|rest|`, the Sum Bound target
`w1 >= OPT_{+1}(C,rest)+OPT_{-1}(C,rest)` is **logically equivalent to** "the DELETE branch
beats-or-ties the KEEP branch" in the trichotomy computing `OPT_{+1}(C,W)` (`W=rest∪{w1}`,
`C={b0,d_{k*}}` fixed along the pure DELETE/KEEP path) — via the certified §13.2 KEEP-branch
closed form at `h=0`: `KEEP = w1 - OPT_{-1}(C,rest)`, `DELETE = OPT_{+1}(C,rest)`. That is
*exactly* the "DELETE-dominates" half of Deletion-Suffices-for-`k*` (which additionally needs
DELETE `<=` MATCH). So proving Deletion-Suffices at general `q` would hand you the Sum Bound's
inductive step (the DELETE-vs-KEEP half) essentially for free, one level down.

**Chain identity found (cheap, useful for the outliner):** since `Shrink-List` gives
`DELETE<=e(C)=D` always, and `A_{3,k*}<=DELETE` always, the top-level Deletion-Suffices claim
`A_{3,k*}=D` FORCES `DELETE=D` too, i.e. it automatically propagates one level down the pure
DELETE-chain (`D<=DELETE<=A_{3,k*}=D` forces equality throughout). So Deletion-Suffices, if ever
proved at the top of a `q`-instance, is self-propagating along the DELETE spine — but this is
internal consistency, not a proof; it does not by itself supply the general induction.

### Distinct openings
1. **Attack Deletion-Suffices-for-`k*`/Per-Partner-Domination at general `q` directly** (Gap 1a's
   own Step 2), and treat Gap 1b's inductive step as a corollary via the equivalence above, rather
   than inventing separate breakpoint machinery for Gap 1b. This merges two "3+ round stuck" gaps
   into one shared target — consistent with the "shared gap" pattern CLAUDE.md flags, except here
   the merge is a genuine simplification (fewer independent open lemmas), not a bypass.
2. **The trigger is NOT intrinsic to `(C,W)` — it references the top-level sibling `A1`, so a pure
   "P(k) holds for `(C,rest)` because P(k-1) held for `(C,rest')`" induction cannot work as stated.**
   Verified computationally (see below): even at the base case `k=0`, `h=0` alone is insufficient
   (37% failure rate without the trigger, matching round-14's own negative control); the *same*
   need for the trigger persists at `k=1` (`q=4`). Any inductive-step proof must carry the *same*
   external `A1` (or an equally powerful surrogate) through every recursion level, not just a
   locally-recomputed analog — a genuinely different structural requirement from a "clean" induction
   on list size alone.
3. **A candidate mechanism the trigger genuinely supports, worth building on:** the two "free"
   ingredients used at the base case (`A1<=b0` via Shrink-List; `A1<=|b0-w_j|` for *any* index `j`
   of the original `Z_0\{z1}`, via Step-1(†)) are available for **every** `w_j` encountered at
   **any** depth of the pure DELETE/KEEP recursion (because along that path, "the current `w1`" is
   always literally some original `z_j`, never a MATCH-derived value — MATCH only fires within the
   *same* trichotomy being analyzed, not along the outer chain). This means the base-case proof's
   two-bound contradiction argument is *available unchanged* at every depth without re-deriving
   `A1` — the obstruction is not "no bound exists," it's "the bound alone gives the Sum Bound's
   DELETE-vs-KEEP half but not DELETE-vs-MATCH," and MATCH is exactly where the recursion stops
   reducing to a smaller same-family instance (§13.2's own diagnosis: "MATCH... carries forward the
   full difficulty of the problem, unreduced, to the next level" — already flagged as the hard
   branch for Gap 1a's own general induction).
4. **Suggested inductive-step shape for the outliner, not attempted further here:** strong induction
   on `q` proving Deletion-Suffices (`A_{3,k*}=e(C)`) directly, splitting into "DELETE beats KEEP"
   (closes via the Sum-Bound-equivalent argument above, using the two free `A1`-bounds at every
   depth) and "DELETE beats MATCH" (the genuinely open, MATCH-branch-carries-full-difficulty piece —
   likely needs the half-step lemma of Gap 1c, or the Two-Touch Lemma's still-open MATCH sub-piece,
   §26.5(e) — a THIRD link between gaps, not yet recorded on file).

### Candidate technique(s)
- Strong induction on recursion depth (not flat `|rest|`), exactly as §23.3 already specifies —
  confirmed necessary, not just a formality: my q=4/q=5 experiments show the trigger's role is
  identical at every depth, so a depth-indexed strong induction carrying the *same* top-level `A1`
  forward is the right shape.
- The KEEP-branch closed form (General Rank-Extraction Identity, §13.1/§13.2) is exactly the tool
  that turns "Sum Bound" into "DELETE-vs-KEEP" — already certified, reusable without re-derivation.
- Shrink-List Monotonicity Corollary and Step-1(†) (`A1<=|b0-z_j|` for any `j`) are the two free
  bounds; both generalize unchanged to any depth (verified structurally above, not just at k=0).

### Cheap-kill candidates
- **Negative control confirms the trigger is load-bearing at every depth, not just `k=0`:** dropping
  the trigger while keeping `h=0` at `q=4` gives `10,901/29,429` (`37.0%`) failures of the
  Deletion-Suffices-style claim — a decisive, freshly-run confirmation (this round's own harness,
  not reused) that any inductive-step proof cannot drop the trigger hypothesis to simplify the
  induction; it must be carried through.
- **Branch-identification check**: in every triggered+`h0` instance sampled at `q=4,5`, `A_{3,k*}`
  is achieved by the *pure* DELETE branch (never KEEP, never MATCH) — `3118/3118` at `q=4`,
  `76/76` at `q=5`. This is a cheap sanity/pruning fact: it means a proof attempt does NOT need to
  handle "KEEP wins" or "MATCH wins" as live cases under trigger+`h0` — only needs to rule them out,
  not characterize what happens when they occur.

### Knowledge-base entries to use
- No `knowledge_base.md` generic entry surfaced as directly applicable beyond what prior rounds
  already used (Rank-Extraction/peeling-style DP arguments); the load-bearing tools are the
  problem's own certified lemmas (see below), not the generic KB.

### Certified lemmas checked for IH-compatibility
- `lemmas/three-bound-domination-and-keep-top-bound.md` (Keep-Top Bound, Three-Bound Domination):
  **usable but already fully absorbed** into the base-case proof; Keep-Top Bound generalizes to any
  `q` for free (it's literally the KEEP-branch closed form's special case) but by itself only gives
  `A_{3,k*}<=w1-D_{k*}`, not the needed lower bound — does not by itself supply new IH content.
- `lemmas/background-release-domination.md` (Background-Release Domination): **checked and does NOT
  directly supply a usable IH bound here** — its two natural chaining routes into Gap 1a were
  already refuted on file (§23.2/§24.4: full telescoping too lossy, `~38%` violations; single-release
  chain against `A1` false, `~16%` violations, concrete witness `z=[6,4,1],b0=7,l=1`). I confirmed
  by re-reading the proof that this lemma's `y` must be an actual background *element* being
  released into the list — `A1`'s relationship to `A_{3,k*}` is not of this "release one background
  element" shape (`A1` uses `z_{k*}` itself in its list, not the derived `d_{k*}`), so this lemma
  genuinely doesn't apply to bridging `A1` and the recursion depth; no new use found this round.
- `lemmas/shrink-list-monotonicity.md` and `lemmas/general-rank-extraction-identity.md` (via
  §13.2's KEEP-branch closed form): **both directly load-bearing**, as detailed above — this is
  the actual machinery the inductive step needs, not the two lemmas explicitly flagged in the
  dispatch.
- `lemmas/sum-bound-base-case.md`: confirmed (by hand and by fresh code) as exactly the `k=0`,
  `q=3` instance of the identity chain above; its "Pure Lemma" (isolated real-number fact) is a
  special case of "DELETE beats KEEP when `A1`'s two free bounds contradict the failure
  hypothesis" — worth checking whether the Pure Lemma itself has a clean higher-`k` analogue (not
  attempted this round; flagged as a concrete next experiment).

### Analogous past problems (cruxes)
Searched `combinatorics` subtopics `induction-and-construction`, `extremal-principle`,
`size-bounding-and-descent`, `processes-and-algorithms` for exchange/domination/peeling patterns.
None found is a close structural match to this problem's specific alternating-sum
DELETE/KEEP/MATCH peeling recursion with a signed background — the corpus's peeling-induction
problems (e.g. `aimo-0084`: "Strengthen the target into an induction that peels off one certified
object at a time, leaving a smaller instance of the same shape for the hypothesis"; `aimo-0012`:
pigeonhole-guaranteed pair-merge induction) share only the generic *shape* (peel-and-recurse with
IH on a smaller instance), not any exploitable technique specific to the trigger/global-argmin
scoping problem found here. **Verdict: no genuinely analogous crux found; do not force a match.**

### Prior progress
- Base case (`rest=∅`, `q=3`) fully proved (round 16), certified `lemmas/sum-bound-base-case.md`.
- General induction (`|Z_1|>=2`): **completely untouched on file until this round's probing.**
  §23.3 states the right induction variable (recursion depth) and three bookkeeping subtleties
  (argmin-tie filtering, continuous zero-slope ties, killed `max(rest)` shortcut) but no actual
  inductive-step attempt exists anywhere in the file.

### Dead ends (do not retry)
- Flat induction on `|rest|` treating `(C,rest)` as a self-contained abstract pair with only `h=0`
  as hypothesis — **confirmed this round to fail even at `k=0`** (37% counterexample rate without
  the trigger); this is not new (round 13/14's own negative controls already showed this at the
  base case), but this round newly confirms the *same* failure mode persists unchanged at `k=1`
  (`q=4`), so a hypothesis-weakening simplification will not work at any depth.
- Background-Release Domination's two chaining routes (§23.2/§24.4) — already dead, reconfirmed not
  applicable to this specific bridging problem (the `A1`/`A_{3,k*}` relationship is not a "release
  one background element" instance of that lemma).
- The killed `max(rest)` shortcut identity (§23.3 point 3, `OPT_{+1}+OPT_{-1}=max(rest)` under
  `h=0`-domination) — already confirmed FALSE on file (`306/1888` violations); do not resurrect.

### Small-case / intuition notes (all conjecture, not proof)
- **Conjecture (this round, `q=4,5` fresh evidence, 0/3118 and 0/76 violations):** under trigger
  (`A_{3,k*}<A1`, top-level `A1`) and `h=0` at `k*`, `A_{3,k*}=e(C)=D_{k*}` exactly — i.e. the base
  case's "DELETE beats KEEP" conclusion extends to "DELETE beats KEEP *and* MATCH" at `q=4,5`, not
  just `q=3`. This is the exact statement of Gap 1a's already-open Deletion-Suffices-for-`k*` /
  Per-Partner Domination conjecture (already corroborated to `q=5` with `62,500`+ checks by round
  14, without the `h=0` filter I imposed) — my fresh sample (restricted specifically to `h=0`,
  filtered by a differently-coded harness, `q=4,5`, `v_max<=6`) adds independent corroboration but
  is not a new proof and does not push past the file's already-known `q=4,5` corroboration scope.
- **Conjecture:** the Sum Bound's inductive step, if it exists, is strictly *implied by* (not
  equivalent to) proving Deletion-Suffices/Per-Partner-Domination at general `q` — so a future
  round should consider whether attacking Deletion-Suffices directly (already the field's
  "PRIORITY BUILD TARGET 1" historically, per §21.4/§23.4) is a strictly better use of effort than
  inventing separate Gap-1b-specific machinery; a single win there closes (part of) both gaps.
- All computation used exact `Fraction` arithmetic and a from-scratch brute-force `OPT_sigma`
  (full enumeration of Keep/Delete/Match selections, not the closed-form recursion), validated
  first against the file's own two worked examples (`OPT_{+1}([5,8],(10,8,7,2))=0`,
  `OPT_{-1}(\cdot)=10`) before trusting it for anything new. Code at
  `/tmp/round-17/gap1b_explore/{opt.py,q4_test.py,q4_deep.py,q5_test.py,negctrl.py}`.
