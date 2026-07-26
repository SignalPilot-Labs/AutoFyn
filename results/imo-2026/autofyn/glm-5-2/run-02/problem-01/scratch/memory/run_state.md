## Goal

Solve IMO 2026 Problem 1 (imo-2026-01): blackboard gcd/lcm process.
Problem: 2026 integers >1 on a board. A move picks two >1 entries m,n from
different places and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n), while
possible. (a) Prove the process terminates with exactly one integer M>1.
(b) Prove M is independent of choices.
Task: proof_only (no final answer).
Metric: proof-reviewer verdict on a complete rigorous proof (solved=APPROVE).
Eval: read results/imo-2026-01/current.md ## Status + approaches/.ranking.json.
Baseline: no workspace yet (round 1).
Target: current.md Status=solved, one APPROVE from proof-reviewer.
Constraints: rigor rules (no skipped cases, name tools, prove don't conjecture);
prose Markdown; one approach = one whole-attempt slug.

## Goal Updates

- [2026-07-25] User: solve imo-2026-01. (Note: difficulty_level=medium, rating 5,
  but user explicitly chose this problem; user priority overrides the
  hard-only default. Proceed with it.)

## Eval History

- [Round 1] BREAKTHROUGH. Status: solved. Both approaches APPROVE by proof-reviewer.
  invariant-first: Elo 1501.5, outcome=verified-milestone.
  monovariant-first: Elo 1498.5, outcome=verified-milestone.
  current.md ## Status = solved; ## Full proof present (M = prod_p p^{g_p},
  g_p = gcd of v_p across board, gcd(0,k)=k; termination via lex monovariant
  (W=sum Omega, C=count>1), Delta W = -Omega(gcd(m,n)), three-case split
  {g=1; m=n; g>1 & m!=n}). Goal achieved round 1.

## Rules

- ALWAYS: the "g>1 & m!=n" move case must be broadened to cover g>1 with one
  exponent =1 (e.g. {4,8},{9,27},{2,4}); it has Delta W=-Omega(g), Delta C=0
  (outline-reviewer caught this gap round 1).
- NEVER: use "count of entries divisible by p^k", "gcd of all board numbers",
  or "min of p-exponents" as invariants — they are NOT preserved (counterexample
  {4,8}->{4,2}); the real invariant is gcd of the v_p multiset.
- NEVER: use the total product or max-of-entries as a monovariant — coprime moves
  ({6,35}->{1,210}) increase them. Use W=sum Omega + C=count>1 lexicographic.

## State

Done: (round 1) full solve. 3 explorers scouted (all converged on per-prime
Euclidean + g_p invariant + (W,C) monovariant); outliner put up 2 rival routings
(invariant-first, monovariant-first); outline-reviewer registered+ranked both,
emitted both as build set, flagged the g>1/m!=n case broadening gap (closed);
2 builders wrote complete proofs; proof-reviewer APPROVE both; current.md solved
with full proof; 2 certified lemmas in lemmas/.

Broken:
Next: SOLVED. No further rounds needed. If session must continue, nothing to build.
