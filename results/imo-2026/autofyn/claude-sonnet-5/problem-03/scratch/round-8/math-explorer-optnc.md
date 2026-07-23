## imo-2026-03 (lens: upper-bound Case (ii), the rescoped conjecture `OPT(Y,p-1)=NC(Y,p-1)`)

### Setup recap (from `potential-weighting-upper-bound.md` §9, certified lemma
`lemmas/layer-cake-and-noncrossing-independence.md`)
`Y=(y_1\ge\dots\ge y_p)` sorted. A **selection** is `(K,D,M)`: kept indices `K`, deleted
indices `D`, non-overlapping matched pairs `M`; cost `=|D|+|M|\le b`; value
`v=e(\{y_k:k\in K\}\cup\{y_i-y_j:(i,j)\in M\})`. `OPT(Y,b)=\min v`; `NC(Y,b)=\min v` over
selections whose matched pairs are pairwise non-crossing (`i<i'<j<j'` forbidden). Trivially
`NC\ge OPT`. General conjecture `OPT=NC$ for all `b` is FALSE (certified counterexample,
`p=7,b=3`, needs a genuine 3-arc crossing chain). The needed target is the narrower
`OPT(Y,p-1)=NC(Y,p-1)` for every `p` — 2218 exact trials, zero mismatches, unproved.

### 1. New structural fact (budget/final-size identity) — elementary, verified, not previously
stated in the file
For any selection, the **final active-multiset size** is `f:=|K|+|M|`. Counting elements,
`|K|+|D|+2|M|=p`, and `\text{cost}=|D|+|M|`, gives the identity
```
f = |K|+|M| = p - \text{cost} + |M| ... (algebra) ... \Longleftrightarrow  |K|+|M| \ge p-b =: \text{gap}.
```
(Direct derivation: `\text{cost}=p-|K|-|M|`, so `\text{cost}\le b \iff |K|+|M|\ge p-b$.) So **the
final size after any legal selection is always `\ge\text{gap}=p-b`**, with equality iff the full
budget `b` is spent. This is just budget-conservation but it cleanly parametrizes the search: at
`\text{gap}=1$ (our target, `b=p-1`), spending the *entire* budget forces a **singleton**
(`f=1`) — but empirically (see §2) the true optimum very often does *not* spend the whole
budget, so "reduce to a singleton" is a valid *upper bound* on `OPT(Y,p-1)` (namely
`\min(\min_i y_i,\ \min_{i<j}|y_i-y_j|)`) but not the mechanism that makes `OPT=NC` true in
general — do not present "always reduces to a singleton" as the load-bearing fact, it's false as
a *characterization* of the optimum, only as one candidate certificate.

### 2. A genuinely new, verified structural lead: induction on `p` splits into a "MIN" and a
"MAX" companion conjecture, self-consistently, at the two gaps that actually occur

Peel the global max `y_1`. **Key elementary identity** (telescoping, `x_{n+1}:=0$ convention):
`e(y_1,\dots,y_p) = y_1 - e(y_2,\dots,y_p)` for ANY sorted list — trivial from the definition of
`e`, and it applies to the "KEEP `y_1`" branch of any selection because `y_1` is the global max
of `Y`, hence remains the max of the final combined multiset (every matched difference
`y_i-y_j\le y_i\le y_1`), so the final sorted list is exactly `(y_1,\text{sorted }R)$ for
whatever residual multiset `R` the rest of the selection produces.

Doing the 3-way case split on `y_1`'s fate (kept / deleted / matched-to-`y_j`) for
`\text{MINOPT}(Y,p-1)` (`|Y|=p`):
- **DELETE `y_1`:** cost 1, residual `Y'=Y\setminus\{y_1\}` (size `p-1`), budget left `p-2`.
  `\text{gap}=(p-1)-(p-2)=1` — **exactly the same gap, one smaller `p`: a direct self-similar
  application of the strong IH.** Verified: this reduction is exact (no approximation).
- **MATCH `y_1,y_j`:** cost 1, new list `Y''=(Y\setminus\{y_1,y_j\})\cup\{y_1-y_j\}` (size
  `p-1`), budget left `p-2`, **same gap `=1`, self-similar again** — BUT see the caveat in
  §3 below: this reduction is only sound for the *unconstrained* (`OPT`) side if it can be
  compared apples-to-apples against `NC`'s own match-branch, and `NC`'s match branch, by the
  ALREADY CERTIFIED non-crossing inside/outside independence lemma, is NOT simply
  `NC(Y'',p-2)` — it is the independent-inside/outside decomposition. This is exactly where
  the general conjecture is known to fail (the `p=7` counterexample's winning move is a
  3-arc *crossing chain*, i.e., a further match that crosses the `(1,j)` arc) — see §3.
- **KEEP `y_1`:** cost 0, residual budget UNCHANGED `=p-1`, residual size `=p-1` — so the
  residual sub-problem sits at **budget `=` size exactly, i.e. `\text{gap}=0`**. Since the total
  value is `y_1-e(R)`, MINIMIZING it means MAXIMIZING `e(R)` over the residual selection — a
  **different (MAX, not MIN) companion optimization**:
  ```
  \text{MAXOPT}(Y',b') := \max_{\text{selections on }Y',\ \text{cost}\le b'} e(\text{final}),
  \qquad\text{MAXNC analogous, non-crossing only.}
  ```
  So: `\text{MINOPT-value of KEEP branch} = y_1 - \text{MAXOPT}(Y',p-1)$, `|Y'|=p-1` — i.e. the
  MAX version **at gap 0**.

**Numerically tested this companion conjecture `\text{MAXOPT}=\text{MAXNC}` (fresh code, exact
`fractions.Fraction`, this round):**
- At `\text{gap}=0` (`b=p`, exactly the case the KEEP branch needs): **0 mismatches / 2000
  random trials**, `p=2..7`.
- At `\text{gap}=1` (`b=p-1`): **0 mismatches / 2100 random trials**, `p=2..8`.
- At larger gap (small budget relative to size), the MAX version **also breaks**, symmetric to
  the MIN version: found real, reproducible mismatches at `\text{gap}=5$, `p=8` (e.g.
  `Y=(47,33,31,29,25,22,17,14)`, `b=3`: `\text{MAXOPT}=46>\text{MAXNC}=45`; 8/400 trials failed
  at this exact `(p,\text{gap})`).

**Why this matters:** peeling the KEEP branch *inside* the gap-0 MAX-problem itself gives, by
the identical telescoping argument, a MIN-problem at budget UNCHANGED `=p'` on a residual of size
`p'-1`, i.e. `\text{gap}=-1` (budget exceeds size) — which is trivially `0` for both `MINOPT` and
`MINNC` (delete everything; already essentially the content of the certified **Slack Collapse**
lemma, `lemmas/slack-collapse.md`, applied to the one-shot/non-cascading setting). **So the
mutual induction closes structurally**: `\text{MIN}(\text{gap}=1)`'s KEEP branch needs
`\text{MAX}(\text{gap}=0)`, whose own KEEP branch needs `\text{MIN}(\text{gap}\le0)`, which is
trivial. This is a genuinely new, internally-consistent skeleton — not previously identified in
the file (which never separates a MAX companion conjecture) — and the numerics support both
needed instances (gap 0 and gap 1) cleanly, while honestly also finding where a *naive*
generalization (arbitrary gap) breaks, mirroring the already-known MIN-side breakdown.

### 3. The one real remaining obstruction, precisely located (not a new dead end — an
open technical gap distinct from those on file)

The DELETE branch is a clean, verified self-similar reduction. The KEEP branch reduces to a new
but numerically robust companion (gap-0 MAX). **The MATCH branch is where the difficulty
concentrates**, and it is *exactly* the same difficulty that makes the fully general conjecture
false: once `y_1` is matched to `y_j`, `NC`'s recursive value (by the certified inside/outside
independence lemma) decomposes into **independent** optimization on "inside" (`2..j-1`) and
"outside" (`j+1..p`) — but `OPT`'s (crossing-allowed) recursive value does *not* have to respect
this decomposition: it may use an arc with one endpoint inside and one outside, "crossing" the
`(1,j)` arc. The certified `p=7` counterexample's winning selection is precisely a 3-arc chain of
this shape. So a bare "reduce match branch to a same-gap smaller instance and invoke IH" step is
**unsound as stated** — it implicitly assumes the reduced list can be treated as a fully fresh,
unconstrained instance, which silently reintroduces the general (all-`b`) conjecture rather than
using the gap-1-specific structure. **This is the one place a genuinely new argument is needed**,
and it should exploit gap-1-specific budget counting: an inside/outside-crossing 3-arc chain
"spends" 3 units of match cost across only a handful of elements; a clean next step (not done
this round, flagged for the builder) is to show that **whenever gap is small (specifically 1),
any winning crossing configuration can be dominated by re-routing at least one of its arcs to
avoid the cross, using the slack afforded by the *small* gap** — i.e., relate the *size* of the
minimal crossing counterexample (empirically `p\ge7$ even at the most favorable found gap) to a
lower bound on gap itself, giving an explicit bound "gap 1 (and empirically gap 2) is provably
too small to admit a crossing-improves-the-value configuration." This has NOT been attempted; it
is a concrete, well-defined next task, distinguishable from the dead local-pairwise-exchange
technique (round 6) because it is a *global* counting argument about how much "room" a crossing
chain needs, not a local 2-arc swap holding the rest of the selection fixed.

### 4. Cheap-kill candidates
- **Minimal-crossing-chain size vs. gap, a concrete counting check (cheap, not yet done):**
  search specifically for the *smallest* `p` at which a genuinely crossing-optimal
  configuration exists, as a function of gap, to see whether gap 1 and gap 2 are provably
  "too small" in a way that scales (this round found empirically: gap 1 → no violation up to
  `p=10`; gap 2 → no violation up to `p=9`; gap 3 → violation starts around `p=8`; gap 4 →
  `p=7` (the certified minimal counterexample)). **New finding this round: gap 2 also shows
  zero violations up to `p=9`** — i.e. the true safe zone may extend beyond gap 1, which is
  reassuring (gap 1 is not on a knife's edge) but the PROOF only needs gap 1.
- **Budget-vs-arc-count pigeonhole:** a crossing chain of length `L` arcs needs `L` units of
  match-cost among the involved elements; combined with the certified pigeonhole style already
  used for the Guaranteed-Untouched-Original Lemma (`lemmas/shallow-cycle-resolution.md`), there
  may be a clean argument bounding the maximum feasible crossing-chain length as a function of
  gap and remaining kept/deleted slack — worth trying before a full induction write-up.

### 5. Candidate technique(s)
- Strong induction on `p` (list size), peeling the global max, with an explicit **mutual
  induction between a MIN-conjecture at gap 1 and a MAX-conjecture at gap 0** (new this round —
  see §2). This is a genuinely different top-level target from the file's own §8 "peel `y_1`,
  three-way fate split" skeleton (which conflates MIN/MAX implicitly and doesn't isolate the
  gap-0 companion) — worth having the outliner state it explicitly as two mutually-recursive
  claims, not one.
- The already-certified Layer-cake identity / Fact 3 block extraction remain the right
  bookkeeping tools for turning "kept `y_1`" into the exact telescoping split.
- A budget-counting (pigeonhole-style) argument bounding how large a crossing chain can be as a
  function of gap, to directly attack §3's residual obstruction — not yet built.

### 6. Knowledge-base entries to use
- `knowledge_base.md`: general induction/strong-induction techniques, invariant/monovariant
  method (the layer-cake identity is exactly this in this problem's language), extremal
  principle (peeling the max element).
- Certified project lemmas: `lemmas/layer-cake-and-noncrossing-independence.md` (both proofs,
  directly reusable for the KEEP-branch telescoping split and the MATCH-branch inside/outside
  decomposition), `lemmas/slack-collapse.md` (the gap`\le0` trivial-zero fact — directly gives
  the base case for the MAX-problem's own KEEP-branch recursion), `lemmas/dm-operation-
  reformulation.md` (background for how `D`/`M` operations correspond to deletions/matches).

### 7. Analogous past problems (cruxes)
- **`aimo-0003`** (combinatorics, subtopics `invariants-and-monovariants` /
  `induction-and-construction`): a 2n-point circle, red/blue points, chords `R_i\to B_i` chosen
  by a greedy nearest-neighbor matching; task is to show a "number of chords covering a fixed
  point" invariant is independent of the pairing/ordering. **Genuinely analogous, best match
  found:** its second solution encodes the matching-count invariant as the **minimum of a
  running +/-1 tally** around the circle (identical in spirit to our Layer-cake/alternating-sum
  `e`), and proves it by **induction that deletes an "innermost" chord** (one whose arc contains
  no other matched point) rather than an extremal (max-value) element — a genuinely different
  peeling order from the one explored in §2 above (peel-the-max). This is worth flagging to the
  outliner as an alternative induction order to try if peel-the-max's MATCH-branch obstruction
  (§3) doesn't resolve: **peel an innermost/adjacent pair instead of the global max**, since an
  innermost pair by definition has nothing "inside" it, potentially sidestepping the
  inside/outside crossing subtlety at the cost of a different case analysis. (Caution: this is
  structurally close to the already-dead "sorted-adjacency" conjecture (`potential-weighting-
  upper-bound.md` §6 Step 4, falsified) — the crux's version is about invariance, not
  optimization, so it isn't the same claim, but any builder revisiting this idea must be careful
  it doesn't quietly regress into the dead adjacency conjecture; the crux's own proof works
  because the *choice of pairing* is fixed/given (greedy), not being optimized over, which is a
  real disanalogy to flag explicitly.)
- No other crux in a search of ~275 combinatorics entries (filtered by "non-crossing / matching
  / crossing / chord / arc / interval / pairing / alternating sum / telescoping" keywords) was a
  close enough structural match to the specific "OPT vs NC over signed alternating-sum objective"
  optimization; most hits were either pure invariant-parity arguments (no optimization) or
  unrelated circle-geometry problems. Report this as "one genuine partial match (`aimo-0003`),
  no others" rather than forcing weaker matches.

### 8. Prior progress
See `potential-weighting-upper-bound.md` §9 (round 7): Layer-cake identity and non-crossing
inside/outside independence both fully proved and certified. `OPT=NC` in full generality is
FALSE (certified counterexample). The correctly-rescoped `OPT(Y,p-1)=NC(Y,p-1)` conjecture is
numerically supported (2218 trials, zero mismatches) but not proved — this round adds: (a) the
budget/final-size identity (§1), (b) the mutual MIN(gap1)/MAX(gap0) induction skeleton with its
own supporting numerics (§2), (c) a precise, non-vague statement of exactly where the induction's
MATCH branch needs new work, tied directly to the known counterexample's crossing-chain
structure (§3), (d) one genuinely analogous crux (`aimo-0003`) suggesting an alternative
peeling order as a fallback if peel-the-max stalls.

### 9. Dead ends (do not retry)
- The fully general `OPT(Y,b)=NC(Y,b)` conjecture for arbitrary `b` — FALSE, certified
  counterexample on file (round 7). Do not re-attempt in general form.
- Local pairwise uncrossing-exchange (holding the rest of the selection fixed while swapping one
  match's two arcs) — confirmed dead (round 6): the true global optimum can change *which*
  elements participate, a move class no local exchange expresses. The MATCH-branch obstruction
  identified in §3 above is NOT this — it is about a global inside/outside decomposition failing
  to dominate a crossing chain, not a local swap; do not conflate the two, but also do not
  attempt to resolve §3 via any local-swap variant, per the round-6 finding.
- "Reduce the whole thing to a singleton via full budget usage" (my own initial hypothesis, §1)
  — checked computationally and found FALSE as a *characterization* of the optimum: 240/300
  random trials at gap 1 had the true optimum using LESS than the full budget (multi-element
  residual with cancellation beating any singleton). Only valid as a one-sided upper-bound
  certificate, not a mechanism.
- Naively treating the MATCH branch's reduced `(p-1)`-element list as "just another same-gap
  instance, apply the IH directly, no further care" — this is UNSOUND for the OPT side (see §3);
  flagging this explicitly so a future outline doesn't silently reintroduce the already-refuted
  general conjecture disguised as an induction step.

### 10. Small-case / intuition notes (all labeled conjecture unless stated as computed fact)
- **Computed fact:** final selection size `f=|K|+|M|\ge p-b` always (elementary budget count).
- **Conjecture (2100+ fresh trials, zero mismatches):** `\text{MAXOPT}(Y,p)=\text{MAXNC}(Y,p)`
  (gap 0) and `\text{MAXOPT}(Y,p-1)=\text{MAXNC}(Y,p-1)` (gap 1) both hold generally — the two
  instances the mutual induction in §2 actually needs.
- **Computed fact:** the MAX-companion conjecture is FALSE at large gap (mirroring the known
  MIN-side falsity), e.g. gap 5, `p=8`: real, reproducible mismatches (`\sim2\%` of random
  trials) — evidence the companion conjecture is exactly as "fragile at large gap, robust at
  small gap" as the original, supporting that both are governed by the same underlying
  phenomenon (crossing chains need enough slack/gap to help).
- **Conjecture (this round's scan, 4000–4000+ trials per gap):** the minimal list size `p` at
  which the original MIN conjecture (`OPT<NC`) has a counterexample appears to grow as gap
  shrinks: gap 4 → `p=7` (known); gap 3 → `p=8` (found this round); gap 2 → no violation found
  up to `p=9`; gap 1 → no violation found up to `p=10`. This is suggestive that gap 1 (and
  perhaps gap 2) may be provably safe via a counting argument relating chain length to gap, but
  this is NOT proved — only a numerical trend across 4 data points.
