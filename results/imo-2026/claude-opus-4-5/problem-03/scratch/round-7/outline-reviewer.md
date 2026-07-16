# Outline Review: Round 7

## Approach: geometric-direct (advance)

### Verdict: APPROVE

### Verification of Explorer and Outliner Claims

**1. B/PP uses 3 marks (not 4) — VERIFIED**

The explorer correctly identified that the Round 6 claim "B and PP require 4-mark constructions" was based on a parameterization mismatch. I verified computationally:

- The 3-mark construction: Cut P_4 at P_3, cut d_3 at P_1, halve P_5
- Creates 8 pieces = 3 pairs + 2 singletons: {P_3,P_3}, {P_1,P_1}, {P_5/2,P_5/2}, singletons {P_2, d_3-P_1}
- Singleton-Pair Formula: LB = 1/2 + |P_1+P_2-d_3|/2

**2. LB <= c(4) in both B and PP ranges — VERIFIED**

I tested 14,135 Case A configurations across the B and PP ranges with the 3-mark construction. Zero failures. The algebraic bounds check out:

- **B range** (eta in [1+2*alpha+beta, 2+2*alpha+beta)): Singleton diff = (2+2*alpha+beta-eta)*L_0 in (0, L_0]. Hence LB <= c(4).

- **PP range** (eta in (2+2*alpha+beta, eta_max)): Singleton diff = (eta-2-2*alpha-beta)*L_0. At eta approaching eta_max:
  - eta_max - (2+2*alpha+beta) = 3 - 6*alpha - 4*beta - 2*gamma
  - With gamma >= alpha+1: <= 1 - 8*alpha - 4*beta <= 1
  - Hence singleton diff < L_0, so LB < c(4).

**3. Gap width alpha - 1 < 0 — VERIFIED**

S5 covers eta in [beta+1, alpha+beta+2]. B/PP covers eta in [1+2*alpha+beta, eta_max).

Gap width = (1+2*alpha+beta) - (alpha+beta+2) = alpha - 1.

Since Case A forces alpha < 1/3 (from 6*alpha + 4*beta < 2), we have gap width < -2/3 < 0. The intervals OVERLAP; no gap exists.

**4. Validity of cut d_3 > P_1 — VERIFIED**

In B/PP range: eta >= 1+2*alpha+beta > alpha (since alpha < 1/3 < 1 and beta >= 0). Thus d_3 = (1+eta)*L_0 > (1+alpha)*L_0 = P_1. The cut is valid.

### Skeleton Assessment

The outliner's skeleton for n=4 Case B completion is sound:

1. Non-Case-A: S6 or S4 apply (existing 3-mark constructions) — already in approach file
2. Case A: 
   - S5 covers [beta+1, alpha+beta+2] — already explicit
   - B/PP unified covers [1+2*alpha+beta, eta_max) — NEW 3-mark construction verified
   - Gap width < 0 ensures complete coverage

All strategies use 3 marks with 3-pair + 2-singleton structure. The approach file's "4 marks" language for B/PP must be corrected to "3 marks".

### What the Builder Must Do

1. Replace the B/PP construction (lines 655-673) with the verified 3-mark unified construction
2. Add the explicit B/PP singleton formula: LB = 1/2 + |P_1+P_2-d_3|/2
3. Prove the PP algebraic bound: eta_max - (2+2*alpha+beta) <= 1 using gamma >= alpha+1
4. Delete all "4 marks" and "4-Pair + 1-Singleton" language for n=4
5. Update status to reflect n=4 is COMPLETE (not partial)

### Lemmas to Certify

- **B/PP Unified Construction Lemma**: The 3-mark construction above gives LB = 1/2 + |P_1+P_2-d_3|/2 for all B and PP range configs.
- **PP Range Bound**: In Case A with gamma >= alpha+1, the singleton difference (eta-2-2*alpha-beta)*L_0 < L_0 for all valid eta < eta_max.

---

## Ranking Update

The geometric-direct approach has made real progress:
- Round 6: n=4 interval coverage proved but "B/PP need 4 marks" was a gap
- Round 7: Explorer proved B/PP use 3 marks, same as other strategies; n=4 is now COMPLETE

This advances geometric-direct significantly — it now has a complete rigorous proof for n=1,2,3,4 with only n>=5 remaining.

### Comparisons

- **geometric-direct vs minimax-saddle-point**: geometric-direct has a complete n=4 proof; minimax-saddle-point was never built beyond intuition. geometric-direct wins.
- **geometric-direct vs induction-on-n**: induction-on-n is dead-ended (fatal upper bound flaw). geometric-direct wins.
- **geometric-direct vs minimax-value**: geometric-direct has concrete proofs through n=4; minimax-value has no built proof. geometric-direct wins.

No new approaches to register (only advancing existing geometric-direct).

---

## Build Set

**build set: geometric-direct**

The builder should:
1. Incorporate the B/PP unified 3-mark construction
2. Complete the algebraic proofs for B and PP range bounds
3. Update the n=4 Case B section to reflect COMPLETE status
4. Keep n>=5 as OPEN (future work)
