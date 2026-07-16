# Outline Review — IMO 2026 P3, Round 2

## Critical Context

Round 2 explorers discovered that Round 1's "arithmetic beats geometric" claim was **WRONG**. The error: Round 1 assumed XY splits pieces equally, but XY's optimal response is often an unequal split. With optimal XY:

- Arithmetic [1/6, 1/3, 1/2] for n=2: XY splits 1/2 into [1/3, 1/6], giving LB only **1/2** (not 7/12).
- Geometric [1/7, 2/7, 4/7] for n=2: ANY split of 4/7 gives LB exactly **4/7**.

**The correct answer is c(n) = 2^n / (2^{n+1} - 1).** This was the "claimed answer" all along; Round 1 incorrectly disputed it.

**Verified computationally:**
- n=1: c(1) = 2/3
- n=2: c(2) = 4/7
- n=3: c(3) = 8/15
- n=4: c(4) = 16/31

---

## Review of Proposed Approaches

### 1. geometric-direct-revised (revise)

**Target:** c(n) = 2^n / (2^{n+1} - 1)

**Verdict: APPROVE**

**Assessment:**

The skeleton is sound. The approach correctly targets the geometric answer with a clear structure:

1. **Greedy Optimality Lemma** — certified and importable. No gap.

2. **Geometric Dominance Lemma** — trivial: 2^n > 2^n - 1. No gap.

3. **Part A (Lower Bound)** — correct structure:
   - Case A.1 (XY avoids L_n): L_n is largest, LB picks it first. Trivial.
   - Case A.2 (XY marks inside L_n): This is the crux. The "Key Invariant Lemma" is stated with a mechanism (doubling property ensures sub-pieces straddle L_{n-1}).

4. **Part B (Upper Bound)** — the harder direction. The "interleaving" strategy is sketched but needs careful proof.

**Key gaps to close during building:**

- **Key Invariant (Lower Bound, Case B):** The claim is that for any partition of L_n into sub-pieces, greedy picking from {L_0, ..., L_{n-1}} union {sub-pieces} gives LB >= L_n. The mechanism (doubling property) is stated but needs rigorous proof for general j marks, not just j = n-1.
  
  *Small-case verification:* I tested n=2 and n=3 exhaustively. The invariant holds. The mechanism is: when sub-pieces sum to L_n = 2^n/D and the original pieces are L_k = 2^k/D, any sub-piece t and L_n-t "straddle" some L_k in sorted order. LB picks one from each straddled level, totaling L_n.

- **Upper Bound Interleaving:** The claim is that XY can limit any LB configuration to <= c(n). The mechanism (create sub-pieces Q_k slightly exceeding P_{k+1}) needs proof that this ordering holds and that LB's total = P_1 <= c(n).

  *Small-case verification:* I tested n=2 for various LB configs. XY can limit all to <= 4/7. For [1/5, 2/5, 2/5], XY splits the 1/5 piece at 1/10, giving LB = 1/2 <= 4/7.

**Watch for:**
- The upper bound is genuinely hard. The approach needs to show that LB cannot do better than geometric, not just that geometric achieves c(n).
- Parity: n marks by XY gives odd piece count (2n+1), hurting XY. This constrains XY to use <= n-1 marks.

---

### 2. minimax-saddle-point (new)

**Target:** c(n) = 2^n / (2^{n+1} - 1)

**Verdict: APPROVE**

**Assessment:**

This is a fresh, game-theoretic perspective. The saddle-point structure is elegant:

- At the geometric config, XY's two principal strategies (split largest vs. split multiple pieces) give **equal values** c(n).
- Any deviation from geometric breaks this equality, allowing one XY strategy to dominate.

**Strengths:**
- The saddle-point framework unifies the lower and upper bounds as two sides of the same coin.
- For n=2, the two-strategy analysis is tractable: split 4/7 at any point vs. split both 2/7 and 4/7.

**Key gaps to close during building:**

- **Two-strategy sufficiency:** Is it true that XY's optimal is always one of a finite set of "principal strategies"? This needs justification. For general n, XY has many more options (distribute n marks among n+1 pieces).

- **Saddle equality for general n:** The outline derives the condition for n=2 but needs the general-n derivation. The claim is that the doubling ratio L_k = 2*L_{k-1} is precisely what makes Strategy A and Strategy B give equal values.

- **Uniqueness of saddle:** Why is the geometric config the unique optimum for LB? This follows if the saddle is unique.

**Watch for:**
- This approach may be harder to make rigorous than geometric-direct-revised. The finite strategy enumeration may not hold for large n.
- If the saddle-point argument stalls, the builder should fall back to the direct proof structure.

---

### 3. induction-on-n-revised (revise)

**Target:** c(n) = 2^n / (2^{n+1} - 1)

**Verdict: CHANGES REQUESTED**

**Assessment:**

This approach has the same structure as Round 1's induction-on-n, which was marked **RETHINK** by the proof-reviewer due to a fatally flawed upper bound. The outliner claims to "fix" the approach, but the skeleton reveals the **same gap persists**.

**The problem:**
- Step 5 says: "If P_1 > c(n), then P_2 + ... + P_{n+1} < 1 - c(n) = (2^n - 1)/D. XY's interleaving exploits this slack... wait, this is backward."
- The outline itself admits confusion and circularity.

**Specific issues:**

1. **The upper bound mechanism is not specified.** The claim "XY's strategy ensures LB's payoff = P_1" is stated without a construction. Which n-1 marks does XY place? What are the sub-piece sizes?

2. **The "P_1 <= c(n) or XY exploits" claim is not proved.** This is exactly the upper bound — it assumes the conclusion.

3. **The recurrence verification is a sanity check, not a proof.** Verifying 1/c(n) = 2 - 2^{-n} doesn't prove the formula.

**Required changes before building:**

- The builder should NOT build this approach as stated. It would repeat Round 1's error.
- If the outliner wants to pursue induction, the upper bound must have a **concrete XY strategy construction** and a **rigorous proof that it limits LB to <= c(n)**.

**Alternative:** Merge this approach into geometric-direct-revised. The inductive structure for the lower bound is sound; the upper bound gap is shared with geometric-direct-revised.

---

### 4. piece-count-parity (advance)

**Target:** c(n) = 2^n / (2^{n+1} - 1)

**Verdict: DO NOT BUILD STANDALONE**

**Assessment:**

The outline correctly notes this is "a structural observation, not a full proof." The parity argument is useful:

- XY should use exactly n-1 marks (giving 2n pieces, even count, no extra pick for LB).
- Using n marks gives 2n+1 pieces (odd count), LB picks n+1 pieces — one more than XY.

**This is a lemma, not an approach.** It constrains XY's strategy space but doesn't prove either bound.

**Recommendation:** Do not build this as a standalone approach. Instead, import the parity observation into geometric-direct-revised and minimax-saddle-point.

---

## Registration and Ranking

### New approaches to register

1. **minimax-saddle-point** — Game-theoretic saddle-point approach to c(n) = 2^n/(2^{n+1}-1)

### Ranking updates

Based on the critical correction and approach viability:

1. **geometric-direct** should be updated to reflect the correct answer (it was marked partial with the wrong conclusion). The revised version is now the lead approach.

2. **induction-on-n** remains dead-end; the revision does not fix the fundamental gap.

3. **minimax-saddle-point** is a fresh approach, starting at Elo 1500.

4. **minimax-value** (existing in ranking) is superseded by minimax-saddle-point.

5. **piece-count-parity** is a supporting lemma, not a standalone approach.

**Comparisons:**
- geometric-direct-revised > induction-on-n-revised (geometric has clearer structure, induction has same gap)
- geometric-direct-revised > minimax-saddle-point (geometric is more direct, minimax requires finite-strategy justification)
- minimax-saddle-point > induction-on-n-revised (fresh perspective vs. repeated dead-end)
- geometric-direct-revised > minimax-value (revised is more developed)

---

## Build Set Decision

**Build this round:**

1. **geometric-direct-revised** — The most promising path. Clear structure, correct target, verified small cases. Key gaps: Key Invariant for lower bound, interleaving for upper bound.

2. **minimax-saddle-point** — Fresh angle worth exploring. May yield a cleaner proof if the two-strategy sufficiency can be justified.

**Do NOT build:**

- **induction-on-n-revised** — Same gap as Round 1. Needs concrete upper bound construction before building.
- **piece-count-parity** — Not standalone; a lemma for other approaches.

---

## Summary

| Slug | Action | Verdict | Build? |
|------|--------|---------|--------|
| geometric-direct-revised | revise | APPROVE | Yes |
| minimax-saddle-point | new | APPROVE | Yes |
| induction-on-n-revised | revise | CHANGES REQUESTED | No |
| piece-count-parity | advance | N/A (lemma) | No |

---

## Warnings for Orchestrator

1. **The Round 1 error is corrected.** The geometric answer c(n) = 2^n/(2^{n+1}-1) is CORRECT. All approaches now target this.

2. **The upper bound is the shared hard step.** Both geometric-direct-revised and minimax-saddle-point need to prove XY can limit any LB to <= c(n). If both stall on this, consider:
   - A combinatorial argument (XY's optimal response is a specific pairing strategy)
   - An LP/convex optimization argument (the game value is a linear program)

3. **induction-on-n-revised is not ready to build.** The outline admits the upper bound is "backward." Do not dispatch a builder to this approach.

---

build set: geometric-direct, minimax-saddle-point

**Note for orchestrator:** The outliner proposed "geometric-direct-revised" as a revision of "geometric-direct". The builder should work on the existing slug "geometric-direct", correcting the Round 1 conclusion and filling the gaps identified above. Similarly, "minimax-saddle-point" is a new approach file to be created by the builder.
