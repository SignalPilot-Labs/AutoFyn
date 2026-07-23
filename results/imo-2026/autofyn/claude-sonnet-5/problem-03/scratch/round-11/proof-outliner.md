# proof-outliner report — round 11, imo-2026-03

## Ranking state consulted
`mcp__approach-ranker__sample_approaches` (k=4, all 4 approaches on file):
- `dyadic-cascade-induction` — Elo 1706.2, last_outcome `verified-milestone` (round 8, lower bound
  vs `D_m` fully closed for every `m`). No new task from this round's explorers; stays as-is.
- `elementary-exchange-smoothing` — Elo 1487.3, formally retired since round 4 (merged into
  `lemmas/vertex-lemma.md`). No dispatch.
- `potential-weighting-upper-bound` — Elo 1479.5, last_outcome `advanced` (round 9). **Revised
  this round — see below.**
- `concavity-minimax-duality` — Elo 1327.0, last_outcome `partial` (round 9). No new task; stays
  benched per its own honest scope note (even full closure gives no new leverage beyond the
  already-closed lower bound).

## What I did
Read `current.md`, all 4 approach files in full (or in the relevant sections — full read for
`potential-weighting-upper-bound.md`, targeted for the other three), all 18 certified lemma files
by name/index, and all 3 round-11 explorer reports in full. Revised
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` in place with a prepended
round-11 Status note, a new "Approaches tried" bullet, and a new `### 15.` section (5 subsections)
appended after `### 14.`.

## Key decision 1 — §14 is now doubly dead (confirmed from the charging explorer's own §1 sanity
check, not taken on faith)
The charging explorer's report opens with a reproduction check of "the Fixed-Support Uncrossing
Conjecture's dead end": `Y=(7,5,4,4,3,1), p=6, b=5`. `OPT(Y,5)=NC(Y,5)=0`, but among the 30
optimal selections, one has a crossing matching whose same-support non-crossing re-pairing
strictly *increases* the value (`0→2`) — a direct violation of §14's own literal statement ("for
ANY OPT-achieving selection with a crossing M, re-pairing the SAME support achieves `v(K,D,M')≤
v(K,D,M)`"). Recovery instead comes from a *different* optimal selection entirely
(`K={2,3},D={0,1,4,5}`, no match) — the identical "existential-support, not positional" failure
mode §13.6 already diagnosed for the flat-background Match-Recovery Lemma. I recorded this in full
in new §15.1, with the diagnosis that both dead routes (§13.6's flat background, §14's fixed
support) fail for the *same* structural reason: neither can express "the recovering witness may
live on a different support/background-history than the one being repaired." This is the reasoning
the orchestrator's dispatch flagged ("superseding the now-doubly-dead §14 material") — I
independently re-derived and confirmed it from the explorer's own computation rather than just
copying the framing.

## Key decision 2 — folded in the Refined Delete-Recovery Conjecture as the next build task (§15.4)
Restated it precisely against this file's own established §13.2/§13.3 notation (`A_1,A_2,A_{3,k}`
unrestricted branches; `B_1,B_2,B_{3,k}` tagged branches; `M_opt,M_tag` the match aggregates),
confirmed the two-case induction skeleton actually closes the whole remaining gap using only
already-certified tools (IH + §13.2's DELETE/KEEP closed forms for the trivial case; the new
conjecture only for the case where MATCH strictly beats *both* DELETE and KEEP) — and flagged that
the conjecture's own hypothesis (`M_opt<A_1` alone) is deliberately broader/weaker than what the
induction strictly needs (`M_opt<min(A_1,A_2)`), which is why it stress-tests cleanly as a
self-contained claim. Recorded the ~10,000+ trial computational support (random q=4..8, exhaustive
q=4..6), the honest scope caveats (no proof mechanism attempted yet; sizes still small; the
σ=-1/|B|=0 "vacuous match branch" observations are sampled only), and the recommended build order
(counterexample-hunt first, then attempt via Rank-Extraction Identity/Fact 3, then the cheap
σ=-1/|B|=0 checks). This supersedes §14 as the file's live route while explicitly not deleting §14
itself (kept as a permanent, precisely-diagnosed dead end per CLAUDE.md's "record everything"
rule).

## Key decision 3 — Hall's theorem dead end and fresh-framing collapse recorded (§15.2, §15.3)
Both written up with the specific structural reasons (not just "didn't work"): Hall's theorem is
inapplicable because the gap is a single-existential value/optimality question in a globally
rank-coupled objective, not a separable multi-way existence question (existence of a non-crossing
completion is always trivially true, 0/2000+ failures — there is no Hall-deficient set even in
principle). The three fresh framings (concavity/KKT — re-confirmed dead, extends the round-3
certified counterexample to m=3; layer-cake toggle-pair — verified but isomorphic to Lemma-P/D-M;
merge-tree/Euclidean — collapses into already-falsified Rule 1/2 policies) are recorded with the
explorer's own reasoning for why each is either already-dead or isomorphic, so no future round
re-opens any of them in a dressed-up form.

## Key decision 4 — aimo-0198 averaging idea: queued as a note, NOT dispatched
The fresh-framing explorer flagged this (crux `aimo-0198`, IMO 2012 P3's `min(A,B)≤(A+B)/2`
averaging device) as a genuinely different *technique* — but explicitly reported it ran out of
budget before running even a single numerical test. There is no confirmed instance where any
weighted average of the DELETE/KEEP/MATCH branch values sits at or below target via any identity.
Dispatching a full proof-builder against a completely untested idea risks a wasted round; I
recorded it (§15.5) as a queued mechanism note with a concrete, cheap next step (a single-instance
verification pass on the known hard case `Y=(39,36,30,28,22,18,14)` at `b=6`) for a future round to
try before any build dispatch. This is explicit reasoning, not a default "add everything" move —
if a future round's cheap check finds nothing, it should be recorded as a dead end in this same
section rather than promoted.

## Key decision 5 — did not un-bench `dyadic-cascade-induction` or `concavity-minimax-duality`
Re-read the fresh-framing explorer's report in full myself (not taking the dispatch's framing on
faith). Its own §1 (concavity) explicitly re-confirms an already-dead result with no new leverage;
its §2/§3 (toggle-pair, merge-tree) explicitly conclude "not a new attack surface" / "collapses
into already-explored territory." No part of the report gives dyadic-cascade-induction or
concavity-minimax-duality new leverage on the actually-open items (general-m upper bound, general
n≥4) — both remain benched exactly as prior rounds left them. No edits made to either file this
round.

## Key decision 6 — no new (5th) slug opened
Per CLAUDE.md's single-gap-trap warning and the explicit instruction not to open a redundant slug:
the Refined Delete-Recovery Conjecture is a re-scoping of the *same* top-level gap
(`OPT(Y,p-1)=NC(Y,p-1)`), not a new whole-problem framing — it belongs inside
`potential-weighting-upper-bound.md`, not as a new slug. The aimo-0198 averaging idea is, by the
fresh-framing explorer's own honest framing, "a different proof method aimed at the same target,"
also not a new whole-problem attempt — queued inside the same file for the same reason. No 5th
slug opened this round.

## Build set nomination
**`potential-weighting-upper-bound`** — dispatch its proof-builder against new §15.4 (the Refined
Delete-Recovery Conjecture), following the recommended build order: (1) a targeted
counterexample-hunt at `|B|=1` shaped like the old `|B|=2` counterexample before committing to a
proof; (2) if it survives, attempt the proof via the General Rank-Extraction Identity/Fact 3; (3)
cheaply, separately, exhaustively check the σ=-1/|B|=0 "vacuous match branch" observations.

No other approach has a new, concrete task this round (`dyadic-cascade-induction` is at its
verified milestone with no further lever identified; `concavity-minimax-duality`'s open Local
Claim is honestly scoped as providing no new leverage even if closed; `elementary-exchange-
smoothing` remains retired). Recommend dispatching exactly one proof-builder this round, on
`potential-weighting-upper-bound`, plus the standard single outline-reviewer/proof-reviewer pass
per CLAUDE.md's "rank every round" rule.
