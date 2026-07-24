# Explorer report — lens: integer-lattice / discrete-structure (round 3)

**Task.** Investigate whether recasting IMO-2026-03 (Liu Bang / Xiang Yu stick game,
conjectured `c(n) = 2^n/(2^{n+1}-1)`) discretely — via the ladder's `2^i`
structure, binary encodings, subset sums, or an integer-lattice/LP-vertex
argument — yields a route around the cross-term/interleaving obstruction that
has stalled all three live approaches (`greedy-halving-adversary`,
`smoothing-compactness-certificate`, `self-similar-potential-certificate`) for
two rounds. This is pure terrain scouting; no proof was attempted.

## 1. The natural discrete encoding

Scale the unit stick by `N := 2^{n+1}-1`. The ladder's piece lengths
`p_i = 2^{n+1-i}/N` become the integers `P_1,...,P_{n+1} = 2^n, 2^{n-1}, ..., 1`,
which sum to exactly `N` — i.e. **the ladder, rescaled, is literally the
binary representation of `2^{n+1}-1`** (all `n+1` bits set). This is a
genuinely clean, previously-unstated-in-this-form observation: `c(n)` is the
value of a game played on the all-ones binary string.

The standard fact about `{1,2,4,...,2^n}` (superincreasing, all `2^{n+1}`
subset sums `0..N` distinct and biject with binary strings) is the precise
reason the ladder is the *hardest* sequence for Xiang Yu to "matching-pair"
without cutting: **no two disjoint sub-collections of the whole original
pieces can ever have equal sum** (uniqueness of binary representation), so by
the certified `leftover-formula` lemma (Lemma 3, `greedy-halving-adversary.md`)
Xiang Yu is forced to actually cut pieces to create any matched pair at all —
he cannot get a free pairing "for zero cuts" the way he could against a
non-superincreasing sequence (cf. the already-recorded counterexample in
`greedy-halving-adversary.md` Open gap 1: `p=(1/2,1/3,1/6)` lets Xiang Yu
match `p_2,p_3` against `p_1` for free). This is a real, easily-provable
discrete fact and is *a* piece of "why superincreasing sequences are optimal,"
but by itself it only rules out zero-cut matches; it says nothing about what
happens once Xiang Yu is allowed to cut (which is the entire content of the
open gap).

## 2. Does an LP-vertex / rational-denominator argument sidestep the obstruction?

This is the framing the round-2 outliner registered as `integer-lattice-reduction`
(elo 1454, never built): for a *fixed* Liu Bang marking, Xiang Yu's
minimization of `Φ` over `≤n` cut points is, within each fixed combinatorial
"order type" (how the cut points interleave with each other and with Liu
Bang's breakpoints), an LP — `Φ` is linear in the cut positions on a polytope
— so the min over that type is attained at a vertex, a rational point whose
denominator is bounded by an integer determinant. This would reduce Xiang
Yu's problem to a finite (if large) rational/lattice search.

**I tested this directly** (exact-`Fraction` brute force, `/tmp/explore.py`,
`/tmp/explore3.py`): for `n=2` (search over cut positions with denominators up
to 28, and separately restricted to denominator exactly `7=N`) and `n=3`
(exhaustive lattice search, denominator `15=N`, all `\binom{14}{3}\times\binom{4}{1,\dots}`
placements of 3 cuts among the 4 pieces — 27720 configurations), the true
minimum `A = 1/(2^{n+1}-1)` **is** attained at lattice-aligned rational points
(denominator dividing `N`), consistent with the vertex-argument's premise.

**But this does not sidestep the obstruction — it only relabels it.**
Concretely:
- The optimum is highly *degenerate*: for `n=2`, configurations with
  denominators 7, 21, and 28 all tie exactly at `A=1/7` — the objective is flat
  across many combinatorially distinct cut placements, not resolved by a
  handful of "the" vertices.
- For `n=3`, restricting to lattice points still leaves 27720 raw
  configurations to search (and this is only for the *ladder*; the real
  problem needs this for *every* Liu Bang marking, plus the outer maximization
  over Liu Bang). The number of order-types grows combinatorially in `n`
  (roughly like ways to interleave `n` cut points among `n+1` breakpoints and
  each other), so "finite" is not "small," and nothing about the vertex
  argument tells you *which* vertex is worst — you still need exactly the
  same rank/interleaving-sensitive case analysis that stalled the continuous
  cross-term approach, just now phrased as "which lattice configuration
  minimizes `A`" instead of "which real-valued cut minimizes `A`." This
  matches the risk the outliner itself flagged when registering the approach
  ("the discrete core is no easier than the continuous one") — confirmed here
  computationally, not just anticipated.

**Verdict on the generic LP-vertex framing: not viable as a shortcut.** It is
a legitimate a-priori reduction (continuous → finite rational search) but
buys no leverage on the actual difficulty, which is combinatorial
(interleaving), not analytic (irrational optima). Do not spend a round trying
to close the general-`n` gap via raw vertex enumeration.

## 3. A genuinely new finding: an exact closed form at the *other* extreme (`c = n`)

All three approaches have fully closed the sub-case `c=0` (Xiang Yu spends
**zero** of his cuts on `p_1`, all `n` on the tail — Lemma 6 /
`untouched-top-piece-lower-bound`). The complementary extreme, `c=n` (Xiang Yu
spends **all** `n` cuts on `p_1` and **none** on the tail), had not been
checked in closed form by any approach. I tested the natural discrete/
self-similar strategy at this extreme: **fragment `p_1` into a scaled copy of
the same `n`-ladder** (fragments `q_i := p_1 \cdot p_i(n)`, `i=1,\dots,n+1`,
using exactly `n` cuts on `p_1`), leaving the tail `p_2,\dots,p_{n+1}`
completely untouched. Exact-`Fraction` computation for `n=1,\dots,8`
(`/tmp/selfsim.py`) gives `A = 1/(2^{n+1}-1)` **exactly, on the nose, every
time** — matching the conjectured target exactly, not just numerically close.

This has a clean, fully elementary proof (no cross-term bound, no numerics
needed) because the merge order is **provably perfectly alternating**:
`q_1 > p_2 > q_2 > p_3 > q_3 > \cdots > p_{n+1} > q_{n+1}`. Direct algebra
gives both comparisons in closed form:
- `q_i > p_{i+1} \iff 2^{n+1} > 2^{n+1}-1` (always true), and
- `p_{i+1} > q_{i+1} \iff 2^{n+1}-1 > 2^n` (true for `n\ge1`).

With this strict alternation, the `2n+1`-element multiset has all `q_i` at
odd rank and all `p_{i+1}` at even rank, so
`A = \sum_i q_i - \sum_{i\ge2} p_i = p_1 - (1-p_1) = 2p_1-1 = 1/(2^{n+1}-1)`
directly (using `\sum q_i = p_1\cdot\sum p_i(n) = p_1`). No casework, no
inequality-with-slack: this is an *equality*, and the interleaving pattern is
rigid, not merely bounded.

**Why this matters for the framing.** It shows the "self-similar/binary"
idea is not vacuous: at *both* extremes of the `c`-parameter (`c=0` and
`c=n`), the ladder's self-similarity gives an exact, cleanly provable value
matching the target — with the messy general-`c` interleaving problem
sandwiched in between. This reframes the open gap concretely: instead of "an
unproved cross-term inequality for arbitrary `c`," it is now "why can't Xiang
Yu do better than either exact endpoint for intermediate `c`" — i.e. a
monotonicity/convexity-in-`c` question, which is a structurally different (and
possibly more tractable) question than the raw interleaving bound the other
approaches stalled on. This is a real, if partial, piece of new terrain: **not
already recorded in any approach file** (the existing `self-similar-potential-
certificate.md` only closes `c=0` via self-similarity and explicitly gives up
on `c\ge1`; it does not notice the exact `c=n` closed form).

## 4. Overall assessment

- **Generic integer-lattice/LP-vertex reduction, as originally registered:**
  not viable as a way to *avoid* the obstruction — confirmed computationally
  that it reduces to a combinatorial search with no fewer cases than the
  continuous version, and the optimum is highly degenerate (many tied
  configurations), so there is no small set of "the" extremal vertices to
  case-check. Recommend not building this exact framing as originally
  scoped.
- **Binary/superincreasing subset-sum framing:** correctly explains why the
  ladder resists *zero-cut* matching (uniqueness of subset sums), but this is
  a fact the existing approaches already implicitly use (Lemma 3's
  characterization) and does not touch the real difficulty (matching *after*
  cuts).
- **New, real progress:** the exact self-similar `c=n` closed form above,
  proved by elementary strict-alternation algebra (no numerics, no gaps),
  complementing the existing exact `c=0` result. This is genuinely new and
  cleanly rigorous, and suggests a **repurposed** discrete approach for next
  round: bracket the general-`c` problem between the two now-exact endpoints
  and attack monotonicity/convexity of the optimal value in `c` (or show the
  worst case is always at an endpoint, `c\in\{0,n\}$, via an exchange
  argument moving one cut at a time between `p_1` and the tail) — rather than
  attacking the raw cross-term inequality head-on or pursuing generic LP-vertex
  enumeration. This is a different mechanism from what any of the three live
  approaches are doing (they attack the cross term directly, or a global mass
  potential), so it would add genuine diversity to the population, not just
  relabel the existing obstruction.
- Small-case evidence: `n=2` — exact search confirms minimum `A=1/7`,
  attained at lattice-aligned cuts, degenerate (tied at multiple
  denominators). `n=3` — exhaustive lattice search (27720 configs) confirms
  minimum `A=1/15`, with the unique (up to relabeling/position permutation)
  optimal multiset produced by cutting the top piece `8/15` into fragments
  `{8,16,32,64}/225` — exactly a rescaled copy of the `n=3` ladder itself,
  matching the `c=n` construction of §3 exactly.

## Recommendation for next round

Do not register a generic "integer-lattice-reduction via LP vertices"
approach as previously scoped — it is confirmed to buy no leverage. If a 4th,
genuinely different framing is wanted to break the plateau, consider instead:
**"self-similar bracketing"** — use the newly-found exact `c=0` and `c=n`
closed forms as the two ends of an induction/exchange argument showing the
optimum over `c\in\{0,\dots,n\}` (and, within each `c`, over how the tail/top
fragments are chosen) is always at an endpoint or reduces to the same value —
this is a concrete, previously untried mechanism (monotonicity-in-budget-split
rather than cross-term bounding) worth an outline slot.
