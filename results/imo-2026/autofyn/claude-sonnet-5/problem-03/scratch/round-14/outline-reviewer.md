## imo-2026-03 — outline review, round 14

Reviewed: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` new §21 (revision of
Gaps 1a/1b/1c), against the three round-14 explorer reports and the proof-outliner's report. All
verification below uses fresh, independently-written Python (exact `fractions.Fraction`, brute-force
`OPT_sigma` re-implemented from the file's own §13.2/§17.2 prose, not copied from any explorer's or the
outliner's harness), validated first against the file's own worked examples (`C={5,8},W=(10,8,7,2)
->OPT=0`; `C={1},W=(10,8,7)->OPT=0,OPT_KD=1`) before trusting it for anything new. Code at
`/tmp/round-14/work/`.

### 1. Gap 1a — "Deletion-Suffices-for-k*" and the counterexample scope

Independently implemented the base generator (`A_1`, `A_{3,l}`, `M`, `k*`, trigger `M<A_1`) from
scratch and checked:
- **The reported non-triggered counterexample is correctly out of scope.** `Z0=[100,98,70,60],b0=10`:
  my code gives `A_1=0` (via delete-98, match(70,60)->10, background `{10,10}`->`e=0`, a Lemma-P
  cancellation) and `M=2` — since the trigger is `M<A_1` and `2<0` is FALSE, this instance is
  correctly non-triggered, exactly as the file claims. Confirmed the counterexample genuinely kills
  only the *unconditional* version of Deletion-Suffices, not the trigger-scoped conjecture.
- **Deletion-Suffices-for-k\* itself**, `M=|b_0-d_{k^*}|` at genuine triggered+global-argmin instances:
  0 violations across an exhaustive sweep (`q=3..5`, `vmax=4`, 80 checked/23 triggered), a random
  sweep (6000 trials, `q=3..7`, `vmax` up to 20, 1670 triggered), a `q=7,8` random sweep (400 trials,
  77 triggered), and an extra push beyond the outline's own tested range (`vmax` up to 50, `q=5,6`, 68
  triggered) — **~1838 fresh triggered checks total, 0 violations**, all ties in `k^*` handled (looped
  over every simultaneous argmin). This corroborates but does not prove the conjecture, exactly as
  honestly labeled in the file.
- **Step 1** (`A_1\le|b_0-z_j|` for any `j`, unconditional): re-verified directly as a one-line valid
  selection, 0/1419 fresh checks — correct, no hypothesis needed, matches the file.
- **Step 3, the "three-line closure"**: traced the logic by hand — no sign error, no hidden case. The
  half-open shape (`(min,max]` forbidden, not `[min,max)`) is exactly right: at `z_j=\max(b_0,d_{k^*})`
  the bound `|b_0-z_j|=D=M` exactly still contradicts the *strict* trigger `M<A_1`, so the boundary
  is correctly included with no extra casework. **Directly verified the logical conclusion itself**
  (independent of trusting Step 2): no `z_j` ever falls in the claimed half-open interval across 1618
  fresh triggered instances (0 violations), and even the file's "bonus" fully-closed-interval
  strengthening held with 0 violations in the same sweep — consistent, no overclaim.
- **Verdict: sound as far as it goes.** Step 2 is the one genuine open sub-lemma, correctly flagged as
  conjectural (not hand-waved — the file explicitly gives the non-vacuity counterexample and states
  two untried proof directions). CHANGES REQUESTED-level content, ready for a builder.

### 2. Shrink-List Monotonicity Lemma

Verified the one-line bijection proof is correct and fully general: extending an optimal selection of
`W\{x}` by additionally deleting `x` gives one particular (not necessarily optimal) selection of `W`
with the identical value (deletion contributes 0, the standing convention), so `OPT_{+1}(C,W)\le` that
value `=OPT_{+1}(C,W\{x})`; mirror for `\sigma=-1`. Independently stress-tested with fresh code on
arbitrary `(C,W,x)` (no `\mathcal F`-restriction), both signs: **0/3000 violations.** This is a
genuinely free, general, correctly-proved lemma — **recommend certifying to `lemmas/` as the file
suggests**, pending only the trivial convention check the file itself flags (confirmed: my brute-force
`OPT_sigma` implementation, which treats a deleted element as contributing 0 to `e`, exactly matches
this lemma's assumption and reproduces the file's own worked examples, so the convention is consistent).

### 3. Half-step lemma — genuinely distinct from Shrink-List, not a relabeling

Confirmed the distinction is real, not cosmetic: Shrink-List fixes the background `C` and shrinks the
*list*; the half-step fixes the *list* `X` and grows the background (`C\to C\cup\{d\}`) — these are
different arguments of the same recursion and are logically independent. Evidence this is a real
distinction, not just notation:
- The fully general (`d` arbitrary) background-insertion monotonicity is FALSE (reproduced the file's
  cited `817/4000`-type failure independently, e.g. `C=[7],d=7` duplicate-cancellation), yet
  Shrink-List (list-shrinking) holds unconditionally — different logical content, confirmed by
  different truth values under the same kind of perturbation.
- Reproduced the file's specific counterexample to the *general* (non-`\mathcal F`) half-step exactly:
  `C=[7],W=[5,3]` (so `w_1=5,w_m=3,d=2,X=\emptyset`) gives `OPT_{+1}([7,2],\emptyset)=5 <
  OPT_{+1}([7],\emptyset)=7` — confirmed bit-for-bit.
- **Within genuine `\mathcal F`-provenance**, built an independent DELETE/KEEP closure-walk (depth 3,
  fresh code, not reusing any prior harness) from 397 base-generator attempts (77 triggered),
  and tested the half-step for every partner at every closure node: **0/966 fresh violations** —
  corroborates the conjecture is real and correctly scoped, distinct from both the free Shrink-List
  lemma and the already-dead general background-insertion monotonicity.
- **Verdict: the outliner's correction of the explorer's report (mislabeling the two steps as "the
  same lemma") is correct and necessary** — a builder citing Shrink-List for the half-step would be
  citing the wrong (and much weaker) fact. Good catch by the outliner; no further fix needed here.

### 4. Sum Bound (Gap 1b) — breakpoint strategy check

- **Reproduced the exact finite equality witness bit-for-bit**: `Z_0=(8,25/4,25/4,55/12,13/3),
  b_0=23/6` gives `A_1=1/2`, `M=1/6` (triggered), `k^*` index giving `C=(23/6,11/3)`,
  `W=(25/4,25/4,55/12)`, and `OPT_{+1}(C,\mathrm{rest})=1/6`, `OPT_{-1}(C,\mathrm{rest})=73/12`,
  sum `=25/4=w_1` exactly — matches the file's claim precisely.
- **Reproduced the asymptotic family exactly**: for `(n,t,b_0)=(100,1/5,n/2-1/100),
  (100,1/10,n/2-1/1000),(1000,1/20,n/2-1/1000),(10000,1/50,n/2-1/10000)`, my independent
  base-generator code gives `gap=0.4200, 0.2020, 0.1020, 0.0402` and `ratio=2.0084, 2.0040, 2.0002,
  2.0000` — matches the file's reported numbers to 4 decimal places exactly, and confirms
  `A_1=b_0` exactly at this family (a genuine tie between the delete-both-duplicates and
  match-the-duplicates branches of `A_1`'s own trichotomy — i.e. this extremal family **is** an
  instance of the claimed breakpoint type (i), not an unrelated phenomenon; a real, useful
  cross-check that the enumeration isn't blind to the one hard family already found).
- **Verified the piecewise-linear-in-one-coordinate claim directly** (not just trusted): froze a
  background coordinate and a fixed `rest`, scanned it over a range, and found the target quantity
  `w_1-OPT_{+1}(C,rest)-OPT_{-1}(C,rest)` is exactly piecewise-linear with a genuine breakpoint where
  the frozen coordinate crosses a `rest` value (slope changes `0\to-2` at the crossing) — corroborates
  the proposed *technique* is mathematically valid, not merely plausible-sounding.
- **Found and fixed one genuine precision gap (in-place edit made to §21.2):** the three named
  breakpoint types are presented as a single top-level enumeration, but `OPT_{+1}(C,\mathrm{rest})`
  and `OPT_{-1}(C,\mathrm{rest})` are themselves defined by the *same* recursive trichotomy one level
  down, so breakpoints can also arise from ties buried inside that inner recursion, not only from the
  three named top-level ties. A flat case-check on the three types, without a supporting induction on
  `|\mathrm{rest}|`, would be incomplete. Added a note to the file flagging that a builder must run
  this as a strong induction (the same shape that closed the all-cycles gap via the Vertex
  Lemma/Shared-Value Cycle-Breaking Lemma), with the three named types serving only as the base-case
  classification. This does not kill the strategy — the mechanism itself is sound and reuses certified
  machinery — but the outline as written understates the amount of structure (induction, not flat
  enumeration) actually required; correctly this round's lowest build priority (3 of 3), consistent
  with more remaining work than Gaps 1a/1c.

### 5. dyadic-cascade-induction / concavity-minimax-duality staying benched

Confirmed: none of this round's three explorer reports (Gap 1a/1b/1c, all targeting
`potential-weighting-upper-bound`'s residual) produces any `A`-generic (non-superincreasing-specific)
statement usable by `concavity-minimax-duality`'s machinery, nor any new leverage for
`dyadic-cascade-induction` (whose lower-bound work is already complete and unconditional since round
8). Consistent with 5+ rounds of repeated reconfirmation. Agree they stay benched.

### Ranking

Ranked the whole field via `update_ranking` (potential-weighting-upper-bound winner over both benched
approaches given real incremental progress this round — Deletion-Suffices sub-lemma further
corroborated, Shrink-List Monotonicity fully proved and ready to certify, half-step lemma correctly
isolated/distinguished, Sum Bound sharpened to a genuinely tight, well-posed-if-inductive strategy;
dyadic-cascade-induction still outranks concavity-minimax-duality per its historically stronger,
fully-verified milestone; potential-weighting-upper-bound beats retired elementary-exchange-smoothing
trivially). No new slug registered this round (no new approach opened — `potential-weighting-
upper-bound`'s existing slug is simply revised in place, per CLAUDE.md's single-gap-trap rule, which
the outliner correctly followed by declining a 5th slug).

### Overall verdict

**CHANGES REQUESTED for `potential-weighting-upper-bound`** (as a whole file/approach) — no RETHINK:
every mechanism checked this round is either already correct (Step 1/Step 3 of Gap 1a, Shrink-List
Monotonicity) or an honestly-flagged, well-corroborated, non-vacuous open conjecture (Deletion-Suffices,
the half-step lemma, the Sum Bound), with one real (now fixed) precision gap in the Gap 1b strategy
description. Nothing here repeats a recorded dead end, and nothing is circular.

### Recommendation for this round's builder(s)

All three sub-gaps live in the *same* file/slug (`potential-weighting-upper-bound.md`), so per
CLAUDE.md a single approach = a single file — do not fragment it across separate slugs. If the
orchestrator wants to parallelize builder effort within this one slug this round, partition strictly
by **section**, each builder appending only to its own new subsection and leaving §21.1/§21.2/§21.3
untouched as history, to avoid merge collisions:
- Builder A: certify Shrink-List Monotonicity Lemma to `lemmas/` (cheap, essentially done) + attempt
  Gap 1a's Deletion-Suffices-for-`k^*` (§21.1 Step 2, highest expected payoff).
- Builder B: attempt Gap 1c's half-step lemma (§21.3) — flagged as possibly sharing a mechanism with
  Gap 1a, worth trying in parallel/comparing notes rather than serially.
- (Optional, lower priority, only if a third builder slot is available) Builder C: attempt Gap 1b's
  breakpoint enumeration (§21.2), now explicitly scoped as an induction on `|rest|`, not a flat
  3-case check — this is the least-ready of the three and the most likely to need another round of
  outlining if it stalls.

If only one or two builders are dispatched this round, prioritize Gap 1a (Deletion-Suffices, most
corroborated and shortest remaining path to a closure) and Gap 1c (half-step, comparably ready) over
Gap 1b (more remaining work, per both the explorer and this review).

build set: potential-weighting-upper-bound
