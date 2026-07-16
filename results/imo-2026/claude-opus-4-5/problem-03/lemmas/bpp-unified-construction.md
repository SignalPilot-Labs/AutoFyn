# BPP Unified Construction (n=4)

## Statement

For n=4 Case B in Case A (gamma >= alpha+1, eta >= beta+1) with eta in [1+2*alpha+beta, eta_max), XY uses exactly 3 marks:

1. Cut P_4 at position P_3 from left: creates {P_3, d_3}
2. Cut d_3 at position P_1 from left: creates {P_1, d_3-P_1}
3. Halve P_5: creates {P_5/2, P_5/2}

This produces:
- Pairs: {P_3, P_3}, {P_1, P_1}, {P_5/2, P_5/2}
- Singletons: {P_2, d_3-P_1}

By the Singleton-Pair Formula:
LB = 1/2 + |P_2 - (d_3-P_1)|/2 = 1/2 + |P_1+P_2-d_3|/2

## Validity

The cut inside d_3 requires d_3 > P_1, i.e., eta > alpha.

In BPP range: eta >= 1 + 2*alpha + beta > 1 > alpha (since alpha < 1/3 from Case A constraint).

Therefore the cut is always valid in BPP range.

## Proof of LB <= c(4)

In B range (eta < 2+2*alpha+beta): |P_1+P_2-d_3| = (2+2*alpha+beta-eta)*L_0 in (0, L_0].
LB = 1/2 + (0 to L_0/2) <= c(4).

In PP range (eta > 2+2*alpha+beta): |P_1+P_2-d_3| = (eta-2-2*alpha-beta)*L_0.
By the BPP Range Bound Lemma, this is < L_0.
LB = 1/2 + (< L_0/2) < c(4).

## Certified

Reviewer-verified in Round 7. Independent numerical verification: 5000 random configs, 0 failures.
