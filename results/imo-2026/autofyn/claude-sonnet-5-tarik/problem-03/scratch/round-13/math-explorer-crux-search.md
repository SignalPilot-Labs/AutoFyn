## imo-2026-03 (lens: crux-corpus search for a technique to prove Gap 1's Non-Matching-Witness
existence claim — `potential-weighting-upper-bound.md` §18.4/§18.6)

**Scope note.** Per dispatch this is a corpus-search + adaptation-sketch report only — no proof
attempt, no lemma skeleton. Read `current.md` in full and `potential-weighting-upper-bound.md`
§17–§18 (lines 3198–3785) before starting; also read the sibling explorer's report
(`/tmp/round-13/math-explorer-argmin-construction.md`, already on disk when I started — its
"Sign-Determined DEL/KEEP-Suffices," "No-Gap," and "Sum Bound" findings are referenced below where
relevant, but not re-derived or re-tested here; this report focuses on retrieval, not on repeating
that computation).

**The exact gap, restated precisely (for reference).** For `(C,W,\sigma)\in\mathcal F` with
`C_{\mathrm{lo}}\ne\emptyset` (background not yet dominated by `\max(W)`), show
`\mathrm{OPT}_\sigma(C,W)` has an optimal witness not matching `w_1:=\max(W)`. Already dead for this
gap (per dispatch, not re-suggested here): Forced Swap Inequality (bounds sibling match-partners,
not a node's own DEL/KEEP vs MATCH), Hall's theorem/bipartite matching (existence-of-structure vs.
existence-of-*value*-achieving-witness mismatch), averaging (too weak, only existential not
index-exact).

### Distinct openings surfaced this round
1. **Extremal-witness + secondary tie-break + local rewrite** — the crux corpus's closest genuine
   analog to "prove some optimal solution avoids property X" (see Candidate 1 below). This is a
   real technique family, not superficial pattern-matching: several corpus solutions solve exactly
   "show SOME extremal/optimal object has property X" by picking the optimal object *plus* a
   secondary extremal criterion, then deriving a contradiction from a local, value-preserving (or
   value-improving) rewrite whenever property X fails.
2. **Restriction-of-a-global-extremal-object-is-itself-extremal** (aimo-0666's leximinimal-coloring
   restriction lemma) — a genuinely different idea from anything on file: instead of proving Claim A
   node-by-node in the DELETE/KEEP recursion, try to show a node's local optimum is *forced* by the
   ORIGINAL top-level `k^*`'s global argmin property directly, over the actual binary DELETE/KEEP
   tree (see Candidate 2 below — an earlier draft of this idea wrongly guessed the tree collapses to
   a single chain; corrected below, with the check that refuted it).
3. A clean negative report: no crux in the corpus targets this *specific* shape (a background-
   carrying alternating-sum optimization closed under DELETE/KEEP, with a "does the top element get
   matched" existence question) closely enough to lift wholesale — see "Honest assessment" at the
   end.

### Candidate technique(s) — with concrete adaptation sketches

**Candidate 1 — Extremal witness + secondary tie-break + local exchange (strongest match found).**
Corpus instances: `aimo-0960` (ISL-style Fibonacci-base representation: take a minimum-length
representation, tie-broken lexicographically-least in its sorted exponent multiset; a repeated
exponent is locally rewritten via `2\psi^e=\psi^{e-2}+\psi^{e+1}`, same length but strictly smaller
in lex order, contradicting minimality — so property "no repeats" is forced onto *some* extremal
representative), `aimo-0438` (minimal path-partition of a lattice diamond; among all edge-maximal
partitions, pick one maximizing a secondary "alignment" statistic `N`; any local deviation from the
target canonical path admits a delete-one/add-one edge swap that preserves edge-count but strictly
raises `N`, contradicting maximality — forcing the target sub-structure onto the extremal
partition), `aimo-0666` (leximinimal coloring: if a vertex had no neighbor in the class it "should"
move to, moving it there would be lex-smaller, contradiction), `aimo-0119`/`aimo-0553` (pick the
config maximizing/minimizing a target quantity, read off a numeric inequality from non-improvement
under a specific single-item transfer).

*Adaptation sketch.* At a node `(C,W,\sigma)\in\mathcal F` with `C_{\mathrm{lo}}\ne\emptyset`, suppose
for contradiction (as Gap 1 needs to rule out) that **every** optimal witness of
`V:=\mathrm{OPT}_\sigma(C,W)` matches `w_1` to some `w_m` — i.e. `\mathrm{DEL}<V` and
`\mathrm{KEEP}<V` strictly, MATCH strictly the unique winner (this is the literal negation of what
Gap 1 needs to rule out, phrased via the already-certified Non-Matching-Witness Criterion). Among all
such matching-only optimal witnesses, pick one with a **secondary extremal criterion** — analogous to
`aimo-0960`'s lex-tiebreak or `aimo-0438`'s alignment statistic. Two natural candidates for this
problem's specific objects: (a) minimize the gap `|w_1-w_m|` (i.e. prefer `w_1` matched to the
*closest* remaining value); or (b) since `C=\{b_0,d_{k^*}\}` (or a subset thereof after
Background-Splitting) throughout the non-dominated tail (per the sibling explorer's "No-Gap"/"`C`
invariant" finding), maximize the number of the *background's own* elements `b_0,d_{k^*}` that remain
untouched by any matched pair anywhere in the witness. Then attempt a **local rewrite**: replace the
pair `(w_1,w_m)` with `w_1` moved to DELETE (or KEEP) and `w_m` reassigned into the recursive
sub-search on the remainder — the exact rewrite formula would have to use the
Rank-Extraction/Background-Splitting machinery (already certified) to track the value change exactly,
the same way `aimo-0960`'s rewrite uses the explicit identity `2\psi^e=\psi^{e-2}+\psi^{e+1}` to make
the value-preservation exact rather than approximate. **This has NOT been attempted** (out of scope
for scouting) — it is a genuine candidate proof *shape*, not a proof; the open sub-task it leaves is
finding the exact rewrite identity (the corpus examples all have a clean closed-form local move
available; this problem's analog would need to be derived from the certified General
Rank-Extraction Identity, not assumed).

*Cheap test performed.* I checked whether the **existence** of such a secondary-extremal
matching-only witness is even a coherent object to reason about in the first place — i.e. whether,
among F-family nodes, "all optimal witnesses match `w_1`" ever actually occurs (this is precisely the
"forced-matching" case the builder's own §18.4 already checked and found `0/417`). I did not re-run
this (it's already on file and re-confirmed by the sibling explorer's independent tests of the
DEL/KEEP-suffices conjecture) — flagging that Candidate 1's contradiction hypothesis ("every optimal
witness matches `w_1`") may be provably **vacuous** on `\mathcal F` specifically (consistent with
everything on file), which would make the "secondary tie-break forces a contradiction" step much
easier than the corpus examples' (which have to work harder because their bad case genuinely can
occur transiently). This is a reason for cautious optimism about Candidate 1's adaptability, not a
proof that it works.

**Candidate 2 — Restriction-of-a-global-extremal-object-is-itself-extremal (aimo-0666's induced-
subgraph lemma), CORRECTED after a cheap check refuted the first draft of this idea.**
`aimo-0666`'s cleanest single move: *given* a global leximinimal coloring, its restriction to an
induced subgraph on any subset of color classes is **itself** leximinimal on that subgraph — proved
by contradiction (a lex-smaller restricted coloring, recombined with the untouched classes, would
beat the global leximinimal coloring). This is a "local extremality is inherited from global
extremality" lemma, structurally the OPPOSITE direction from Candidate 1 (which builds a local
witness's extremality from scratch at each node) — a genuinely different idea from everything tried
so far on Gap 1 (FSI, averaging, Hall's, or induction-node-by-node): **can a node
`(C,W,\sigma)`'s own local optimum be shown to inherit non-matching-ness directly from the ORIGINAL
top-level `k^*`'s global-argmin property over the whole `Z_0`, rather than reasoning about `(C,W)` as
a fresh, decontextualized instance?**

*A speculative over-simplification I tested and must flag as WRONG, so the outliner doesn't repeat
it:* my first-draft reasoning was that since DELETE always removes exactly the current max and KEEP
always keeps exactly the current max (neither closure rule has any internal choice), the entire
family `\mathcal F` generated from one base trigger might collapse to a **single deterministic chain**
of nodes indexed by depth rather than a branching tree — which would have made Candidate 2 much
easier (a single closed-form function of depth, rather than a genuine tree induction). **A 30-second
by-hand trace refutes this:** both closure rules (2, DELETE and 3, KEEP) apply *simultaneously* to
every node with `W\ne\emptyset`, so `\mathcal F` is a genuine **binary tree**, not a chain — the
DELETE-child keeps `C` unchanged and drops `w_1` from `W`; the KEEP-child in general has a
*different* `C` (`C_{\mathrm{lo}}\subsetneq C` whenever `h:=|\{c\in C:c>w_1\}|>0`) and a flipped
`\sigma`; both children are simultaneously present in `\mathcal F` at the next depth. So there is no
shortcut collapsing the induction's shape — Candidate 2's underlying idea (explain a node's local
optimality via `k^*`'s *original* global minimality, not via sibling-depth comparisons) is still
worth attempting, but only as a genuine induction over the actual binary DELETE/KEEP tree, exactly as
the current outline already frames it (§17.5) — **this candidate does NOT reduce the size of the
problem the way I first (wrongly) hoped; it only offers a different proof *mechanism* (global-argmin
inheritance) for the same tree-shaped induction**, not a shortcut around needing it.

### Cheap-kill candidates
- **Ran this round:** the "does `\mathcal F` collapse to a single chain" check above — refuted
  in 30 seconds by hand-tracing the two closure rules; saves the next round from chasing this
  simplification.
- Test whether "all optimal witnesses match `w_1`" (Candidate 1's contradiction hypothesis) is
  already known/provably vacuous on `\mathcal F` (strongly suggested, not independently re-verified
  this round, by the builder's `0/417` and the sibling explorer's independent corroboration) — if
  vacuous, Candidate 1 reduces to a much easier "does a matching-only optimum even arise" question
  rather than a genuine secondary-extremal argument.

### Knowledge-base entries to use
- `lemmas/general-rank-extraction-identity.md`, `lemmas/empty-background-and-background-splitting.md`
  (Non-Matching-Witness Criterion, Background-Splitting) — the exact certified machinery any local
  rewrite (Candidate 1) or global-inheritance argument (Candidate 2) would need to compute value
  changes exactly.
- `lemmas/forced-swap-inequality.md` — already decisively ruled out for this gap (§18.4); not
  re-suggested.
- `knowledge_base.md`'s generic "exchange argument" / "extremal principle with secondary tie-break"
  entries, if present, are the closest generic KB match to Candidate 1 (did not cross-check
  `knowledge_base.md`'s exact entry names this round — dispatch's KB-listing task is not the focus
  here; the crux corpus itself supplies the concrete worked examples above).

### Analogous past problems (cruxes)
- **`aimo-0960`** (ISL-style: representations `\psi x+y=\sum\psi^{j_r}`) — crux
  `symmetric-functions-and-substitution`: "Among minimum-length representations pick the
  lexicographically minimal exponent multiset, then kill any repeated exponent by a local
  length-preserving rewrite that lowers the multiset in the ordering, contradicting minimality." Best
  analog found: the *shape* (extremal object + secondary tie-break + local rewrite killing an
  unwanted repeated/matched feature) is a close structural match to what Gap 1 needs; the *specific*
  algebraic identity (`2\psi^e=\psi^{e-2}+\psi^{e+1}`) does not transfer — this problem would need its
  own analog identity derived from Rank-Extraction, not borrowed.
- **`aimo-0438`** (lattice-diamond minimal path-partition) — crux `extremal-principle`: "among all
  optimal configurations select one maximizing a secondary alignment statistic, then show any local
  deviation from the target admits an edge-count-preserving exchange that strictly increases the
  statistic, contradicting maximality." Same structural family as `aimo-0960`, applied to a
  combinatorial (not algebraic) extremal object — reinforces that this is a genuine reusable *shape*,
  not a one-off algebraic trick, but again the specific "secondary alignment statistic" and its local
  exchange move are bespoke to that problem's lattice geometry and do not transfer literally.
- **`aimo-0666`** (rainbow/leximinimal graph coloring) — crux `extremal-principle` +
  `graph-theory-and-connectivity`: leximinimal tie-break forcing a local neighbor constraint, PLUS the
  "restriction of a global extremal object to a sub-instance is itself extremal" lemma (Candidate 2
  above). Best analog for the *reframing* idea (local optimality inherited from global optimality),
  though the specific restriction argument (to an induced subgraph) has no literal analog in this
  problem's DELETE/KEEP-tree structure.

None of these is a subject-matter match (as expected — the dispatch's own framing, "background-
carrying alternating-sum recursion closed under DELETE/KEEP with a global-argmin-seeded base case,"
is bespoke to this problem and unlikely to appear verbatim in a pre-2026 olympiad corpus). All three
are cited for their **proof shape**, to be adapted and re-derived from scratch, not cited as
authority — consistent with CLAUDE.md's crux-corpus usage rule.

### Prior progress
Per `current.md`/`potential-weighting-upper-bound.md` §18: Gap 2 closed in full; Empty-Background and
Background-Splitting Lemmas certified, unconditionally closing Claim A on the dominated tail of every
path; `B_0` proved always size exactly 1 (never 0) at the base generator; Non-Matching-Witness
Criterion certified (Claim A `\iff` some optimal witness of `(C,W,\sigma)` doesn't match `w_1`); FSI
proved (by explicit trace and `417/417` computational check) NOT to directly close Gap 1. Gap 1's
residual content, precisely: for `(C,W,\sigma)\in\mathcal F` with `C_{\mathrm{lo}}\ne\emptyset`, show
`\mathrm{OPT}_\sigma(C,W)` has an optimal witness not matching `\max(W)`.

### Dead ends (do not retry)
- Forced Swap Inequality adaptation to Claim A (§18.4) — bounds sibling match-partner values, not a
  node's own MATCH vs. its own DEL/KEEP; decisively ruled out with an explicit mechanism trace plus a
  `417`-instance computational check finding the rare numerical agreements are coincidental.
- Hall's theorem / bipartite matching framing — per dispatch, structural mismatch (existence-of-
  matching-structure vs. existence-of-value-achieving-witness).
- Averaging (both the round-12 swap-average and all-partners-average variants) — per dispatch, too
  weak, proves only existential RDRC, never the index-exact SAR/Claim-A form.
- **New this round:** the naive "`\mathcal F` collapses to a single DELETE/KEEP chain" simplification
  — refuted by hand-tracing the two closure rules (both apply simultaneously at every node, giving a
  genuine binary tree). Do not assume this shortcut in a future proof attempt.
- (Not re-tested this round, but consistent with the sibling explorer's finding) treating the
  Sign-Determined DEL/KEEP-Suffices conjecture or the Sum Bound as free-standing universal facts
  (non-`\mathcal F`-provenance) — both explicitly refuted at 4%–45% failure rates on arbitrary
  same-shape instances.

### Small-case / intuition notes (all labeled conjecture)
- The corpus search strongly suggests the *shape* of proof most likely to close Gap 1 is an
  extremal-witness argument with a secondary tie-break criterion and a bespoke local rewrite (not a
  generic inequality like FSI) — this is consistent with, and reinforces, the builder's own §18.6
  "concrete next step" (construct the non-matching witness explicitly, using `d_{k^*}`'s global-argmin
  defining property, not yet used in §18's reductions).
- **Honest assessment / overall negative finding:** the crux corpus has NO problem whose *subject
  matter* resembles this bespoke background-carrying alternating-sum DELETE/KEEP/MATCH recursion —
  confirming the sibling explorer's own conclusion. What the corpus *does* supply is a well-attested,
  reusable *proof shape* (extremal witness + secondary tie-break + local exchange, Candidate 1) that
  is structurally the right kind of tool for an existence claim like Gap 1's, and one further
  reframing idea (Candidate 2, local optimality inherited from global optimality) that is
  structurally different from every mechanism tried so far (FSI, averaging, Hall's) — but neither is
  a ready-made proof, and constructing the actual rewrite/inheritance argument (using `d_{k^*}`'s
  global-argmin defining property, which — as the builder's own §18.6 notes — has not yet been used
  anywhere in the existing reductions) remains the genuine open task for the next build round.
