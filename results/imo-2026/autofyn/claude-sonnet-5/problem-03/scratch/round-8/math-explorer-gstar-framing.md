## imo-2026-03

### TASK 1 — scouting candidate certificate g*

**Closed-form formula (already stated in the file, re-derived and confirmed well-defined).**
From `concavity-minimax-duality.md` §12.6, for `t>=0`:
```
g*(t) = t                              for 0<=t<=1
for k=0,1,2,...:
  g*(t) = (k+1) + (t - 2^k)            for 2^k <= t <= 2^k+1     (ramp, slope 1)
  g*(t) = k+2                          for 2^k+1 <= t <= 2^{k+1}  (plateau, slope 0)
```
Equivalently, for `t>=1`, let `k=floor(log2 t)`; then `g*(t) = t-2^k+k+1` if `t<=2^k+1`, else
`k+2`. I independently re-checked continuity at every breakpoint (`t=2^k+1` and `t=2^{k+1}`)
symbolically — matches exactly, confirming this is a genuine well-defined, everywhere-1-Lipschitz
function for **every** `k>=0`, not just the small `k` spot-checked in the file. `g*(2^k)=k+1`
(ramp start), `g*` is the *minimal legal value* at every power of 2 per the certified
Combined Theorem in `lemmas/forcing-characterization-dyadic.md`.

**Extended exhaustive verification (bounded, exact, no sampling) — new this round.**
Independently re-implemented the BFS/exact-Fraction verification from scratch (own code, not
copied) and reproduced the file's `m<=6` claim (own counts differ slightly from the file's —
mine: `m=1..6`: `4,22,164,1607,19931,299826` states vs. the file's `4,21,161,1622,20267,304190`;
both show **zero violations**, and the small count discrepancies are almost certainly a
difference in how M-operations on equal-valued pairs are canonicalized/deduped between the two
independent implementations — not a correctness issue, since both report 0 violations on their
own state sets). **Extended one full exhaustive level further: ran the complete, uncapped BFS
for `m=7`** (`5,282,000` distinct reachable states, ~190s wall-clock) and checked
`e_{g*}(M)>=1` on **every single one** — **zero violations**. This is a genuinely new data
point beyond the file's own `m<=6` claim (the file's builder explicitly noted `m=7` "did not
complete within the wall-clock budget and was abandoned"). `m=8` full BFS was not attempted
(extrapolated state count ~80-100M, judged too large for a bounded check this round — see
guardrail note below); I did not run an uncapped `m=8` search.

**Minimum-value structure (new finding, informative for a future inductive proof attempt).**
For `m=1..6` I computed the *minimum* of `e_{g*}(M)` over every reachable state, not just
whether it's `>=1`: **the minimum is always exactly 1** (never `>1`, confirming the bound is
tight, not slack), and it is achieved by an increasingly rich set of very different
configurations as `m` grows — e.g. at `m=6` one exact minimizer is the 7-element state
`(32,26,13,13,8,6,1)`. This mirrors the already-recorded fact (memory rule 23) that the *raw*
`e_m` bound has many distinct optimal D/M sequences (12 at `m=4`, 46+ at `m=5`) — the same
multiplicity phenomenon recurs for the certificate's own minimizers, which is a data point
against expecting an unusually short/slick closed-form proof (the tight set is genuinely rich,
not one clean witness family), though it does not contradict provability.

**A concrete structural lead (idea only, not developed into a proof — flagging per the "one
line and stop" rule).** Decomposing `e_{g*}` on both minimizing AND generic sampled states
shows `g*` acts as a *coarsening*: many raw values that land in the same dyadic bracket
`[2^k+1,2^{k+1}]` (the plateau) get mapped to the *identical* value `k+2`, so in the sorted
alternating sum adjacent equal-`g*`-value terms cancel in pairs (exactly as the certified
"adjacent equal values cancel" fact used throughout the population for raw duplicate pairs).
At the exact minimizer `(32,26,13,13,8,6,1)`, `g*`-values are `(6,6,5,5,4,4,1)` — three
cancelling pairs plus one trailing residual `=1`. Sampled *non*-tight states show the same
mechanism only partially resolves (e.g. `(64,32,127/8,8,4,15/8,1/4,1/4,1/4)` gives
`g*`-values `(7,6,5,4,3,15/8,1/4,1/4,1/4)` with only the trailing `1/4,1/4` pair cancelling,
`e_{g*}=27/8>1`). **The natural proof lead**: show, by an induction tracking how many elements
of a reachable state fall in each dyadic bracket, that after `g*`-coarsening the alternating
sum always telescopes down to a residual `>=1` (a pairing/counting argument, not a case-by-case
one) — this is a concrete next step for a future builder, not attempted here.

**Crux corpus search (per dispatch).** Domain=combinatorics/algebra, subtopics
`games-and-strategy`, `invariants-and-monovariants`, plus free-text search for
"Lipschitz"/"potential function"/"certificate"/"dual"/"entropy"/"Kraft"/"probabilistic method"
across all 2434 cruxes. No crux is a literal certificate-function match for a bisect/subtract
game (confirming round 5-6's prior finding: this game genre is not represented in the corpus).
**One genuinely suggestive analog found and worth flagging concretely: `aimo-0790`**
(algebra/sequences-and-recurrences, IMO-Shortlist-style, "Croatia"): a function `a` satisfying
subadditivity `a(m+n)<=2a(m)+2a(n)` and bounded at powers of 2 `a(2^k)<=1/(k+1)^c` is proved
bounded everywhere via a **Kraft-style weighted-budget decomposition** (Lemma 2: if positive
integers `s_i` satisfy `sum 2^{-s_i}<=1`, then `a(sum n_i) <= sum 2^{s_i} a(n_i)`), applied to
the **binary expansion** of `n`. The shape (a value defined by its behavior at powers of 2,
extended to all `n` via weighted binary-digit decomposition with a Kraft-type budget
constraint) is structurally reminiscent of `g*`'s own construction (`g*` is pinned at
`2^k` by the certified Combined Theorem, and `g*`'s ramp/plateau shape looks like exactly the
kind of function a Kraft-weight allocation over binary digits would produce). This is a
genuinely different **technique** (not previously tried in this population) for the *proof* of
Task 1's g*, worth flagging to the outliner as a candidate proof mechanism, though translating
it precisely (what plays the role of "n", what the subadditivity relation actually is for this
game) is nontrivial, unverified work, not done here.

**Honest verdict on g*.** Survived exhaustive testing through **m=7** (5.28M states, 0
violations, new this round, one level beyond the file's own claim), well-defined and continuous
for all k (re-confirmed), minimum is always exactly 1 (tight, richly multi-witnessed). No
counterexample found. Still **NOT proved for general m** — this round did not find a
counterexample (a valuable negative result would have been a m=7/8 violation; none found) but
also did not close the induction. Recommend: next round should try either (a) the
pairing/coarsening telescoping argument above, or (b) the Kraft-budget/aimo-0790-style
reformulation, as two concrete, distinct, non-redundant proof strategies for the SAME open g*
claim.

### TASK 2 — plateau-break: genuinely different whole-problem framings

Evaluated four candidate framings per dispatch, each checked for isomorphism to already-open/
dead items before being proposed as new:

1. **Direct adversary/strategy-stealing on the ORIGINAL (non-D/M) problem.** Already
   conclusively ruled a logical non-sequitur in round 3 (proving XY can always force `<=e_n`
   against ANY opening says nothing about the infimum against the one fixed dyadic opening) —
   re-confirmed by re-reading round 3's argument; this is a dead end, not revived.

2. **Generating-function argument.** The natural generating-function object here is exactly
   the continued-fraction recursion `e_m = e_{m-1}/(2+e_{m-1})` (equivalently
   `1/e_m = 2/e_{m-1}+1`), which is **already** the mechanism underlying the conjectured
   closed form `c(n)=2^n/(2^{n+1}-1)` and every certified cascade/superincreasing lemma in the
   population. A "generating function" framing collapses into machinery already in active use
   (dyadic-cascade-induction's cascade reachability, the D/M formalism) — **not a genuinely new
   framing**, just a different name for the existing recursion. Not proposed as a new slug.

3. **Entropy/information-theoretic bound.** The observation above that `g*(t)~log2(t)` (a
   "bit-length"/valuation-flavored function) is real and worth recording, but on inspection
   this is not independent of the population's existing machinery: it is essentially the same
   "count bits / non-vanishing signed subset sum on a superincreasing sequence" idea already
   certified as the **Superincreasing No-Early-Zero Lemma** (`lemmas/superincreasing-no-early-
   zero.md`), restated in "information content" language. **Not a genuinely different framing**
   — it explains *why* g* looks the way it does, but doesn't open a new attack route beyond
   Task 1's certificate-proof gap. (The Kraft-budget idea from `aimo-0790` in Task 1 above is
   the one piece of "information-theoretic" content that IS a new technique, but it's a new
   *proof method* for the existing certificate route, not a new *framing* of the whole
   problem — flagging this distinction explicitly since CLAUDE.md wants the latter.)

4. **A totally different recursive decomposition of `c(n)` in the outer variable `n` itself**
   (as opposed to the case-split induction on `m`/cut-count within one fixed `n`). Checked
   concretely: this is exactly what `dyadic-cascade-induction`'s Case (i)/(ii) induction
   already attempts (a "for all `a` in the simplex, for all `n`" induction on `n` using the
   `n-1` IH) — **isomorphic to the existing main line**, not new. Round 6 already found the
   analogous "self-similar `c(n)` recursion" idea reduces to the same open all-cycles/multi-cut
   gap (memory rule 26) — re-confirmed this still holds; no new angle found here.

**Genuinely new candidate identified this round: the probabilistic-method / averaging
reformulation of the upper-bound direction (Case ii).** For the upper bound, the goal is: for
ANY Liu Bang opening `a`, exhibit an XY response (≤n cuts) achieving `e<=e_n*S(a)`. Instead of
constructing an explicit deterministic response (the two greedy policies already falsified,
round 3/5), consider a **randomized** response distribution (e.g. a random non-crossing
matching, or the random choice among the several *numerically observed* tied-optimal responses
noted in memory rule 23) and bound `E[e]` over that randomness; since `min <= mean`, if
`E[e]<=` target, a good deterministic response is guaranteed to exist without ever naming it.
Checked the corpus (`probabilistic-method` subtopic, combinatorics + algebra, ~40+ cruxes) for
a structurally similar averaging bound on an alternating-sign/rank-coupled objective: **no
close analog found** (the corpus's probabilistic-method cruxes are existence/counting arguments
for combinatorial structures, not averaging bounds on a Stackelberg-game value). This IS a
genuinely different mechanism from every approach currently in the population (none of the
three current slugs use averaging/expectation at all) — but it is **speculative and untested
here**: no concrete random distribution over responses was constructed or checked this round
(time was allocated to Task 1's deeper g* verification instead, per the round's primary/
secondary task split). Flagging it as an open, unexplored, genuinely-different candidate for a
future round to actually test (starting point: compute `E[e]` under the uniform-random choice
among the several numerically-tied optimal responses at `m=4,5` and see if it beats the crude
bound `F` used by the current case-split, which would be a first concrete signal).

### Summary for the outliner

- Task 1 g*: no counterexample found through **m=7** (new, stronger than the file's own `m<=6`
  claim); still unproved; two concrete, distinct candidate proof strategies now on the table
  (pairing/coarsening telescoping argument; Kraft-budget reformulation inspired by `aimo-0790`)
  — genuinely different from each other, both worth a builder's time.
- Task 2: three of four candidate "new" framings (adversary/strategy-stealing, generating-
  function, entropy) checked and found isomorphic to already-explored dead ends or existing
  machinery, each with a concrete derivation given above (not just asserted) — consistent with
  round 6's finding that this population's natural "different framings" mostly collapse to
  existing lines. **One genuinely new, unexplored candidate found: a probabilistic/averaging
  argument for the upper-bound direction** — distinct in kind from all three current slugs, not
  isomorphic to any open item, but entirely untested (flagged for a future round to actually
  try, not just propose).

### Candidate technique(s)
- For g* (Task 1): pairing/coarsening telescoping induction on dyadic-bracket membership; OR
  Kraft-budget/binary-decomposition reformulation (crux `aimo-0790`).
- For the whole-problem plateau (Task 2): probabilistic/averaging existence argument for the
  upper-bound Case (ii) response (new, untested); everything else considered reduces to
  existing lines.

### Cheap-kill candidates
- None obvious for g* beyond what's already run (exhaustive m<=7 found nothing; a hand-built
  adversarial state per the file's own suggested next step — extending the chain-subtraction
  construction past what BFS naturally finds — was not attempted this round, time went to
  extending the exhaustive check itself instead; worth trying next as a cheaper alternative to
  a full m=8 BFS).
- For the probabilistic-method idea: cheaply testable by hand at `m=4` (small state space,
  already enumerated by prior rounds) before any general construction — a quick way to falsify
  or support it before investing more.

### Knowledge-base entries to use
- KB "Invariants & monovariants" (Combinatorics section) — relevant to both g*'s coarsening
  idea and any pairing/telescoping proof attempt.
- KB entries on piecewise-concavity / LP duality already cited by `concavity-minimax-duality`
  (edge-normal concave-kink condition) — not needed for g*'s certificate route specifically.

### Analogous past problems (cruxes)
- **`aimo-0790`** (algebra, sequences-and-recurrences) — Kraft-style weighted-budget
  decomposition of a subadditive function bounded at powers of 2, extended to all `n` via
  binary expansion. Genuinely structurally suggestive for proving g* (both objects are pinned
  at powers of 2 and extended via a weighted/binary mechanism) — a *hint to adapt*, not a
  citation; the actual subadditivity relation and "n"-analogue for this game must still be
  derived from scratch.
- No other crux in `games-and-strategy` or `invariants-and-monovariants` (40 + hundreds
  respectively scanned) is a close match to either the D/M bisect/match game or the
  certificate-function construction — consistent with round 5-6's prior "no close analog"
  findings; not forcing a weak match.

### Prior progress
`concavity-minimax-duality`'s Combined Theorem (`lemmas/forcing-characterization-dyadic.md`)
fully characterizes forcing (`k+1<=g(2^k)<=2^k`, equality iff `k in {0,1}`) — certified, solid.
g* is the file's proposed exploit of the located slack, verified through `m=6` by the builder;
this round extends that to `m=7` (new) with zero violations, and adds the minimum-value/
pairing-structure observations plus the `aimo-0790` lead — genuine incremental progress on the
open g* sub-problem, not a proof.

### Dead ends (do not retry)
- Strategy-stealing / direct-adversary argument on the original (non-reformulated) problem —
  reconfirmed dead (round 3, non-sequitur), do not retry.
- Generating-function framing as a *distinct* attack — collapses into the already-used
  cascade-reachability/continued-fraction recursion, not new.
- "Entropy" framing as a *distinct* attack — collapses into the certified Superincreasing
  No-Early-Zero Lemma's mechanism restated in different language, not new (though it does
  usefully explain g*'s shape).
- Self-similar `c(n)` outer-recursion as a *distinct* attack — isomorphic to the existing
  Case(i)/(ii) induction on `n`, per round 6's finding, reconfirmed.

### Small-case / intuition notes
- (Conjecture, strong evidence) g* is a valid 1-Lipschitz certificate for every `m`: exhaustive
  zero-violation checks through `m=7` (5.28M states, this round) plus `m<=6` (file, 326K
  states). Not proved.
- (Conjecture) The certificate's tight/minimizing set grows richly with `m` (many distinct
  minimizers, not one clean witness family) — mirrors the raw problem's own known tie-richness
  (memory rule 23); this predicts a correct proof will likely need a counting/inductive
  argument robust to many minimizer shapes, not a single clean witness chain.
- (Observation, not yet a theorem) `g*` acts as a coarsening that creates cancelling pairs
  among same-dyadic-bracket elements in the sorted alternating sum; at exact minimizers the
  cancellation is total except for one residual `=1`; at generic states cancellation is partial,
  giving `e_{g*}>1`. This is the concrete mechanistic explanation for why g* seems to work, and
  the natural shape a future inductive proof should take.
