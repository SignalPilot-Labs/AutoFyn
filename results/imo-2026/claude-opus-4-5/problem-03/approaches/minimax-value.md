# Approach: minimax-value

## Status
partial

## Target
Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.

## Overview
Frame the problem as a two-player zero-sum game and compute the minimax value. The game has a Stackelberg structure: LB (leader) commits to marks, then XY (follower) responds optimally, then both pick greedily.

## Technique
Game theory / minimax analysis. Value function recursion on piece configurations.

---

## Skeleton

### Part 1: Game Formulation

**Game tree:**
1. LB chooses a marking strategy: M_LB in [0,1]^{<=n} (up to n points).
2. XY observes M_LB and chooses M_XY in [0,1]^{<=n} \ M_LB (up to n distinct points).
3. Pieces are formed by cutting at M_LB union M_XY.
4. Picking phase: LB and XY alternate (LB first), each greedily taking the largest unclaimed piece.
5. Payoff = LB's total length.

**Minimax value:** c(n) = max_{M_LB} min_{M_XY} GreedyValue(M_LB, M_XY).

**Claim.** The minimax value equals 2^n / (2^{n+1} - 1).

---

### Part 2: Simplification via Greedy Optimality

**Lemma 1.** The picking phase reduces to: sort pieces descending, LB takes odd-indexed pieces (1, 3, 5, ...).

**Proof.** Greedy (take the largest) is optimal for both. This is a standard result: deviating to take a smaller piece lets the opponent take the larger one, a net loss.

**Consequence.** Given pieces p_1 >= p_2 >= ... >= p_N, LB's value = p_1 + p_3 + p_5 + ... = sum of odd-indexed pieces.

---

### Part 3: LB's Optimal Strategy (Lower Bound)

**Claim.** LB achieves value c(n) with the geometric marking.

**Construction:** LB marks at (2^k - 1) / D for k = 1, ..., n, creating pieces {1, 2, 4, ..., 2^n} / D.

**Claim.** Against any XY response with <= n marks, LB's greedy value >= c(n).

**GAP:** Prove this claim. The proof requires case analysis on XY's mark placement.

---

### Part 4: XY's Optimal Response (Upper Bound)

**Claim.** Against LB's geometric marking, XY achieves value exactly c(n) with the (n-1)-mark strategy.

**Construction:** XY marks inside L_n to create the paired configuration.

**Result:** 2n pieces, LB picks n at odd positions, total = c(n).

**Claim.** Against ANY LB marking, XY can respond to limit LB to <= c(n).

**GAP:** Prove this claim. This is the harder direction.

---

### Part 5: Value Function Approach

Define V(S) = LB's optimal value when pieces are S = {s_1, ..., s_k} (sorted descending), under greedy picking.

V(S) = s_1 + s_3 + s_5 + ...

Now, define W(P) = min over all XY responses to LB's pieces P (after LB's marking but before XY's).

W(P) = min_{M_XY} V(refine(P, M_XY))

where refine(P, M_XY) splits pieces according to XY's marks.

**LB's problem:** Choose marks M_LB to maximize W(P(M_LB)).

**Claim.** W(geometric pieces) = c(n).

**GAP:** Compute W for general piece configurations and show geometric is optimal.

---

### Part 6: Recursive / Inductive Value Computation

**Base case n=1:** 
LB marks at x. Pieces {x, 1-x}. 
XY can mark at y in (x, 1-x) or elsewhere.
Analysis shows c(1) = 2/3 when x = 1/3.

**Inductive claim:** c(n) satisfies 1/c(n) = 2 - 2^{-n}.

**GAP:** Prove the recurrence by analyzing the game tree.

---

## Key Lemmas (with mechanism)

1. **Greedy optimality:** V(S) = sum of odd-indexed pieces in S (sorted descending). This is because greedy is dominant.

2. **Geometric dominance (from crux aimo-0117):** The geometric configuration {1, 2, ..., 2^n}/D has 2^n > 2^{n-1} + ... + 1, so LB's first pick is guaranteed to be the largest piece if XY doesn't cut it.

3. **XY's odd-piece penalty:** Creating 2n+1 pieces gives LB n+1 picks, which increases LB's value.

4. **Minimax saddle point:** The geometric LB strategy and the (n-1)-mark XY strategy form a Nash equilibrium where both achieve value c(n).

---

## Open Gaps

1. **Lower bound rigorous proof:** Show W(geometric) >= c(n) against all XY responses.

2. **Upper bound rigorous proof:** Show W(any LB config) <= c(n), i.e., XY can always achieve c(n).

3. **Saddle point verification:** Show the geometric strategies are mutual best responses.

---

## Cases to Cover

- All XY responses to the geometric LB marking (for lower bound)
- All LB markings and XY's optimal counter (for upper bound)

---

## Watch out for

- The minimax theorem applies here because the strategy spaces are compact and payoffs are continuous. But we need explicit constructions, not just existence.
- The game is not symmetric; LB moves first and picks first.
- The refinement operation (splitting pieces) is XY's only power; XY cannot move or merge pieces.
