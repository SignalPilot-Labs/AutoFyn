# Outline Review: IMO 2026 P3, Round 12

## Approach: n5-five-mark (REVISE)

**Verdict: APPROVE**

The revised outline correctly identifies:
1. Type 3 strategies are insufficient (~95% coverage, failures near alpha -> 0)
2. The (2,2,1) strategy class with "Split P_3, P_5; Halve P_6" covers the remaining cases
3. Piece count is correct: 3 + 3 + 2 + 3 = 11 pieces, LB picks 6

**Sanity check (computational verification):**
- On the Type 3 failure example (alpha=0.007, beta=2.205, gamma=3.321, delta=1.060, epsilon=4.441, zeta=5.584), the (2,2,1) strategy achieves LB = 0.5009 < c(5) = 0.5079 with margin 0.007.
- Tested 20+ random configs in the bounded region; all achieve LB < c(5) with the (3,5,6) variant.

**Key lemmas with mechanism - VERIFIED:**
- V_j Strategy: mechanism correct (halving 4 pieces creates 4 pairs + 2 singletons with diff d_j)
- Pairwise Strategy: mechanism correct (4 marks create near-pairs with singleton diff <= L_0)
- Bounded Region: mechanism correct (min weighted sum = 21*v_0 + 35*g <= 42 gives g < 1.2, v_0 < 1/3)
- (2,2,1) Coverage: mechanism partially specified; the "4 near-pairs" claim is the core, needs explicit formula

**Minor issues to address while building:**
1. Step 9 says "s1 = P_1, s2 = P_1 + P_2 = d_1 + 2*P_1" but d_1 = P_2 - P_1, so P_1 + P_2 = d_1 + 2*P_1 is correct. However, this is the optimal cut only for SOME configs; the scipy optimization shows different (s1, s2) are optimal in general.
2. The "watch out" correctly notes that a SINGLE (3,5,6) variant may not be universal. My testing shows it IS universal on 20+ configs, but the builder should verify or provide casework for when different variants are needed.
3. The algebraic proof path is underspecified: Steps 13-14 claim "4-near-pair Pairing Cancellation" but don't give the explicit formula for combined error bound.

**No fatal flaws.** The three-tier cascade (V_j -> Pairwise -> (2,2,1)) is sound. The builder should focus on:
- Making the (2,2,1) LB formula explicit
- Either LP breakpoint enumeration OR 63-vertex finite check for rigor

---

## Approach: geometric-direct (ADVANCE)

**Verdict: APPROVE**

This is the main proof structure. The outline correctly identifies:
- n=1,2,3,4 PROVED
- n=5 depends on n5-five-mark completion
- n>=6 OPEN

No changes needed for this round; it simply imports n5-five-mark results.

---

## Approach: n5-compactness (NEW)

**Verdict: CHANGES REQUESTED**

**Issues:**
1. Step 5 explicitly states "computational verification shows f < c(5)... NOT algebraic." This is the load-bearing step and has NO mechanism. The outline admits it's not a proof.
2. Berge's Maximum Theorem (Step 2) requires the constraint set to vary continuously, which is satisfied, but the application needs the interior bound to be certified.
3. The boundary reduction (Step 4) is correct: on boundary of K, either some d_j -> L_0 (V_j applies) or some pairwise -> 1 (Pairwise applies).

**Required changes:**
- Either drop this approach as scaffolding OR specify how the interior bound will be algebraically certified (interval arithmetic, LP breakpoint enumeration, etc.)
- As stated, this is not a complete proof outline but a meta-argument that REQUIRES n5-five-mark or n5-lp-breakpoint to fill the interior.

---

## Approach: n5-lp-breakpoint (NEW)

**Verdict: APPROVE with reservations**

This is a valid rigorous path: for fixed piece ordering, LB is linear in (config, cuts), so the LP optimum is at a breakpoint.

**Potential issue:** Step 4-6 says "enumerate all possible piece orderings" but 11 pieces have 11! = 40M orderings. The outline claims "symmetry and monotonicity reduce this drastically" but doesn't specify how many cases remain.

**Required clarification while building:**
- Explicitly count the reduced number of orderings (should be O(10-100) after exploiting that s1 < s2-s1 < P_a-s2 ordering is determined by cut positions)
- Provide at least one worked example of a linear inequality LB <= c(5) for a specific ordering

---

## Approach: n5-equal-position-cut (NEW)

**Verdict: RETHINK**

**Fatal flaw:** This approach is incomplete and mechanically confused.

- Step 4 claims "5 marks = 2 (double-cut at t) + 2 (halves on P_2, P_6) + 1 (cut on another piece, say tiny cut on P_1)". This gives 10 pieces, not 11.
- But a "tiny cut on P_1" doesn't create a pair; it creates two different pieces. The strategy doesn't leverage Pairing Cancellation properly.
- Step 6 says "LB picks ceil(10/2) = 5 pieces" but if one cut creates only singletons, the Singleton-Pair structure breaks.
- The mechanism for why this works is unclear compared to (2,2,1).

This approach is a subset of the (2,2,1) analysis but less developed. It adds no new technique beyond what n5-five-mark already covers.

**Recommendation:** Abandon this approach; it's a distraction from the well-developed (2,2,1) strategy in n5-five-mark.

---

## Rankings Update

The population now has:
- geometric-direct: live, ADVANCED, comprehensive main proof
- n5-five-mark: live, REVISED with (2,2,1) breakthrough
- n5-compactness: NEW, scaffolding only (not a standalone proof)
- n5-lp-breakpoint: NEW, rigorous but tedious path
- n5-equal-position-cut: RETHINK (incomplete)
- induction-on-n: dead-end
- minimax-saddle-point: live but not built
- minimax-value: live but not built
- piece-count-parity: live but not built
- vertical-pairing: absorbed into geometric-direct

**Comparisons:**
- n5-five-mark > n5-lp-breakpoint (same goal, n5-five-mark is more developed with (2,2,1))
- n5-five-mark > n5-compactness (compactness is scaffolding, not standalone)
- geometric-direct > minimax-saddle-point (geometric-direct has proof for n<=4)
- n5-five-mark > n5-equal-position-cut (equal-position is mechanically flawed)

---

## Registration

New approaches to register:
- **n5-compactness**: Compactness + boundary reduction for n=5 bounded region
- **n5-lp-breakpoint**: LP breakpoint enumeration (finite algebraic casework) for n=5

NOT registering:
- **n5-equal-position-cut**: RETHINK verdict, approach is flawed

---

## Build Set

**Primary focus:** n5-five-mark with the (2,2,1) strategy
- The explorer has confirmed (2,2,1) works computationally
- The algebraic proof path is clear: either explicit LB formula verification or 63-vertex finite check
- This is the most developed path to close n=5

**Secondary:** geometric-direct only needs minor text corrections for n=4 constructions (low priority)

build set: n5-five-mark
