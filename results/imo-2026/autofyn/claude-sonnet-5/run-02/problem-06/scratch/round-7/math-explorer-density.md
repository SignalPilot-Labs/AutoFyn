## imo-2026-06 (lens: density / growth-rate argument for FAH)

### Summary verdict up front
I could NOT find a genuine density/growth-rate mechanism that forces FAH (or Symmetric
FAH). Worse: a naive probabilistic/density heuristic actually argues *against* FAH being
true "by accident" (see below) — which is itself useful negative information: it tells
the outliner that the missing ingredient is a deterministic, structural fact, not a
counting/density estimate, and explains why growth-rate charging (already RETHINK'd
round 6) and Lemma I's diagnosis are the right read. However, in the course of testing
growth/size-based candidate mechanisms I found one genuinely NEW, unreported empirical
regularity — the "Two-Witness Intersection is a Singleton" phenomenon — that is a
counting/extremal fact in the spirit of the dispatch's "pigeonhole on the greedy
selection rule" suggestion, distinct from anything in Lemma I's scope, and worth
surfacing as a concrete next target even though I did not find a proof of it either.

### 1. Why naive density/probabilistic heuristics point the WRONG way
If a_n's prime factorization behaved like a "generic" integer of its size, the
probability that a SPECIFIC prime p divides a_n is heuristically ~1/p (Mertens-type). A
density argument built on this model would predict that the Lemma-G prime q divides only
a small, bounded-away-from-1 fraction of A'-occurrences (roughly 1/q), not literally
100%. But round 6's own explorer note (echoed in the dispatch) and my own numeric checks
(below) show q divides ~100% of A'-occurrences after n_B, while OTHER primes of F' (the
"junk" companions) divide only a small fraction (~1-10%) — i.e. the asymmetry between q
and its F'-companions is exactly the OPPOSITE of what a probabilistic/density model would
predict for q (100% is astronomically higher than any generic 1/p heuristic), while it
IS roughly consistent with a generic model for the junk primes. This means: whatever
forces q's universal presence is a genuine structural/deterministic fact about the greedy
rule, not decodable via density/growth heuristics — a density argument is at best capable
of explaining the LOW frequency of junk primes, never the high (literally 100%) frequency
of q. I recommend the outliner NOT dispatch a "density-one" or "positive density"
argument as a standalone route to FAH: even a full proof of "q divides a density-1 subset
of A'-occurrences" would be weaker than FAH (which needs literally EVERY occurrence, no
exceptions — confirmed empirically with 0 counterexamples across every occurrence
checked, not just a density-1 subset) and would not close the finish in Step 8.5, which
needs the cofinite/complete form to conclude ρ₁(n) = A'∪{q} for literally every large n
(a single missed occurrence would keep an infinite exceptional class alive at the refined
level, reopening the same collateral-rogue-pair machinery Step 8.2 was built to shut off).

### 2. Growth-rate (a_n = O(n)) does not by itself bound recruitment or pin q
Reconfirmed (not re-derived, just re-checked) that the two growth-rate charging
candidates from round 6's `recruitment-round-charging` (charging against Ω(a_1)/ω(a_1),
charging against a_n=O(n)) are correctly dead ends — a bounded per-term factorization
size (O(log N) prime factors up to index N) is compatible with unboundedly many DISTINCT
primes recurring across different terms, and says nothing about which specific prime
recurs. I did not find a repair. This confirms round 6's RETHINK verdict rather than
opening a new angle.

### 3. New empirical finding: Two-Witness Intersection is always a singleton
(This is NEW — not reported in current.md, Lemma I, or any approach file I read.)

For a rogue pair (A', B') with n_A < n_B the two EARLIEST-occurrence witnesses (as in
Lemma G / the FAH statement), define F' := P(a_{n_B}) \ S₀ and F'' := P(a_{n_A}) \ S₀
(both finite; Lemma G already guarantees F' ∩ F'' ≠ ∅). I tested, across 10 seeds with
known rogue pairs (175, 187, 209, 247, 385, 4807, 11305, 1547, 2431, 3689, 6851 — 34
distinct rogue-pair instances total, re-simulated from scratch with trial-division
factorization, not reusing any prior agent's code) whether **|F' ∩ F''| = 1 always**,
even in the cases where |F'| or |F''| individually is ≥ 2 (i.e. exactly the cases the
falsified Universal Singleton Hypothesis said couldn't be controlled). Result: **|F' ∩
F''| = 1 in all 34/34 instances, zero exceptions**, including:
- a_1=11305: F'={11,103} (|F'|=2), F''={11} (|F''|=1), F'∩F''={11} — a singleton even
  though F' alone is not.
- a_1=6851 (multiple pairs): F'={5,23}, F''={5,23} or {5}; F'∩F''={5} always.
- The a_1=4807 case matching current.md's own numbers (A'={3,5,19}, B'={2,11}): recomputed
  independently — F'=P(a_{n_B})\S₀={13,17}, F''=P(a_{n_A})\S₀={17}, F'∩F''={17}=singleton,
  and this q=17 is NOT min(F')=13 nor obviously distinguished by size — ruling out a
  simple "q = smallest/largest prime of F'" characterization (checked directly; ordinary
  magnitude comparison of the primes in F' does not pick out q).

I also tested this at NON-earliest witness pairs (any occurrence of A', any occurrence of
B', not just the earliest of each): |F_a ∩ F_b| is usually still 1 but occasionally 2 (0
times empty — consistent with FAH) — so the EARLIEST-witness version is measurably
special/sharper than the general pairwise version, not just a restatement of "usually
singleton."

**Why this might matter (one-line idea only, not developed into a proof — per
instructions I stop here):** this "Two-Witness Intersection Uniqueness" fact, if proved,
would give an unambiguous, canonically-defined q with no arbitrary choice (unlike Lemma
G's proof, which only picks "some" shared prime) — a genuinely different kind of fact
than anything in the certified toolkit (Free Facts/Generalized Bounded Witness/Gap
Lemmas/Lemma H only ever produce existential "∃ shared prime" statements per Lemma I's
diagnosis; this is instead a claim about the SIZE of an intersection of two finite sets
derived from two DIFFERENT witnesses, which is a new type of statement not covered by
Lemma I's inspection). It does NOT by itself close FAH (uniqueness at the two earliest
witnesses says nothing yet about occurrence n_B+1000), but it is a concrete, narrower,
fully checkable target that a future approach could attempt as a first new certified
building block, genuinely distinct from Attempts 2a-2c.

### 4. Crux corpus check (per dispatch instruction)
Filtered `past_crux_moves_database.json` by domain=number_theory, subtopics
{p-adic-valuation, sequences-and-recurrences, processes-and-algorithms,
divisibility-and-gcd} for "eventually all / density-one / cofinite" language. Found one
genuinely analogous problem: **aimo-0477** (Mongolia, "sum of consecutive ratios is an
integer for n≥k ⟹ sequence eventually constant"). Its crux move: track d_n :=
gcd(a_1,a_n); show d_n | d_{n+1} (monotone) and d_n ≤ a_1 (bounded) ⟹ eventually constant
by a bounded-monotone-integer-sequence argument; its alternate solution runs the same
idea per-prime via v_p valuations, using the integrality of the specific algebraic
expression to force v_p(a_{n+1}) into a one-sided inequality relative to v_p(a_n) and
v_p(a_1) at EVERY step (not just infinitely often).

**I tested whether this transfers, and it does NOT, for a specific reason (recorded so
it isn't re-tried).** I directly computed gcd(a_{n_B}, a_n) for successive A'-occurrences
n (using the earliest B'-witness a_{n_B} as the fixed reference, mirroring aimo-0477's
gcd(a_1,a_n)) on a_1=6851's rogue pairs. Unlike aimo-0477's d_n, this quantity is **NOT
monotone**: it is usually exactly q (=5), but occasionally jumps up to a multiple of q by
a junk prime (5→115=5·23→5 again, 5→265=5·53→5 again) — i.e. it fluctuates rather than
climbing to and staying at a ceiling. The reason aimo-0477's trick works and this
problem's doesn't: aimo-0477's monotonicity comes from a precise ALGEBRAIC identity (the
partial-sum expression's integrality forces a strict one-sided valuation inequality at
EVERY consecutive step n→n+1, an "if valuation drops, the sum can't be an integer"
argument). This problem's only tool (Free Facts: gcd(a_i,a_j)>1) is a much weaker,
purely EXISTENTIAL pairwise fact with no such recursive step-to-step algebraic relation —
there is no analogue of "the sum is an integer" linking consecutive A'-occurrences'
valuations. This is a genuinely new (if negative) transfer-attempt result, distinct from
Lemma I (which only inspects the FOUR already-certified in-workspace tools, not external
crux techniques) — I recommend recording it so a future round does not re-attempt
importing aimo-0477's monotone-valuation trick verbatim.

No other corpus entry in the searched subtopics looked genuinely analogous (most
"eventually" results in the corpus rely on an algebraic recursion/identity this
problem's greedy-minimality condition does not supply).

### Cheap-kill / structural checks tried
- Checked whether q = min(F') or max(F') (a cheap size-based rule): FALSE in general
  (a_1=4807: F'={13,17}, q=17≠min). Rules out any simple magnitude ordering as the
  selection mechanism for q — supports point 1's conclusion that no growth/size
  heuristic determines q.
- Checked whether Ω(a_n) or ω(a_n) growth trends correlate with A'-persistence density:
  not pursued further after confirming (point 2) this reduces to the already-RETHINK'd
  charging candidates.

### Candidate technique(s) for the outliner
- NOT density-one / positive-density arguments (shown insufficient in strength even if
  provable, point 1).
- NOT growth-rate charging (confirmed dead end again, point 2).
- A genuinely new candidate: attempt to prove **"Two-Witness Intersection Uniqueness"**
  (|F' ∩ F''| = 1 at the two earliest-occurrence witnesses of a rogue pair) as a
  standalone lemma — untested by any prior round, empirically bulletproof (34/34), and
  structurally different in kind from the four tools Lemma I shows are insufficient
  (it's a size-of-intersection claim between two DIFFERENT witnesses' factor sets, not an
  existential-per-occurrence or magnitude-per-integer statement). Even if proved, note
  honestly: the further step from "the two earliest witnesses have unique intersection"
  to "every later occurrence carries that same prime" (FAH itself) is NOT bridged by this
  finding and would need its own new argument — flag this gap explicitly to whoever
  attempts it, do not let it be presented as a full route to FAH.

### Knowledge-base entries used
Pigeonhole / extremal principle, CRT / modular arithmetic (both already central to the
live approaches; no new KB entry looks applicable to a density mechanism specifically —
`knowledge_base.md` has no dedicated density/asymptotic-domination entry for number
theory sequences).

### Analogous past problems (cruxes)
- `aimo-0477` (Mongolia, sequences-and-recurrences / p-adic-valuation) — closest
  analogue for "prove eventual stabilization of a divisibility/valuation pattern," but
  its monotone-valuation mechanism does NOT transfer (tested and shown to fail, see
  section 4) because it relies on an algebraic recursion (sum integrality) this problem's
  weaker pairwise-gcd hypothesis does not supply.
- No other corpus entry in the searched subtopics (p-adic-valuation,
  sequences-and-recurrences, processes-and-algorithms, divisibility-and-gcd) looked
  genuinely analogous beyond generic "eventually constant sequence" framing already
  covered above.

### Prior progress
As recorded in current.md: (†) is unconditionally reduced (Projection Lemma +
Collateral-Safety Theorem, round 6, certified) to base-type-pair-level termination, which
in turn reduces (Step 8.5, conditional) to FAH + Symmetric FAH. FAH is empirically
bulletproof (0 counterexamples across every instance checked by any agent, now also by
me: 34 rogue-pair instances across 10 seeds, checked over the full generated index range,
0 failures on either side) but unproved; three proof mechanisms (Lemma H branch analysis,
inductive chaining, exchange/minimality) are shown to fail via Lemma I.

### Dead ends (do not retry)
- Universal Singleton Hypothesis, "V=∅ always," PUCL, universal-glue-prime/cost≤1,
  reversible-transition-map bypass, well-ordering descent on witness-index/set-size
  measures, recruitment-round-charging's 3 candidates (all per current.md, reconfirmed
  not re-litigated).
- NEW this round: a "density-one" or "positive-density" weakening of FAG/FAH as a
  standalone target — even if provable, insufficient in strength for Step 8.5's finish
  (point 1 above).
- NEW this round: importing aimo-0477's monotone-gcd/monotone-valuation trick verbatim
  (gcd(a_{n_B}, a_n) is empirically NOT monotone in n for A'-occurrences — tested and
  falsified on a_1=6851, point 4 above) — the mechanism requires an algebraic recursion
  this problem's hypothesis doesn't provide.
- q = min(F') / q = max(F') as a magnitude-based characterization of the Lemma-G prime:
  falsified (a_1=4807, q=17≠min(F')={13,17}).

### Small-case / intuition notes (all labeled conjecture, not proof)
- Conjecture (new, 34/34 seeds, 0 counterexamples): for a rogue pair's two EARLIEST
  witnesses, |P(a_{n_B})\S₀ ∩ P(a_{n_A})\S₀| = 1 always (stronger/narrower than "some
  prime recurs infinitely often," and distinct from the falsified Universal Singleton
  Hypothesis, which was about |F'| alone, not the two-witness intersection).
- Conjecture (qualitative, matches round 6's own note, re-confirmed): q's divisibility
  frequency among A'-occurrences is ~100% while F'-companion primes' frequency is low
  (~1-10%, consistent with a generic/no-structural-force baseline) — this asymmetry is
  itself evidence that whatever forces q is a deterministic mechanism tied to the greedy
  rule's legality requirement, not a density/frequency phenomenon, i.e. FAH is "too true"
  to be a density coincidence and needs a hard combinatorial reason.
