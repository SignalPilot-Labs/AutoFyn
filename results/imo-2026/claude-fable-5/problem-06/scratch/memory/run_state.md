# Run State

## Goal
Solve problem `imo-2026-06` (IMO 2026 P6, number_theory, difficulty 9, proof_only) with a complete, rigorous prose proof.
- Metric: `results/imo-2026-06/current.md` `## Status` reaches `solved` (proof-reviewer APPROVE), plus approach ranking health (`approaches/.ranking.json`).
- Eval: read `results/imo-2026-06/current.md` Status + `.ranking.json` each round.
- Baseline (round 1): Status unsolved, no approaches exist yet.
- Target: Status = solved with Full proof in current.md.
- Constraint: prose Markdown proof, rigor rules in CLAUDE.md enforced by proof-reviewer.

Problem statement: Infinite sequence a_1,a_2,... of integers >1; a_{n+1} is the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i ≤ n. Prove there exist T, L with a_{n+T} = a_n + L for all n.

## Goal Updates
- [2026-07-16 06:16] User: solve imo-2026-06. (initial task)

## Eval History
- Round 1 baseline: Status unsolved, 0 approaches.
- Round 2 result: **Status: solved (re-confirmed)** — IMPROVED. Independent adversarial re-verification by fresh proof-reviewer: APPROVE. Step 6 descent re-derived from scratch; fresh sieve-based computational check (independent of round-1 scripts): EP 0 failures on 9 seeds; a_1=385 edge case re-confirmed ({2,11,19} ∈ M, E={2,3,5,7,11,19} all < 5390, T=5088, L=43890, periodicity over 3 full periods); periodicity confirmed on 8 further seeds. verified-milestone recorded for crt-window-small-prime-lockin.
- Round 1 result: **Status: solved** — BREAKTHROUGH. proof-reviewer APPROVE on `crt-window-small-prime-lockin` (chain: Exclusion Principle → Quantitative Witness → multiplicative descent → every essential prime < a_1·g → E finite → L=∏E, T=|V∩[a_1,a_1+L)|, exact periodicity from n=1). Reviewer re-derived Step 6 from scratch; computational checks: EP 0 failures on 17341 non-terms, periodicity confirmed on 9 seeds incl. a_1=385 edge case (T=5088, L=43890). Full proof in results/imo-2026-06/current.md. Rankings: crt-window (APPROVE/solved), valid-set-sunflower-core (CHANGES REQUESTED/partial, GAP 1 open in-route but closable by importing essential-prime-bound lemma), self-blocking-clutter-induction (RETHINK — pure clutter theorem refuted by certified ladder counterexample; recorded as no-go lemma).

## Rules
- ALWAYS: route number-theoretic input into the finiteness crux — the pure combinatorial theorem "identically self-blocking ⟹ finite" is FALSE (ladder-clutter counterexample, certified lemmas/no-go-infinite-self-blocking-clutter.md, round 1).
- NEVER: aim at the strict bound ∪M ⊆ {p ≤ g} — false for a_1=385 ({2,11,19} ∈ M, g=14); the correct theorem is every essential prime < a_1·g (round 1).

## State
### Done
- Round 2: independent adversarial re-verification of the approved proof (fresh proof-reviewer, fresh computational code) → APPROVE, Status stays solved. Goal fully achieved and double-checked.
- Round 1: full pipeline (3 explorers → outliner (4 approaches) → outline-reviewer (cut 1, build set 3) → 3 builders → proof-reviewer). Problem SOLVED: crt-window-small-prime-lockin approved; full proof in results/imo-2026-06/current.md. Certified lemmas: terms-equal-valid-set, dodging-and-witness, finite-core-implies-periodicity, essential-prime-bound, no-go-infinite-self-blocking-clutter.
### Broken
- (nothing)
### Next
- Nothing required: problem solved and independently re-verified (rounds 1 and 2). If end_session is still time-locked and further rounds run, do NOT re-open the proof; at most, low-value polish (e.g. import essential-prime-bound into valid-set-sunflower-core to close its GAP 1 as a second complete route) — optional.
