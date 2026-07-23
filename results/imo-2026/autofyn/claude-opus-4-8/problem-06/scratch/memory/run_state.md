## Goal

Produce a complete, rigorous prose proof of IMO 2026 Problem 6 (`imo-2026-06`).

**Problem:** Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than 1. For all positive integers $n$, $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, \ldots, n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T} = a_n + L$ for every positive integer $n$ (the sequence is eventually — in fact everywhere — arithmetic-periodic in the shift sense).

**Metric:** proof-reviewer verdict on the best approach in `results/imo-2026-06/`.
**Eval:** proof-reviewer judgment (solved | partial | unsolved) + approach ranking `results/imo-2026-06/approaches/.ranking.json`.
**Baseline (round 1 start):** no workspace, Status = unsolved, no approaches.
**Target:** Status = solved (proof-reviewer APPROVE) — complete rigorous proof, no gaps.
**Constraint:** prose Markdown proof; every step justified; no hand-waving; name every theorem.

## Goal Updates

- [Round 1] Run started: solve imo-2026-06 (IMO 2026 P6, number theory, difficulty 9/hard).
- [Round 2] GOAL ACHIEVED: proof-reviewer APPROVE on descent-shared-prime, Status = solved. Complete rigorous proof recorded in current.md ## Full proof.

## Eval History

- [Round 1 baseline] Status: unsolved. No approaches yet.
- [Round 2] Status: **SOLVED** — BREAKTHROUGH. Round-1's Lemma S found FALSE (counterexample a₁=385: terms 3·7·19 & 2·11·19 share only large prime 19>P₁=11). Corrected crux threshold to a₁ (not P₁). descent-shared-prime proved **Lemma S′** ("any two clauses share a prime ≤ a₁") by minimum-height violating-pair descent (companion x with supp(x)=σ(S_j), a₁≤x<a_j via Lemma S4, adapting IMO-2024-P5 Claim 4/5) ⇒ Prop 1′ (every minimal clause ⊆ {primes ≤ a₁}, finite ground set) ⇒ finitely many minimal clauses ⇒ certified finish gives a_{n+T}=a_n+L ∀n. proof-reviewer APPROVE: independently re-derived Lemma S4 bound + both descent cases from scratch; Lemma S′ 0 violations for a₁∈{15,35,77,143,210,255,385,1001,2310,4199}. Certified lemmas: shared-small-prime.md (S′, S4, Prop 1′), clutter-and-reconciliation.md (clique-descent's Lemmas 1–3). Ranking: descent-shared-prime 1545.7 (solved) > clique-descent 1541.2 (partial) > sieve-closure 1485.5 > finite-state-bijection 1427.6. clique-descent's gap now closed by S′ but kept partial as standalone framing.
- [Round 1] Status: **partial** — BREAKTHROUGH. Whole problem rigorously reduced (two independent framings, non-circular, off-by-one-clean finish verified) to ONE finiteness crux. Ranking: clique-descent 1531.3 (partial) > sieve-closure 1500.7 (partial) > finite-state-bijection 1468.0 (not built). All supporting steps proved & reviewer-certified into lemmas/bounded-gaps-and-clique.md: gaps 0<a_{n+1}-a_n<=a1; pairwise gcd>1; every term in A=∩A_n; Sub-lemma E (admissible>a1 ⇒ term); minimal-clause reduction; the for-EVERY-n finish (a_{n+1}=min(A∩(a_n,∞)) ∀n ⇒ greedy enumeration of periodic A ⇒ a_{n+T}=a_n+L, L=M=∏essential primes, T=|A mod M|). Verified a1=143 ⇒ E={2,3,11,13}, L=858, T=64; Lemma S zero violations across 18 starts.
  - **The sole open gap (crux, shared by both approaches):** Lemma S — no two clauses (terms' prime-support) share ONLY a large prime (>P1=largest prime factor of a1); equiv. any two clauses share a prime ≤P1 ⇒ every minimal clause ⊆ {primes≤P1} ⇒ finitely many minimal clauses ⇒ A periodic. sieve-closure's equivalent form: "essential primes finite." Partial progress: first-appearance clauses of a large prime shown non-minimal (mild size condition).

## Rules

- NEVER certify a "reduced to Lemma X" milestone without a computational check that Lemma X is TRUE — round 1 certified the reduction to Lemma S, but Lemma S itself was FALSE (a₁=385). A reduction to a false lemma is worthless (because the reviewer's "airtight reduction" verdict does not check the target lemma's truth, round 2).
- ALWAYS state gcd/shared-prime thresholds as a₁ (the term itself), NOT P₁ (largest prime factor of a₁) — the correct bound for "two clauses share a small prime" is ≤ a₁; the P₁ version is false (round 2).
- ALWAYS keep rival approaches far apart in framing (not just technique) — shared framing = shared wall (CLAUDE.md, round 1).
- NEVER split one proof across slugs — each slug is a complete end-to-end attempt at the actual claim (single-gap trap, round 1).
- ALWAYS treat the reduction (§§0–4) as DONE and reusable — the certified lemmas file holds it; round 2+ should attack ONLY the finiteness crux (Lemma S), not re-derive the finish (because reviewer certified it airtight, round 1).
- SHARED-GAP WATCH: both live approaches bottomed out on the SAME finiteness crux in round 1. If round 2's attacks on Lemma S both stall on the same sub-step, round 3's outliner MUST open ≥1 approach that establishes finiteness from a genuinely different framing (e.g. sunflower/Δ-system on the clause family, or a direct growth/density bound), per CLAUDE.md shared-gap rule.

## State

**Done:**
- [Round 1] Env setup: installed numpy/scipy/sympy; created results/imo-2026-06/ workspace.
- [Round 1] Full flow: 3 explorers → outliner (3 approaches) → outline-reviewer (built clique-descent, sieve-closure) → 2 builders → reviewer. Result: problem reduced to a single finiteness crux; both approaches partial; reduction certified into lemmas/.
- [Round 2] Full flow: 3 explorers (sunflower found Lemma S FALSE; density+finite-state converged on aimo-0030/IMO-2024-P5 descent) → outliner (corrected threshold P₁→a₁, opened descent-shared-prime, revised clique-descent & sieve-closure) → outline-reviewer (verified corrected reduction, build set: descent-shared-prime, clique-descent) → 2 builders → reviewer. **descent-shared-prime SOLVED (APPROVE); problem complete.**

**Broken:** none. GOAL ACHIEVED.

**Next:** Goal is met (Status = solved, proof-reviewer APPROVE, Full proof in current.md). No further build work required. If run continues: optionally have a fresh proof-reviewer do a final adversarial pass on the complete proof for extra confidence, or polish clique-descent as an independent second solution for robustness. Otherwise end session.
