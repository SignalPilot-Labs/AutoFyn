## Goal

Solve IMO 2026 Problem 6 (problem_id `imo-2026-06`).

**Statement:** Let a_1,a_2,... be an infinite sequence of integers >1 such that for every n, a_{n+1} is the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for every i=1..n. Prove there exist positive integers T,L with a_{n+T} = a_n + L for all n.

**Domain:** number_theory. **Task:** proof_only (no numeric answer). **Difficulty:** 9/10 (hard).

**Metric / eval:** proof-reviewer verdict on `results/imo-2026-06/current.md` `## Status`.
- **Eval command:** read `results/imo-2026-06/current.md` `## Status` (solved | partial | unsolved) + `results/imo-2026-06/approaches/.ranking.json` Elo.
- **Baseline:** unsolved, no approaches, no ranking (round 1, fresh).
- **Target:** `solved` — proof-reviewer APPROVE on a complete rigorous proof (every case settled, no gaps, theorems named).
- **Constraints:** prose Markdown, no Lean; rigor rules per CLAUDE.md (no skipped cases, no hand-waving, name tools, prove don't conjecture).

## Goal Updates

- [2026-07-25 R1] User: solve imo-2026-06. Problem fixed for the whole run.

## Eval History

- [R1] Baseline established: Status = unsolved (no approaches yet); ranking empty. Fresh workspace.
- [R2] **BREAKTHROUGH — SOLVED.** Status = `solved`. proof-reviewer APPROVE on `essential-monovariant`, outcome `verified-milestone`. Key insight: P6's greedy sequence is EXACTLY the increasing enumeration of "good numbers" of the game-of-numbers in corpus crux `aimo-0030` (Italy TST / IMO-SL 2013 N5), parameter k=a_1 (Theorem GC, proved from scratch via G1–G4, no circularity). The stripping descent (Lemma G6, re-proved from scratch, adapting aimo-0030's Claim 5) shows any two good numbers share a small prime ≤ k; transfer via GC gives Lemma 4' (every pair of terms shares a prime ≤ a_1) — the round-1 crux, now closed. Round-1 periodicity machinery at threshold B=a_1 then yields a_{n+T}=a_n+L_0 for all n≥1, T=|V|, L=L_0=∏_{p≤a_1}p, no transient (φ cyclic permutation/bijection ⟹ pure periodicity from n=1). Empirically verified for a_1∈{2,3,5,6,7,10,15}. Full proof written to current.md `## Full proof`. Post-R2 Elo: essential-monovariant 1584 (leader, solved), crude-reduced-type 1579, grid-counting-shared-primes 1502, propagation-bezout 1499, covering-system-redundancy 1445 (dormant), translation-self-similarity 1391 (dormant). Other verdicts: crude CHANGES REQUESTED/partial (conditional bridge, now fillable from Lemma 4', redundant); propagation-bezout RETHINK/unsolved (circular: shift algebra φ defined via V which needs Lemma 4); grid-counting CHANGES REQUESTED/partial (large-prime-span lemma certified; Lemma 5 arithmetic error 389/900→17/36, not load-bearing).

## Rules

- ALWAYS: when a builder risks grinding on an open induction/crux, give a BOUNDED deliverable — write floor deliverables (certify any free partial lemmas into lemmas/) FIRST, then time-box the ceiling attempt; if stalled, write the precise obstruction and stop. (Round 1's essential-monovariant builder was force-interrupted idle 908s grinding Lemma 4's induction; round 2's bounded-task builders all completed cleanly. Round 2.)
- NEVER: assume a retrieved crux (corpus) is a citation — every borrowed step must be re-proved from scratch in prose. The P6 solve rested on re-deriving aimo-0030's game-equivalence (Theorem GC) and stripping descent (G6) inside the writeup, not citing them; the reviewer verified this explicitly. (Round 2.)
- ALWAYS: when the field collapses to one shared gap (single-gap trap), commission genuinely different PROOF ROUTES to the gap itself, not different framings of the whole problem. Round 2 fielded descent+transversal (Route D, won), propagation (Route P), grid-counting (Route G) — three distinct mechanisms. (Round 2.)
- ALWAYS: verify analytic bounds numerically before writing them as rigorous — grid-counting Lemma 5 stated 389/900<1/2 which is false (true ≈0.4522); the conclusion survived via 17/36 but the proof as written was wrong. (Round 2, reviewer finding.)

## State

### Done
- R1: Read CLAUDE.md, problem statement, knowledge_base.md, crux_moves_documentation.md. Installed numpy/scipy/sympy. Created workspace results/imo-2026-06/{approaches,lemmas}. Fielded 5 approaches (4 registered, windowed cut). essential-monovariant builder proved gap bound (Lemma 2) + full periodicity machinery conditional on crux Lemma 4; got stuck grinding Lemma 4 (round ended early).
- R2: 3 explorers (crux-descent, alt-framing, corpus) in parallel — converged: no framing escapes the crux; identified 3 genuinely different routes (descent+transversal aimo-0030, propagation aimo-0648, grid-counting aimo-0447). Outliner fielded essential-monovariant(advance, Route D) + crude-reduced-type(advance) + propagation-bezout(new) + grid-counting(new). Outline-reviewer registered 2 new, ranked (essential-monovariant 1584 leader), emitted 4-slug build set with bounded deliverables. 4 builders ran in parallel (no stuck). **essential-monovariant SOLVED via game-equivalence (Theorem GC) + stripping descent (Lemma G6) → Lemma 4' closed → periodicity machinery → theorem.** proof-reviewer APPROVED, recorded verified-milestone, wrote full proof to current.md. Certified lemmas: multiple-of-r-satisfies-lemma-4, large-prime-span-divides-at-most-one-term (in lemas/). GOAL ACHIEVED.

### Broken
- grid-counting-shared-primes Lemma 5: arithmetic error (389/900 false; should be 17/36). Not load-bearing (only feeds the [GAP] growing-window ceiling). Moot — theorem already solved. (Round 2, reviewer finding.)
- propagation-bezout: circular as filed (shift algebra φ defined via V which needs Lemma 4). Confirmed dead-end. Moot. (Round 2.)

### Next
- GOAL ACHIEVED (Status solved). No further proof work needed on imo-2026-06. Optional hygiene if the run continues: (a) make crude-reduced-type self-contained by importing Lemma 4' into its Step 5; (b) fix grid-counting Lemma 5 (389/900→17/36); (c) retire propagation-bezout (dead-end). Recommend closing the run.
