## imo-2026-03

geometric-direct: advance
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Direct proof — geometric lower bound via dominance + upper bound via Singleton-Pair Formula with case-covering XY strategies
Skeleton:
  1. Lower bound: LB uses geometric config {L_0, ..., L_n}. By Geometric Dominance, L_n is uniquely largest. XY's optimal split of L_n recreates the geometric pieces with pairs; by Pairing Cancellation, LB gets exactly c(n). — PROVED for all n
  2. Upper bound Case A (P_1 <= L_0): XY halves P_2, ..., P_{n+1} (n marks). By Pairing Cancellation, LB = 1/2 + P_1/2 <= c(n). — PROVED for all n
  3. Upper bound Case B trivial (P_{n+1} <= c(n)): XY uses 0 marks, LB picks P_{n+1} <= c(n). — PROVED for all n
  4. Upper bound Case B n=1: P_1 > 1/3 forces P_2 < 2/3 = c(1). — PROVED
  5. Upper bound Case B n=2: Sum constraint forces d_1 < L_0; halving strategy gives LB < c(2). — PROVED
  6. Upper bound Case B n=3: Three strategies S1/S2/S3 with Singleton-Pair Formula cover all configs. — PROVED
  7. Upper bound Case B n=4: NOW FULLY PROVED with five strategies:
     - Non-Case-A (gamma < alpha+1 or eta < beta+1): S6 or S4 apply — 3-mark explicit constructions
     - Case A (gamma >= alpha+1 and eta >= beta+1): Case A constraint forces alpha < 1/3
       - S5 covers eta in [beta+1, alpha+beta+2] — 3-mark explicit construction
       - B/PP UNIFIED covers eta in [1+2alpha+beta, eta_max) — 3-mark explicit construction (NOT 4 marks!)
       - Gap width = alpha - 1 < -2/3 < 0, so S5 and B/PP overlap with no gap
     - All strategies use 3 marks with 3-pair + 2-singleton structure, giving LB = 1/2 + (singleton diff)/2 <= c(4)
  8. Upper bound Case B n >= 5: OPEN. Computationally verified (0/500k failures), but algebraic proof needs generalization of interval coverage.
Key lemmas (claim + mechanism):
  - B/PP Unified Construction (NEW, Round 7): XY cuts P_4 at P_3 from left (pair {P_3,P_3}), cuts d_3 at P_1 from left (pair {P_1,P_1}), halves P_5 (pair {P_5/2,P_5/2}). Singletons = {P_2, d_3-P_1}. LB = 1/2 + |P_1+P_2-d_3|/2 — because Singleton-Pair Formula with absolute value handles both B (d_3 < P_1+P_2) and PP (d_3 > P_1+P_2) automatically.
  - B range bound: In B range eta in [1+2alpha+beta, 2+2alpha+beta), singleton diff = (2+2alpha+beta-eta)*L_0 in (0, L_0], so LB <= c(4) — because the interval definition directly bounds the difference.
  - PP range bound: In PP range eta in (2+2alpha+beta, eta_max), singleton diff < L_0 — because eta_max - (2+2alpha+beta) = 3-6alpha-4beta-2gamma <= 1-8alpha-4beta <= 1 (using gamma >= alpha+1 and alpha,beta >= 0).
  - Validity of cut inside d_3: d_3 > P_1 always in B/PP range — because eta >= 1+2alpha+beta > alpha (since alpha < 1/3 < 1).
Open gaps: 
  - n >= 5 upper bound Case B (computationally verified, algebraic proof open)
Cases to cover: n=1,2,3,4 now COMPLETE; n >= 5 open
Watch out for:
  - The old approach file claims B/PP need 4 marks and "4-Pair + 1-Singleton" structure — THIS IS WRONG, must be corrected to 3 marks and "3-Pair + 2-Singleton"
  - The reviewer's parameterization mismatch led to the false claim that 3 marks give LB > c(4) for eta=2.18 — in the correct parameterization, 3 marks give LB = 0.500 << c(4)

---

Notes for the builder:

**n=4 is NOW COMPLETE.** The gap from Round 6 ("B and PP require 4-mark constructions") was a false alarm caused by a parameterization mismatch in the verification code. The 4-mark explorer proved:

1. B and PP use the SAME 3-mark construction as S5 (just with different singleton pairs):
   - Cut P_4 at P_3 from left -> pair {P_3, P_3}
   - Cut d_3 at P_1 from left -> pair {P_1, P_1}
   - Halve P_5 -> pair {P_5/2, P_5/2}
   - Singletons: {P_2, d_3-P_1}
   - LB = 1/2 + |P_1+P_2-d_3|/2

2. Merge B and PP into one "BPP" strategy — the absolute value handles the sign flip at the B/PP boundary (d_3 = P_1+P_2).

3. Delete all references to "4 marks" and "4-Pair + 1-Singleton" for n=4 — these were incorrect.

4. The proof for n=4 Case B is now:
   - Non-Case-A: S6 or S4 (explicit 3-mark constructions)
   - Case A: S5 union BPP cover all eta values with gap width alpha-1 < 0
   - All strategies are 3-mark with 3-pair + 2-singleton structure

**Structure for n >= 5 (OPEN):**
The general-n explorer found:
- Two strategy families suffice: D_ij (|d_i - d_j| <= L_0) and S_{j,k} (|d_j - P_k| <= L_0)
- Pigeon-hole argument works for n <= 9 (using n(n+1)(4n-1)/6 > 2^n - 1)
- For n >= 10, need the "interleaving" argument: when all |d_i - d_j| > L_0, some |d_j - P_k| <= L_0 automatically (verified but unproved)
- True induction on n may work via the "Case A cascade" structure
