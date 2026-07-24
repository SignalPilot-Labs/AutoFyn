## imo-2026-03 (lens: e_{g*}'s MINIMUM = 1, concavity-minimax-duality's remaining gap)

### Precise target (confirmed from the file)
`g*` is the piecewise 1-Lipschitz certificate (§12.6): for integer `t>=1`, writing `k` with
`2^k<=t<2^{k+1}`, `g*(t)=(k+1)+(t-2^k)` if `t<=2^k+1`, else `g*(t)=k+2`; `g*(0)=0`. The certified
Integer-Preservation Lemma (§13.5) reduces the target `e_{g*}(M)>=1` (for every state `M`
reachable from `D_m` via <=m legal D/M operations, every `m`) to the strict-sign statement
`e_{g*}(M)>0`, since `e_{g*}` is always an integer on reachable states. §13.3 exhaustively
verified (m<=6, not proved) that `min` over size-`k` reachable states of `e_{g*}` equals
`ceil(k/2)` exactly. §13.6 proves single-operation (edge-wise) monovariance of `e_{g*}` is FALSE
(exact drop-of-4 counterexample `(32,8,4)->(8,4)`) — a real dead end for that technique, per the
dispatch, confirmed correct on inspection (verified independently below, see "Dead ends").

### New finding this round: a closed form for g*, and a much stronger structural invariant

**1. Closed form (new, not stated explicitly in the file, algebraically equivalent to the
piecewise definition, verified exactly for t=0..39 by direct comparison):**
```
g*(t) = bit_length(t-1) + 1     for integer t>=1     (g*(0)=0)
```
i.e. `g*(t)-1 = ceil(log2 t)`. This makes `g*`'s "level sets" (buckets) exactly the classical
dyadic doubling intervals: `B_1={1}`, `B_2={2}`, and for `k>=3`, `B_k = (2^{k-2}, 2^{k-1}]` (an
interval of `2^{k-2}` consecutive integers). `g*(2^i)=i+1` (§13.4, already proved) is the special
case where `t` sits at the TOP of its bucket.

**2. Distinct-Bucket Lemma (NEW empirical finding, strongly supported, not yet proved) — the
key structural fact that would close the whole gap.** Computed, for every state `M` reachable
from `D_m`, the multiset of buckets `{g*(v): v in M}` and checked whether any bucket is ever
occupied by 2+ elements simultaneously:
```
m=1..7 (FULL exhaustive BFS, all D/M sequences of every length <=m):
  max # elements of any reachable state sharing a g*-bucket = 1, in EVERY case (0 collisions,
  0 exact value-ties), across 3, 9, 31, 125, 585, 3117, 18537 total distinct reachable states
  respectively (my independent BFS reproduces the file's own m=6 count of 3117 exactly, an
  independent cross-check).
m=8,10,12,15 (80,000 total RANDOM D/M walks, bounded, not exhaustive): 0 bucket-collisions found.
```
In other words: **every element of every reachable state, so far as checked, occupies a
DIFFERENT dyadic doubling-bracket from every other element of that same state** — no two active
values are ever "close" (within a factor of 2, roughly) to each other simultaneously.

**3. Why this would finish the proof (elementary, verified by hand + spot-checked numerically):**
if the Distinct-Bucket Lemma holds, then for any reachable `M`, sorting descending
`v_1>v_2>...>v_k` gives STRICTLY decreasing bucket indices `g*(v_1)>g*(v_2)>...>g*(v_k)` (since
`g*` is nondecreasing in value and constant only within a bucket — distinct buckets + sorted
order forces strict inequality at every consecutive pair, and since buckets are intervals,
"pairwise distinct" and "consecutive distinct" coincide for a sorted list). These are `k`
strictly decreasing POSITIVE INTEGERS (Integer-Preservation), so pairing consecutive terms,
`g*(v_{2i-1})-g*(v_{2i})>=1` for every pair, plus (if `k` odd) an unpaired trailing term
`g*(v_k)>=g*(1)=1` (monotonicity + `v_k>=1`). Summing: `e_{g*}(M) >= ceil(k/2) >= 1` for every
`k>=1` — **this reproduces the exhaustively-checked `ceil(k/2)` floor pattern in §13.3 EXACTLY,
via a 5-line elementary argument, with no per-edge monovariance needed at all.** (I verified this
implication directly: the size-1 row is free — any reachable single-element state `{t}` has
`t>=1` integer, so `g*(t)>=g*(1)=1` by monotonicity alone, no computation needed; the size-2 row
reduces to exactly the Distinct-Bucket claim, since two distinct buckets already forces
`e_{g*}={g*(v1)-g*(v2)}>=1`.)

**Net effect:** the *entire* remaining gap in this approach (`e_{g*}`'s minimum is 1, for every
`m`) reduces, via an elementary and already-verified argument, to proving ONE clean structural
claim: **no two elements of any state reachable from `D_m` (any `m`, any legal <=m-operation
D/M sequence) ever lie in the same dyadic doubling bracket `(2^{j},2^{j+1}]`.** This is a
genuinely different target from both `e_{g*}\ge1` directly (avoids the dead edge-wise-monovariant
route entirely: it is a state-level structural invariant, not a scalar potential that must not
drop too fast) and from the size-class-wide "argue about every possible predecessor" induction
flagged as the next step in §13.7 (this sidesteps that entirely by not inducting on `e_{g*}` at
all, only on bucket-membership).

### Why Distinct-Bucket plausibly holds (a proof *shape*, not attempted here)
`D_m`'s own elements are exactly `2^0,...,2^m`, trivially one per bucket (bucket of `2^i` is
`i+1`). Every reachable value is built from these by a chain of `D`(delete, no-op on remaining
values) and `M`(replace `x,y` by `x-y`) — i.e. every active value is (up to which original
"slots" have already been discarded) a **signed-subtraction combination** of a subset of the
original superincreasing dyadic sequence, structurally the same object the already-certified
**Superincreasing No-Early-Zero Lemma** (`lemmas/superincreasing-no-early-zero.md`) analyzes
(that lemma proves such signed combinations never vanish within budget). The classical
superincreasing/"knapsack" fact that subset (and, plausibly, iterated-difference) combinations of
`2^m,...,2^0` have their magnitude essentially pinned to the doubling-bracket of their
highest-surviving power strongly suggests Distinct-Bucket is provable by a **token/level-tracking
induction in the same family as** that certified lemma — likely by strengthening its invariant
from "never exactly 0" to "the current top surviving power-of-2 level is never shared by two
simultaneously-active tokens." This is a concrete, well-scoped next proof target, NOT a proof
(I did not attempt to close it — this is exploration only, per instructions).

### Cheap-kill / sanity checks done
- Re-verified `g*(t)=bit_length(t-1)+1` matches the file's piecewise definition exactly for
  `t=0..39` (closed form, not previously stated explicitly in the file).
- Re-verified the file's own `m<=6` size-class-floor table (§13.3) independently from scratch,
  and **extended it one level further to `m=7`** (18537 states, still exactly `ceil(k/2)`,
  matches perfectly) — one level beyond the file's own claim, per the "push exhaustive checks one
  level further" house rule.
- Re-verified the file's decisive edge-wise-monovariance counterexample `(32,8,4)->(8,4)` exactly
  (`e_{g*}` drops from `6-4+3=5` to `4-3=1`, a drop of `4`) — confirms the DEAD END is real, not
  an artifact.
- Tested a natural "Kraft-budget" candidate potential `Phi(M) = sum_{v in M} 2^{-(g*(v)-1)}`
  (motivated by crux `aimo-0790`'s weight-splitting mechanism) for edge-wise monotonicity across
  the full BFS graph: **NOT monotone** — mostly decreasing but with real exceptions (`m=2`: 1/18
  edges increase; `m=3`: 5/97; `m=4`: 21/542; `m=5`: 95/3252 — roughly 1.5–3% of edges increase
  the raw Kraft sum). This specific naive potential is a dead end as a direct P2-style
  monovariant; report honestly, do not re-propose unmodified.

### Kraft-budget crux (aimo-0790) — applicability assessed
Read the crux via `past_crux_moves_database.json`/`past_problems_database.json`
(`crux_moves_documentation.md`'s field names). `aimo-0790` (algebra,
`sequences-and-recurrences`/`telescoping-and-summation`) is: given `a(m+n)<=2a(m)+2a(n)` and
`a(2^k)<=1/(k+1)^c`, prove `a(n)` bounded. Its crux move: iterate the 2-term subadditive
inequality into a many-term bound `a(sum n_i) <= sum 2^{s_i} a(n_i)` valid whenever
`sum 2^{-s_i}<=1` (a genuine Kraft-inequality budget constraint on the weights), proved by an
induction that merges the two largest-weight terms; then decompose `n` via its BINARY digits
into geometrically-spaced blocks and apply this. **Structural resemblance to our problem:** both
involve (a) a base sequence of values at DYADIC/power-of-two indices, (b) building up general
values via a binary-digit / doubling-bracket decomposition, (c) a pairwise "merge" process
(their induction literally merges two terms into one — exactly analogous to our `M(x,y)->x-y`
operation collapsing two active tokens into one). **But the goal is a mismatch in direction**:
their target is an UPPER bound on a general value built from many summands; ours is a LOWER
bound (positivity) on an ALTERNATING sum of a doubling-bracket-valued function over a
STRUCTURALLY CONSTRAINED (Distinct-Bucket, if provable) small set. The raw "Lemma
2"/Kraft-weight-merge technique does not transfer as a direct citation — but the general
*shape* ("track which doubling bracket each token occupies, bound behavior via how the process
respects that bracket structure") is a genuine hint toward proving Distinct-Bucket itself (the
`M`-operation is the same kind of "merge two dyadic-scale objects into one" step central to
`aimo-0790`'s induction). **Assessment: a real but indirect match — worth citing as the shape
for a future Distinct-Bucket proof attempt, not a literal transferable lemma.**

### Candidate technique(s)
1. **(Primary, new lead this round) Prove the Distinct-Bucket Lemma** by extending the
   Superincreasing No-Early-Zero Lemma's token/signed-sum machinery from "never exactly 0" to
   "the current highest surviving dyadic level is never occupied by two simultaneous active
   tokens" — likely an induction on operation count tracking, for each level `j=0..m`, whether
   it is "occupied" (an active token currently in `(2^{j-1},2^j]`) or "vacated" (already
   consumed/merged away), analogous to a binary-carry argument. If this closes, the elementary
   pairing argument above (already fully verified, not just sketched) finishes the whole `g*`
   minimum-is-1 target for every `m` in one shot — no case split by `m` needed.
2. **(Fallback, per original dispatch) Kraft-budget reformulation (`aimo-0790`)** — same
   doubling-bracket bookkeeping, different mechanism (weight-merge induction instead of
   token-survival). Worth trying if (1) stalls, since it targets the same Distinct-Bucket-style
   structure from a different angle (a genuine "size-class-wide" argument, per §13.7's own
   flagged need, rather than edge-wise).
3. A **size-class-wide strong induction directly on `e_{g*}`** (§13.7's own flagged next step) is
   now superseded/subsumed by (1): if Distinct-Bucket is proved, no `e_{g*}`-specific induction
   is needed at all — it becomes a corollary of a purely structural (non-numeric) fact.

### Dead ends (confirmed, do not retry)
- Single-operation/edge-wise monovariance of `e_{g*}` — FALSE, exact counterexample
  `(32,8,4)->(8,4)$ (drop of 4). Re-verified exactly this round. Do not build a proof that needs
  "each move drops `e_{g*}` by at most a bounded amount."
- Naive raw Kraft-sum `sum 2^{-(g*(v)-1)}` as a direct edge-wise monovariant — tested this round,
  FALSE (1.5–3% of BFS edges increase it). Do not reuse unmodified; if revisited, it would need a
  size/budget-aware correction term (same lesson as the file's own already-dead `Phi_1,Phi_2`
  potentials for the raw, non-`g*` problem, round 4).

### Knowledge-base entries to use
- KB "Invariants & monovariants" (combinatorics) — general framing, though this round's actual
  lead is a *structural* (set-membership) invariant, not a scalar potential.
- KB entries on superincreasing sequences / subset-sum uniqueness (if present) would directly
  support the Distinct-Bucket proof shape; otherwise cite the already-certified
  `lemmas/superincreasing-no-early-zero.md` as the closest in-repo precedent and adapt its
  token-tracking technique.

### Analogous past problems (cruxes)
- `aimo-0790` (algebra, sequences-and-recurrences / telescoping-and-summation) — Kraft-budget
  weight-merge induction over binary-digit blocks of a dyadic-indexed sequence; genuine
  structural resemblance (dyadic blocks + pairwise merge) but goal-direction mismatch (upper
  bound vs. our lower bound) — a shape hint for proving Distinct-Bucket, not a literal transfer.
  This is the crux explicitly flagged by the dispatch; assessed in detail above.
- No other crux in the corpus was found to be closer; did not do a fresh broad corpus search this
  round (out of scope for a single fixed crux-assessment lens) beyond confirming `aimo-0790`'s
  content and fit.

### Prior progress
See "Precise target" above — everything in §13 up to and including the Integer-Preservation
Lemma, the exact base-case formula, and the (correct, re-verified) edge-wise-monovariance dead
end is solid, certified-adjacent progress. The genuinely new content from this round is: (a) the
closed form `g*(t)=bit_length(t-1)+1`, (b) the Distinct-Bucket empirical finding (0 violations,
`m<=7` exhaustive + 80,000 random trials to `m=15`), (c) the elementary proof that Distinct-Bucket
implies the exact `ceil(k/2)` floor (hence `e_{g*}>=1`) with no further gap, (d) the Kraft-sum
edge-wise-monovariant test (negative), (e) the `aimo-0790` applicability assessment.

### Small-case / intuition notes (all labeled conjecture except where marked PROVED)
- **PROVED (elementary, in this report):** Distinct-Bucket `=>` `e_{g*}(M)>=ceil(|M|/2)>=1` for
  every reachable `M`. This is a real, checked implication, not a numeric observation — reduces
  the entire remaining gap to one clean structural conjecture.
- **CONJECTURE, strongly supported (0/N violations, `N` up to tens of thousands of states/walks,
  `m` up to 15):** the Distinct-Bucket Lemma itself. Not proved. This is the single concrete
  target to hand to the outliner/builder next round.
- The size-1 and size-2 rows of the `ceil(k/2)` floor table are now understood in closed form
  (size-1: trivial from monotonicity; size-2: exactly Distinct-Bucket for `k=2`) — no longer just
  numeric table entries.
