# Outline Review: IMO 2026 P3 (Round 6)

## Context

The proof for c(n) = 2^n / (2^{n+1} - 1) is complete for n=1,2,3. The gap is Case B upper bound for n >= 4. Three explorers provided:
1. **LP-duality explorer**: Saddle-point structure; five singleton-difference formulas A,B,C,D,E
2. **n4-explicit explorer**: Complete algebraic pigeonhole proof that min(A,B,C,D,E) <= 1
3. **Sum-slack explorer**: Strategy S5 construction; interval coverage proof for Case A

---

## Approach 1: geometric-direct (advance)

**Target:** c(n) = 2^n / (2^{n+1} - 1) for all n  
**Verdict:** APPROVE

**Technique assessment:** The Singleton-Pair Formula + sum-slack + pigeonhole approach is sound. The n=4 Case B now has two complementary attack paths:

1. **Five-formula pigeonhole** (n4-explicit explorer): min(A,B,C,D,E) <= 1 under 4x+3y+2z+w < 15. The two-case proof (Case II: x>2 gives C<=1; Case I: x<=2 gives chain contradiction) is algebraically verified (0/45,000 failures, max min = 0.79 < 1).

2. **Interval coverage** (sum-slack explorer): For "Case A" (gamma >= alpha+1, eta >= beta+1), the strategies S5+B+PP cover all eta values with no gaps. Key: gap width = alpha - 2 < 0 since alpha < 1/3. Also verified (0/49,000 failures).

**Sound skeleton:** 
- Step 1-3 (PROVED): Lower bound, Case A, n=1,2,3 - all rigorous.
- Step 4 (BUILD): n=4 Case B via the algebraic coverage. Two valid paths:
  - Path A: S1/S2/S3 for d_j <= L_0 (follows n=3 pattern); S4+S5+S6+B+PP for "all d_j > L_0".
  - Path B: Direct pigeonhole on min(A,B,C,D,E) <= 1 with explicit strategies S_A through S_E.

**Load-bearing lemmas with mechanisms:**
- Singleton-Pair Formula (CERTIFIED): LB = 1/2 + (s2-s1)/2 because pairing cancellation isolates the singleton difference.
- n=4 Pigeonhole Lemma: min(A,B,C,D,E) <= 1 because Case II (x>2) forces C<=1 and Case I (x<=2) leads to sum contradiction via chain A>1->z>x+1, B>1->w>x+1, etc.
- Case A interval coverage: gap width = alpha - 2 < -5/3 < 0 because alpha < 1/3 (from sum constraint 6*alpha + 4*beta < 2).

**Missing pieces (for builder):**
- S_E explicit construction (formula E = |2P_1+d_1-d_3| <= L_0). The explorers note this needs a non-standard structure. The sum-slack explorer suggests S5+B+PP may cover this range implicitly via the interval analysis.
- The builder should choose ONE of the two paths (pigeonhole vs interval coverage) and complete it fully.

**Small-case sanity:** VERIFIED. Both algebraic claims (pigeonhole and interval coverage) pass 50k+ random configs with 0 failures.

**Avoids dead ends:** Yes. The induction-on-n approach (Round 1 dead-end) is not used. The "single recursive strategy" trap is avoided.

**Recommendation:** APPROVE. The builder should add n=4 Case B using the **interval coverage approach** from the sum-slack explorer (S4+S5+S6+B+PP) because it has cleaner algebraic structure than the five-formula pigeonhole. The key is to:
1. Handle "some d_j <= L_0" via S4/S6 (existing patterns)
2. For "all d_j > L_0, gamma >= alpha+1, eta >= beta+1": prove S5/B/PP cover [beta+1, eta_max] with gap width = alpha-2 < 0
3. For "all d_j > L_0, gamma < alpha+1 or eta < beta+1": show S4 or S6 applies

---

## Approach 2: n4-algebraic-coverage (new)

**Target:** c(4) = 16/31 with complete algebraic proof  
**Verdict:** CHANGES REQUESTED

**Technique assessment:** Valid. The reduced-variable parameterization (alpha, beta, gamma, eta) is correct and simplifies the algebra.

**Issues:**
1. **Interval endpoints need verification.** The outline claims S5 covers eta in [beta+1, alpha+beta+2] and B covers [2*alpha+beta, 2*alpha+beta+2]. The sum-slack explorer verified these numerically but the builder should confirm the exact boundary conditions (e.g., is eta=beta+1 strict or non-strict?).

2. **Non-Case-A handling incomplete.** The outline says "S6 or S4" but doesn't specify the exact sub-cases. Specifically: when gamma < alpha+1 but eta >= beta+1, only S6 works; when gamma >= alpha+1 but eta < beta+1, only S4 works. The builder should verify these don't overlap.

3. **S5, B, PP explicit constructions.** The outline lists these as "builder task" but they're critical. The sum-slack explorer gave S5 explicitly; B and PP need clearer descriptions.

**Recommendation:** CHANGES REQUESTED. This is essentially the same proof as geometric-direct Step 4 but isolated as a standalone approach. Since geometric-direct is further along and includes n=1,2,3, building both would be redundant. **Do not build separately** - fold into geometric-direct.

---

## Approach 3: n4-pigeonhole (copy-of geometric-direct)

**Target:** c(4) = 16/31 with five-formula pigeonhole  
**Verdict:** RETHINK

**Technique assessment:** The pigeonhole approach (min(A,B,C,D,E) <= 1) is mathematically valid and verified. However:

**Fatal flaw:** This is NOT a distinct approach - it's the same proof as the n4-algebraic-coverage with different notation (x,y,z,w vs alpha,beta,gamma,eta). Both reduce to "show some singleton-difference formula <= L_0." Creating this as a copy-of geometric-direct would be the **single-line trap** - two slugs pursuing identical proofs. If the five-formula approach fails, both fail together.

**S_E gap:** The pigeonhole proves min(A,B,C,D,E) <= 1 but the explicit strategy for E <= L_0 is missing. The explorer notes "S_E explicit construction pending." This is the same gap as in n4-algebraic-coverage (both need S5/B/PP to cover the E regime).

**Recommendation:** RETHINK. Do not copy as a separate approach. The pigeonhole proof and the interval-coverage proof are complementary views of the SAME algebraic structure. The builder should use the cleaner interval-coverage path within geometric-direct.

---

## Approach 4: minimax-saddle-point (advance, lower priority)

**Target:** c(n) for all n via saddle-point theory  
**Verdict:** CHANGES REQUESTED (but de-prioritize)

**Technique assessment:** Sion's minimax theorem guarantees the saddle point exists. The geometric config is indeed the saddle point. However:

**Issues:**
1. **"XY's geometric-response works universally" is FALSE.** The LP-duality explorer explicitly notes this. The geometric-config XY response (split L_n into {L_{n-1},...,L_0,L_0}) does NOT limit arbitrary LB configs to c(n). Different LB configs require different XY strategies.

2. **No direct proof path.** The outline says "provides intuition but not direct proof." This is correct - saddle-point existence doesn't give a constructive proof of the strategies.

**Recommendation:** CHANGES REQUESTED but **do not build this round**. The geometric-direct approach is much further along. If n=4 is closed via interval coverage, the saddle-point approach becomes unnecessary for n=4 and remains open for n>=5 anyway.

---

## Approach 5: induction-on-n (dead-end)

**Verdict:** Confirmed DEAD END. Round 1 showed fatal flaw in upper bound. Do not retry.

---

## Registration and Ranking

**New approaches to register:**
- None. The outliner proposed n4-algebraic-coverage and n4-pigeonhole, but:
  - n4-algebraic-coverage is effectively the n=4 portion of geometric-direct, not a distinct whole-problem approach
  - n4-pigeonhole was proposed as copy-of geometric-direct but should not be copied (same proof, single-line trap)

**Ranking comparisons:**

- geometric-direct vs minimax-saddle-point: **geometric-direct wins** (has complete proof for n=1,2,3 and clear path to n=4; minimax has no direct proof path)
- geometric-direct vs induction-on-n: **geometric-direct wins** (induction is dead-ended)
- minimax-saddle-point vs induction-on-n: **minimax-saddle-point wins** (live vs dead)

---

## Build Set

**build set: geometric-direct**

**Instructions for builder:**
1. Add n=4 Case B proof using the **interval-coverage approach** from the sum-slack explorer.
2. Structure:
   - **Non-Case-A** (gamma < alpha+1 or eta < beta+1): S6 or S4 applies.
   - **Case A** (gamma >= alpha+1 AND eta >= beta+1): S5+B+PP cover all eta in [beta+1, eta_max] with gap width = alpha-2 < 0.
3. Verify S5, B, PP explicit constructions (8 pieces = 3 pairs + 2 singletons).
4. Complete the algebraic verification that sum constraint forces alpha < 1/3 in Case A.
5. Once n=4 is closed, outline the generalization path to n>=5 (extra marks give more flexibility, gap widths remain negative).
