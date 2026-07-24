# Build report — claiming-order-invariant (round 4)

**Verdict: dead end (unsolved), with a structural reason, honestly recorded.**

## What I did
1. Read `current.md`, the outline in `approaches/claiming-order-invariant.md`,
   `knowledge_base.md`, the certified `claiming-subgame-reduction` and
   `leftover-formula` lemmas, and the on-file $n=3$ vertex example in
   `approaches/rank-tie-vertex-reduction.md` §3.
2. Pulled the two `aimo-0117` crux entries from `past_crux_moves_database.json`
   directly (no dedicated corpus-query tool needed for a single problem_id
   lookup) plus the source problem statement from
   `past_problems_database.json`, to pin down exactly what its "defer
   commitment" mechanism requires.
3. Compared that mechanism's requirements against our problem's actual rules
   (re-read from `problems.jsonl`): Liu Bang marks up to $n$ points in one
   shot, *then* Xiang Yu marks up to $n$ points in one shot. This is a
   two-move Stackelberg game, not the many-round alternating stone-game
   `aimo-0117` is. `aimo-0117`'s invariant is a loop invariant maintained
   across $n$ rounds of real alternating information exchange; our marking
   stage has only one such exchange total, and the claiming stage (which
   *is* sequential) has zero remaining strategic freedom — it's already
   fully solved by the certified `claiming-subgame-reduction` lemma
   (greedy-max is the unique mutual best response, forced, not a locus of
   cleverness).
4. Tested the outline's Step-2 candidate invariant with exact `Fraction`
   arithmetic (Bash/Python) against the on-file $n=3$ tie-vertex example
   ($S=\{4,4,3,2,1,1\}$, units $1/15$): it fails already at the first claim
   ($4 \not< 4$), and even where it holds it's shown to be a trivial artifact
   of $S$ being pre-sorted, not information about which $S$ is extremal.

## Result
Wrote a full negative writeup to
`results/imo-2026-03/approaches/claiming-order-invariant.md`: Status
`unsolved`, a structural argument (§1) for why no invariant of this shape
can work here, the numeric falsification (§2) confirming it, and a concrete
recommendation (§3) that future rounds redirect any further crux-`aimo-0117`
inspired work toward the marking stage (where the one real round of
adaptive information transfer lives) rather than the claiming stage — and
specifically toward the round-4 explorer's higher-ranked sibling candidate
`rank-pigeonhole-budget` rather than a repaired claiming-order invariant.

No new lemmas produced (nothing here survived long enough to be reusable).
This is intentionally an honest negative result per CLAUDE.md's "record
everything" — the value is in ruling out this framing precisely, not in
partial progress.
