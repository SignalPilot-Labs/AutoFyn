# BPP Range Bound (n=4)

## Statement

In the BPP range eta in [1+2*alpha+beta, eta_max) for n=4 Case A:

The singleton difference |2+2*alpha+beta-eta| (in reduced units) satisfies:
- In B range (eta < 2+2*alpha+beta): difference in (0, 1]
- In PP range (eta > 2+2*alpha+beta): difference < 1

Therefore LB <= c(4) in all BPP configurations.

## Proof

**B range:** eta in [1+2*alpha+beta, 2+2*alpha+beta).
Difference = 2+2*alpha+beta-eta in (0, 1]. Immediate.

**PP range:** eta in (2+2*alpha+beta, eta_max).
Difference = eta - 2 - 2*alpha - beta.

From sum constraint: 4*alpha + 3*beta + 2*gamma + eta < 5.
In Case A: gamma >= alpha + 1.
Therefore: eta < 5 - 4*alpha - 3*beta - 2*(alpha+1) = 3 - 6*alpha - 4*beta = eta_max.

Maximum difference = eta_max - (2 + 2*alpha + beta)
                   = (3 - 6*alpha - 4*beta) - (2 + 2*alpha + beta)
                   = 1 - 8*alpha - 4*beta
                   < 1 (since alpha, beta > 0)

## Corollary

LB = 1/2 + |2+2*alpha+beta-eta|*L_0/2 <= 1/2 + L_0/2 = c(4).

Equality only at eta = 1+2*alpha+beta (BPP lower bound), where LB = c(4) exactly.

## Certified

Reviewer-verified in Round 7. Note: Original approach file had typo "5*beta" corrected to "4*beta".
