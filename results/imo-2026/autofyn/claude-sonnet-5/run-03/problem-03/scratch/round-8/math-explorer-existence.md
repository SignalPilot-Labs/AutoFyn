## imo-2026-03 (Existence Theorem / balanced-region residual, upper-bound direction)

### Headline finding (numeric, independent, this round)
The reported "0/300 survivors at n=6,7,8" for best-of-{k=1, k=2 Anchor-Merge,
Subset-Tie} is almost certainly an **undersampling artifact, not a genuine
near-closure**. Re-running an honest, unbiased uniform sample of the
"large-gaps-everywhere" balanced region (uniform Dirichlet composition of
n+1 pieces, conditioned on p1<1/2 and every consecutive gap >
gamma(n)=1/(2^{n+1}-1)) and computing the true value of k=1-best,
k=2-best, and Subset-Tie-best (verified both via the closed-form formulas
*and* by direct construct-and-sort-and-sum simulation, matching to
floating precision) gives survivor rates of **33%–46%** at n=6,7,8,10,12
(not 0%!). This matches `current.md`'s own honest caveat that the
percentage table "is not precisely reproducible under an
independently-chosen sampling scheme (a methodology difference, not an
error)" — this round's finding sharpens that from "a methodology
difference" to "the residual, sampled honestly, is an order of magnitude
larger than the reported table suggested; 300 trials at a true ~35% rate
would essentially never show 0 survivors, so the earlier '0/300' results
likely came from a narrower/biased sampling procedure (e.g. sampling near
specific hand-picked or previously-known-hard points), not from
representative coverage of the region."

### A richer, untried tool closes most (not all) of this gap
Generalizing Subset-Tie so that the piece being subdivided-and-tied can be
**any** index (not only p1 — the file's Theorem 11 is stated only for
splitting p1), and taking best-of{k=1, generalized-subset-tie-over-all-idx}
(k=2 adds little beyond this and is expensive to include at scale, so
tested separately/optionally):
- n=4..8: survivor rate drops to 1.25%–4%.
- n=10: 8.25%. n=12: 12–17%. n=14: 23%. n=15: ~29%.
This is a genuinely new, untried construction (splitting a *non-top* piece
into ties, generalizing Theorem 11) worth handing the outliner as a
candidate additional tool — but the **key second finding** below shows it
does not rescue the additive-family strategy asymptotically.

### The residual is NOT shrinking with n — it appears to be growing
Across every tool combination tested (k1+subset-tie(p1-only), or
k1+generalized-subset-tie, with/without k2), the survivor **rate increases
with n**, from ~1–4% at n=4–8 up to ~10–30% at n=10–15 (see numbers above).
The excess magnitudes shrink with n (typically 1e-4 down to 1e-6) — c(n)
itself converges to 1/2 exponentially fast (gamma(n)=Theta(2^{-n})) — but
the *frequency* of instances these named tools fail on does not shrink to
match; if anything it worsens. This is a strong quantitative signal (not
proof) that **no finite named "tie-a-subset-and-bisect-the-rest" additive
construction family closes the residual as n grows**: the mechanism
appears to be that gamma(n) shrinks like 2^{-n}, and the best achievable
"leftover" r from any *fixed* combinatorial subset-tie rule is itself a
subset-sum-covering quantity whose typical achievable granularity is also
around 2^{-n} for n items — i.e., it's a genuine race between two
same-order-of-magnitude quantities, not one dominating the other, so a
constant (or growing) fraction of instances will generically lose the
race as n grows. This is exactly the mechanism CLAUDE.md's plateau-break
instruction anticipates: an additive/local construction hits a wall that
does not vanish with more effort, because the *type* of argument (explicit
finite tie-pattern) is intrinsically too coarse at the scale gamma(n)
requires.

### Distinct openings
1. **(Additive family, marginal juice left, but likely capped)** — the
   generalized-subset-tie-over-all-indices tool above is new and untried;
   worth formalizing as one more named lemma (cheap, mechanical corollary
   of the already-certified Singleton-Interleaving Lemma, same proof style
   as Theorem 11) since it materially shrinks the residual at small-to-
   moderate n. But per the growth trend above, do **not** expect it (or
   any single further named tool) to close the gap for all n — flag this
   to the outliner explicitly so effort isn't sunk into "one more
   construction" expecting full closure.
2. **(Global/LP-vertex reframing — the one CLAUDE.md flags as needed)**
   Instead of exhibiting one more explicit finite construction, prove
   directly that the TRUE optimum of XY's full inner minimization (over
   *all* cut patterns, not a named subfamily) is ≤ c(n) on the whole
   compact balanced-region polytope, via a vertex/LP argument analogous to
   `lp-duality-split-polytope`'s Single/Two-Piece-Split Vertex Lemma and
   its Theorem B (which is a genuinely different style: a global
   peeling/rank-counting argument over an AltSum reformulation, uniform in
   n, that does not decompose per-piece). Concretely: OddSum, as a
   function of a fixed cut-pattern's fragment values, is piecewise-linear
   in those values (this is already established via the greedy-optimality
   / rank-parity machinery certified in `lemmas/tie-neutrality-and-first-
   mover-half.md` and the AltSum reformulation
   OddSum=(1+AltSum)/2 used throughout `lp-duality-split-polytope`), hence
   its minimum over any *fixed* combinatorial cut-pattern (which piece
   splits into how many parts) is a **linear program** over the simplex of
   fragment values, attained at a **vertex** — i.e., where some fragment
   values coincide with each other or with an untouched piece (exactly the
   phenomenon the whole "anchor-merge/subset-tie" family is trying to
   guess at by hand). The Existence Theorem is then the claim: over the
   *finitely many* combinatorial cut-patterns available within budget n,
   at least one pattern's LP-vertex value is ≤ c(n), for every point of
   the balanced-region simplex. This reframes "does some finite
   construction always work" into "does the max-over-LB-partition,
   min-over-cut-pattern, of a finite collection of vertex-LPs, stay below
   c(n) everywhere" — a compactness/continuity argument (each vertex value
   is a continuous, indeed piecewise-linear, function of p; the whole
   region is compact) reduces this to checking finitely many *extremal*
   configurations (where several vertex-LPs' optimal values tie), rather
   than an unbounded search over instances — structurally the same
   "reduce an existence claim about an entire compact region to its
   extreme points" move that Theorem 3 (Perfect-Pairing) and Theorem B
   already used successfully, just one level up (over LB's whole
   partition-simplex, not just over one construction's fragment-simplex).
   This is a real proof sketch-level idea (do not develop further — this
   is exploration, not outline).
3. **(Diagnose why "large-gaps-everywhere" is the hard case at all)** —
   worth asking whether the residual's *existence* (not just its
   closability by named tools) can be turned into a genuine
   counterexample to c(n) itself, i.e. whether the TRUE inner minimum
   (not restricted to any named family) ever exceeds c(n) on a
   large-gaps instance. This round's evidence (generalized-subset-tie
   closing all-but-~1-4% at small n) suggests the true optimum is *always*
   achievable ≤ c(n) — i.e. c(n) itself remains plausible — but this was
   not verified by a genuinely unrestricted numeric optimizer (e.g.
   simulated annealing over arbitrary cut-patterns) this round; doing so
   on the specific n=6/n=8 hard survivors found here would be a cheap,
   valuable sanity check before investing in a global LP argument (if the
   TRUE optimum on a survivor instance already exceeds c(n), the whole
   conjectured closed form c(n) would need re-examination — but there is
   no evidence yet for this; it's a caution, not a finding).

### Candidate technique(s)
- LP-vertex / rank-parity (AltSum) global argument, extending
  `lp-duality-split-polytope`'s Theorem A/B machinery (peel-the-max +
  AltSum bound) from "prove necessity for one construction family" to
  "prove sufficiency over all cut-patterns" — this is the technique
  CLAUDE.md's dispatch explicitly points toward.
- Compactness/continuity reduction of an existence claim over a simplex to
  its vertices/boundary — same style as Theorem 3's slack-budget closure
  and Theorem B's uniform-in-n peeling argument.

### Cheap-kill candidates
- None obvious for actually closing the gap. But a cheap sanity check
  (not yet done): run an unrestricted numeric optimizer (basin-hopping /
  simulated annealing over cut-pattern + fragment values) on the specific
  n=6, n=8 survivor instances found here and by round 7, to confirm the
  TRUE optimum (not just the named-tool best) is ≤ c(n) — this is a
  30-minute script, cheap, and would either reassure the population that
  c(n) itself is safe (expected) or (if it fails) flag a much bigger
  problem than the Existence Theorem.

### Knowledge-base entries to use
Checked `knowledge_base.md` directly for LP/duality/vertex entries: no
generic "LP duality" or "minimax" theorem entry exists there (grep found
only unrelated "vertex" hits in geometry/coloring sections). The relevant
machinery is entirely project-internal (certified lemmas), not from
`knowledge_base.md`:
- `lemmas/singleton-interleaving-and-k-anchor-merge.md` (Theorems 9, 10) —
  reused as-is for the generalized-subset-tie construction (opening 1
  above is literally a corollary of Theorem 9, same proof template as
  Theorem 11).
- `lemmas/tie-neutrality-and-first-mover-half.md`, `lemmas/vertex-pinning-
  lemma.md`, `lemmas/single-piece-split-vertex-lemma.md`,
  `lemmas/non-top-piece-theorem-b.md` — the vertex/AltSum/peeling
  machinery to build on for opening 2 (the global LP-vertex argument).

### Analogous past problems (cruxes)
Searched `games-and-strategy`, `extremal-principle`, `linear-algebra-
method`, and `inequalities-SOS-and-convexity` subtopics (both
`combinatorics` and other domains) for LP-duality/minimax/vertex-style
upper-bound arguments in combinatorial games. Found **none genuinely
analogous**: the `games-and-strategy` hits (e.g. `aimo-0461`, `aimo-0115`)
are graph/board partition-and-respond strategies, not continuous-simplex
LP-vertex arguments. The `extremal-principle` hits are almost all
"take an extremal vertex/object, do a local move" graph arguments, not
LP duality over a continuous polytope. No crux in the corpus resembles
the "reduce a two-player continuous-partition game's value to a
finite-vertex LP characterization" mechanism this problem needs — report
this honestly as "no good match" rather than forcing one.

### Prior progress
Best-of-{k1, k2 Anchor-Merge, Subset-Tie(p1 only)} — proved constructions,
narrows but does not close the balanced-region residual (current.md,
Theorem 11). Multi-Piece Necessity (a related but distinct gap, on the
*other* half of the project — proving a construction is *needed*, not
sufficient) is separately at Theorem B, closing n of n+1 index cases.

### Dead ends (do not retry)
- Continuity/boundary-layer graft of Theorem 2 onto p1→1/2^- (checked and
  refuted in round 7; confirmed here it's the wrong mechanism, not
  re-tested).
- k=3 anchor-merge as a monotone improvement over k=2 (proven false,
  round 6/7).
- Trusting small (n≤300) uniform random samples as evidence of "near-zero
  residual" — this round shows such samples badly undercount a true
  ~35%-rate residual; any future round reporting "0/300" on this specific
  gap should be treated with suspicion unless sample size and generation
  method are stated and cross-checked (methodological note for next
  round's math-explorer / builder).

### Small-case / intuition notes (conjectural)
- Survivor rate (best-of additive tools fails) grows with n: roughly
  1–4% (n=4–8) → 8–30% (n=10–15), while typical excess shrinks
  (1e-4→1e-6). Conjecture: this reflects a genuine race between
  gamma(n)~2^{-n} and the granularity of subset-sum-based tie
  constructions, which is also ~2^{-n} generically — i.e. the additive
  family is asymptotically borderline, not asymptotically dominant. This
  is evidence, not proof, but is a fairly strong and easily-reproducible
  signal (scripts: `/tmp/explore_existence.py`, `/tmp/verify_direct.py`,
  `/tmp/explore2.py`, `/tmp/explore3.py`, `/tmp/explore4.py`, all in
  `/tmp/`, reproducible with `random.seed`).
- No evidence found that c(n) itself is wrong — the generalized-subset-tie
  tool alone already closes the vast majority of instances at every n
  tested; the open question is entirely about whether a finite named
  toolkit (vs. a global optimality argument) can certify the rest.
