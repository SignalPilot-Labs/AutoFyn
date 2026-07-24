# Math-explorer report — lens: Universal Singleton Hypothesis (round 6)

## Headline finding

**I found two independent, computationally robust counterexamples to the Universal
Singleton Hypothesis as literally stated.** At the *literal earliest-witness* rogue
pair (the exact convention mandated by rounds 4–5 after the witness-selection bugs),
the later witness's outside-S₀ prime factor set F′ has **size 2**, not 1, in both
cases. Full data below, independently reproducible. If this holds up under a second
from-scratch reimplementation (as round 5's 4 counterexamples were), the Universal
Singleton Hypothesis is **dead as a universal claim** and the population needs a
substitute (a bounded-|F′| version, or a version stated about the *recurring* prime
rather than the *whole* witness factor set — see "What survives" below, since a
weaker, still-useful fact does hold in both my examples).

## 1. What has been tried on the Singleton Hypothesis, and why it stalled

Read in full: `current.md` (all of ROUND 4/5), `approaches/covering-system-construction.md`
(lines ~890–1340), `approaches/greedy-exchange-cost-potential.md` (lines ~689–848),
`lemmas/critical-prime-dichotomy.md`, `lemmas/generalized-bounded-witness-lemma.md`,
`lemmas/forced-linking-prime.md`.

- **Setup.** Fix S₀ ⊇ Q, a rogue pair of S₀-extended-persistent types (A′,B′) with
  disjoint base types and A′∩B′=∅. By Lemma G (Extended Earliest-Witness
  Intersection), using the *global earliest* occurrences n_A := min{n:ρ(n)=A′},
  n_B := min{n:ρ(n)=B′} (WLOG n_A<n_B), some prime q∉S₀ divides both a_{n_A} and
  a_{n_B}. Define **F′ := P(a_{n_B}) \ S₀** (all outside-core primes of the *later*
  witness). The Singleton Hypothesis is |F′| = 1 for every such rogue pair.
- **Round 5's only real attack (greedy-exchange-cost-potential): Lemma H (Critical
  Prime Dichotomy).** For any outside-core prime q′ | a_n, either (a) stripping q′
  drops the value ≤ a_{n−1}, or (b) some earlier a_i shares *exactly* {q′} with a_n.
  This is a clean, fully proved, unconditional per-prime necessary condition — but
  it is symmetric in q′: nothing distinguishes *why* one particular q′ would be the
  only one. The file's own honest "attempted repair" section (lines 798–812) tried
  to force two witnessing indices i, i′ (for two different primes q′,q″ satisfying
  branch (b)) to coincide, and explicitly found no argument for this — Free Facts is
  a pairwise-intersection existence statement, never a global bound on how many
  distinct primes one integer's factorization can need to satisfy many different
  earlier terms' legality simultaneously. This is exactly the same wall round 3's
  Lemma F hit (certified magnitude lemmas only build *larger* competing candidates,
  never smaller ones, so no exchange argument closes this from the existing toolkit).
- **Computational support claimed by round 5:** ~20–200 seeds, all singleton — but
  per the file's own account this was scoped to |Q| ≤ 2 seeds mostly, or seeds
  without deep scanning (see below — my scan used much larger N and specifically
  targeted |Q|=3,4 seeds, which is where I found the counterexamples).
- **Why it stalled:** every certified lemma in the stack (Free Facts, Bounded
  Witness Lemma, Generalized Bounded Witness Lemma, Lemma G, Lemma H) is a
  *pairwise* or *single-witness* statement. None of them bound the *total* number
  of distinct outside-core primes a single integer's factorization can carry. The
  Singleton Hypothesis is fundamentally a claim about *one integer's total prime
  count outside a fixed finite set*, and nothing in the stack talks about total
  prime counts — only about existence of *some* shared prime. This is a real gap
  in kind, not just in effort.

## 2. My computational search — methodology and the two counterexamples

**Convention used (matches rounds 4/5's corrected convention exactly):** generate
the full greedy sequence a_1,...,a_N by brute-force trial division (large N, 3000–8000
terms, well beyond any tail-window shortcut); for each nonempty subset B of Q, take
m_B := the GLOBAL MINIMUM index n with τ(n)=B (persistence checked by requiring
the type to recur after the halfway point of the computed range, and I additionally
verified persistence directly by listing full occurrence counts — see below, not just
the tail heuristic); build S := ⋃(P(a_{m_B})\Q), S₀ := Q∪S exactly per the Finite Core
Theorem (`covering-system-construction` Step 3); compute extended types ρ(n) =
P(a_n)∩S₀, find S₀-extended-persistent types 𝒫′ (same persistence check); for every
disjoint-base-type pair (A′,B′) with A′∩B′=∅, take the GLOBAL MINIMUM occurrence
indices n_A, n_B (not a tail-window witness) and compute F′ = P(a_{n_{max}})\S₀ where
n_max is the larger of the two.

**Counterexample 1: a_1 = 4807 = 11·19·23** (Q = {11,19,23}).

- S = {2,3,5,7,73,127} (from witnesses: type {11} witness a_2=4818=2·3·11·73; type
  {19} witness a_3=4826=2·19·127; type {23} witness a_4=4830=2·3·5·7·23; type
  {11,19} witness a_15=5016=2·3·11·19; type {11,23} witness a_17=5060=2·5·11·23;
  type {19,23} witness a_28=5244=2·3·19·23; type {11,19,23} witness a_1 itself).
  S₀ = {2,3,5,7,11,19,23,73,127}.
- Rogue pair: **A′ = {3,5,19}** (base type {19}), **B′ = {2,11}** (base type {11}).
  Base types {19},{11} disjoint; A′∩B′=∅ in S₀ — genuine rogue pair.
- Earliest witnesses: **n_A = 6** (a_6 = 4845 = 3·5·17·19), **n_B = 7**
  (a_7 = 4862 = 2·11·13·17). Both are the literal global-earliest occurrences of
  their extended types (checked directly, no tail-window shortcut): the full
  occurrence list of A′={3,5,19} up to n=8000 is [6, 561, 1114, 2223, 3335, 3892,
  4445, 5002, 6667, 7223, 7775] (11 occurrences, roughly period ≈555 — a strong sign
  this is a genuine persistent type, not a fluke single hit); B′={2,11} occurs 151
  times up to n=8000.
- gcd(a_6, a_7) = gcd(4845, 4862) = **17** (confirms Lemma G's guaranteed shared
  prime).
- **F′ = P(a_7) \ S₀ = {13, 17}. |F′| = 2.** (a_7 = 2·11·13·17; 13,17 ∉ S₀.)

**Counterexample 2: a_1 = 11305 = 5·7·17·19** (Q = {5,7,17,19}).

- S = {2,3,13,23,29,37,43,101}, S₀ = {2,3,5,7,13,17,19,23,29,37,43,101}.
- Rogue pair: **A′ = {3,7}** (base type {7}), **B′ = {2,5}** (base type {5}).
- Earliest witnesses: n_A = 4 (a_4 = 11319 = 3·7³·11), n_B = 7
  (a_7 = 11330 = 2·5·11·103).
- gcd(a_4,a_7) = gcd(11319,11330) = **11**.
- **F′ = P(a_7) \ S₀ = {11, 103}. |F′| = 2.**

Both examples were checked with N large enough (3000–8000 terms) that the witness
types recur many times well past the halfway point of the computed range, so this is
not a repeat of the round-3/4 "non-minimal witness" bug — I used the actual global
minimum, and I additionally re-verified the S/S₀ computation is internally consistent
(Q ∪ (witnesses' extra primes) literally equals the stated S₀, unlike the earlier
buggy computations flagged in `current.md`'s ROUND 4 correction).

**A scan for context.** Across 235 seeds (all products of 3 distinct primes < 6000,
and 4 distinct primes < 12000, from primes up to 40, N=900 per seed as a first pass),
only these 2 seeds showed |F′| ≥ 2 among all rogue pairs found. So |F′| ≥ 2 appears
to be *rare* but real — consistent with the Singleton Hypothesis being "usually true,
not always," exactly the same pattern round 5 found for "V=∅ usually, not always"
before it was falsified. **This is the same shape of overclaim the population has
made twice before** (round 3/4's "zero recruitment rounds" and round 4's "V=∅
always") — a claim that holds on the easy/common seeds and silently fails on rarer
ones, always eventually found by widening the seed search past |Q|=2.

## 3. What survives — a candidate weaker, possibly-true replacement hypothesis

I checked, in both counterexamples, whether the **specific prime guaranteed by
Lemma G** (the one shared with the earlier witness — 17 in example 1, 11 in example
2) recurs on (nearly) ALL later same-type terms, even though F′ itself has size 2:

- Example 1: among all 151 occurrences of B′={2,11} up to n=8000, **17 divides
  all 151** (100%), while 13 divides only 11/151 (≈7%).
- I did not finish the symmetric check for example 2 in the time available, but the
  pattern (Lemma G's prime is load-bearing on ~100% of occurrences, while the
  "extra" prime in F′ is incidental/rare) is exactly what Lemma H's dichotomy
  predicts: the extra prime 13 (resp. 103) is present at that ONE witness for a
  branch-(b) reason specific to *that* index (legality against some particular
  earlier term), not because it is needed for reconciliation with A′.

**This suggests the correct fix is not to prove |F′|=1, but to prove a WEAKER,
possibly still-sufficient statement**: "the Recruitment Corollary's pigeonhole-selected
prime (the one recurring infinitely often on the A′-side) is unique / well-defined
independent of which witness index is chosen" — i.e. relocate the target from
"the witness's total factor set outside S₀ has size 1" (false, per above) to "the set
of primes that actually recur infinitely often on the A′-side, as opposed to merely
appearing once at the witness, has size 1." This second claim is NOT refuted by my
examples (17 recurs at 100%, 13 does not) and may be exactly what the Conditional
Simultaneous/Single-Pair Resolution Theorems in `covering-system-construction`
actually need — worth checking against their proofs directly, since if they only
invoke "there exists a q recurring on infinitely many A′-terms" (which is exactly
what the Recruitment Corollary already unconditionally proves!) rather than
"F′ has exactly one element," the conditional theorems might already be
UNCONDITIONAL, and the whole Singleton Hypothesis chase may be a red herring — next
round should carefully re-read exactly which fact `covering-system-construction`'s
proofs invoke, sentence by sentence, distinguishing "F′ is a singleton" from "the
Corollary's pigeonhole-prime is singled out."

## 4. Candidate mechanisms for connecting distinct primes' witnessing indices
(requested — sketches, not proofs)

- **Total-prime-count obstruction (why I don't think a direct contradiction from
  CRT/pigeonhole alone works).** Free Facts and its descendants are *existential*
  (some shared prime exists between any two terms); nothing in the stack is
  *cardinal* (bounding how many total primes one term needs across many pairwise
  constraints). A CRT-style argument would need to first show something like "a_n's
  outside-S₀ part is forced to be a single prime power," which is a magnitude/growth
  claim, not a divisibility claim — outside what CRT alone gives. I do not see a
  CRT mechanism that closes this without new input.
- **Minimality-of-index mechanism (round 5's approach, and mine): does forcing q′,q″
  both branch-(b) force i=i′?** No — as the greedy-exchange file also found, i and i′
  range over *different, unrelated* earlier terms. In my example 1, is there such an
  i for prime 13 at a_7=4862? Check: an earlier term a_i must share EXACTLY {13} with
  a_7. None of a_1..a_6 is divisible by 13 (a_6=3·5·17·19). So branch (b) does NOT
  hold for q′=13 at n=7 within the window i<7 — meaning branch (a) must hold instead:
  stripping 13 from a_7 gives c = 4862/13 = 374 = 2·11·17, and indeed 374 ≤ a_6=4845.
  **This is a clean confirmation of Lemma H's dichotomy in a live example** (13 falls
  into branch (a), 17 — the Lemma-G-guaranteed prime — would need separate checking,
  but likely also branch (a) or coincides with reconciliation). This suggests a
  refined dichotomy-based classification: *maybe every element of F′ beyond the
  Lemma-G prime always falls into branch (a)* (i.e., "junk" primes are exactly the
  ones whose removal drops below the previous term, while the Lemma-G/reconciling
  prime need not). If provable in general, this would show F′ splits into "one
  necessarily-recurring prime" + "arbitrarily many branch-(a)-only junk primes that
  don't matter for persistence" — which is precisely the "relocate the target" fix
  proposed in §3. **This is a genuinely new, not-yet-tried angle**: classify every
  element of F′ (not just one arbitrary element) via Lemma H, and check whether the
  Lemma-G-guaranteed prime is always the unique element that can be in branch (b),
  while all OTHER elements of F′ are forced into branch (a). I did not have time to
  attempt a general proof of this refined claim, only the one-instance spot check
  above; it is the single most promising concrete next step I found.
- **Pigeonhole on residues:** not fruitful as a direct mechanism — the number of
  distinct primes an integer can have outside a fixed S₀ is not controlled by any
  residue-class argument already in the stack; CRT enters only after (†) is granted
  (Step 5), not as a tool for proving (†) itself.

## 5. Crux corpus — relevant techniques (queried `number_theory`, subtopics
`divisibility-and-gcd`, `sequences-and-recurrences`, `pigeonhole`)

- **aimo-0477** (`divisibility-and-gcd`): "Track gcd(fixed term, current term) and
  show it divides the next one, producing a divisor-chain bounded by the fixed term
  that must stabilize." Potentially adaptable: if one could show the "junk primes"
  in F′ form a divisor-chain relative to some fixed earlier quantity that must
  stabilize, this could bound |F′|. Not obviously applicable but worth a look — the
  sequence here is genuinely a "smallest legal successor" construction, similar in
  flavor.
- **aimo-0421** (`divisibility-and-gcd`): "gcd of a fixed element with a varying one
  is always a divisor of that fixed element... only finitely many values, so over an
  infinite family of partners infinitely many must give the same gcd value" — this
  is essentially the same pigeonhole already embedded in the Bounded Witness Lemma /
  Recruitment Corollary; no new content beyond what's certified, but confirms the
  "pigeonhole over an infinite family onto a fixed finite witness's factor set" move
  is the standard one for this genre, i.e. the population is already using the
  standard tool and the crux corpus doesn't offer a sharper cardinal-bounding version.
- **aimo-0813** (`divisibility-and-gcd`): "Take the minimal element d of an
  addition-closed subset of N... minimal-counterexample descent" — same family as
  round 3/5's already-attempted-and-failed size-measure descents (documented dead
  end); do not re-attempt without a new monovariant.
- **aimo-0928** (`divisibility-and-gcd`): Euclid-style "evaluate at the product of
  known qualifying primes to get a value coprime to all of them, forcing a new prime
  divisor" — this is basically the *opposite* direction (constructing new primes),
  already well understood as the Recruitment Corollary's own mechanism; no new
  leverage for bounding |F′| from above.
- No crux in the scanned subtopics directly attacks "bound the total number of
  distinct prime factors a single greedily-constructed term can have outside a fixed
  finite reference set" — this appears to be a genuinely uncommon move in the corpus,
  consistent with why the population has stalled on it for 2 rounds.

## Recommendation for next round

1. **Do not re-propose the Universal Singleton Hypothesis (|F′|=1) as a target** —
   report the two counterexamples above (4807, 11305) for independent
   reverification (per the round-5 protocol: at least one more from-scratch
   reimplementation before treating this as settled, given the workspace's history
   of witness-computation bugs). If confirmed, retract it explicitly in `current.md`.
2. **Immediately check** whether `covering-system-construction`'s Conditional
   Single-Pair / Simultaneous Resolution Theorems actually need literal |F′|=1, or
   only need "the Recruitment Corollary's pigeonhole-prime is well-defined/unique" —
   this may already be provable unconditionally (the Corollary already gives
   existence; only uniqueness/independence-of-witness-choice might be missing) and
   could shortcut the whole Singleton chase.
3. **New concrete sub-target, not yet attempted:** prove that every element of F′
   other than the Lemma-G-guaranteed shared prime necessarily falls into Lemma H's
   branch (a) (spot-checked true once, in counterexample 1, for prime 13). This
   would justify "relocating" the needed hypothesis away from |F′|=1 toward "the
   recurring prime is unique," which the evidence above suggests is likely still
   true even where |F′|≥2.

## Files/paths referenced
- `/home/agentuser/repo/results/imo-2026-06/current.md`
- `/home/agentuser/repo/results/imo-2026-06/approaches/covering-system-construction.md`
- `/home/agentuser/repo/results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`
- `/home/agentuser/repo/results/imo-2026-06/lemmas/critical-prime-dichotomy.md`
- `/home/agentuser/repo/results/imo-2026-06/lemmas/generalized-bounded-witness-lemma.md`
- Scripts used (scratch, not part of the workspace): `/tmp/gen.py`, `/tmp/analyze.py`,
  `/tmp/scan.py`, `/tmp/batch.py` — reproducible; re-run `analyze.py 4807 8000` and
  `analyze.py 11305 4000` to reproduce the two counterexamples directly.
