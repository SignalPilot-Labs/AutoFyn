## Goal

Problem: imo-2026-03
Statement: Let n be a positive integer. Liu Bang and Xiang Yu have a stick of length 1 and want to divide it between themselves. Liu Bang marks at most n points on the stick, and then Xiang Yu marks at most n points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating pieces. Afterwards, they take turns claiming any unclaimed piece, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each n, determine the largest value c such that Liu Bang may guarantee a total length of at least c, regardless of Xiang Yu's play.

Metric: solved (proof-reviewer APPROVE)
Eval command: read results/imo-2026-03/current.md ## Status
Baseline: unsolved
Target: solved
Constraint: must compute c(n) and prove both upper bound and construction

## Goal Updates

## Eval History

## Rules

## State

### Done
- Round 1: Setup. Problem workspace created.

### Broken

### Next
- Dispatch math explorers, outliner, reviewer, builders

## Eval History

### Round 1
- pairing-exchange-normal-form: APPROVE — BREAKTHROUGH
- Status: solved
- Reviewer: "complete and rigorous, both bounds verified numerically and analytically"
- c(n) = 2^n/(2^{n+1}-1) proved

## State (updated)

### Done
- Round 1: Problem imo-2026-03 SOLVED. Answer c(n) = 2^n/(2^{n+1}-1). Proof in results/imo-2026-03/approaches/pairing-exchange-normal-form.md, current.md status=solved.

### Broken
(none)

### Next
- end_session
