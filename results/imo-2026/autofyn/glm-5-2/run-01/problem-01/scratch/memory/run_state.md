## Goal

Solve IMO 2026 Problem 1 (`imo-2026-01`): prove both (a) the gcd/lcm blackboard
process terminates with exactly one integer M>1 regardless of choices, and (b) M
is independent of choices. Deliver a complete rigorous prose proof in
`results/imo-2026-01/current.md` `## Full proof`.

- Metric: proof-reviewer verdict on `results/imo-2026-01/current.md` ## Status.
- Eval command: read `results/imo-2026-01/current.md` `## Status` and
  `results/imo-2026-01/approaches/.ranking.json`; reviewer returns
  APPROVE/CHANGES REQUESTED/RETHINK.
- Baseline: unsolved (no workspace, no approaches).
- Target: solved (proof-reviewer APPROVE on a complete proof covering (a) and (b)).
- Constraints: prose Markdown, no Lean; rigor rules in CLAUDE.md (no skipped cases,
  no hand-waving, name tools, prove don't conjecture). One problem this run.

## Goal Updates
- [2026-07-23] User: "solve the following IMO Problem 1" — the Confucius
  gcd/lcm blackboard problem. Note: this problem is `difficulty_level: medium`
  in the benchmark, NOT hard. The user explicitly overrode the "hard only"
  default by naming IMO P1. This run attacks imo-2026-01 end to end.

## Eval History
- Round 1 baseline: Status = unsolved; 0 approaches; Elo n/a.
- Round 1 BREAKTHROUGH: Status = SOLVED. proof-reviewer APPROVE on all three
  approaches. Ranking (outline-reviewer, head-to-head): per-prime-euclidean-invariant
  Elo 1531 > integer-termination-invariant-pin 1500 > confluence-unique-normal-form 1469.
  All three record_outcome = verified-milestone. M = prod_p p^{D_p},
  D_p = gcd(v_p(x_1),...,v_p(x_2026)) from initial board. canonical proof in
  current.md credited to per-prime-euclidean-invariant; 4 lemmas certified in
  results/imo-2026-01/lemmas/. Goal ACHIEVED.

## Rules
- ALWAYS: For blackboard-replacement problems, first translate the move to its
  action on p-adic valuations (gcd=lattice meet=min, lcm/gcd=max-min=|diff|);
  this reveals the per-prime Euclidean structure and the invariant D_p=gcd of
  valuations (round 1, imo-2026-01).
- ALWAYS: pair a strict-decreasing primary potential (W=sum Omega, or plain
  product P) with a secondary count c for the coprime-move case where the
  primary is fixed; argue termination via lexicographic descent on N^2 (round 1).
- NEVER: frame the gcd/lcm move's termination as a staged "Euclidean-phase then
  coprime-merge-phase" split — it is a DEAD framing; non-coprime states persist
  mid-process for arbitrary move orders (explorer + outline-reviewer, round 1).
- NEVER: prove local confluence on POSITIONED boards for this move — it fails
  (72/1331, e.g. (2,3,2)); confluence must be argued on MULTISETS (outline-reviewer,
  round 1).

## State
- Done: Round 1 — SOLVED imo-2026-01 both parts. Three APPROVED approaches in
  results/imo-2026-01/approaches/; canonical full proof in current.md; 4 shared
  lemmas in lemmas/. Ranking sidecar .ranking.json written by ranker tools.
- Broken: (none)
- Next: Problem solved. If further rounds run, consider hardening (cross-review
  the confluence proof's overlapping-critical-pair prose) or move on — goal met.
