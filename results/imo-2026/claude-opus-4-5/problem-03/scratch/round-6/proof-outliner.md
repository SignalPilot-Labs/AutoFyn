## imo-2026-03

geometric-direct: advance
Target: c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Singleton-Pair Formula + algebraic case coverage on (d_j > L_0) sub-cases
Skeleton:
  1. (PROVED) Lower bound for all n: geometric config achieves c(n)
  2. (PROVED) Upper bound Case A (P_1 <= L_0): Halve-All gives LB = 1/2 + P_1/2 <= c(n)
  3. (PROVED) Upper bound Case B for n=1,2,3
  4. (OPEN -> BUILD THIS ROUND) Upper bound Case B for n=4: five strategies cover all d_j > L_0 sub-cases
  5. (OPEN) Upper bound Case B for general n >= 5: induction from n=4 pattern
Key lemmas (claim + the one-line mechanism that makes it true):
  - Singleton-Pair Formula (certified): LB = 1/2 + (s2-s1)/2 for 2n pieces = (n-1) equal pairs + 2 singletons -- because pairing cancellation gives LB = (pairs total)/2 + larger singleton
  - n=4 Case B Strategy Coverage: the five-strategy family {S1, S2, S3, S4, S5+B+PP} covers all (P_1 > L_0, P_5 > c(4)) configs -- because S1/S2/S3 cover (some d_j <= L_0) and S4/S5/B/PP cover (all d_j > L_0) with no gaps
  - Sum-Slack Bound for n=4: 4P_1 + 3d_1 + 2d_2 + d_3 < 15L_0 -- because P_5 > 16L_0 = c(4) implies P_1+P_2+P_3+P_4 < 15L_0
  - Case A Sub-case (all d_j > L_0): when gamma >= alpha+1 AND eta >= beta+1, sum forces 6*alpha + 4*beta < 2, so alpha < 1/3 -- because Case A with all d_j > L_0 is very constrained
  - Gap Width < 0: gap between S5 and B has width alpha - 2 < 1/3 - 2 < 0 -- because S5 covers eta up to alpha+beta+2 and B starts at 2*alpha+beta, their overlap when alpha < 1/3
Open gaps:
  - Strategies S4, S5, B, PP explicit constructions for all d_j > L_0 sub-case
  - Strategy B/PP may not use 3 pairs + 2 singletons structure (need to verify what structure works)
  - Extension to n >= 5
Cases to cover: 
  - n=4: S1/S2/S3 when some d_j <= L_0; S4+S5+B+PP when all d_j > L_0
Watch out for:
  - S4 = strategy from explorer with singletons {P_1, d_3} when |d_1 - d_3| <= L_0 (NOT |d_3 - P_1|)
  - S5 (singletons {P_2, d_3}) = explorer 1's formula D = |d_3 - P_2|
  - B and PP together handle formula E = |2P_1 + d_1 - d_3| range; explicit construction needed

n4-algebraic-coverage: new
Target: c(4) = 16/31 with complete algebraic proof
Technique: Reduced-variable parameterization + interval coverage proof
Skeleton:
  1. Setup: alpha = P_1/L_0 - 1, beta = d_1/L_0 - 1, gamma = d_2/L_0 - 1, eta = d_3/L_0 - 1, all > 0
  2. Sum constraint: 4*alpha + 3*beta + 2*gamma + eta < 5 (from P_1+P_2+P_3+P_4 < 15L_0)
  3. Non-Case-A: if gamma < alpha + 1 (|d_2 - P_1| < L_0), use S6 (= S_A = S3-type); if |beta - eta| < 1 (|d_1 - d_3| < L_0), use S4
  4. Case A: gamma >= alpha + 1 AND eta >= beta + 1 simultaneously
  5. Case A sum bound: 6*alpha + 4*beta + 2 + (beta + 1) < 5 gives 6*alpha + 5*beta < 2, so alpha < 1/3
  6. S5 coverage: eta in [beta+1, alpha+beta+2] (d_3 in [d_1+L_0, P_2+2L_0])
  7. B coverage: eta in [2*alpha+beta, 2*alpha+beta+2] (d_3 in [2P_1+d_1-2L_0, 2P_1+d_1])
  8. PP coverage: eta > 2*alpha+beta+2 (d_3 > 2P_1+d_1)
  9. Gap S5-to-B: width = (2*alpha+beta) - (alpha+beta+2) = alpha - 2 < -5/3 < 0. EMPTY.
  10. PP bound: eta_max < 3 - 6*alpha - 3*beta, so PP's diff < 1 - 8*alpha - 4*beta < L_0. Done.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Case A definition forces alpha < 1/3 -- because gamma >= alpha+1 and eta >= beta+1 substituted into sum gives 6*alpha + 4*beta + gamma + eta > 6*alpha + 4*beta + (alpha+1) + (beta+1), sum < 5 forces 7*alpha + 5*beta < 3
  - Gap width formula: S5 ends at eta = alpha+beta+2, B starts at eta = 2*alpha+beta, width = alpha - 2 < 0
  - PP remainder < L_0: max eta = 3 - 6*alpha - 3*beta, so max(eta - 2*alpha - beta - 2) = 1 - 8*alpha - 4*beta < 1
Open gaps:
  - Explicit constructions for S5, B, PP (builder task)
  - Verify the interval endpoints are correct (beta+1 vs beta+1+1, etc.)
Cases to cover: Non-Case-A (S6 or S4), Case A (S5, B, PP partition)
Watch out for:
  - The reduced units have +1 offsets everywhere; easy to make sign errors
  - Need to verify that S5's end (alpha+beta+2) >= B's start (2*alpha+beta) is wrong (gap is negative)

n4-pigeonhole: copy-of geometric-direct
Target: c(4) = 16/31 with pigeonhole proof on five formulas
Technique: Five-formula pigeonhole (explorer 1's approach)
Note: This is an alternative to the n4-algebraic-coverage approach. Both target n=4; if one gets stuck, the other may succeed.
Skeleton:
  1. Setup: x = P_1/L_0, y = d_1/L_0, z = d_2/L_0, w = d_3/L_0, all > 1, sum 4x+3y+2z+w < 15
  2. Five formulas: A=|z-x|, B=|w-x|, C=|z+w-x|, D=|w-x-y|, E=|2x+y-w|
  3. Claim: min(A,B,C,D,E) <= 1 always (i.e., some formula <= L_0)
  4. Case II (x > 2): sum forces 3y+2z+w < 7, so z < 3/2, w < 2, z+w < 7/2. With x > 2, |z+w-x| < 3/2, and if z+w > x+1: sum > 5x+6 > 16 > 15. So C <= 1.
  5. Case I (x <= 2): A>1 => z > x+1; B>1 => w > x+1; D>1 => w > x+y+1; E>1 => w > 2x+y+1; sum > 8x+4y+3 > 15. Contradiction.
  6. For each formula <= L_0, use corresponding strategy S_A through S_E
Key lemmas (claim + the one-line mechanism that makes it true):
  - Case II forces C <= 1 -- because z+w bounded by sum and x > 2 forces |z+w-x| small
  - Case I chain forces sum contradiction -- because A,B,C,D,E all > 1 implies z,w large, sum exceeds bound
  - S_A through S_D explicit constructions (from explorer 1)
  - S_E = B+PP from explorer 2
Open gaps:
  - Complete the Case I/II case analysis rigorously
  - S_E explicit construction (or show B+PP cover it)
Cases to cover: x > 2 (Case II: C works), x <= 2 (Case I: some of A,B,D,E works)
Watch out for:
  - Case I has sub-cases based on y <= 2 or y > 2
  - The five formulas are not independent; some overlap (e.g., A+B = C when signs align)

minimax-saddle-point: advance (lower priority)
Target: c(n) = 2^n / (2^{n+1} - 1) for all n via saddle-point theory
Technique: LP duality / Sion's minimax theorem
Skeleton:
  1. Game is compact zero-sum; Sion gives max_LB min_XY = min_XY max_LB = c(n)
  2. Geometric config is THE saddle point; prove uniqueness
  3. Any deviation from geometric has strictly lower game value
  4. Upper bound: XY's optimal response to geometric works for ALL configs (need to verify)
Open gaps:
  - The key claim "XY's geometric-response works universally" is FALSE as stated
  - This approach provides intuition but not direct proof
Cases to cover: All n simultaneously
Watch out for:
  - Saddle-point uniqueness is hard to prove without explicit strategy analysis
  - This approach should be de-prioritized; geometric-direct is further along

induction-on-n: dead-end (do not build)
Status: Round 1 showed fatal flaw
