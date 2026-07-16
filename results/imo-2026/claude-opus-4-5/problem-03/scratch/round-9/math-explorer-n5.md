# n=5 Case B Explicit Strategies — Lens Report

## Setup

**n=5:** D=63, L0=1/63, c(5)=32/63. Pieces P1<=P2<=P3<=P4<=P5<=P6 (from LB's 5 marks), sum=1.

**Case B:** P1 > L0, P6 > c(5).

**Reduced units** (each minus 1, in multiples of L0):
- alpha = P1/L0 - 1  →  P1 = (1+alpha)*L0
- beta  = d1/L0 - 1  →  d1 = (1+beta)*L0   [d1 = P2-P1]
- gamma = d2/L0 - 1  →  d2 = (1+gamma)*L0  [d2 = P3-P2]
- delta = d3/L0 - 1  →  d3 = (1+delta)*L0  [d3 = P4-P3]
- epsilon=d4/L0 - 1  →  d4 = (1+epsilon)*L0 [d4 = P5-P4]

**Sum constraint:** P1+P2+P3+P4+P5 < 31*L0, which gives:

    5*alpha + 4*beta + 3*gamma + 2*delta + epsilon < 16

(P2 = (2+alpha+beta)*L0, P3 = (3+alpha+beta+gamma)*L0)

---

## Strategies: 11 total, each using 4 XY marks → 10 pieces = 4 pairs + 2 singletons

**Singleton-Pair Formula:** LB = 1/2 + |s2-s1|/2. Works when |s2-s1| <= L0.

Each row: Strategy | Condition | Singletons {s1,s2} | Construction (4 marks)

| Strategy | Works when | Singletons | XY's 4 marks |
|----------|-----------|-----------|--------------|
| A1 | |gamma-alpha| <= 1 | {P1, d2} | cut P3 at P2; halve P4, P5, P6 |
| A2 | |delta-beta| <= 1 | {d1, d3} | cut P2 at P1; cut P4 at P3; halve P5, P6 |
| A3 | |delta-(1+alpha+beta)| <= 1 | {P2, d3} | cut P4 at P3; 2-mark split P6 with P1 in center; halve P5 |
| A4 | |epsilon-gamma| <= 1 | {d2, d4} | halve P1; cut P3 at P2; cut P5 at P4; halve P6 |
| A5 | |epsilon-(2+alpha+beta+gamma)| <= 1 | {P3, d4} | cut P5 at P4; 2-mark split P6 with P2 in center; halve P1 |
| A-x | |epsilon-beta| <= 1 | {d1, d4} | cut P2 at P1; halve P3; cut P5 at P4; halve P6 |
| A-y | |alpha-epsilon| <= 1 | {P1, d4} | cut P5 at P4; cut P3 at P2 (+ halve d2 = 2 marks); halve P6 |
| A-z | |alpha-delta| <= 1 | {P1, d3} | cut P4 at P3; halve P2; halve P5; halve P6 |
| B3  | |2+2alpha+beta-delta| <= 1 | {P2, d3-P1} | cut P4 at P3; cut d3-piece at P1; halve P5; halve P6 |
| B4  | |2+2alpha+beta-epsilon| <= 1 | {P2, d4-P1} | cut P5 at P4; cut d4-piece at P1; halve P6; halve P2 |
| DB4 | |4+2alpha+2beta+gamma-epsilon| <= 1 | {P3, d4-P2} | cut P5 at P4; cut d4-piece at P2; halve P6; halve P1 |

**Key constructions detail:**
- A3: "2-mark split of P6 with P1 in center" means XY places 2 marks at distance (P6-P1)/2 from each end of P6, creating sub-pieces {r, P1, r} where r=(P6-P1)/2.
- A5: analogous but with P2 in center, r2=(P6-P2)/2.
- A-y: 2 marks on P3 interval: first at distance P2 from left (creating P2-subpiece and d2-subpiece), second at midpoint of d2-subpiece. Creates {P2, d2/2, d2/2} from P3.
- B3/B4/DB4: "cut d3-piece at P1" means after cutting P4 to isolate d3, XY places another mark within that d3-sized sub-interval.

---

## Coverage (numerical evidence)

**500,000 random Case B configs tested: 0 failures** (LB <= c(5) for every config).

**Maximum of min-singleton-difference:** 0.9575 < 1 (achieved at alpha≈1.5, beta≈1.1, gamma≈0.3, delta≈0.17, epsilon≈2.5). Since the maximum is strictly < 1, **at least one strategy always applies**.

This is strong numerical evidence that the 11 strategies cover all n=5 Case B configurations.

---

## Case A constraint for n=5

"Case A" (all differences doubly large): gamma >= alpha+1 AND delta >= beta+1 AND epsilon >= gamma+1.

Substituting into sum constraint:
  5alpha + 4beta + 3(alpha+1) + 2(beta+1) + (gamma+1) <= 5alpha+4beta+3alpha+3+2beta+2+(alpha+1+1) < 16
  →  9*alpha + 6*beta < 9   →  alpha < 1  (compare with n=4's alpha < 1/3)

The Case A constraint is weaker than n=4: alpha < 1 rather than alpha < 1/3. This is fine because the BPP-type argument needs only alpha < 1 (gap = alpha-1 < 0).

---

## Key structural observations

1. **11 strategies vs 4 for n=4**: n=5 needs substantially more coverage strategies due to 5 parameters instead of 4.

2. **Gap pattern**: The strategies A1-A-z cover "nearby comparisons" between di's and Pj's. B3, B4, DB4 are the "nested BPP" strategies for large d3 or d4.

3. **Why BPP-d3 is needed**: Large d3 (delta >> 1+2alpha+beta) isn't covered by A2 or A3; B3 handles it via singletons {P2, d3-P1}.

4. **Why new strategies A-x, A-y, A-z arise**: These compare "across" the two halves of the difference sequence (d1 vs d4, P1 vs d4, P1 vs d3). These were not needed in n=4 because there was only ONE "big" difference (d3 = eta); in n=5 there are TWO (d3, d4) and they can be large independently.

5. **Singleton-pair formula always applies**: All 11 strategies use exactly 4 XY marks, creating 4 pairs + 2 singletons. LB = 1/2 + |diff|/2.

---

## Gap in algebraic proof

The numerical evidence strongly suggests coverage, but the FORMAL proof that "none of the 11 conditions can all fail simultaneously (given sum constraint)" needs:

Either:
(a) An algebraic case analysis: show for each combination of failures that the sum constraint gives a contradiction. With 11 conditions and 5 parameters, this is a 2^11 case analysis in principle (but most are impossible by sum constraint). Likely a tree structure works.

(b) A sum-slack argument: Show that if |s2-s1| > 1 for all 11 strategies, then 5alpha+4beta+3gamma+2delta+epsilon >= 16. This mirrors the n=4 BPP Range Bound argument.

The numerical maximum of 0.9575 (not 1) suggests there is SLACK in the sum constraint — the coverage doesn't "just barely" work, and an algebraic proof should close.

---

## Summary for outliner

- **Claim**: 11 explicit 4-mark XY strategies cover all n=5 Case B configurations.
- **All strategies use Singleton-Pair Formula**: LB = 1/2 + |s2-s1|/2 with the explicitly constructed pairs/singletons.
- **Computational verification**: 0 failures in 500k random configs; max min-diff = 0.9575 < 1.
- **Sum constraint**: 5alpha + 4beta + 3gamma + 2delta + epsilon < 16 (key algebraic handle).
- **Remaining gap**: Formal algebraic proof that the 11 strategies cover all cases (not just numerical).
- **Pattern for n>=6**: Similar structure but with even more strategies needed (n-1 gaps create O(n^2) pairwise comparisons to check).
