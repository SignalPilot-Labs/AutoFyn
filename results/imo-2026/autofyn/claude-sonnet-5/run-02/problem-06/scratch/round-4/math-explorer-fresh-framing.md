## imo-2026-06

- Distinct openings (my lens: hunt for a framing genuinely far from the
  persistent-type/covering-system field):

  1. **Finite-state automaton / mod-M pigeonhole** (crux corpus aimo-0678's
     second move: "once one coordinate is bounded, reduce the other mod a
     fixed M, turning the state pair into a deterministic map on a finite
     set, forcing eventual periodicity"). I traced this through carefully
     and it is **NOT actually a new framing for this problem** — it is
     isomorphic to the population's existing endgame
     (`covering-system-construction` Step 5's CRT + cyclic-pigeonhole
     finish, already unconditionally derived given (†)). The reason: to make
     "a_{n+1} is a function of a_n mod M" TRUE, M must already encode which
     primes are "load-bearing" for every persistent type — i.e. it needs
     exactly the Finite Core Theorem + persistent-type machinery the
     population already built. There is no smaller/different M that makes
     the transition literally memoryless without first solving (something
     equivalent to) gap (†). I do NOT recommend proposing this to the
     outliner as new — it would just re-derive Step 5 under new names and
     waste a build slot (matches CLAUDE.md's "technique variant, not framing
     diversity" trap already flagged in round 3 for
     minimal-counterexample-glue).

  2. **A genuinely open, different PROOF TECHNIQUE for terminating the
     recruitment process (not a bypass): round-number induction via a
     "first bad round" / reversibility-style minimality, not size-based
     well-ordering.** Both documented failed attacks on residual set V
     (`covering-system-construction` Step 4f) used well-ordering on the
     STATIC size measure |A'|+|B'| of a rogue pair, which fails because
     recruitment only ever grows that measure. Crux corpus aimo-0514
     ("assume nontermination forces a repeating state-cycle; take the
     minimal-index object acted on within the cycle; show restoring it
     requires a forbidden smaller-index action") and aimo-0077 ("assume
     nontermination forces a repeating state-cycle... minimal card number
     flipped in the cycle... contradiction from minimality") both use a
     *time/creation-order* minimality, not a size minimality: they assume
     the process runs forever (or cycles) and look at the FIRST round at
     which a specific bad event happens, then derive a contradiction from
     that round's specific transition being forced by something that should
     have already been available earlier. This is a different induction
     variable from what's been tried (round number / first-occurrence-time
     of a rogue pair type, not |A'|+|B'|) and has not been attempted on gap
     (†) yet. It stays inside the recruitment-process framing (so it is a
     technique, not a wholly new top-level target) but per CLAUDE.md this
     is worth flagging distinctly from the two already-failed size-based
     attacks, since "the wall documented in Step 4f" is specific to size
     orderings.

  3. **Direct global monotonicity claim (already flagged in run_state's
     "Next" section (b), still untried): recruitment can only ever RESOLVE
     rogue pairs, never CREATE new ones.** If provable, well-ordering on
     (number of unresolved rogue pairs) directly gives termination without
     needing the failed size-based descent on individual pairs. This is
     the single most promising still-unexplored angle inside the existing
     framework, distinct from routes 1 and 2 tried in round 3. I did not
     attempt to prove or refute it (out of scope for exploration), but flag
     it as untested and high-value.

  4. **A genuinely different top-level target I looked for and could NOT
     find a viable version of: proving a_n/n -> 1/(density) via a direct
     sieve/inclusion-exclusion argument on the acceptance sequence, entirely
     bypassing persistent types, then upgrading asymptotic density to exact
     eventual periodicity via a rigidity argument.** I could not construct
     even a plausible mechanism for the second (rigidity) step without
     re-deriving finiteness of a "core" constraint set — i.e. the same
     obstruction as route 1. I recommend NOT pursuing this; it is a dead
     end in disguise (bounded-gap + rational asymptotic density does not by
     itself force EXACT periodicity for a general local rule — e.g.
     Sturmian-type sequences have bounded gaps and well-defined rational-ish
     density-like limits without being eventually periodic — so this route
     needs the same finite-state ingredient the population already has, with
     no shortcut visible).

- Candidate technique(s): stick with the recruitment-process framing
  (already the population's best-developed target), but attack gap (†) /
  set V via route 2 (round-number / first-bad-round minimality, a
  reversibility-style argument in the style of aimo-0514/aimo-0077) or route
  3 (prove recruitment is monotone-resolving, never pair-creating) instead
  of re-trying the two size-based well-ordering routes already shown to
  fail in round 3.

- Cheap-kill candidates: none new found this round beyond what's already
  certified. (The already-certified Free Facts / Bounded Gap Lemma /
  Finite Core Theorem already dispatch the easy structural prunes.)

- Knowledge-base entries to use: `knowledge_base.md`'s "General Proof
  Methods" and "Monotone Subsequences" sections were checked — nothing new
  beyond what's already cited (pigeonhole, well-ordering, CRT) is directly
  applicable; no untapped KB entry found for this problem beyond what prior
  rounds already used.

- Analogous past problems (cruxes):
  - `aimo-0678` (IMO-SL sequences-and-recurrences / modular-arithmetic-and-CRT):
    already exploited by the population (greedy-exchange-cost-potential); I
    re-verified its 2nd crux (mod-M finite-state pigeonhole) is the same
    mechanism as the population's existing CRT finish, not a new route — do
    not re-propose it as fresh.
  - `aimo-0514` (processes-and-algorithms / invariants-and-monovariants,
    "reversible deterministic process ⇒ purely periodic, minimal-turn-in-cycle
    contradiction"): genuinely analogous in STRUCTURE (finite-state process,
    contradiction via minimality of the object acted on within an assumed
    cycle) but not directly transplantable — our process isn't obviously
    reversible. Useful as a template for route 2 above (first-bad-round
    minimality), not as a plug-in lemma.
  - `aimo-0077` (extremal-principle, "assume nontermination forces a
    repeating state-cycle; minimal-index card flipped in the cycle;
    restoring it requires a forbidden smaller-index move"): same template
    as aimo-0514, slightly closer in spirit to a "recruitment round" process
    with forced/forbidden moves. Worth the outliner's attention specifically
    for how it turns "assume infinite/cyclic recruitment" into a concrete
    minimal-witness contradiction — but the transplant is not automatic and
    would need real new work, not a citation.
  - None found that solve an isomorphic "smallest-integer-greater-than
    satisfying a gcd covering condition against ALL prior terms" problem
    directly — this exact combinatorial-number-theory setup does not appear
    to have a close analog elsewhere in the corpus (checked
    divisibility-and-gcd, sequences-and-recurrences, processes-and-algorithms
    subtopics for "greedy"/"covering system"/"eventually periodic" keywords).

- Prior progress: unchanged from `current.md` — Status partial. 12 certified
  lemmas (see current.md items 1–12), gap (†) localized to residual set V
  (rogue pairs where neither extended-persistent type is its base type's
  canonical refinement). Two size-based well-ordering attacks on V already
  failed for documented structural reasons (round 3, `covering-system-
  construction` Step 4f).

- Dead ends (do not retry): "zero further recruitment rounds" conjecture
  (falsified a_1=175, confirmed again this round — see below); "universal
  glue prime"/"cost ≤ 1" conjectures (falsified a_1=35); minimal-
  counterexample well-ordering on |A'|+|B'| (round 3, documented failure —
  measure is non-decreasing under recruitment); exchange argument using only
  the certified magnitude lemmas (round 3 "Lemma F" — only ever builds
  larger competing candidates); witness-depth-bound as scoped (RETHINK,
  round 3 — doesn't address recruitment-beyond-S₀ even if proved); the
  mod-M finite-state pigeonhole "fresh framing" I checked this round — it
  collapses into the existing Step 5 finish, not a new route, do not
  re-propose as new.

- Small-case / intuition notes (conjectural, numeric only): re-ran the
  actual greedy sequence (not the abstract recruitment model) for 9 seeds
  with 2–4 missing small primes. Confirms round 3's a_1=175 result exactly
  (T=274, L=2730=2·3·5·7·13, extra primes {2,3,13} — THREE extra primes,
  not two, exceeding |Q|=2). New data points: a_1=455 (Q={5,7,13}) needs
  extras {2,3}, T=442, L=2730; a_1=143 (Q={11,13}) needs extras {2,3},
  T=64, L=858; a_1=2310 (Q={2,3,5,7,11}, already "dense") needs zero
  extras, T=1, L=2 (trivial/degenerate — every term already shares 2).
  Two seeds, a_1=385 (Q={5,7,11}) and a_1=5005 (Q={5,7,11,13}), did NOT
  stabilize within 8000–20000 sampled gap terms / max term ~172,900 — i.e.
  the transient before periodicity kicks in can be very long for larger
  |Q|, consistent with the already-recorded rule that witness INDEX depth
  is not a function of |Q| alone. This is weak evidence (not proof) that
  the true period for wider-Q seeds may be large and/or the recruitment
  process may need several rounds — worth the outliner treating |Q|=3,4
  seeds as still-unresolved test cases rather than assuming small-|Q|
  behavior (T ~ dozens to low hundreds) generalizes. No violation of the
  recruitment-process MECHANISM was found in any seed (every case where a
  period was found matches "extra primes = recruited primes" exactly, as
  in round 3), so nothing here contradicts the framework, only reinforces
  that (†)/V needs a real proof rather than a shortcut.
