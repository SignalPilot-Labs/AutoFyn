## imo-2026-03 (Case B upper bound lens)

### Summary of findings this round

**MAJOR DISCOVERIES** (new this round, not in prior reports):

---

### 1. Simplified / Unified Case A proof

**Claim**: When P1 ≤ L0(n) = 1/(2^{n+1}-1), XY uses the following strategy with exactly n marks:
- Place one mark at the midpoint of EACH of P2, P3, ..., P_{n+1} (one mark per piece, n marks total).
- New pieces: {P1, P2/2, P2/2, P3/2, P3/2, ..., P_{n+1}/2, P_{n+1}/2}.

By the certified Pairing Cancellation Lemma, applied n times (once per pair {Pk/2, Pk/2}):
LB = (P2+P3+...+P_{n+1})/2 + lb_score({P1}) = (1-P1)/2 + P1 = 1/2 + P1/2.

This is ≤ c(n) iff P1 ≤ L0(n). The key point: this works for ALL Case A configs without any condition on P_{n+1}'s size.

**Impact**: The existing proof in geometric-direct.md has a gap labeled "Case A.1" (when P_{n+1} ≤ (1-P1)/2, the original pairing sub-pieces r can be negative). The new halve-all strategy fills this gap cleanly. Verified computationally for n=3 equal pieces {1/15,14/45,14/45,14/45}: halving P2,P3,P4 gives LB = 8/15 = c(3). The proof uses only Pairing Cancellation (certified).

---

### 2. Case B2 inductive proof

**Claim**: When P1 > L0(n) AND P_{n+1} ≥ c(n), XY's strategy:
- Place 1 mark to halve P_{n+1} into {P_{n+1}/2, P_{n+1}/2}.
- Use remaining n-1 marks on {P1,...,Pn} to enforce the inductive bound c(n-1).

By Pairing Cancellation: LB = P_{n+1}/2 + lb_score({P1,...,Pn} after n-1 marks). By inductive hypothesis (n-piece game, n-1 marks): lb_score ≤ c(n-1)*(1-P_{n+1}). So:
LB ≤ P_{n+1}/2 + c(n-1)*(1-P_{n+1}).

This is ≤ c(n) iff P_{n+1} ≥ c(n) (proved: threshold = c(n) via algebraic identity c(n) = 2c(n-1)/(1+2c(n-1))). ✓

**Verification**: The n-piece sub-game {P1,...,Pn} has P1 ≤ P_{n+1} and sum = 1-P_{n+1}. After normalizing (scaling by 1/(1-P_{n+1})), the sub-game satisfies either Case A or Case B for (n-1), and by the inductive hypothesis XY can limit LB_sub ≤ c(n-1)*(1-P_{n+1}).

Note: When P1 > L0(n) and P_{n+1} ≥ c(n), the algebraic constraint P1+...+Pn < 1-c(n) = (2^n-1)/(2^{n+1}-1) with all n pieces ≥ P1 forces a structural constraint on the sub-game that the induction can exploit.

---

### 3. Complete Case B1 proof for n=2

**Case B1**: P1 > L0(2) = 1/7 AND P3 ≤ c(2) = 4/7. FULLY PROVED using 1-mark XY strategies.

**Sub-case B1a (P3 ≥ 1/2)**: Shadow strategy. Since P3 ≥ 1/2 implies P1+P2 ≤ P3, XY can place mark at t with P1 < t < P3-P2 (valid since P1 < P3-P2 iff P1+P2 < P3). This creates pieces {P2, t, P3-t} with P3-t > P2 > P1 > t (strictly). LB picks positions 1 and 3 from sorted {P3-t, P2, P1, t}: LB = (P3-t) + P1 < P3-P1+P1 = P3 ≤ c(2). ✓

**Sub-case B1b (3/7 ≤ P3 < 1/2)**: Duplicate-P2 strategy. XY splits P3 at P3-P2, creating pieces {P1, P2, P3-P2, P2}. Since P3 < 1/2: P3-P2 < P1 < P2 (key: P3 < 1/2 iff P3-P2 < P1, proved since P3 < P1+P2). Sorted: P2, P2, P1, P3-P2. LB picks positions 1,3 = P2+P1 = 1-P3 ≤ 1-3/7 = 4/7 = c(2). ✓

**Sub-case B1c (P3 < 3/7)**: Halve-P1 strategy. XY halves P1 into {P1/2, P1/2}. By Pairing Cancellation: LB = P1/2 + lb_score({P2, P3}) = P1/2 + P3 (LB picks larger of P2, P3 in 2-piece sub-game = P3). LB = P3+P1/2 = (2P3+P1)/2 = (P3+(1-P2))/2. Now: P3 < 3/7 and P2 > 2/7 (from sum constraint: P1+P2 > 4/7-P3 > 4/7-3/7=1/7... more carefully: P1+P2+P3=1 and P3 < 3/7 gives P1+P2 > 4/7; since P2 ≥ P1: 2P2 ≥ P1+P2 > 4/7, so P2 > 2/7). Therefore LB = (P3+(1-P2))/2 < (3/7+(1-2/7))/2 = (3/7+5/7)/2 = 4/7 = c(2). ✓

**Case B2 for n=2 (P3 > c(2) = 4/7)**: Halve-P3 strategy. Key algebraic fact: P1 > L0 = 1/7 and P3 > 4/7 imply P2 < 2/7 (from P1+P2 < 3/7 and P1 > 1/7). Hence P2-P1 < 2/7-1/7 = 1/7 = L0. XY halves P3. LB = P3/2+P2 = 1/2+(P2-P1)/2 < 1/2+L0/2 = c(2). ✓

All four sub-cases verified computationally by exhaustive search over denominators up to 100.

---

### 4. Structural algebraic facts established

- **P2-P1 < L0 forced in Case B2**: When P1 > L0(n) and P_{n+1} > c(n), the sum constraint P1+P2+...+Pn < 1-c(n) with P1 > L0(n) forces each difference Pk-P1 < ... This was proved for n=2 explicitly.

- **P3-P2 < P1 when P3 < 1/2**: Algebraic identity: P3-P2 < P1 iff P3 < P1+P2 = 1-P3, iff P3 < 1/2. Used in B1b.

- **The threshold 3/7 = c(2)-L0**: In Case B1b vs B1c split, threshold is 3/7 = c(2)-L0 = 4/7-1/7. This pattern generalizes: threshold for nth sub-case is c(n)-L0.

- **The recursion P_{n+1}/2 + c(n-1)*(1-P_{n+1}) ≤ c(n) holds iff P_{n+1} ≥ c(n)**: Verified for n=2,3,4. The threshold is exactly c(n) via the identity 2c(n)-1 = L0 and c(n) = 2c(n-1)/(1+2c(n-1)).

---

### Distinct openings for the outliner

1. **Unified two-strategy proof** for all configs: Strategy A (halve P2,...,P_{n+1}) covers P1 ≤ L0; Strategy B2 (halve P_{n+1} + induction) covers P_{n+1} ≥ c(n). The hard remaining piece is P_{n+1} < c(n) with P1 > L0 (Case B1).

2. **Induction with strong hypothesis**: IH(k): "For any k+1 pieces summing to S, XY (k marks) ensures LB ≤ c(k)*S." Inductive step: split by P_{n+1} ≥ c(n) (Case B2 closes) vs P_{n+1} < c(n) and P1 ≤ L0 (new halve-all strategy closes). Only Case B1 remains open.

3. **Case B1 sub-case analysis extended to general n**: For n=2, proved via 4 sub-cases. For general n, the sub-cases would be based on the sizes of "gaps" P_{k+1}-P_k relative to L0. The pattern for n=2: gaps B1a/B1b/B1c correspond to whether the consecutive differences exceed a threshold. Conjecture: for general n, the sub-cases iterate on which differences exceed L0(k) for sub-levels k.

4. **Alternative: prove B1 by showing "XY uses fewer marks"**: In Case B1, all pieces are < c(n). XY might be able to use FEWER than n marks. If XY uses j marks creating 2j+n+1 pieces... the structure changes and LB might already be < c(n).

5. **Halve-all-but-max**: A single unified XY strategy: halve P1,...,Pn (leaving P_{n+1} whole). LB = 1/2+P_{n+1}/2 ≤ c(n) iff P_{n+1} ≤ L0. This fails for Case B (P_{n+1} >> L0). But it points to the DUALITY: halving "small" pieces (Case A strategy) vs halving "large" pieces (Case B strategy).

---

### Candidate technique(s)

- **Pairing Cancellation** (certified lemma): core technique for both Case A and Case B2.
- **Induction on n** with normalized sub-games: clean for Case B2, needs extension for B1.
- **Sub-case analysis by threshold comparisons**: proven complete for n=2, structural template for general n.
- **Algebraic inequalities from sum constraint**: key for closing sub-cases (e.g., P2 > 2/7 when P3 < 3/7).

### Cheap-kill candidates

- **Case A.1 (the gap)**: Settled by the new halve-all strategy. XY halves P2,...,P_{n+1} (n marks). LB = 1/2+P1/2 ≤ c(n) for P1 ≤ L0. This requires only Pairing Cancellation, no case analysis.
- **Case B2**: Settled by induction. Halve P_{n+1} + inductive hypothesis. Only requires the IH to hold for smaller n.
- **Parity/counting**: With XY using j marks, LB picks ceil((n+1+j)/2) pieces. Using more marks changes parity and can hurt XY.

### Knowledge-base entries to use

- **Pairing Cancellation** (in approaches file, certified): lb_score({v,v}∪S) = v + lb_score(S).
- **Greedy Optimality Lemma** (certified in lemmas/): LB picks positions 1,3,5,...
- **Induction** (knowledge_base.md): strong induction structure for IH(k).
- **Invariant/monovariant**: sum constraint P1+...+P_{n+1}=1 used to bound differences.
- **Constructive proof**: explicit XY strategies (halve-all, shadow, duplicate-P2, halve-P1).

### Analogous past problems (cruxes)

None retrieved from crux corpus this round (focus was computational verification). The problem's structure is specific to the alternating-pick greedy game.

### Prior progress

- Status: partial.
- Proved: lower bound (geometric config achieves c(n)), Case A (P1 ≤ L0) via pairing — though Case A proof had a sub-case gap (Case A.1) now filled by halve-all strategy.
- Open: Case B1 (P1 > L0 AND P_{n+1} < c(n)) for general n ≥ 3.

### Dead ends (do not retry)

- **Inductive halving of P1** as universal strategy: XY halves P1 (1 mark) + induction gives LB = P1/2 + c(n-1)*(1-P1) > c(n) when P1 < c(n) (wrong direction). FAILED.
- **Equal sub-pieces of P_{n+1}**: Simple splitting P_{n+1} into equal halves without the sub-game induction fails for Case A.1 when r < 0.
- **Interleaving/pairing for upper bound**: The Q_k = P_{n+1-k} construction gives LB = P_{n+1}, too large. Only valid for lower bound.

### Small-case / intuition notes (labeled as conjecture)

- **Conjecture**: Case B1 for general n has a sub-case structure based on whether the differences P_{k+1}-P_k exceed L0(k) for some k. For n=3, the sub-cases would be based on P4-P3, P3-P2, P2-P1 vs L0(3)=1/15. This is a conjecture from the n=2 pattern.

- **Computational evidence (n=2)**: All Case B1 configs achievable with 1 XY mark (not 2). This suggests a SINGLE general XY strategy might cover all of B1 for general n with only 1 mark (or at most k marks for k-level sub-cases).

- **Threshold pattern (conjecture)**: The sub-case boundaries 1/2, 3/7, ... appear to be c(n)-k*L0 for k=0,1,2,... This would give n sub-cases in B1 for n+1 pieces.

- **MOST IMPORTANT OPEN QUESTION**: Can the Case B1 sub-cases for n=2 extend to n=3 via the following pattern? For n=3 Case B1 (P4 < c(3), P1 > L0(3)):
  - B1a: P4 ≥ 1/2: Shadow P4 → LB = P4 ≤ c(3). [conjectured]
  - B1b: P4 ∈ [c(3)-L0, 1/2): Duplicate P3 from P4 → LB = 1-P4-P2+P2 = ?. [needs verification]
  - B1c: P4 < c(3)-L0: Halve P1 → LB = P4+P2+P1/2 ≤ c(3). [needs algebraic proof]

### Recommended next actions for the outliner

1. **Adopt the halve-all strategy for Case A**: Replace the existing Case A proof (with Case A.1 gap) by the clean halve-P2...P_{n+1} strategy. This closes the gap cleanly.

2. **Build the induction on Case B2**: The halve-P_{n+1} + IH argument is clean. Formalize it in the approach file, connecting it to the verified Case A halve-all strategy for the sub-games.

3. **For Case B1 general n**: Attempt extending the n=2 sub-cases to n=3 explicitly, then generalize. The key sub-cases are B1a (shadow when max piece > 1/2), B1b (duplicate second-largest when max in [c-L0, 1/2)), B1c (halve minimum when max < c-L0).

4. **Challenge**: If Case B1 for n=3 cannot be closed with explicit sub-cases, consider whether Case B1 can actually never occur in tight configs (i.e., does the lower bound construction force P_{n+1} ≥ c(n) for the worst LB strategy?).
