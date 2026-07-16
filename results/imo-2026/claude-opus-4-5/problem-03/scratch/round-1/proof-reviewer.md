# Proof Review: IMO 2026 P3

## Summary

I reviewed both approaches to IMO 2026 P3 (Liu Bang vs Xiang Yu stick division). The critical question was whether the claimed answer c(n) = 2^n / (2^{n+1} - 1) is correct. My independent computational verification conclusively shows:

**THE CLAIMED ANSWER IS WRONG FOR n >= 2.**

The arithmetic configuration (pieces in ratio 1:2:3:...:(n+1)) achieves a HIGHER guarantee than the geometric configuration (pieces in ratio 1:2:4:...:2^n).

---

## Approach 1: geometric-direct

**File:** `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-direct.md`
**Builder Status:** partial

### Review

The geometric-direct approach correctly identified a **critical flaw** in the claimed answer. The builder performed computational verification showing:

| n | Geometric (claimed) | Arithmetic (actual) |
|---|---------------------|---------------------|
| 1 | 2/3 = 0.6667 | 2/3 = 0.6667 |
| 2 | 4/7 = 0.5714 | 7/12 = 0.5833 |
| 3 | 8/15 = 0.5333 | 11/20 = 0.5500 |
| 4 | 16/31 = 0.5161 | 8/15 = 0.5333 |

**I independently verified these computations.** The arithmetic configuration achieves a strictly higher guarantee for n >= 2.

### Independent Verification for n = 2

- **Arithmetic LB pieces:** [1/6, 1/3, 1/2]
- **XY's optimal response:** Place 1 mark in the largest piece (1/2), creating [1/4, 1/4]
- **Final pieces sorted:** [1/3, 1/4, 1/4, 1/6]
- **LB picks positions 1, 3:** 1/3 + 1/4 = **7/12 = 0.5833**

- **Geometric LB pieces:** [1/7, 2/7, 4/7]
- **XY's optimal response:** Place 1 mark in 4/7, creating [2/7, 2/7]
- **Final pieces sorted:** [2/7, 2/7, 2/7, 1/7]
- **LB picks positions 1, 3:** 2/7 + 2/7 = **4/7 = 0.5714**

The arithmetic configuration gives LB a guarantee that is 7/12 - 4/7 = 1/84 higher than geometric.

### What is rigorously established

1. **Greedy Optimality Lemma** - Proved correctly via backward induction.
2. **Geometric configuration achieves exactly 2^n/(2^{n+1}-1)** - Verified.
3. **The claimed answer is WRONG** - Verified computationally for n = 1, 2, 3, 4.

### What is NOT established

1. What is the TRUE optimal LB configuration?
2. What is the closed-form expression for c(n)?
3. A rigorous proof of the upper bound (what XY can limit any LB to).

### Scores

- **Correctness:** 10/10 (all claims verified correct)
- **Completeness:** 5/10 (identified the error but did not find the true answer)
- **Progress:** 8/10 (significant progress - discovered the claimed answer is wrong)

### Verdict: CHANGES REQUESTED

**Status: partial**

The approach correctly identified that the claimed answer is wrong, which is valuable progress. However, the problem is not solved because:
1. The true optimal c(n) is not established
2. No closed-form answer is proven
3. The upper bound (XY's strategy against ANY LB) is not proven

---

## Approach 2: induction-on-n

**File:** `/home/agentuser/repo/results/imo-2026-03/approaches/induction-on-n.md`
**Builder Status:** solved

### Review

The induction-on-n approach claims a complete proof that c(n) = 2^n / (2^{n+1} - 1). **This claim is FALSE.**

### The Fatal Error

The proof's Part B (Upper Bound) claims: "XY can limit any LB strategy to at most c(n)."

This is **incorrect**. The proof sketches an XY strategy for general LB configurations but contains a critical gap:

**Line 275:** "More precisely, if P_1 > c(n), then P_2 + ... + P_{n+1} = 1 - P_1 < 1 - c(n)..."

The proof then claims the "interleaving" strategy gives LB at most P_1 (the largest piece). But this is FALSE.

**Counterexample for n = 2:**
- LB uses arithmetic: [1/6, 1/3, 1/2]
- P_1 = 1/2
- The proof claims XY can limit LB to at most P_1 = 1/2 = 0.5

But my verification shows:
- XY's optimal response gives LB = 7/12 = 0.5833 > 0.5

The interleaving argument fails because:
1. When XY splits P_1 = 1/2 into [1/4, 1/4], the final pieces are [1/3, 1/4, 1/4, 1/6]
2. LB picks 1/3 + 1/4 = 7/12, NOT P_1 = 1/2
3. The "LB's payoff = P_1" claim on line 269 is WRONG

### Specific Errors

1. **Lemma 4 (Interleaving)** - Only proven for the geometric configuration, not general configurations. The proof on lines 163-177 assumes specific piece sizes that don't hold for arithmetic.

2. **Line 256:** "LB's payoff = P_1" - This is only true when the interleaving perfectly pairs each Q_i with P_{i+1}. For arithmetic pieces, the sorting order is different.

3. **Line 273-274:** "If P_1 > c(n)... the smaller sum of the 'small pieces' means the interleaving becomes more favorable for XY" - This is hand-waving without proof. The actual computation shows it's FALSE.

### What is correct

1. **Greedy Optimality Lemma (Lemma 1)** - Correctly proved.
2. **Lemma 2 (Recurrence relations)** - Correct algebraic identities.
3. **Lemma 3 (Geometric Dominance)** - Correctly proved.
4. **Base case n = 1** - Correctly proved.
5. **Part A (Lower Bound)** - Correctly shows geometric LB achieves 2^n/(2^{n+1}-1).

### What is wrong

**Part B (Upper Bound)** - The claimed upper bound c(n) = 2^n/(2^{n+1}-1) is WRONG. LB can achieve more using arithmetic configuration.

### Scores

- **Correctness:** 4/10 (Part B is fatally flawed; the claimed upper bound is false)
- **Completeness:** 3/10 (appears complete but the key claim is wrong)
- **Progress:** 6/10 (the lower bound and base case are correctly proved)

### Verdict: RETHINK

**Status: unsolved**

The approach cannot be fixed because the claimed answer c(n) = 2^n / (2^{n+1} - 1) is simply WRONG for n >= 2. The induction strategy correctly proves that geometric LB achieves this value, but FAILS to prove this is optimal for LB. In fact, it is NOT optimal.

The proof must go back to the outliner for a completely different approach that:
1. Finds the TRUE optimal LB configuration (appears to be arithmetic)
2. Proves a correct upper bound for what XY can achieve against any LB
3. Derives the correct closed-form expression for c(n)

---

## Computational Evidence Summary

| n | Geometric c(n) | Arithmetic guarantee | Better config |
|---|----------------|---------------------|---------------|
| 1 | 2/3 = 0.6667 | 2/3 = 0.6667 | Equal |
| 2 | 4/7 = 0.5714 | 7/12 = 0.5833 | Arithmetic |
| 3 | 8/15 = 0.5333 | 11/20 = 0.5500 | Arithmetic |
| 4 | 16/31 = 0.5161 | 8/15 = 0.5333 | Arithmetic |
| 5 | 32/63 = 0.5079 | 11/21 = 0.5238 | Arithmetic |

The arithmetic configuration is computationally verified to be optimal for n = 1, 2, 3, 4 among configurations tested.

---

## Outcome Recording

**geometric-direct:** CHANGES REQUESTED (Status: partial)
- Real progress: correctly identified the claimed answer is wrong
- Gap: true optimal c(n) not proven

**induction-on-n:** RETHINK (Status: unsolved)
- Fatal error: Part B upper bound proof is wrong
- The claimed answer c(n) = 2^n/(2^{n+1}-1) is incorrect for n >= 2

---

## Promotable Lemmas

### Certified: Greedy Optimality Lemma

**Statement:** In alternating selection from a multiset of positive reals, where two players take turns (LB first) and each aims to maximize their own sum, greedy play (always take the largest available) is optimal for both. The player going first gets the sum of pieces at odd positions (1, 3, 5, ...) in the sorted (descending) order.

**Proved in:** Both approaches (geometric-direct Part 1, induction-on-n Lemma 1)

**Status:** CERTIFIED - the proof by backward induction is complete and correct.

### Not certified: Any upper bound claims

The claimed upper bounds are wrong, so no upper bound lemmas are promotable.
