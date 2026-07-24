## imo-2026-06

### Summary of my mandate
I was asked to look for a genuinely different WHOLE-PROBLEM framing that escapes
the "existential-to-universal promotion" wall (Full Absorption Hypothesis / FAH)
that has killed all 9 prior mechanisms inside the covering-system-construction
skeleton. Conclusion up front: **every one of the four specific bypass ideas in my
dispatch brief (bounded-gap finite-state pigeonhole, ultrafilter/compactness,
crux-corpus transplant, smarter finite-state pigeonhole) has already been tried in
this workspace under a different name and independently shown to be either (a)
provably equivalent to the open gap, or (b) refuted by an explicit counterexample.**
I did find one angle that is NOT yet tried in this exact form — a quantitative
(size/density) rather than qualitative (existential pigeonhole) attack on FAH itself
— but it stays inside the same overall skeleton (it targets the same Successor
Claim / Cofinite-FAH target, just with new evidence). I am reporting this honestly
rather than forcing a "new framing" that doesn't actually exist.

### Distinct openings actually examined this round

1. **Finite-state / de Bruijn pigeonhole on a_n mod a fixed modulus (dispatch idea
   (a)/(d)).** Already attempted and FULLY RESOLVED as a dead bypass: see
   `approaches/reversible-transition-map.md` (round 5). It proves, both directions,
   that for ANY fixed finite prime set S ⊇ S₀, "S-sufficiency" (the finite-state
   transition map built from `a_n mod ∏_{p∈S}p` accurately describing the true
   greedy rule for large n) is **logically equivalent** to "V = ∅ at level S" —
   i.e., exactly gap (†) restated in automaton language, not a different or easier
   claim. The reason is structural, not an artifact of a bad choice of state: the
   true legality condition at step n is "gcd(c,a_i)>1 for ALL i=1..n" — an
   unboundedly-growing conjunction — and the only way anyone has found to compress
   it to a bounded amount of state is exactly the core-prime-recruitment argument
   already in the population. No smarter choice of finite state escapes this,
   because whatever finite alphabet you pick, "sufficiency of that alphabet"
   unpacks to exactly the same intersection condition. **Do not re-propose this
   lens; it is closed, not merely stalled.**

2. **Compactness / ultrafilter argument on "possible local pictures" (dispatch idea
   (b)).** No existing approach in the corpus attempts a literal ultrafilter/
   topological-compactness argument, but on inspection it reduces to the same wall:
   any compactness argument here would need the space of "signatures relative to a
   fixed finite prime set" to be compact (it is — it's finite) and would need the
   transition rule on that space to be well-defined, which is exactly the
   S-sufficiency question shown equivalent to (†) in point 1. Compactness doesn't
   supply new information about WHICH finite core is sufficient; it only formalizes
   "if a sufficient finite core exists, periodicity follows," which is already
   the certified Step 5 CRT finish in `covering-system-construction`. This is not a
   new route, just a different vocabulary for the already-certified finish.

3. **A fixed-pool / bounded-witness-factorization bound on how many NEW primes can
   ever be recruited (my own candidate reduction, independently reconstructed
   before I found it was already tried).** Idea: if a base-type pair's rogue
   extended-refinements could always be witnessed using a SINGLE fixed integer's
   factorization (e.g. the canonical earliest-occurrence witness a_{m_B}), then only
   finitely many primes (⊆ P(a_{m_B})) could EVER be recruited for that pair, giving
   termination directly, bypassing FAH. **This is exactly what round 9's
   `covering-system-construction` "Recruitment-Budget Lemma" (a global fixed pool
   W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B})) already proposed and it was REFUTED with an
   explicit, independently-reconfirmed counterexample**: a_1=209, recruitment round
   2 forces prime q=7 which lies outside W_{A,B}={2,3,5,11,19} (reconfirmed by the
   reviewer's own from-scratch reimplementation; a second escape found on a_1=247).
   The reason it fails: only the *canonical* extended refinement of a base type has
   a witness whose factorization is fixed a priori (this is exactly what the
   certified **Canonical-Refinement Lemma** already handles unconditionally); the
   genuinely open "rogue" case V is, by definition, precisely the case where NEITHER
   side is canonical, so the relevant witness is a refinement discovered arbitrarily
   deep in the recruitment history, with no a priori bound on its factorization.
   **Do not re-propose a fixed-pool / bounded-witness-set bypass; it is refuted, not
   merely stalled.**

4. **Crux-corpus transplant search (dispatch idea (c)).** Queried both
   `past_crux_moves_database.json` and `past_problems_database.json` per
   `crux_moves_documentation.md`'s field names (`technique`, `how_used`, `domain`,
   `subtopic`; `problem`, `solutions`). Searched NT subtopics
   `sequences-and-recurrences`, `p-adic-valuation`, `divisibility-and-gcd`,
   `invariants-and-monovariants`, plus combinatorics `processes-and-algorithms`
   and `invariants-and-monovariants`, for keywords `greedy`, `periodic`,
   `eventually periodic`, `all previous`/`all earlier`, `shares a prime`/`shares a
   factor`. Two closest hits, both **already known to the population and already
   ruled out as templates**:
   - `aimo-0678` (NT, `modular-arithmetic-and-CRT`): "Once one coordinate of a
     coupled integer recurrence is bounded, reduce the other coordinate modulo the
     lcm of the bounded coordinate's attainable values, turning the state pair into
     a deterministic map on a finite set." This is the literal "reduce to a finite
     automaton" template — round 7's `covering-system-construction` explicitly
     attempted an "aimo-0678-style algebraic-recursion transplant" and it was
     REFUTED by an exact counterexample plus a general structural argument
     (**Witness Discontinuity Obstruction**, certified in
     `lemmas/witness-discontinuity-obstruction.md`, though I did not re-open that
     file this round — flagged by name in `current.md` round 7 section). Consistent
     with finding 1 above: the "bounded coordinate ⟹ finite state" trick needs the
     boundedness to be established INDEPENDENT of the recruitment process, which is
     circular here.
   - `aimo-0514` (combinatorics, `processes-and-algorithms` /
     `invariants-and-monovariants`): "Show a deterministic process is reversible so
     its state graph is a union of cycles, forcing the orbit to be purely periodic
     rather than eventually periodic" — the classic finite-bijection-⟹-pure-cycles
     template. This is precisely the template `reversible-transition-map` (finding
     1) tried to import; it was shown to need S-sufficiency as a hypothesis (which
     is (†) itself for the primary target) and, even granting (†) for the tail, to
     face a genuinely separate obstruction for extending periodicity back to n=1
     (early terms face a strictly weaker legality constraint than eventual-regime
     terms, so they need not lie on the eventual cycle) — this secondary-gap framing
     is still open and is a legitimate small independent target, but it is not a
     route to the primary FAH gap.
   - No other crux in the corpus (searched ~109 candidates matching
     periodic/greedy keywords, and specifically for "gcd with all previous terms"
     constructions) resembles this problem's actual structure (an infinite greedy
     sequence whose legality is a conjunction against ALL prior terms, not a
     bounded-lookback recurrence). `aimo-0503` ("gcd of consecutive terms exceeds
     the preceding term") looked promising by keyword match but is a different
     constraint (only consecutive pairs, not all-pairs) — not genuinely analogous,
     flagging so no one wastes a round on it.
   - Conclusion: **the crux corpus has nothing that transplants past the
     already-tried finite-automaton idea.** No new match to report beyond what's
     already been tried and killed.

### The one genuinely under-explored angle (not previously tried in this exact
    form, but stays inside the current skeleton — offered as a possible new
    sub-mechanism, not a new top-level framing)

Round 9 certified two conditional reduction lemmas that both still need an open
hypothesis: **Cofinite Sufficiency Lemma** (`lemmas/cofinite-sufficiency-lemma.md`,
weakens literal FAH to "all but finitely many occurrences," still sufficient for the
finish) and **Successor-Transport Reduction Lemma**
(`lemmas/successor-transport-reduction-lemma.md`, reduces Cofinite FAH to a bare
"eventual one-step successor implication," the **Successor Claim**: q*|a_{n_j} ⟹
q*|a_{n_{j+1}} for all large j, where n_1<n_2<... enumerate A'-type occurrences).
Both routes tried to prove the Successor Claim via the EXISTING qualitative toolkit
(Critical Prime Dichotomy, Free Facts) and stalled at the same wall. **Nobody has
tried a quantitative/size argument specifically for the Successor Claim**: using the
certified Generalized Bounded Gap Lemma (a_{n+1} ≤ a_n + c for any c divisible by
every prime of Q, in particular a_{n+1} ≤ a_n + a_1·q*), one could try to bound how
many CONSECUTIVE A'-type occurrences can fail to be divisible by q* by a counting
argument over the bounded "room" between consecutive A'-occurrences (values, not
just indices, since a_n = O(n) by the Bounded Gap Lemma) — i.e. attempt to show that
failing divisibility by q* at n_j forces n_{j+1} - n_j (or a_{n_{j+1}} - a_{n_j}) to
be anomalously large, and that this can only happen finitely often by a growth/
counting bound, giving the Successor Claim (or Cofinite FAH directly) via a
Zsigmondy-style "growth outpaces the escape budget" argument (cf. crux `aimo-0611`'s
technique: "prove a term grows larger than the product of all earlier terms, so
some prime must appear to a strictly higher exponent" — same flavor of
size-forces-divisibility argument, though aimo-0611's problem is different in
substance). This is **speculative and unverified — I did not attempt to carry it
out** (per my mandate, I do not develop ideas into steps); flagging it only because
it is a genuinely unexplored SOURCE of information (magnitude/counting, not another
recombination of the four existential tools Lemma I already showed to be
insufficient) that could feed the Successor Claim without hitting the same
existential-to-universal wall, since it would supply a DIRECT finiteness bound on
exceptions rather than an infinite-pigeonhole existence statement.

### Candidate technique(s)
- The certified reduction chain (Cofinite Sufficiency + Successor-Transport) remains
  the sharpest currently-open target; any new mechanism should aim at the Successor
  Claim specifically.
- If a quantitative/counting argument (bounding exception density via the Bounded
  Gap Lemma family) is attempted, name it explicitly as distinct from the four
  tools Lemma I already ruled out (Free Facts, Generalized Bounded Witness Lemma,
  the Gap Lemmas used qualitatively, Critical Prime Dichotomy) — it must use the
  Gap Lemmas QUANTITATIVELY (as a numeric bound on room/density), not just as an
  existence statement, to actually be new content.

### Cheap-kill candidates
- Before any new mechanism, computationally test whether the Successor Claim's
  failure set (`E` in the Cofinite Sufficiency Lemma) has bounded SIZE (not just
  "empirically empty") across the existing |F'|≥2 seeds — e.g. is |E| ≤ some small
  constant like 1 or 2 across all tested seeds? If |E| is always tiny, a
  quantitative bound (rather than an existence-style proof) might be tractable and
  cheap to state precisely. This is a data-gathering cheap-kill, not a proof
  attempt — worth 5 minutes of compute before committing a round to it.
- None of the four dispatch-brief bypass ideas survive as cheap kills on their own
  merits — all four are already dead per the findings above; don't re-spend a
  round re-verifying them.

### Knowledge-base entries to use
- `knowledge_base.md`: "Order of an element, Fermat/Euler: periodicity of aⁿ mod m"
  and "Zsigmondy's theorem" entries — both already flagged in the workspace as
  candidates; Zsigmondy's specific growth-forces-new-prime flavor is the closest KB
  entry in spirit to the quantitative idea above (though Zsigmondy itself doesn't
  apply directly — no aⁿ−bⁿ structure here).
- No other KB entry looks newly relevant beyond what's already cited in the
  certified lemma stack (pigeonhole/extremal principle, CRT).

### Analogous past problems (cruxes)
- `aimo-0678` (NT, modular-arithmetic-and-CRT) — "bounded coordinate ⟹ finite
  automaton" template; ALREADY TRIED (round 7) and refuted (Witness Discontinuity
  Obstruction). Do not retry.
- `aimo-0514` (combinatorics, processes-and-algorithms/invariants-and-monovariants)
  — "reversible deterministic finite map ⟹ pure cycles" template; ALREADY TRIED
  (round 5, `reversible-transition-map`) and shown equivalent to (†) for the primary
  gap, with a separate genuine obstruction identified for the secondary "periodicity
  from n=1" gap. Do not retry as a primary-gap route; could be revisited ONLY for
  the secondary gap once (†) is closed.
- `aimo-0611` (NT, zsigmondy-and-primitive-divisors) — "term grows larger than
  product of all earlier terms ⟹ new prime at higher exponent" — not directly
  transplantable (different problem structure) but the closest KB-adjacent flavor
  to the quantitative Successor Claim idea sketched above; not previously tried in
  this workspace in this specific application.
- No other crux in the corpus is genuinely analogous; searched broadly (see above),
  found nothing else worth reporting.

### Prior progress
Unconditional (independent of the open gap), current best per `current.md`:
Free Facts, Bounded/Generalized Bounded Gap Lemmas, Persistent-Type Pigeonhole,
Bounded/Generalized Bounded Witness Lemmas, Finite Core Theorem, Extended
Persistent-Type Pigeonhole, Canonical-Refinement Lemma, F_A∩F_B≠∅,
Projection Lemma, Collateral-Safety Theorem (gap (†) reduced exactly to base-type-
pair-level termination over a FIXED finite index set, with open(k) provably
non-increasing), Cofinite Sufficiency Lemma, Confined-GCD Lemma, Successor-Transport
Reduction Lemma, Same-Type Free Facts Vacuity. The single remaining crux is FAH /
Cofinite FAH / the Successor Claim (three equivalent-in-strength formulations at
decreasing cost, all still open).

### Dead ends (do not retry)
- Finite-automaton / bounded-coordinate-mod-lcm bypass (any form): proven
  EQUIVALENT to (†), not a bypass (`reversible-transition-map`, round 5). Includes
  the `aimo-0678` and `aimo-0514` transplant templates specifically.
- Fixed-pool / bounded-witness-factorization global recruitment bound (any form):
  REFUTED by explicit counterexample (a_1=209, a_1=247) — `covering-system-
  construction`'s round 9 Recruitment-Budget Lemma, independently reconfirmed by
  the reviewer.
- All 9 prior FAH mechanisms (see `current.md` "Approaches tried" for the full
  list back to round 1) — all stall at the same existential-to-universal promotion
  wall; do not recombine Free Facts / Generalized Bounded Witness Lemma / Gap
  Lemmas (used qualitatively) / Critical Prime Dichotomy — Lemma I (round 6,
  `greedy-exchange-cost-potential`, not separately certified but recorded as
  guidance) shows no composition of exactly these four tools can promote an
  existential "some prime works" to a universal "this specific prime always works."
- "Charging" strategies against ω(a_1)/Ω(a_1) or against O(n) growth rate
  (`recruitment-round-charging`, round 6): both confirmed dead ends (recruited
  primes need not divide a_1; bounded per-term factorization size is compatible
  with unboundedly many distinct primes across terms).

### Small-case / intuition notes (conjecture only)
- FAH and Symmetric FAH have 0 counterexamples across 550+ seeds tested by five
  independent implementations (builders + reviewers across rounds 6–9), including
  the critical |F'|≥2 regime. This is very strong evidence the target claim is TRUE,
  but per CLAUDE.md rigor rules this remains a conjecture, not a proof — the
  population's problem is entirely proof-technique, not correctness of the target.
- My own reconstruction of the "fixed witness pool" idea (before discovering it was
  already tried) independently arrived at the same natural-but-wrong idea as round
  9's Recruitment-Budget Lemma — this is a mild piece of evidence that the
  population has now covered the "obvious" bypass ideas fairly exhaustively, and
  that closing this gap likely needs either (i) the quantitative Successor Claim
  angle sketched above, or (ii) an idea from outside the standard toolkit entirely
  (e.g. an analytic density/equidistribution argument on the primes recruited,
  which no approach has attempted).
