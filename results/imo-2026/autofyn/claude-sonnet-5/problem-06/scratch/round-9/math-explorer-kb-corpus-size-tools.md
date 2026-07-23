## imo-2026-06 (lens: KB/corpus search for SIZE-bounding, not COUNT-bounding, tools)

**Scope of this report.** Per dispatch, I searched `knowledge_base.md` and the crux
corpus (`past_crux_moves_database.json`/`past_problems_database.json`, per
`crux_moves_documentation.md`'s exact field names) specifically for techniques that
bound the SIZE of a single object produced by a greedy/extremal/recursive
construction, as opposed to counting how many such objects exist — i.e. candidates
for `(UB_S)`: `sup{|rad(a_i)∖S| : i∈I_S}<∞` (equivalently `sup_{n∉I_{P_1}}ω(a_n)<∞`).
I did **not** attempt a proof; this is a terrain report only.

### Searches run and results

**1. `knowledge_base.md`, full read (247 lines).** No entry bounds `ω(m)` (number of
distinct prime factors) directly for any structured/constrained integer set. The
closest entries are generic and structurally the wrong shape:
- "Divisor analysis" (`d(n)`, gcd structure) — bounds divisor COUNT of a fixed `n`,
  not `ω` of a member of an evolving family; no transfer.
- "Extremal graph theory: edge-count thresholds force substructures" — this is the
  *only* KB entry resembling "max degree/clique size in an evolving graph." It is
  a one-line pointer with no explicit max-degree-bounding technique attached; on
  inspection it is aimed at forcing substructures from edge-count thresholds
  (COUNT-side), not at capping a single vertex's degree. **Not transferable as
  stated** — would need to be built from scratch if used at all, and there's no
  natural graph encoding here that turns "ω(a_n) bounded" into a max-degree claim
  (the natural graph — vertices = indices, edges = shared prime — has `a_n`'s prime
  set as a *hyperedge label*, not a vertex degree; recasting would require a
  different graph, e.g. primes-as-vertices with `a_n` as a hyperedge of size
  `ω(a_n)`, at which point "bound `ω(a_n)`" is just "bound hyperedge size," a
  restatement, not a reduction to a known tool).
- No VC-dimension / Sauer–Shelah entry exists in the KB at all (checked General
  Proof Methods, Combinatorics, Combinatorial Geometry sections — absent).
- No "potential function / amortized analysis for greedy algorithms" entry exists
  either — the closest, "Invariants & monovariants," is a one-line generic pointer,
  no worked amortized-charge machinery of the shape needed.

**2. Crux corpus, `subtopic=size-bounding-and-descent` (the most on-target
subtopic), both domains.** `number_theory`: 120 cruxes, read in full (titles +
`how_used`). `combinatorics`: 4 cruxes, read in full with problem statements.
**None bound `ω(m)`/number-of-distinct-prime-factors for a term of a growing,
self-referential (greedy/gcd-chain) sequence.** The techniques found split into
three buckets, all structurally mismatched:
  - *Bounded-ambient-set descent* (aimo-0028, aimo-0173, aimo-0211, aimo-0356,
    aimo-0503): these all crucially use a FIXED finite reference object (`a_1`, a
    known square `B²`, a bounded interval) to trap a growing quantity. **This is
    exactly the mechanism `NEVER`-flagged in `/tmp/memory/math-explorer.md` (round
    6 entry): imo-2026-06's proper-core companion bundles have no such fixed
    ambient bound** — recruited primes are unboundedly large with no reference
    integer to sit inside. Confirms the round-6 finding rather than adding a new
    angle.
  - *Ω(m)-LOWER-bound-by-induction* (aimo-0138, aimo-0098): these show a
    quantity `Ω` (with multiplicity) grows or is pinned via an *algebraic identity*
    (Aurifeuillian factorization, a functional equation forcing `f(p)` constant on
    primes). Wrong direction (we need an upper bound) and wrong mechanism (no
    algebraic identity of this kind exists for `a_n`, which is defined by a
    minimality/greedy condition, not a closed algebraic formula).
  - *"Finitely many primes divide any value" arguments* (aimo-0212, aimo-0682,
    aimo-0727, aimo-0851): these bound `ω`/prime-support by first proving all
    relevant primes lie in *one fixed finite set* (via a polynomial-value /
    resultant / Bezout argument, or a "bounded multiplier forces bounded prime
    support" contradiction). **This is structurally the same move as
    `forced-primes-well-ordering`'s `S^+`/`S^{++}` mechanisms already tried and
    refuted this workspace (Vacuity Proposition, Intersection-Fragility
    Proposition, `lemmas/lemma-vacuity-and-intersection-fragility.md`)** — pure
    prime-set-fixing cannot recover a prime absent from even one class member, and
    these corpus cruxes all rely on an algebraic/polynomial rigidity (Bezout
    resultant, "prime > all coefficients ⟹ can't appear") that `a_n`'s
    minimality-defined recursion does not have an analogue of. **Do not
    resurrect S^+/S^{++}-style fixed-prime-set arguments under a new name from
    this corpus family — already dead for the reason given in round 8's certified
    negative lemma.**

**3. Targeted keyword sweeps** (`distinct prime factors`, `omega(`, `radical`,
`squarefree`, `max degree`, `maximum degree`, `clique`, `potential function`,
`amortiz`, `exchange argument`, `greedy`, `VC-dimension`/`Sauer-Shelah`, `finitely
many primes`) across all 2434 cruxes, both domains. Found:
  - `aimo-1025`/`aimo-0645` (combinatorics, clique-cover potential functions) — the
    genuine "potential-function bounding an evolving object" pattern the dispatch
    asked me to check. On inspection, both bound a SUM/COUNT (total edges covered
    by a clique cover; number of maximal cliques through a vertex, capped at 2 via
    a parity/coboundary argument on TRIPLES) — again count-of-pieces, not the size
    of one recursively-constructed object growing without an external anchor.
    `aimo-0019`'s amortized-ink potential is the closest true "amortized charge
    against a monotone frontier" mechanism in the corpus, but it bounds a
    CUMULATIVE resource (total ink spent) against linear progress of a frontier —
    again a sum/count bound with a built-in linear anchor (`3x_r`), not a
    per-object size bound with no anchor.
  - `aimo-0102` (halving/pigeonhole greedy) — bounds a COUNT (hidden numbers)
    via geometric decay, same count-not-size shape.
  - No VC-dimension/Sauer–Shelah crux exists anywhere in the corpus (0 hits for
    those terms across all 2434 entries).
  - `aimo-0421` (infinite-set gcd pigeonhole: "every prime divides finitely many
    elements ⟹ pick a third element coprime to a bad pair") is the single closest
    analogue in spirit (an infinite set + prime-divisibility dichotomy), but its
    crux move is a pigeonhole EXISTENCE argument (produce *some* triple with a
    property), not a uniform SIZE bound on a growing per-index quantity — the
    problem shape (find 3 elements with a gcd-inequality pattern) doesn't
    resemble bounding `ω(a_n)` closely enough to adapt.

### Assessment of each candidate family (per dispatch's request)

- **Explicit `ω(m)` bounds for structured `m`.** Absent from both KB and corpus.
  The only generic fact available (not corpus-retrieved, standard analytic NT) is
  the *maximal order* `ω(m) = O(log m / log log m)` (attained by primorials) —
  this is a TRUE but far too weak bound (grows without limit; we need `O(1)`), and
  it is a worst-case-over-all-integers bound, not conditioned on the gcd-chain
  minimality structure `a_n` actually has. Citing it would give zero content
  (already implicitly known: `ω(a_n) ≤ log₂ a_n` trivially, an old, already-
  superseded round-3 bound). **Not a viable route as-is** — the required `(UB_S)`
  bound is a problem-specific structural fact, not a generic number-theoretic
  ceiling; nothing in the corpus supplies a sharper generic tool.
- **Extremal graph theory / max-degree bounds.** No usable KB or corpus entry;
  the natural graph encoding (primes-as-vertices, `a_n` = hyperedge) turns
  "bound `ω(a_n)`" into "bound hyperedge size," which is a relabeling of the open
  question, not a reduction to a known extremal-graph-theory result. **Does not
  transfer**, and I could not find a graph model where `ω(a_n)` becomes an actual
  vertex-degree (as opposed to a hyperedge/set size) — degree bounds in the corpus
  (aimo-0137, aimo-0230, aimo-0295) all concern genuine simple-graph vertex
  degree, structurally unrelated.
- **Potential-function / amortized-analysis (greedy-algorithm) arguments.**
  Present in the corpus (aimo-0019, aimo-1025, aimo-0645, aimo-0102) but every
  instance bounds a CUMULATIVE/COUNT quantity via a monotone anchor (frontier
  progress, total original edges, vertex-clique-membership count via parity). None
  bounds the size of a single recursively-produced object with no external
  anchor — which is precisely `(UB_S)`'s difficulty (no fixed ambient bound
  exists for proper-core recruited primes, confirmed round 6). **Structurally the
  same "count, not size" limitation already diagnosed for the pigeonhole/Δ-system
  machinery (rounds 6–8) — these corpus techniques would hit the identical wall,
  not a new one.**
- **VC-dimension / Sauer–Shelah / set-system size bounds.** Zero presence in
  either KB or the 2434-entry corpus. No assessment possible beyond "absent
  tool" — if pursued, it would have to be built from scratch with no crux
  precedent, and I see no natural set-system structure in this problem (the
  radical sets `rad(a_i)` are not obviously VC-bounded — there is no forbidden
  shattered-pattern argument visible from the problem's minimality rule).
- **Any crux with a "greedily construct next term, bound a size-parameter"
  shape.** The single closest match by problem *shape* (greedy sequence, minimal
  next-term rule) is **`aimo-0727`** (Netherlands, `a_{k+1} | 2(a_1+…+a_k)`,
  prove infinitely-many-primes-dividing-some-term ⟹ every `n` eventually
  divides some term). Its crux ("bounded multiplier ⟹ finite prime set,
  contradicting infinitely-many-primes hypothesis") is a NECESSITY argument in
  the opposite direction of what we need (it shows a quantity is unbounded from
  a hypothesis of unboundedly many primes; our target is to show `ω(a_n)` IS
  bounded) and depends on an explicit closed recurrence (`b_{k+1}a_{k+1} =
  (b_k+2)a_k`) that `imo-2026-06`'s greedy-gcd rule has no analogue of (no such
  telescoping algebraic identity is available here — already confirmed absent by
  round-3/4's search for algebraic recurrences). **Not transplantable**, though
  worth noting as the nearest surface-level analogue in the whole corpus.

### Candidate technique found worth flagging (not developed, structural note only)

None of the searched techniques transfer. The one genuinely new observation from
this search (not a proof step, a framing note for the outliner): every corpus
technique that bounds a per-object SIZE (not a count) does so by anchoring the
object to a FIXED external reference (a_1, a known square, a bounded interval,
Bezout's constant term, a polynomial's coefficients). `(UB_S)`'s companion bundles
have **no such fixed anchor** by construction (the whole point of a proper,
non-top core is that its companion primes range over an a priori unbounded set).
This suggests, as a structural diagnosis (not a fix), that **any correct
`(UB_S)` proof must manufacture its own anchor from the sequence's own
recursive/minimality structure** (e.g. the greedy "smallest such integer" rule
itself, or the already-certified growth bound `a_{n+1}-a_n ≤ rad(a_1)`) rather
than import one from outside — which is consistent with, and reinforces, round
8's own diagnosis that this needs a "genuinely problem-specific insight," not a
technique transplant. I found no such problem-specific anchor construction in my
search; this is a diagnosis, not progress.

### Cheap-kill candidates
None obvious from this search specifically (this lens is a retrieval search, not
a structural-pruning pass) — see the persistent-backbone-monovariant /
forced-primes-well-ordering files for the existing structural facts (Escape-
Confinement Lemma, growth bound `a_{n+1}-a_n≤rad(a_1)`) that any new attempt
should build on rather than re-derive.

### Knowledge-base entries to use
None found that transfer to `(UB_S)` directly. For context/completeness, the KB
entries already load-bearing elsewhere in this workspace remain: CRT/modular
arithmetic (used throughout), pigeonhole/extremal principle (used for the
already-exhausted count-bounding machinery), "prune before you compute" meta-note
(motivated this search itself).

### Analogous past problems (cruxes)
- **`aimo-0727`** (Netherlands, greedy divisibility-chain sequence,
  `subtopic=size-bounding-and-descent`/`divisibility-and-gcd`) — closest by
  surface shape (greedy next-term rule on an integer sequence, prime-support
  question) but its crux mechanism (explicit closed recurrence + necessity
  argument, opposite direction) does not transplant; flagged above, not
  recommended for reuse beyond noting the shape-similarity.
- No other crux found to be a genuine analogue for `(UB_S)` specifically (as
  opposed to the whole problem, already searched exhaustively in rounds 3 and 6
  per `/tmp/memory/run_state.md`'s Rules). **I could not find 1–3 genuinely
  analogous cruxes for this exact sub-question** — the honest finding is "none,"
  consistent with rounds 3/6's prior confirmations that this workspace's core gap
  has no corpus precedent.

### Prior progress
See `results/imo-2026-06/current.md` round-8 update: the whole problem is
unconditionally reduced to `(UB_S)` (Theorem-UBS-sufficiency,
`lemmas/theorem-UBS-sufficiency.md`). `(UB_S)` itself is untouched; numerically
`max ω(a_n)` off the top core stays single-digit in all tested hard cases (247→6,
2747→6, 21528751→7), consistent with but not proving `(UB_S)`.

### Dead ends (do not retry)
- Bundle-COUNT-bounding techniques (Escape-Confinement, RBD/ERD, S^+/S^{++},
  Δ-system/sunflower dichotomy) — proven round 8 to structurally bound count, not
  size; this round's search found no corpus technique that escapes the same
  count/size distinction (see "Assessment" above — every corpus size-bounding
  technique found relies on a fixed external anchor `(UB_S)`'s bundles lack).
- Fixed-prime-set arguments modeled on aimo-0212/aimo-0682/aimo-0727/aimo-0851
  (Bezout/resultant/bounded-multiplier "all primes lie in one finite set")
  — same mechanism as the already-refuted `S^{++}` (Vacuity/Intersection-
  Fragility Propositions); the algebraic rigidity these corpus proofs need
  (a fixed polynomial, a fixed linear recurrence) has no analogue in
  `imo-2026-06`'s minimality-defined recursion.
- Generic analytic/probabilistic tools — reconfirmed absent per dispatch context
  (rounds 3, 6); not re-searched this round per explicit instruction.

### Small-case / intuition notes
Not applicable to this report (a corpus/KB terrain search, not a numeric probe) —
see round 8's `current.md` for the existing verified numerics (`max ω(a_n)`
single-digit in all tested cases through `N≤3000`), which I did not re-run since
this lens's mandate was retrieval, not re-simulation, and no new numeric question
arose from the search.
