# Round 7 outline report (proof-outliner)

## What I read
- All three round-7 explorer reports in full
  (`math-explorer-multicompanion-induction.md`,
  `math-explorer-cross-bucket-domination.md`,
  `math-explorer-orthogonal-mechanism.md`).
- `results/imo-2026-06/current.md` in full (rounds 1–6 history).
- `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`,
  `forced-primes-well-ordering.md` (both in full), `core-depth-induction.md`
  and `imprint-automaton-periodicity.md` (open-gaps/status sections), plus
  `.ranking.json` for current Elo state.

## State of the population (Elo, from `.ranking.json`)
- `intersecting-family-covering-construction` (1688.4, "advanced," round 3) —
  fully closed on its own scope (periodicity-from-`n=1` conditional on FCBC);
  not touched, no change needed.
- `forced-primes-well-ordering` (1611.7, stale, round 6) — carries the
  Coarsening Lemma / cross-bucket-domination framing of the shared gap.
- `persistent-backbone-monovariant` (1573.9, stale, round 6) — carries the
  `Λ_S`-Reduction / Single-Companion Finiteness / Multi-Companion Reduction
  framing of the shared gap.
- `core-depth-induction` (1487.5, stale, round 6) — `|S|`-induction Step 3
  refuted; Lemma B1 survives as reusable content only.
- `explicit-window-backbone-construction` (1487.4, round 4) — Pool Lemma,
  architectural clarification, not independently pursued since.
- `imprint-automaton-periodicity` (1445.9, round 5) — same shared gap in a
  third notation (Theorem CD/Lemma TC); redundant, not rebuilt round 6.
- `bounded-gap-density-covering` (1322.0, dead-end, round 1).
- `backbone-existence-crt` (1411.5, round 1).

## What I did this round
Four file operations, all persisted (verified with `ls` — all four files
show fresh mtimes, `global-recruiter-finiteness.md` confirmed present):

1. **`persistent-backbone-monovariant.md` — revised** (new "Round 7 Outline"
   section inserted after Status, before the round-6 material). Directs the
   next builder to:
   - Certify the **Permanent Pair Lemma** (cheap — 3 lines from the already-
     certified Permanent-Inadmissibility Lemma + the contrapositive of the
     Single-Companion Finiteness Lemma): any bundle `Q=\{q_1,q_2\}` with both
     primes outside `D_S\setminus P_1` is **permanently** undominated. This
     formalizes the multicompanion explorer's proof (not just its numerics).
   - Record explicitly *why* this forecloses bundle-size induction as a
     whole family (not just this attempt) — same self-similarity mechanism
     as round 6's refuted `|S|`-induction. Explicit instruction: **do not
     attempt a third syntactic size-induction** without first hand-checking
     the self-similar-permanence obstruction on a concrete instance.
   - Pivot to the sharpened, still-open target: bound the **number** of
     distinct `D_S`-disjoint bundles ever realized for a fixed core `S` (a
     direct counting/extremal question, not an existence/induction
     argument) — per the orthogonal-mechanism explorer's own convergent
     recommendation. Explicit trap warning: do not resurrect the refuted
     Growth-Budget/Markov pointwise-vs-cumulative mechanism verbatim.

2. **`forced-primes-well-ordering.md` — revised** (new "Round 7 Outline"
   section, same insertion point). Directs the next builder to:
   - Certify the **Escape-Confinement Lemma** (unconditional, 3 lines from
     the already-certified Lemma P′): any escape from a blocked bucket is
     confined to the fixed finite companion set of the blocking witness.
   - Target proving the escape-confinement recursion has **uniformly
     bounded depth** (confirmed depth `\ge2` occurs on a concrete instance)
     — explicitly flagged as a *different* well-founded structure from the
     now-doubly-refuted size-induction family, so legitimate to pursue.
   - Explicitly told **not** to independently develop the "global recruiter
     set `W(a_1)`" idea in this file — assigned to the new approach below,
     to avoid duplicated effort — with the Step-0 tension (see below)
     flagged as belonging to that new file.

3. **`global-recruiter-finiteness.md` — new approach opened.** Builds
   directly on this round's most substantive new finding: the cross-bucket
   explorer's empirical pattern that every proper core of a fixed `a_1`
   seems to draw its eventual antichain support from the *same* small global
   set `W(a_1)`. States Hypothesis (GW) precisely, gives the (mostly-
   citation) reduction chain (GW) ⟹ whole problem via already-certified
   lemmas (Theorem CD, Lemma TC, Theorem V/V-MRS, Lemma MS, Theorem 5.1).
   **Important: I found, by cross-referencing this round's two positive
   explorer findings against each other, that (GW) as literally stated
   appears to already be in tension with — quite possibly refuted by — the
   multicompanion explorer's own data on the same `a_1=21528751`**: the
   depth-2 core `S=\{103,197\}` has `D_S\setminus P_1=\{2,3,7\}` (same bound
   as the singleton cores) yet a *provably permanent* bundle `\{11,97\}`
   (via the Permanent Pair Lemma) entirely outside that set — while the
   cross-bucket explorer's `W(21528751)=\{2,3,7\}` claim was only checked
   against singleton cores. I made this the mandatory **Step 0** of the new
   file: confirm or refute this candidate counterexample first, before any
   further development; if confirmed, pivot immediately to a depth-dependent
   weakening (`W` a function of core depth, or of nesting structure) rather
   than silently continuing to develop a hypothesis that may already be
   false. This is exactly the kind of "genuinely different framing, but
   honestly checked before being built on" the plateau-break guidance calls
   for — a global reformulation, not a new local technique (the orthogonal-
   mechanism explorer already confirmed no new local/outside technique
   exists), so it doesn't force a fake "genuinely new mechanism" where none
   was found; it's a different *route* to the same target.

4. **`core-depth-induction.md` — light cross-reference note added** (not
   rebuilt, stays parked). Records, for the historical record, that this
   round's bundle-size-induction refutation reinforces this file's own
   already-refuted `|S|`-induction finding via the same self-similarity
   mechanism — so a future round doesn't have to rediscover this connection.

`imprint-automaton-periodicity` — left untouched, stays parked as redundant
(same gap in a third notation, no new mechanism to add this round; its
Theorem CD/Lemma TC continue to be imported by the other three approaches).

## Recommended field for the outline-reviewer to rank / select a build set
- `persistent-backbone-monovariant` — revise (Permanent Pair Lemma
  certification + companion-count pivot). Real, well-defined next step.
- `forced-primes-well-ordering` — revise (Escape-Confinement Lemma
  certification + bounded-recursion-depth target). Real, well-defined next
  step.
- `global-recruiter-finiteness` — new. Higher risk/reward: Step 0 alone
  (resolve the cross-explorer tension) is a cheap, valuable, fast-fail-or-
  advance check regardless of whether the rest of the approach pans out.
- `core-depth-induction`, `imprint-automaton-periodicity` — stay parked, not
  recommended for this round's build set (no new mechanism to build on).
- Others (`intersecting-family-covering-construction`,
  `explicit-window-backbone-construction`, `backbone-existence-crt`,
  `bounded-gap-density-covering`) — no change, not recommended for build.

I did not select a formal "build set" line (that's the outline-reviewer's
job per the workflow), but the three revised/new files above are, in my
judgment, the round's live, well-motivated candidates.
