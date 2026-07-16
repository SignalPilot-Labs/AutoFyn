# Build report — ll-inclusion-gap (Round 6)

**Status: partial.** Obeyed both outline-reviewer corrections. Wrote
`results/imo-2026-03/approaches/ll-inclusion-gap.md`.

## What was delivered (rigorous, new this round)

1. **Parity-Condition Lemma (correction #1).** Replaced the decertified FALSE "Structural Lemma"
   ("no Q-part in a forbidden-band interior") with the TRUE parity version: `S_Q ⊆ S_R ⟹ N_Q even
   wherever N_R even`; for R=G_{n−1}, `N_Q` even throughout every forbidden dyadic band ⟹
   `#{parts ≥ 2^j}` even at forbidden-band tops, and interior parts occur with even multiplicity
   (equal pairs like {3/2,3/2} admissible). General n, rigorous. The reviewer's counterexample
   Q={3/2,3/2,2,3} SATISFIES this parity version (it is genuinely INC), confirming the reword is
   correct, not a re-import of the false claim.

2. **Complete, correct n=3 INC base case (R=G_2).** Full casework `m∈{2,4}`, and within m=2 the
   sub-cases `e=2` (the previously-missed even-multiplicity interior pair {s,s}⊂(1,2)) and `e=0`
   (ℓ=0,1,2). Every branch gives `A(Q) ≤ 2 = A(G_2)−1`, so `A(Q∪R) ≥ 1`. This CLOSES the INC branch
   for n=3 and fixes the R5 incompleteness. Budget `|Q|≤4` used (correction #2).

3. **Top-band decomposition identity (general n).** With `h=#{parts≥2^{n−2}}` proved EVEN by the
   parity lemma, `A(G_{n−1})−A(Q) = deficit_top + M`, both ≥0, reducing the general "+1" to the single
   scalar inequality `deficit_top + M ≥ 1` (open, G-INC-1). Rigorous; verified 0-failure n=3,4.

4. **Odd-index reformulation** `A(Q)=2O_Q−2^n`, giving the equivalent clean target `O_Q ≤ O_{G_{n−1}}`.

5. **Clean subcase** `max(Q)≤2^{n−2}` and **GAP Case-1** (`b≥1`) — rigorous, general n.

## Numeric checks (all bounded, <2 min total, budget enforced)
- Arithmetic INC bound `A(Q) ≤ A(R)−1`: 0 violations / 400 budget-valid n=3 instances (incl. refined
  R with A(R)≥1), min margin exactly 1. Matches reviewer's 574-instance result.
- Decomposition identity + `h` even + margin≥1: 0 failures at n=3 (grid 1/4, 52 configs) and n=4
  (grid 1/2, 36 configs).
- n=3: `#{parts≥2}` even and `A(Q)≤2` for all 52 INC configs (0 failures).

## Open gaps honestly flagged
- **G-INC-1**: general-n `deficit_top + M ≥ 1` (the crux; reduced to one scalar inequality, not closed).
- **G-INC-2**: refined-R general n (needs S_R-level-structure strengthened IH; budget essential —
  R={4,2,½,½} counterexample is over-budget).
- **G-GAP**: alignment cost ≥1 (tight half-interval-pair witnesses documented; unproven).

## Promotable lemmas for certification
Parity-Condition Lemma; Top-band decomposition identity; Odd-index reformulation; Complete n=3 INC
base case. All reviewer-checkable; Lemma 1 is the corrected replacement for the decertified Structural
Lemma. `ll-dyadic-symdiff`'s Sub-3b INC sub-case = G-INC-1 (shared).

## Spec concerns
None. Outline was workable. INC branch now fully rigorous for n=3 (all R, budget-valid) and reduced to
one scalar inequality for general n; GAP residual and refined-R general n remain the honest gaps.
