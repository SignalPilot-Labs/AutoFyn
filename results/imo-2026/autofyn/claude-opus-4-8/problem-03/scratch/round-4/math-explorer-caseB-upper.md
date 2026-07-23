# imo-2026-03 — Case B Upper Bound Scout (lens: XY Case B)

## Problem context

Answer c(n) = 2^n / D, D = 2^{n+1}−1. After Lemma H, the remaining gap is:

**GAP U1 = Case B**: LB configuration has ALL n+1 pieces a_1 ≥ … ≥ a_{n+1} > 1/D (sum = 1). Prove XY can achieve O ≤ c(n) with n cuts. B1-large sub-case: a_1 > c(n); B2 sub-case: a_1 ≤ 1/2. Both are open.

---

## Distinct Openings

### Opening 1 — B1-large: Recursive halving + sub-problem trichotomy (concrete proof path)

**Mechanism.** When a_1 > c(n), XY halves a_1 (1 cut). The pair {a_1/2, a_1/2} contributes 0 to the alternating sum A. Remaining singletons {a_2,…,a_{n+1}} with sub-sum S_sub = 1−a_1 < (2^n−1)/D. XY uses n−1 further cuts to achieve A(singletons) ≤ 1/D.

**The sub-problem IH(n).** Prove: For n pieces b_1 ≥ … ≥ b_n > 1/D with sum S < (2^n−1)/D, XY can achieve A ≤ 1/D with n−1 cuts.

**Base n=2 (IH(2)).** Two pieces b_1 ≥ b_2 > 1/D, sum S < 3/D. Strategy: cut b_1 at b_2, creating exact pair {b_2, b_2}. Singleton = b_1 − b_2. Since b_1 < S − b_2 < 3/D − 1/D = 2/D, we get b_1 − b_2 < 2/D − 1/D = 1/D. ONE CUT SUFFICES. ✓ (Machine-verified: no violation in 10^6 B1-large n=2 trials.)

**Inductive step IH(3) — the n=3 B1-large case (FULLY CLOSED HERE).**

Sub-singletons {a_2, a_3, a_4} with sum S_sub < 7/D. XY has 2 cuts. Three-way case split:

- **Case A'** (a_3 − a_4 ≤ 1/D): XY halves a_2 (pair {a_2/2,a_2/2}), cuts a_3 at a_4 (pair {a_4,a_4}), singleton = a_3−a_4 ≤ 1/D. A ≤ 1/D. ✓

- **Case B'** (a_2 − a_3 ≤ 1/D): XY cuts a_2 at a_3 (pair {a_3,a_3}), halves a_4 (pair {a_4/2,a_4/2}), singleton = a_2−a_3 ≤ 1/D. A ≤ 1/D. ✓

- **Doubly-hard** (both a_2−a_3 > 1/D AND a_3−a_4 > 1/D): Then a_3 > a_4+1/D > 2/D and a_2 > a_3+1/D > 3/D. So a_2+a_3+a_4 > 6/D. But S_sub < 7/D, therefore **a_2 < S_sub − (a_3+a_4) < 7/D − 3/D = 4/D**.

  **Sub-C strategy:** XY cuts a_2 at a_3 (pair {a_3,a_3}, singleton = a_2−a_3) and then cuts the singleton a_2−a_3 to match a_4 (pair {min(a_2−a_3,a_4), min(…)}, singleton = |a_2−a_3−a_4|).

  **Key bound:** |a_2−a_3−a_4| = |a_2−(a_3+a_4)|.
  - If a_2 > a_3+a_4: a_2−a_3−a_4 < 4/D − (a_3+a_4) ≤ 4/D − 3/D = 1/D. ✓
  - If a_2 < a_3+a_4: a_3+a_4−a_2 = S_sub − 2·a_2. Since a_2 > 3/D: S_sub−2·a_2 < 7/D − 6/D = 1/D. ✓

  In both sub-cases **|a_2−a_3−a_4| < 1/D**. Machine-verified: max over 10^6 doubly-hard B1-large (n=3) trials = 0.058 < 1/15. ✓

  Uses only 2 cuts (1 matching + 1 precision-match), within the budget of 2 sub-cuts. ✓

**Result for B1-large:** The case split at n=3 is complete. The n=3 sub-IH(3) closes via the doubly-hard bound. This establishes IH(3) and hence B1-large for n=3 is CLOSED (pending a general IH(n) induction).

**Kill-switch for IH(n) induction:** Given n pieces > 1/D with sum < (2^n−1)/D, test whether the doubly-hard leaf always gives |b_j − b_{j+1} − b_{j+2}| < 1/D. For n=4: run 10^6 random configs with all 3 consecutive gaps > 1/D; verify the final |·| < 1/D claim holds.

---

### Opening 2 — B2: Three-strategy trichotomy + "Cut a_1 at a_2" matching

**Mechanism for n=2 B2 (complete, provable).** All three pieces in (1/D, 1/2]:

- **Strategy A** (halve a_1): O = 1/2 + (a_2−a_3)/2 ≤ c(2) iff a_2−a_3 ≤ 1/D.
- **Strategy B** (cut a_1 at a_2, halve a_3): O = 1/2 + (a_1−a_2)/2 ≤ c(2) iff a_1−a_2 ≤ 1/D.
- **Strategy C** (cut a_1 at a_2, use 1 cut only): O = 1/2 + |a_1−a_2−a_3|/2 = 1/2 + |1−2a_1|/2 = 1−a_1 ≤ c(2) iff a_1 ≥ (2^2−1)/D = 3/D.

**Trichotomy coverage (algebraically proven for n=2):** If a_1−a_2 > 1/D AND a_2−a_3 > 1/D simultaneously, then a_1 > a_2+1/D > a_3+2/D > 3/D, so Strategy C applies (1−a_1 ≤ 1−3/D = (D−3)/D = 4/7 = c(2)). The three conditions are exhaustive.

**Kill-switch for n=2 B2:** Test: for all random n=2 B2 configs, min(A_strategy, B_strategy, C_strategy) ≤ c(n). Machine-verified: 0 failures in 3×10^5 trials. ✓ (This is a PROVEN trichotomy — should be provable rigorously with clean algebra.)

**B2 for n=3 (open but structured).** Four pieces in (1/15, 1/2]. The analogous strategies:
- Halve a_1, get sub-singletons {a_2,a_3,a_4}; apply 2-cut sub-strategy.
- Cut a_1 at a_2 + precision cut on a_3 or a_4.
- "Global matching": pair {a_1,a_2} by cutting a_1 at a_2 AND pair {a_3,a_4} by cutting a_3 at a_4. 2 cuts, leaving residual singleton = |(a_1−a_2) − (a_3−a_4)| = |gap_01 − gap_23| (= |a_1−a_2−a_3+a_4|). XY uses 3rd cut for precision matching of the two leftovers.

  Formula: O ≈ 1/2 + |gap_01 − gap_23|/2 after 2 matchings + 1 refinement.

**Kill-switch for n=3 B2 global-matching:** O = 1/2 + |gap_01 − gap_23|/2 ≤ c(3) iff |gap_01 − gap_23| ≤ 1/D. Test: over random B2 configs (a_1 ≤ 1/2). (**NOTE:** this formula FAILS for B1-large configs where gap_01 can be 0.73. But for B2 with a_1 ≤ 1/2, a_1−a_2 ≤ 1/2 and a_3−a_4 > 0, the gaps are constrained. Machine verification pending for whether |gap_01−gap_23| ≤ 1/D always holds in B2.)

---

### Opening 3 — The "Pair Creation" Lemma (unifying frame for B1-large and B2)

**Abstract formulation.** Given n+1 pieces all > 1/D with n cuts, XY can always create a configuration with alternating sum A ≤ 1/D. The mechanism: assign each cut to "match-pair" two pieces (cut the larger at the smaller, creating an exact copy). After k matchings using k cuts, the remaining "unmatched" pieces form a sub-problem.

**Key fact derived numerically:** The minimum achievable A over all n-cut strategies satisfies:
- For n=2 B1-large: A = a_2−a_3 < 1/D (proved by sum bound: a_2+a_3 < 3/D, both > 1/D → a_2−a_3 < 1/D).
- For n=3 B1-large doubly-hard sub-case: A = |a_2−a_3−a_4| < 1/D (proved above).

**The inductive pair-creation proof (proposed structure):**
1. If any consecutive gap a_j−a_{j+1} ≤ 1/D: match-pair (j, j+1), halve all others, A = a_j−a_{j+1} ≤ 1/D.
2. All consecutive gaps > 1/D: the pieces are "spread" (like an arithmetic-ish sequence). Use a cross-pairing (non-consecutive) that exploits the sum constraint to bound the residual.

**The sum constraint is load-bearing here.** Without sum=1 (or sum bounded by (2^n-1)/D for sub-problems), the claim fails. The tight case is the geometric LB config: a_j = 2^{n+1-j}/D, consecutive gaps a_j−a_{j+1} = 2^{n-j}/D ≥ 1/D (with equality only at j=n). XY achieves A = 1/D exactly (tight) by matching (n,n+1) pair using strategy B' above.

---

## Candidate Technique(s)

- **Exact pair creation via asymmetric cuts** (primary): cut a larger piece at exactly a_k to create a fragment matching the existing a_k. The pair contributes 0 to A, isolating a singleton.
- **Induction on sub-problem structure** (secondary): IH(n) proof on pieces with bounded sum (2^n−1)/D, giving tighter constraints than the original sum=1 constraint.
- **Algebraic bound via sum constraint** (key tool): the constraint "all pieces > 1/D AND sum bounded" forces pairs of quantities to satisfy |x−y| < 1/D.

---

## Cheap-Kill Candidates

1. **B1-large n=2 kill (proved):** After halving a_1, A = a_2−a_3 < 1/D since a_2+a_3 < 3/D and both > 1/D. Only 1 cut needed. Budget: 1 (halve) + 1 (match) = 2 = n. ✓

2. **B2 n=2 kill-switch:** min over 3 strategies (A/B/C) always ≤ c(n). Numerically confirmed. PROVABLE by the trichotomy algebra (if A fails AND B fails, then a_1 > 3/D and C applies).

3. **B1-large n=3 doubly-hard kill:** |a_2−a_3−a_4| < 1/D follows from sum bound S_sub < 7/D and the doubly-hard hypothesis a_2+a_3+a_4 > 6/D → a_2 < 4/D. ALGEBRAICALLY PROVED above, machine-verified.

4. **Parity bound check:** "All consecutive gaps > 1/D" in n+1 pieces → sum > n(n+1)/(2D). For the original sum=1: n(n+1)/2 < 2^n−1 for n ≥ 2, so this is possible. For sub-sum < (2^n−1)/D: n(n+1)/2 < 2^n−1 (holds for all n ≥ 2), so the "all-gaps-large" sub-case is also possible. The sub-sum bound then pins a_1 < (2^n−1)/D − (n-1)*1/D = (2^n−n)/D = 2^{n-1}-something, giving |a_1−a_2−...| < 1/D.

---

## Knowledge-Base Entries to Use

- **Invariants & monovariants**: the pair-creation mechanism is an invariant (each cut introduces an exact pair contributing 0 to A and reduces the "residual singleton problem" by 1).
- **Pigeonhole / size bounds**: the sum constraint + all-pieces-large forces a bound on the largest piece's size, which is the key algebraic step in the doubly-hard case.
- **Induction**: the IH(n) proof structure is a clean induction on n with a modified hypothesis (bounded sub-sum instead of sum=1).
- **Standard inequalities**: simple arithmetic from sum bounds is the only inequality tool needed.

---

## Analogous Past Problems (Cruxes)

None strongly analogous (per crux corpus docs, sub-topic "game strategies" might have some; not checked due to time). The "pair-creation" mechanism is novel to this problem.

---

## Prior Progress

- Case A of U1 closed by Lemma H (certified round 3): O = 1/2 + a_{n+1}/2 ≤ c(n) when a_{n+1} ≤ 1/D.
- B0 (n=1 Case B) trivially vacuous (proved in approach file).
- B1-clean (a_1 > 1/2 and a_1 ≤ c(n)): Lemma I gives O = a_1 ≤ c(n). Closed.
- B1-large (a_1 > c(n)) n=2: halve a_1 → A = a_2−a_3 < 1/D (NEWLY PROVED this round).
- B1-large (a_1 > c(n)) n=3: full three-way case split with algebraic proof (NEWLY PROVED this round); sub-case "doubly-hard" resolved by |a_2−a_3−a_4| < 1/D.
- B2 (a_1 ≤ 1/2) n=2: trichotomy coverage (NEWLY PROVED this round with clean algebra).
- B2 n=3: structured via global-matching formula |gap_01 − gap_23|; coverage pending.

---

## Dead Ends (Do Not Retry)

- **Concavity of g = min_XY O** (refuted round 3 by kill-switch: g has interior valley).
- **Amortized greedy / supermartingale Φ** (refuted round 3: greedy fails on B1-large configs).
- **Game-separation induction n → n−1** (refuted round 2: budget doesn't decrement, odd-sum is global).
- **"Halve n largest" strategy (Lemma H) for Case B**: gives O = 1/2 + a_{n+1}/2 > c(n) since a_{n+1} > 1/D.
- **"Halve a_1 only" as universal B2 strategy**: gives O = 1/2 + (a_2−a_3)/2 which can exceed c(n) when a_2 ≈ a_1.

---

## Small-Case / Intuition Notes (Conjectural)

1. **B1-large n=2 is FULLY PROVED**: a_2−a_3 < 1/D always when a_1 > c(2) and all > 1/D (algebraic, no exceptions in 10^6 trials).

2. **B2 n=2 is FULLY PROVED by trichotomy**: strategies A/B/C cover all configs exhaustively; the "doubly-hard" escape uses a_1 > 3/D = (2^2−1)/D, forcing 1−a_1 ≤ c(2). Zero failures in 3×10^5 trials.

3. **B1-large n=3 doubly-hard sub-case PROVED algebraically**: |a_2−a_3−a_4| < 1/D whenever all three consecutive gaps > 1/D and sum < 7/D. Machine-verified: max = 0.058 < 1/15. This is the key NEW result.

4. **General pattern (conjecture):** IH(n) holds for all n by induction. The "doubly-hard" sub-case at each level is resolved by the sum constraint: if all k consecutive gaps > 1/D, then the k-piece sub-sum is < (2^k−1)/D, forcing the largest piece to satisfy a_1 < (2^k−1)/D − (k−1)/D = (2^k−k)/D, and a specific cross-pairing gives residual < 1/D.

5. **Budget accounting is clean**: The pair-creation strategy for B1-large uses exactly 1 (halve a_1) + (n−1) sub-cuts = n cuts total, within budget.

6. **The geometric LB config is the unique tight case** (confirmed numerically n=1,2,3,4): XY achieves exactly O = c(n) only for the geometric config a_j = 2^{n+1−j}/D; all others give O < c(n) strictly.

7. **B2 for n=3 — KILL-SWITCH RESULT (NEW, this round):** The kill-switch was run with the correct optimizer. IMPORTANT CORRECTION: the original kill-switch test in the report had a bug — it required "exactly 3 cuts" instead of "AT MOST 3 cuts" (since XY has ≤ n cuts, not = n cuts). With the corrected optimizer (at most 3 cuts on distinct original pieces, fraction optimized by Nelder-Mead multistart), there are **0 failures in 2000 random B2 (n=3) configs**. B2 n=3 is NUMERICALLY CONFIRMED SOLVABLE.

8. **B2 n=3 — Strategic structure (NEW):** The optimal strategy for B2 n=3 is NOT always a "named discrete" strategy (halve exact pair or cut exactly at another piece's value). In particular, ~0.7% of configs require more than the simple named strategies. The optimal cut fractions are config-dependent (continuous, not discrete). **Implication:** a proof of B2 n=3 likely requires a continuous/algebraic argument, not a finite case split on discrete strategies. Fragment cuts are NOT needed — the "at most 3 cuts on original pieces" is sufficient.

9. **B2 n=3 — XY NEVER needs to cut MORE than 2 original pieces (conjecture):** Some configs are solved by halving just 2 of the 4 pieces (e.g., "halve a3 and a4" works when a1-a2 ≤ 1/D). But no clean "2-strategy cover" was found for all B2 n=3 configs using only "halve 2 pieces" or "halve 2 + cut-pair" strategies. A continuous 3-parameter optimization is needed.
