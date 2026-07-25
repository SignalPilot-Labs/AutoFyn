## imo-2026-03

### (1) Plateau check — are GT(m) sub-case (i) and Sigma-shape the SAME obstruction?

**Re-verified: still NOT the same obstruction after round 16.** Round 13's
plateau-check finding stands and is, if anything, reinforced by round 16's
events:

- GT(m) sub-case (i)'s residual (`self-similar-induction-on-n`, width-1
  window `a_1 in (2^(k-1), 2^(k-1)+1)`, every excess `e>=0`) is a purely
  **arithmetic/identity** obstruction: a specific multiset recursion
  `OddSum(D ∪ Γ_{j-1})` under repeated peeling, where the failure mode
  round 16 hit was a mis-chained algebraic identity (silently converting a
  certified Odd→Even peeling step into an Odd→Odd step across `e` peels).
  This is a **finite, exactly-specified** algebra bug, not a combinatorial
  blow-up — current.md's round-16 entry already reports the reviewer
  independently re-derived the *correct* two-step relation
  `O_j = 2^{j-1} + O_{j-2}` (when q=0 holds at both levels j, j-1; 3000
  trials, zero violations), so the fix is a clean, already-diagnosed
  re-assembly using the two already-certified sub-lemmas (Half-Sum
  Corollary, Large-Sum Closure Theorem) — no new machinery needed.
- `global-lp-vertex-sufficiency`'s Sigma-shape gap is a **combinatorial
  existence/classification** obstruction: characterizing which of a
  super-exponential (Stirling-number-many, round 11's `|Σ(n,k)|` count)
  family of response-shapes attains the polytope's vertex maximum, now
  narrowed (round 16) to a *joint* branch-comparison-boundary +
  within-branch-tie family, with **no** proposed closed-form recursion at
  all — this is existence-over-an-unbounded-shape-space, structurally
  unlike GT(m)'s single fixed recursive identity.

These remain genuinely different mechanisms (one: fix an identity-chaining
bug in a fully specified recursion; the other: find/characterize an
extremal-vertex family in a huge combinatorial space) — **no plateau-break
is forced by this criterion**. Do not merge them into one target.

### (2) Fresh top-level framing — crux search

Per rule (round 6/round 2): games-and-strategy cruxes in this corpus are
uniformly discrete board/pairing games, structurally unlike the
continuous "split budget then alternately claim sorted items" game here —
re-confirmed, no new match found there.

**Found a genuinely different, better match outside games-and-strategy:**
`aimo-0119` (Dutch TST, `combinatorics`/`extremal-principle`) — "distribute
cards (a finite multiset of reals) into 100 boxes to minimize the maximum
box sum; find the worst-case bound." Its solution's crux move (the 5th
`solutions` entry, not the mismatched first one — same "check the
`solutions` field matches the `problem` field" caution as round 4's
aimo-0127) is:

> Among all distributions minimizing the max box-load, pick the one using
> the *fewest* boxes at that max load. Let `d_1<=...<=d_100` be the sorted
> box sums. From the sum bound, `99*d_1 + d_100 <= 1000`. Then argue: moving
> one positive card from a max-loaded box to the min-loaded box `d_1` can't
> yield a strictly better distribution (by extremal-choice minimality), so
> the post-move `d_1` must be `>= d_100`. This pins down the extremal
> shape exactly.

This is a genuinely analogous **extremal-choice + single-item-transfer
non-improvement** exchange argument for a *min-max distribute-into-groups*
problem — structurally close to what `global-lp-vertex-sufficiency`'s
Sigma-shape gap needs (characterizing the optimal adversary response
shape σ*(p) that maximizes/minimizes OddSum). It differs from every
already-tried construction family here (cyclic tie, star/tree, descending
chain — all *specific hand-built topologies*, all refuted) by being an
**extremal-selection** argument instead: define the target response as
"the legal response minimizing OddSum, tie-broken by fewest tied
fragments," then derive structural consequences from single-fragment-
transfer non-improvement, rather than trying to guess+verify one
construction family at a time. This has NOT been tried in this form in
any of the 4 already-refuted tie-topology families (round 13-15) or the
round-13 adversary-exchange class (round 13's finding refuted a
*single-choice/existential* exchange **at a fixed candidate point**, not
this two-stage extremal-selection-then-transfer argument on the *response
itself*— worth double-checking they are not the same before building).

**Recommendation: do NOT open a 4th top-level approach this round.** The
lp-duality/global-lp-vertex/self-similar trio still have concrete,
non-exhausted, correctly-diagnosed next steps (Step-0 reassembly; the
aimo-0119-style exchange argument as a *new mechanism inside*
`global-lp-vertex-sufficiency`, not a new slug — its Sigma-shape gap is
already that approach's designated home for exactly this kind of
argument). Feed the aimo-0119 lead into `global-lp-vertex-sufficiency`'s
next-round dispatch as a new mechanism to cheap-kill numerically before
investing proof effort (see cheap-kill below), rather than spinning up a
structurally-separate 4th approach — CLAUDE.md's diversity rule is about
the *field*, and the field is not stuck on one framing (3 approaches, 3
distinct obstructions, no shared-gap trap currently), so a plateau-break
approach is not warranted per the round-13/round-14 precedent (both times
the outliner declined to open a break approach when the sibling
approaches still had live, distinct leads — same situation now).

### (3) lp-duality-split-polytope's soft numeric lead (s<n-1 never reaches floor)

This is a **narrow, secondary** question — whether `s=n-1` active pieces
is *necessary* (not just sufficient, already proved via the certified
Perfect-Tie-Family Characterization Theorem, round 12) to reach the
universal floor `V=1/2` specifically at the region vertex `e_0`. It does
NOT bear on the critical-path gaps (GT(m) sub-case (i), Sigma-shape); it's
a self-contained sub-question about one specific vertex.

- The round-16 evidence (Nelder-Mead, `n=8,10`, `s=n-2,n-3,n-4`, best
  `≈0.5007-0.503`, margin shrinking as `s→n-1`) is **numeric only, float
  optimizer, not exact arithmetic** — same caliber of evidence that round
  9 found could give false negatives (concavity) and false positives
  (round 8's speed-cap artifact) elsewhere in this project. Per the
  standing rule (NEVER trust a "residual shrinking to zero"/no-violation
  numeric claim without independent high-fidelity re-verification), this
  lead is *suggestive but not solid* yet.
- **Recommendation:** worth firming up cheaply if a builder has spare
  capacity (not the critical path) via one of two routes: (a) exact
  rational-arithmetic re-verification at a few concrete small `n` (`8,9,10`)
  replacing the float Nelder-Mead, to rule out an optimizer-precision
  artifact near the shrinking margin; (b) a genuine counting/injection
  argument in the style of the already-certified Mass-Constraint Theorem
  (round 11, `Π>=1/2` forces `s>(n+1)/3`) — i.e., try to *derive* `s>=n-1`
  as a necessary condition for hitting the exact floor via a mass/parity
  count, rather than more sampling. If (b) succeeds it would be a genuine
  proved sub-result (not just consistent numerics), reusable as a
  structural fact about the vertex `e_0`'s extremal family — but this is
  a "nice to have," not blocking anything else.
- Not a dead end, but also not a priority: hold at "light/secondary" as
  current.md's own round-17 dispatch note already says.

### Candidate technique(s)
- self-similar-induction-on-n: fix Step 0's identity chaining using the
  reviewer's already-derived two-step relation `O_j=2^{j-1}+O_{j-2}`
  (q=0 at both levels j, j-1) — purely a correct-assembly task, no new
  lemma needed.
- global-lp-vertex-sufficiency: try the aimo-0119-style two-stage
  extremal-selection + single-fragment-transfer-non-improvement argument
  as a NEW mechanism for the joint branch-comparison/within-branch-tie
  family (cheap-kill it numerically first, per the mandatory-cheap-kill
  rule this project has followed since round 9).
- lp-duality-split-polytope: exact-arithmetic firm-up of the `s<n-1`
  numeric lead, or a Mass-Constraint-style counting argument, as spare-
  capacity work only.

### Cheap-kill candidates
- For the aimo-0119 exchange lead: before any proof investment, check
  numerically (exact `Fraction`, small n) whether "the OddSum-minimizing
  legal response, tie-broken by fewest tied fragments, is stable under
  single-fragment transfer from the largest tied group to the smallest"
  — this is directly testable against the already-catalogued hard `n=3,4`
  points in `global-lp-vertex-sufficiency.md` Section 7 with no new
  infrastructure.
- For lp-duality's `s<n-1` lead: rerun with exact rational arithmetic
  (sympy `Rational` / `Fraction`) at `n=8,9,10` restricted to the box
  constraints already flagged (avoid the documented negative-fragment
  optimizer artifact) before trusting the float result further.

### Knowledge-base entries to use
(No specific new knowledge_base.md entries surfaced this round beyond what
prior rounds already cite — the problem-specific machinery lives entirely
in the certified `lemmas/` directory at this point; knowledge_base.md's
generic LP/exchange-argument and pigeonhole entries remain the relevant
general background for the two live routes above, consistent with prior
rounds' citations.)

### Analogous past problems (cruxes)
- **`aimo-0119`** (Dutch TST, combinatorics/extremal-principle) — genuinely
  analogous min-max distribute-into-groups problem; its exchange-argument
  crux move (extremal selection by max-load then by count-at-max, then
  single-item-transfer non-improvement) is a concrete, untried mechanism
  for `global-lp-vertex-sufficiency`'s Sigma-shape gap. Caution: its
  `past_problems_database.json` entry has 6 `solutions` entries covering
  multiple sub-problems of that TST sheet; the relevant one is the LAST
  entry (cards-in-boxes), not the first (which is an unrelated recurrence
  problem) — same "verify solutions field matches the actual crux" caution
  as round 4's aimo-0127 mismatch.
- No other crux in `games-and-strategy` (any domain) or a broader sweep of
  `technique`/`how_used` text for "alternating," "peel," "vertex,"
  "polytope," "tie" turned up anything closer than the already-known
  aimo-0003/aimo-0019 (already used) and aimo-0146 (already used, per
  memory rules) — confirms no untapped strong match beyond aimo-0119.

### Prior progress
See current.md — 3 live approaches (self-similar-induction-on-n,
global-lp-vertex-sufficiency, lp-duality-split-polytope), ~40 certified
lemmas. Critical path: GT(m) sub-case (i) width-1 window (all e>=0, full
open, fix is a diagnosed reassembly not a new proof); Sigma-shape joint
branch-comparison/within-branch-tie family (open, no mechanism proven yet,
4 topology families ruled out).

### Dead ends (do not retry)
- Cyclic pairwise-tie chain, star/tree topology, descending fragment
  chain, response-side/single-choice adversary-exchange (all refuted,
  rounds 13-16) — do not re-attempt any of these four bounded-topology
  or single-choice-exchange families for the Sigma-shape gap.
- Naive one-step Odd→Odd chaining of the peeling identity across `e`
  peels (round 16's bug) — the correct relation is the two-step
  `O_j=2^{j-1}+O_{j-2}` (both levels q=0), not a one-step relation.
- Region-geometry-driven exchange mechanisms (fixed-boundary, tightest-gap
  symmetric, existential-over-candidates) — refuted round 13, do not
  retry.

### Small-case / intuition notes
- The GT(m) Step-0 bug is arithmetic, not structural: a concrete
  counterexample (k=1,e=1,m=2: OddSum=3.96<4) pins the failure to one
  identity-chaining step, and the corrected two-step relation was already
  independently verified (3000 trials, zero violations) — this is about
  as close to "just needs correct bookkeeping" as this project's gaps get.
- lp-duality's `s<n-1` numeric evidence (best ≈0.5007-0.503 at n=8,10,
  margin shrinking toward s=n-1) is a **conjecture**, not yet a proof;
  treat consistent-with, not confirmed.
