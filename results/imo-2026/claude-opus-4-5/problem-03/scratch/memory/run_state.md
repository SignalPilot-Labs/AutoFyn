## Goal
Solve IMO 2026 P3 (imo-2026-03).
Metric: proof-reviewer verdict. Eval: read `results/imo-2026-03/current.md` Status and reviewer report. Baseline: unsolved. Target: solved. Constraint: rigorous proof with explicit formula for c(n).

## Goal Updates

## Eval History
- R1 baseline: Status `unsolved`, no approaches yet.
- R1 end: Status `partial`. Answer c(n) = 2^n/(2^{n+1}-1) verified for n=1,2,3. Lower bound proven. Upper bound gap: need rigorous proof that XY can limit ANY LB marking to ≤c(n). IMPROVED.
- R2 end: Status `partial`. induction-on-n built and reviewed. **Lemma 5 (pigeonhole bound) is FALSE** — counterexample found: [107/700, 93/350, 407/700] for n=2 violates both conditions. Answer still computationally verified correct. Lower bound rigorous. Upper bound proof needs different argument. PLATEAU (gap persists, now better characterized).
- R3 end: Status `partial`. k*-LARGEST pigeonhole approach attempted: use k* = max{k : p_k ≤ 2^{k-1}·S·t_m}. Upper bound Case A (k* < m+1) is now RIGOROUS: ratio > 2 prevents interleaving, sub-problem size bound gives algebraic cancellation. Upper bound Case B (k* = m+1, "sandwich case") remains GAP: no proof that XY can achieve A ≤ S·t_m when all pieces p_1,...,p_m exceed geometric thresholds. Numerical evidence supports but no rigorous proof. IMPROVED (partial progress, gap narrowed to one case).
- R4 end: Status `solved`. BREAKTHROUGH. Explorers found sandwich case fix: XY cuts p_{m+1} at p_m, creating pair (p_m, p_m) at positions 1-2 that cancels. Sub-problem sum S-2p_m handled by P(m-1). Bound (S-2p_m)·t_{m-1} ≤ S·t_m follows from sandwich condition. Proof-reviewer APPROVE 10/10 on all criteria.

## Rules
- ALWAYS: Upper bound requires showing G(L, XY_response) ≤ c(n) for ALL LB markings L, not just geometric.
- ALWAYS: XY's optimal response is NOT always halving — unequal splits can be better.
- NEVER: Use Lemma 5 "p_1 ≤ t_n OR p_{n+1} ≤ c(n)" — it is FALSE (R2 counterexample).
- ALWAYS: Pair-cancellation lemma requires pairs to be consecutive in sorted order — verify this condition holds before applying.
- ALWAYS: When applying k*-largest approach, verify k* < m+1 before using halve+recurse. The sandwich case k* = m+1 needs separate treatment.
- ALWAYS: In sandwich case (k* = m+1), use create-duplicate strategy: cut p_{m+1} at p_m to create pair (p_m, p_m).

## State
**Done:** 
- R1: explored problem (3 explorers), outlined 3 approaches, built 2 (geometric-dominance, induction-on-n), both partial.
- R2: 2 explorers (direct UB, framing), outliner revised field (added ratio-based-induction, exchange-argument), built induction-on-n. Reviewer found Lemma 5 false. Still partial.
- R3: 3 explorers (potential/minimax, ratio/threshold, exchange/variational) found k*-largest fix. Outliner revised induction-on-n with k*-largest. Builder proved Case A rigorously. Case B (sandwich) remains gap.
- R4: 2 explorers (asymmetric splits, reduction) found sandwich case fix. Outliner revised induction-on-n with create-duplicate strategy. Builder completed Case B. Proof-reviewer APPROVE. STATUS: SOLVED.

**Broken:** None.

**Next:** Problem solved. Session can end.
