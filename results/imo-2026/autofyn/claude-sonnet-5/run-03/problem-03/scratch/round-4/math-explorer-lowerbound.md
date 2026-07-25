## imo-2026-03 (lens: lower-bound gap — T(m) m≥3, TOP-ONLY outside Dominant-Chain, general Case 2)

### Distinct openings

1. **[NEW, verified] Alternating-sum reformulation — a genuinely different
   potential, not per-fragment peeling.** For any finite multiset of positive
   reals sorted descending `x1≥x2≥…`, `OddSum − EvenSum = AltSum :=
   x1−x2+x3−x4+…`, and since `OddSum+EvenSum = total`, `OddSum =
   (total+AltSum)/2`. Applied to `T(m,k)` (`Γ_m` has total `2^{m+1}−1`,
   target `OddSum≥2^m`): **`T(m,k)` is exactly equivalent to `AltSum ≥ 1`**
   (checked algebraically and by 2000 random-instance identity tests, exact
   match). This is a strictly different top-level target from "OddSum ≥ half
   the total" — it turns the claim into a **monovariant/potential-budget**
   statement: the untouched `Γ_m` has `AltSum(Γ_m) = 2^m(1−(−1/2)^{m+1})·(2/3)
   ≈ (2/3)·2^m`, a large positive slack, and the claim becomes "no allocation
   of ≤m cuts can drive this slack down below 1." This sidesteps Proposition
   C's circularity entirely because it is not an induction on fragment count
   `j` at all — it is a global amortized-budget argument over the whole
   sorted sequence. I did NOT attempt to close this; it is an opening, not a
   proof. Two natural sub-directions to hand to the outliner:
   - **(1a) Per-cut potential-drop bound.** Numerically tested (20,000 random
     trials): splitting a single element `x` of a multiset into two positive
     parts can decrease `AltSum` by **at most `x`** (i.e. `Δ ≥ −x`, checked,
     zero violations), and this bound is close to tight when `x` strictly
     dominates its neighbors and the split fragments both fall below the next
     element (a rank "demotion" event — exactly the mechanism behind
     Proposition C's circularity: splitting the dominant top fragment into
     pieces that no longer dominate the tail can cost close to the full value
     of the split piece). The *naive* per-cut bound `Δ≥−x` is far too weak on
     its own (summed over `m` cuts it can exceed the whole `(2/3)2^m` slack),
     so a real proof needs a **sharper, structure-aware per-cut bound** (e.g.
     tied to the local gap to the neighboring rank, not the raw piece value) —
     this is the concrete open sub-problem this framing produces, distinct in
     kind from Proposition C's obstruction.
   - **(1b) Superadditivity of EvenSum (certified, currently unused for the
     lower bound).** `lemmas/perfect-pairing-subadditivity-and-general-
     insertion.md`'s Lemma S (`OddSum(A∪B)≤OddSum(A)+OddSum(B)`) has an
     immediate dual, **`EvenSum(A∪B) ≥ EvenSum(A)+EvenSum(B)`** (derived
     algebraically from Lemma S plus `Odd+Even=sum`; independently
     re-verified numerically, 20,000 trials, zero violations). This is
     exactly a "positive" (not abstract-dual-lemma) tool of the shape
     Proposition C's `U(m,k)` needs (`EvenSum(B'∪S) ≥ sum(B')`), but alone it
     is insufficient (confirmed algebraically: `EvenSum(B')+EvenSum(S)` can
     be far below `sum(B')` when `B'` is small in cardinality, e.g. one
     element gives `EvenSum(B')=0`) — this is a *second, independent*
     confirmation of Proposition C's circularity from a different angle
     (superadditivity alone can't close the gap, matching the "peeling alone
     can't reduce problem size" finding), not a new dead end to avoid
     re-deriving, but worth recording so nobody re-tries "just use
     subadditivity/superadditivity directly" as a shortcut.

2. **Case 2 general is NOT structurally separate from TOP-ONLY j≥2 — same
   wall, not a harder one.** Checked precisely: `self-similar-induction-on-n`'s
   `T(m,k)` induction already allows `S` to be *any* actual refinement of
   `Γ_{m-1}` (i.e. `c>0` tail cuts, not just `c=0`), so it already IS "the
   fully general Case 2" in the sense the dispatch describes — Proposition C's
   circularity was derived for general `c` (the tail `S` enters only through
   `T(m-1)`'s hypothesis `OddSum(S)≥2^{m-1}`, with no assumption `c=0`).
   Meanwhile `T(2)`'s hand-closed `j=2` case is exactly `c=0` (tail forced
   untouched by the budget). So the evidence points the other way from what
   one might guess: **`c=0` (pure top-splitting, TOP-ONLY) is not easier in
   kind** — it already required a full order-statistics case analysis by hand
   at `m=2`, and the obstruction (rank demotion when the dominant fragment
   splits into non-dominant pieces) is present regardless of whether the tail
   is refined further. Recommend the outliner treat `T(m)` general and
   TOP-ONLY-outside-Dominant-Chain as **the same open problem**, not two
   separate sub-goals — closing the `j≥2` mechanism (however it's done) should
   close both at once, and effort should not be split trying to solve "Case 2
   with `c>0`" as if it were a harder superset requiring separate technique.

3. **A genuinely different induction variable: induct on total fragment count
   of the WHOLE multiset (not on `m`, and not by peeling the max).** Instead
   of `T(m,k)` (fixed target `2^m`, growing tail via `m`), consider inducting
   on `N` := total number of pieces in the final multiset (`N ≤ 2n+1` since
   each of the ≤n cuts adds exactly one piece), using a *global* strong
   induction hypothesis about `AltSum` for smaller `N` — a "remove the
   smallest pair of adjacent ranks and show the invariant transfers" argument,
   rather than "remove the largest element and recurse on `m`." This is
   speculative (not tested this round beyond the identity/per-cut checks
   above) but is a genuinely different induction skeleton from every approach
   in the population so far (all four current approaches induct on `m`
   / geometric level, none inducts on raw fragment count with a merge-based
   IH). Flagging as a route to scout further, not attempted here.

### Candidate technique(s)
- Potential/monovariant argument on `AltSum` (KB: "Invariants & monovariants,"
  `knowledge_base.md` Combinatorics section) — genuinely different in kind
  from the certified Peeling Lemma / single-max-removal induction used by
  all four current approaches.
- Amortized/charging argument bounding total potential loss over ≤`m` cuts
  (classical monovariant-budget technique) — the natural next step for
  opening 1a.
- Superadditivity-family lemmas (Lemma S and its EvenSum dual) as reusable
  building blocks, not as a standalone closer (see 1b).

### Cheap-kill candidates
- None obvious beyond the numeric checks already run (identity + per-cut
  bound verified). No new pruning found this round beyond confirming the
  `Δ≥−x` per-split bound and the EvenSum-superadditivity dual are both true
  but individually insufficient — worth recording so neither is re-derived
  from scratch as if it might be the missing piece.

### Knowledge-base entries to use
- `knowledge_base.md` "Combinatorics" → **Invariants & monovariants** (the
  AltSum reframing is exactly this).
- `knowledge_base.md` "Problem-Solving Heuristics (Pólya)" → **Reformulate**
  (translate `OddSum≥half` into `AltSum≥1`) and **Generalize / strengthen the
  hypothesis** (the outliner may want to track a stronger per-level
  invariant, as the `G(m,k;V)` family in `self-similar-induction-on-n`
  already gestures at).

### Analogous past problems (cruxes)
Searched the corpus (`domain=combinatorics`, subtopics `games-and-strategy`,
`invariants-and-monovariants`, plus free-text scan for stick/cut/alternating-
claim/sorted-descending/pairing motifs). No problem in the corpus matches
this game's precise shape (alternating claim from a cut-generated multiset,
adversarial cutting phase before the claiming phase). The closest general
*technique* match is `aimo-0560` (gardener/lumberjack majestic-tree game,
`games-and-strategy`): its crux is a **surrogate-adversary** move ("replace
the adversary with a strictly stronger surrogate whose reply is pointwise at
least as damaging, so a win against the surrogate transfers down"). This is
the *mirror image* of what round 2/3 already tried and killed here (replacing
LB with a weaker, easier-to-analyze *static* strategy — Q-priority,
tail-priority — both refuted by exact game-tree counterexample). A surrogate
on **XY's side** (strengthen XY to a canonical worst-case response family and
prove *that* family is truly extremal, rather than restricting LB) is a
different direction not yet tried in this form, but I found no strong enough
structural match in the corpus to call this a genuine crux transfer — flagging
as a weak lead, not a confirmed analogy. No other corpus entry is a close
enough match; report "none genuinely analogous" beyond this weak surrogate-
adversary parallel.

### Prior progress
- `T(m,k)` closed for `m≤2` (all `j,c`); Dominant-Chain regime of TOP-ONLY
  closed for all `n`; Proposition C proves (not just diagnoses) that the
  natural single-peel completion of Case A (`b1≥2^{m-1}`) reduces to an
  equally-hard (one-more-fragment) instance, cross-confirmed independently by
  two approaches. See `results/imo-2026-03/current.md` and
  `approaches/self-similar-induction-on-n.md` /
  `approaches/greedy-reduction-geometric.md` for full detail — already
  summarized accurately in `run_state.md`.

### Dead ends (do not retry)
- Static Q-priority LB strategy (round 2) and static tail-priority LB
  strategy (round 3): both refuted by exact game-tree computation
  (floor `7/15 < 8/15` at `n=3`, and floor `7<8` at `n=3` respectively).
- Literal single-step Cut-Reallocation Exchange Lemma (round 3): refuted by
  exact counterexample.
- Lemma X′ (round 2's diagnosed abstract dual EvenSum-lower-bound statement,
  round 3 disproof by two independent explorers): false in general, do not
  resurrect under a new name.
- (New this round, confirmed not a shortcut, but not literally "dead" — a
  documented insufficiency) Naive per-cut `AltSum` bound `Δ≥−x` and the
  EvenSum-superadditivity dual (`EvenSum(A∪B)≥EvenSum(A)+EvenSum(B)`): both
  true (verified) but **individually too weak** to close `T(m)` — do not
  hand either to a builder as "the missing lemma" without first finding the
  sharper per-cut/structural strengthening described in opening 1a.

### Small-case / intuition notes (conjecture, not proof)
- The worst-case mechanism for `AltSum` loss, observed numerically across
  thousands of random splits, is always a **rank-demotion event**: a
  dominant element split into fragments that fall below the current
  second-largest element loses close to its *full* value in `AltSum`,
  whereas splitting an element that stays dominant after splitting (or
  splitting a non-dominant element) loses much less. This is consistent
  with — and gives a cleaner numeric lens on — exactly the mechanism
  Proposition C already isolates algebraically (Case A's circularity is
  precisely about what happens when the top fragment does or doesn't stay
  dominant after the split). Suggests any successful proof of `T(m)` for
  `m≥3`, in whichever framing, will have to make "how much of the potential
  a demotion event can destroy, as a function of how far the fragments fall
  below the current tail," precise and boundable in terms of the number of
  cuts left in the budget — not just the raw value of the split piece.
