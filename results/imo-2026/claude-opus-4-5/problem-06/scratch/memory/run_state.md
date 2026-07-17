## Goal

Solve IMO 2026 P6: Prove that for the greedy gcd-linked sequence (a_{n+1} is smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i ≤ n), there exist T, L such that a_{n+T} = a_n + L for all n.

Metric: Status of results/imo-2026-06/current.md
Eval: proof-reviewer verdict (APPROVE = solved)
Baseline: unsolved
Target: solved (APPROVE from proof-reviewer)
Constraint: rigorous proof, all cases, no gaps

## Goal Updates

## Eval History

Round 1: Status partial. two-of-k-structure CHANGES REQUESTED (K_k^2 claim false, backward extension needs rigor). backbone-periodicity RETHINK (wrong constraint characterization - uses backbone primes only but actual constraints involve all primes). Key finding: K_k^2 structure is FALSE for a1=35 (antichain includes {2,3,7} which has 3 elements), but periodicity still holds - K_k^2 is not needed.

Round 2: Status SOLVED. two-of-k-structure APPROVE - complete proof via dichotomy lemma (H_stable finite OR common prime) + CRT periodicity. saturation-route CHANGES REQUESTED (functionally complete but self-describes incorrectly). BREAKTHROUGH: Removed false K_k^2 claim, used trivial backward extension (every a_n ∈ V_stable by pairwise gcd), proved dichotomy via pigeonhole on backbone primes.

## Rules

NEVER: Claim the constraint antichain H equals K_k^2 (all 2-element subsets) - this is FALSE for many starting values (e.g., a1=35 gives {5,7}, {2,5}, {2,3,7}, {3,5}).

ALWAYS: Use P(a_i) (all primes) not just backbone primes B = P(a_1) when characterizing constraints - primes outside B can enter and affect the valid set.

ALWAYS: Verify backward extension rigorously - show a_{n+T} = a_n + L holds for n < N (startup phase), not just n >= N. [RESOLVED in Round 2: trivial by pairwise gcd + V_stable ⊆ V_n]

## State

Done:
- Round 1: Created workspace, 3 explorers, 4 approaches, 2 builds (two-of-k-structure partial, backbone-periodicity RETHINK)
- Round 2: 3 explorers (stabilization, backward, alternative), outliner revised approaches, outline-reviewer ranked, 2 builds (two-of-k-structure APPROVE, saturation-route partial)
- **PROBLEM SOLVED**: two-of-k-structure proof is complete and verified

Broken:
- backbone-periodicity: fundamentally flawed (restricts to backbone primes but constraints involve all primes)
- clique-valid-set: cut by outline-reviewer (fatal gap in coprime-pair resolution)

Next:
- None - problem is SOLVED
