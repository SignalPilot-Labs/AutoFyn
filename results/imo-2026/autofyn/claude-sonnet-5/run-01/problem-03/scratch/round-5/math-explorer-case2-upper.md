## imo-2026-03 — lens: Case (ii) upper bound at general m≥3 (`dyadic-cascade-induction` /
`potential-weighting-upper-bound` framework)

**Explicit confirmation up front:** everything below is a genuinely different mechanism class.
Nothing here is a variant of Rule 1 (top-two-ratio greedy), Rule 2 (smallest-gap greedy), or the
"K-level lookahead + scalar-IH fallback" induction-loading family — all three remain dead,
confirmed by re-deriving the round-3/4 counterexamples myself (see Verification below) before
building on them.

### Distinct openings

**1. (Primary, strong new numerical support) "Chain-prefix + static one-shot allocation"
— a structurally different mechanism, not a lossy-fallback scheme.**

Restrict Lemma D/M's operation-sequence space (already certified, `lemmas/dm-operation-
reformulation.md`) to a two-parameter *static* family, indexed by an integer `c` (`0≤c≤m`), not
by an adaptive/sequential decision process:
- **Chain-prefix of length `c`:** repeatedly `M`-merge the *running top result* against the next
  original element, `c` times: `r_0=a_1`, `r_i = M(r_{i-1}, a_{i+1})` for `i=1..c` (this is
  literally `c` applications of Lemma D/M's `M` operation, so achievability is automatic — no new
  achievability lemma needed).
- **One-shot tail:** on the resulting multiset `{r_c} ∪ {a_{c+2},…,a_k}` (`k-c` elements), with
  the remaining budget `m-c`, take the *exact* optimum over the (finite, non-adaptive)
  "one-shot allocation" subspace: every further `D`/`M` operation acts **only on elements of this
  fixed residual set**, never on a value produced by another operation in the tail (i.e. no
  further cascading) — a static matching/deletion problem on `k-c` fixed numbers, decomposable via
  the already-certified **Fact 3** (block extraction, `lemmas/insertion-and-cascade-facts.md`).
- Take the **minimum over `c=0..m`** of (chain-prefix value, then exact one-shot-tail optimum).

**Why this is not a repackaged bounded-lookahead scheme (the critical distinction):** round 4's
dead mechanism failed because, after a *bounded* explicit prefix, it fell back to a **lossy
scalar bound** `e_{m'}·S(residual)`. This family has **no lossy fallback anywhere** — the tail is
evaluated by its own *exact* optimum over its (admittedly restricted, but fully searched) static
subspace, and the chain-length `c` ranges over the *entire* `0..m`, not a fixed small `ℓ`. The
thing being conjectured is not "a bounded amount of lookahead suffices to make a lossy bound
valid" but "the TRUE minimum of a specific *structured, finite* family of legal strategies (not
the whole exponential game tree) already meets the target, with no bound-tightening needed." This
is a difference in kind, not degree.

**Numerical evidence (all exact `fractions.Fraction`, not floats), built and cross-checked by me
this round:**
- Re-derived the two certified-dead-end counterexamples independently first (sanity check before
  building anything new): `A_1=(239,112,75,74)/500`, `m=3` (Rule 1's counterexample) and
  `A_2=(1/2,333/1000,167/1000)`, `m=2` (Rule 2's counterexample) — confirmed both fail plain
  one-shot-only and greedy rules exactly as the round-3/4 files report.
- **Pure one-shot allocation alone (no chain), tested first:** passed 650+ random Case-(ii)
  trials (`m=2..6`, including boundary cases with `a_1` close to `2a_2`, near-uniform/near-tie
  configurations) — *but* I found a genuine counterexample where pure one-shot fails and true
  cascading is required: `A=(23,12,6,3)`, `m=3`. Target `e_3·S = 44/15 ≈ 2.9333`; best pure
  one-shot value is `3` (fails, `3 > 44/15`); the true optimum (full D/M search) is `2`, achieved
  only by the cascading sequence `M(23,12)=11 → M(11,6)=5`, giving final `{5,3}`, `e=2`. **This
  is a real, useful negative result: pure static one-shot allocation is not universally
  sufficient by itself** (report this as a partial dead end for "one-shot alone," distinct from
  the chain+one-shot combination below).
- **Chain-prefix + one-shot tail, combined (the actual proposal):** solves all three known hard
  cases exactly (`A_1→1/500`, well under `1/15`; `A_2→0`, well under `1/7`; `A=(23,12,6,3)→2`,
  under `44/15`, via `c=2`). Stress-tested with **~650 additional fresh random Case-(ii) trials**
  (`m=2,3,4` uniform random, `m=2,3,4` boundary-focused with `a_1 ∈ [1.9a_2, 2a_2)`, `m=3,4,5`
  with forced near-ties, `m=6` spot check) — **zero failures** across all of it. This is strong
  (though purely numerical/conjectural) support for a genuinely new closure mechanism.
- **Caveat, honestly flagged:** this is small-`k`/small-`m` numerical evidence only, not a proof.
  I did not find a closed-form argument for *why* `min_c(...)` always works — that is exactly the
  gap for the outliner/builder to attack, likely via an exchange/rearrangement argument on the
  static one-shot sub-problem (see opening 2) combined with a case split on `c`.

**2. Exchange/rearrangement argument on the static one-shot sub-problem itself.** Since the
one-shot tail is a *finite, non-adaptive* combinatorial optimization (choose a partial matching +
deletion set on a fixed list of numbers, no game-tree order-dependence), it is a natural target
for a rearrangement-inequality-style exchange argument: conjecture that the optimal one-shot
matching always pairs *sorted-adjacent* elements (never crosses), which would collapse the search
from exponentially many matchings to `O(k)` candidates and make Fact 3 (block extraction)
directly applicable to compute its value in closed form. I did not verify this narrower
adjacency conjecture this round (no time) — flagging it as the natural next probe, structurally
analogous to the "sorted-adjacent pairing" cruxes found in the corpus (see below).

**3. Majorization / Schur-convexity as a genuinely different global invariant.** `e(M)` for
sorted `M` looks Schur-convex under majorization (spread-out multisets have larger `e`; e.g.
`e(3,1)=2 > e(2,2)=0` and `(2,2)` majorizes... — actually `(3,1)` majorizes `(2,2)`, consistent
with `e` increasing with spread). If `D`/`M` operations can be shown to always move the active
multiset toward being majorized by a canonical "balanced" benchmark with known `e`-value within
`m` steps, that would give a global argument with no per-state lookahead at all — a genuinely
different budget-aware invariant from anything tried so far. **Not tested this round** (flagged
as an idea only, per the "note it and stop" rule) — worth a dedicated future probe, but note the
already-certified negative result in `concavity-minimax-duality.md` (Φ(M,r)=S(M)/(2^{r+1}-1)
passes for `D`-moves but fails for `M`-moves with two exact counterexamples) shows the *simplest*
single-scalar rescaled-budget potential is dead; majorization is a strictly richer (vector-valued,
order-theoretic) invariant than that scalar Φ, so it is not simply a re-skinning of the already-
falsified candidate, but any future attempt must explain why it survives where Φ failed.

**4. Duality/certificate framing — not separately pursued, folded into opening 1.** The dispatch
asked about a "certificate strategy for XY constructed directly from the target bound, argued by
contradiction." Opening 1 is effectively this: instead of adaptively choosing XY's moves in
response to LB's, it *directly constructs* a candidate response (parametrized by `c` and a static
matching) from the target and verifies it meets the bound — no simulation of "what LB does" is
needed since LB has already committed to `A` before XY moves. I did not find a separate
contradiction-style argument beyond this.

### Candidate technique(s)

- Restricted-subspace static optimization (opening 1) + exchange/rearrangement argument on sorted
  lists (opening 2) — closest in spirit to the KB's "rearrangement inequality" idea and to
  `lemmas/insertion-and-cascade-facts.md`'s Fact 3 (block extraction), which already gives the
  exact formula for splitting a sorted multiset into a dominant block plus residual — directly
  reusable for scoring any specific `(c, matching)` candidate without new machinery.
- Majorization/Schur-convexity (opening 3) — a genuinely different global order-theoretic
  invariant, distinct from the already-falsified scalar `Φ=S/(2^{r+1}-1)`.

### Cheap-kill candidates

- Before investing in a general proof of opening 1's conjecture, the builder should first try to
  **falsify it harder** than I did in the time available: push denominators/`m` further, and
  specifically hunt near `a_1` just under `2a_2` with several near-tied lower elements (the shape
  of my one counterexample `(23,12,6,3)`, which needed `c=2`) — if a case needing `c` close to `m`
  (deep chains) turns up, that would be a strong signal the mechanism degenerates the same way
  bounded lookahead did, and should be reported as a new dead end rather than pursued further.
- Cheap structural check: verify whether the one-shot tail's optimal matching is *always*
  sorted-adjacent (opening 2) on the ~15 hardest instances already on file across all approach
  files — a fast confirm/refute before attempting a general proof.

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section) — generic pointer for opening 3.
- **Rearrangement inequality territory** is not named explicitly in `knowledge_base.md` as a
  standalone entry, but the "Piecewise-concavity smoothing" and general exchange-argument
  heuristics under "Problem-Solving Heuristics (Pólya)" (specialize/reformulate) support the
  exchange-argument framing of opening 2.
- **Hall's marriage theorem / SDR** — potentially relevant if opening 1/2's static matching
  problem is cast as a bipartite matching/allocation with a feasibility side-condition (not
  verified this round, but a natural fit given the "one-shot allocation" framing is literally a
  matching problem on a fixed vertex set).

### Analogous past problems (cruxes)

- **`aimo-0388`** (combinatorics, subtopic `telescoping-and-summation`) — "coins" problem:
  splitting a sorted 100-element list into two stacks via pairing consecutive elements so each
  pair's contribution telescopes to a non-positive gap, leaving isolated boundary terms. This is
  **structurally the same alternating-pairing identity already fully exploited** in this project
  (Facts 1–3, Lemma P) — confirms the existing machinery is the standard tool for this shape of
  problem, but does **not** by itself resolve the sequencing/cascading subtlety that is the open
  gap here. Relevant as confirmation, not as a new idea.
- **`aimo-0758`** (algebra, subtopic `inequalities-SOS-and-convexity`) — "Shiny tuples": bounds a
  global pairwise-product sum by **decomposing it into edge-disjoint Hamiltonian-path sums** (via
  a residue-class relabeling) each covered by a known per-permutation bound, handling the
  leftover residual by a separate sorted-adjacent-pairing argument. The *decomposition-into-
  known-solvable-pieces-plus-structured-leftover* pattern is a loose structural analogy to
  opening 1's "chain-prefix + one-shot-tail" split (attack the top elements one way, the rest a
  different, simpler way) — worth reading for the flavor of a decomposition-based proof, but the
  underlying objects (pairwise products of a permutation vs. an alternating claiming game) are
  different enough that this is a loose analogy, not a directly transferable crux move.
- No crux in `games-and-strategy` (39 combinatorics + subset of number_theory entries checked)
  is a genuine analog: that subtopic is dominated by pairing/mirroring/blocking strategies for
  discrete combinatorial games (Nim-like, board games), not continuous-value alternating-claim
  optimization with an adversarial *cutting* phase before the claiming phase. None forced a match;
  reporting this honestly rather than stretching a weak analogy.

### Prior progress

See `results/imo-2026-03/current.md` and the approach files for full detail. Summarized here only
what's directly load-bearing for this lens: Lemma D/M (achievability of any D/M sequence),
Lemma P (duplicate-pair cancellation), Facts 1–5 (dominant extraction, block extraction,
insertion bound, chain-cancellation/ceiling-achievability) are all certified and directly usable
by the mechanism in opening 1 (chain-prefix is literally a sequence of certified `M` operations;
one-shot tail scoring uses Fact 3 directly).

### Dead ends (do not retry)

- **Rule 1 (top-two-ratio greedy)** — falsified, exact counterexample `A_1` at `m=3`
  (`37/500 > 1/15`). Re-confirmed by me this round.
- **Rule 2 (smallest-gap greedy)** — falsified, exact counterexample `A_2` at `m=2`
  (`83/500 > 1/7`). Re-confirmed by me this round.
- **Bounded-lookahead / induction-loading (any fixed depth `ℓ` independent of `m`)** — falsified,
  failure rate does not shrink with `m` for fixed `ℓ`. Not retried, and my opening 1 is explicitly
  designed to avoid its specific failure mode (no lossy scalar fallback, full range of `c`
  searched exactly).
- **New this round: "pure one-shot allocation alone" (no chain at all)** — genuinely insufficient
  by itself; concrete counterexample `A=(23,12,6,3)`, `m=3` (target `44/15≈2.933`, best one-shot
  `3`, true optimum `2` needs a depth-2 cascade). Record this so no future round re-proposes "just
  restrict to non-cascading moves" as if it were sufficient on its own — the chain-prefix
  component in opening 1 is not optional.
- **The scalar potential `Φ(M,r)=S(M)/(2^{r+1}-1)`** (already recorded in
  `lemmas/dm-completeness-partial.md`'s sibling file `concavity-minimax-duality.md` §9) — fails
  under `M`-moves with two exact counterexamples. Do not re-propose this exact scalar form; a
  majorization-based invariant (opening 3) is a different, richer object, not this.

### Small-case / intuition notes (all labeled conjecture — numerical evidence only, not proof)

- **Conjecture A (opening 1):** for every Case-(ii) configuration `A` (`a_1<2a_2`) and every
  `m≥1`, `min_{0≤c≤m}` [chain-merge top `c+1` elements, then exact one-shot optimum on the
  `(m-c)`-budget residual] `≤ e_m·S(A)`. Supported by ~650+ random exact-fraction trials
  (`m=2..6`) plus all 3 known hardest adversarial instances on file, zero failures found. Not
  proven; no closed-form argument found this round.
- **Conjecture B (refuted this round, recorded as a real finding):** "pure one-shot allocation
  (no chaining at all) always suffices" — **false**, concrete counterexample given above. The
  correct family needs the chain-prefix component.
- **Observation:** in every hard case found, the winning chain-prefix length `c` was small
  (`0`, `1`, or `2`) relative to `m` — unlike the bounded-lookahead family's diagnosed pathology
  (needing `ℓ=m`, the *entire* budget). This is the key structural difference suggesting opening 1
  is not just a relabeling of the dead mechanism — but this is only observed on `m≤6`; whether `c`
  stays bounded (or needs to scale with `m`) for larger `m` is untested and should be checked
  early next round before committing to a full proof attempt.
