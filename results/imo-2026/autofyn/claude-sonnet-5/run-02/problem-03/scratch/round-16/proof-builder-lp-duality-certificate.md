# Build report — lp-duality-certificate (round 16)

**Status: partial** (unchanged from round 15 — Open Gap 1 / case (b2)
still open; this round's contribution is a certification fix plus a
genuine negative result, not new coverage).

## Task 1 (hygiene) — sign bug: fixed, and deeper than expected

The round-15 sign bug in `alternating-gap-cross-lemma.md` is fully
corrected. The fix is **not** the simple relabeling the round-16 outline
described ("$(-1)^j\to(-1)^{j'}$ in the tail prefactor"): re-testing the
round-15 reviewer's own counterexample $(45,45,31,27)$ shows that example
has an *empty tail*, so the tail-prefactor relabeling alone changes nothing
and the bug persists. The actual second bug: the **gap-sum's own per-pair
sign** must be indexed by a split pair's rank among split pairs only
($s=1,2,\dots$), not its raw pair index $i$, since an equal (untouched)
pair contributes an even number of raw elements (2) and never flips
parity. Both signs (gap-sum and tail) are now correctly reindexed by
split-rank; proved in full and re-verified by a fresh 30000-trial
exact-`Fraction` script, zero mismatches across 17834 feasible
constructions, including exact resolution of the original counterexample
($A=4=4$). Both round-14 case-(b2) witnesses remain closed (unaffected, as
predicted — neither uses a mixed equal/split configuration). Lemma
re-certified as corrected in `lemmas/alternating-gap-cross-lemma.md`.

## Task 2 (primary, gated) — algebraic check: mechanism confirmed inert

Per the outline-reviewer's mandatory gate, checked algebraically (before
any numerics) whether "recursed image lands in case (a)/(b1) one level
down" gives anything below the round-14 zero-slack ceiling $a_{n-1}T'$.
**Confirmed: it does not.** Case (a)/(b1)'s own proven bound for the
recursed tail is exactly $a_{n-1}T'$ — the same ceiling substituted by
`peel-zero-slack-dead-end`/`bisect-containment-dead-end` — and this
ceiling is tight (attained with equality by genuine instances at every
level of the induction, traced back to the fully-closed $P(2)$ base case).
So "which case the tail falls into" changes only *how* the $a_{n-1}T'$
bound was established, never *what* its value is, and substituting it into
Theorem C′/B$_k$ reproduces exactly the already-derived, already-ruled-out
zero-slack thresholds. This is a clean, general (any $n$, any peel target
$k$) negative result — proved algebraically, not by numerics — now
certified as `lemmas/recursive-image-escape-dead-end.md`. Per the
outline's explicit branching instruction, the numeric diagnostic was
correctly **not** run (a "generic escape" numeric finding would have been
mathematically vacuous given this result).

## Task 3 (fallback) — grid check: non-closing, honestly reported

Ran a broadened (denser, exact-`Fraction`, not random) grid check of case
(b2)'s box at $n=3$, combining every certified construction on file. 212
of 214 grid points are covered; the two exceptions cluster at round 14's
own already-known near-tight witness and are attributable to this round's
non-optimized (midpoint) parameter choice within the multi-parameter
families, not a newly found gap. This is non-rigorous corroboration only —
**does not close case (b2)** at $n=3$ or $n=4$; the joint vertex
fixed-point obstruction (R11.5/R12.5/R14.3) remains the real blocker and
was not resolved this round.

## Net effect

Open Gap 1 (general upper bound, case (b2)) remains open. Genuine,
non-overclaimed progress this round: (1) a corrected, re-certified lemma;
(2) a new certified negative lemma that forecloses an entire family of
"peel/bisect + case-membership" recursive arguments (not just the two
prior instances), sharpening what any future closure of case (b2) must
look like — it needs either the *exact* value of a recursive sub-instance
(not a case-ceiling), or a non-recursive mechanism (joint vertex
fixed-point system, or further extension of the Alternating-Gap-Cross /
Cross-Piece family).

## Files touched

- `results/imo-2026-03/approaches/lp-duality-certificate.md` (Status,
  Approaches tried, Current best, new "Round 16 build" section)
- `results/imo-2026-03/lemmas/alternating-gap-cross-lemma.md` (corrected
  identity, re-certified)
- `results/imo-2026-03/lemmas/recursive-image-escape-dead-end.md` (new)
- Scripts: `/tmp/round-16/verify_altgapcross_fixed2.py`,
  `/tmp/round-16/verify_witnesses_round16.py`,
  `/tmp/round-16/grid_check_n3_full.py`
