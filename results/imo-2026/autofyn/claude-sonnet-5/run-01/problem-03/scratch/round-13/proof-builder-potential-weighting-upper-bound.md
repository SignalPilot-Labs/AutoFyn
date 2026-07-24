# Round 13 build — potential-weighting-upper-bound

## Status: partial (unchanged — no gap closed this round)

## What was done

Dispatched to resolve the outline-reviewer's flagged precision gap in the No-Gap Lemma (Gap 1a)
and attempt Gaps 1b (Sum Bound) and 1c (MATCH-vs-DEL/KEEP) in priority order. All work is fresh,
independent Python (exact `int`/`fractions.Fraction`, bounded brute force), archived at
`/tmp/round-13/builder-work/`, validated against the file's own three worked examples before being
trusted. Appended as new §20 to `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`
(plus a short round-13 pointer added to `## Status` and `## Current best`, and a new entry in
`## Approaches tried`). **None of Gaps 1a/1b/1c is closed — Status correctly stays `partial`.**

**Gap 1a (highest priority, per dispatch).** Confirmed the outline-reviewer's flagged issue is
real: re-deriving the `h=1` event from the certified `h:=|\{c\in C:c\ge w_1\}|$ convention shows it
occurs on the **half-open** interval `(\min(b_0,d_{k^*}),\max(b_0,d_{k^*})]` (weak at the high end,
because `\ge` counts equality as dominating) — not the open interval the prior statement covered.
Corrected the Conjectured Lemma to this precise form; re-checked the propagation argument (DELETE/
KEEP-while-`h=0` never changes `C`) still goes through unchanged for the corrected statement.
Extended computational corroboration specifically targeting the previously-untested tie/boundary
case: `9267` fresh random (duplicate-allowing) checks + `6552` exhaustive small-case checks, `0`
violations on all of strict/half-open/tie-at-hi/tie-at-lo; a fine-grained rational hill-climb
(step size down to `1/16`) found the margin shrinking toward but never crossing `0`, ruling out the
"integer artifact" reading of the outline-reviewer's own integer-only hill-climb. Proved one new
elementary fact (the **Coincidence Identity**, `d_i-d_l=z_l-z_i`) and used it to reduce a sub-case
of Gap 1a to a two-element-shift perturbation question about `e(\cdot)` — did **not** complete the
sign argument (the shift's sign is uncontrolled without further use of the trigger condition
`M<A_1`, which was not incorporated this round). **Gap 1a remains open**, but its statement is now
precise and far more thoroughly tested, including exactly the case the reviewer flagged as
untested.

**Gap 1b (Sum Bound).** Extended corroboration from the base-generator level only (`112/112`) to
deep DELETE-closure chains: `156` (`q\le6,v_{\max}=5$, depth `\le4`) + `337` (`q\le8,v_{\max}=6`,
depth `\le6`) fresh checks, `0` violations. Isolated the cleanest tractable sub-case
(`\mathrm{rest}=\emptyset`, where the Sum Bound reduces to the fully explicit numeric claim
`w_1\ge2|c_1-c_2|`) and found a `\ge3\times` margin computationally (comfortably above the `2\times`
needed) — a concrete, promising foothold for a future proof attempt, **not completed this round**.

**Gap 1c (MATCH-vs-DEL/KEEP).** Per the dispatch's suggested cheap shortcut, checked whether
"forced matching never occurs" could be a fully general (background-size-bounded but
provenance-free) fact. **It cannot** — decisive counterexample at background size 1
(`C=[3],W=(4,1,0)`: the only two optimal witnesses both match `w_1=4`, value `0`, vs. `1` for the
best non-matching selection), extended to `99/3000`, `116/3000`, `138/3000` forced-matching events
at background sizes `1,2,3` respectively (vs. `0/3000` at size `0`, matching the certified
Empty-Background Lemma). This rules out the cheapest possible route and confirms `\mathcal F`'s
specific provenance is doing real work (parallel to the already-known Sum-Bound provenance
dependence). Extended the `\mathcal F`-restricted corroboration (fresh, deeper, more
duplicate-heavy than any prior sweep) to `19{,}862` total checks, `0` forced-matching events —
`\sim48\times` the file's prior `0/417`. **The existence claim itself remains unproved**; a direct
construction (not the heavier extremal-rewrite machinery, since no forced-matching instance has
ever been found to rewrite away from) remains the recommended next step.

## Files

- `/home/agentuser/repo/results/imo-2026-03/approaches/potential-weighting-upper-bound.md` — new
  §20 appended (full detail of all findings above), `## Status` and `## Current best` updated with
  a round-13 pointer, `## Approaches tried` extended.
- `/tmp/round-13/builder-work/` — all fresh code this round: `mydefs.py`, `base_gen.py`,
  `test_nogap.py`, `exhaustive_nogap.py`, `hillclimb_nogap.py`, `inspect_gap.py`,
  `explore_sumbound.py`, `test_forced_matching.py`, `test_forced_matching_general.py`.

## Promotable lemmas

- **Coincidence Identity** — for any two indices `i,l` (both `\ne1`) in the base-generator's
  sorted list `Z_0`, writing `d_i:=z_1-z_i,d_l:=z_1-z_l`: `d_i-d_l=z_l-z_i`. Trivial (immediate
  substitution) but genuinely useful bookkeeping: it shows that the background-element swap
  `d_{k^*}\to d_j` and the kept-value swap `z_j\to z_{k^*}` (in a candidate witness for `A_{3,j}`
  built from an optimal witness of `A_{3,k^*}`) are **the same shift** `\delta:=z_{k^*}-z_j$ applied
  to both elements simultaneously — a clean reduction (not yet completed) of a sub-case of the
  No-Gap Lemma to a two-element-shift perturbation question about `e(\cdot)`. Proved in full in
  §20.1 of the approach file. Likely too minor/incomplete-in-its-application to certify as a
  standalone lemma file on its own yet (its only current use is an unfinished proof attempt); flagged
  here for the reviewer's discretion rather than proposed for immediate certification.
- No other fully independent, reusable lemma was proved this round (the Sum Bound and Gap 1c
  findings are computational corroboration / negative results about existing conjectures, not new
  general-purpose facts in their own right).
