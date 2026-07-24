# proof-builder report — covering-system-construction — round 10

## Task
Build out Step 11 "Growth-Forced Divisibility" / the Escape-Cost Lemma, dispatched
this round as a new mechanism for Joint Cofinite FAH. Instructed to check the
outline-reviewer's flagged vacuity risk (linear value-ceiling vs linear index-gap
growth may cancel) concretely, numerically and algebraically, before investing in a
full proof, and to report honestly if the mechanism doesn't work.

## What I did
1. Numeric premise check (Step 11.2c) on the standing `a_1=4807` |F'|,|F''|≥2 rogue
   pair, regenerated from scratch (fresh trial-division script, N=6000). Confirmed
   the properly-recruited `S₀={2,3,5,11,19,23}` gives `A'={3,5,19}` (n_A=6),
   `B'={2,11}` (n_B=7), `q*=17`, `D_bad={13}` — but this extended type is rare (only
   9 occurrences in 6000 terms) and had zero exceptions (`E=E_sym=∅`), so the numeric
   check is consistent with FAH but too sparse to exercise the Escape-Cost Lemma's
   actual premise (repeated same-bad-class hits). A control check at the WRONG,
   un-recruited `S₀=Q` level reproduced the already-understood large failure rate
   (1503/1602), confirming that finding is a known artifact, not new information.
2. Converted the outline-reviewer's flagged risk into a full proof: the **Sandwich
   Genericity Theorem** (the Bounded Gap Lemma's value-vs-index sandwich
   `n-m ≤ a_n-a_m ≤ (n-m)a_1` holds identically for every pair of indices, with no
   reference to type/extended-type/divisor-class data anywhere) and the **Escape-Cost
   Vacuity Theorem** (a determinism-of-deduction argument: no argument built solely
   from class-blind premises, including the Sandwich Genericity Theorem, can output a
   class-sensitive conclusion). Together these prove the Escape-Cost Lemma, as scoped
   by this round's outline, cannot be derived from Step A alone — not a numerical risk
   flag, a structural impossibility proof.
3. This retires the Growth-Forced Divisibility mechanism cleanly (the tenth confirmed-
   dead mechanism for FAH/Cofinite FAH in this workspace), with two new reusable
   negative-result lemmas proposed for certification, and no overclaiming — the crux
   itself (Joint Cofinite FAH / the Successor Claim) remains exactly as open as round
   9 left it.

## Files touched
- `/home/agentuser/repo/results/imo-2026-06/approaches/covering-system-construction.md`
  — updated Status/Current best headers, added Step 11.5 (numeric premise check) and
  Step 11.6 (Sandwich Genericity Theorem + Escape-Cost Vacuity Theorem, full proofs),
  and a "Promotable lemmas (round 10 addendum)" section.
- `/home/agentuser/repo/results/imo-2026-06/lemmas/sandwich-genericity-theorem.md`
  (proposed, not yet certified).
- `/home/agentuser/repo/results/imo-2026-06/lemmas/escape-cost-vacuity.md` (proposed,
  not yet certified).

## Status: partial
Real, honest negative progress: the dispatched mechanism is proved dead (not merely
suspected), with two new promotable screening lemmas. Joint Cofinite FAH / the
Successor Claim remains the sole open gap for the whole problem, unchanged from round
9's isolation.
