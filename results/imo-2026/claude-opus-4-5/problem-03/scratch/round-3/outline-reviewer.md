# Outline Review: IMO 2026 P3 (Round 3)

## Field Summary

The outliner proposed 4 approaches:
1. **induction-on-n** (revise) - k*-largest pigeonhole fix for failed Lemma 5
2. **n2-explicit-casework** (new) - direct 4-case analysis for n=2 base, then induction
3. **ratio-based-induction** (advance) - ratio threshold 2 organizing principle
4. **exchange-argument** (advance) - variational proof that geometric marking is LB-optimal

## Approach Reviews

---

### induction-on-n (revise)

**Verdict: APPROVE**

The k*-largest pigeonhole approach is mathematically sound. I verified the key claims:

1. **Pigeonhole existence** (at least one k satisfies p_k <= 2^{k-1}*S*t_m): Correct. If all k fail, the sum exceeds S by the geometric sum identity.

2. **No-interleaving ratio bound** (p_{k*+1}/p_{k*} > 2): Correct. Follows from k* satisfying the condition and k*+1 failing it.

3. **Sub-problem size bound** (S_{k*} < (2^{k*}-1)*S*t_m): Correct. Derived from summing the strict inequalities for j > k*.

4. **Algebraic miracle** (S_{k*}*t_{k*-1} < S*t_m): Correct. The (2^{k*}-1) factor cancels with 1/(2^{k*}-1) = t_{k*-1}.

Tested on the R2 counterexample [107/700, 93/350, 407/700]:
- k* = 2 (the largest satisfying index)
- Ratio p_3/p_2 = 2.19 > 2, so no interleaving
- S_2 = 0.419 < 0.429 = 3/7 = (2^2-1)*t_2
- XY's halve+recurse strategy yields LB take = 0.556 < 0.571 = c(2)

**Open gaps identified in outline are real:**
- Sandwich strategy for k* = m+1 (when largest piece is small)
- Formal verification that pairs don't interleave with sub-problem pieces

Both are tractable given the ratio > 2 condition. The builder can close these.

---

### n2-explicit-casework (new)

**Verdict: CHANGES REQUESTED**

The n=1 base is fine (already proven). The n=2 casework has issues:

**Case B formula is WRONG.** The outline claims that when a_3 in [3/7, 4/7], cloning gives A = |2a_3 - 1|, hence LB = (1 + A)/2 = a_3.

Numerical test with (3/14, 5/14, 3/7):
- After cloning a_1 twice: pieces become [3/14, 3/14, 1/7, 3/14, 3/14]
- Sorted: four 3/14 pieces and one 1/7 piece
- LB takes positions 1,3,5: gets 3*(3/14) = 9/14 = 4/7 (NOT a_3 = 3/7)

The formula "A = |2a_3 - 1|" doesn't match the actual alternating sum computation.

**Changes needed:**
1. Rework Case B with correct alternating sum calculation
2. Verify sorted order for both a_3 <= 1/2 and a_3 > 1/2 sub-cases
3. The Cases C and D also need verification before building

The approach is viable (explicit casework is rigorous when done correctly), but the current Case B is broken.

---

### ratio-based-induction (advance)

**Verdict: CHANGES REQUESTED**

The n=1 base case is complete and rigorous. The inductive step has known gaps (already flagged in the approach file):

1. Sorted order after first XY move (halved/cloned pieces may interleave)
2. Residual problem satisfies IH conditions
3. Combining alternating sum contributions

These are the SAME gaps as induction-on-n faced, and the k*-largest fix addresses them directly. The ratio-based framing adds no new insight beyond what the revised induction-on-n approach provides.

**Recommendation:** This approach is essentially a re-skin of induction-on-n. The k*-largest fix applies equally here. Not worth building separately; focus on induction-on-n which is further along.

---

### exchange-argument (advance)

**Verdict: CHANGES REQUESTED**

The variational/exchange approach is elegant but underspecified:

**Critical gap:** The first-order optimality claim "dV/dp_k = 0 at geometric" is stated without mechanism. The value function V(L) = min_X G(L,X) is not differentiable (it's a piecewise linear function of piece sizes, with discontinuities when sorted order changes). The outline acknowledges "tied pieces create discontinuities" but offers no resolution.

**Deeper issue:** This approach proves the same conclusion (geometric is unique LB optimum) by a different method, but the induction-on-n approach already establishes this via the saddle-point argument. The exchange argument adds nothing to the proof unless it can handle the non-differentiability.

**Recommendation:** Not ready for building. The variational analysis is a dead end without regularization, and regularization would add complexity without benefit. The direct induction approach is more tractable.

---

## Diversity Check

The four approaches share the same target (prove c(n) = 2^n/(2^{n+1}-1)) and mostly attack via the same reduction (show XY can limit any LB marking). This is appropriate - the answer is computationally verified, so diversity should be in proof technique, not in final claim.

However, three of the four approaches (induction-on-n, ratio-based-induction, n2-explicit-casework) are variations of the same inductive structure. Only exchange-argument attempts a different route (variational), and it's currently stuck.

**Assessment:** The field has collapsed to one framing (induction). This is acceptable because the induction approach has now fixed its fatal flaw (k*-largest instead of false Lemma 5). If this round's build still fails, the next outliner should explore minimax theorem formalizations or direct LP duality arguments.

---

## Rankings

Comparing the field:

- **induction-on-n** > **ratio-based-induction** (same approach, induction-on-n is more developed with k*-largest fix)
- **induction-on-n** > **n2-explicit-casework** (n2 has a broken Case B formula)
- **induction-on-n** > **exchange-argument** (exchange is stuck on non-differentiability)
- **n2-explicit-casework** > **ratio-based-induction** (n2 at least attempts full casework; ratio-based is just less-developed induction)
- **exchange-argument** draws **ratio-based-induction** (both incomplete, different routes)

---

## Build Set

**Build:** induction-on-n

This is the only approach with a sound skeleton and tractable gaps. The k*-largest pigeonhole fix addresses the R2 failure. The builder should:
1. Formalize the sandwich case (k* = m+1)
2. Prove pair-cancellation applies when ratio > 2 ensures no interleaving
3. Handle the equal-pieces edge case in the sandwich

Do NOT build n2-explicit-casework this round (Case B formula is wrong - fix needed first).
Do NOT build ratio-based-induction (redundant with induction-on-n).
Do NOT build exchange-argument (stuck on variational discontinuity).

**build set: induction-on-n**
