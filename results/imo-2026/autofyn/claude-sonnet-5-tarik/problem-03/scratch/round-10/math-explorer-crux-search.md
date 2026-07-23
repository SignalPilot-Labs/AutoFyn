## imo-2026-03 — crux-corpus scouting pass for the Match-Recovery Lemma

Scope note: this is a retrieval/scouting pass only, per dispatch. No proof attempted, no
outline written. All corpus queries used the exact field names from
`crux_moves_documentation.md` (`technique`, `how_used`, `domain`, `subtopic`), filtered by
`domain` (combinatorics/algebra, occasionally number_theory) then scanned by keyword and by
`subtopic` (`games-and-strategy`, `extremal-principle`, `processes-and-algorithms`,
`double-counting`, `graph-theory-and-connectivity`). Read `past_problems_database.json` for
full statement+solution of every candidate before judging analogy.

### The precise target (for reference, from potential-weighting-upper-bound.md §13.2–§13.3)

Sorted `Z=(z_1≥...≥z_q)`, background `B`. Trichotomy on `z_1`'s fate: DELETE (bijective, free),
KEEP (closed form via General Rank-Extraction Identity, free), MATCH (bijective map to a
smaller instance, but the *branch value* needs `TAGGED` — the non-crossing, split-respecting
restriction — which is NOT free: individual per-`k` equality `A_{3,k}=B_{3,k}` fails ~30% of
random trials). **Match-Recovery Lemma (open):** if the unrestricted MATCH minimum strictly
beats DELETE and KEEP, some `k` (not necessarily the argmin) has `TAGGED` value `≤` that
minimum. The known negative result: the *un-conditioned* MATCH-only aggregate (ignoring
DELETE/KEEP) is FALSE (3/500 counterexamples) — DELETE/KEEP compensation is load-bearing.

### Distinct openings surfaced by this pass

**Opening 1 (strongest new find) — "charge the obstacle, not the case": aimo-0043's
peeling-induction with resource transfer between branches.**
`aimo-0043` (mine-avoiding lattice paths, prove ≥`2^{n-|M|}` paths) has EXACTLY the shape the
dispatch asked for: a naive two-branch case split (paths through `(1,0)` vs `(0,1)`) where, if
BOTH branches are live, IH gives `2^{n-1-|M|}+2^{n-1-|M|}=2^{n-|M|}` for free (this is
Match-Recovery's easy "global min at DELETE or KEEP" sub-case, already closed in §13.3). But if
one branch is dead (say no path via `(0,1)`), the naive fallback ("just use the surviving
branch with the SAME `|M|`") is lossy by exactly a factor of 2 — the same shortfall shape as
Match-Recovery's MATCH-only aggregate failing. The fix: **the branch's death is not accidental —
it is CAUSED by an identifiable element of `M`** (some `(0,k)∈M` blocking the axis), and that
element can be legitimately *subtracted from the surviving branch's own resource budget*
(`|M|-1` instead of `|M|`), because it played no further blocking role there. This "charge the
diagnosed obstacle against the compensating branch's ledger" move is the precise mechanism
class the dispatch's item (a) is asking for, and it is a genuinely different proof shape from
the population's current "prove an existential recovery statement by search/induction-on-`q`"
approach (§12.2, already shown in §13.3 to be circular/no-reduction).
**Adaptation sketch (untested, a hint only):** when the global MATCH-minimum is attained
strictly at some `k*` and its `TAGGED` value `B_{3,k*}` is expensive (crossing-taxed), the tax is
caused by a specific structural obstruction — an intervening element `z_j` (`1<j<k*`) that
`(1,k*)` would have to cross. Instead of hunting for "some other `k`" (existential, the
population's current framing, already known to need aggregation), try a *direct accounting*
identity: show the crossing tax incurred by `(1,k*)` equals (or is dominated by) a
correspondingly-sized *saving* obtainable by DELETING or KEEPING that same obstructing `z_j`
— i.e. redirect the compensation to a *specific, algebraically identified* element rather than
an unspecified alternative match partner. This would replace the open existential claim with a
closed accounting identity, structurally mirroring aimo-0043's "subtract the blocking mine from
the surviving branch's budget."

**Opening 2 (already flagged in the file, §12.3, independently re-confirmed as apt) —
aimo-0558's forced-inclusion/charge-to-distinct-skip.** Verified the crux is real (not
mis-remembered): `aimo-0558` (ISL C7/Czech 2022, `±1`-sequence gap-≤2 subsequence, answer
`C=506`) proves its *lower bound* (achievability) half via a greedy that always takes the
majority sign and skips a minority element only when forced, then constructs an EXPLICIT
injection {included minority elements} → {a distinct skipped minority element immediately
before it}, capping the minority contribution at `⌊majority-count/2⌋`. This is a genuinely
different technique from Opening 1: instead of "diagnose the obstacle and transfer it between
two branches of a case split," it is "run one greedy policy and prove an aggregate cap via an
explicit injection from bad outcomes to good ones." Useful if a future attempt tries to
construct an explicit non-crossing selection achieving the Match-Recovery target directly
(rather than reasoning about `OPT` abstractly) — the injection technique could plausibly map
"positions where the non-crossing restriction forces a suboptimal match" to "a distinct
DELETE/KEEP compensation opportunity," giving a constructive (not existential) proof.
Read the full problem+solution independently (not just the crux stub) — confirms the
`technique`/`how_used` fields accurately describe a real, load-bearing move (5 independent
crux-extraction passes on this one problem in the corpus, all consistent).

**Opening 3 (new, a different proof *shape* — Hall/defect-Hall + iterated peeling) —
aimo-0063's cupcake-partition problem.** `aimo-0063` (`m` cupcakes on a circle, `n` people,
partition-and-distribute) proves an existence-of-compatible-assignment claim via: pick one
"anchor" person's own valid partition into `n` arcs, try to Hall-match all `n` people to those
`n` arcs; if Hall's condition fails for some bad set `B₁` of people, **delete `B₁` and its
whole neighborhood, match everyone outside `B₁` first (a genuine, non-circular sub-instance),
then recurse via strong induction on the leftover people/arcs** (the anchor person is always a
"universal vertex" that can't be deleted, guaranteeing termination). This is a structurally
different mechanism from Openings 1–2: it recasts an "exists a good assignment/index"
existential claim (exactly the Match-Recovery Lemma's shape: "some `k` works") as a **bipartite
matching feasibility problem**, solvable via Hall's theorem (cited in `knowledge_base.md`'s
"Hall's marriage theorem / SDR" entry) plus iterated deficient-set removal when Hall fails
outright. **Adaptation sketch (untested):** build a bipartite graph with one side = candidate
match partners `k∈{2,...,q}` and the other side = "target slots" that need to be filled at
value `≤` the global MATCH minimum; if a naive one-to-one matching (`k↔` its own `TAGGED` value)
fails Hall's condition for some subset of partners, peel that subset off (à la aimo-0063) and
recurse on the smaller residual `Z`. This is speculative — the Match-Recovery Lemma's own
"target" isn't obviously a saturating-matching statement, so translating it into Hall's
framework first needs real work — but it is a genuinely different top-level proof *shape*
(existence-via-matching-feasibility, not existence-via-induction-on-list-size) worth having in
the population if the current recursive-on-`q` framing (already shown circular, §13.3) stays
stuck.

**Weaker/rejected candidate — aimo-0719 (right-down/right-up path partition lower bound).**
Its crux ("compensating count: forbid a cheap pairing type from occurring twice via planarity,
forcing the saved cost to reappear as an expensive type") has the right *narrative* shape
(shortfall in one place recovered as cost elsewhere), but the actual mechanism (laser-mirror
bijection through a grid, non-crossing beam types) is deeply geometry/planarity-specific with
no clean translation to a 1-D sorted-list peeling recursion. Report as a weak structural
echo only, not a genuine adaptation candidate — do not spend a round translating it.

**Re-confirmed dead end (not a new finding, cross-checked):** per round-6's math-explorer note
(rule 19 in `/tmp/memory/math-explorer.md`), the corpus has no literal signed/rank-coupled
alternating-sum matching-optimization analog. This pass's broader keyword sweep (crossing,
non-crossing, matching, exchange, rearrangement, compensation, recovery, charging — 356+498
raw hits across both keyword families) turned up nothing closer than aimo-0558 (already known)
and the two new finds above (aimo-0043, aimo-0063) — confirming, not contradicting, the
round-6 finding that this is a genuinely under-represented problem shape in the corpus.

### Candidate technique(s) to hand to the outliner
1. **Obstacle-charging / resource-transfer between branches of a case split** (aimo-0043) — the
   single best-matching crux for dispatch item (a); a genuinely different framing from the
   current population's recursive-induction-on-`q` route (§12.2, already diagnosed circular).
2. **Explicit greedy + injective charge-to-a-distinct-witness** (aimo-0558, already flagged,
   independently reconfirmed apt) — a constructive alternative to reasoning about `OPT`
   abstractly.
3. **Hall's theorem / defect-Hall + iterated deficient-set peeling** (aimo-0063, new) — recasts
   the existential "some `k` works" claim as a bipartite-matching-feasibility claim; speculative
   translation effort required, flagged as an unexplored proof *shape*, not a ready plan.

### Cheap-kill candidates
None obvious for the Match-Recovery Lemma itself (it is a deep aggregation fact, not amenable
to a one-line parity/pigeonhole kill) — this matches the population's own assessment across
5+ rounds. One easy sanity/scoping check worth running before investing a round in Opening 3:
verify computationally whether the "one-to-one Hall-style" reading of Match-Recovery (each `k`
needs its own dedicated target slot) is even the right translation, or whether the true target
is inherently many-to-one (several `k`'s could jointly satisfy the aggregate bound) — if
many-to-one, Hall's theorem doesn't directly apply and Opening 3 needs a generalized
(defect/many-to-one) version first.

### Knowledge-base entries to use
- **Hall's marriage theorem / SDR** (`knowledge_base.md`, Combinatorics section) — directly
  citable if Opening 3 is pursued.
- **Invariants & monovariants**, **Constructive/incremental** (KB Combinatorics section) —
  generic framing for Opening 1's "identify and transfer a specific quantity between branches"
  mechanism, though the KB has no entry specific enough to cite as the actual tool (would need
  to be proved from scratch either way, per CLAUDE.md's crux rule).
- Nothing in the KB's Algebra/Number Theory/Geometry sections is closer than these two.

### Analogous past problems (cruxes) — ranked
1. **`aimo-0043`** (new this pass) — mine-avoiding lattice paths, `≥2^{n-|M|}` paths. Crux:
   two-branch peeling induction with an obstacle-charging mechanism (a dead branch's blocking
   element is subtracted from the surviving branch's own resource budget) that exactly recovers
   the factor lost by the branch's death. **Best structural analog found for Match-Recovery's
   DELETE/KEEP-compensates-MATCH-shortfall pattern** — a genuinely different framing from the
   population's current recursive-on-`q` route.
2. **`aimo-0558`** (already known/flagged in the file, re-confirmed apt this pass) — `±1`
   gap-≤2 subsequence, `C=506`. Crux: greedy + explicit injective charge from forced-includes to
   distinct skips, proving an aggregate bound without solving per-position.
3. **`aimo-0063`** (new this pass) — cupcake circular partition/assignment. Crux: Hall's
   theorem + iterated deficient-set-peeling induction for an existential "good assignment
   exists" claim. Weaker/more speculative fit (translation to the Match-Recovery setting is
   nontrivial and untested) but offers a genuinely different top-level proof shape.

No closer matches exist in the corpus for the *specific* signed/rank-coupled, sorted-multiset,
3-branch (DELETE/KEEP/MATCH) aggregate-equality structure — this reconfirms round 6's finding
that the problem's core difficulty is genuinely underrepresented in the pre-2026 corpus; the
above three are hints to adapt, not ready-made proofs (per CLAUDE.md, every borrowed step still
needs to be proven from scratch).

### Prior progress
Current best (from `potential-weighting-upper-bound.md`, round 9, reviewer-certified): the
lower bound against `D_m` is fully unconditional for every `m` (rounds 5+8, a separate
milestone, not touched by this pass). The upper bound is fully reduced to the single
Match-Recovery Lemma above; DELETE, KEEP, and the MATCH bijection are all proved free; only the
MATCH branch's `TAGGED`-vs-`OPT` aggregate equality remains open, with a decisive negative
result already on file ruling out the un-conditioned (ignore-DELETE/KEEP) strengthening.

### Dead ends (do not retry)
- Per-partner (non-aggregated) equality `A_{3,k}=B_{3,k}` for a fixed `k` — FALSE (round 8/9,
  exact counterexamples).
- Un-conditioned MATCH-only aggregate ignoring DELETE/KEEP compensation — FALSE (round 9,
  `3/500` counterexamples).
- Treating the recursive strong-induction-on-`q` skeleton (§12.2) as an independent reduction
  in difficulty — proved NOT to reduce difficulty (round 9, §13.3): its one non-free branch
  needs the identical aggregated content, recursively, at every background size.
- Local pairwise uncrossing-exchange as a proof technique for the general non-crossing
  conjecture — proved not to work (rounds 6–7, exact counterexample).

### Small-case / intuition notes
No new small-case computation performed this pass (scouting/retrieval only, per dispatch scope
— extensive small-case verification of the Match-Recovery Lemma itself already exists on file,
500+ trials, 0 failures for the full aggregate). The aimo-0043 analogy is structural, not yet
numerically cross-checked against Match-Recovery's own data — a natural next step for a builder
adopting Opening 1 would be to check, on the existing `3/500` MATCH-only-aggregate
counterexamples, whether the shortfall is exactly recoverable by an "obstacle transferred from
MATCH to DELETE/KEEP" accounting (conjecture, untested).
