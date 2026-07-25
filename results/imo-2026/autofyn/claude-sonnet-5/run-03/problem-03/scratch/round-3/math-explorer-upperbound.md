## imo-2026-03 (lens: the two open upper-bound regimes for `universal-halving-adversary`)

### Setup used for numerics
Confirmed from `lemmas/reduction-to-multiset-minimax.md`: XY's budget is the **full** `n`
cuts, *independent* of how many pieces `k` LB used (not `n-(k-1)`). I built an exact
numerical XY-best-response solver (Python, `scipy.optimize.differential_evolution` over
every "shape" — a composition of the budget among the `k` pieces — with the true
`OddSum` objective) and cross-checked all headline numbers with hand fractions.

### Central new finding: the "Perfect-Pairing" principle unifies almost everything found
**Fact (easy corollary of the already-certified Doubling-Lemma "Claim" / Tie-Neutrality
Lemma A — not new machinery, just a new *use* of it):** if XY's response makes the final
multiset have **every distinct value occurring an even number of times** ("perfectly
paired"), then `OddSum = (total sum)/2 = 1/2` exactly — the absolute floor from
First-mover-half (Lemma B). This is because each maximal same-value block has even
length, and the Claim inside Theorem 1's proof (already certified) shows any even-length
block splits exactly half-half to each player *regardless of where it starts* — so ties
of the whole multiset, not just self-duplicated `R`, contribute exactly half.

This single fact explains **every** numerically-optimal split I found in both open
regimes:
- Bisecting *every* piece pairs each piece with itself → perfectly paired → `1/2`.
- "Duplicate-the-rest" (Theorem 2) is the case of pairing `p_1`'s fragments against
  `p_2,\dots,p_k` themselves, with one deliberately unpaired leftover `\ell`.
- The best split found for `[0.6,0.35,0.05]`, `n=2` — bisect `p_1` **and** bisect `p_2`,
  leave `p_3` alone — is *not* perfectly paired (`p_3` is a lone odd-multiplicity
  singleton) but comes very close, and is exactly matched by an *alternative* optimal
  split that instead pairs a `p_1`-fragment against `p_2` itself and self-pairs the
  remainder of `p_1` — both give `0.525`.

### Cheap-kill / clean sub-case closed this round (new, not previously reported)
**"Bisect-everything closes the slack-budget case completely.`** If `k<n+1` (LB did not
use its full allotment), XY can pick `k\le n` of the budget's cuts to bisect *every*
piece once, using only `k\le n` cuts (well within budget). This perfectly pairs the whole
multiset and forces `OddSum=1/2\le c(n)` **for every `n` and every such partition, no
matter what `p_1` is** (numerically confirmed at `n=2,k=1,2`; `n=3,k=1,2,3`, exact
matches to `1/2`). Since Tie-Neutrality (Lemma A) and the Doubling-Lemma Claim are already
certified black boxes, this is essentially **a free, already-provable full closure of the
case `k\le n`** — meaning the entire remaining open upper-bound problem (both flagged
regimes) can be restricted to **`k=n+1` exactly** (LB using its full budget), which is
also the case the geometric extremal example lives in. This narrows the outliner's job
considerably: no case analysis on `p_1` is even needed when `k<n+1`.

### Regime (a): `p_1>c(n)`, `k=n+1` (tight budget) — candidate strategy found, not proved general
Numeric evidence (`n=2`: several instances; `n=3,k=4`: two instances) shows the winning
move is **not** a fixed rule on `p_1` alone but a **recursive "bisect-or-match" process**
run down the sorted list of pieces:
- At `n=2`, `(0.6,0.35,0.05)`: optimal `0.525` (vs. Theorem-2's useless `0.6`), achieved by
  *either* (i) bisect `p_1` then bisect `p_2` (leave `p_3`), *or* (ii) bisect `p_1` alone
  into 3 fragments, one of which exactly matches `p_2` (Theorem-2-style pairing against
  `p_2` only, not all of `R`), leaving the rest of `p_1`'s mass self-paired. Both give the
  *same* value `p_1/2+p_2/2+p_3` here.
- At `n=3,k=4`, `(0.55,0.25,0.15,0.05)`: optimal `0.525 = p_1/2+p_2/2+p_3/2+p_4`
  (bisect the three largest pieces, leave the smallest) — matches the "bisect all-but-
  smallest" heuristic exactly.
- At `n=3,k=4`, `(0.6,0.2,0.15,0.05)` (here `p_1\ge p_2+p_3+p_4`, Theorem 2's hypothesis
  applies but only gives `0.6`): optimal is **`0.5`, the absolute floor** — achieved by
  bisecting `p_1` (1 cut) and using the remaining 2 cuts to split `p_2` so its fragments
  exactly match `p_3` and `p_4` (perfect pairing of the whole multiset). This is `p_1`
  self-paired + `(p_2,p_3,p_4)` perfectly paired via Theorem-2 applied one level down
  (to `p_2` vs. `\{p_3,p_4\}`, since here `p_2=p_3+p_4` exactly).

**Pattern (conjectural, not proved):** XY's optimal move is *self-similar* — process the
sorted list `p_1,\dots,p_k` from the top; at each step, treat the current largest
still-unresolved piece as a fresh instance of the *same* upper-bound problem relative to
the remaining tail, with the leftover cut-budget, choosing between "bisect this piece
alone" (cost 1 cut, value → half) and "match it against (some of) the tail" (Theorem-2
style, cost = pieces matched, value → tail-sum + leftover). This is consistent with, and
would explain, why `self-similar-induction-on-n`'s recursive/peeling framing is the right
shape for the *upper* bound too, not just the lower bound. I did **not** find or verify a
closed-form recursive formula — only exhibited it working correctly on 4 hand-checked
instances via exact numeric optimization. No counterexample to "some pairing/bisecting
recursive strategy always reaches `c(n)`" was found in regime (a).

### Regime (b): `p_1<1/2` — no counterexample found; the `p_1<1/2` label is a red herring for the *near-equal* worst case
Tested `n=2,3` with several near-boundary and near-equal partitions. All comfortably beat
`c(n)` (e.g. `(0.4,0.35,0.25)`→`0.525<4/7`; `(0.38,0.33,0.29)`→`0.52`;
`(0.28,0.26,0.24,0.22)`→`0.5` exactly). **Important negative result:** the naive
"bisect all pieces except the smallest" heuristic, which works well when one piece is
dominant, **fails badly** for *nearly-equal* partitions (e.g. `(0.336,0.333,0.331)` at
`n=2`: this heuristic gives `0.665`, way above `c(2)=0.571`, because the untouched
"smallest" piece — barely smaller than the others — becomes the *new* largest element
after the others are halved). The **true optimum** for near-equal/exactly-equal
partitions is instead achieved by bisecting **only one piece** (any one, e.g. the
smallest), which already gives the perfectly-paired floor `1/2` exactly (verified exactly
for `(1/3,1/3,1/3)`, `n=2`, and numerically for the near-equal perturbation). So the
right dividing line for "which piece(s) to touch" is *not* simply `p_1` vs. `1/2`; it
depends on the shape of the whole partition. No genuine counterexample to
`c(n)` was found in this regime across all trials.

### Cheap-kill candidates
- **Bisect-everything ⇒ 1/2 floor, whenever `k\le n`.** Free, already provable from
  certified lemmas (Lemma A / Doubling-Lemma Claim) — closes the entire `k<n+1` case for
  *every* `p_1`, before any case split on `p_1` is needed. Recommend the outliner state
  this explicitly as a lemma (`Perfect-Pairing / Bisect-Everything Corollary`) and restrict
  all remaining upper-bound work to `k=n+1`.
- **Perfect-pairing test**: for any candidate XY response, check whether every value in
  the resulting multiset has even multiplicity — if so, the value is `1/2` immediately, no
  further computation needed. This is a fast necessary/sufficient-for-optimality-when-
  achievable check that both explains and predicts every winning example found above.

### Candidate technique(s) for the outliner
- Formalize the **self-similar recursive bisect-or-match algorithm** sketched above for
  `k=n+1`: at each level, decide between self-bisecting the current top piece (via the
  Doubling Lemma degenerate case `R=\{p_i/2\}`) and Theorem-2-style matching against part
  of the tail, then recurse on the residual with the leftover budget. This is the natural
  generalization of both `duplicate-the-rest` (all-matching) and `bisect-everything`
  (all-self-bisecting) as the two extremes of one family.
- Alternatively, since **Perfect-Pairing ⇒ 1/2 ≤ c(n)** whenever achievable, and the
  tight-budget case (`k=n+1`) is *always exactly one cut short* of the naive
  "bisect-everything" pairing (needs `k` cuts, has `n=k-1`), the crux is precisely
  characterizing how to spend the budget to get as close to perfectly-paired as possible
  — i.e., minimizing the single unavoidable "odd one out" leftover's contribution. This
  reframes both open regimes as **one unified question**: "minimize the odd-leftover's
  rank-weighted contribution," which might unify what are currently treated as two
  separate regimes.

### Knowledge-base entries to use
- `knowledge_base.md` "Invariants & monovariants" and "Pigeonhole/extremal principle"
  (Combinatorics section) — generic backing for the parity/pairing argument.
- Certified lemmas already in the repo (not `knowledge_base.md` per se, but the reusable
  proved facts): `lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`
  (Doubling Lemma's even-length-block Claim is the engine behind Perfect-Pairing),
  `lemmas/tie-neutrality-and-first-mover-half.md` (Lemma A: Tie-neutrality; Lemma B:
  First-mover-half = the `1/2` floor being matched).

### Analogous past problems (cruxes)
Filtered `combinatorics` domain, `games-and-strategy` subtopic (40 cruxes).
- **`aimo-0596`** (card deck, alternating pick, parity-of-digit-occurrence win condition):
  crux move "in a pairing/misère take-turns game, have the responder answer each opponent
  pick with its fixed involution-partner, and seed the responder with one floating unpaired
  card, handing it off (taking a fresh card as new floating partner) when the pairing
  breaks." **This is structurally the closest analog found**: it is exactly the "everything
  paired except one floating/leftover element" situation that Theorem 2's `\ell` and my
  Perfect-Pairing analysis both hinge on — the crux move there is a strategy for managing
  exactly one unpaired element under budget constraints, which is the same shape as our
  "one cut short of perfect pairing" obstruction. Worth reading in full for the outliner
  (the handling of the floating element, not the specific game mechanics, is the reusable
  idea).
- **`aimo-0117`** (Jesse/Tjeerd stone game, dyadic/geometric value assignment so the
  largest value strictly exceeds the sum of the rest): analogous to LB's *own* extremal
  geometric construction (`p_i=2^i/(2^{n+1}-1)`) rather than to XY's response, but
  confirms "geometric/dyadic domination" is a recognized recurring extremal shape in this
  corpus — supports (does not newly prove) the standing conjecture that LB's optimal
  partition is the geometric one.
- Others in the sample (`aimo-0115`, `aimo-0854`, `aimo-0663`) are generic
  domino/board-pairing strategies for *different* game mechanics (occupation games, not
  alternating-claim-on-a-multiset) — same "pairing strategy" flavor but not close enough
  structurally to adapt directly; not recommended beyond the general idea already used.

### Prior progress
See `results/imo-2026-03/current.md` / `approaches/universal-halving-adversary.md`: regime
`p_1\in[1/2,c(n)]` fully closed (Theorem 2). Both open regimes (`p_1>c(n)`, `p_1<1/2`)
previously had only single worked examples with no general rule. This round's numerics
strictly extend that: (1) proves (modulo write-up) that `k<n+1` is *entirely* free via
Perfect-Pairing/Bisect-Everything, regardless of `p_1` — reducing the real open problem to
`k=n+1` only; (2) finds a consistent recursive bisect-or-match pattern across 4+ instances
in regime (a); (3) shows the `p_1<1/2` boundary is not the right invariant — the real
danger zone is *near-equal* partitions, where naive heuristics (bisect-all-but-smallest)
badly fail but the true optimum (bisect any single piece) is easy and exact.

### Dead ends (do not retry)
- **"Bisect all-but-the-smallest-piece" as a universal rule**: numerically REFUTED for
  near-equal partitions (`n=2`, `p\approx(0.336,0.333,0.331)`: gives `0.665\gg c(2)`,
  because the untouched smallest piece becomes the new dominant element). Works fine when
  `p_1` is genuinely dominant but is not a safe universal rule — do not propose it as-is.
- Confirms (re-derived independently, not just trusted) the existing doc's claim that a
  *single* cut confined to `p_1` alone cannot beat `p_1` in the `(0.6,0.35,0.05)` example
  — but a **second** cut confined to `p_1` alone (splitting it into 3 pieces, matching one
  fragment to `p_2`) *does* reach the optimum without ever touching `p_2` — so "no
  single-piece response suffices" (as stated in the current doc) is true only for
  budget-1 responses on `p_1`; with the piece's full local budget it is not accurate, and
  the doc's framing "requires splitting two pieces" is one valid witness but not the only
  one — the outliner should not treat "must cut `p_2` too" as an established necessary
  condition.

### Small-case / intuition notes (all labeled conjecture)
- Conjecture: for `k<n+1`, `OddSum\le 1/2` is always achievable, hence this whole
  sub-case is dominated by (and much easier than) `k=n+1` — believe this is provable
  outright from already-certified lemmas with no new machinery, essentially for free.
- Conjecture: the real difficulty of the whole upper-bound problem is confined to
  `k=n+1`, and within it, to how XY should spend its budget "one cut short of a perfect
  pairing" — i.e. which single element to leave unpaired (or how large to let a matched
  leftover `\ell` be) to minimize its rank-weighted contribution. This suggests a possible
  unification of the lower-bound approach (`self-similar-induction-on-n`'s peeling) and
  the upper-bound approach into one shared recursive/self-similar machine, both keyed on
  `k=n+1`.
- No counterexample to the conjectured closed form `c(n)=2^n/(2^{n+1}-1)` was found in any
  regime or any of the ~10 hand-verified instances plus the broader randomized sweeps.
