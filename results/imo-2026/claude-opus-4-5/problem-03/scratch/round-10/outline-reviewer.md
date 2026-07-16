# Outline Review — Round 10

## Summary of Field

The outliner proposed four approaches:
1. **geometric-direct (revise)**: Add S_last strategy, correct Case B structure
2. **vertical-pairing (new)**: Articulate full V_j strategy family
3. **pigeonhole-gaps (new)**: Pigeonhole on n gaps (weak)
4. **halve-ih-plus-slast (new)**: Two-strategy sufficiency via impossibility argument

## Critical Finding from Explorers (Verified)

The sum-slack explorer found a COUNTEREXAMPLE in the B_small region (P6 < c(5), all d_j > L0):
- Config: alpha=2.641, beta=2.594, gamma=0.206, delta=0.253, epsilon=4.913
- P6 = 0.292 < c(5) = 0.508 (B_small region)
- All d_j > L0 (all shifted params > 0)
- **All 11 Singleton-Pair strategies fail** (min condition = 2.27 >> 1)
- **All V_j vertical pairing strategies fail** (all d_j > L0)

**BUT XY CAN still limit LB to c(5)** via a NEW strategy:
- Cut P6 at P3 (1 mark), halve P1, P2, P5 (3 marks) = 4 marks
- Creates pairs {P1/2, P1/2}, {P2/2, P2/2}, {P3, P3}, {P5/2, P5/2}
- Singletons: {P4, P6-P3}
- Singleton difference = |P4 - (P6-P3)| = 0.004 < L0 = 0.016
- LB = 1/2 + 0.002 = 0.502 < c(5) = 0.508

This strategy works when |41 - 7*alpha - 6*beta - 5*gamma - 3*delta - epsilon| <= 1.

---

## Approach-by-Approach Review

### 1. geometric-direct (revise) — CHANGES REQUESTED

**Technique assessment**: The core technique (Singleton-Pair strategies with gap-overlap) is sound for n <= 4 but **incomplete for B_small (n >= 5)**.

**Critical issues**:

1. **The gap-overlap argument FAILS in B_small**. The outliner claims "gap = alpha - 1 < 0" in B_small, but:
   - In B_small Case A (all d_j doubly large), the sum constraint is 9*alpha + 6*beta > 10 (NOT < 9)
   - This does NOT force alpha < 1. Example: alpha=1.2, beta=0.1 gives 11.4 > 10.
   - The gap-overlap argument from B_large does NOT transfer to B_small.

2. **S_last alone is insufficient**. The V_j strategies work when d_j <= L0, but the counterexample has ALL d_j > L0 (all V_j fail).

3. **Missing strategy for B_small "all d_j > L0" corner**. The new strategy (cut P6 at P3; halve P1,P2,P5) covers part of this region but is NOT in the current outline.

**Required changes**:
- Add the new strategy: "Cut P6 at P3; halve P1, P2, P5" with condition |41 - 7*alpha - 6*beta - 5*gamma - 3*delta - epsilon| <= 1
- Enumerate more strategies for B_small (the 11+V_j+new may still not cover all)
- Acknowledge that the proof structure for B_small differs from B_large (no universal alpha < 1 bound)

**Verdict: CHANGES REQUESTED**

---

### 2. vertical-pairing (new) — CHANGES REQUESTED

**Technique assessment**: The V_j family (halve all except {P_j, P_{j+1}}) is correct and adds useful strategies, but is **insufficient alone**.

**Critical issues**:

1. **Coverage claim is WRONG**. The outline claims "at least one d_j <= L0" in B_small. This is FALSE:
   - The counterexample has all d_j > L0 (beta, gamma, delta, epsilon all > 0)
   - So all V_j strategies fail, yet the config is valid B_small
   
2. **The minimum-sum bound is not tight enough**. Step 5-6 attempts to derive contradiction from all d_j > L0, but:
   - P_j > j*L0 gives sum > L0*(1+2+...+(n+1)) = L0*(n+1)(n+2)/2
   - For n=5: sum > 21/63 = 1/3 < 1 (no contradiction)
   - Adding P_{n+1} < c(n) constraint still doesn't force contradiction

**Verdict: CHANGES REQUESTED** — The V_j strategies should be incorporated into geometric-direct as additional strategies, not as a standalone approach claiming complete coverage.

---

### 3. pigeonhole-gaps (new) — RETHINK

**Technique assessment**: Pure pigeonhole on gaps is **provably insufficient**.

**Fatal flaw**:
- Pigeonhole: If all G_j > L0, then sum > n*L0 = n/(2^{n+1}-1)
- For contradiction with B_small (P_{n+1} < c(n)), need n*L0 >= c(n), i.e., n >= 2^n
- This is FALSE for all n >= 1

The outline itself acknowledges this in Step 6: "Need weighted pigeonhole or case analysis."

**This reduces to the same gap as the other approaches** — there's no new technique here, just a weaker framing.

**Verdict: RETHINK** — The pigeonhole bound is too weak. This approach cannot close the gap without adding the same strategy enumeration as geometric-direct.

---

### 4. halve-ih-plus-slast (new) — RETHINK

**Technique assessment**: The "two-strategy sufficiency" claim is **FALSE**.

**Fatal flaw**: The impossibility argument (Step 4c: "all d_j > L0 in B_small is IMPOSSIBLE") is WRONG:
- The outliner itself acknowledges in "Watch out for" that the counterexample (alpha=2.641, etc.) has all d_j > L0 AND is in B_small
- The sum constraint in B_small does NOT force contradiction when all d_j > L0
- The proof attempts show: sum > 6/15 but B_small requires sum > 7/15, gap = 1/15 = L0... but this doesn't give contradiction

The approach is predicated on proving "all d_j > L0" impossible, which is verifiably false. The correct fix (as the outliner notes) is to add MORE strategies, which makes this identical to geometric-direct.

**Verdict: RETHINK** — The impossibility argument is false. This approach collapses to geometric-direct with strategy enumeration.

---

## Ranking Update

Comparing approaches:
1. **geometric-direct** (Elo 1702): Most advanced, has complete proof for n <= 4, clear path for n=5 via strategy enumeration
2. **vertical-pairing** (new, Elo 1500): Adds useful V_j strategies but coverage claim wrong; should merge into geometric-direct
3. **pigeonhole-gaps** (new): Provably insufficient technique
4. **halve-ih-plus-slast** (new): Predicated on false impossibility claim

I will NOT register pigeonhole-gaps or halve-ih-plus-slast since they have fatal flaws.

I will register vertical-pairing since the V_j strategies are valid (even though the coverage claim is wrong) — they should be incorporated into geometric-direct.

**Comparisons**:
- geometric-direct BEATS vertical-pairing (geometric-direct has complete n<=4 proof; vertical-pairing's coverage claim is wrong)
- geometric-direct BEATS pigeonhole-gaps (pigeonhole bound is provably too weak)
- geometric-direct BEATS halve-ih-plus-slast (impossibility claim is false)

---

## Registrations

Register **vertical-pairing** as a new approach (the V_j strategies are valid additions).

Do NOT register pigeonhole-gaps or halve-ih-plus-slast (fatal flaws).

---

## Build Set

The only viable approach is **geometric-direct (revise)** with the required changes:
1. Add S_last (V_{n-1}) strategy for d_{n-1} <= L0
2. Add the new B_small strategy: cut P6 at P3; halve P1,P2,P5
3. Enumerate more strategies to cover remaining B_small corner cases
4. Acknowledge that B_small coverage requires explicit strategy enumeration, NOT the gap-overlap shortcut

The vertical-pairing approach should be merged into geometric-direct rather than built separately.

---

## build set: geometric-direct
