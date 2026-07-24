# Outline review — round 16, imo-2026-03

Reviewed: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §25 (round-16
outliner revision), against `results/imo-2026-03/current.md`, `lemmas/three-bound-domination-and-
keep-top-bound.md`, `lemmas/shrink-list-monotonicity.md`, and the round-16 explorer reports.
All three claims were independently re-verified with **fresh code written from scratch**
(`/tmp/round-16/verify_reviewer/`), not reusing the outliner's or explorers' harnesses.

## §25.1 — Gap 1b's base case (`rest=∅`, `q=3`): Sum-Bound Base Case Lemma

**Verdict: SOLID. Independently re-derived by hand and re-verified computationally — no gap
found. Certify.**

Re-traced the whole ~10-line contradiction chain from the definitions up, and separately checked
each imported ingredient's scope against the base case's exact hypotheses:

- **Ingredient 1 — `A_1<=b_0`.** This is literally the certified Shrink-List Corollary
  (`OPT_{+1}(C,W)<=e(C)`, no restriction). Confirmed unconditionally, `0/20,000` fresh random
  trials (own harness).
- **Ingredient 2 — `A_1<=w_1-b_0`.** This is `§21.1`'s Step-1 `(†)` bound (`A_1<=|b_0-z_j|` for
  any `j`, unconditionally proved, no hypothesis) instantiated at `w_1`'s index, using `b_0<w_1`
  (from `h=0`) to drop the absolute value. Confirmed: `0/20,000` fresh trials of `(†)`'s
  unrestricted form, and confirmed the `h=0`-conditioned simplification `A_1<=w_1-b_0` separately,
  `0` failures when `b_0<w_1`.
- **Ingredient 3 — the "certified exact `q=3` dichotomy" `M=min(D_{k*},w_1-D_{k*})`.** I checked
  this is *not* actually a standalone certified lemma file (the `three-bound-domination-and-keep-
  top-bound.md` file itself says the dichotomy identity was **declined for certification**, "too
  narrow/one-line"). §25.1's citation is loose wording, but the underlying fact is true and cheap:
  a singleton residual list has exactly two selections (delete/keep), so
  `A_{3,k*}=min(D_{k*},\text{keepval})`, and under `h=0` the certified Keep-Top Bound gives
  `keepval=w_1-D_{k*}` exactly (its "keep `w_1`, delete the rest" witness, applied here to a
  1-element `W`). I independently confirmed this combination directly: `0/8,434` fresh `h=0`-
  filtered trials. **Recommend the builder cite this explicitly as "singleton-list dichotomy +
  certified Keep-Top Bound" rather than as if it were itself a named certified lemma** — a minor
  wording fix, not a math error.
- **The algebra chain itself** (steps (i)/(ii), forcing `D_{k*}=d_{k*}-b_0`, substitution,
  contradiction with `h=0`'s `d_{k*}<w_1`) — re-derived by hand independently, matches exactly.

**My own independent computational battery** (all fresh code, not reusing the outliner's):
random mixed-alphabet sweep (`0/1,861` genuine triggered `h=0` instances out of 30,000 raw
trials), **exhaustive** small-integer grid `0..6` including duplicates/ties (`0/24`), **exhaustive**
half-integer grid `0..4` step `0.5` targeting boundary/tie cases (`0/88`), a **targeted boundary
construction** explicitly engineered near `2D_{k*}=w_1` (`0/1,630`), and negative controls: dropping
the trigger while keeping `h=0` gives `12.4%` violations (confirms the trigger is load-bearing, as
expected). Also independently confirmed the stated tightness/vacuity argument at the boundary
`2D_{k*}=w_1` by hand — correct.

**Scope check (per dispatch instruction):** the proof is specific to the base-generator's own
`(B_1,Z_1)` node, where `C={b_0,d_{k*}}` is fixed exactly as produced by the base generator (not
a generic 2-element `C` arising deeper in the recursion after a KEEP-closure step) — this matches
what "the base case of the `|rest|`/recursion-depth induction" needs to be, consistent with how the
Vertex Lemma / all-cycles closures elsewhere in this population were built (base case first, general
induction separately). **This is genuine progress on Gap 1b, not merely the most degenerate
sub-case treated in isolation** — it is exactly the base case the outliner's own §21.2/§23.3
induction skeleton requires, and the file's own scope note ("PROVED at `|Z_1|=1`; open for
`|Z_1|>=2`") is accurate, not an overclaim.

**Recommendation: certify `lemmas/sum-bound-base-case.md` this round, with the wording fix above
(cite the dichotomy as a two-step combination, not as a pre-existing certified lemma).**

## §25.2 — Gap 1a Two-Touch Lemma

**Verdict: sound target, correctly scoped, safe to build.**

- `|C|=1` formula `OPT_{+1}(\{b_0\},W)=\min(e(\{b_0\}),\min_w e(\{b_0,w\}),\min_{i<j}e(\{b_0,|w_i-
  w_j|\}))`: independently confirmed **`0/6,000`** fresh trials (`q` up to 6, mixed alphabets) —
  reproduces the outliner's `0/4,000`.
- `|C|=2` "touch<=2" analog dead end: my independent construction gives **`541/3,000` (18.0%)**
  failures — same order of magnitude as the outliner's `23.8%`/explorer's `24%` (the numeric gap is
  a benign artifact of a differently-shaped candidate set/value-range choice, not a discrepancy in
  substance) — **confirms this really is a hard structural wall, not a fluke.** Do not port to
  `|C|=2`, as the outline already warns.
- The proposed induction-on-`|W|` route (base case = certified Three-Bound Domination Lemma, read
  as an inequality) is structurally sound on inspection — Three-Bound Domination's own statement
  (`min(x,|x-y|,|x-z|)<=e_sorted({x,y,z})`) is literally the `|W|=2` instance of Two-Touch's target
  inequality once you substitute `x=b_0`. No issue found with this reduction.
- The outline's caveat that proving Two-Touch does **not** by itself close the general-`q`
  Per-Partner Domination induction (a separate per-`q` case analysis on `A_{3,l}`'s own recursion
  is still needed) is correctly and explicitly stated — not silently glossed over.

## §25.3 — Gap 1c half-step Step-3 construction

**Verdict: the reusable identity is SOLID and should be certified now; the Step-3 construction
remains genuinely unverified (matches the outline's own honest flag) — and my own attempt to
verify it surfaced an extra precision gap worth handing to the builder.**

- **Insertion-Difference Identity** `e(M∪{d})-e(M)=(-1)^h(d-2e(tail_d))`: independently confirmed
  **`0/8,000`** random (mixed alphabets, `|M|` up to 6) **+ `0/780` exhaustive** (integers `0..4`,
  `|M|` up to 3, all `d`). Clean, general, no `F`-provenance needed. **Recommend certifying
  `lemmas/insertion-difference-identity.md` immediately, independent of whether Step 3 closes** —
  exactly as the outline recommends.
- **Step-3 construction** (`c:=argmin_{x in ξ*}|x-d|`, conjecture
  `e(B_1∪(ξ*\{c}))<=OPT_{+1}(B_1∪\{d\},X)`): I attempted an independent re-verification and could
  **not** get a clean read on it, for a reason worth flagging explicitly to the builder beyond what
  the outline already says: **`ξ*` ("the LHS-optimal witness") is often NOT uniquely determined.**
  When I built genuine `F`-provenance instances one level past the base generator and computed an
  actual optimal witness for `OPT_{+1}(B_1,X)`, the optimum was very frequently tied with the
  **empty** witness (`ξ*=∅`, i.e. delete everything — consistent with the already-proved Shrink-List
  Corollary `OPT_{+1}(C,X)<=e(C)` often being tight there), in which case `c:=argmin_{x in
  ξ*}|x-d|` is **undefined** (empty set has no argmin) and the construction doesn't even apply.
  This isn't a refutation of Step 3 — it's a **specification gap**: the outline needs to state
  explicitly whether the claim is "for every optimal witness `ξ*`" or "for some (canonically
  chosen, e.g. maximal/least-degenerate) optimal witness `ξ*`", and separately handle the `ξ*=∅`
  boundary case (which likely reduces to a variant of the already-proved Deletion-Suffices bound,
  not to Step 3's own mechanism). **Add this as an explicit sub-task before the algebra**: pin down
  `ξ*`'s definition and dispose of the `ξ*=∅` case first, THEN attempt the nearest-neighbor-drop
  algebra on genuinely nonempty witnesses. This sharpens, but does not invalidate, the outline's own
  "builder's first task: re-verify this construction" flag — it explains *why* a naive
  re-verification attempt stalls, which the outline didn't anticipate.
- Watch-outs in the outline (do not resurrect Step-2's naive witness-reuse; stay within
  top-level-only `F`-provenance per round 15's simplification) are consistent with everything on
  file — no issue.

## Diversity / single-gap-trap check

Unchanged from prior rounds: `potential-weighting-upper-bound` is the sole live slug; `dyadic-
cascade-induction` (lower bound, verified milestone) and `concavity-minimax-duality` (superincreasing-
tied machinery, no leverage on the open upper-bound gap) remain correctly benched, reconfirmed by
this round's outliner as having no new applicable leverage. No new slug opened this round — correct
per CLAUDE.md's single-gap-trap rule; Gaps 1a/1b/1c are three genuinely different sub-lemmas of one
target (Claim A), not a single proof mechanically split into three files.

## Overall verdict

**APPROVE.** The technique (strong induction on `q`/recursion depth within the scope family `F`,
via the certified DELETE/KEEP/MATCH trichotomy) remains sound and is the only mechanism on file
capable of closing SAR/Claim A. §25.1's Gap 1b base-case proof is genuinely complete and correct —
independently re-derived and stress-tested well beyond the outliner's own sweep (exhaustive grids,
targeted boundary construction, negative controls) with zero violations found anywhere. §25.2 and
§25.3 correctly distinguish proved general facts (Three-Bound Domination base case; Insertion-
Difference Identity) from still-open conjectural constructions, with no missing cases and no
circular reasoning. One precision gap found in §25.3 (well-definedness of `ξ*` under ties) — not
fatal, added as an explicit sub-task for the builder, not a routing change.

## Recommended build order (confirms §25.4, with the one addition above)

1. Write up and certify `lemmas/sum-bound-base-case.md` (near-zero risk, ready to go) — fix the
   citation wording for the "q=3 dichotomy" per the note above (cite it as Keep-Top Bound + the
   trivial singleton-list observation, not as a separately-certified lemma).
2. Certify `lemmas/insertion-difference-identity.md` (general, proved, no risk).
3. Gap 1c Step-3: FIRST pin down `ξ*`'s exact definition and dispose of the `ξ*=∅` boundary case
   (new sub-task surfaced this round), THEN attempt the nearest-neighbor algebraic closure.
4. Gap 1a Two-Touch Lemma: attempt the induction on `|W|` (base case already certified via
   Three-Bound Domination).
5. If time remains: Gap 1b's general recursion-depth inductive step (large, lower priority).

## Ranking

Ranked the field via `update_ranking` (4 approaches in population): `dyadic-cascade-induction` beats
`potential-weighting-upper-bound` (verified-milestone status, more complete than this round's
still-partial progress); `potential-weighting-upper-bound` beats both benched/retired
`concavity-minimax-duality` and `elementary-exchange-smoothing` (real new progress this round vs.
stale/no-further-leverage). Updated Elo: `dyadic-cascade-induction` 1709.4 (top, benched),
`potential-weighting-upper-bound` 1557.3 (live), `elementary-exchange-smoothing` 1430.2 (retired),
`concavity-minimax-duality` 1303.1 (benched). No new approach registered this round (no new slug
opened).

build set: potential-weighting-upper-bound
