## imo-2026-06

**Problem.** a_1>1 given; a_{n+1} := smallest integer > a_n with gcd(a_{n+1},a_i)>1 for all i≤n.
Prove ∃T,L with a_{n+T}=a_n+L for all n. (proof_only, answer_type none — no numeric
answer needed, just the existence proof.)

### Context digested
Read `results/imo-2026-06/current.md` in full (all 8 rounds), `knowledge_base.md`, all
11 approach files' summaries via `.ranking.json`, and searched the crux corpus
(`past_crux_moves_database.json` / `past_problems_database.json`) by subtopic
(`processes-and-algorithms`, `sequences-and-recurrences`, `divisibility-and-gcd`,
`pigeonhole`) and by keyword (periodic, greedy, gcd, eventual).

The whole population (covering-system-construction, greedy-exchange-cost-potential, and
every spinoff: amortized-charging-budget, witness-depth-bound, witness-index-descent,
reversible-transition-map, recruitment-round-charging, scalar-well-ordering-lock-in,
seed-coupling-induction) has converged onto ONE crux: **Full-Absorption Hypothesis
(FAH)/Symmetric FAH** — for a "rogue" disjoint base-type pair (A,B) with canonical
Lemma-G prime q* := min(F'∩F''), q* divides EVERY (not just infinitely many)
sufficiently-large term of the extended-persistent refinement, on BOTH sides. This is the
sole open gap in an otherwise fully-reduced, fully-certified chain: Free Facts → Bounded
Gap → Persistent-Type Pigeonhole → Finite Core Theorem → Projection Lemma +
Collateral-Safety Theorem (round 6, unconditional) reduce (†) exactly to base-type-pair
termination, and FAH/Symmetric FAH ⟹ that termination (Step 8.5, verified). Every
mechanism tried to prove FAH directly — pigeonhole/dichotomy (round 8's Divisor-Chain),
inductive chaining, exchange/minimality (Lemma I diagnosis, round 6), two-witness
intersection uniqueness (round 7, dead), scalar algebraic-recursion transplant
(round 7/8, refuted by Witness Discontinuity Obstruction), seed-coupling induction on
ω(a_1) (round 8, refuted) — has failed. This is now 3+ rounds stuck on the same wall,
so per CLAUDE.md I focused entirely on structurally different top-level framings.

### Distinct openings

**1. "Recruitment-budget" / fixed-witness-pool finiteness argument (global counting,
not per-pair absorption) — the most concrete new lead.**
Collateral-Safety (certified, round 6) already gives: open(k) := {disjoint base-type
pairs not yet fully safe at core S₀^(k)} is non-increasing over a FIXED finite index set
(≤ C(|𝒫|,2) pairs, 𝒫 fixed once and for all since Q never changes). (†) holds iff
open(k)=∅ for some finite k. Crucially, whenever open(k)≠∅, the Generalized Bounded
Witness Lemma's Corollary is ALWAYS triggered and recruits a genuinely NEW prime q∉S₀^(k)
— so S₀^(k) strictly grows every round that open(k) is nonempty. **This suggests a
purely cardinality-based finish that never needs FAH's "cofinite divisibility" content
at all**: if one could show the total number of DISTINCT primes that can EVER be
recruited across all rounds, for all pairs, is bounded by a fixed finite number N*
(computable from the ORIGINAL, S₀-independent, Q-level base-type witnesses a_{m_A},
a_{m_B} — e.g. N* ≤ Σ_{(A,B) disjoint} |P(a_{m_A})∪P(a_{m_B})|, a concrete number one can
compute from a finite prefix of the sequence), then after ≤ N* rounds no new prime can be
recruited, forcing open(k)=∅ by the contrapositive of the Corollary. This closes (†) via
pure pigeonhole/counting on a fixed pool, with ZERO need to prove any prime divides
*every* later term of a type — only that the process of adding primes to S₀ must halt.
- **Why this is genuinely different from what's been tried:** `recruitment-round-charging`
  (round 6, RETHINK) tried charging against ω(a_1)/Ω(a_1), growth rate O(n), and hub-batch
  counting — none of these anchor to the FIXED Q-level base-type witness's own factor set;
  this framing does, and it is exactly what round 8's Fixed-Witness Divisor-Chain
  mechanism was reaching for at the single-pair level (it stalled on a dichotomy step
  within ONE pair's absorption, not on the multi-round global counting bound itself — the
  counting-bound question was never separately posed or tested).
- **Where it likely hits a wall (be honest):** the certified **Witness Discontinuity
  Obstruction** (round 7) shows that when S₀ grows, an extended type's *own* earliest
  witness can jump to a later, unrelated index with no controlled relationship to the
  recruited prime — so the *next* round's Bounded-Witness-Lemma pigeonhole may draw from
  a completely different, uncontrolled divisor set, not the original P(a_{m_A})∪P(a_{m_B}).
  If so, N* is not actually fixed and the budget argument fails exactly where Witness
  Discontinuity already bit the algebraic-recursion transplant. The one thing NOT yet
  checked: whether this discontinuity is confined to *extended*-type witnesses (S₀-level)
  while the *base*-type witnesses m_A, m_B (defined purely from Q, provably S₀-independent
  per the Same-Side Ordering Lemma) stay fixed — and whether the recruited prime at EVERY
  stage can be shown to still lie in a set determined by m_A, m_B alone (not by whatever
  shifted extended witness triggered that particular round). This is an open, checkable
  sub-question worth a dedicated computational + structural pass before ruling the
  framing out — it has NOT been tested computationally by any approach so far.

**2. Density/double-counting contradiction against the (already-proven) finite cardinality
of 𝒫, instead of direct absorption.**
Rather than trying to prove FAH's strong per-occurrence divisibility claim, prove the much
weaker statement "q* divides a POSITIVE-DENSITY subset of later A'-occurrences" via an
elementary double-count in a window [1,N] (using the Generalized Bounded Gap Lemma to
lower-bound the NUMBER of A'-type terms in [1,N], and a counting argument on how many can
avoid q* while still being pairwise-coprime-compatible with everything constructed so
far). Then attempt to upgrade "positive density, not full absorption" to a contradiction
via a completely different mechanism than exchange/minimality: if infinitely many
A'-occurrences avoid q*, show this infinite subfamily is ITSELF eventually persistent as a
strictly-refined extended type (a genuinely new element of 𝒫' at some larger, explicit
core), and iterate — since Persistent-Type Pigeonhole + Finite Core Theorem already give a
hard finite UPPER BOUND on |𝒫| (≤ 2^{|Q|}−1) at any FIXED core, the goal is to show this
refinement process (not the prime-recruitment process, a different sequence of
refinements) cannot run forever without violating that fixed bound — i.e., attack via
contradiction against an already-certified counting fact rather than trying to build the
absorption directly.
- **Why genuinely different:** every prior mechanism (Lemma H branch analysis, exchange,
  two-witness uniqueness, divisor-chain, seed-coupling) tries to construct or force a
  SPECIFIC divisibility; this instead tries to derive a contradiction from a cardinality
  ceiling that is already unconditionally proved, sidestepping the need to identify or
  construct any particular witnessing index at all.
- **Wall:** the "iterate the refinement" step is exactly what Collateral-Safety already
  shows CANNOT spawn genuinely new pairs beyond a fixed 𝒫 — so the refinement process
  this framing needs is refinement of a SINGLE type's *extended* structure at growing
  cores, which is unbounded in cardinality only if the core itself grows unboundedly
  (same open question as Opening 1). Likely reduces to the same underlying finiteness
  question, but via a different, not-yet-tried proof mechanism (counting contradiction vs.
  constructive absorption), so still worth opening as a rival slug — a "no" on this
  mechanism is informative even if it converges to the same ultimate gap.

**3. Bypass the type/absorption vocabulary entirely: direct de Bruijn/automaton argument
on raw residues a_n mod M for an EXPLICIT, generously-oversized M — genuinely different
target, most speculative.**
Fix M := lcm of ALL primes appearing in a_1,...,a_K for K large but explicit (not derived
from the type machinery at all). Attempt to show directly, via a magnitude/size argument
(not existence-pigeonhole), that for n large enough, whether a given m>a_n is a legal
successor depends ONLY on (m mod M) and a BOUNDED lookback window of the most recent
O(1) terms — i.e., attack "only finitely many primes ever matter" as a raw factorization-
size claim (large-index terms a_i for i≪n automatically satisfy gcd(m,a_i)>1 for generic m
divisible by enough small primes, EXCEPT for a bounded exceptional set that can be
enumerated explicitly from a_1..a_K) rather than via the type/Q/S₀ apparatus. If
successful this reduces the whole problem to a literal finite-state automaton on residues
mod M with an explicit (if large) M, giving eventual periodicity by pure pigeonhole
(state repeats ⟹ cycle) with NO absorption content needed.
- **Why distinct:** this was checked and found to be LOGICALLY EQUIVALENT (not a bypass)
  to (†) in one specific instantiation (`reversible-transition-map`, round 5, "S-sufficiency
  ⟺ V=∅ at level S" — RETHINK, confirmed equivalence both directions). But that
  equivalence proof used the SAME notion of "core S" and "extended type" as the rest of
  the population; it did not test whether a DIFFERENT, cruder state space (raw a_n mod M
  for an explicitly huge M, not the minimal type-theoretic core) could sidestep the
  equivalence by simply being large enough that the automaton is trivially well-defined
  by a crude magnitude bound (e.g. via Bertrand's postulate / prime-counting estimates on
  how many small primes are needed to guarantee coprimality with a bounded window) instead
  of needing the SHARP minimal core the type framework insists on.
- **Wall (be honest, this is the weakest of the three):** "explicit M large enough" begs
  the question of WHY finitely many primes control everything at all — this is precisely
  the content the Finite Core Theorem already supplies unconditionally; a cruder
  magnitude argument would need to independently re-derive finiteness of the relevant
  prime set without leaning on Q/persistent-types, which the current population has not
  found any way to do (all attempts at finiteness use the pigeonhole-on-types
  argument). Most likely this collapses into a strictly weaker restatement of
  already-proven facts and does not touch FAH at all — flagged as low-priority /
  exploratory only, not a strong rival slug.

### Candidate technique(s)
- Opening 1: pigeonhole/counting on a FIXED finite pool (elementary, not analytic) —
  closest in spirit to KB's "Divisor analysis" and "Pigeonhole" entries, combined with
  the already-certified Collateral-Safety monotone-open(k) reduction.
- Opening 2: double-counting / density lower bound in a window, then contradiction against
  an established cardinality ceiling (KB's "double-counting" style, and the crux corpus's
  `pigeonhole` / `divisibility-and-gcd` subtopics).
- Opening 3: automaton/state-repetition pigeonhole with an explicit magnitude bound (KB's
  Bertrand's postulate entry could plausibly supply the "enough small primes in a bounded
  range" ingredient if this is pursued, though I did not find a clean way to make it work).

### Cheap-kill candidates
- Opening 1 has a genuine cheap kill available before any heavy proof effort: **compute,
  for a handful of seeds with a genuine multi-round rogue history (a_1=187, 209, 4807),
  whether the recruited prime at round 2 (if a second round is ever needed) lies in
  P(a_{m_A}) ∪ P(a_{m_B}) for the FIXED, Q-level (not extended-type) base witnesses m_A,
  m_B** — this is a one-script computational check that would immediately falsify or
  support the framing's core assumption before committing proof effort. (Not yet run by
  any approach — worth doing first thing next round.)
- Opening 2's cardinality-ceiling contradiction can be spot-checked similarly: track
  |𝒫'| (number of distinct extended-persistent types at increasing explicit cores) across
  several recruitment rounds on the same seeds, and see whether it is bounded by the
  Finite Core Theorem's a priori ceiling 2^{|Q|}−1 even as the core grows — if it isn't,
  the framing needs the ceiling restated at each level, not assumed fixed.
- Opening 3: no cheap kill beyond noting it likely restates already-known content;
  lowest priority to build.

### Knowledge-base entries to use
- **Order of an element, Fermat/Euler** and **Linear recurrences** (`knowledge_base.md`
  Number Theory section) — "eventual periodicity of products of a sequence mod m" is the
  closest generic KB statement to the target claim, but the current population has already
  gone well past this generic template into problem-specific machinery.
- **Bertrand's postulate**, **Dirichlet's theorem (primes in AP)** — potentially useful only
  for Opening 3's magnitude-bound version, not otherwise engaged by the current field.
- **Divisor analysis / pigeonhole** (generic KB entries) — underlie Opening 1's proposed
  fixed-pool counting argument.
- No CRT/three-gap/Zsigmondy-type KB entry looks newly relevant beyond what's already in
  use (CRT is already the population's finish mechanism, Step 5).

### Analogous past problems (cruxes)
- **aimo-0678** (`number_theory`, `modular-arithmetic-and-CRT`) — "Once one coordinate of
  a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of
  the bounded coordinate's attainable values, turning the state pair into a deterministic
  map on a finite set." Genuinely the closest structural analogue (two-scalar
  bounded-then-CRT-reduced state), but **already imported and refuted** this workspace
  (`scalar-well-ordering-lock-in`, round 7/8: the hypothesized coupled recursion is FALSE,
  refuted by an exact counterexample and the certified Witness Discontinuity Obstruction).
  Do not re-import literally; any revival needs to NOT assume continuity of witness
  selection across stages, which is exactly what killed it last time.
- **aimo-0514** ("Planar National Park", `combinatorics`, `processes-and-algorithms`) —
  "Show a deterministic process is reversible so its state graph is a union of cycles,
  forcing the orbit to be purely periodic rather than eventually periodic." Also already
  tried in substance (`reversible-transition-map`, round 5: proved the natural finite-
  automaton formalization is logically EQUIVALENT to (†), not a bypass) — the target here
  (eventual, not pure, periodicity) is weaker than aimo-0514's, so reversibility is
  unnecessary; this analogy is exhausted, not fresh.
- I searched specifically for "eventually periodic" / "greedy sequence" / "smallest
  positive integer greater than" crux moves; nothing else in the corpus is closer than
  these two, and both are already recorded as tried-and-not-a-bypass in this workspace.
  **Nothing genuinely new was found in the corpus for this problem** — the crux corpus
  does not contain a problem with the exact "greedy pairwise-gcd covering" structure; the
  two closest analogues are already exhausted. This itself is useful negative information:
  the outliner should not expect the corpus to hand a ready-made bypass, and any fresh
  framing must be built from first principles on this specific problem's structure (as
  Openings 1–2 above attempt).

### Prior progress
See current.md for the full certified stack (11 unconditional lemmas + 2 fully-resolved
special cases: |Q|=1, and Singleton-Side FAH). The single remaining gap, restated exactly:
prove FAH/Symmetric FAH for the canonical prime q* on a rogue base-type pair with
|F'|,|F''| ≥ 2 (the |F'|=1 or |F''|=1 case is now fully closed, unconditionally, via
Singleton-Side FAH). Equivalently (Opening 1's reformulation, not yet certified): prove the
recruitment process on the fixed finite index set of disjoint base-type pairs halts.

### Dead ends (do not retry)
- Direct FAH mechanisms: pigeonhole/dichotomy via Fixed-Witness Divisor-Chain in its
  round-8 dispatched form (branch "r∈S₀ ⟹ contradicts rogueness" is FALSE — a prior,
  more basic gap than previously flagged); joint Lemma-H branch analysis / Two-Witness
  Intersection Uniqueness (dead, round 7, both abstractly and computationally); exchange/
  minimality built solely from Free Facts + Generalized Bounded Witness + Gap Lemmas +
  Critical Prime Dichotomy (Lemma I's diagnosis, round 6); seed-coupling induction via
  single-prime removal on ω(a_1) (round 8, reproducibly falsified whenever 2∉Q').
- Well-ordering/monovariant descents: round-3's |A'|+|B'| size measure and round-5's
  witness-index descent both independently hit "refinement manufactures new small-index
  classes" — do not retry a single global monovariant descent without a provably
  refinement-robust measure (none found so far).
- Charging arguments: ω(a_1)/Ω(a_1) charging, growth-rate O(n) charging, hub-batch
  charging (round 6, all three RETHINK/dead or reduce to FAH) — Opening 1 above is
  explicitly NOT a repeat of these (it charges against a fixed witness's finite divisor
  pool, not ω(a_1)/growth/hub-count), but should be framed carefully to the outliner as
  distinct so it isn't mistaken for a repeat and auto-rejected.
- aimo-0678-style algebraic-recursion transplant (`scalar-well-ordering-lock-in`) —
  refuted by an exact counterexample (a_1=175) and the certified Witness Discontinuity
  Obstruction; do not re-import the literal coupled-recursion hypothesis.
- `reversible-transition-map`'s finite-automaton bypass in its S-sufficiency
  formalization — proved equivalent to (†), not a bypass.

### Small-case / intuition notes (conjecture, not proof)
- All positive computational evidence for FAH gathered so far (a_1=187, 209, 247, 385,
  4807 at the correctly-recruited core) shows 0 failures — this is consistent with FAH
  being TRUE, just currently unproved, not with FAH being false. (Conjecture, well
  supported: FAH holds.)
- The one place where a "6.2% divisibility, not cofinite" rate was reported (a_1=4807 at
  the RAW, un-recruited core S₀=Q) is measuring a different, strictly weaker statistic —
  base-type divisibility before any core recruitment, not the actual S₀-extended-type FAH
  claim used in the finish — so it is NOT evidence against FAH itself; I flag this only
  because a careless reading of current.md could conflate the two and mistakenly think FAH
  has empirical counterexamples. It does not: every genuine test of FAH (at the correct,
  recruited core) has 0 failures across every seed tried.
- No seed tested so far has ever needed a SECOND recruitment round for the same base-type
  pair (every tested case resolves in exactly one round) — mild evidence that if Opening
  1's fixed-pool framing is right, the pool per pair is probably very small (often size 1),
  which would make the budget argument easy to close computationally once its core
  assumption (recruited primes stay within the Q-level witness pool) is confirmed or
  refuted. This is exactly why the cheap-kill check under Opening 1 should be run first.
