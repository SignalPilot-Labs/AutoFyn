## imo-2026-03 — lens: Branch-I.A-restricted window (self-similar-induction-on-n)

### Precise statement of the window

Inside `self-similar-induction-on-n`'s `L_0^{gen}(ℓ,ε)` machinery (ℓ≥1,
ε∈(0,1); `L_0(ℓ,ε)`: for `C` with ≤ℓ+1 parts, sum(C)=2^ℓ+ε, claim
`OddSum(C∪Γ_{ℓ-1})≥2^ℓ`), round 7–8 closed everything except one region.
Writing `c_1:=max(C)`, the **Branch-I.A-restricted window** is exactly

```
c_1 ∈ [2^(ℓ-1), 2^(ℓ-1)+1-ε)   AND   max(C\{c_1}) < 2^(ℓ-1)  (i.e. C has
                                       no second element ≥ 2^(ℓ-1))
```

(piece cap ≤ℓ+1 on C still applies). Round 8 proved (Branch II peel
identity + Step 2 ε′-range argument + strong induction on ℓ, base case
ℓ=1 vacuous) that this window is the *unique* possible non-terminating
landing point of the recursion that unifies the whole tail-untouched
sliver: **Branch II** (the complementary `c_1<2^{ℓ-1}` open range from
round 6/7) is logically **equivalent** to `L_0(ℓ-1,ε')` for a
derived `ε'∈(ε,1)` strictly interior — so recursing on `ℓ` either lands in
this window, or in the already-closed Branch I.B (two large elements,
Two-Peel Theorem) or Branch I.A's main range (cap-free, closed round 8).
An explicit witness (`ℓ=3,ε=1/2`) confirms the recursion genuinely
*reaches* the window at a lower level for some instances — it is not
vacuously avoided. **The window is genuinely open**: no proof attempt has
closed it yet (round 7's order-statistics/two-peel transplant attempt
failed — the needed direction is an *upper* bound on `OddSum(R∪T'')`
after peeling, and discarding a nonnegative remainder only gives a
*lower* bound, the wrong direction; this negative finding is correct and
should not be retried in the same form).

### New this round: numeric/symbolic pin-down of the exact extremal margin

I ran targeted local optimization (hill-climbing + random restarts, exact
construction checks in Python) directly on the window's own free
parameters (`c_1` inside the window, and the composition of
`C\{c_1}` subject to `max<2^{ℓ-1}` and the piece cap) for `ℓ=3,4,5,6` and
several `ε`. Findings, **conjectured, not proved**:

1. **The minimum of `OddSum(C∪Γ_{ℓ-1})-2^ℓ` over the whole window is
   exactly `ε/2`, uniformly in `ℓ`**, attained exactly at the window's own
   left endpoint `c_1=2^(ℓ-1)` (which the window definition includes).
   Local search converges to `ε/2` to 3+ significant figures at every
   tested `(ℓ,ε)` pair and does not find anything below it after
   thousands of restarts/iterations at a fixed `c_1=2^(ℓ-1)`.

2. **Exact closed-form witness achieving this margin** (verified
   symbolically with exact fractions, not just numerically): take
   `c_1=2^(ℓ-1)` and
   ```
   C = {2^(ℓ-1)} ∪ (Γ_{ℓ-2} with its minimum element "1" replaced by
        TWO copies of r := (1+ε)/2).
   ```
   This uses exactly `ℓ+1` parts (Γ_{ℓ-2} has `ℓ-1` elements; replacing
   one by two gives `ℓ` elements for `C\{c_1}`, plus `c_1` itself = `ℓ+1`
   — exactly saturates the piece cap). Direct computation (checked for
   `ℓ=3,4,5,6` by hand/sympy): the merged sorted sequence puts `Γ_{ℓ-1}`'s
   own values and `C`'s values in exact lockstep pairs at every level
   above the bottom, so
   `OddSum(C∪Γ_{ℓ-1}) = 2^ℓ + ε/2` **exactly**. This is a genuine
   generalization/instance of the certified **Doubling Lemma**
   (`OddSum(R∪R)=sum(R)`, `lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`)
   applied at the bottom rank only (since the piece budget forbids
   duplicating the whole tail, only the last element can be split into a
   tied pair) — i.e. the extremal shape is a **budget-starved partial
   duplicate-the-rest construction**.

3. As `c_1` moves away from `2^(ℓ-1)` toward the window's other end
   `2^(ℓ-1)+1-ε`, the margin (using the same duplicate-the-min-element
   family) **increases monotonically** (checked exactly:
   `margin(c_1) = ε/2 + (fraction of the way through the window)·(1-ε)/2`
   roughly, matching the numeric sweep at `frac=0,1/4,1/2,3/4`), so the
   left endpoint is the binding case, consistent with local search never
   finding a smaller value anywhere else in the window.

4. This `ε/2` value **exactly matches round 6's independently-derived
   Two-Level-Half-Bound-refuted conjecture for the outer Case-B(m,k)
   sliver margin** (memory rule #9: "the exact minimum margin is `eps/2`
   ... matching `(V-2^(m-1))/2`"), and matches round 5's Extremal
   Boundary Identity (`B*={2^{m-1}}∪(Γ_{m-2}` with `1`→`2`)`, exact
   equality `2^m-1`) — that identity is the `ε→1` degenerate case of
   exactly this same duplicate-the-min-element family. **This is strong
   corroborating evidence the window's extremal value is genuinely
   `2^ℓ+ε/2`, self-similarly at every recursion level**, not a numeric
   coincidence at one level — it is the *same* extremal mechanism
   recurring, which is exactly what you'd expect given the window
   recurs self-similarly.

**This is a concrete, closed-form target for the outliner to hand to a
builder**: prove `OddSum(C∪Γ_{ℓ-1}) ≥ 2^ℓ+ε/2` (or at least `≥2^ℓ`,
weaker) for every admissible `C` in the window, with equality exactly at
the identified extremal family. Since `ε/2>0` always, this closes the
window (and hence, via round 8's proved equivalence, all of Branch II)
unconditionally.

### Candidate proof mechanism: exchange-smoothing (crux match)

Filtered the corpus (`domain=combinatorics`, subtopics `extremal-principle`,
`invariants-and-monovariants`, `games-and-strategy`) for exchange/smoothing
techniques on sorted-sequence weighted sums. **`aimo-0146`** (2017
mathematicians/graph-degree problem, USAMO-flavor) is a strong structural
analogue: its algebraic lemma bounds a **fixed-weight sum of a sorted
sequence under a sum constraint** (`x_2+2x_3+...+63x_64+x_65 ≤ 4034`,
`x` sorted descending) via **exchange-smoothing** — "if `x_i>x_{i+1}` and
`x_{j-1}>x_j` for `i<j`, replacing `(x_i,x_j)` by `(x_i-1,x_j+1)` strictly
changes the objective toward the extremum" — pushing all free coordinates
to equalize except a controlled tail, reducing an infinite-dimensional
optimization to **finitely many candidate profiles to check by hand**.
This is structurally the *same shape* of problem as the window: `OddSum`
is a fixed-weight (`1,0,1,0,...`) sum of a sorted sequence (the merge of
`C` and `Γ_{ℓ-1}`) under a sum constraint (`sum(C)` fixed) and a
piece-count budget — exactly the genre `aimo-0146`'s technique targets.
The already-certified **Single-Insertion Lemma**
(`self-similar-induction-on-n`, gives the exact `ΔAltSum` when one value
is inserted at an arbitrary sorted position) is the ready-made tool for
running this exact exchange argument on `AltSum` (equivalently `OddSum`
via Lemma AS) directly: it tells you precisely how moving mass between
two of `C`'s free parts changes the objective, which is what an
exchange-smoothing proof needs step by step. **This is a genuinely new
mechanism not yet tried on this window** (rounds 6–8 tried peel+scalar-
bound and order-statistics/two-peel; exchange-smoothing toward an
explicit finite extremal family is different in kind — it directly
targets minimizing over the *whole* window at once rather than casework
by sub-threshold).

No other corpus entry in the filtered set (aimo-0003 adjacent-transposition
generation, aimo-0439/aimo-0596 pairing games, aimo-0261/aimo-0438 local
exchange for extremal partitions) was as close a structural match; they
are genre-adjacent (extremal/exchange) but not on a fixed-weight
sorted-sum-under-budget target. Report aimo-0146 as the best (single)
analogue, not a family.

### Cross-pollination check: greedy-reduction-geometric's Level-Absorption

Checked whether the window is secretly the same object as
`greedy-reduction-geometric`'s open Level-Absorption (Subcase (b) of
Theorem 7'). Level-Absorption's target (per `current.md`/round 7-8) is
about the **interleaved joint Case 2** (top piece split AND tail cut
simultaneously, general `m`, not tail-untouched) with a leftover-mass
parameter `L`, whereas the window here is specifically the **tail-
untouched** regime (`S=Γ_{ℓ-1}` exactly, no cuts on the tail at all) at a
*nested* recursion level. They share the same underlying peeling/Lemma-B
machinery and the same `eps/2`-type margin flavor (per round 6's
cross-substitution finding, memory rule #32, that `Case-B(m,k)`'s
reduction target is algebraically identical to `greedy-reduction-
geometric`'s own `d=1` residual bound) — but Level-Absorption itself is a
**different, more general** open sub-problem (tail is *also* being cut),
not literally the same statement as this window. They are related
(same family of tools, same `eps/2` margin shape) but **not equivalent**
as stated — closing one does not automatically close the other, though a
proof mechanism (exchange-smoothing per above) that works on the window
is a good candidate to try on Level-Absorption next, given the shared
flavor.

### Cheap-kill / sanity checks before a full proof attempt

- Verify the window is genuinely non-vacuous at every `ℓ` (already done,
  round 8's `ℓ=3` witness) — no cheap parity/pigeonhole kill exists; the
  window is a real, populated region, not a degenerate edge case.
- Before building a general proof, re-verify the `ε/2` conjecture at
  `ℓ=7,8` (this round's search only went to `ℓ=6`) and check whether the
  minimizing `c_1` is *exactly* the closed endpoint `2^(ℓ-1)` (included in
  the window) or whether the infimum is only approached in the open
  interior — this affects whether the theorem needs `≥` or a limiting
  argument.

## Summary

- **Distinct openings:** (1) a closed-form target `OddSum ≥ 2^ℓ+ε/2` with
  an exact, checkable extremal witness (the budget-starved partial
  duplicate-the-rest construction, an instance of the certified Doubling
  Lemma) — strong numeric+symbolic evidence, not proved; (2) an
  exchange-smoothing proof mechanism (crux `aimo-0146`) using the
  already-certified Single-Insertion Lemma to formalize "any deviation
  from the extremal family can only increase OddSum," genuinely
  untried on this gap; (3) a noted (not equivalence, but shared-tooling)
  relationship to `greedy-reduction-geometric`'s Level-Absorption.
- **Candidate technique(s):** exchange-smoothing / rearrangement on the
  sorted merged multiset via the Single-Insertion Lemma, targeting the
  explicit closed-form margin `ε/2`, rather than another peel+scalar-
  bound or order-statistics attempt (both already tried and diagnosed as
  insufficient/wrong-direction in rounds 6–7).
- **Cheap-kill candidates:** none found beyond re-confirming
  non-vacuousness (already done) — no parity/pigeonhole shortcut; this is
  a genuine extremal-optimization gap.
- **Knowledge-base / certified-lemma entries to use:** Doubling Lemma /
  Generalized Duplicate-the-Rest (`lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`),
  Single-Insertion Lemma (in `self-similar-induction-on-n.md`, not yet a
  standalone certified file but proved and reusable), Peeling
  Lemma/Companion Peeling Lemma, Lemma B (First-mover-half),
  `lemmas/branch-ib-two-peel-theorem.md` (for context on why the
  two-peel mechanism doesn't transplant here — upper- vs lower-bound
  direction mismatch).
- **Analogous past problems (cruxes):** `aimo-0146` — exchange-smoothing
  a fixed-weight sum of a sorted sequence under a sum budget, reducing to
  finitely many candidate extremal profiles; the closest structural match
  found. No strong match in `games-and-strategy` subtopic (those are
  pairing/mirroring board games, not continuous sorted-sum optimization —
  consistent with prior rounds' finding, memory rule #35).
- **Prior progress:** Branch II ⟺ window equivalence (round 8, proved);
  Branch I.B and Branch I.A's main range fully closed (rounds 7–8); the
  window itself is the sole remaining piece, now with a conjectured exact
  closed form (`ε/2` margin) and candidate extremal witness, both new
  this round.
- **Dead ends (do not retry):** round 7's order-statistics/two-peel
  transplant of the Branch-I.B mechanism to the window's lower half
  (wrong bound direction — peeling only gives lower bounds, the window
  needs an upper-bound-shaped intermediate step); the vestigial
  `max(C)≤2^ℓ-ε` cap (already correctly dropped, not a live issue).
- **Small-case / intuition notes (conjectured, not proved):** the
  window's minimum margin over `OddSum-2^ℓ` is exactly `ε/2`, attained at
  `c_1=2^(ℓ-1)` by the duplicate-the-min-element construction, uniformly
  in `ℓ` (checked `ℓ=3..6` numerically to 3+ sig figs, and exactly by
  symbolic construction) — this uniformity-in-`ℓ` is itself evidence the
  window closure, if provable, will be a single clean lemma (no further
  `ℓ`-dependent casework needed), reinforcing that this is the right
  place to concentrate effort.
