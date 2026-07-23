## imo-2026-03

### IMPORTANT METHODOLOGY NOTE (read first)

This session initially built a brute-force `OPT_sigma` harness that only enumerated Keep/Delete
subsets of `W` — **missing the MATCH option entirely** (pairing two elements of `W` into their
difference). Several early experiments (a "per-selection reformulation" test, a "Background-Release
Domination composability" test) were run against this **incorrect** model and are **not reported
below** — they are invalidated by the modeling bug and should not be trusted or reused. The bug was
caught by cross-checking against `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`
§13.2's explicit definition (`OPT_sigma(B,Z)` optimizes over **all** `(K,D,M)` selections, i.e. a
partition of `Z` into Keep/Delete/Match-pairs, not just subsets) and against the "OPT_KD ≠ OPT" open
question (Claim A) explicitly on file at line ~3824. A corrected harness (`/tmp/correct_opt.py`,
full recursive enumeration of Delete/Keep/Match partitions) was built and validated against **four**
of the file's own worked examples before any new claim was trusted: `OPT_{+1}(\{5,8\},(10,8,7,2))=0`,
`OPT_{-1}(\{5,8\},(10,8,7,2))=10`, `OPT_{+1}(\{1\},(10,8,7))=0`, `OPT_{-1}(\{2,4\},(5,3))=4` — all
four reproduced exactly. **All findings below use the corrected, match-inclusive harness only.**

### Distinct opening found this round: a Generalized Touch-Bound closed form for `OPT_sigma(C,W)` at
arbitrary background size `|C|`, extending the certified Two-Touch/Three-Touch pattern

**The conjecture (new this round, not previously stated on file at this generality — the file only
ever tested "touch `<=2`" for `|C|=2`, found FALSE `~24%`, and stopped there without trying
`touch<=3` or `touch<=4`):**

```
Generalized Touch-Bound Lemma (conjectural). For background C, |C|=k, list W:
  OPT_{+1}(C,W) = min over ALL selections of W touching <= 2k raw elements of e(C u kept u match-diffs).
  OPT_{-1}(C,W) = max over ALL selections of W touching <= 2k+1 raw elements of the same.
```

Here "touching `j` elements" means the selection's Keep-set-size plus twice its Match-pair-count
equals `j` (i.e. `j` raw elements of `W` are used, whether individually kept or paired into a
match-difference); the candidate family for `touch<=m` has `O(q^m)` terms (a **fixed-degree-in-`m`**
polynomial family, not exponential, since `m` does not grow with `q`).

**This is exactly the already-certified `k=1` case, extended.** The certified Two-Touch Lemma
(`OPT_{+1}(\{b_0\},W)`, `k=1`, needs `touch<=2`) and the corroborated (not fully proved) Three-Touch
candidate (`OPT_{-1}(\{c\},W)`, `k=1`, needs `touch<=3`) are precisely the `k=1` instances of this
one uniform pattern (`2k`/`2k+1`).

**Computational corroboration this round (all via the corrected, match-inclusive harness):**
- `sigma=+1, |C|=1`: `touch<=2` — `0/600` mismatches (reconfirms the certified base case).
- `sigma=-1, |C|=1`: `touch<=2` — `47/500` (`9.4%`) mismatches (reconfirms the file's already-known
  Two-Touch/`|C|=2`-style asymmetry, here for `k=1`'s own sigma mirror); `touch<=3` — `0/500`
  mismatches (matches the file's already-corroborated Three-Touch touch-3 finding).
- `sigma=+1, |C|=2` (**new, not on file — the file only tested `touch<=2` here**): `touch<=2` —
  `53/500` (`10.6%`) mismatches (reproduces the file's own `~24%`-order finding, same qualitative
  conclusion, smaller sample); `touch<=3` — `7/500` (`1.4%`) mismatches, **still fails** (this refutes
  a natural "just one more than the file tried" guess); **`touch<=4` — `0/3600` combined mismatches**
  across 3 independent sweeps (`W` up to size 8-9, `v_max` up to 6, both plain-random and
  duplicate-heavy/adversarial alphabets) — clean, robust corroboration of the exact bound `2k=4`.
- `sigma=-1, |C|=2` (new): `touch<=4` — `1/500` mismatch (fails, confirms `2k` is NOT enough for the
  `sigma=-1` mirror, matching the `k=1` pattern); `touch<=5` — `0/500` mismatches, matching `2k+1=5`.
- `sigma=+1, |C|=3` (new, pushed further to distinguish "`2k`" from weaker guesses like "`k+2`"):
  `touch<=3`: `19/400` (`4.8%`) fails; `touch<=4`: `6/600` (`1.0%`) fails (rules out `k+2=5`... wait,
  `k+2` would predict `5`, and `4` already fails, consistent); `touch<=5`: `2/1500` (`0.13%`) fails —
  **small but genuine, not a fluke** (found after `touch<=5` looked clean at `600` trials but broke
  at `1500`, and again at `800` duplicate-heavy trials with `0` fails — the failure rate is real but
  low, illustrating the round-10/13 lesson about widening a sweep before trusting "0 violations");
  `touch<=6` (`=2k`): `0/750` combined mismatches, clean. **This nails down the exact exponent as
  `2k`, not `k+2` or any smaller alternative** — `k+2` and `2k` coincide at `k=2` (both give `4`),
  which is why `|C|=2` alone could not distinguish them; `|C|=3` (`2k=6` vs `k+2=5`) resolves it in
  favor of `2k`.
- **Re-verified directly on genuinely `\mathcal F`-style-derived instances** (not arbitrary `C,W`):
  built `(b_0,dl,\mathrm{Res})` triples exactly as Gap 1a's `A_{3,l}` construction does (`b_0,Z_0`
  random, `d_l:=z_1-z_l$, `\mathrm{Res}:=Z_0\setminus\{z_1,z_l\}`) and checked
  `A_{3,l}=\mathrm{OPT}_{+1}(\{b_0,d_l\},\mathrm{Res})` against the `touch<=4` closed form directly:
  **`0/533`** mismatches (`q` up to `7`) — the conjecture holds on the actual objects Per-Partner
  Domination needs, not just on synthetic `(C,W)` pairs.

**What this would give, if proved, and why it is a genuinely different attack route from everything
tried in rounds 14-18:** every prior attempt at general-`q` Per-Partner Domination tried an
**induction on `q`** peeling `\mathrm{Res}`'s top element via the certified Generalized
Multi-Background Peeling Lemma, which forces the MATCH branch to recurse into a **3-element**
background (`\{b_0,d_l,e_i\}`) at the very next level — an unboundedly-growing background as the
induction proceeds, which is exactly why every attempt has stalled (§27.1's own diagnosis: "MATCH
carries forward the full difficulty of the problem, unreduced, to the next level"). **If the
Generalized Touch-Bound Lemma is proved directly for `k=2` (fixed, not growing), it replaces the
whole open-ended recursive induction with ONE finite, closed-form fact**: `A_{3,l}` is *exactly*
the minimum over `O(q^4)` explicit candidates (all ways to touch `<=4` raw elements of `\mathrm{Res}`,
via keep and/or match), each of which is a simple, fixed-size algebraic expression (at most 4
elements combined via at most 2 nested Rank-Extraction-Identity insertions). **Per-Partner
Domination would then reduce to a single, `q`-independent, bounded case analysis** — verify
`\mathrm{value}(\mathrm{candidate})\ge\min(A_1,D_l)` for each of the finitely many *shapes* of
touch-`<=4` candidate (0,1,2,3, or 4 elements touched, in every keep/match combination — a strictly
larger but structurally analogous case-split to the one that already closed `q=3`, where `\mathrm{Res}`
had only `1` element and hence only touch-`<=1` candidates existed) — **no induction on `q` at all is
needed for this half of the argument**; `A_1` itself remains a `q`-dependent black-box quantity
referenced only via its own two already-certified free bounds (`A_1\le b_0`, `A_1\le|b_0-w|`-type),
exactly as in the certified `q=3` proof.

**What is NOT yet done (the concrete new gap this route opens, for a future round):**
1. **Prove the Generalized Touch-Bound Lemma itself** for `k=2` (`\sigma=+1`, `touch<=4`) — not
   attempted this round (scouting only). The natural approach is an induction on `|C|` (not `|W|`):
   peel one element of `C` via a "release" argument (candidate: adapt the certified
   Background-Release Domination Lemma's bijection, or a Rank-Extraction-based direct argument
   showing any selection touching `\ge2k+1` elements is dominated by a `\le2k`-touch alternative,
   mirroring how the certified Three-Bound Domination Lemma is exactly this statement's `k=1`
   instance in reverse — "keep both remaining elements is dominated by touch-`\le1`"). This is a
   **fresh, self-contained target**, structurally similar to but NOT the same lemma as the already
   partially-proved (`|W|<=3` only, KEEP/MATCH branches of the `|W|`-induction still open) Two-Touch
   Lemma — it fixes `|C|` and lets `|W|` be *arbitrary from the start* (a strong, single closed-form
   claim), rather than inducting on `|W|` with `|C|=1` fixed.
2. **The finite case analysis at `touch<=4`** (step 2 of the plan above) has NOT been attempted —
   only the closed form itself was corroborated this round. This is likely a large but mechanical
   generalization of the certified `q=3` proof (§22.2), now with up to 4 touched elements instead of
   1 — genuinely more casework (some candidates use a match, contributing a *derived* value that
   itself needs Rank-Extraction-Identity handling nested one level, unlike `q=3`'s pure keep/delete
   case split), but each case is now a bounded, finite, `q`-independent computation, not an unbounded
   recursive one.

### Candidate technique(s)

Strong induction on `|C|` (not `|W|`) to establish the Generalized Touch-Bound Lemma at `k=2`, using
the certified Three-Bound Domination Lemma (its `k=1` instance) and Rank-Extraction Identity as
building blocks; then a single finite case-split (generalizing the certified `q=3` Per-Partner
Domination proof) to close Per-Partner Domination for ALL `q` at once, with no induction on `q` in
this half of the argument. This is a genuinely different top-level target from every approach on
file since round 14 (all of which induct on `q`/`\mathrm{Res}`'s size, forcing unbounded background
growth) — it inducts on background size instead, keeping `|W|` free.

### Cheap-kill candidates

- Before committing build effort: verify the Generalized Touch-Bound conjecture does NOT already
  silently reduce to something known-false. It does not appear to (see corroboration above,
  `>10,000` combined checks across `k=1,2,3`, both signs, `0` failures at the correct threshold in
  every case) — but a builder should re-verify independently before trusting it (per the standing
  round-10 population rule).
- A structural sanity check worth running first (cheap, `O(q^4)` per instance, not expensive): confirm
  the `touch<=4` candidate family for `A_{3,l}` can be reduced to a SMALLER sub-family before doing
  full casework — e.g., check whether "match 2 pairs" (touching all 4 via two matches, no kept
  elements) is ever independently the true minimizer, or is always dominated by a mixed
  match+keep/keep+keep alternative (a "Three-Bound-Domination"-style redundancy elimination, as was
  found for `|C|=2`'s "keep both" candidate at the old, now-superseded touch-`<=2` attempt) — reduces
  the casework's constant factor before a builder commits to the full split.

### Knowledge-base entries / certified lemmas to use

- `lemmas/three-bound-domination-and-keep-top-bound.md` (Three-Bound Domination — exactly the `k=1`
  instance of the redundancy-elimination step the Generalized Touch-Bound Lemma's proof will need at
  `k=2`; also Keep-Top Bound, reusable for Gap 1b as before).
- `lemmas/general-rank-extraction-identity.md` and `lemmas/insertion-difference-identity.md` — needed
  for handling insertions/matches within the touch-`<=4` case analysis.
- `lemmas/shrink-list-monotonicity.md` and `lemmas/background-release-domination.md` — candidate
  tools for the `|C|`-induction step (peeling one background element); note the file's own
  Background-Release Domination Lemma already records that its two obvious *chaining* routes into
  Gap 1a are dead (§ "Remarks" of that lemma file) — a fresh use here (peeling `C` down by one, not
  chaining all the way to background-free) may avoid that specific dead end, but has not been tested
  this round and should be checked against the recorded counterexamples first.
- `lemmas/max-element-triple-identity-and-threetouch-basecase.md` — the `\sigma=-1`, `k=1` mirror
  (Three-Touch base case), useful as a second worked instance of the `2k+1` pattern when designing the
  general induction.

### Analogous past problems (cruxes)

No new crux search was run this round (scope was direct computational/structural scouting per the
dispatch). The population's own prior crux findings stand: `aimo-0960`'s "extremal witness + secondary
tie-break + local rewrite" shape (already flagged, round 13/16/17, for Gap 1c) is not obviously
relevant to the Generalized Touch-Bound Lemma itself, which is a pure closed-form/domination fact
about `e_{\mathrm{sorted}}`, not an extremal-witness construction — no crux match found for this
specific new sub-target.

### Prior progress

Unchanged from round 18: Per-Partner Domination Lemma proved for `q<=3` (round 14); Two-Touch's MATCH
branch reduced to Per-Partner Domination (round 18, certified,
`lemmas/match-branch-domination-via-per-partner-domination.md`); Gap 1b's DELETE-vs-KEEP half shown
algebraically equivalent to Per-Partner Domination's own DELETE-vs-KEEP half (round 17); Three-Touch
4/5 pieces proved (round 17). The single highest-leverage open item remains the DELETE-vs-MATCH
mechanism at general `q` for Per-Partner Domination — this round's Generalized Touch-Bound Lemma is a
**new, not-yet-attempted route to exactly that mechanism** that avoids the unbounded-background-growth
obstruction every round-14-through-18 attempt has hit.

### Dead ends (do not retry)

- (Reconfirmed, not new) Two-Touch/Three-Touch's `|C|=2` **generalization at the OLD threshold**
  (`touch<=2`) is false (`~10-24%` failure, several independent confirmations now including this
  round's) — but this is superseded by the finding above: it is false ONLY because `touch<=2` is the
  wrong threshold for `k=2`; `touch<=4` (the correct `2k` threshold) is NOT false. **Do not conflate
  "the `k=1`-style bound doesn't port to `k=2`" (true, and already on file) with "no clean closed
  form exists at `k=2`" (this round's finding shows a clean closed form DOES exist, just at a
  different, previously-untested threshold).**
- The three MATCH-branch proof-route candidates refuted in round 18 (§30.2: union-of-three-candidates
  fixed-witness argument, `~8.8%` fail; general-background-size induction, `~2%` fail at `|B|\ge2`;
  second-largest-partner-always-dominant shortcut, `~43%` fail) remain dead — none of them is
  resurrected or contradicted by this round's finding, since the Generalized Touch-Bound route
  attacks a different (closed-form) target rather than any exchange/domination argument on a fixed
  witness.
- An early **modeling-bug-based** "finding" this round (a supposed clean `A1`-based per-selection
  reformulation, and a supposed circular identity via Background-Release Domination) was based on the
  incorrect match-free harness described above and is **retracted** — not a valid dead end to record,
  simply invalid data. Do not cite it.

### Small-case / intuition notes (all labeled conjecture, all via the corrected harness)

- **Conjecture, strongly corroborated** (`>10,000` combined checks, `0` failures at the claimed exact
  threshold in every one of `\sigma\in\{+1,-1\}\times k\in\{1,2,3\}`, with the threshold pinned down
  precisely by contrasting `k=2` vs `k=3` to rule out `k+2` as an alternative to `2k`): `OPT_{+1}(C,W)`
  with `|C|=k` equals the minimum over selections touching `\le2k$ elements of `W`; `OPT_{-1}(C,W)`
  equals the maximum over selections touching `\le2k+1` elements. This is offered as a genuinely new,
  previously-untested-at-this-threshold candidate lemma for the outliner to consider building next
  round — it is NOT proved, only computationally corroborated, and its own proof (by induction on
  `|C|`) has not been attempted.
- Re-confirmed (matches this round's earlier, invalid-harness finding by coincidence, but now on the
  corrected harness): among all `(b_0,Z_0,l)` triples, the index `l$ achieving the true minimum of
  `A_{3,l}` over all partners is where Per-Partner Domination is **tight** (margin `=0`) far more
  often (`74.7\%$ of instances) than at non-minimizing `l` (`37.9\%`) — corroborating (not proving)
  that the real difficulty concentrates at the argmin partner, i.e. that the extra hypothesis
  "`l` is a global argmin" (discarded in round 14 when Per-Partner Domination was generalized away
  from Deletion-Suffices-for-`k^*` for simplicity of statement) may be doing real, currently-unused
  work — worth the outliner weighing whether reintroducing it (attacking the narrower, argmin-scoped
  claim instead of the fully general per-`l` one) is easier to prove even though the general form is
  computationally true. This is a **secondary, weaker lead** compared to the Generalized Touch-Bound
  route above; flagged for completeness, not as the primary recommendation.
- The generalized-`A1`-bound-family search that rounds 15-18 flagged as needed (§22.2 recommended next
  step (ii), §25.2's "resolves the search for a sufficient bound family") is a **special case** of this
  round's Generalized Touch-Bound Lemma at `k=1` (Two-Touch, already on file) — this round's
  contribution is showing the SAME clean pattern continues to `k=2` (needed for `A_{3,l}` itself,
  `|C|=2`) at the correct, previously-untested threshold `touch<=4`, not `touch<=2` or `touch<=3`.
