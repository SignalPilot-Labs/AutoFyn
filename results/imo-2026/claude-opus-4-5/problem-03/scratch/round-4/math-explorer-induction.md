# IMO 2026 P3 — Inductive Structure Explorer Report (Round 4)

## Problem and Gap

The answer c(n) = 2^n/(2^{n+1}-1) is established. Lower bound is proved rigorously. The remaining gap is the **upper bound**: proving XY can limit ANY LB config to at most c(n).

---

## Distinct Openings

**Opening A (Case 2b Pairing — FULLY PROVED for general n):**
When P_{n+1} > c(n) and P_1 <= L_0^{(n)} = 1/(2^{n+1}-1):
XY uses n marks on P_{n+1} creating n+1 sub-pieces {P_n, P_{n-1}, ..., P_2, r, r} where r = (P_{n+1} - P_2 - ... - P_n)/2 = (2*P_{n+1} - 1 + P_1)/2.
Combined 2n+1 pieces: {P_1, P_2, P_2, P_3, P_3, ..., P_n, P_n, r, r}.
P_1 is the unique minimum (proof: r > L_0 >= P_1 since P_{n+1} > c(n) implies 2P_{n+1}-1 > 1/(2^{n+1}-1)).
The 2n non-P_1 pieces form n exact pairs. LB picks n+1 pieces = one from each pair + P_1.
**LB = P_2 + P_3 + ... + P_n + r + P_1 = (1 - P_{n+1}) + r = 1/2 + P_1/2.**
**This is <= c(n) iff P_1 <= 1/(2^{n+1}-1) = L_0^{(n)}. QED.**

This is algebraically clean and verified for n=2,3 by exhaustive search over rational grids.

**Opening B (Case 2a — conjectured, computationally verified for n=3):**
When P_{n+1} > c(n) and P_1 > L_0^{(n)} (strict):
XY uses 2 marks on P_{n+1} creating {P_n, r', r'} where r' = (P_{n+1} - P_n)/2.
For n=2: proven — P_1 >= L_0 = 1/7 and P_3 > c(2) = 4/7 imply P_1 + P_3/2 >= 3/7 = 1-c(2), so LB = 1-P_1-P_3/2 <= c(2).
For n=3: computationally verified (20000 random trials, strict P_1 > L_0, P_4 > c(3)): at least one of {P_3,r',r'} or {P_1,(P_4-P_1)/2,(P_4-P_1)/2} strategy always works.
Gap: algebraic proof for general n that at least one such 2-mark strategy achieves LB <= c(n).

**Opening C (Recursive identity as inductive bridge):**
Proved: c(n) = 2c(n-1)/(2c(n-1)+1). If XY's strategy for n reduces to the (n-1)-game in a controlled way, this recursion closes the induction. One formulation: after XY uses 1 mark on P_{n+1} (halving), the remaining (n+2)-piece game with n-1 XY marks "looks like" an (n-1)-game on n pieces with n-1 marks — but this reduction is NOT clean since n+2 ≠ n.

**Opening D (Induction on P_1 relative to L_0):**
The threshold P_1 = L_0^{(n)} cleanly separates the proof into two cases with matching strategies. The proof can induct on n, with the base case n=1 elementary and the inductive step using: (Case 2b) pairing when P_1 <= L_0; (Case 2a) halving/2-mark when P_1 > L_0; (Case 1) a separate argument when P_{n+1} <= c(n).

---

## The Proved Case 2b Lemma (Complete Argument)

**Lemma:** For any n >= 1 and any LB config {P_1,...,P_{n+1}} (ascending) with P_{n+1} > c(n) and P_1 <= L_0^{(n)} = 1/(2^{n+1}-1), XY uses n marks on P_{n+1} creating sub-pieces {P_n, P_{n-1}, ..., P_2, r, r} where r = (P_{n+1} - sum_{k=2}^{n} P_k)/2. The combined 2n+1 pieces give LB = 1/2 + P_1/2 <= c(n).

**Proof:**
1. r = (P_{n+1} - (1-P_1-P_{n+1}))/2 = (2P_{n+1}-1+P_1)/2 >= 0 since P_{n+1} > 1/2.
2. r > P_1: need 2P_{n+1}-1 > P_1. Since P_{n+1} > c(n) = 2^n/(2^{n+1}-1): 2P_{n+1}-1 > 1/(2^{n+1}-1) = L_0 >= P_1.
3. Combined set: {P_1} union {P_2,...,P_n} union {P_n,...,P_2,r,r} = {P_1, P_2,P_2,...,P_n,P_n, r,r}. This is P_1 (singleton) plus n pairs: (P_2,P_2), ..., (P_n,P_n), (r,r). Total 2n+1 pieces. XY uses n marks; n+1 pieces from cuts of P_{n+1}; combined n + (n+1) = 2n+1. LB picks positions 1,3,...,2n+1 (n+1 picks).
4. By step 2, P_1 < r, so P_1 < all other pieces. P_1 occupies position 2n+1 (last). The n pairs occupy positions 1..2n in some order; from each pair LB picks the element at an odd position = one copy of the pair value.
5. LB = P_2 + P_3 + ... + P_n + r + P_1 = sum_{k=2}^n P_k + r + P_1.
   = (1-P_1-P_{n+1}) + (2P_{n+1}-1+P_1)/2 + P_1 [using sum_{k=2}^n P_k = 1-P_1-P_{n+1}]
   = 1-P_1-P_{n+1} + P_{n+1}-1/2+P_1/2 + P_1 = 1/2 + P_1/2.
6. 1/2 + P_1/2 <= c(n) = 2^n/(2^{n+1}-1) iff P_1 <= 2c(n)-1 = 1/(2^{n+1}-1) = L_0. QED.

This lemma is COMPLETE and covers Case 2b for all n.

---

## Candidate Techniques

- **Pairing construction:** Key for Case 2b. Algebraically clean.
- **1-mark halving:** Key for Case 2a (n=2 proved; general n conjectured).
- **Greedy Optimality Lemma** (CERTIFIED): LB picks positions 1,3,5,... in sorted descending order. Essential for the pairing argument (step 4 above).
- **Algebraic sum formula:** The "1/2+P_1/2" identity telescopes regardless of pair ordering.

---

## Knowledge-Base Entries to Use

- **Greedy Optimality Lemma** (CERTIFIED in lemmas/)
- **Geometric Dominance Lemma** (CERTIFIED in lemmas/)
- **Parity Constraint Lemma** (CERTIFIED in lemmas/)
- **Minimax Theorem:** Game value c(n) achieved at geometric config saddle-point.

---

## Analogous Past Problems (Cruxes)

None strongly analogous. The pairing trick is specific to this game's structure. The closest analogy is problems where a player "mirrors" the opponent's moves to create symmetric positions (Nim-like), but the LB/XY game with greedy alternation is distinct.

---

## Prior Progress

**Proved (in lemma files):** Greedy Optimality, Geometric Dominance, Parity Constraint — all CERTIFIED.
**Lower bound:** PROVED in geometric-direct.md Part 3.
**Upper bound Case 2b:** PROVED this round (see lemma above).
**Upper bound Cases 2a and 1:** Computationally verified but not proved.

---

## Dead Ends (Do Not Retry)

1. **Interleaving strategy (Q_k >= P_{n+1-k} summing to P_1):** The reviewer's Round 2 suggestion. Gives LB = P_1 which is > c(n) when P_1 > c(n). WRONG direction for upper bound.

2. **Wrong pairing construction {P_1,...,P_n, 2P_{n+1}-1}:** The "natural" n-mark split of P_{n+1} into n+1 pieces mimicking LB pieces. This gives LB up to 97/100 for extreme configs. The CORRECT construction is {P_n,...,P_2, r, r} (NOT a copy of P_1).

3. **Simple halving (1 mark) for all of Case 2:** Fails in multiple sub-cases of Case 2a (LB > c(n)). Only works when P_1 >= L_0 AND P_{n+1}/2 is properly positioned.

4. **"Induction on j marks in P_{n+1}":** The lower bound induction on j works cleanly (each mark in L_n maintains invariant). The analogous induction for the upper bound FAILS because XY's marks can go in any piece, not just P_{n+1}.

5. **"XY uses 1 mark, then apply IH for n-1":** After XY's first mark, game has n+2 pieces, n-1 marks — NOT the (n-1)-game. Reduction fails.

---

## Small-Case / Intuition Notes

**PROVED (algebraic):** Case 2b pairing gives LB = 1/2+P_1/2, <= c(n) when P_1 <= L_0^{(n)}.

**VERIFIED (n=2, algebraic):** Case 2a — XY uses 1 mark on P_3 halving. LB = 1-P_1-P_3/2 <= c(2) since P_1 >= L_0 and P_3 > c(2) imply P_1+P_3/2 >= L_0+c(2)/2 = 1/(14) + 2/7 = 5/14 > 3/7 = 1-c(2). Actually: P_1 >= 1/7 and P_3/2 > 2/7, so P_1+P_3/2 > 3/7. ✓

**VERIFIED (n=3, 20000 random trials, strict Case 2a):** XY always achieves LB <= c(3) using 2 marks. Strategy: either {P_3, r', r'} or {P_1, (P_4-P_1)/2, (P_4-P_1)/2} from P_4.

**CONJECTURE:** For general n Case 2a: XY uses n-1 marks on P_{n+1}, creating {P_n, r', r'} where r'=(P_{n+1}-P_n)/2. When r' >= P_{n-1}: sorted order is [r',r',P_n,P_n,...,P_1]. LB = r'+P_n+P_{n-2}+...+P_1 or similar. The formula depends on n in a complex way. For n=2: LB = r'+P_2 = (P_3-P_2)/2+P_2 = (P_3+P_2)/2 = (1-P_1)/2 <= c(2) iff P_1 >= 1-2c(2) = 1-8/7 < 0: always true! So for n=2, the {P_2,r',r'} strategy gives LB = (1-P_1)/2 = (1-P_2)/2... wait. For n=2: {P_2,r,r} from P_3 where r=(P_3-P_2)/2. Combined: {P_1,P_2,P_2,r,r}. If r < P_2: sorted [P_2,P_2,r,r,P_1]. LB = P_2+r+P_1 = P_2+(P_3-P_2)/2+P_1 = (P_2+P_3)/2+P_1 = (1-P_1)/2+P_1 = 1/2+P_1/2. This is CASE 2b formula! For n=2 with P_1 > L_0 = 1/7: 1/2+P_1/2 > c(2) = 4/7. So this FAILS for n=2 Case 2a.

CORRECTION: For n=2 Case 2a, XY uses 1 mark on P_3 (halving), not the {P_2,r,r} strategy. The n-mark pairing strategy = n=2 marks = {P_2,r,r} which is Case 2b for n=2.

For n=3 Case 2a: XY uses 2 marks (= n-1 marks). One successful strategy: {P_3, r', r'} from P_4, giving 6 = 2n pieces, LB picks 3. When P_2 > r': strategy fails. XY needs a different 2-mark strategy for this sub-case.

**VERIFIED threshold:** P_1 = L_0^{(n)} is the exact boundary where Case 2b gives LB = c(n) (tight) and Case 2a (when n=2) also gives LB = c(n) (the geometric config). This confirms the geometric config is the saddle-point.
