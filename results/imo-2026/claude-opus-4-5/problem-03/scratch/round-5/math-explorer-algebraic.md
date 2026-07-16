## imo-2026-03 (Algebraic Structure Lens)

### Problem Recap
c(n) = 2^n/(2^{n+1}-1). Lower bound proved; Case A upper bound proved; Case B upper bound (P_1 > L_0) is the only gap.

---

## Key Algebraic Identities (all verified)

**Identity 1 (Boundary):** 2c(n) - 1 = L_0(n) = 1/(2^{n+1}-1). Equivalently c(n) = 1/2 + L_0/2.
Meaning: the Case A upper bound formula LB = 1/2 + P_1/2 equals c(n) exactly when P_1 = L_0. The geometric config (P_1 = L_0) is the unique LB config where the Case A formula is tight. Case A gives LB ≤ c(n) iff P_1 ≤ L_0; Case B is exactly when this formula would give LB > c(n).

**Identity 2 (Recurrence):** c(n) = 2c(n-1) / (1 + 2c(n-1)) for all n ≥ 2.
Equivalently: (1-c(n))/c(n) = 1/(2c(n-1)). This is a Möbius transformation; the inverse is c(n-1) = c(n) / (2(1-c(n))). Verified numerically for n=2,...,6.

**Identity 3 (Complement):** 1 - c(n) = (2^n-1)/(2^{n+1}-1) = (2^n-1) * L_0(n).
So c(n) + (1-c(n)) = 1 and both c(n), 1-c(n) are rational with denominator 2^{n+1}-1.

**Identity 4 (XY mark rule):** Note from experiments that XY uses n-1 marks (not n) in Case B for all n ≥ 2. Using exactly n-1 marks creates n+1+(n-1) = 2n total pieces. LB picks ceil(2n/2) = n pieces. With 2n pieces summing to 1 and LB picking n, if pieces form n equal pairs then LB = exactly 1/2 < c(n).

---

## Geometric Config at the Boundary: Why It's Not a Coincidence

The geometric config has P_1 = L_0. The Case A formula gives LB = 1/2 + L_0/2 = c(n) exactly. This is the MAXIMUM of LB = 1/2 + P_1/2 subject to P_1 ≤ L_0. So the geometric config is the hardest Case A config for XY.

No Case A config can beat the geometric config: for ALL P_1 ≤ L_0, LB ≤ c(n). The geometric config achieves LB = c(n) exactly by sitting at the boundary P_1 = L_0, where the pairing formula is tight.

The boundary P_1 = L_0 also makes c(n) = 1/2 + L_0/2. This is the defining characterization: c(n) is the unique value satisfying c = 1/2 + (2c-1)/2 (the boundary P_1 = 2c-1 gives LB = 1/2 + P_1/2 = c).

---

## Case B: What the Algebra Reveals

**Computational finding:** For ALL Case B configs tested (n=2,3,4), XY using n-1 marks achieves LB ≤ c(n). In fact LB ≤ 1/2 < c(n) in many cases.

**Key distinction from Case A:** In Case A, XY uses ALL n marks (on P_{n+1}), creating 2n+1 pieces (odd), leaving P_1 as a "free singleton" for LB → LB = 1/2 + P_1/2.
In Case B, XY uses n-1 marks, creating 2n pieces (even), LB picks n = half the pieces. If XY can create n pairs, LB = 1/2 < c(n). There is NO "free singleton" contribution.

**Case B has a clean sub-case analysis (proved for n=2, conjectured for general n):**

For n=2 (P_1 > 1/7, P_1 ≤ P_2 ≤ P_3, sum=1):

Sub-case B2 (P_3 > c(n) = 4/7): 
- P_1 > 1/7 AND P_3 > 4/7 forces P_1+P_2 < 3/7, hence P_2 < 2/7, hence P_2-P_1 < 2/7-1/7 = 1/7 = L_0.
- XY halves P_3 (1 mark). Pieces: {P_1, P_2, P_3/2, P_3/2}. LB picks 2. LB = (1+P_2-P_1)/2 < (1+L_0)/2 = c(2). PROVED.
- This is a direct algebraic consequence: large P_3 forces small gap P_2-P_1 < L_0.

Sub-case B1-b (3/7 ≤ P_3 ≤ 4/7):
- XY splits P_3 at P_2 (1 mark). Pieces: {P_1, P_2, P_2, P_3-P_2}.
- If P_3 ≥ 1/2: P_3-P_2 ≥ P_1 (since P_3 ≥ P_1+P_2). Sorted: [P_2, P_2, P_3-P_2, P_1] giving LB = P_2+(P_3-P_2) = P_3 ≤ c(2). PROVED.
- If P_3 < 1/2: P_3-P_2 < P_1. Sorted: [P_2, P_2, P_1, P_3-P_2] giving LB = P_2+P_1 = 1-P_3 ≤ 1-3/7 = 4/7 = c(2). PROVED.

Sub-case B1-a (P_3 < 3/7, i.e., P_1+P_2 > 4/7):
- Strategy "halve P_2": LB = 1-P_1-P_2/2. Works iff 2P_1+P_2 ≥ 6/7.
- Strategy "halve P_1": LB = 1-P_1/2-P_2. Works iff P_1+2P_2 ≥ 6/7.
- If BOTH fail: 3(P_1+P_2) < 12/7, so P_1+P_2 < 4/7. But P_3 < 3/7 means P_1+P_2 > 4/7. Contradiction. PROVED.

Therefore: for n=2, at least one 1-mark XY strategy always works. The 3 sub-cases are mutually exclusive and exhaustive.

---

## The Recurrence as an Induction Handle

**Identity:** c(n) = 2c(n-1)/(1+2c(n-1)) means c(n)(1+2c(n-1)) = 2c(n-1), so:
  c(n) * 1 + c(n) * 2c(n-1) = 2c(n-1)
  c(n) = 2c(n-1)(1 - c(n)).

Rearranged: c(n-1) = c(n)/(2(1-c(n))).

**Game-theoretic interpretation:** When XY uses 1 mark optimally (halving the largest LB piece P_{n+1}), the resulting game might reduce to a (n-1)-mark subgame. The recurrence says c(n-1) is determined by c(n) in exactly the way expected if "one XY mark halves the problem."

**Potential inductive proof of Case B upper bound:**
- Base: n=1. If P_1 > L_0(1)=1/3 then P_2 < 2/3 = c(1). XY uses 0 marks; LB = P_2 < c(1). Done.
- Inductive step: Given P_1 > L_0(n), show XY can achieve LB ≤ c(n) using n-1 marks.
  - XY uses 1 mark on P_{n+1} to create {Q, P_{n+1}-Q} for suitable Q.
  - The remaining n-1 marks are applied to an effective (n-1)-piece sub-game.
  - The recurrence c(n) = 2c(n-1)(1-c(n)) should govern the reduction.

The key question is: which Q does XY choose for the first mark?

---

## Critical Algebraic Finding: Case B Sub-case Structure for General n

**Sub-case B2 (P_{n+1} > c(n)):** When P_1 > L_0(n) and P_{n+1} > c(n):
- P_1+...+P_n = 1-P_{n+1} < 1-c(n) = (2^n-1)*L_0(n).
- Each P_k ≤ P_{n+1} ≥ c(n) and each P_k ≥ P_1 > L_0(n).
- n pieces each > L_0(n) summing to < (2^n-1)*L_0(n). This forces maximum piece gap.
- Specifically: max(P_2,...,P_n) - P_1 < [(2^n-1)*L_0-n*L_0]/something... **algebraically force P_n-P_1 < L_0?**
- For n=2: proved P_2-P_1 < L_0. For general n: THIS IS THE KEY CLAIM NEEDED.

Computational evidence (n=2,3,4): In Sub-case B2, the piece spread is controlled and XY can halve P_{n+1} (using 1 mark) to reduce to a Sub-case B1 problem for the remaining n-2 marks.

**Sub-case B1 (P_{n+1} ≤ c(n)):** XY uses the "greedy pairing" strategy.
- XY uses n-2 marks on P_{n+1} to create sub-pieces {P_1, ..., P_{n-2}, s_1, s_2} (matching first n-2 pieces).
- One more mark (the n-1-th) splits the remainder to create the final pair.
- Resulting singletons: s_1 = P_n, s_2 = P_{n+1}-(P_1+...+P_{n-1}) = 2P_{n+1}-1+P_n... wait: 
  s_2-s_1 = 2P_{n+1}-1. So |s_2-s_1| = |2P_{n+1}-1|.
- LB = 1/2 + |2P_{n+1}-1|/2 = max(P_{n+1}, 1-P_{n+1}).
- For P_{n+1} ∈ [1-c(n), c(n)]: LB = max(P_{n+1}, 1-P_{n+1}) ≤ c(n). WORKS.
- For P_{n+1} < 1-c(n): greedy pairing gives LB = 1-P_{n+1} > c(n). Need different strategy.

**Sub-case B1-a (P_{n+1} < 1-c(n)):** All pieces are < 1-c(n). Sum=1, n+1 pieces all < 1-c(n):
  P_1+...+P_n > 1-(1-c(n)) = c(n). Combined with P_1 > L_0(n) and n pieces summing to > c(n):
  At least one piece P_k > c(n)/n. This "balance" allows a complementarity argument (as for n=2).
  Strategy: At least one of {halve P_1, halve P_2, ..., halve P_n} gives LB ≤ c(n).
  Algebraic reason: If ALL halvings fail, summing the failure conditions leads to a contradiction
  with P_1+...+P_n > c(n) (analogous to n=2 argument where contradiction was P_1+P_2 < 4/7).

---

## Distinct Openings for the Outliner

**Opening 1 (Sub-case coverage, direct):** Prove Case B for general n by splitting into:
- B2 (P_{n+1} > c(n)): Show P_k-P_1 < L_0(n) for all k ≤ n (from the constraint P_1+...+P_n < (2^n-1)*L_0). Then halve P_{n+1}.
- B1-b (P_{n+1} ∈ [1-c(n), c(n)]): XY uses greedy pairing (n-1 marks on P_{n+1}).
- B1-a (P_{n+1} < 1-c(n)): Complementarity argument for halvings of smaller pieces.

**Opening 2 (Induction via recurrence):** Use c(n) = 2c(n-1)/(1+2c(n-1)) to give a direct inductive proof. XY's first mark reduces the n-mark game to a (n-1)-mark subgame whose value is c(n-1). The recurrence guarantees c(n) = correct value.

**Opening 3 (Even-parity trick):** XY uses n-1 marks to create 2n pieces, ensuring LB picks exactly n pieces summing to ≤ 1/2 < c(n). Prove this is always achievable when P_1 > L_0 by showing the pieces can always be arranged in n pairs. The condition P_1 > L_0 is exactly what guarantees this (prevents P_1 from being an "uncancelable singleton").

**Opening 4 (LP duality):** Invoke the minimax theorem. Since the game has finite piece-count structure and the strategy spaces are compact, by Fan's minimax theorem, the order of max/min can be exchanged. The geometric config proves the max is achieved at c(n). Existence of the minimizing XY strategy is guaranteed without construction. Then separately prove that the Case A XY strategy achieves c(n) against the geometric config to establish the saddle point. (Non-constructive but avoids Case B explicit construction.)

---

## Candidate Technique(s)
- **Möbius recurrence induction**: The recurrence c(n) = 2c(n-1)/(1+2c(n-1)) provides an inductive structure where XY's first mark "reduces" the problem.
- **Even-parity pairing**: Creating 2n pieces with n pairs guarantees LB = 1/2 < c(n).
- **Complementarity / covering argument**: Multiple XY strategies whose failure conditions contradict a sum constraint (as proved for n=2).

## Cheap-Kill Candidates
- **Sub-case B2 (P_{n+1} > c(n))**: The constraint P_1+...+P_n < (2^n-1)*L_0 combined with n pieces each > L_0 forces the spread P_n-P_1 < (2^n-1-n)*L_0/(n-1)... check if this forces all P_k-P_1 ≤ L_0. If yes, XY halving P_{n+1} gives LB < c(n) by formula.
- **For Sub-case B2**: Verify explicitly that P_j-P_1 < L_0 for all j ≤ n when P_1 > L_0 and P_{n+1} > c(n). (For n=2 this is: P_2-P_1 < L_0. Proved above. For general n: needs checking.)

## Knowledge-Base Entries to Use
- **Invariants & monovariants**: The formula LB = 1/2 + P_1/2 (Case A) is a linear invariant of the pairing strategy. Case B breaks this invariant by using fewer marks.
- **Constructive vs. existence**: For Case B, the three sub-cases need constructive XY strategies (Opening 1) OR minimax duality (Opening 4).
- **Induction**: The recurrence c(n) = 2c(n-1)/(1+2c(n-1)) screams for induction. Opening 2.
- **Pigeonhole / extremal**: Sub-case B2 uses: sum of n pieces < (2^n-1)*L_0, each > L_0, to bound the spread. This is a pigeonhole/averaging argument.

## Analogous Past Problems
- None identified — this specific stick-division game structure doesn't obviously match crux-corpus problems. The algebraic structure (Möbius recurrence, boundary identity, even/odd parity of pieces) is unusual.

## Prior Progress
- Case A (P_1 ≤ L_0): FULLY PROVED for all n. LB = 1/2 + P_1/2 ≤ c(n).
- Lower bound (geometric config achieves c(n)): FULLY PROVED for all n.
- Case B (P_1 > L_0): verified computationally for n=2,3 (prior rounds) and n=4 (this round). Gap = general algebraic proof.

## Dead Ends (Do Not Retry)
- "XY uses n marks in Case B" → gives LB = 1/2 + P_1/2 > c(n). Wrong.
- "XY halves P_{n+1} universally in Case B" → fails for n=4 (some configs need more marks).
- "Arithmetic config beats geometric" → WRONG, confirmed Round 2.
- "Greedy pairing alone covers all of Case B" → only covers P_{n+1} ∈ [1-c(n), c(n)]; fails for P_{n+1} outside this range.

## Small-Case / Intuition Notes (Conjectural)

**Conjectured Sub-case B2 lemma:** For P_1 > L_0(n) and P_{n+1} > c(n), we have P_j - P_1 < L_0(n) for all j ≤ n. (Proved for j=2, n=2. Numerical evidence for n=3,4 in Sub-case B2.)

**If this lemma holds:** XY halves P_{n+1} (1 mark), giving 4 remaining pieces {P_1,...,P_n, P_{n+1}/2, P_{n+1}/2} with XY having n-2 more marks. The spread among P_1,...,P_n being < L_0 suggests applying Case A logic to the sub-game.

**Boundary behavior:** The geometric config (P_1 = L_0, P_k = 2^{k-1}*L_0) sits EXACTLY at the boundary between Case A (LB ≤ c(n)) and Case B (LB > c(n) from Case A strategy). This boundary is NOT a coincidence: the geometric config is the unique saddle point of the minimax game, where both players are "optimal." LB achieves c(n) and can't do better; XY achieves c(n) and can't do better.

**Key open claim:** For general n, when P_1 > L_0, XY's optimal strategy uses n-1 marks to create 2n pieces. LB picks n pieces summing to ≤ 1/2 < c(n). The explicit XY algorithm for n-1 marks follows from one of Opening 1 (sub-case coverage), Opening 2 (recurrence induction), or Opening 3 (pairing existence).
