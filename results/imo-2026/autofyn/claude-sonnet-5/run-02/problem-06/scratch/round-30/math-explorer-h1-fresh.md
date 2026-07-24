## imo-2026-06 (H1/H2 fresh-framing lens, round 30)

### Verdict up front
No genuinely new mechanism was found. Every candidate I checked against the
task's suggested list (Ramsey-type arguments, structural graph coloring,
algorithmic/computational-complexity arguments, analytic-NT sieve tools beyond
Legendre, a reformulation as a known combinatorial process, and "prove H1/H2
for a larger natural class instead of full generality") either (a) collapses
into an already-certified-dead mechanism in `results/imo-2026-06/approaches/`,
or (b) is provably orthogonal/inapplicable to the actual obstruction. This is
the 24th consecutive plateau round on H1 itself (rounds 6-30). Below is each
candidate with the concrete reason it dies, so the outliner does not have to
re-derive the refutation.

### What H1 (FAH) and H2 actually are, precisely (from current.md / Master
Conditional Theorem)
- Ground set: a finite "core" S of primes (Finite Core Theorem). Each index n
  gets an "extended-persistent type" ρ_S(n) ⊆ S (finite alphabet).
- H1 (FAH): for two extended-persistent types A, B with disjoint BASE
  (Q-level) types, do their occurrence sets intersect cofinitely/literally in
  the gcd>1 sense (i.e. does gcd(a_n,a_m)>1 for all/cofinitely many pairs
  n∈occ(A), m∈occ(B))? This is an "existential → universal/cofinite
  promotion" question for a specific disjoint pair (a "rogue pair"), not a
  statement about infinitely many pairs at once.
- H2: does the "absorption chain" S_0 ⊆ S_1 ⊆ ... (add a prime whenever a
  rogue pair is found) terminate in finitely many steps — equivalently
  (Termination Criterion Lemma, certified round 15), is the threshold sequence
  N(S_k) bounded?
- The single, already-isolated hard obstruction (confirmed by 30+ mechanism
  attempts) is: the recursion's legality test is Boolean-blind to WHICH prime
  realizes gcd>1 and to any count/density/statistic of prior terms
  (Ambient-Statistic Obstruction, certified, generalizes to ANY
  statistic-based method); and any attempt to promote "infinitely often" to
  "cofinitely/always" hits the same "existential recruitment is
  non-exclusive" wall (Lemma I, Two-Sided Singleton Witness residual).

### Candidates checked this round (per the dispatch's suggested list)

**1. Ramsey-type argument.** Modeling the pair (n∈occ(A), m∈occ(B)) as an
edge 2-colored by [gcd(a_n,a_m)>1], Ramsey's infinite theorem would give an
infinite monochromatic subset — but this only re-derives "infinitely often"
(already free from the Bounded Witness Lemma), never "cofinitely." Ramsey
theorems are existence-of-infinite-substructure results, not tail/cofinite
results, so promoting to H1's actual cofinite target is exactly the same
existential→universal gap already fatal to 9+ prior mechanisms (Lemma I,
cofinite-window-capacity-bound, successor-transport-reduction-lemma, all
certified dead). Ramsey adds no new leverage here; it is a repackaging of the
already-dead promotion gap, not a bypass.

**2. Structural graph coloring.** The finite-core structure already gives a
finite alphabet of types (a genuine, already-exploited fact — Finite Core
Theorem). A "coloring" of indices by extended type is exactly the object the
subword-complexity-periodicity / Morse-Hedlund approach already builds
(`approaches/subword-complexity-periodicity.md`, Status `partial`, explicitly
flagged in run memory as an iff-reformulation, not a strictly easier bypass:
bounded factor complexity ⟺ eventual periodicity of g_n, same difficulty).
Chromatic-number / graph-coloring machinery proper (proper colorings, clique
covers, from the crux corpus's `graph-theory-and-connectivity` subtopic —
checked all 3 number_theory hits and the 61 combinatorics hits) is about
FINITE simple graphs with a fixed edge relation; it has no traction on an
infinite occurrence sequence whose "edges" (gcd>1) are defined by an
adaptively-growing history, and none of the 61 combinatorics hits (matchings,
clique covers, Euler circuits, Hall's theorem, tournament out-degrees) map
onto "two disjoint labeled infinite occurrence sets must eventually always
share a prime." No genuine analog found.

**3. Algorithmic/computational-complexity arguments.** Already tried and
dead: "priority-argument/computability" and "compactness/König's-lemma" are
both explicitly listed in the given dead-mechanism list (rounds 19-20 fresh-
framing sweeps). The sequence is trivially computable (deterministic greedy
recursion), so any argument of the shape "eventually the process must
stabilize because only finitely many computational states exist" needs an
actual finite state space — and the workspace has already proved (rule 3,
Master Conditional chain) that the TOTAL prime support of the sequence is
unbounded, so there is no finite state space to invoke. A "Kolmogorov
complexity" framing was also already tried and dead (round 20-21 sweep list).

**4. Analytic NT beyond Legendre (Bombieri–Vinogradov, better sieves).**
These are tools for bounding the ERROR TERM in prime-counting-in-APs
uniformly over a range of moduli — useful for tightening finite per-`p`
subfamily closures (a1-pq template), not for the FAH crux itself, which is
not a statement about prime density/counting at all but about a specific
adaptively-defined recursive legality test. Checked concretely: the existing
elementary Legendre Sieve Gap Bound + Primorial Floor Bound already suffice
for every per-`p` subfamily closure attempted so far (5,7,11,13,17q all
closed without needing a stronger sieve) — the residual gap in a1-pq (the
general-`p`, all-`q` closure) is a BOOKKEEPING/casework gap (per-p exceptional
table), not an insufficient-sieve-strength gap, so Bombieri–Vinogradov-level
machinery would not close it either; it is simply unneeded strength aimed at
the wrong obstruction.

**5. Reformulating the recursion as a known combinatorial process.** Checked
the crux corpus's `processes-and-algorithms` subtopic (48 combinatorics
hits) and searched the whole 2434-crux corpus for "greedy"+"gcd/coprime"
co-occurrence: zero hits — no crux problem in the corpus is a "greedy
integer sequence built by an all-prior-terms gcd condition." The nearest
corpus analog previously tried, `aimo-1000` (IMO 2021 P6 ferry-islands
growing-invariant/repair-on-failure template, flagged round 29 rule 33), was
in fact tried THIS round already in `bipartite-network-invariant-fah.md` and
independently re-confirmed RETHINK/dead: both readings collapse into
already-certified-insufficient content (Generalized Bounded Witness Lemma) or
into the open H2 termination question verbatim, not a new mechanism. I found
no other "growing invariant/repair on failure" analog in the corpus that
hasn't already been tried.

**6. Prove H1/H2 for a LARGER natural class instead of full generality (e.g.
bound the number of rogue pairs ever created).** Checked directly: "the
absorption chain S_0⊆S_1⊆... only ever adds finitely many primes total" is
DEFINITIONALLY the same object as H2/N(S_k)-boundedness (Termination
Criterion Lemma, certified round 15) — a rogue pair triggers exactly one
core-growth step, so "finitely many rogue pairs ever created" IS "the
absorption chain terminates," not a distinct or easier target. This has
already been attacked directly three times (core-growth-monotonicity round
16/19, direct-s0-self-absorption round 23) and proved, by a genuine
toolkit-independent argument (round 16's Proposition 3, "two consistent
finite-prefix extensions" — a basic fact about infinite 0/1 sequences: no
finite prefix ever decides eventual behavior), to be UNRESOLVABLE by any
finite-data/computational method. `a1=p·q·r` or other larger `a_1`-shape
families are a genuinely different (and still-live) axis — but that's the
existing subfamily-extension program (a1-pq, a1-3aq, etc.), not a new attack
on H1/H2 themselves; it proves more disjoint corollaries of the Master
Conditional Theorem's *conclusion*, without touching H1/H2 as open
hypotheses.

### Cheap-kill / structural pruning notes
- None obvious beyond what's already certified. The Ambient-Statistic
  Obstruction (rule 6) is itself the strongest available "cheap kill": before
  proposing ANY new H1 mechanism, check whether it only ever reads a
  count/density/statistic of prior occurrences (as opposed to literal
  divisor-chain/witness-identity content) — if so it is pre-emptively dead
  without needing a fresh disproof.

### Knowledge-base entries relevant (none new)
- Dirichlet's theorem (primes in APs), Bertrand's postulate, LTE, Zsigmondy —
  all previously checked (rule 23) and confirmed orthogonal/inapplicable to
  H1's actual obstruction (additive/greedy recursion, not
  multiplicative/exponential).
- No sieve-beyond-Legendre entry exists in `knowledge_base.md` (confirmed by
  reading the Number Theory section in full this round); nothing to newly
  cite for H1/H2.

### Analogous past problems (cruxes)
- `aimo-1000` (IMO 2021 P6, ferry islands) — the single closest structural
  analog for a "repair on failure, growing invariant" template; already
  imported and killed this exact round (see `bipartite-network-invariant-fah`
  above), so not re-proposable as fresh.
- No other crux in the 2434-entry corpus matches "infinite greedy integer
  sequence, legality = gcd>1 against the ENTIRE prior history" closely enough
  to count as a genuine analog (checked via subtopic filter +
  keyword search for greedy/gcd/coprime co-occurrence: zero results outside
  what's already been mined).

### Prior progress
See `results/imo-2026-06/current.md` — 10 certified solved subfamily
theorems (2|a_1; a_1=p^k; a_1=3q; a_1=3q^2; a_1=3q^3; a1-3aq a=1..5; a1-5q;
a1-7q; a1-11q; a1-13q; a1-17q) plus the gap-free Master Conditional Theorem
reducing full generality to H1+H2. Both H1 and H2 remain open; H2 is proved
(round 16 Prop 3, structural, not workspace-contingent) to be unresolvable by
any finite-data method, so genuine progress on H2 would need a true
invariant/monotonicity/compactness argument — none has been found in 24
rounds of dedicated search across many technique families.

### Dead ends (do not retry — full list per dispatch, reconfirmed)
triangle-consistency-pigeonhole variants; orbit-merging-additive-offset-
dichotomy; bipartite-network-invariant-fah (reconfirmed dead again this
round via independent structural check, not just cited); reversible-
transition-map; witness-index-descent; seed-coupling-induction; rogue-pair-
termination-potential; all ~32 fresh-whole-problem-framing sweeps listed in
the dispatch (Kolmogorov complexity, martingale/optional-stopping, renewal
theory, return-words/Rauzy graphs, coding theory, combinatorial game theory,
priority-argument/computability, o-minimality, nonstandard-analysis/model-
theory, spectral/operator, p-adic/algebraic NT, generating functions,
probabilistic/Borel-Cantelli, extremal graph theory, finite-Fourier/
character-sums, transfer-matrix, ergodic/symbolic-dynamics, compactness/
König's-lemma, additive-combinatorics); plus the 6 newly-checked candidates
above (Ramsey-type, structural graph coloring, computational-complexity,
Bombieri-Vinogradov/advanced sieves, combinatorial-process reformulation,
"bound rogue pairs as a larger class") — all now confirmed to collapse into
this same graveyard or into the H2 non-constructivity wall.

### Small-case / intuition notes
No new numeric experiments were run this round (the obstruction is now
structural/proved-unresolvable-by-finite-data for H2, and class-blindness-
proved for H1's statistical-method family, so further seed simulation would
not add evidence beyond what's already certified). Recommend the outliner
treat H1/H2 as genuinely exhausted at the current technique-repertoire level
and prioritize (a) further subfamily-extension APPROVEs (a1-19q, a1-23q, or
a genuinely new axis like a1=p*q*r) as the floor deliverable, and/or (b) if
H1/H2 is revisited, require a NON-statistical, NON-existential-promotion,
NON-finite-data mechanism as an explicit precondition before dispatch (the
only kind not yet exhaustively refuted) — e.g. an actual invariant that is
literally conserved by the recursion (not merely bounded), which no explorer
across 24 rounds has yet exhibited even a candidate for.
