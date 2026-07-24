# Run State — IMO 2026 P6

## Goal
Metric: proof-reviewer verdict on a rigorous prose proof of IMO 2026 P6 (`imo-2026-06`).
Problem: sequence a_1,a_2,... of integers >1; a_{n+1} = smallest integer > a_n with gcd(a_{n+1},a_i)>1 for all i≤n. Prove ∃ T,L with a_{n+T}=a_n+L for all n (sequence is eventually periodic-linear).
Eval: proof-reviewer verdict (APPROVE=solved) + `results/imo-2026-06/current.md ## Status` + `.ranking.json` Elo.
Baseline (round 1): unsolved, no approaches yet.
Target: solved (APPROVE, complete rigorous proof).
Constraints: prose Markdown proof, full rigor per CLAUDE.md rigor rules. task=proof_only, answer_type=none, domain=number_theory, difficulty 9.

## Goal Updates
- [Round 1, 2026-07-24] Initial task: solve imo-2026-06. Goal set.

## Eval History
- Round 2 (end): **SOLVED. BREAKTHROUGH.** proof-reviewer APPROVE on `admissible-set-periodicity` — complete rigorous proof of the WHOLE problem; Status = solved; `## Full proof` written to current.md. The open finiteness nucleus (HS/MCL) CLOSED via greedy-minimality + extremal descent (NOT counting): bridge (★)/G3 from greedy Rule ⇒ compression witness Step C ⇒ minimal-counterexample descent Step D proving (SP) any two terms share a prime ≤ a₁ ⇒ S={primes ≤ a₁} finite hitting set ⇒ certified periodicity machine ⇒ a_{n+T}=a_n+L ∀n≥1. Reviewer independently re-derived the spine; SP confirmed 0 violations across 27 values. Lead came from crux aimo-0030 (good-numbers construction), re-proven from scratch in static admissible-set language. Ranking: admissible-set-periodicity 1571.6 (SOLVED), profile-class-recruitment 1515.4 (partial hedge), essential-prime-counting 1484.8, finite-state-reversible 1428.1. New certified lemma: spine-small-common-prime.md (A/G3, B, C, D). `profile-class-recruitment` = partial (Steps 1-4a rigorous, REC gap honestly flagged) — superseded.
- Round 1 (start): no approaches, Status = unsolved. Baseline established.
- Round 1 (end): Status = partial. IMPROVED. Whole problem RIGOROUSLY REDUCED (reviewer-certified, no gaps, exact from n=1) to ONE finiteness nucleus. Ranking (Elo): admissible-set-periodicity 1531 (partial), essential-prime-counting 1500 (partial), finite-state-reversible 1469 (registered, not built). Verdicts: both built = CHANGES REQUESTED/partial.
  - THE REDUCTION (certified lemmas): A={x>1:gcd(x,a_i)>1 ∀i}; sequence = increasing enumeration of A∩[a_1,∞); gaps ≤ R=rad(a_1); any FINITE prime hitting-set S ⇒ A∩[a_1,∞) exactly ∏S-periodic ⇒ a_{n+T}=a_n+L for EVERY n≥1 (T=|A∩[a_1,a_1+L)|). Numerically confirmed: a_1=15→(T,L)=(8,30); 143→(64,858); 1001→(282,2002); 858→(1,2).
  - REMAINING GAP (both approaches, same wall): (HS/MCL) finiteness of the sole-connector prime set Π={min(supp a_i ∩ supp a_j)}. Pure counting/density (Σ1/p²) PROVEN insufficient — cannot exclude sparse density-zero disjoint essential families.

## Rules
- ALWAYS keep rival approaches far apart in framing/route, not one idea tried many ways (single-gap trap, round 1).
- ALWAYS run outline-reviewer every round; no fast-path advance-the-leader (round 1).
- ALWAYS each slug is a complete attempt at the whole claim end-to-end, gaps as explicit gaps (round 1).
- NEVER attack finiteness (HS/MCL) with pure counting/density (Σ1/p², interval-occupancy) — PROVEN a dead wall in round 1 (cannot exclude sparse density-zero disjoint essential prime families). Any new finiteness attack must use GREEDY MINIMALITY (a non-greedy pairwise-gcd sequence can have infinitely many essential primes, so the greedy "smallest next term" rule is load-bearing), round 1.
- NEVER target "primes dividing infinitely many terms" as the essential set — that set is ALL small primes here (terms fill residue classes mod L), a false target; the essential set is the finite sole-connector/min-common set Π=primefactors(L) (round 1).
- ALWAYS reuse certified lemmas in results/imo-2026-06/lemmas/ (enumeration-and-bounded-gaps, finite-hitting-set-periodicity) — the reduction is DONE; do not re-prove it. The ONLY open problem is (HS/MCL) finiteness (round 1).
- SINGLE-GAP-TRAP FORMING: all 3 approaches share the finiteness nucleus. Next round MUST open ≥1 genuinely different framing of FINITENESS itself (not a new finish), per CLAUDE.md shared-gap-plateau guidance (round 1).

## State
### Done
- Round 1: env setup; workspace created. Reduced whole problem to ONE finiteness nucleus (HS/MCL), reviewer-certified. 2 reusable lemma files. 3 approaches registered; 2 built (partial).
- Round 2: **PROBLEM SOLVED.** Explorers fanned out on 3 distinct finiteness mechanisms (greedy / covering / extremal); extremal lens surfaced crux aimo-0030 template. Outliner revised leader with extremal-descent finiteness graft + opened diversity hedge. Reviewer APPROVE — complete rigorous proof of whole problem, Status=solved, Full proof recorded. Finiteness nucleus CLOSED. Certified new lemma spine-small-common-prime.md.
### Broken
- Nothing open on the main goal. (Optional: `profile-class-recruitment` hedge still has REC gap, but it is superseded by the solve — no need to close.)
### Next
- GOAL ACHIEVED. Nothing further required. If run continues (end_session time-locked), a verification round could independently re-audit the Step D descent and the (★) bridge once more for maximal confidence, but the proof is already reviewer-APPROVED and complete.
