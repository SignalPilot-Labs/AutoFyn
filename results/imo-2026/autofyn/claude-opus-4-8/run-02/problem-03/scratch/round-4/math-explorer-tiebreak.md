## imo-2026-03 (GAP-L residual: tied non-degenerate minimizer, lens = tie-breaking/reduction)

- **Distinct openings** (this lens surfaced one strong new route, sharply different from
  "prove f≥1 directly at the tie"):
  1. **LP-vertex reduction.** `f` restricted to any fixed cut-pattern chamber is *affine with
     integer ±1 coefficients* (Lemma I's slopes are always ±1), and the chamber itself is a
     polytope cut out by hyperplanes with **integer** equations (`x_i=x_j`, or `x_i = 2^k` for a
     fixed uncut piece, or `x_i=0`). By standard LP theory the min of an affine function over a
     compact polytope is attained at a **vertex**. So the global minimizer (over all ≤n-cut
     refinements) can be taken to be an actual vertex of this rational hyperplane arrangement —
     i.e. pinned by enough tight equalities to be 0-dimensional. Every vertex is either
     degenerate (`x_i=0`, closed by induction) or non-degenerate and pinned *purely by ties*
     (with itself or with another fixed/variable piece).
  2. **Block-decomposition identity (new, exact, provable — the key finding).** If a set of `r`
     sub-pieces of ONE original piece occupies a *contiguous* run of ranks `[a, a+r-1]` in the
     global sort order (guaranteed to hold locally in a neighborhood of a tie, since at the tie
     itself the `r` values are exactly equal, hence trivially contiguous — verified numerically,
     see below), then
     ```
     contribution of that block to f(P) = σ_a · f_block(v_1,...,v_r)
     ```
     where `f_block` is the **same alternating-sum function** applied just to the block's own
     `r` values (`v_1≥...≥v_r`, summing to the piece's fixed total `2^k`), and `σ_a=(-1)^{a+1}`
     is the sign at the top of the block. This is an exact identity (trivial consequence of
     grouping the definition of `f` by contiguous rank ranges — essentially Lemma A/B's
     top-band decoupling generalized to an *arbitrary* rank band, not just the top one).
     Verified numerically for random contiguous blocks (embedded so the block ranks are
     genuinely consecutive): exact match to machine precision; confirmed it FAILS when the
     block is not rank-contiguous (as expected — contiguity is exactly what a tie guarantees).
  3. **Consequence: the tied-vertex problem is exactly a smaller COPY of the same
     extremal problem.** Locally perturbing the `r` tied sub-pieces of one piece (holding
     everything else fixed) changes `f` by exactly `σ_a` times the change in `f_block`, an
     `r`-element alternating-sum minimization/maximization on the simplex `{v_i≥0, Σv_i=2^k}` —
     literally the same type of object the whole problem is about, one level down. This gives
     genuine strong-induction traction (on `r`, or on total sub-piece count) rather than a
     bespoke inequality: if `σ_a=+1` we need `f_block` minimized, if `σ_a=-1` we need it
     *maximized*, and both extremes of the *same* alternating sum are governed by the *same*
     toolkit (Lemma 0's `0≤f≤Σ` bounds, Lemma J/degenerate induction applied recursively to the
     block).
  4. **Direct numeric confirmation the "residual" example is a false alarm.** Full vertex
     enumeration for the given example ({4/3,4/3,4/3,2,1}, piece `4→x,y,z`, fixed `2,1`): the
     *only* vertex with non-integer `f` is the fully-symmetric internal tie `x=y=z=4/3`
     (`f=5/3`), and it is **strictly dominated** — every other candidate vertex (any vertex where
     at least one tie crosses to an external/different piece) has **integer** `f` (`f∈{1,2}`),
     and the true minimum over the whole chamber is `f=1`, attained at genuinely integer
     configurations like `{2,2,1,1,1}` (an *already-Theorem-F-covered* configuration). Repeated
     for the analogous `n=3` case (piece `8→x,y,z`, fixed `4,2,1`): same pattern — symmetric
     point gives `f=7/3` (non-integer, dominated), every cross-tie vertex gives integer `f`
     (values `1,3,1,3,2,1,1`), true min `=1`.

- **Candidate technique(s):** the block-decomposition identity above, combined with strong
  induction on total sub-piece count / cut budget (the SAME induction skeleton already used for
  the degenerate leg), applied recursively to the tied block as a smaller instance of the
  identical alternating-sum minimization. This is a genuinely new lever not used in Lemma I/J
  (which only handle tie-*free* points) — it directly attacks exactly the case Lemma J excludes.

- **Cheap-kill candidates:** none beyond what's used — the LP-vertex argument itself is a cheap
  structural reduction (no computation needed): it already rules out "flat unbounded" pathologies
  since the domain is compact and finitely many chambers, so the argument is airtight as a
  *reduction*, even though the recursive step (bounding `f_block` appropriately signed) is not
  yet fully closed.

- **Knowledge-base entries to use:** the KB's general "layer-cake / alternating sum" and
  "extremal induction / self-similar recursion" style entries (matches the existing certified
  Lemma 0, Lemma L layer-cake, and Lemma I/J already in `lemmas/`) — no new external KB entry
  needed; the fix is internal (a new identity building on Lemma I).

- **Analogous past problems (cruxes):** did not find a corpus problem whose crux is specifically
  "alternating-sum tie-block recursion" — the self-similar block-decomposition here is closely
  parallel in *spirit* to Lemma A/B's top-band decoupling (already in this workspace, not the
  corpus), so I did not force an external match. (Did not have time this round to do a full
  corpus subtopic sweep given the numeric investigation above; recommend the outliner or a future
  explorer round check `crux_moves_documentation.md` subtopics "extremal combinatorics" /
  "alternating sums" / "game theory / adversary" specifically for a block-recursion match.)

- **Prior progress:** as recorded in `current.md` / `self-similar-recursion.md` — GAP-U fully
  closed; GAP-L closed on tie-free non-degenerate (Lemma J) and degenerate (induction) cases;
  residual is exactly the non-degenerate tied vertex.

- **Dead ends (do not retry):** matched-pair-deletion induction on the tied pair directly (already
  recorded as obstructed in `current.md` — breaks dyadic conservation `Σ(sub-pieces)=2^k`). My
  investigation confirms *why* this fails and offers the fix: don't delete the pair, instead
  recurse on the **within-piece alternating sum of the tied block itself** (block-decomposition
  identity above), which does NOT break conservation (the block's own sum is exactly `2^k`,
  preserved) — this is the natural replacement for the failed deletion-induction idea.

- **Small-case / intuition notes (conjectural but numerically strong):**
  - The purely-internal-symmetric tie (all `r` sub-pieces of one piece mutually equal, no
    cross-piece tie) is **never the true minimizer** — confirmed by exhaustive rational vertex
    enumeration for two small cases (`n=2`: piece 4→3 parts; `n=3`: piece 8→3 parts). In both,
    the symmetric point gives a strictly larger, non-integer `f`, dominated by nearby integer
    vertices.
  - Every vertex with at least one tie crossing to a *different* piece (or to a fixed/uncut
    piece) has **integer** `f` in both tested cases — suggesting the recursive block-reduction
    "bottoms out" at integer configurations exactly when the tie is not purely internal, which
    would let Theorem F (integer parity) finish those sub-cases immediately, leaving only the
    purely-internal-symmetric point to handle via the recursive `f_block` argument (and that
    point is conjectured to never be the true min, i.e. `f_block` can always be perturbed to
    decrease/increase appropriately toward its own boundary — degenerate or cross-tied — a smaller
    version of the exact same problem, terminating by induction on block size `r`).
  - This is evidence, not proof: the recursive step (showing the internal-symmetric tie-block
    point is always dominated, in full generality for all `r`, `2^k`, and arbitrary surrounding
    structure, not just these two hand-checked cases) is the concrete remaining task — but it is
    now a **precisely-scoped smaller claim** (a self-contained statement about one alternating-sum
    block against its own boundary) rather than the amorphous "handle all ties" gap.
