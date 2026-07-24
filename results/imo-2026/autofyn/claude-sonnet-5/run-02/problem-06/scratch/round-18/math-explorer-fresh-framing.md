## imo-2026-06 — fresh-framing search for FAH (round 18, dedicated "genuinely new corridor" lens)

### Summary verdict
Found **one genuinely new candidate framing** not represented anywhere in the
17-round dead list: recasting the problem as a **complete graph on the index
set colored by shared-prime data** and importing the **triangle-forcing
pigeonhole technique** of ISL 2021 N8 (crux corpus `aimo-0866`/`aimo-0421`).
This is structurally different from every dead mechanism (it is not
existential-witness recruitment, not magnitude-sandwich, not
minimality/competitor-construction, not CRT-glue, not density/sieve, not an
automaton/transition-map walk, not well-ordering/measure descent, not
ultrafilter/compactness, not per-prime decomposition). It is a genuine
"identity-pinning via inter-triple consistency" mechanism, which is exactly
the category the round-11 diagnosis says is missing. I did **not** find any
other qualifying new corridor after a systematic sweep of (a) analytic
number theory, (b) a_1's CRT structure, (c) probabilistic heuristics, (d)
non-number-theory corpus techniques — details below. I recommend the round
put ONE approach on this new corridor and, in parallel, spend real effort
consolidating/polishing the Master Conditional Theorem + `2|a_1` deliverable
as insurance, per the plateau-break guidance.

### The new opening: gcd-colored complete graph / triangle-forcing pigeonhole

**Structural match, confirmed exact.** The certified, unconditional **Free
Facts Lemma** (`lemmas/free-facts-gcd.md`) already proves `gcd(a_i,a_j) > 1`
for **every** pair `i < j`, not just consecutive indices (one line: apply the
defining property of `a_j` at index `j-1`, using `i ≤ j-1`). This means the
whole sequence, viewed as an index set, is *literally* the complete graph `K_∞`
on which the crux corpus problem ISL 2021 N8 (`aimo-0866`, German original
`aimo-0421`) operates: color edge `{i,j}` by `c(i,j) := gcd(a_i,a_j)` (or,
refined, by a canonically-chosen shared prime). Every vertex's incident edges
take only finitely many colors relative to any FIXED reference vertex (since
`gcd(a_m, ·)` only takes values among the finitely many divisors of `a_m`), which
is the exact "pigeonhole a fixed vertex's divisor set" step the ISL N8 proof
opens with — a structural coincidence, not a stretch: this workspace's own
`Bounded Witness Lemma` / `Finite Core Theorem` already rely on the same
finiteness-of-divisors fact, just never organized as a colored-graph
argument.

**The technique (`aimo-0866` crux, adapted, not directly transplantable —
adaptation is the open work for the outliner/builder):**
1. Fix a reference term `a_m`. Pigeonhole an infinite index set `X` on which
   `gcd(a_m, a_x)` is constant (`= d`), using only finiteness of divisors of `a_m`.
2. Pick an outside index `y` with `gcd(a_m,a_y) ≠ d`.
3. Pigeonhole again: within `X`, find `x_1, x_2` with `gcd(a_y,a_{x_1}) =
   gcd(a_y,a_{x_2}) =: d'`.
4. A short case split (`d = d'` vs `d ≠ d'`) forces a **triangle among three
   actual terms** where two of the three pairwise gcds coincide and the third
   differs — i.e. it extracts *cross-triple* consistency information, not
   single-pair existence/magnitude information.

This is precisely the missing ingredient the round-11 diagnosis names: a
mechanism that pins down relationships *between* multiple far-apart terms'
factorizations simultaneously, rather than recruiting one witness prime at a
time. Whether the triangle-forcing conclusion (a bi-colored triangle exists)
can be turned into a proof that two persistent types A', B' *must* intersect
(FAH) is NOT established here — that is exactly the gap the next round's
outliner/builder must attack; I have deliberately stopped at "here is a
structurally new tool," not developed it into a proof.

**Where the adaptation is nontrivial (flag for the outliner, not resolved
here):** `aimo-0866`'s conclusion is "a bi-colored triangle exists" — a much
weaker statement than FAH's "every two persistent types intersect." The
outliner will need to either (i) run the triangle-forcing pigeonhole
specifically among terms of the two disjoint persistent types A, B (not
arbitrary terms) to try to force a shared prime between them directly, or
(ii) use it to derive some other exploitable rigidity (e.g., a bound on how
many distinct gcd-values/colors can appear against a single persistent-type
representative, which the KB does not yet have). Neither direction is
attempted or verified feasible here — flagged as the actual work.

### Systematic sweep of the other three prompted directions — all came up empty

**(a) Analytic NT (Dirichlet series / multiplicative functions).** No
natural analytic object presents itself: the sequence's terms are not a
multiplicative function of `n`, there's no natural Dirichlet series whose
analytic continuation would encode "which prime persists" (an identity-level,
not an asymptotic-density, question). The already-dead
`sieve-density-exception-bound`/`Density-Argument Vacuity` findings show
*why*: the greedy selection rule is a Boolean predicate (`gcd(c,a_i)>1`)
consulting no aggregate/averaged statistic, so any analytic-density tool is
structurally blind to it (Selection-Rule Class-Blindness, already certified).
This rules out Dirichlet series/analytic-density approaches for the same
proved reason, not merely "not tried" — do not re-open this without a
concrete class-sensitive analytic object, which none of my search turned up.

**(b) CRT/multiplicative structure of `a_1` itself.** This is genuinely
under-exploited (the diagnosis is right that it's "barely exploited"), but
the *specific* mechanisms that would use it — CRT-glue competitor
construction, covering-system construction — are exactly the confirmed-dead
family (CRT Magnitude Obstruction, 8 orders-of-magnitude overshoot,
independently reconfirmed round 11). The one CRT-flavored idea not yet dead
is the graph-coloring approach above, which does use `a_1`'s (and other
terms') divisor-set finiteness, but via pigeonhole not via explicit
construction — that's the escape from the CRT-glue dead end's specific
failure mode (magnitude blowup from explicitly building a competitor number).

**(c) Probabilistic/random-model heuristics made rigorous.** Considered a
"random greedy process" second-moment/concentration argument (e.g., model
each `a_{n+1}-a_n` as roughly a random variable over residues avoiding a
covering set, argue concentration forces a fixed period). This is
structurally the same shape as the already-dead sieve/density family (an
aggregate/statistical argument over a class-blind selection rule) — the
Selection-Rule Class-Blindness argument applies verbatim to any probabilistic
model built from the same rule, since the rule itself never references
statistical/averaged information. No rigorous rescue found; not a new
corridor, just a relabeling of a dead one.

**(d) Corpus techniques from combinatorics/algebra outside number_theory.**
Searched `combinatorics` (subtopics `processes-and-algorithms`,
`invariants-and-monovariants`, `pigeonhole`, `bijections-and-encoding`) and
`algebra` (`sequences-and-recurrences`) for "identity-pinning" cruxes with no
number-theoretic flavor. Nothing surfaced that resembles FAH's shape (proving
a specific relation holds between ALL sufficiently-far-apart pairs from two
infinite classes, given only pairwise non-coprimality); the closest hits
(`aimo-0079`, `aimo-0134`, `aimo-0678`) are all already-known-dead families
in this workspace (monovariant/difference-identity, already ruled out
16th-mechanism-dead) or Omega-parity periodicity arguments not applicable
here (no analogous parity invariant found — Omega(a_n) is not shown periodic
by anything in the workspace and doesn't obviously help pin down WHICH prime).
The gcd-colored-graph technique (found via `divisibility-and-gcd` /
`pigeonhole` subtopics, not the ones the dispatch suggested) is the one
genuine hit; I did not find a second.

### Candidate technique(s) for the outliner
- **Primary new lead:** triangle-forcing pigeonhole on the gcd-colored
  complete graph (`aimo-0866`/`aimo-0421` crux), adapted to persistent types.
  Genuinely new to this workspace (grep of `knowledge_base.md` for
  "coloring/triangle/monochromatic" returns nothing relevant).
- Everything else checked is either already-dead or reduces to an
  already-dead mechanism for a proved structural reason (class-blindness).

### Knowledge-base entries to use
- `knowledge_base.md` "Pigeonhole / extremal principle" entries (general
  pigeonhole guidance, lines ~108, ~188) — generic, applies to the new
  triangle-forcing setup's two nested pigeonhole steps.
- No KB entry currently covers graph-coloring/triangle-forcing arguments —
  this would be a genuinely new KB technique if it works, worth certifying.

### Cheap-kill candidate to run before a full build
Before committing a full approach/build cycle: check on 2-3 concrete seeds
(e.g. `a_1=175`, `a_1=4807`) whether the triangle-forcing pigeonhole, run
specifically with `v = a_m` a canonical witness of persistent type A and `y`
a canonical witness of persistent type B, actually produces a bi-colored
triangle whose "differing color" edge is informative about A∩B (rather than
about some irrelevant third type C) — a 10-minute numeric probe that could
kill or validate the adaptation's core step before investing a full round.

### Analogous past problems (cruxes)
- **`aimo-0866`** (ISL 2021 N8 English) and **`aimo-0421`** (same problem,
  German statement) — genuinely analogous: both hinge on the fact that
  `gcd(fixed, ·)` takes finitely many values (divisors of the fixed integer),
  exploited via nested pigeonhole + a 2-case triangle argument to force
  identity-level (not just existence-level) relations among gcd values. This
  is a strong structural analogy to FAH's needed "which prime, provably,
  divides infinitely many terms of BOTH types" gap — not previously present
  in this workspace's crux search history (the earlier rounds searched
  number_theory `pigeonhole`/`divisibility-and-gcd` less systematically for
  graph-coloring-shaped problems specifically).
- Everything else in the `sequences-and-recurrences` subtopic
  (`aimo-0079`, `aimo-0134`, `aimo-0278`, `aimo-0374`, `aimo-0378`) is either
  already a confirmed-dead family here or not genuinely analogous (different
  shape: difference identities, polynomial recurrences, hypergeometric
  closed forms — none involve identity-pinning across an infinite
  gcd-colored structure).

### Prior progress
See `current.md` — unchanged by this exploration: `2|a_1` subfamily fully
solved (Even-Seed Literal Periodicity Theorem); general case reduced to H1
(FAH, 17+ dead mechanisms) ∧ H2 (absorption-chain termination) via the Master
Conditional Theorem. This report does not change that state; it proposes one
new candidate mechanism for H1 only.

### Dead ends (do not retry — confirmed, not re-verified here beyond the
dispatch's own list)
Existential/pigeonhole witness-recruitment; magnitude-sandwich; tautological-
minimality/competitor-construction (Lemma K family, Minimality Tautology
Lemma); CRT-glue; sieve/density (Density-Argument Vacuity, Escape-Cost
Vacuity, Sandwich Genericity); automaton/graph-walk transition-map
(`reversible-transition-map` — proved equivalent to the crux, a DIFFERENT
graph structure than the one proposed here — that one is a functional graph
of residue-class transitions, i.e. a walk/automaton; the new proposal is a
static edge-colored complete graph on term-indices with no walk/transition
structure at all); Morse-Hedlund; Central Sets/idempotent ultrafilter;
ultraproduct/compactness; per-prime indicator decomposition; transfer
operators; LP duality; well-ordering/minimal-counterexample descent (3
measures); seed-coupling induction. Also newly reconfirmed dead-by-reduction
here (not previously logged as explicitly killed, now diagnosed): analytic
Dirichlet-series/multiplicative-function approaches and probabilistic/
concentration heuristics, both killed by the existing Selection-Rule
Class-Blindness argument (the greedy rule consults no aggregate statistic),
so they inherit the sieve/density family's death for the same proved reason
— flag this explicitly so no future round re-opens either without a genuinely
new class-sensitive ingredient.

### Small-case / intuition notes (conjecture, not proof)
Not separately re-verified numerically this round beyond the structural
confirmation that Free Facts gives full pairwise (not just consecutive)
non-coprimality — this is a certified fact, not a conjecture, and is the
load-bearing premise for the graph-coloring reframing being literally
applicable (no numeric check needed, it's a one-line proof already
certified in `lemmas/free-facts-gcd.md`). Whether the triangle-forcing
technique actually yields FAH-level information when specialized to
persistent-type witnesses is genuinely open and should be the very first
thing next round's builder checks computationally (see Cheap-kill above)
before investing in a full proof attempt.
