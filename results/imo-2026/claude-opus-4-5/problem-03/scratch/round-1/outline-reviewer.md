# Outline Review: IMO 2026 P3

## Problem Summary
Determine c(n) = largest value LB can guarantee in a stick-division game. The claimed answer is c(n) = 2^n / (2^{n+1} - 1).

## Small-Case Verification (Sanity Check)
I verified the claimed answer computationally:
- c(1) = 2/3: Confirmed. LB marks at 1/3 (or 2/3), and XY's best response gives LB exactly 2/3.
- c(2) = 4/7: Confirmed. LB's geometric marking at 1/7, 3/7 with XY's optimal 1-mark response gives exactly 4/7.
- c(3) = 8/15: Confirmed. LB's geometric marking with XY's optimal 2-mark response gives exactly 8/15.

The formula and constructions check out.

---

## Approach 1: geometric-direct

**Summary:** Direct construction (geometric-ratio partition) plus case analysis.

**Structure Check:**
- Target is the full claim c(n) = 2^n / D: YES, complete attempt.
- Both directions (upper + lower bound): YES, explicitly stated.

**Technique Assessment:** Sound. The geometric construction is standard for these problems, and the "geometric dominance" property (2^n > 2^n - 1) is the right crux. The crux aimo-0117 reference is appropriate.

**Skeleton Review:**
1. LB's geometric strategy: Well-defined, verified correct.
2. XY's optimal counter: Correct structure (n-1 marks creating paired configuration).
3. Greedy optimality lemma: Stated with correct mechanism (exchange argument).
4. Upper bound (XY limits LB to c(n) on geometric LB): Partially complete. The exact sorted structure and alternating sum need verification, but the outline acknowledges this gap.
5. Lower bound Case A (XY marks outside L_n): Complete and correct.
6. Lower bound Case B (XY marks inside L_n): **GAP** - this is a real gap requiring case analysis.
7. Upper bound for arbitrary LB strategies: **GAP** - the hardest direction, acknowledged.

**Issues:**
- Gap 6 (Case B) is tractable: it requires careful case analysis on j marks inside L_n, but the geometric structure should yield. The mechanism "intact pieces compensate" is plausible but needs formalization.
- Gap 7 (arbitrary LB upper bound) is the shared hard gap across all approaches. This requires showing XY's "equalizing" response works for any LB configuration.

**Verdict: APPROVE**

The approach is sound and targets the full claim. The gaps are real but tractable. The geometric-direct route is the most concrete and closest to a buildable proof.

---

## Approach 2: induction-on-n

**Summary:** Strong induction on n, using the recurrence 1/c(n) = 2 - 2^{-n}.

**Structure Check:**
- Target is the full claim: YES.
- Base case complete: YES (n=1 with exhaustive case analysis).
- Inductive step: Outlined but not filled.

**Technique Assessment:** Sound. The recurrence is correct (verified: 1/c(n) = D/2^n = 2 - 2^{-n}). The scaling lemma relating n to n-1 is algebraically correct.

**Skeleton Review:**
1. Base case n=1: Complete and verified.
2. Inductive hypothesis: Standard.
3. Scaling lemma: The pieces {1, 2, ..., 2^{n-1}}/D rescale to the (n-1) geometric configuration. This is algebraically correct but the interaction with XY's marks and pick order is subtle.
4. Lower bound via induction: **GAP** - the reduction to the (n-1) problem is not cleanly stated. When XY marks inside L_n, how does the problem reduce?
5. Upper bound via induction: **GAP** - same shared gap as geometric-direct.

**Issues:**
- The scaling is not exact: after XY marks, the subproblem on L_0, ..., L_{n-1} is not independent of the sub-pieces from L_n. The greedy picks interleave both parts. This makes the induction non-trivial.
- The mechanism for the inductive step is vague ("scaling lemma" without explaining how the interleaved picks work).

**Verdict: APPROVE**

The approach is structurally sound, and induction is a valid technique. However, the inductive step's mechanism is under-specified. The builder should focus on formalizing how XY's marks on L_n interact with the (n-1) sub-structure during greedy picking.

---

## Approach 3: piece-count-parity

**Summary:** Parity analysis of piece count to explain XY's optimal mark count (n-1).

**Structure Check:**
- Target is the full claim: YES.
- Both directions: YES.

**Technique Assessment:** The parity insight is correct and useful: XY prefers even piece count (2n) to avoid giving LB an extra pick. However, parity alone does not prove the exact value c(n). This is acknowledged in the outline.

**Skeleton Review:**
1. Piece count analysis: Correct.
2. XY prefers even count: Correct mechanism.
3. LB uses all n marks: Correct (verified: fewer marks hurt LB).
4. XY's optimal is n-1 marks: Correct.
5. Exact alternating sum: **GAP** - not computed.
6. Lower bound cases: **GAP** - similar to geometric-direct.
7. Upper bound for arbitrary LB: **GAP** - the shared hard gap.

**Issues:**
- The parity argument is a supporting insight, not the main proof technique. The outline correctly identifies that it must combine with value calculations.
- This approach is essentially geometric-direct with an extra lens (parity). It doesn't offer a fundamentally different route.

**Verdict: APPROVE**

Sound but less distinct from geometric-direct. The parity insight is valuable as a lemma but doesn't bypass the hard gaps. Keep as a supporting perspective.

---

## Approach 4: minimax-value

**Summary:** Game-theoretic minimax formulation; value function on piece configurations.

**Structure Check:**
- Target is the full claim: YES.
- Both directions: YES (via saddle point).

**Technique Assessment:** Correct framing. The game is a finite, perfect-information, zero-sum game, so the minimax theorem applies. However, the outline correctly notes that we need explicit constructions, not just existence.

**Skeleton Review:**
1. Game formulation: Correct.
2. Greedy optimality: Correct (V(S) = sum of odd-indexed pieces).
3. LB's optimal strategy: **GAP** - proving W(geometric) >= c(n) against all XY.
4. XY's optimal response: **GAP** - proving XY can achieve c(n) against any LB.
5. Value function recursion: Mentioned but not developed.
6. Saddle point: Would follow from 3 and 4.

**Issues:**
- This approach is more abstract than geometric-direct. It's valuable for framing but doesn't offer a shortcut to the proofs.
- The gaps are exactly the same as geometric-direct (lower bound Case B, upper bound for arbitrary LB).
- The value function recursion (Part 6) could potentially help, but it's not developed.

**Verdict: APPROVE**

The minimax framing is correct and provides good conceptual clarity. However, it has the same gaps as geometric-direct and doesn't offer a fundamentally different attack. Keep as a secondary perspective.

---

## Shared Gaps Across All Approaches

1. **Lower bound, Case B:** When XY places j >= 1 marks inside L_n, prove LB >= c(n). This is tractable via case analysis.

2. **Upper bound for arbitrary LB:** Prove XY can limit any LB configuration to <= c(n). This is the hard direction. All approaches punt on this. Mechanisms suggested include:
   - "Equalizing" XY response
   - Induction on n
   - Showing geometric is optimal for LB

This shared gap is a risk, but it's correctly identified and there are plausible attack vectors.

---

## No Circular Reasoning or Dead-End Repeats

- No approach assumes the conclusion.
- No approach repeats a known dead end (the `current.md` has no prior attempts).

---

## Comparisons and Ranking

The four approaches are:
1. **geometric-direct**: Most concrete, closest to a buildable proof.
2. **induction-on-n**: Valid technique, but the inductive step is under-specified.
3. **piece-count-parity**: Good supporting insight, but essentially a lens on geometric-direct.
4. **minimax-value**: Good framing, but doesn't simplify the gaps.

Ranking:
- geometric-direct > induction-on-n (more concrete skeleton, fewer mechanism gaps)
- geometric-direct > piece-count-parity (parity is a sub-lemma, not a full route)
- geometric-direct > minimax-value (same gaps, more abstract)
- induction-on-n ~ minimax-value (different techniques, similar incompleteness)
- induction-on-n > piece-count-parity (induction is a full technique, parity is supplementary)

---

## Summary of Verdicts

| Approach | Verdict | Notes |
|----------|---------|-------|
| geometric-direct | APPROVE | Register; prioritize for build |
| induction-on-n | APPROVE | Register; secondary priority |
| piece-count-parity | APPROVE | Register; lower priority (supplementary insight) |
| minimax-value | APPROVE | Register; lower priority (framing, same gaps) |

---

## Build Set

Given the overlapping gaps, focus on the two most distinct and promising approaches:

1. **geometric-direct** - the most concrete, closest to a full proof.
2. **induction-on-n** - offers a potentially different route via recursion.

The other two (parity, minimax) provide useful lenses but don't offer fundamentally different attacks on the hard gaps. Defer them unless the primary approaches stall.

---

build set: geometric-direct, induction-on-n
