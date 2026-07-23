# Outline Review: IMO 2026 P5

## Problem
Determine all functions f: R+ -> R+ such that sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x*f(y)) for every x, y > 0.

---

## orbit-invariance

**Verdict: CHANGES REQUESTED**

**Assessment:** This is the strongest approach. The core technique is sound:
1. The x = f(y) substitution correctly forces f(f(y)) = 2f(y) - y (verified algebraically).
2. The orbit-invariance g(f(y)) = g(y) follows immediately.
3. The algebraic identities L + R = 2(x - f(y))^2 and L - R = 2(g(y) - g(x))*(sum) are correct (verified by computer algebra).
4. The descent argument for g >= 0 is correct.

**Issues to fix:**

1. **Step 5 (orbit-growth) incomplete case coverage.** The outline flags the a = 0 case but doesn't handle it. I verified:
   - When 0 < a < b: The orbit-growth argument works. Choosing n ~ bt, m ~ at makes (x - f(y))^2 = O(1) while RHS = (b-a)*O(t) diverges. Contradiction confirmed numerically.
   - When a = 0 and b > 0: The orbit-growth argument FAILS (LHS grows as O(m^2), RHS as O(m)). However, a DIRECT violation occurs at finite (x, y): at any fixed point x (g(x) = 0) and any point y with g(y) = b > 0, the constraint R >= 0 requires (x - y - b)^2 >= b*(2x + 2y + b), which fails for many (x, y) pairs (verified numerically with multiple examples).

   **Fix needed:** The builder must add the a = 0 case explicitly, showing R < 0 at some finite (x, y) when g is not identically zero or positive everywhere.

2. **Orbit index validity.** The note about n, m being positive integers is correct but the fix is easy: for large enough t, round(bt) and round(at) are both positive. State this explicitly.

**No circular reasoning detected. Skeleton is sound.**

---

## differentiability-squeeze

**Verdict: CHANGES REQUESTED**

**Assessment:** The technique is viable as a cleaner route, but the differentiability assumption is a load-bearing gap that needs a mechanism, not just a label.

**Issues:**

1. **Gap in Step 4: Differentiability unjustified.** The outline says "Justifying the differentiability assumption" but provides no mechanism. This is a load-bearing lemma stated without a reason it's true.

   **Fix needed:** Either:
   - (a) Prove f is locally Lipschitz from the constraint (e.g., from L >= 0, bound |f(x) - f(y)| in terms of |x - y|), or
   - (b) Replace the derivative with a finite-difference argument: from L(f(y) + eps, y) >= 0 and L(f(y) - eps, y) >= 0 for small eps, derive the same constraint algebraically without derivatives.

   Option (b) is more promising: the second-order Taylor expansion of L at x = f(y) is dominated by the quadratic term (L achieves its minimum there), so the first-order coefficient must vanish by expansion, not by calculus.

2. **Step 5 range argument is vague.** "The range of f is (c, infinity)" needs proof. If f(x) = x + c, range is (c, infinity). But proving the range structure a priori requires showing f is continuous and strictly increasing first.

**The approach can work, but is more delicate than orbit-invariance.**

---

## direct-squeeze

**Verdict: CHANGES REQUESTED (low priority)**

**Assessment:** This approach correctly identifies that the solution has (f(x) + y)/2 = AM(x, f(y)), but Step 4 (the crux) is essentially empty.

**Issue:**

1. **Step 4 is not a proof step.** "The claim is: if g is non-constant, for some (x, y) either L < 0 or R < 0" is the statement to prove, not a method. The outline admits this likely "reduces back to the orbit or differentiation argument."

   This approach collapses to orbit-invariance at the crux step. It's not independent.

**No fatal flaw, but low diversity value. Deprioritize unless the builder finds a shortcut.**

---

## Diversity Assessment

All three approaches share the same framing: derive f(f(y)) = 2f(y) - y from x = f(y), then prove g = f - id is constant. They differ only in the technique for the final step:
- orbit-invariance: orbit growth + R < 0 at finite points
- differentiability-squeeze: calculus / finite differences at the minimum
- direct-squeeze: (no technique specified)

This is technique variation on one framing, not independent approaches. If the shared reduction (x = f(y) forces the functional equation) turns out wrong, all three fail together.

However, I verified the x = f(y) reduction algebraically and numerically - it is correct. The framing is sound, so technique variation is acceptable here.

---

## Ranking

Registered approaches: orbit-invariance, differentiability-squeeze, direct-squeeze

Comparisons:
- orbit-invariance > differentiability-squeeze (no regularity assumption, more elementary)
- orbit-invariance > direct-squeeze (direct-squeeze has no mechanism for crux)
- differentiability-squeeze > direct-squeeze (at least has a stated technique)

Current Elo: orbit-invariance (1531) > differentiability-squeeze (1500) > direct-squeeze (1469)

---

## Build Set

Prioritize **orbit-invariance** (strongest, most elementary, clear path to completion). Include **differentiability-squeeze** as a parallel track if the builder can resolve the regularity gap quickly. Skip direct-squeeze (it reduces to orbit-invariance anyway).

**build set: orbit-invariance, differentiability-squeeze**
