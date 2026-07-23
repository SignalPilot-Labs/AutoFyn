## imo-2026-03

### Assigned lens
The generalized `A_1`-bound family needed to close Gap 1a's DELETE/KEEP/MATCH branches for
general `q>=4` (and, per round 15, also Gap 1c's half-step lemma via the shared mechanism).

### Headline finding — a strong new candidate: the Single-Background Two-Touch Lemma

**Conjecture (new this round, NOT yet proved, but exhaustively/adversarially corroborated —
this is a *characterization*, not merely a bound):**
```
For ANY single background value b0 (|C|=1) and ANY finite list W of nonnegative reals,
  OPT_{+1}({b0}, W)  =  min( e({b0}),                              [delete all of W]
                              min_{w in W} e({b0,w}),               [keep exactly one]
                              min_{i<j in W} e({b0, |w_i-w_j|}) )   [match exactly one pair, delete rest]
```
i.e. the true `\sigma=+1` optimum with a **single** background element is *always* achieved by a
selection that touches (keeps or matches) **at most 2** elements of `W` — never needs to keep 2+
elements together untouched-by-a-match, never needs 2+ simultaneous matched pairs, and never
needs a "keep-1-and-match-1" 3-touch combo, no matter how large `|W|` is or how adversarially the
values are chosen (near-duplicates, chained telescoping alphabets, etc.).

**Why this matters directly for the assigned gap.** `A_1 := OPT_{+1}(\{b_0\}, \mathrm{rest})` in
`potential-weighting-upper-bound.md`'s Gap 1a machinery is *exactly* an instance of this (`|C|=1`,
`W=\mathrm{rest}=Z_0\setminus\{z_1\}`, arbitrary size `q-1`). If this lemma is proved, it gives an
**exact, closed-form** value for `A_1` at ANY `q` — turning the "generalized `A_1`-bound family"
that rounds 14-15 have been searching for from an open-ended search into one clean, explicit,
`O(q^2)`-term formula. This is a strictly stronger deliverable than "a bound that happens to
suffice" — it is the tightest possible bound (equality).

### Computational verification performed this round (own fresh code, `/tmp/round-16/work/`,
validated against the file's 4 worked examples first, all reproduced exactly)

1. **Root-cause reproduction of round 15's `q=4` MATCH-branch failure (439/62,580 ≈0.7%).**
   Traced the failing worked example type by hand: `b0=1, zl=2(=z1, a duplicate!), u1=3/2, u2=1/2`
   gives `A_1=0`, achieved by **matching `u1` and `u2`** (`|u1-u2|=1`, combined with `b0=1` gives
   `e_sorted(\{1,1\})=0` via the certified duplicate-pair cancellation, Lemma P) — a selection type
   completely absent from the naive 3-bound family `\{b_0,|b_0-u_1|,|b_0-u_2|\}` used in round 15's
   §24.2. This is the precise internal-duplicate-cancellation mechanism round 15 diagnosed but did
   not yet resolve.
2. **Ablation at `q=4` (27,000 fresh `(b_0,z_1,z_l,u_1,u_2)` checks, `0` true-lemma violations
   throughout — Per-Partner Domination itself always held):**
   - Naive 3-bound family: `147/27{,}000` (0.54%) family-certification failures (reproduces round
     15's finding at a different sample size/seed).
   - Adding `|b_0-z_l|` (the "missing" 4th delete-all-but-one bound, an oversight in round 15's
     naive family which only used `\mathrm{Res}`'s own elements, not `z_l`): **negligible fix**,
     `158/27{,}000` — barely moves the needle, so this was NOT the missing piece.
   - Adding **only** `e(\{b_0,|u_1-u_2|\})` (match Res's own two elements, delete `z_l`): **`0/27{,}000`**
     — a single new bound completely closes the `q=4` gap. Adding `|z_l-u_1|`- or `|z_l-u_2|`-type
     match bounds alone does NOT fully close it (149/27,000 and 66/27,000 respectively) — the
     specific missing piece is the match of `\mathrm{Res}`'s own top-two elements.
3. **General-`q` extension (this is the load-bearing new result): the "ALL PAIRS of `\mathrm{Res}`"
   family (not just the top-two, and not just "top vs. all") closes the gap cleanly through every
   `q` tested:**
   - `q=5` (`|\mathrm{Res}|=3`, 3 pairs): naive family 2.6% failures; "top-2-of-Res only" 1.4%
     (insufficient); **all `C(3,2)=3` pairs: `0/8000`.**
   - `q=6` (`|\mathrm{Res}|=4`, 6 pairs): naive 4.0%; top-2-only 2.7% (insufficient); **all pairs:
     `0/5000`.**
   - `q=7` (`|\mathrm{Res}|=5`, 10 pairs): "top-vs-all" (`O(q)` pairs, cheaper) still **insufficient**
     (1.1% failures); **all `C(5,2)=10` pairs: `0/1800`.** This rules out an `O(q)`-sized family —
     genuinely need the full `O(q^2)` pairwise family, not a cheaper linear-sized subset.
4. **Direct test of the general Two-Touch conjecture (dropping the Gap-1a framing entirely, testing
   `OPT_{+1}(\{b_0\},W)` against the touch-`<=2` formula directly, for arbitrary `b_0,W`):**
   - Random, `|W|\in\{2,\dots,5\}`, mixed alphabets: `0/6000`.
   - **Exhaustive** small-alphabet sweep, `|W|\le4`, values in `\{0,1,2,3\}`: **`0/1344`**, zero
     mismatches, no case omitted.
   - **Exhaustive**, `|W|=5`, values in `\{0,1,2\}`: **`0/729`**.
   - Random, `|W|\in\{6,7\}`: `0/1500`.
   - Adversarial duplicate/near-tie-heavy sweep (values drawn from small repeated pools designed to
     trigger deep telescoping/chained cancellation), `|W|\in\{3,\dots,8\}`: **`0/4400`**, including a
     deliberately constructed "deep chain" attempt (`u_1=9,u_2=5,u_3=4,u_4=3` designed so a 3-way
     interaction might be needed) that turned out to still be captured by a single pair.
   - **Total across all batteries: 0 violations in ~13,800+ combined checks, spanning random,
     exhaustive, and deliberately adversarial regimes.** This is a genuinely strong corroboration,
     stronger than a single random sweep — but it is NOT a proof.
5. **Boundary/negative check (important, tells you where NOT to expect the same trick): the
   analogous "Two-Touch" claim is FALSE once `|C|=2`** (i.e. it does NOT directly give a similarly
   clean closed form for `A_{3,l}` itself, only for `A_1`). Tested `OPT_{+1}(C,W)` with `|C|=2`
   against "touch `<=2` of `W`" (delete-all/keep-1/match-1-pair, background now 2 fixed points):
   **`962/4000` (24%) violations** — concrete witness `C=\{5/2,5\}, W=(1,9/2,0,5/2,5)`: true value
   `0`, "touch `<=2`" formula gives `5/2`. **Do not attempt to extend the Two-Touch mechanism to
   `A_{3,l}` directly (`|C|=2`) — it needs strictly more touches there; this is a genuine boundary,
   not a bug.** (Consistent with, and possibly explaining, why `q=4`'s Per-Partner Domination proof
   needed real casework even after the `A_1` side is fully closed — `A_{3,l}`'s own structure is
   intrinsically richer once background size is `2`.)

### A concrete, promising proof-strategy pointer for the Two-Touch Lemma (an opening, not a
proof — flagged for the outliner, not developed further per my role)

The already-**certified** Three-Bound Domination Lemma (`lemmas/three-bound-domination-and-keep-top-bound.md`)
is *exactly* the `|W|=2` instance of this conjecture stated as an inequality
(`min(x,|x-y|,|x-z|) <= e_sorted(\{x,y,z\})`, i.e. "keep both remaining elements is dominated by
touch-`<=1`"). This strongly suggests the Two-Touch Lemma is provable by **induction on `|W|`**,
using the certified Generalized Multi-Background Peeling Lemma's own DELETE/KEEP/MATCH trichotomy
to peel `W`'s top element, and repeatedly invoking Three-Bound-Domination-style triple collapses
to show any selection touching `k\ge3` elements is always dominated by a strictly-fewer-touch
alternative — i.e. the same case-split machinery that already closed `q=3`'s Per-Partner Domination
proof (§22.2) and the Three-Bound Domination Lemma itself, one level of induction further. This
looks like the natural next attempt, not a new mechanism.

### Additional check: branch-by-branch confirmation at `q=5,6`

Beyond the aggregate family-certification check in finding 3, I re-ran the check split explicitly
by which of `A_{3,l}`'s own DELETE/KEEP/MATCH branches (peeling `\mathrm{Res}`'s own top element
`u_1`) is being certified, using the exact Two-Touch-conjectured `A_1` formula as the certifying
bound (`family_min(b_0,\mathrm{Res})`, re-verified `==` the true brute-force `A_1` in every single
trial, an inline assertion that never failed): **`q=5` (2400 checks) and `q=6` (900 checks): `0`
failures in ALL THREE branches (`DEL`, `KEEP`, `MATCH`) simultaneously** — confirms that, with the
enriched all-pairs family in hand, not just the previously-flagged MATCH branch but the whole
Per-Partner Domination target closes cleanly at `q=5,6`, consistent with (and extending) round 15's
finding that DEL/KEEP were already free at `q=4`.

### What this does and does NOT close

- **Gives:** an exact, general, `q`-independent formula for `A_1` (IF proved), immediately supplying
  the correct "generalized `A_1`-bound family" for Gap 1a's DELETE/KEEP/MATCH branches at every
  `q\ge4` — this was precisely the item flagged as open in round 15's §24.2/§23.4 item 4.
- **Does NOT (by itself) close** the Per-Partner Domination Lemma's own general-`q` induction — even
  with an exact `A_1` formula in hand, the DELETE/KEEP/MATCH branches of `A_{3,l}$'s own recursive
  peeling (over `\mathrm{Res}`, `q-2` elements) still need their own case analysis (as `q=3`'s proof,
  §22.2, already does) to show `A_{3,l}\ge\min(A_1,D_l)`; what changes is that `A_1` is no longer an
  opaque quantity needing an ad hoc bound family — it is now a fully explicit, hand-computable
  expression to plug into that case analysis.
- **Does NOT close Gap 1c's half-step lemma directly** — that claim (`OPT_{+1}(C\cup\{d\},X)\ge
  OPT_{+1}(C,X)`) has `|C|\ge2$ (it operates on `B_1=\{b_0,d_{k^*}\}` or deeper), exactly the regime
  where finding 5 above shows the simple Two-Touch mechanism does NOT hold — so the shared mechanism
  round 15 identified between Gap 1a and Gap 1c should NOT be expected to close via this same trick;
  it needs its own (still open) argument. This is a useful negative delimiter: the shared mechanism
  is real (round 15's finding stands), but this round's new lemma is a `|C|=1`-specific tool that
  helps ONE side (the `A_1`-bound family for DELETE/KEEP/MATCH) without touching the other
  (`|C|\ge2` half-step).

### Candidate technique(s)
- Strong induction on `|W|` for the Two-Touch Lemma, via repeated application of the already-
  certified Three-Bound Domination Lemma to interior triples (peel-and-collapse), likely combined
  with the Generalized Multi-Background Peeling Lemma's own DELETE/KEEP/MATCH trichotomy and the
  General Rank-Extraction Identity (for handling where an inserted/matched value lands relative to
  `b_0` and the rest).
- Once the Two-Touch Lemma is available, Gap 1a's general-`q` induction (§22.2's recommended next
  step) should attempt the induction on `q` with `A_1` now treated as this explicit `O(q^2)`-term
  minimum rather than an opaque recursive quantity — likely simplifies the DELETE/KEEP branches
  significantly and gives a mechanical way to construct the MATCH-branch bound at every `q`.

### Cheap-kill candidates
- The "top-vs-all" `O(q)`-sized pairwise family is a cheap-kill that FAILS (1.1%-2.7% failures at
  `q=5,6,7`) — do not propose it as a cheaper substitute for the full `O(q^2)` all-pairs family;
  confirmed by direct test, not assumption.
- `|C|=2` Two-Touch is a cheap-kill that FAILS (24% violations) — do not attempt to reuse the `A_1`
  mechanism verbatim for `A_{3,l}` or the half-step lemma.
- Adding just `|b_0-z_l|` to the naive family is a cheap-kill that barely helps (0.54%->0.59% in one
  ablation direction, i.e. no real effect) — the missing piece is specifically a MATCH-type bound,
  not another delete-all-but-one bound.

### Knowledge-base entries / lemma files used
- `lemmas/three-bound-domination-and-keep-top-bound.md` (Three-Bound Domination Lemma — the `|W|=2`
  base case of, and probable induction engine for, the new Two-Touch conjecture).
- `lemmas/shrink-list-monotonicity.md` (used implicitly: `A_1 <= OPT_{+1}(\{b_0\},S)` for any
  `S\subseteq\mathrm{rest}` is a direct, already-certified, one-line consequence of this lemma —
  it's exactly what licenses treating any subset-restricted quantity as a valid upper bound on `A_1`
  in the first place, before the new Two-Touch finding shows which subsets actually matter).
- `lemmas/general-rank-extraction-identity.md`, `lemmas/insertion-and-cascade-facts.md` (Facts 3-5,
  likely useful for a future induction proof of Two-Touch — block extraction / single-insertion
  bound machinery matches the shape of the needed argument).
- `lemmas/duplicate-pair-invariance.md` (Lemma P) — the underlying mechanism of the internal-
  cancellation failure mode itself (the `q=4` failing example is literally a duplicate-pair
  cancellation, `e_sorted(\{1,1\})=0`).

### Analogous past problems (crux corpus)
Did not run a fresh crux-corpus query this round — the dispatch's lens is narrowly computational
(find/test a stronger `A_1` bound family), and round 13's prior crux search
(`crux_moves_documentation.md`-informed) already established no closer subject-matter match exists
for this problem's bespoke background-carrying alternating-sum recursion than the "extremal witness
+ secondary tie-break + local rewrite" shape (aimo-0960/aimo-0438/aimo-0666, recorded in
`potential-weighting-upper-bound.md` §19.3). Nothing in this round's findings changes that
assessment or suggests a new crux match — the Two-Touch Lemma is an internally-generated structural
fact about the `e_sorted` function, not a technique transfer.

### Prior progress
See `results/imo-2026-03/current.md` and `potential-weighting-upper-bound.md` §17-§24 (context
given in dispatch) — Per-Partner Domination Lemma proved for `q<=3`; `q=4` DELETE/KEEP free with
the naive family, MATCH branch was the open ~0.7% gap (now closed computationally by this round's
new single bound, `A_1<=e(\{b_0,|u_1-u_2|\})`, pending proof of the Two-Touch Lemma or at minimum a
direct proof of this specific instance).

### Dead ends (do not retry)
- `|C|=2` (or deeper) analogue of the Two-Touch Lemma (this round, 24% failures) — do not port this
  mechanism to `A_{3,l}` or the half-step lemma without a genuinely different argument.
- `O(q)`-sized "top-vs-all" pairwise family as a cheaper substitute for full `O(q^2)` all-pairs (this
  round, 1.1%-2.7% failures at q=5-7) — the full pairwise family is necessary, not just sufficient-
  and-convenient.
- Adding `|b_0-z_l|` alone to the naive `q=4` family (this round, negligible effect) — the gap is
  specifically about MATCH-type bounds, not more delete-type bounds.

### Small-case / intuition notes (all conjectural, computational evidence only, not proofs)
- The Single-Background Two-Touch Lemma is conjectured to be TRUE for all `q`/`|W|`, based on
  exhaustive verification through `|W|=5` (small alphabet) and extensive random/adversarial coverage
  through `|W|=8` — no counterexample found despite deliberate adversarial construction attempts
  (duplicate-heavy, chained-telescoping alphabets).
- The natural generalization to `|C|=2` is FALSE — background size genuinely changes how many
  elements must be "touched" for optimality; whatever the true pattern is for `|C|=2` (untested this
  round beyond the single negative check — a natural next question is whether `|C|=2` needs a
  "Three-Touch" analogue, untested), it is qualitatively different from `|C|=1`, not a simple
  generalization.
