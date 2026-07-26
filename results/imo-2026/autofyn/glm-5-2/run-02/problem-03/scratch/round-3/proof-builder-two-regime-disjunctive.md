# Proof-builder — two-regime-disjunctive (round 3) — build summary

**Slug:** `two-regime-disjunctive`  **Problem:** `imo-2026-03`  **Status:** `partial`

## What was dispatched

Close **G2 (regime-N upper bound for `n ≥ 3`)** via Engine R-pile (greedy recursive
pile-matching of the two largest pieces: cut `a_2` out of `a_1` when `a_1 ≥ 2 a_2`,
bisect fallback when balanced), generalizing the `n = 1` sliver mode and `n = 2`
Strategy A. Reviewer's required fixes: (1) consecutive-rank invariant inductively,
(2) balanced fallback `n ≥ 3`, (3) dyadic detection.

## Outcome: Engine R-pile FALSIFIED (genuine gap, honestly recorded)

I implemented the engine in python (exact rational arithmetic) and stress-tested it.
**It does not close G2.** Three classes of counterexamples:

1. **Exact dyadic** `(8,4,2,1)/15` → `A = 1/5`, `Liu = 3/5 > 8/15` (the explorer's
   known overshoot; now characterized cleanly by the dyadic-ratio lemma below).
2. **Balanced non-dyadic** `(.5, .3, .15, .05)` → `Liu = 11/20 = 0.55 > 8/15` (the
   bisect fallback overshoots; no clean `n ≥ 3` recursive rule replaces the `n = 2`
   four-strategy template).
3. **Extreme-dominant with tiny tail** `(.9, 1/30, 1/30, 1/30)` → `Liu = 0.9` (cutting a
   tiny `a_2` out of a huge `a_1` is negligible). A grid sweep of `86` dominant `n = 3`
   configs (`N = 30`) finds `42` failures.

The true optimal Xiang cap on every tested non-dyadic `n = 3` config is `31/60 < 8/15`
(verified by brute force, grid `N = 60`), so the **regime-N conjecture holds
numerically** — the greedy just fails to find the optimum.

## Reviewer's required fixes — status

1. **Consecutive-rank invariant** — MOOT. The greedy's failure is suboptimality, not
   interleaving. Once a frozen pair forms, the full-multiset greedy treats pair members
   as `a_2`-candidates and bisects them, destroying cancellation (trace documented on
   `(.6, .25, .1, .05)`). Controlling the sort locally at each step does not fix bad
   cut selection.
2. **Balanced fallback `n ≥ 3`** — UNSOLVED within the greedy family. The `n = 2`
   four-strategy template does not lift; optimal `n = 3` strategies have no recursive
   structure the greedy reproduces.
3. **Dyadic detection** — SOLVED (the one clean result this round). The **dyadic-ratio
   overshoot lemma**: the greedy cancels its created pair iff `a_1 > 2 a_2` strictly;
   at `a_1 = 2 a_2` it builds an odd-multiplicity block and overshoots. The order-`n`
   dyadic telescopes (`a_1 = 2 a_2` at every level), so the greedy overshoots on the
   dyadic — regime-N tool only, dyadic routed to pair-pile (regime D). **Proposed for
   certification** (`lemmas/lemma-dyadic-ratio-overshoot.md`).

## What survives (rigorous)

- All round-2 results intact: `c(1) = 2/3`, `c(2) = 4/7` end-to-end; regime-D (dyadic)
  upper bound for all `n` via the certified pair-pile; `U(1)` two-mode, `U(2)` four-
  strategy.
- NEW: dyadic-ratio overshoot lemma (one-step characterization, dyadic-detection).
- The regime-N conjecture is numerically robust (`31/60 < 8/15` on all tested
  non-dyadic `n = 3` configs) but analytically OPEN for `n ≥ 3`.

## Direction for a future outliner

The greedy R-pile is RULED OUT. A genuinely different mechanism is needed for regime-N.
Candidate (NOT proved, flagged in Section 5b.7): an **even-block / multiplicity-parity**
strategy — Xiang uses his `n` marks to make every piece of value `≥ α(n)` have EVEN
multiplicity in the final `2n + 1`-piece multiset, leaving only sliverable (`< α(n)`)
pieces at odd multiplicity, forcing `A < α(n)`. Obstruction: `2n + 1` is odd, so an odd
number of values have odd multiplicity; the conjecture is that for non-dyadic configs
Xiang can push all odd-multiplicity excess below `α(n)` (on the dyadic, the pair-pile's
residual `(3, 2)`-pair is exactly the irreducible `α(n)` excess). Different framing from
the greedy (targets multiplicity parity, not pile-matching) — worth a new approach slug.

## Files touched

- `results/imo-2026-03/approaches/two-regime-disjunctive.md` (updated: new Approaches-
  tried entry, updated Current best, new Section 5b with falsification + lemma, updated
  synthesis, new promotable lemma #3).
- `results/imo-2026-03/lemmas/lemma-dyadic-ratio-overshoot.md` (NEW, proposed for
  certification).

Did NOT touch: other slugs' files, `.ranking.json`, `current.md`.
