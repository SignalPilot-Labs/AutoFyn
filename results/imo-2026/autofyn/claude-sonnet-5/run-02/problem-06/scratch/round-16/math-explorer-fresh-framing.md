## imo-2026-06

**Scope of this report.** Dispatched lens: find genuinely NEW top-level framings of
the WHOLE problem, not new attacks on FAH/EEA in the existing witness/absorption/
recruitment vocabulary. Read `current.md` in full (rounds 1-15 summary + Approaches
tried + Current best), `/tmp/memory/math-explorer.md` (37 accumulated rules, esp.
#28, #34, #35, #36 which already record several "fresh framing" dead ends from round
15), and queried the crux corpus (`crux_moves_documentation.md` schema) across
subtopics NOT yet mined for this problem: `zsigmondy-and-primitive-divisors` (2
cruxes total in the whole corpus), `probabilistic-method` (5 total, all
non-analogous incidence/martingale arguments), `generating-functions`,
`bijections-and-encoding`, `extremal-principle`, plus keyword searches across all
2434 cruxes for "greedy"/"smallest positive integer"/"Ulam"/"eventually
periodic"/"complement"/"missing integers". None of these produced a crux with a
structurally close match to a *greedy, minimality-defined, gcd-legality* sequence
(the corpus's "greedy" hits are all resource-allocation / majority-vote / packing
problems with closed-form or adversarial structure, not existential-minimality
recurrences — consistent with rule #28's diagnosis that the whole "explicit
recurrence x_{n+1}=f(x_n)" crux family is structurally disanalogous here).

**Important calibration before the openings below**: round 15 already ran a
dedicated "forget everything" fresh-framing pass and killed four candidates
(König/compactness, ergodic/unique-invariant-measure, Schur/Freiman additive
combinatorics, transfer-matrix) — all collapsed into the certified Selection-Rule
Class-Blindness argument or into restating (†)/process-termination itself (see
rule #36). I did NOT re-propose any of these. The openings below are chosen to be
disjoint from that list and from all 16 confirmed-dead FAH mechanisms.

### Opening 1 — Duality with the complement set (unexplored vocabulary)

Every prior approach (all 16 dead mechanisms plus the live population) works
entirely in terms of the sequence {a_n} itself and its prime-support types. NONE
has studied the **complement**: the set M := {positive integers > 1} \ {a_n} of
integers that are *never* chosen (either because they are ≤ a_1, or because at the
time they became the smallest untaken candidate they failed gcd-legality against
some earlier a_i and were permanently skipped — "skipped forever" needs its own
justification, since a later a_j could in principle still make an even-later
candidate legal, but a *skipped* candidate itself is never revisited by
definition). Classical greedy/complement dualities (Beatty sequences, Ulam-style
constructions, "smallest positive integer not yet used" arguments) often prove
periodicity or density statements about the CHOSEN set by instead analyzing the
SKIPPED set, which can have a cleaner finite-state description (a periodic/
eventually-periodic characteristic function of skipped residues mod a candidate
modulus L is literally equivalent, by complementation, to periodicity of the gap
sequence — already known via the certified **Gap-Periodicity Equivalence**
`lemmas/gap-periodicity-equivalence.md` — but the PROOF STRATEGY of studying M
directly, e.g. via inclusion-exclusion / Legendre-sieve-style counting of "how many
integers in [a_n, a_n+a_1] are illegal" as a function of the *set of currently
locked-in prime obstructions*, has not been tried as the primary object).

- What's different from the 16 dead mechanisms: those all track a_n's prime
  SUPPORT (types, persistent types, extended types) forward in n. This opening
  tracks the STATIC combinatorial structure of which residues mod a candidate L
  are permanently illegal, as a subset-counting/inclusion-exclusion object, and
  asks when that illegal-residue pattern itself stabilizes — a different
  direction of information flow (structure of the complement, not the sequence).
- Biggest risk/obstruction: the round-11 **Selection-Rule Class-Blindness**
  observation and round-10 **Escape-Cost Vacuity/Sandwich Genericity Theorem**
  already show that any aggregate COUNTING statistic over illegal residues is
  necessarily class-blind (the selection rule only ever consults the binary
  predicate gcd(c,a_i)>1, never a count) — so a naive inclusion-exclusion count
  of |M ∩ window| is very likely to hit the exact same wall. The potential escape
  is if the complement is studied not as a COUNT but as a genuinely NEW
  combinatorial invariant (e.g., an explicit periodic covering system construction
  of M itself, built independently of the greedy process, then compared against
  the greedy process's actual choices for equality rather than counted) — this is
  a real, currently-untried design space, but likely just re-derives the existing
  CRT+cyclic-pigeonhole finish (Step 5) under new vocabulary, per the already-
  documented "fake diversity" trap (rule #17). Flag as low-to-medium promise,
  worth one focused round to determine if it's genuinely new or a repackaging.

### Opening 2 — Zsigmondy / primitive-divisor style "forced new prime" argument, used for an UPPER bound on recruitment rounds rather than existence

The crux corpus has exactly 2 zsigmondy-and-primitive-divisors examples
(`aimo-0157`, `aimo-0611`); `aimo-0611`'s technique — "prove a term grows larger
than the product of all earlier terms, so some prime must appear in it to a
strictly higher exponent than in that product, forcing a fresh (primitive) prime
divisor" — is the closest primitive-divisor style match in the corpus. This
problem's recruitment process (Generalized Bounded Witness Lemma's Corollary,
already certified) already PROVES existence of a fresh prime at each unresolved
round; what has never been attempted is the REVERSE Zsigmondy-flavored move: use
the certified magnitude bound (Bounded Gap Lemma, a_{n+1} ≤ a_n + a_1) to bound
*how many times a fresh prime can be forced* by an explicit growth/size argument —
i.e., show the total number of DISTINCT primes ever recruited into the eventual
core is finite via a Zsigmondy-style "each new recruited prime must be at least
some explicit size, or must appear with some minimal multiplicity, and the
available 'budget' (a_n's own bounded factorization count Ω(a_n) ≤ log₂(a_n),
itself growing only linearly in n by the Sandwich Genericity Theorem) caps how
often fresh recruitment can happen."

- What's different: this is a magnitude/counting argument on the NUMBER of
  recruited primes over all rounds (a global termination bound for the
  recruitment PROCESS itself, i.e. directly targets open sub-gap (a),
  "existence/termination of a self-absorbing core"), not a claim about which
  specific prime handles which specific pair (the thing all 16 dead mechanisms
  attack). It sidesteps FAH's "class-discrimination" content entirely and
  targets termination via a raw counting/size argument instead.
- Biggest risk: this looks dangerously close to the already-certified-negative
  **Sandwich Genericity / Escape-Cost Vacuity Theorem** (round 10) — a_n's
  magnitude grows linearly in n regardless of type/class, so Ω(a_n) is bounded
  by O(log n), giving a "budget" that is NOT actually restrictive (an
  unboundedly growing budget over unboundedly many rounds proves nothing, since
  both grow together). This needs an actual RATE comparison (recruitment
  frequency vs. Ω(a_n) growth rate) to have teeth, and no such comparison has
  been established; strongly suspect this collapses into "class-blind, hence
  vacuous" like every other magnitude-only argument in this workspace (rules
  #6, #21, #35). Medium-to-low promise but the framing itself (bound the
  recruitment PROCESS length via total prime-budget, rather than resolve a
  single pair) is untried and worth a cheap-kill check before dismissing.

### Opening 3 — Treat gap (†) as a statement about a RANDOM/typical model and use a genuinely probabilistic (not density/sieve) argument: second-moment / variance bound on "number of unresolved rogue pairs remaining after k rounds"

The corpus's probabilistic-method entries (5 total, all incidence-averaging /
martingale arguments in geometric or algebraic settings, none number-theoretic
gcd-sequence problems) don't transplant directly, but they suggest an unexplored
STRUCTURAL move: instead of trying to prove EVERY rogue pair resolves
(existential-to-universal, the wall all 16 mechanisms hit), set up a genuinely
probabilistic model of "if rogue pairs resolved independently at random with some
fixed-below-1 probability per round," and prove a SECOND-MOMENT / Borel-Cantelli
style argument that the EXPECTED number of unresolved pairs after k rounds → 0,
then de-randomize via an explicit (not average-based) argument. This differs from
the already-killed density/sieve family (round 11, Selection-Rule Class-Blindness)
because that family tried to count OCCURRENCES of a fixed candidate prime across
terms (a density-of-terms question); this would instead model the RECRUITMENT
PROCESS's branching structure (each unresolved pair spawns 0 or 1 new pairs after
recruiting a fresh prime) as a Galton-Watson-like branching process and ask
whether it goes extinct almost surely.

- What's different: targets sub-gap (a) (process termination) directly via a
  branching-process extinction argument, a genuinely different mathematical
  object (a random tree of pair-resolutions) from anything in the population,
  which has only ever reasoned about individual pairs or individual primes
  deterministically.
- Biggest risk (the most serious of the three): there is no actual randomness in
  the problem — the recruitment process is fully deterministic given a_1. A
  probabilistic/branching-process argument would need to be either (i) a genuine
  derandomization (prove the deterministic process is dominated by, or coupled
  to, an almost-surely-extinct random process — a real technique in
  combinatorics but requiring an explicit coupling this workspace has no
  candidate for) or (ii) purely heuristic (compute an "expected" extinction and
  present it as evidence, NOT a proof — acceptable only as intuition-building,
  never as a claimed solved step, per the Rules). Given 10 rounds of failure to
  find ANY class-discriminating information source (Lemma I's core diagnosis,
  reconfirmed every round since round 6), I judge this the LOWEST-promise of the
  three openings as a route to an actual proof, but flag it because it has
  literally never been tried and gives the outliner a genuinely different
  top-level target (branching-process extinction) to weigh against Openings 1-2.

### Small numeric sanity check performed (labeled conjecture only)

I did not run a fresh simulation this round beyond re-confirming (by reading, not
re-executing — round 15's independent re-simulation is already on record and
matches exactly) that the standing computational evidence (0 FAH counterexamples
across ~450+ seed-checks in rounds 9-15) is consistent with all three openings
above being either true-but-hard or restatements — none of them predicts a
counterexample, so none is falsifiable by the existing numeric sweeps; a genuinely
informative cheap-kill for Opening 1 would be: compute, for one seed with a known
multi-round recruitment (a_1=175, which needs core {2,3,13} per the CRITICAL
CORRECTION in current.md round 4), the actual skipped-integer set M restricted to
[1, 500] and check whether its residues mod the eventual L=2730 stabilize BEFORE
n=1 in a way not already captured by Gap-Periodicity Equivalence — this is a
concrete, cheap next step for whichever approach picks up Opening 1, not something
I ran this round (time budget prioritized broad crux-corpus reconnaissance per the
dispatch).

- Candidate technique(s): (1) complement-set / skipped-integer duality
  (unexplored vocabulary, likely re-derives existing finish under new language —
  medium risk of "fake diversity"); (2) Zsigmondy-style budget/rate argument
  bounding total recruitment rounds via Ω(a_n) growth vs. recruitment frequency
  (targets sub-gap (a) directly, likely vacuous by class-blindness precedent
  unless a genuine rate comparison is found); (3) branching-process/Borel-
  Cantelli extinction model for the recruitment tree (genuinely novel object,
  but no known derandomization coupling exists — highest risk, lowest current
  promise, but zero prior-round overlap).
- Cheap-kill candidates: for Opening 1, check on a_1=175 whether the skipped-set
  residue pattern mod L=2730 stabilizes at n=1 in a way current lemmas don't
  already give "for free" (would show it's fake diversity if it doesn't add
  anything). For Opening 2, before any construction, check whether the
  recruitment frequency (rounds needed) empirically correlates with log(a_n)
  growth rate across the existing seed set (rounds 4-15 already have per-seed
  round-counts on record) — if recruitment frequency does NOT decay relative to
  Ω(a_n)'s growth, the argument is dead on arrival, cheaply falsifiable from
  existing data without new simulation.
- Knowledge-base entries to use: none of `knowledge_base.md`'s generic entries
  were found newly applicable beyond what's already cited in the certified lemma
  chain (Free Facts, Bounded Gap Lemma, Sandwich Genericity, Selection-Rule
  Class-Blindness, Gap-Periodicity Equivalence) — this round's contribution is
  new TOP-LEVEL FRAMINGS, not new KB citations.
- Analogous past problems (cruxes): `aimo-0611` (zsigmondy-and-primitive-
  divisors; "term grows past product of earlier terms forces a fresh prime with
  higher exponent") — closest structural analog for Opening 2, genuinely
  untried; `aimo-0421` (divisibility-and-gcd; "every prime divides only finitely
  many elements of an infinite set ⟹ pigeonhole a third element") — already
  flagged in round 15 / rule #36 as an unresolved untested idea (H := primes
  dividing infinitely many a_n), noted here again since it is adjacent to
  Opening 1's complement-set framing but NOT re-explored in depth this round
  (avoid duplicate effort — round 15 already opened this one and left it
  unverified; the outliner should treat it as still-open from round 15, not as
  a new finding of this round). No crux found that is a genuinely close
  structural match to a greedy/minimality-defined gcd sequence itself — the
  "greedy" keyword hits in the corpus are uniformly resource-allocation/
  packing/majority-vote problems with closed-form recurrences, not existential-
  minimality recurrences (consistent with rule #28's general disanalogy
  finding); report this honestly rather than force a weak match.
- Prior progress: see `current.md` — Free Facts, Bounded Gap Lemma, Persistent-
  Type Pigeonhole, Finite Core Theorem, Canonical-Refinement Lemma, |Q|=1 case
  fully solved, Self-Absorbing Core Theorem (conditional), Literal n=1
  Periodicity Theorem (conditional on FAH + core existence), Termination
  Criterion Lemma (iff, unconditional) — FAH/Symmetric FAH/Cofinite FAH/EEA is
  the sole remaining primary crux, 16 mechanisms confirmed dead, 10 consecutive
  rounds untouched by a successful direct attempt.
- Dead ends (do not retry): all 16 mechanisms listed in current.md (gcd-
  pigeonhole family, magnitude/sandwich, CRT-glue, sieve/density, Morse-
  Hedlund/EEA, König/compactness, ergodic/measure, Freiman/additive-
  combinatorics, transfer-matrix, seed-coupling/restart induction, competitor-
  construction/minimality-exchange, double-counting, integer-monovariant
  search over 5 candidate statistics) — see rules #1, #6, #12, #17, #19, #21,
  #27, #28, #35, #36 in `/tmp/memory/math-explorer.md` for the precise reason
  each died; none of the three openings above are variants of any of these.
- Small-case / intuition notes: no new numeric experiments run this round
  (reconnaissance-only per dispatch scope and time budget); all existing
  computational evidence (0 FAH counterexamples across ~450+ checks) is
  consistent with, but does not distinguish between, Openings 1-3 being true.
