## imo-2026-06 — H1/FAH fresh-corridor hunt (lens: genuinely new framing for H1, not a technique variant)

### Verdict up front
**No concrete new corridor found.** After (a) re-reading the full dead-mechanism trail in
`current.md` (30+ named mechanisms across rounds 3-25), (b) reading the certified
`ambient-statistic-obstruction.md` lemma and its exact stated scope limits, (c) reading
`triangle-consistency-pigeonhole.md` §5.3's independent obstruction diagnosis, and (d)
querying the crux corpus by subtopic (per `crux_moves_documentation.md`'s exact field
names), I found one theoretical loophole worth recording precisely (below), but on
inspection it is very likely blocked by an *already-documented* (though not yet formally
certified as a negative theorem for this exact case) obstruction, not a live opening. I
recommend NOT dispatching a build slot on it without a sharper idea than what I found. 19
consecutive plateau rounds (6-25) plus this round's negative search is real signal the
"prove H1 as literally stated, head-on" well is close to exhausted for now — the
productive frontier remains the subfamily-theorem track (a1-pq, a1-3aq, a1-3qk), not H1
itself.

### The one loophole I found, and why it's probably not real progress
The certified **Ambient-Statistic Obstruction** (`lemmas/ambient-statistic-obstruction.md`)
kills only arguments built from statistics `Φ(X)` that are computable *without ever
running the greedy recursion past n_B* — i.e. purely ambient number theory (Mertens
products, sieve counts over ALL integers in a range). Its **mandatory scope note**
explicitly says it does NOT cover, and does NOT rule out: density ratios *conditioned on
realized `A'`-occurrences*, second moment *over pairs of realized occurrences*,
Borel–Cantelli *over the realized indicator* `1[ρ(n)=A']`, or finite-Fourier/character-sum/
LP-relaxation built from the *realized occupation-count vector*. I checked `current.md`
end-to-end (grep for "occupancy-referencing", "realized occupation", "second moment",
"Borel-Cantelli") and confirmed: this exemption was *named* in round 19-20 as an honest
scope gap, but **no round since has actually attempted to build a proof using an
occupancy-referencing statistic** — it has only ever been cited as "formally
un-ruled-out," never tried as a positive construction. That makes it, on paper, the most
literally-untried corridor in the whole H1 trail.

**Why I do not recommend building it anyway.** `triangle-consistency-pigeonhole.md` §5.3
(round 19, kept as a documented — not certified as a formal negative lemma, but carefully
argued — diagnosis) already explains why *any* sieve/density-family technique (ambient or
occupancy-conditioned) needs *independent local-density or CRT-independence control* over
the index set `X_A = {n : ρ(n)=A'}` and over which outside prime divides `a_n` at each
`n ∈ X_A`, and that no such control exists: `X_A` has no closed form (defined only via the
entire greedy legality history), and whether an outside prime `p` divides `a_n` is an
*adaptive, path-dependent* fact (depends on which prime happened to already supply
`gcd>1` earlier), not a residue-class rule in `n`. This diagnosis does not literally
mention "occupancy-conditioned second moment/Borel–Cantelli" by name, but its argument is
generic to the *entire* statistical-method family, ambient or not — conditioning on
realized occupancy indices does not supply the missing independent local-density
structure; it just relabels the index set you'd need that structure for. So the
loophole in the certified lemma's *scope* is real, but the *practical* obstruction
(no local-density handle on a path-dependent recursive index set) applies regardless,
and was already found independently. I judge this NOT a genuinely promising build
target — flagging it explicitly so no future round re-discovers the scope-exemption and
treats it as fresh without checking this.

### Weakening H1 — checked, target is already minimal
Per the dispatch's suggestion to look for a weaker-but-sufficient H1: I traced exactly
what the CRT + cyclic-pigeonhole finish (`covering-system-construction.md` Step 5) needs.
It requires, for `n` beyond a finite threshold, that `ρ(n)` literally *equals* an
extended-persistent type in `𝒫'` and that every two elements of `𝒫'` share an `S_0`-prime
— i.e. it needs the "existential witness → cofinite (finitely many exceptions)"
promotion *exactly as H1 already states it* (`E := {n>n_B : ρ(n)=A', q*∤a_n}` finite).
A density-1 or "bounded gaps between failures" (syndetic) version would NOT suffice for
the literal residue-driven cyclic argument used in Step 5 (infinitely many exceptions,
even sparse ones, break the "read legality off a_n mod L alone" reduction). So H1 as
currently stated (finite, not zero, exceptions) is already the minimal sufficient
weakening for this finish — there is no slack to extract here without redesigning Step 5
itself, which is a different, larger undertaking than "weaken H1."

### Crux corpus search (per crux_moves_documentation.md, exact field names)
Queried `past_crux_moves_database.json` directly (not guessed field names):
- `domain=number_theory, subtopic=graph-theory-and-connectivity` (3 entries: aimo-0365,
  aimo-0365, aimo-0928) — both about counting connected components / bounding edges via
  out-degree in a *fixed, explicitly-defined* congruence graph. Not analogous: our
  obstruction is precisely the absence of a closed-form/explicit definition for the
  relevant index set, which these cruxes assume from the start.
- `domain=number_theory, subtopic=sequences-and-recurrences` (6 entries) — closest is
  aimo-0079 (Omega-parity forced periodic via a fixed-shift reindexing of an *explicit*
  polynomial `P(x)=(x+a)(x+b)`), but again relies on an explicit closed form; not
  analogous to a path-dependent greedy recursion.
- Keyword search for "greedy" across the full corpus (2434 cruxes): found aimo-1025
  ("run a canonical greedy version of a graph-closure process... until it gets stuck") —
  already checked and confirmed dead for this workspace's H2 mechanism in round 24
  (presupposes a finite ambient state space a priori, which H1/H2 do not have
  independently). No other greedy-sequence crux resembles an "existential-to-cofinite
  divisibility promotion in a recursively/adaptively defined sequence."
- `combinatorics, probabilistic-method` (4 entries) and `algebra, probabilistic-method`
  (1 entry) — skimmed; all are finite/discrete extremal arguments (majority/minority
  bounds, greedy-vs-average comparisons) with no analog to promoting an "occurs
  infinitely often" gcd fact to "occurs cofinitely."
- **Conclusion: no genuinely analogous crux found.** This corroborates (does not just
  repeat) the prior rounds' finding that aimo-0477/aimo-0016/aimo-0051 (already
  transplanted and dead in this workspace, per memory rule) are the closest matches in
  the entire corpus, and nothing new surfaced under this round's different subtopic
  queries (graph-theory-and-connectivity, sequences-and-recurrences, greedy-keyword,
  probabilistic-method).

### Candidate technique(s)
None newly surfaced for H1 itself. Existing candidates remain what's already
certified/attempted (persistent-type pigeonhole family, recruitment-process/Finite Core
Theorem machinery) — no new technique name to add.

### Cheap-kill candidates
None obvious for H1 itself this round (already an extremely well-screened crux). For the
broader run, the cheapest continuing wins remain outside H1: `a1-pq-subfamily-theorem`'s
per-`p` `Bad(p)` computation (machinery already certified and `p`-uniform, just needs the
finite table computed for `p≥5`, same toolkit as the already-3x-successful `a1-3q^m`
closures) and H2's flagged-but-untried "attack N(S_0)=0 directly on the explicit S_0"
mechanism (memory rule, round 23) — neither is a new H1 corridor, but both are concrete,
low-risk, high-probability-of-another-certified-result build targets if the outliner
wants a non-H1 slot this round.

### Knowledge-base entries to use
No new `knowledge_base.md` entries surfaced as applicable to H1 this round (consistent
with rounds 19-25's exhaustive KB sweeps). For the subfamily track: the certified
Legendre Sieve Gap Bound + Primorial Floor Bound (this workspace's own lemmas, not KB)
remain the load-bearing tools, already in use.

### Analogous past problems (cruxes)
None genuinely analogous found this round (see corpus search above). The best
historical matches remain the already-transplanted-and-dead aimo-0477 (divisor-chain
bounded by a fixed integer), aimo-0016 (IMO SL C5), aimo-0051 (USA TST 6) — do not
re-propose any of these as fresh.

### Prior progress
Unchanged by this exploration: Master Conditional Theorem (gap-free) reduces the general
case to H1+H2; 4 certified subfamily theorems (`2|a_1`; `a_1=p^k`; `a_1=3q`;
`a_1=3^a q`, a=1..5); certified standalone `a_1=3q^2`, `a_1=3q^3`; certified `p`-uniform
`a_1=pq` machinery (Bad(p) open for p≥5). H1 itself: 19 consecutive plateau rounds,
unchanged this round.

### Dead ends (do not retry)
All ~30+ previously catalogued mechanisms (ambient statistics of every kind, sieve/
density on the path-dependent index set, singleton-witness variants, competitor/CRT-glue
constructions, orbit-merging/additive-offset dichotomy, priority-argument/computability,
o-minimality, nonstandard analysis, spectral/operator, Kolmogorov complexity, martingale/
optional-stopping, renewal theory, Rauzy graphs, coding theory, game theory, Zsigmondy,
Dirichlet-in-APs, amortized charging/exchange-cost). This round additionally confirms:
occupancy-conditioned statistical methods (density-ratio/second-moment/Borel-Cantelli/
Fourier on the realized occupation vector), while not formally covered by the certified
Ambient-Statistic Obstruction, are practically blocked by the same independently-
diagnosed local-density obstruction (§5.3 of `triangle-consistency-pigeonhole.md`) — do
not build this as if it were a fresh loophole without a genuinely new idea for supplying
the missing local-density control.

### Small-case / intuition notes
No new numeric experiments run this round (this lens was a structural/documentation/
corpus search, not a numeric probe) — prior rounds' extensive simulation record (12/12
seeds with no FAH counterexample, exact periods computed for several hard seeds) stands
unchanged and is not contradicted by anything found here.
