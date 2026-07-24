# Round 19 proof-builder report — `potential-weighting-upper-bound`

## Task
Dispatched to (1) prove §32's candidate target (Two-Touch's KEEP `b0<=w1` sub-case at `|W|=3`) in
full, closing the exact gap round 18's proof-reviewer flagged as an overclaim; (2) attempt §31's
Generalized Touch-Bound Lemma at `|C|=2` (best-effort, allowed to stay partial).

## Result

**Item 1 (§32) — CLOSED, full rigorous proof written.** New §33 in
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md`:
- §33.1 proves the new **Two-Variable Reflection Bound** (`w1-|b0-w| >= |b0-(w1-w)|`, `0<=b0,w<=w1`)
  in full, 3 exhaustive cases, re-derived by hand from scratch (matches, and completes, the outline's
  sketch).
- §33.3 proves all 5 per-term bounds of §32's `min`-of-terms reduction in full, with every case
  settled (including a necessary 2-region/4-sub-case split for the match term `A_4`, and a 3-case
  split for the keep-all-three term `A_5`, using the certified Lemma A at each step) — no step left
  as "clearly" or "similarly."
- §33.5 assembles this with already-certified pieces (Empty-Background Lemma, Three-Bound Domination
  Lemma, the certified `b0>w1` KEEP formula, Lemma B, and
  `lemmas/match-branch-domination-via-per-partner-domination.md` with its Per-Partner-Domination
  dependency discharged at the already-certified `q<=3` range) into a **complete, non-circular proof**
  that `OPT_{+1}(C,W) = TwoTouch(C,W)` for every `|C|<=1, |W|<=3` — i.e. **Two-Touch is now genuinely,
  unconditionally proved for `|W|<=3`** (not merely corroborated, and this time actually earning the
  claim round 18's reviewer rejected).
- Computational corroboration (not the proof itself, a sanity check): `/tmp/round-19-build/verify_32.py`,
  exact `Fraction` arithmetic — `0` failures on target (*), all 5 per-term bounds, and the reflection
  bound across a 462-tuple exhaustive integer grid and a 19,894-trial random half-integer sweep
  (`v_max=200`); two negative controls (dropping each load-bearing hypothesis) both fail 100% of the
  time, confirming neither hypothesis is vacuous.
- New reusable lemma drafted for certification: **Two-Variable Reflection Bound** (general, standalone,
  no `|W|=3` restriction).

**Item 2 (§31) — NOT proved, honest partial progress only, exactly as the dispatch allowed.** New §34:
- §34.1: found and confirmed a concrete **negative result** — the cheapest possible domination
  shortcut ("drop the smallest element of `W`") is FALSE at the first genuine excess instance
  (`|C|=2, |W|=5`, touch=5 > threshold 2k=4): **366/3000 (12.2%) failures**.
- §34.2: a shape census over 500 instances shows all 6 possible touch-`<=4` selection shapes occur as
  the unique dominating witness in a non-trivial fraction of cases — ruling out any small fixed witness
  set, meaning a genuine multi-case rank-based proof (larger than Lemma B's own 4-case `k=1` analog)
  would be needed even for this single smallest excess instance.
- §34.3: a structural (non-computational) argument shows the natural "peel-`W`" induction route to
  `k=2` (mirroring Two-Touch's own proof technique) requires, recursively, a brand-new `k=2, sigma=-1`
  mirror object plus the same unbounded-MATCH-background-growth obstruction the touch-bound framework
  was introduced to avoid — i.e. **this route is not independently easier** than the already-multi-round
  -open `k=1` general induction (Two-Touch's own general-`q` closure). This is a genuine, useful
  diagnostic finding (in the spirit of round 9's and round 18's "not independently easier" findings),
  not a proof.
- The outline's own recommended "peel-`C`" Step-3 mechanism (via the certified Background-Release
  Domination Lemma) was **not attempted** this round due to time — flagged as the best next concrete
  target.
- Verification script: `/tmp/round-19-build/explore_31.py` (Fraction-exact, seeded, reproducible).

## Status set on the approach file
`partial` (correctly — §31/Generalized Touch-Bound Lemma, Two-Touch's own general-`q` closure,
Three-Touch's MATCH branch, Gap 1a's general-`q` Per-Partner Domination, Gap 1b, and Gap 1c all remain
open). The file's Status/Approaches-tried/Current-best sections were all updated with round-19 entries
per the file contract; `current.md` (reviewer-owned) was **not** touched.

## Files touched
- `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` — new §33, §34; updated Status,
  Approaches tried, Current best, Promotable lemmas sections.
- `/tmp/round-19-build/verify_32.py`, `/tmp/round-19-build/explore_31.py` — saved, reproducible
  verification scripts (exact-`Fraction` arithmetic, seeded, no unbounded search).

## Promotable lemma for reviewer certification
**Two-Variable Reflection Bound** — `for 0<=b0<=w1 and 0<=w<=w1: w1-|b0-w| >= |b0-(w1-w)|`. Full proof
in §33.1 of the approach file (also restated in the "Promotable lemmas" section at the top of that
file). Recommend certifying as `results/imo-2026-03/lemmas/two-variable-reflection-bound.md`.

Also recommend the reviewer independently re-verify and, if confirmed, formally record the corollary
**"Two-Touch fully, unconditionally proved for `|W|<=3`"** (§33.5) — this both supersedes and actually
delivers what round 18's rejected overclaim tried to assert, this time backed by a complete proof
chain traced explicitly through every certified ingredient (no remaining conditional dependency at
`|W|<=3`).
