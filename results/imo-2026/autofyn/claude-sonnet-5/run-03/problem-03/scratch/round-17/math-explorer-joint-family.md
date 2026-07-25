## imo-2026-03 (lens: joint Σ-shape / combined-degeneracy family)

- **Distinct openings surfaced this round:**
  1. **Self-Bisection-Crossover family.** Independently re-implemented (own
     from-scratch script, `/tmp/round-17/probe.py`, `flat_check2.py`) the
     round-16 diagnostic at the 3 catalogued $n=3$ hard points and confirmed:
     at hard point 3, $(0.4211,0.3348,0.1910,0.0531)$, the winning shape's
     within-branch tie ($0.0955=0.0955$) is a **genuine sharp local minimum**
     — a fine sweep of the free split parameter $x$ around $x=p_2/2$ shows a
     true kink (value strictly increases moving either direction away from
     $x=p_2/2$; the "flat window" is $\approx2\times10^{-4}$ wide, i.e.
     numerical-precision-scale, not a real degenerate direction). This is a
     concrete, testable **joint mechanism**: a piece bisects itself exactly
     in half, and that exact halfway point is *simultaneously* the boundary
     where the relative rank-order of that piece's two fragments against a
     third element flips (a within-branch tie sitting exactly on a
     branch-comparison/rank-order kink). Candidate family: parametrize by
     (a) *which* piece(s) are chosen to self-bisect (a discrete/topology
     parameter — this is the "branch" choice) and (b) the resulting
     bisection value $p_i/2$, required to coincide with a genuine rank-order
     crossover against a neighboring fragment or untouched piece (the "tie"
     equation) — giving exactly the two coupled conditions (discrete branch
     choice + continuous tie value) the round-16 diagnostic asked for. This
     differs structurally from all 4 previously-refuted families (cyclic,
     linear-chain, descending-chain, star/tree): those all tie **fragments
     of two different pieces** to each other; this ties **a piece to
     itself** (exact self-bisection) and separately requires that value to
     hit a rank-order boundary — a genuinely different combinatorial object,
     not a variant of the same tie-graph topology.
  2. **Flat-Edge family (new, possibly higher-value opening).** The *same*
     experiment at hard point 1, $(0.4416,0.3035,0.1851,0.0698)$, found the
     **opposite** structure: no sharp self-bisection, but instead a
     genuinely **wide flat interval** of the free split parameter $x$ (piece
     3's fragment) — width $\approx0.091$ (from $x\approx0.047$ to
     $x\approx0.138$), three orders of magnitude wider than any numerical
     tolerance used elsewhere in this file's history — over which the exact
     same minimal value $0.5114$ is attained (re-optimizing the co-adjusting
     partner fragment at every $x$ in the sweep). This means the true
     optimal-shape set at hard point 1 is (at least numerically) a whole
     **1-dimensional edge**, not an isolated vertex or a small finite set of
     tied vertices as round 16's "≥5 branches tied" table implicitly framed
     it. **This reframes the round-16 finding**: some of the reported
     "branch-comparison-boundary near-degeneracy" may be *samples along one
     shared flat edge* (different nominal $\mathbf m$/pin-choices are just
     different points of the same edge, or its zero-padded extensions per
     the already-certified Zero-Removal Invariance Lemma) rather than
     independent isolated vertices genuinely colliding. If true generally,
     the "joint family" the outliner should target may not be a
     0-dimensional vertex candidate at all, but a **whole degenerate face
     (edge) of $Q$**, with the true extremal $p^*$ possibly living at an
     *endpoint* of such an edge (where the edge itself terminates against a
     third constraint) — a genuinely different top-level target than either
     of round 16's two named families. **This is the most promising and
     least-explored opening; recommend the outliner treat it as a rival
     approach in its own right, distinct from both round 16 candidate
     families.**
  3. **Zero-Removal-explained ties are a red herring, but not the whole
     story.** Several of the round-16-reported "tied branches" at point 2
     (e.g. $\mathbf m=(1,0,1,0)$ vs. $(1,0,1,1)$ vs. $(1,0,2,0)$) are exactly
     explained by the already-certified Zero-Removal Invariance Lemma
     (`lemmas/generalized-twin-anchor-floor-theorem.md`'s sibling result,
     `lemmas/vertex-pinning-lemma.md`-adjacent content in Section 6.2 of the
     approach file): adding a cut that produces a genuinely $0$-valued (or,
     in my re-run, near-$0$) fragment cannot change OddSum, so of course
     many nominally-different $\mathbf m$ tie trivially. This **does not**
     invalidate round 16's core finding (several *non-trivial*, non-zero-
     padding branch ties remain, e.g. $(1,0,1,0)$ vs. $(1,1,0,0)$ at point 1,
     which use genuinely disjoint pairs of split pieces, $\{1,3\}$ vs.
     $\{1,2\}$ in 1-indexed terms) — but it means a chunk of the observed
     "≥5-way degeneracy" is not new phenomenology and should be filtered out
     before counting "how many genuinely distinct branches tie."

- **Candidate technique(s):** (i) local sensitivity/perturbation analysis
  (sweep the free continuous parameter within one fixed cut-allocation and
  check for a kink vs. a flat interval — cheap, exact-arithmetic-capable,
  and immediately distinguishes "genuine joint vertex" from "flat edge"
  from "zero-padding artifact"); (ii) LP-duality / complementary-slackness
  language: a **flat edge** of $Q$ corresponds to a *degenerate* LP vertex
  in the underlying per-cell affine-optimization (multiple optimal bases),
  which is the natural LP-theoretic explanation for "co-occurring
  degeneracies" — the existing Global Vertex Lemma / finite-cell machinery
  (Section 4 of `global-lp-vertex-sufficiency.md`) already has the language
  ($L$'s between-branch and within-branch functional groups) to state "this
  cell's optimum is degenerate" but has not yet been used to test for
  *edges* of $Q$, only isolated vertices — this is the concrete next
  formalization step, not a new proof technique.

- **Cheap-kill candidates:**
  - Before trusting any joint-family construction, **run the sweep-for-
    flatness test** (as above) at each catalogued hard point: if the
    within-branch "tie" is a flat interval of width $\gg10^{-6}$, it is
    evidence for the edge-type opening (2), not the sharp-crossover opening
    (1); if the interval width is at numerical-precision scale, it supports
    opening (1). This is a $<5$-line, cheap, decisive discriminator to run
    at all 8 hard points before either family gets proof investment.
  - Filter branch-comparison ties through the certified Zero-Removal
    Invariance Lemma first (checked at points 1, 2 in my re-run): any tie
    between $\mathbf m$ and $\mathbf m'=\mathbf m+e_i$ (one extra cut on an
    otherwise-identical shape) where the extra fragment is $\approx0$ is not
    new phenomenology and should be excluded from the "how many genuinely
    distinct branches" count.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s generic
  entries were newly implicated this round beyond what prior rounds already
  cited (Vertex Pinning Lemma, Lipschitz/order-statistic facts, standard LP
  vertex-of-affine-function-on-polytope fact) — I did not find a
  knowledge-base entry specifically about **degenerate LP vertices /
  multiple optimal bases** (the natural formal language for opening (2));
  if the outliner wants to formalize the Flat-Edge opening rigorously, it
  will likely need to introduce this as new content (complementary
  slackness / degenerate-basis characterization), not import it.

- **Analogous past problems (cruxes):** searched `combinatorics` /
  `games-and-strategy` (39 cruxes) and skimmed the closest-sounding hit,
  `aimo-0117` (a stone/box value-balancing game using a doubling/dyadic
  power-of-2 assignment strategy, "the largest power strictly exceeds the
  sum of the others"). This is a superficial dyadic-structure analog (the
  project's own $\Gamma$/OddSum machinery is also fundamentally about
  powers of 2) but it is a **first-player constructive strategy** problem,
  not an LP-vertex/degenerate-optimum classification problem — **not
  genuinely analogous** to the joint-degeneracy classification task at
  hand. No other crux in `games-and-strategy`, `extremal-principle`, or
  `linear-algebra-method` (skimmed titles) targets "multiple simultaneous
  tie types at an LP optimum." **Verdict: no strong match in the corpus for
  this specific joint/coupled-degeneracy classification technique** — this
  is consistent with the problem's genuinely unusual double-minimax
  structure (a game value that is itself a min over a max over multisets),
  which the pre-2026 crux corpus (largely single-layer combinatorial games)
  does not have a close counterpart for.

- **Prior progress:** `global-lp-vertex-sufficiency`'s round-16 numeric
  classification (8/8 points show branch-comparison-boundary degeneracy;
  5/8 co-occur with within-branch ties) stands, independently reproduced
  this round at all 3 catalogued $n=3$ hard points (own script, values
  $0.51140,0.51500,0.51660$ matched digit-for-digit against the file's
  reported values). No lemma certified on this line yet.

- **Dead ends (do not retry):** the 4 bounded tie-topology families
  (cyclic, linear-chain, descending-chain, star/tree) — confirmed still
  dead per run_state's Rules; my re-derivation gives no reason to revisit
  them. Also: do **not** assume the round-16 "≥5-way branch degeneracy"
  count is 5 genuinely independent vertices colliding — my re-run shows at
  least part of it is Zero-Removal padding (not new) and at least one point
  (point 1) is actually a continuous flat edge, not discrete ties at all —
  treating the raw "≥5" count at face value would overstate how special
  these points are.

- **Small-case / intuition notes (all conjectural, numerical only, own
  independent re-implementation, not exact rational arithmetic except
  where stated):**
  - Point 3 ($n=3$): sharp joint vertex — self-bisection of piece 3
    ($p_3=0.1910\to0.0955,0.0955$) exactly at a rank-order kink. Genuinely
    matches round 16's "within-branch tie" report and is a real (not
    artifact) local phenomenon.
  - Point 1 ($n=3$): a genuine flat **edge** of width $\approx0.091$ in the
    free-split parameter, all achieving the identical value $0.5114$ —
    a structurally different (and previously unreported) degeneracy type,
    likely underlying much of the "≥5 branches tied" observation there.
    Recommend the next round explicitly test whether hard point 1's true
    maximizer status ($p^*$ vs. merely a near-maximizer) is itself sitting
    at one of this edge's two endpoints (test the edge's endpoints in exact
    `Fraction` arithmetic before building any theory on this point).
  - Point 2 ($n=3$): several reported "tied branches" are explained by
    Zero-Removal padding (extra wasted cuts); the genuine content (if any)
    beyond that was not re-verified this round for lack of time — flagged
    as an open item for whichever approach picks this up.
  - No claim is made about $n=4$ hard points this round (not re-run,
    budget-limited) — round 16's own $n=4$ table entries are taken as
    reported, not independently re-verified here.
