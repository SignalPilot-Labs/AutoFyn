## imo-2026-06 (H2/NTBT crux scouting — round 18)

### Task 1 result: a_1=255255, type {5,7,11,13,17} — RESOLVED, RECURS (supports NTBT)

Extended the exact greedy-sequence simulation (brute-force `gcd(c,a_i)>1` for
all prior `i`, verified faithful to the literal problem definition — see
Method below) for `a_1 = 255255 = 3·5·7·11·13·17` (`Q = {3,5,7,11,13,17}`,
`|Q|=6`) from the round-17-flagged window of 65,000 out to **500,000 terms**
(pushed further to ~980,000 before a memory ceiling, see caveat below).

**Headline finding: the flagged type `{5,7,11,13,17}` DOES recur.** Its full
occurrence list through n=500,000 is:
```
n = 27184, 135914, 190280, 299010, 353376, 462106
```
i.e. it needed a runway of **108,730** more terms past its first occurrence
(27184 → 135914) before the second occurrence appeared — nearly 4× longer
than the 65,000-term window round 17 checked. This is exactly the same
"window artifact" failure mode already diagnosed and resolved for the other
two flagged seeds (`a_1=30030`, `a_1=15015`) in round 17, now confirmed for
the third and last remaining unresolved candidate. **The round-17-flagged
"currently-unresolved candidate exception to NTBT" is no longer open — it is
resolved in NTBT's favor** (recurs, not a permanent transient).

Stronger: at n=500,000, **every one of the 63 distinct persistent/observed
types for this seed has now recurred at least 6 times** (`min(count) = 6`,
zero single-occurrence types remain) — including the full-`Q` type
`τ(1) = {3,5,7,11,13,17}` itself, which recurs *exactly periodically* at
```
n = 1, 81549, 163097, 244645, 326193, 407741, 489289   (constant gap 81548)
```
This is the strongest and cleanest recurrence evidence for this seed to
date — `a_1=255255` is now fully consistent with NTBT through 500,000 terms,
matching (and now exceeding in confirmation depth) the two previously
resolved seeds.

Interesting substructure (evidence, not proof): the target type's gaps
alternate `108730, 54366, 108730, 54366, 108730` (`54366 = 108730/2`),
suggestive of two interleaved arithmetic sub-progressions rather than a
single constant period — noted for whoever eventually attacks literal
periodicity/period-length questions, not pursued further here (out of scope
for this task).

**Method / correctness.** Brute-force greedy generation (`c = a_n+1, a_n+2,
...`, `c` legal iff its prime factorization's primes, unioned over "which
prior indices they divide" via a bitmask-per-prime representation, cover all
indices `1..n`) — cross-checked byte-for-byte against a naive
`math.gcd`-against-every-prior-term reimplementation on `a_1=175, n≤20`
(exact match) before trusting it at scale. This is NOT sympy (per memory
rule 20) and NOT an approximation — it is the literal sequence.

**Performance/memory caveat (new finding, worth recording for future
rounds).** The per-prime-bitmask representation (Python big-int per prime,
OR'd together to check candidate legality) is very fast (500,000 terms in
~19s) but its memory use is **not** `O(n)` — it is `O(n · (number of
distinct primes ever used))`, because even a single-occurrence "junk" prime
still needs a dense bitmask up to its occurrence index. Since the total prime
support of this sequence is known to grow roughly linearly in `n` (memory
rule 4), memory blows up (~7GB+ RSS observed) and the process is OOM-killed
around `n≈980,000–1,000,000` on this container regardless of time budget —
this is a genuine scaling wall of this particular representation, not a
timeout. **500,000 terms was reached cleanly and is more than sufficient
runway to resolve the flagged question** (the second occurrence appeared at
135,914, well inside the 500k window); pushing to 1M+ would need a smarter
sparse-prime data structure (e.g. plain per-prime index lists + merge-based
coverage check, or periodic garbage-collection of "dead" rarely-used primes)
which was not built this round given the question was already answered.

**Bottom line for the outliner:** treat NTBT's numeric support as now
strictly stronger than reported in round 17 — the one open candidate
exception is closed (in NTBT's favor), leaving **zero** open numeric
counterexamples to NTBT anywhere in the workspace's ~50+ tested seeds. This
does **not** constitute a proof of NTBT (still a conjecture, no new proof
route found — see Task 2) but the round-17 "genuine, currently-unresolved
candidate" language in `current.md`/`vacuous-self-absorption-lemma.md`
should be updated: it is resolved, not open.

### Task 2 result: |𝒫'(S)|-combinatorial-bound angle — collapses, no new corridor

Investigated whether a genuinely different (not index-based `N(S_k)`,
not `M_B`) combinatorial bound using `|𝒫'(S)|` (bounded trivially by
`2^{|S|}-1`, per `lemmas/binary-refinement-and-threshold-recursion.md`'s own
Binary Refinement Lemma: adjoining one prime at most doubles the persistent-
type count) could bound the number of self-absorption rounds. Concretely
tried three framings, all collapse:

1. **Bound total rounds by "each round permanently resolves a disjoint
   base-type pair, and pairs are bounded by `|𝒫'(S)|` at each stage."** This
   is exactly the mechanism round 17's `type-alphabet-counting-bound` was
   dispatched with and RETHINK'd pre-build (`/tmp/round-17/outline-
   reviewer.md`): the outline-reviewer proved "finitely many rounds" is
   **literally the same statement** as "`N(S_k)` bounded" (one-line
   equivalence, both directions, independently re-checked by me — it's a
   correct proof, not a hand-wave), so bounding round-count this way is not
   a new target, just `N(S_k)`-boundedness (round-16-certified
   non-constructive `M_B`) under new vocabulary. **Confirmed dead, do not
   retry.**
2. **Bound `|S_∞| := |⋃_k S_k|` directly, then `|𝒫'(S_∞)| ≤ 2^{|S_∞|}-1`
   bounds the type-alphabet outright, hence rounds.** This is memory rule 28
   verbatim ("`|S_k|` stays within some finite ambient set" — circular with
   H2 itself, since there is no independent finiteness source for `S_∞`; the
   only proven finiteness fact, total-prime-support-unboundedness, cuts the
   *other* way). **Confirmed dead/circular, do not retry.**
3. **A genuinely weaker target: does `|𝒫'(S_k)|` itself (the type-*count*,
   not `S_k` or `N(S_k)`) stabilize/become eventually constant, even if
   `S_k` keeps growing?** This is the one framing not literally identical to
   (1)/(2) — a new angle in principle. But even if provable, it would NOT
   close H2 as needed: the Master Conditional Theorem's chain
   (`n1-periodicity-reconciliation`, `self-absorbing-core-theorem.md`) needs
   a fixed terminal core `S*` with `S* = S*⁺` (the absorption process itself
   halting), not merely a bounded type-count while the core keeps absorbing
   new primes forever. This is structurally the same "vacuous/wrong-strength
   weaker target" trap round 12's `subword-complexity-periodicity` hit with
   its "finitely many colliding residue classes" headline (found vacuous,
   see round 12 in `current.md`) — a genuinely provable-looking side fact
   that doesn't actually discharge the hypothesis needed. I did not find a
   way to strengthen (3) back into something that both (a) avoids collapsing
   into (1)/(2) and (b) actually implies chain termination.

**Verdict: no new angle exists here — the `|𝒫'(S)|`-combinatorial-bound
family collapses into either the already-dead `N(S_k)`/`M_B` territory, the
already-flagged-circular `|S_∞|`-finiteness claim, or a vacuous weaker
target that doesn't reach the theorem's actual needed conclusion.** This
matches (does not contradict) round 17's H2-termination explorer's own
honest "may hit the same M_B-style wall, or may not" hedge — it does hit
that wall, now confirmed rather than merely suspected. Recommend the
outliner treat H2's "index/round-counting" corridor (in all three of these
shapes) as exhausted, same status as H1's mechanism family — if H2 is to be
cracked, it needs an ingredient outside "bound a count via `2^{|S|}`" or
"bound `N(S_k)`/`M_B` directly," e.g. possibly something about the specific
*arithmetic* structure of which primes get recruited (unexplored: is there
any correlation between a recruited prime's size/identity and the round
number, e.g. via the Sandwich Genericity magnitude bounds combined with
prime-counting/PNT-style density estimates on candidate factorizations? Not
investigated this round — flagged as a genuinely untried direction, distinct
from pure counting/pigeonhole, for a future round if the outliner wants one
more H2 corridor before conceding it as a second open hypothesis alongside
H1).

### Task 3: confirmed-dead H2 mechanisms (do not retry)

- **`type-alphabet-counting-bound`** (round 17, RETHINK pre-build) — "finitely
  many absorption rounds" proved literally equivalent to "`N(S_k)` bounded";
  its fallback mechanism (permanently-resolve-a-pair-per-round) reduces to
  the FAH recruitment process itself. Dead, not registered in the ranker.
- **"`|S_k|` stays within some finite ambient set"** (memory rule 28,
  round 17 H2-termination explorer) — circular with H2 (no independent
  finiteness source for `S_∞`). Dead.
- **`M_B` (the natural one-prime-at-a-time refinement of `N(S)`)** — proved
  **provably non-constructive** in general (round 16, Proposition 3 of
  `lemmas/binary-refinement-and-threshold-recursion.md`, a toolkit-
  independent structural fact, not a workspace gap). Any future H2 attempt
  bounding `M_B` or an `M_B`-shaped quantity directly is dead on arrival;
  needs a genuinely different quantity.
- **`rogue-pair-termination-potential`** (round 15) — not H2-specific
  originally but same shape trap: verbatim duplicated the certified
  Collateral-Safety Theorem's own text; its "new" key lemma was FAH restated.
  Relevant precedent for screening any future "count resolved pairs" H2
  idea (memory rule 15).
- (H1-side, for completeness/non-duplication only, not H2): 18 confirmed-dead
  FAH mechanisms as of round 17 (`current.md`'s cumulative count) — none of
  these were re-examined this round since this task was scoped to H2/NTBT
  specifically, per dispatch.

### Distinct openings for the outliner
1. **Update the NTBT numeric-evidence claim** in `current.md`/
   `vacuous-self-absorption-lemma.md`: the round-17-flagged `a_1=255255`
   exception is now resolved (recurs at n=135914), zero open numeric
   counterexamples to NTBT remain across ~50+ seeds. This is bookkeeping, not
   a new proof route, but should be recorded accurately before the next
   round builds on it.
2. If a general NTBT proof is attempted: the two already-tried-and-dead
   routes (class-blind magnitude arguments; reduction to/from FAH) should
   not be retried verbatim; a genuinely different route (e.g., an explicit
   density/PNT-style argument on how often a *specific* subset of `Q` gets
   "reselected" as the covering type, distinct from the class-blind Sandwich
   Genericity family) has not been tried and is a candidate for a future
   round, though no concrete mechanism was found this round (honestly
   unexplored, not vetted).
3. H2's counting/pigeonhole corridor (index-based `N(S_k)`, `M_B`, and now
   `|𝒫'(S)|`-based) is exhausted per Task 2 above — treat as parallel to
   H1's mechanism-family exhaustion. A future H2 attempt needs either (a) an
   arithmetic/density argument on recruited-prime identity (untried,
   speculative), or (b) accept H2 as a second permanently-open hypothesis
   alongside H1 and focus remaining effort on write-up/robustness of the
   Master Conditional Theorem, per CLAUDE.md's plateau-breaking guidance.

### Candidate technique(s)
None beyond what's already certified (`termination-criterion-lemma.md`,
`binary-refinement-and-threshold-recursion.md`, `vacuous-self-absorption-
lemma.md`). No new technique family surfaced this round for either H1 or H2
that survives scrutiny — this was a numeric-resolution + negative-scouting
round by design (per dispatch), not a fresh-corridor round.

### Cheap-kill candidates
None new. The `2^{|S|}-1` bound on `|𝒫'(S)|` (Binary Refinement Lemma) is
real but, as shown in Task 2, does not cheaply kill or resolve H2 in any of
the three ways I tried to use it.

### Knowledge-base entries to use
No new generic `knowledge_base.md` entries identified beyond what prior
rounds already cite (pigeonhole/finite-state entries already exhausted per
round 17's fresh-framing sweep). This task was scoped narrowly to the H2/
NTBT numeric question and the `|𝒫'(S)|` angle specifically, per dispatch —
did not re-run a full knowledge-base sweep.

### Analogous past problems (cruxes)
None newly queried this round (out of scope for the dispatched task; prior
rounds' crux-corpus mining for this problem, rounds 9/14/15, already covered
the relevant subtopics — number_theory gcd/lcm eventual-periodicity and
combinatorics-on-words — exhaustively per those rounds' reports).

### Prior progress
See `results/imo-2026-06/current.md` round 17 entry and
`lemmas/vacuous-self-absorption-lemma.md` — `N(Q) ≤ 1 ⟹ S_0=Q` self-absorbing
(certified, unconditional). NTBT (`N(Q) ≤ 1` for all `a_1`) remains the open
conjecture; its numeric support is now stronger than reported (see Task 1).

### Dead ends (do not retry)
See Task 3 above — `type-alphabet-counting-bound` in its dispatched form,
`|S_k| ⊆ fixed finite ambient set`, direct `M_B`-bounding, and
`rogue-pair-termination-potential`-shaped "count resolved pairs" mechanisms.
Plus (H1, unchanged from round 17): 18 confirmed-dead FAH mechanisms,
3 consecutive fresh-framing sweeps (rounds 13/15/17) finding zero new H1
corridors.

### Small-case / intuition notes
- (Conjecture, strong new evidence) NTBT continues to hold on every tested
  seed including the previously-most-marginal case `a_1=255255`; the
  round-17 "one open candidate exception" language is now stale and should
  be corrected.
- (Conjecture, structural curiosity only) the target type's recurrence gaps
  for `a_1=255255` alternate `108730/54366` (ratio exactly 2) rather than
  being constant — unexplained, not pursued, possibly relevant to a future
  literal-period-length computation but not to H2/NTBT truth itself.
