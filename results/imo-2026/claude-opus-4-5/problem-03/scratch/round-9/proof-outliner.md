## imo-2026-03

geometric-direct: advance
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: Singleton-Pair Formula + interval coverage for Case B; Halve-All and Halve+IH for Case A variants.
Skeleton:
  1. Lower bound: Geometric configuration achieves c(n) — by induction with Pairing Cancellation (PROVED for all n)
  2. Upper bound Case A (P_1 <= L_0): Halve-All Strategy — by Pairing Cancellation (PROVED for all n)
  3. Upper bound Case B large P_{n+1} (P_{n+1} >= c(n)): Halve + IH — by Pairing Cancellation + (n-1)-game IH (PROVED for all n >= 2, new this round)
  4. Upper bound Case B small pieces (n=1,2,3,4): Singleton-Pair strategies — by interval coverage (PROVED)
  5. Upper bound Case B for n=5: 11 explicit strategies — algebraic proof OPEN (new this round)
  6. Upper bound Case B for n>=6: Pattern generalizes — OPEN
Key lemmas (claim + the one-line mechanism that makes it true):
  - c(n-1)*(1-c(n)) = c(n)/2 — because 2^{n-1}/(2^n-1) * (2^n-1)/(2^{n+1}-1) = 2^{n-1}/(2^{n+1}-1) (NEW, proved this round)
  - Halve + IH Strategy — because halving P_{n+1} gives LB <= P_{n+1}/2 + c(n-1)*(1-P_{n+1}), which is decreasing and equals c(n) at P_{n+1}=c(n) (NEW, proved this round)
  - Gap-width alpha - 1 < 0 — because sum constraint + failure conditions force alpha < 1 in deepest Case A (verified for n=3,4,5)
Open gaps: n=5 algebraic proof (show sum constraint prevents all 11 strategy conditions from failing); n>=6 enumeration
Cases to cover: n=5 algebraic casework or sum-slack argument; n>=6 strategy enumeration
Watch out for: The "Case B Trivial" claim (P_{n+1} <= c(n) => XY uses 0 marks) was WRONG for n>=2 and has been removed.

---

## Changes made this round

**1. Fixed error (Case B Trivial removed):**
The claim "If P_{n+1} <= c(n), XY uses 0 marks and LB picks P_{n+1}" was WRONG for n >= 2. With 0 XY marks and n+1 pieces, LB picks ceil((n+1)/2) pieces, not just the largest. Example: n=2, P={1/3,1/3,1/3}, LB gets 2/3 > 4/7. This claim has been struck and replaced with a note explaining the error. The correct approach for large P_{n+1} is now Part 2.5.

**2. Added Part 2.5 (Halve + IH Strategy):**
New PROVED lemma for all n >= 2: When P_{n+1} >= c(n), XY halves P_{n+1} (1 mark) and applies the (n-1)-game upper bound (n-1 marks). By Pairing Cancellation:
  LB <= P_{n+1}/2 + c(n-1)*(1 - P_{n+1})
This is decreasing in P_{n+1}, and at P_{n+1} = c(n) it equals exactly c(n) via the identity c(n-1)*(1-c(n)) = c(n)/2. This closes the "large P_{n+1}" sub-case for all n.

**3. Added Part 2.6 (n=5 strategies):**
- 11 explicit 4-mark strategies identified (A1-A5, A-x, A-y, A-z, B3, B4, DB4).
- All use Singleton-Pair Formula with LB = 1/2 + |s_2-s_1|/2.
- Computationally verified: 0 failures in 500k configs; max min-diff = 0.9575 < 1.
- Case A constraint: alpha < 1 (gap width alpha-1 < 0, so intervals overlap).
- OPEN GAP: Algebraic proof that the 11 strategies cover all cases.

**4. Updated Current best and Part 4 sections:**
- Removed references to "Case B trivial (0 marks)".
- Added "Case B large P_{n+1}" as a proved result for all n >= 2.
- n=5 now shows "IDENTIFIED 11 strategies, computationally verified, algebraic proof OPEN".

**5. Added two new promotable lemmas:**
- Halve + IH Strategy
- c(n-1)*(1-c(n)) = c(n)/2 Identity

---

## Build set recommendation

build set: geometric-direct

The approach is ready for the builder to:
1. Verify the new Part 2.5 proof (Halve + IH Strategy).
2. Attempt the n=5 algebraic casework to close the 11-strategy coverage gap.

No new approaches opened this round — the geometric-direct approach remains the clear leader with complete proofs for n=1,2,3,4 and strong progress on n=5.
