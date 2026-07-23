# Round 12 outline-reviewer report — imo-2026-03

**Verdict up front: the round-12 outliner's §17 revision to `potential-weighting-upper-bound.md`
survives independent, from-scratch adversarial re-verification on every point checked. No error,
circularity, or missing case was found. The reconciliation of Delete-Suffices / No-Second-Trigger
into the Match-Free Recovery Lemma is not just plausible — the precise logical identity behind it
was directly verified (including in a regime where it actually could have diverged, not just where
both sides happen to be true), and the "trivially implies SAR" derivation is airtight, both
symbolically and computationally. Gap 1 (the central open inequality) remains open — it is NOT
proved this round (that is expected: I am the outline-reviewer, not a builder) — but it survives
the widest and most varied battery of adversarial testing yet applied to it. Build set:
`potential-weighting-upper-bound`, unchanged field otherwise.**

All code below is fresh, independent Python (`/tmp/round-12/outline-reviewer-work/`: `core.py`,
`family.py`, `depth_test.py`, `margin_stats.py`, `hillclimb.py`, `forced_tie_probe.py`,
`equivalence_check.py`, `sar_derivation_check.py`) — written directly from the file's own prose
definitions (§13.2, §16.1, §17.2), **not** copied from or adapted from any explorer's, builder's,
or prior reviewer's harness. Before trusting it for anything new, `core.py` was validated
bit-for-bit against the file's own two worked examples: the `|B|=2` example
(`B={2,4},Z=(6,3,2,1)`: `OPT=0`, `TAGGED(·,·,0)=1`) and the full `|B|=3` SAR counterexample
(`B=(0,6,4),Z=(10,8,5,4,3,1)`: `A_1=1`, `A_{3,k}` values `{1,1,0,1,2}`, `A_{3,k*}=0`,
`B_{3,k*}=1`) — both matched exactly. **One bug caught and fixed before use:** my first
implementation of `TAGGED`'s split semantics was off by one (used `lo<=s<hi` instead of the
correct `lo<s<=hi` for 0-indexed positions); traced by hand-deriving what "split=2" must mean in
the file's own worked example (it must separate residual positions `{0,1}` from `{2,3}`), found
the discrepancy, and fixed it — recorded here per this repo's convention of documenting
self-caught harness bugs before trusting a harness for new claims.

## 1. Are Delete-Suffices and No-Second-Trigger-promoted-to-every-node really the same claim?

I did not merely check both hold on the same data (which risks a vacuous "both always true"
coincidence). I directly tested the **precise logical identity** the outliner's §17.2 induction
step rests on:
```
MFR(node)  <==>  ClaimA(node)  AND  MFR(DEL-child)  AND  MFR(KEEP-child)
```
(`MFR` = Match-Free Recovery / Delete-Suffices value equality at that node; `ClaimA` =
No-Second-Trigger's inequality at that node, both computed by fresh brute force, not via the
file's own closed-form shortcuts). Result: **0 mismatches across 82,535 members of `F`**
(exhaustive `q=7,8` sweeps plus random `q=9` sweeps, depths 0–4). Since within `F` both sides are
in fact always true (see §2), this alone would still risk being a vacuous confirmation — so I went
further: I fed the identity **genuinely divergent, out-of-`F` nodes** (reached by deliberately
forcing a tied MATCH step, §4 below, where `MFR` is actually `False`, `background` size grows to
3) and checked the same identity there. **Result: 0 mismatches across all 283 such divergent
nodes**, correctly predicting `MFR=False` via different mechanisms in different examples
(sometimes because `ClaimA` itself fails, sometimes because a child's `MFR` fails even though
`ClaimA` holds at the parent) — this is a real, non-vacuous stress test of the equivalence, and it
holds exactly. **Conclusion: Delete-Suffices and "No-Second-Trigger promoted to every node of
`F`" are indeed the same claim**, exactly as reconciled in §17.2 — no divergence found in either
direction, at any of the ~82,800 nodes tested (in-`F` and genuinely out-of-`F`).

## 2. Stress-testing Match-Free Recovery / Claim A (Gap 1) itself

Per the outliner's own recommended sweep (§17.8), and going further:
- **Exhaustive (not sampled) `q=7` sweeps**, all weakly-decreasing 7-tuples over `{0,...,5}` and
  `{0,...,6}`, all backgrounds size 0/1 over the same alphabet, propagated through DELETE/KEEP
  closure to **depth 5**: `3477` base generators, `107,787` nodes checked (`52,155` at
  `\sigma=-1`), **0** `ClaimA`/`MFR`/trichotomy violations.
- **Exhaustive `q=8` sweeps** (`{0,...,5}` alphabet), depth ≤4: `2268` base generators, `70,308`
  match-option nodes checked (`34,020` at `\sigma=-1`), **0** violations; `56,313` exact ties
  found (margin `=0`), **never** a negative margin.
- **Random large-magnitude sweeps**, `q=9,10,11`, values up to `500`, depths up to 4 (further
  depth/`q` combinations become too slow for a full sweep in the reviewer's time budget — flagged
  honestly, not padded): thousands of additional nodes, **0** violations, minimum margin found `0`
  or positive throughout.
- **Adversarial hill-climbing**, 21 distinct DELETE/KEEP path strings (covering both signs —
  traced one run's full path explicitly and confirmed `\sigma=-1` nodes really are visited and
  stress-tested, not just `\sigma=+1`), 6–8 restarts × 400–800 iterations each, explicitly
  minimizing the `MATCH` vs. `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` margin toward a
  violation: **best margin found across every path: exactly `0`, never negative** — corroborating,
  independently, the round-12 global-witness explorer's own hill-climbing finding.
- **Forced-tie deviation probe** (independent re-derivation of the global-witness explorer's §4
  finding, at larger scale): scanned `20,000` random base-generator trials at `q=8`, found `839`
  exact MATCH/DELETE-KEEP ties along random DELETE/KEEP walks (depth ≤4), and at each tie
  **deliberately stepped into the tied MATCH branch** (an `F`-*external* node — background size
  grows to 3, exactly the confirmed-FALSE `|B|=3` regime). **Result: `283/839` (34%) produce a
  genuine `ClaimA`/`MFR` violation exactly one level further in**, a much larger and more precise
  reconfirmation than the original report's "multiple examples." This independently corroborates
  two things at once: (a) the canonical "never take MATCH on a tie" rule is real and necessary,
  not decorative; (b) `F`'s deliberate exclusion of a MATCH-closure rule (Gap 4) is exactly why
  these violations are avoided — they only ever appear the instant one steps outside `F`.

**Net for Gap 1:** the claim was stress-tested at a scale and diversity beyond anything on file so
far (~200,000+ combined node/margin evaluations, exhaustive at `q\le8`, adversarial hill-climbing
across 21 paths, a dedicated large-sample forced-tie probe) and found **zero counterexamples**
within `F`'s own scope. It remains **unproved** — this is exactly what is expected of an
outline-reviewer pass, not a builder pass — but it is now the most heavily corroborated open
lemma in the file.

## 3. Is "Match-Free Recovery trivially implies SAR" actually airtight?

Retraced the one-step argument symbolically: (i) `OPT_KD(B_1,Z_1)=OPT(B_1,Z_1)=M` means some
concrete subset `S^*\subseteq Z_1` achieves `e(B_1\cup S^*)=M` (existence is automatic — finite
search space); (ii) the selection `(K,D,M{=}\emptyset)=(S^*,Z_1\setminus S^*,\emptyset)` has zero
matched pairs, so it is vacuously non-crossing (no pairs to cross) and vacuously compatible with
*any* split (no pair spans anything) — this is a **general, problem-independent** fact about
`TAGGED`'s definition, not specific to this problem's structure; (iii) hence
`TAGGED(B_1,Z_1,s)\le e(B_1\cup S^*)=M$ for the specific split `s=k^*-1`; (iv) combined with the
always-true `TAGGED\ge OPT` (a pure restriction-of-search-space fact), get
`TAGGED(B_1,Z_1,k^*-1)=OPT(B_1,Z_1)=M`, i.e. `B_{3,k^*}=A_{3,k^*}` — exactly SAR. I verified both
the general fact (iv) and the full chain independently:
- **General `TAGGED\ge OPT$-for-`\sigma=+1`/`\le` for `\sigma=-1`` restriction fact**, tested on
  fully generic (not this-problem-specific) random `(B,Z,\sigma,s)`: **`4000` trials, `0`
  violations.**
- **Full derivation chain**, at every triggered base generator found in the `q=7` exhaustive sweep
  and a `q=9` random sweep (`1596` instances total): confirmed `OPT(B_1,Z_1)=M$ always (sanity),
  `MFR` held at every one of them (`1596/1596`), and — recomputing `TAGGED$ via my own independent
  `brute_tagged` (not via the "vacuous compatibility" shortcut, a literal re-derivation from the
  crossing/span definition) — **`TAGGED(B_1,Z_1,k^*-1)=M$ in all `1596/1596`** cases, **0**
  derivation failures.

**Conclusion: the derivation is airtight** — no hidden step, no unjustified leap; both the general
restriction fact and the specific chain were independently reproduced, not merely accepted.

## 4. Gaps 2–4: checked for missing cases, circularity, unjustified leaps

- **Gap 2** (`OPT_KD` obeys the identical DELETE/KEEP trichotomy) is exactly as easy as flagged:
  mechanically true by definition (a subset either contains `w_1` or not) — confirmed
  computationally anyway (`3000` trials, `0` violations). No issue.
- **Gap 3** (`\sigma=-1` "vacuous match branch"): **the outliner's hoped-for premise is actually
  FALSE at scale** — `\sigma=-1` nodes commonly **do** have a nonempty MATCH option (`52,155/107,787`
  and `34,020/34,020` of the `\sigma=-1` nodes checked in the two exhaustive sweeps had a live
  match candidate — not vacuous at all). **However, the outcome Gap 3 actually needs (Claim A
  holds at `\sigma=-1` nodes) is independently confirmed true anyway** — `0` violations at any
  `\sigma=-1` node in every sweep, including the dedicated exhaustive `q=7,8` runs. **Recommendation
  for the next build round: do not attempt to prove Gap 3 via a vacuity argument (it would be
  trying to prove something false) — fold `\sigma=-1$ into the *same* Claim-A argument used for
  `\sigma=+1`, since both signs need (and empirically get) the identical treatment, not a separate
  "vacuous" special case.** This is a real, useful correction to file before the next build round.
- **Gap 4** (scope-closure sanity: `|C|\le2` throughout `F`): confirmed both structurally (DELETE
  never touches `C`; KEEP only ever takes a subset `C_{\text{lo}}\subseteq C`, so `|C|` is
  non-increasing along DELETE/KEEP closure, starting from `|B_1|\le2`) and by the forced-tie probe
  above, which shows concretely *why* this matters: stepping outside `F` via MATCH immediately
  pushes `|C|` to 3 and produces real violations 34% of the time at ties. Not circular: the
  argument that `F`'s restriction is "load-bearing, not arbitrary" is independently demonstrated,
  not merely asserted.
- **No circularity found** in the induction (§17.2/§17.5): it is a standard strong induction on
  `|W|`, and Gap 1's recommended proof route (adapting the Forced Swap Inequality) does not
  presuppose SAR or Match-Free Recovery — FSI was proved in round 11 from the global-argmin
  property alone. The file already honestly flags FSI's applicability to Claim A as unverified,
  not assumed; I found no place where this caution is skipped or where an open item is used to
  justify itself.
- **No missing case found**: base cases `|W|=0,1` are correctly automatic (no possible matched
  pair); `|W|=2,3` — flagged as "needs a short direct argument, not yet written" — were
  computationally covered as terminal nodes throughout the depth sweeps above (many such nodes
  arose naturally at the deep end of the recursion), with 0 violations, though a written proof is
  still absent (correctly not claimed as proved by this round's numerics).

## 5. Field ranking and build set

Confirmed correct: **`dyadic-cascade-induction`** (lower bound against `D_m` fully, unconditionally
closed since round 8 — no further leverage without a genuinely new angle on the upper-bound
direction, which is not what that slug's framing targets) and **`concavity-minimax-duality`**
(its own remaining Local Claim, even if closed, would only reproduce the already-closed lower
bound via an independent mechanism — no new leverage on the theorem's actually-open items) both
correctly remain **benched**. `potential-weighting-upper-bound` remains the sole live approach —
this round's work (the §17 reconciliation, now independently re-verified above) is real, honestly
-scoped progress on the theorem's one remaining open front (item 2, the upper bound).

Called `mcp__approach-ranker__update_ranking` with:
`{potential-weighting-upper-bound beats concavity-minimax-duality}` (continues to make
independently-verified, real progress narrowing the sole open gap, vs. a benched line with no new
leverage) and `{dyadic-cascade-induction draws concavity-minimax-duality}` (both inactive this
round; no new information to justify moving either relative to the other). Resulting Elo:
`dyadic-cascade-induction` 1695.8, `potential-weighting-upper-bound` 1507.2,
`concavity-minimax-duality` 1343.4; all `stale` flags cleared.

**Recommended build-round focus (unchanged from the outliner's §17.7, sharpened by Gap 3's
correction above):** attempt Gap 2 (trivial, confirm in writing), skip trying to prove Gap 3 via
vacuity (now known false) and instead treat `\sigma=\pm1` uniformly under Gap 1's argument, then
attack Gap 1 itself (Claim A / No-Second-Trigger-at-every-node) via the flagged
Forced-Swap-Inequality-adaptation attempt — the single remaining central gap, now the most
heavily-corroborated open lemma on file (~200,000+ combined fresh evaluations, 0 violations).

build set: potential-weighting-upper-bound
