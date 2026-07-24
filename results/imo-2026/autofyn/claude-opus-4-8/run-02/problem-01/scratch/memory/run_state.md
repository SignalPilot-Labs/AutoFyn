# Run State — imo-2026-01

## Goal
Produce a complete, rigorous prose proof of IMO 2026 Problem 1 (`imo-2026-01`, medium, number_theory).

Statement: 2026 integers >1 on a blackboard. A move picks two integers m>1, n>1 from different places and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). Moves continue while ≥2 entries are >1.
- (a) Prove that after finitely many moves exactly one integer M on the board is >1.
- (b) Prove that the value of M does not depend on the choices.

Metric: proof-reviewer verdict. Target: Status `solved` (APPROVE) — complete proof of both (a) and (b).
Eval command: proof-reviewer adversarial review of results/imo-2026-01/approaches/<slug>.md + current.md.
Baseline (round 1): no workspace, unsolved.
Constraints: prose Markdown proof, full rigor per CLAUDE.md; both parts proved.

## Goal Updates
- [Round 1] User: "solve the problem imo-2026-01." (Note: `medium` problem; user request overrides hard-only default.)

## Eval History
- [Round 1] SOLVED (BREAKTHROUGH). Two independent complete proofs, both APPROVE by proof-reviewer.
  Closed form M = ∏_p p^{g_p}, g_p = gcd_i v_p(x_i). Ranking sidecar:
    perprime-valuation  Elo 1531.3  outcome verified-milestone (frontrunner, adopted as Full proof)
    descent-induction   Elo 1500.7  outcome verified-milestone (second independent proof)
    confluence-newman   Elo 1468.0  registered, not built (no diversity gain)
  Core verified computationally by 3 explorers + reviewer (2000 random boards × 40 play-orders): halts,
  order-independent, matches closed form.

## Rules
- ALWAYS decompose gcd/lcm-move board problems prime-by-prime: the move sends valuation pair (a,b)→(min(a,b),|a-b|), one subtractive-Euclid step (because round 1 this cracked the whole problem).
- ALWAYS remember gcd(k,0)=k when reasoning about g_p=gcd of valuations across a board (because a valuation can hit 0 mid-process and the edge case is load-bearing for M>1, round 1).

## State
Done:
- Round 1: solved imo-2026-01 (a)+(b). current.md Status `solved` with Full proof; two approach files
  (perprime-valuation, descent-induction) both APPROVE; confluence-newman registered as backup.
  Four lemmas certified in results/imo-2026-01/lemmas/ (perprime-move-step, lex-monovariant-termination,
  gp-valuation-invariant, three-cell-joinability). Env set up (numpy/scipy/sympy installed).
Broken: none.
Next: Goal achieved. If continued, options: polish/consolidate current.md exposition, or (per user) pick a
  new problem. No outstanding gaps.
